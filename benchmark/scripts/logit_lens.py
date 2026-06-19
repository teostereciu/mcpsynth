#!/usr/bin/env python3
"""
logit_lens.py — Layer-by-layer probability probe for memory vs. context conflict.

For each mutation pair (original, mutated), runs a single forward pass on the
synthesis prompt with output_hidden_states=True, then applies the logit lens:
projects each layer's residual stream through the unembedding matrix to get
P(original) and P(mutated) at every layer depth.

This reconstructs the full resolution curve showing at which layer the model
commits to one name over the other.

Usage:
    uv run python benchmark/scripts/logit_lens.py --dataset stripe
    uv run python benchmark/scripts/logit_lens.py --dataset zulip
    uv run python benchmark/scripts/logit_lens.py --dataset alphavantage
    uv run python benchmark/scripts/logit_lens.py --dataset stripe --model Qwen/Qwen2.5-7B-Instruct
    uv run python benchmark/scripts/logit_lens.py --dataset stripe --probe-position pre  # token before param name
    uv run python benchmark/scripts/logit_lens.py --dataset stripe --probe-position at   # first token of param name
"""

import argparse
import json
import math
import sys
from pathlib import Path
from textwrap import indent

# ---------------------------------------------------------------------------
# Corporate-proxy workaround: patch huggingface_hub's httpx client to skip
# SSL verification (the proxy injects a self-signed cert not in system bundle).
# Must happen before any HF or transformers imports.
# ---------------------------------------------------------------------------
try:
    import httpx
    import huggingface_hub.utils._http as _hf_http

    def _patched_client_factory() -> httpx.Client:
        return httpx.Client(
            event_hooks={"request": [_hf_http.hf_request_event_hook]},
            follow_redirects=True,
            timeout=None,
            verify=False,
        )

    _hf_http.set_client_factory(_patched_client_factory)
except Exception:
    pass  # not in a corporate-proxy environment, no patch needed

import torch
import torch.nn.functional as F

ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(ROOT))

# Re-use the dataset configs and doc extraction from logprob_conflict.py
from benchmark.scripts.logprob_conflict import DATASET_CONFIGS, extract_doc_section, SYSTEM_PROMPT, HUMAN_TEMPLATE

DEFAULT_MODEL = "Qwen/Qwen2.5-7B-Instruct"

# ---------------------------------------------------------------------------
# Device selection
# ---------------------------------------------------------------------------

def best_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------

def load_model(model_id: str, device: torch.device):
    from transformers import AutoTokenizer, AutoModelForCausalLM

    print(f"Loading {model_id} on {device}...", flush=True)
    dtype = torch.float16 if device.type in ("cuda", "mps") else torch.float32

    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=dtype,
        device_map=str(device),
        trust_remote_code=True,
    )
    model.eval()
    print(f"Loaded — {sum(p.numel() for p in model.parameters()) / 1e9:.1f}B params, "
          f"{model.config.num_hidden_layers} layers, "
          f"hidden_dim={model.config.hidden_size}", flush=True)
    return tokenizer, model


# ---------------------------------------------------------------------------
# Logit lens
# ---------------------------------------------------------------------------

def get_unembedding(model) -> torch.Tensor:
    """Return the unembedding matrix W_U (vocab_size, hidden_size)."""
    # Works for most decoder-only models (GPT-2, Llama, Qwen, Mistral, etc.)
    # lm_head.weight has shape (vocab_size, hidden_size)
    return model.lm_head.weight.detach().float()


def logit_lens_at_position(
    hidden_states: tuple,   # tuple of (batch, seq_len, hidden) — one per layer
    position: int,          # token index to probe
    W_U: torch.Tensor,      # (vocab_size, hidden_size)
    token_ids: list[int],   # vocab IDs of tokens we care about
    model,
) -> list[dict]:
    """
    For each layer, project the hidden state at `position` through W_U,
    apply softmax, and return the probabilities of the requested token_ids.

    Returns a list of dicts, one per layer:
        {"layer": l, "probs": {token_id: prob, ...}, "logits": {token_id: logit, ...}}
    """
    results = []
    has_ln = hasattr(model, "model") and hasattr(model.model, "norm")

    for l, hs in enumerate(hidden_states):
        h = hs[0, position, :].float()  # (hidden_size,)

        # Apply final layer norm if probing intermediate layers
        # (the logit lens without LN is noisier in early layers)
        if has_ln and l < len(hidden_states) - 1:
            h = model.model.norm(h.unsqueeze(0)).squeeze(0)

        logits = W_U @ h  # (vocab_size,)
        log_probs = F.log_softmax(logits, dim=-1)

        layer_result = {"layer": l}
        layer_result["probs"]  = {tid: math.exp(log_probs[tid].item()) for tid in token_ids}
        layer_result["logits"] = {tid: logits[tid].item()              for tid in token_ids}
        results.append(layer_result)

    return results


# ---------------------------------------------------------------------------
# Token ID resolution — handles multi-token names
# ---------------------------------------------------------------------------

