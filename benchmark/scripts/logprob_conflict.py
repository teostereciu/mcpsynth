#!/usr/bin/env python3
"""
logprob_conflict.py — Memory vs. context conflict probe via token log-probabilities.

For each mutated parameter in a given dataset, this script:
  1. Builds a single-turn prompt containing the relevant (mutated) doc snippet
  2. Asks the model to generate ONE Python function for that API endpoint
  3. Collects logprobs (top 20) from the response
  4. Finds the token positions where mutated parameter names are generated
  5. Extracts P(mutated) and P(original) at those positions as a conflict signal

Usage:
    uv run python benchmark/scripts/logprob_conflict.py --dataset stripe
    uv run python benchmark/scripts/logprob_conflict.py --dataset zulip
    uv run python benchmark/scripts/logprob_conflict.py --dataset stripe --model azure-chat-completions-gpt-4o-mini-2024-07-18
    uv run python benchmark/scripts/logprob_conflict.py --dataset stripe --runs 3

Environment:
    CHOMSKY_ENDPOINT   Override the default Chomsky gateway endpoint
"""

import argparse
import json
import math
import os
import re
import sys
from pathlib import Path
from textwrap import indent

ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(ROOT))

from langchain_core.messages import HumanMessage, SystemMessage
from pychomsky.chchat import AzureOpenAIChatWrapper

# ---------------------------------------------------------------------------
# Dataset configs: which doc file to use, and which endpoint section to extract
# ---------------------------------------------------------------------------

DATASET_CONFIGS = {
    "stripe": {
        "doc": "benchmark/datasets/stripe/docs_mutated/payment_intents.md",
        "endpoint_header": "# Create a PaymentIntent",
        "endpoint_desc": "POST /v1/payment_intents",
        "mutations_file": "benchmark/datasets/stripe/mutations.json",
    },
    "zulip": {
        "doc": "benchmark/datasets/zulip/docs_mutated/api_get-messages.md",
        "endpoint_header": "# Get messages\n",   # matches the real content header at line 198
        "endpoint_desc": "GET /api/v1/messages",
        "mutations_file": "benchmark/datasets/zulip/mutations.json",
    },
    "ebay_sell": {
        "doc": "benchmark/datasets/ebay_sell/docs_mutated/api_account_get-fulfillment-policies.md",
        "endpoint_header": "# getFulfillmentPolicies",
        "endpoint_desc": "GET /fulfillment_policy",
        "mutations_file": "benchmark/datasets/ebay_sell/mutations.json",
    },
    "jira": {
        "doc": "benchmark/datasets/jira/docs_mutated/api_issue-search.md",
        "endpoint_header": "## Search for issues using JQL enhanced search (GET)",
        "endpoint_desc": "GET /rest/api/3/search",
        "mutations_file": "benchmark/datasets/jira/mutations.json",
    },
    "alphavantage": {
        "doc": "benchmark/datasets/alphavantage/docs_mutated/api_time_series_data.md",
        "endpoint_header": "#### TIME_SERIES_DAILY\n",
        "endpoint_desc": "GET /query?function=TIME_SERIES_DAILY",
        "mutations_file": "benchmark/datasets/alphavantage/mutations.json",
    },
}

# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are an expert Python developer building MCP (Model Context Protocol) tool servers.
Given an API documentation snippet, write a single Python function that wraps the described endpoint.

Rules:
- Use @mcp.tool() decorator
- Function parameters must exactly match the parameter names documented (spelling matters)
- Use requests to make the HTTP call
- Pass parameters as a dict called `params` for query params or `data` for form-encoded bodies
- Return the JSON response as a dict
- Keep it concise — no docstring needed, just the function
"""

HUMAN_TEMPLATE = """\
Here is the API documentation for one endpoint:

---
{doc_snippet}
---

