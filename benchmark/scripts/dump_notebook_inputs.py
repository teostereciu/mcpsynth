#!/usr/bin/env python3
"""
dump_notebook_inputs.py — prints the doc snippet and mutations JSON
ready to paste into logit_lens_h100.ipynb.

Usage:
    python benchmark/scripts/dump_notebook_inputs.py --dataset zulip
    python benchmark/scripts/dump_notebook_inputs.py --dataset stripe
"""
import argparse, json
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent

DATASET_CONFIGS = {
    "stripe": {
        "doc": "benchmark/datasets/stripe/docs_mutated/payment_intents.md",
        "endpoint_header": "# Create a PaymentIntent",
        "mutations_file": "benchmark/datasets/stripe/mutations.json",
    },
    "zulip": {
        "doc": "benchmark/datasets/zulip/docs_mutated/api_get-messages.md",
        "endpoint_header": "# Get messages\n",
        "mutations_file": "benchmark/datasets/zulip/mutations.json",
    },
    "ebay_sell": {
        "doc": "benchmark/datasets/ebay_sell/docs_mutated/api_account_get-fulfillment-policies.md",
        "endpoint_header": "# getFulfillmentPolicies",
        "mutations_file": "benchmark/datasets/ebay_sell/mutations.json",
    },
    "jira": {
        "doc": "benchmark/datasets/jira/docs_mutated/api_issue-search.md",
        "endpoint_header": "## Search for issues using JQL enhanced search (GET)",
        "mutations_file": "benchmark/datasets/jira/mutations.json",
    },
    "alphavantage": {
        "doc": "benchmark/datasets/alphavantage/docs_mutated/api_time_series_data.md",
        "endpoint_header": "#### TIME_SERIES_DAILY\n",
        "mutations_file": "benchmark/datasets/alphavantage/mutations.json",
    },
}


def extract_doc_section(doc_path: Path, section_header: str, char_limit: int = 6000) -> str:
    text = doc_path.read_text()
    start = text.rfind(section_header)
    if start == -1:
        return text[:char_limit]
    level = len(section_header) - len(section_header.lstrip("#"))
    next_h = text.find("\n" + "#" * level + " ", start + len(section_header))
    end = next_h if next_h != -1 else len(text)
    return text[start:end].strip()[:char_limit]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="zulip", choices=list(DATASET_CONFIGS.keys()))
    args = parser.parse_args()

    cfg = DATASET_CONFIGS[args.dataset]
    doc_section = extract_doc_section(ROOT / cfg["doc"], cfg["endpoint_header"])
    mutations_json = (ROOT / cfg["mutations_file"]).read_text()

    sep = "=" * 70
    print(f"\n{sep}")
    print("PASTE INTO RAW_DOC (between the triple-quotes):")
    print(sep)
    print(doc_section)
    print(f"\n{sep}")
    print("PASTE INTO RAW_MUTATIONS (between the triple-quotes):")
    print(sep)
    print(mutations_json)


if __name__ == "__main__":
    main()