def get_first_token_ids(tokenizer, names: list[str]) -> dict[str, list[int]]:
    """
    For each name, return the token IDs of the first sub-token when the name
    appears after a space (as it would in a Python function signature).
    We probe the first sub-token position since that's where divergence starts.
    """
    result = {}
    for name in names:
        # Try with leading space (most common in code context)
        for prefix in (" ", "", "\n    ", "\n"):
            ids = tokenizer.encode(prefix + name, add_special_tokens=False)
            if ids:
                result[name] = ids[0]  # first sub-token ID
                break
    return result


# ---------------------------------------------------------------------------
# Find probe position in the token sequence
# ---------------------------------------------------------------------------

def find_probe_positions(
    token_ids_seq: list[int],
    tokenizer,
    target_names: list[str],
    probe_at: str = "pre",  # "pre" = token before name, "at" = first token of name
) -> dict[str, int | None]:
    """
    Decode the token sequence cumulatively and find where each target name
    first appears, then return the probe position.
    """
    decoded_parts = [tokenizer.decode([t]) for t in token_ids_seq]
    cumulative = []
    running = ""
    for part in decoded_parts:
        running += part
        cumulative.append(running)

    positions = {}
    for name in target_names:
        pos = None
        for i, (text_before, text_at) in enumerate(
            zip([""] + cumulative[:-1], cumulative)
        ):
            if name not in text_before and name in text_at:
                if probe_at == "pre":
                    pos = max(0, i - 1)   # token just before the name
                else:
                    pos = i               # first token of the name itself
                break
        positions[name] = pos
    return positions


# ---------------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------------