Write a single Python @mcp.tool() function that implements this endpoint.
Parameter names in your function signature MUST match the documentation exactly.
"""


def extract_doc_section(doc_path: Path, section_header: str) -> str:
    """Extract the section starting at section_header until the next same-level header.

    Uses the *last* occurrence of section_header to skip nav sidebars that
    repeat the page title near the top of scraped docs.
    Caps output at 6000 chars to stay within reasonable prompt size.
    """
    text = doc_path.read_text()
    # Use rfind to get the last (real content) occurrence, not a nav sidebar copy
    start = text.rfind(section_header)
    if start == -1:
        return text[:6000]
    # Determine header level (count leading #)
    level = len(section_header) - len(section_header.lstrip("#"))
    header_marker = "\n" + "#" * level + " "
    next_header = text.find(header_marker, start + len(section_header))
    end = next_header if next_header != -1 else len(text)
    return text[start:end].strip()[:10000]


# ---------------------------------------------------------------------------
# Logprob extraction
# ---------------------------------------------------------------------------

def _token_matches(token: str, name: str) -> bool:
    """True if token is a prefix of name, name is a prefix of token, or exact match.
    Handles cases where a name tokenises differently than expected."""
    return token == name or name.startswith(token) or token.startswith(name)


def find_token_conflicts(
    logprob_content: list[dict],
    mutations: list[dict],
    top_k: int = 20,
) -> list[dict]:
    """
    For each mutation pair (original, mutated), find the first position in the
    token stream where *either* name newly appears, then rank the *other* one
    in top_logprobs.

    This covers both outcomes:
      - Model used original (memory won)  → rank mutated in alternatives
      - Model used mutated (doc won)       → rank original in alternatives

    conflict_score = P(loser) / (P(winner) + P(loser))
      0.0 = loser not in top-k at all (winner dominated completely)
      0.5 = both equally probable (genuine tug-of-war)
    """
    tokens = logprob_content
    cumulative = []
    running = ""
    for t in tokens:
        running += t["token"]
        cumulative.append(running)

    results = []

    for mutation in mutations:
        orig = mutation["original"]
        mut = mutation["mutated"]

        for i, t in enumerate(tokens):
            text_before = cumulative[i - 1] if i > 0 else ""
            text_at = cumulative[i]

            orig_appears = orig not in text_before and orig in text_at
            mut_appears  = mut  not in text_before and mut  in text_at

            if not orig_appears and not mut_appears:
                continue

            # Determine which name won and which is the rival
            if orig_appears:
                winner, loser = orig, mut
                outcome = "memory"      # model used memorized original
            else:
                winner, loser = mut, orig
                outcome = "doc"         # model followed the doc

            chosen_token   = t["token"]
            chosen_logprob = t["logprob"]
            chosen_prob    = math.exp(chosen_logprob)
            top = t.get("top_logprobs", [])

            # Find the loser in top_logprobs
            loser_rank     = None
            loser_logprob  = None
            loser_tok_match = None
            for rank, alt in enumerate(top):
                if _token_matches(alt["token"], loser):
                    loser_rank     = rank
                    loser_logprob  = alt["logprob"]
                    loser_tok_match = alt["token"]
                    break

            loser_prob = math.exp(loser_logprob) if loser_logprob is not None else 0.0
            total = chosen_prob + loser_prob
            conflict_score = loser_prob / total if total > 0 else 0.0

            results.append({
                "mutation": {"original": orig, "mutated": mut},
                "outcome": outcome,
                "token_position": i,
                "winner": winner,
                "loser": loser,
                "chosen_token": chosen_token,
                "chosen_logprob": round(chosen_logprob, 4),
                "chosen_prob": round(chosen_prob, 6),
                "loser_token_match": loser_tok_match,
                "loser_rank": loser_rank,        # None = not in top-k
                "loser_logprob": round(loser_logprob, 4) if loser_logprob is not None else None,
                "loser_prob": round(loser_prob, 6),
                "conflict_score": round(conflict_score, 4),
                "top_alternatives": [
                    {
                        "rank": r,
                        "token": a["token"],
                        "logprob": round(a["logprob"], 4),
                        "prob": round(math.exp(a["logprob"]), 6),
                    }
                    for r, a in enumerate(top)
                ],
            })
            break  # one match per mutation per run

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run(dataset: str, model: str, runs: int, endpoint: str) -> None:
    cfg = DATASET_CONFIGS[dataset]
    doc_path = ROOT / cfg["doc"]
    mutations_path = ROOT / cfg["mutations_file"]

    mutations = json.loads(mutations_path.read_text())["mutations"]
    doc_snippet = extract_doc_section(doc_path, cfg["endpoint_header"])

    print(f"\n=== Logprob Conflict Probe ===")
    print(f"Dataset : {dataset}")
    print(f"Endpoint: {cfg['endpoint_desc']}")
    print(f"Model   : {model}")
    print(f"Runs    : {runs}")
    print(f"Mutations tracked ({len(mutations)}): {[m['original'] + '→' + m['mutated'] for m in mutations]}")
    print(f"\nDoc snippet ({len(doc_snippet)} chars, first 200): {doc_snippet[:200]!r}...\n")

    # gpt-5 series requires max_completion_tokens and caps top_logprobs at 5
    uses_completion_tokens = any(x in model for x in ("gpt-5", "o1", "o3", "o4"))
    top_logprobs_limit = 5 if uses_completion_tokens else 20
    llm_kwargs = dict(
        model_name=model,
        temperature=1.0,       # some variability across runs
        logprobs=True,
        top_logprobs=top_logprobs_limit,
    )
    if uses_completion_tokens:
        llm_kwargs["max_completion_tokens"] = 1200
    else:
        llm_kwargs["max_tokens"] = 1200
    if endpoint:
        llm_kwargs["chgw_endpoint"] = endpoint
    llm = AzureOpenAIChatWrapper(**llm_kwargs)

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=HUMAN_TEMPLATE.format(doc_snippet=doc_snippet)),
    ]

    all_run_results = []

    for run_idx in range(runs):
        print(f"--- Run {run_idx + 1}/{runs} ---")
        response = llm.invoke(messages)
        output_text = response.content
        logprob_data = response.response_metadata.get("logprobs", {})
        token_stream = logprob_data.get("content", [])

        print(f"Output ({len(token_stream)} tokens):\n{indent(output_text, '  ')}\n")

        conflicts = find_token_conflicts(token_stream, mutations, top_k=20)

        if not conflicts:
            print("  [neither original nor mutated parameter tokens found in output]\n")
        else:
            for c in conflicts:
                orig = c["mutation"]["original"]
                mut  = c["mutation"]["mutated"]
                cs   = c["conflict_score"]
                rank = c["loser_rank"]
                bar  = "█" * int(cs * 20) + "░" * (20 - int(cs * 20))
                outcome_label = "MEMORY WON" if c["outcome"] == "memory" else "DOC WON   "
                pull_label = (
                    "STRONG PULL" if cs > 0.3
                    else "MILD PULL"   if cs > 0.1
                    else "no pull"
                )
                rank_str = f"rank {rank}" if rank is not None else "not in top-k"
                print(f"  [{outcome_label}]  {orig!r:20s} ↔  {mut!r}")
                print(f"    pos={c['token_position']:3d}  winner={c['winner']!r}  loser={rank_str}  "
                      f"P(winner)={c['chosen_prob']:.6f}  P(loser)={c['loser_prob']:.6f}")
                print(f"    conflict_score={cs:.4f}  [{bar}]  {pull_label}")
                print(f"    top-k at this position:")
                for alt in c["top_alternatives"]:
                    marker = ""
                    if alt["token"] == c["chosen_token"]:
                        marker = f"  <-- {'MEMORY' if c['outcome'] == 'memory' else 'DOC'} (chosen)"
                    elif c["loser_token_match"] and alt["token"] == c["loser_token_match"]:
                        marker = f"  <-- {'DOC' if c['outcome'] == 'memory' else 'MEMORY'} (loser)"
                    print(f"      [{alt['rank']}] {alt['token']!r:20s}  logprob={alt['logprob']:7.3f}  prob={alt['prob']:.6f}{marker}")
                print()

        all_run_results.append({
            "run": run_idx + 1,
            "output": output_text,
            "conflicts": conflicts,
            "token_count": len(token_stream),
        })

    # Summary across runs
    print("=== Summary across runs ===")
    by_mutation: dict[str, list[dict]] = {}
    for run_result in all_run_results:
        for c in run_result["conflicts"]:
            key = f"{c['mutation']['original']}→{c['mutation']['mutated']}"
            by_mutation.setdefault(key, []).append(c)

    if not by_mutation:
        print("Neither original nor mutated parameter tokens found in any run output.")
    else:
        print(f"{'Mutation':<40} {'Found':>5}  {'Outcome':>12}  {'Mean conflict':>14}  {'Loser rank':>10}")
        print("-" * 90)
        for key, entries in sorted(by_mutation.items(), key=lambda x: -sum(e["conflict_score"] for e in x[1]) / len(x[1])):
            scores   = [e["conflict_score"] for e in entries]
            outcomes = [e["outcome"] for e in entries]
            ranks    = [e["loser_rank"] for e in entries if e["loser_rank"] is not None]
            mean_cs  = sum(scores) / len(scores)
            mem_wins = outcomes.count("memory")
            doc_wins = outcomes.count("doc")
            outcome_str = f"{mem_wins}mem/{doc_wins}doc"
            rank_str = f"{sum(ranks)/len(ranks):.1f}" if ranks else "n/a"
            bar = "█" * int(mean_cs * 20) + "░" * (20 - int(mean_cs * 20))
            print(f"  {key:<38} {len(entries):>5}  {outcome_str:>12}  {mean_cs:>13.4f}  {rank_str:>10}  [{bar}]")

    # Save raw results
    out_path = ROOT / f"benchmark/output/logprob_conflict_{dataset}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps({
        "dataset": dataset,
        "model": model,
        "endpoint": cfg["endpoint_desc"],
        "mutations": mutations,
        "runs": all_run_results,
    }, indent=2))
    print(f"\nFull results saved to {out_path.relative_to(ROOT)}")


def main():
    parser = argparse.ArgumentParser(description="Memory vs. context conflict probe via logprobs")
    parser.add_argument("--dataset", default="stripe", choices=list(DATASET_CONFIGS.keys()))
    parser.add_argument("--model", default="azure-chat-completions-gpt-4o-mini-2024-07-18")
    parser.add_argument("--runs", type=int, default=3, help="Number of independent generations")
    parser.add_argument("--endpoint", default=None, help="Chomsky gateway endpoint URL (overrides env)")
    args = parser.parse_args()

    endpoint = args.endpoint or os.environ.get("CHOMSKY_ENDPOINT") or None

    run(args.dataset, args.model, args.runs, endpoint)


if __name__ == "__main__":
    main()