def run(dataset: str, model_id: str, probe_at: str, max_new_tokens: int) -> None:
    cfg = DATASET_CONFIGS[dataset]
    doc_path    = ROOT / cfg["doc"]
    mut_path    = ROOT / cfg["mutations_file"]
    mutations   = json.loads(mut_path.read_text())["mutations"]
    doc_snippet = extract_doc_section(doc_path, cfg["endpoint_header"])

    print(f"\n=== Logit Lens Probe ===")
    print(f"Dataset   : {dataset}")
    print(f"Endpoint  : {cfg['endpoint_desc']}")
    print(f"Model     : {model_id}")
    print(f"Probe at  : {probe_at} (token {'before' if probe_at == 'pre' else 'at'} param name)")
    print(f"Mutations : {[m['original'] + '→' + m['mutated'] for m in mutations]}")
    # Cap doc snippet to 3000 chars so the prompt stays short enough for MPS generation.
    # MPS has a 2^32-byte intermediate buffer limit; long prompts + KV-cache hit it.
    doc_snippet = doc_snippet[:3000]
    print(f"Doc       : {len(doc_snippet)} chars (capped for MPS)\n")

    device = best_device()
    tokenizer, model = load_model(model_id, device)
    W_U = get_unembedding(model).to(device)
    n_layers = model.config.num_hidden_layers

    # Build the prompt using the same template as logprob_conflict.py
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user",   "content": HUMAN_TEMPLATE.format(doc_snippet=doc_snippet)},
    ]
    prompt_ids = tokenizer.apply_chat_template(
        messages, tokenize=True, add_generation_prompt=True, return_tensors="pt",
    )
    if hasattr(prompt_ids, "input_ids"):
        prompt_ids = prompt_ids.input_ids
    prompt_ids = prompt_ids.to(device)
    print(f"Prompt    : {prompt_ids.shape[1]} tokens", flush=True)

    # --- Generate a response first so we know what the model wrote ---
    print("Generating response...", flush=True)
    with torch.no_grad():
        gen_ids = model.generate(
            prompt_ids,
            max_new_tokens=max_new_tokens,
            do_sample=False,   # greedy — deterministic, matches logit lens expectation
            temperature=1.0,
            pad_token_id=tokenizer.eos_token_id,
        )
    response_ids = gen_ids[0, prompt_ids.shape[1]:]
    response_text = tokenizer.decode(response_ids, skip_special_tokens=True)
    print(f"Response ({len(response_ids)} tokens):\n{indent(response_text, '  ')}\n")

    # Full sequence = prompt + response (we probe positions in the response)
    full_ids = gen_ids[0].tolist()
    response_start = prompt_ids.shape[1]

    # --- Resolve token IDs for all mutation names ---
    all_names = [name for m in mutations for name in (m["original"], m["mutated"])]
    name_to_first_token_id = get_first_token_ids(tokenizer, all_names)
    print("Token ID mapping:")
    for name, tid in name_to_first_token_id.items():
        print(f"  {name!r:25s} → token_id={tid:6d}  ({tokenizer.decode([tid])!r})")
    print()

    # --- Find where each name appears in the response token sequence ---
    response_token_strs = [tokenizer.decode([t]) for t in full_ids[response_start:]]
    probe_positions_in_response = find_probe_positions(
        full_ids[response_start:], tokenizer,
        target_names=all_names, probe_at=probe_at,
    )

    # --- Logit lens for each mutation (per-mutation windowed forward pass) ---
    # MPS has a 2^32-byte intermediate buffer limit. Running output_hidden_states=True
    # over the full prompt+response sequence (~1000+ tokens) can exceed this.
    # Instead, for each probe position we slice a window of WINDOW_SIZE tokens
    # ending at the probe position and run just that shorter sequence.
    WINDOW_SIZE = 256  # tokens; enough context to avoid degrading attention badly

    all_results = []
    for mutation in mutations:
        orig = mutation["original"]
        mut  = mutation["mutated"]

        orig_pos = probe_positions_in_response.get(orig)
        mut_pos  = probe_positions_in_response.get(mut)
        winner_name, winner_pos = (mut, mut_pos) if mut_pos is not None else (orig, orig_pos)
        outcome = "doc" if mut_pos is not None else "memory"

        if winner_pos is None:
            print(f"  {orig}→{mut}: neither name found in output, skipping")
            continue

        # Absolute position in the full sequence
        abs_pos = response_start + winner_pos
        abs_pos = min(abs_pos, len(full_ids) - 1)

        # Slice a window of tokens ending at abs_pos to keep MPS happy
        win_start = max(0, abs_pos - WINDOW_SIZE + 1)
        window_ids = full_ids[win_start : abs_pos + 1]
        pos_in_window = len(window_ids) - 1  # always the last token of the window

        print(f"  Running hidden-state pass: window [{win_start}:{abs_pos+1}] "
              f"= {len(window_ids)} tokens", flush=True)
        win_tensor = torch.tensor([window_ids], device=device)
        with torch.no_grad():
            out = model(win_tensor, output_hidden_states=True)
        hidden_states = out.hidden_states  # (n_layers+1) x (1, win_len, hidden)
        del out, win_tensor

        # Token IDs we care about
        orig_tid = name_to_first_token_id.get(orig)
        mut_tid  = name_to_first_token_id.get(mut)
        token_ids_to_probe = [t for t in [orig_tid, mut_tid] if t is not None]

        layer_data = logit_lens_at_position(
            hidden_states, pos_in_window, W_U, token_ids_to_probe, model
        )
        del hidden_states

        print(f"  [{('DOC WON' if outcome == 'doc' else 'MEMORY WON'):10s}]  "
              f"{orig!r:20s} ↔  {mut!r}   (probe pos={abs_pos}, response tok={winner_pos})")
        print(f"  {'Layer':>6}  {'P(orig='+orig+')':>22}  {'P(mut='+mut+')':>22}  {'Winner':>10}  {'Gap (nats)':>12}")
        print(f"  {'-'*80}")

        prev_winner = None
        flip_layer  = None

        for ld in layer_data:
            l         = ld["layer"]
            p_orig    = ld["probs"].get(orig_tid, 0.0) if orig_tid else 0.0
            p_mut     = ld["probs"].get(mut_tid,  0.0) if mut_tid  else 0.0
            leading   = orig if p_orig >= p_mut else mut
            gap_nats  = abs(math.log(p_orig + 1e-30) - math.log(p_mut + 1e-30))

            if prev_winner is not None and leading != prev_winner and flip_layer is None:
                flip_layer = l
                print(f"  {'':>6}  ← LEAD CHANGES HERE at layer {l}")

            bar_len   = 30
            orig_bar  = int(p_orig / max(p_orig + p_mut, 1e-9) * bar_len)
            mut_bar   = bar_len - orig_bar
            bar       = "O" * orig_bar + "M" * mut_bar

            pct_depth = l / max(n_layers, 1) * 100
            label     = (f"{'early' if pct_depth < 33 else 'mid' if pct_depth < 66 else 'late ':5s}"
                         f" L{l:02d}")
            print(f"  {label:>10}  {p_orig:>22.6f}  {p_mut:>22.6f}  {leading:>10s}  "
                  f"{gap_nats:>10.2f}  [{bar}]")
            prev_winner = leading

        summary = {
            "mutation": mutation,
            "outcome": outcome,
            "probe_position": abs_pos,
            "flip_layer": flip_layer,
            "layers": layer_data,
        }
        all_results.append(summary)
        print()

    # Save
    out_path = ROOT / f"benchmark/output/logit_lens_{dataset}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps({
        "dataset": dataset,
        "model": model_id,
        "probe_at": probe_at,
        "mutations": mutations,
        "results": all_results,
    }, indent=2))
    print(f"Full results saved to {out_path.relative_to(ROOT)}")


def main():
    parser = argparse.ArgumentParser(description="Logit lens layer probe for memory vs. context conflict")
    parser.add_argument("--dataset", default="zulip", choices=list(DATASET_CONFIGS.keys()))
    parser.add_argument("--model",   default=DEFAULT_MODEL)
    parser.add_argument("--probe-position", default="pre", choices=["pre", "at"],
                        help="'pre' = token just before param name (default); 'at' = first token of name")
    parser.add_argument("--max-new-tokens", type=int, default=400)
    args = parser.parse_args()
    run(args.dataset, args.model, args.probe_position, args.max_new_tokens)


if __name__ == "__main__":
    main()
