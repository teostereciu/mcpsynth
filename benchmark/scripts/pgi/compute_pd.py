"""
compute_pd.py — Parametric Density Proxy (P_d)

Fetches GitHub star counts for each API's primary SDK/official repo as a proxy
for how well-represented the API is in LLM pre-training data. Also records
doc corpus size (bytes) as a secondary proxy for API surface area prominence.

Outputs: pgi/pd_scores.json

Usage:
    python compute_pd.py [--token GITHUB_TOKEN]

A GitHub token is optional but strongly recommended to avoid rate limiting
(60 req/hr unauthenticated vs 5000/hr authenticated).
"""

import argparse
import json
import os
import time
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# SDK repo registry
# Each entry: (owner, repo) for the most prominent official or community SDK.
# Selection criteria: official SDK preferred; if none, most-starred community
# library. All choices are defensible and documented below.
# ---------------------------------------------------------------------------
SDK_REPOS: dict[str, tuple[str, str]] = {
    # Official Stripe Python SDK — canonical, 5000+ stars
    "stripe": ("stripe", "stripe-python"),
    # PyGithub — most prominent Python GitHub client; octokit is JS-only
    "github": ("PyGithub", "PyGithub"),
    # Official Atlassian Python API (covers Confluence + Jira)
    "confluence": ("atlassian-api", "atlassian-python-api"),
    "jira": ("atlassian-api", "atlassian-python-api"),
    # shopify-python-api — official Shopify Python library
    "shopify": ("Shopify", "shopify_python_api"),
    # Mastodon.py — the dominant Python Mastodon client
    "mastodon": ("halcy", "Mastodon.py"),
    # notion-sdk-py — official Notion Python SDK
    "notion": ("ramnes", "notion-sdk-py"),
    # Zulip Python API bindings — official
    "zulip": ("zulip", "python-zulip-api"),
    # alpha_vantage — most prominent Python wrapper; no official SDK
    "alphavantage": ("RomelTorres", "alpha_vantage"),
    # pyowm — de facto standard Python OWM client; no official SDK
    "openweathermap": ("csparpa", "pyowm"),
    # spoonacular-python-client — official generated client
    "spoonacular": ("ddsky", "spoonacular-api-clients"),
    # eBay SDK for Python — official
    "ebay_buy": ("eBay", "ebay-sdk-python"),
    "ebay_sell": ("eBay", "ebay-sdk-python"),
    "ebay_commerce": ("eBay", "ebay-sdk-python"),
}

# Doc corpus sizes in bytes (computed from `wc -c` on docs/*.md, excl. manifest)
# These are stable measurements from the local dataset.
DOC_SIZES_BYTES: dict[str, int] = {
    "stripe":         1_522_965,
    "github":         7_072_827,
    "zulip":          2_998_513,
    "notion":           356_140,
    "confluence":     1_026_366,
    "jira":           1_802_117,
    "shopify":        3_994_407,
    "mastodon":         458_667,
    "openweathermap":   104_242,
    "alphavantage":     773_375,
    "spoonacular":      335_141,
    "ebay_buy":       1_490_457,
    "ebay_sell":        519_771,
    "ebay_commerce":    379_751,
}

APIS = list(DOC_SIZES_BYTES.keys())


def fetch_stars(owner: str, repo: str, session: requests.Session) -> int | None:
    url = f"https://api.github.com/repos/{owner}/{repo}"
    resp = session.get(url, timeout=10)
    if resp.status_code == 200:
        return resp.json()["stargazers_count"]
    if resp.status_code == 404:
        print(f"  [WARN] Repo not found: {owner}/{repo}")
        return None
    if resp.status_code == 403:
        print(f"  [WARN] Rate limited fetching {owner}/{repo} — add a GitHub token with --token")
        return None
    print(f"  [WARN] HTTP {resp.status_code} for {owner}/{repo}")
    return None


def normalize(values: dict[str, float]) -> dict[str, float]:
    """Min-max normalize to [0, 1]."""
    valid = {k: v for k, v in values.items() if v is not None}
    lo, hi = min(valid.values()), max(valid.values())
    if hi == lo:
        return {k: 0.5 for k in values}
    return {k: (v - lo) / (hi - lo) if v is not None else None for k, v in values.items()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", default=os.environ.get("GITHUB_TOKEN"), help="GitHub API token")
    parser.add_argument("--out", default=Path(__file__).parent / "pd_scores.json")
    args = parser.parse_args()

    session = requests.Session()
    session.headers["Accept"] = "application/vnd.github+json"
    if args.token:
        session.headers["Authorization"] = f"Bearer {args.token}"
        print("Using authenticated GitHub API (5000 req/hr limit)")
    else:
        print("No GitHub token — using unauthenticated API (60 req/hr). Pass --token or set GITHUB_TOKEN.")

    # --- Fetch star counts ---
    stars_raw: dict[str, int | None] = {}
    seen_repos: dict[tuple, int] = {}  # cache deduped repos (confluence/jira share one repo)

    for api in APIS:
        owner, repo = SDK_REPOS[api]
        key = (owner, repo)
        if key in seen_repos:
            stars_raw[api] = seen_repos[key]
            print(f"  {api:20s} {owner}/{repo} — cached {seen_repos[key]:,} stars")
            continue
        stars = fetch_stars(owner, repo, session)
        stars_raw[api] = stars
        if stars is not None:
            seen_repos[key] = stars
        label = f"{stars:,}" if stars is not None else "N/A"
        print(f"  {api:20s} {owner}/{repo} — {label} stars")
        time.sleep(0.3)  # be polite even when authenticated

    # --- Normalize star counts ---
    stars_norm = normalize(stars_raw)

    # --- Normalize doc sizes ---
    doc_norm = normalize(DOC_SIZES_BYTES)

    # --- Composite P_d = 0.7 * stars_norm + 0.3 * doc_norm ---
    # Stars are a stronger pre-training signal; doc size is a secondary proxy.
    # APIs with missing star data fall back to doc_norm only.
    pd_composite: dict[str, float] = {}
    for api in APIS:
        s = stars_norm.get(api)
        d = doc_norm[api]
        if s is None:
            pd_composite[api] = d
        else:
            pd_composite[api] = 0.7 * s + 0.3 * d

    # Re-normalize the composite to [0,1]
    pd_final = normalize(pd_composite)

    out = {
        "description": (
            "Parametric Density Proxy (P_d) for each API. "
            "Composite of normalized GitHub SDK stars (weight 0.7) and "
            "normalized doc corpus size (weight 0.3), re-normalized to [0,1]. "
            "Higher = more prominent in pre-training data."
        ),
        "components": {
            "stars_raw": stars_raw,
            "stars_norm": {k: round(v, 4) if v is not None else None for k, v in stars_norm.items()},
            "doc_size_bytes": DOC_SIZES_BYTES,
            "doc_norm": {k: round(v, 4) for k, v in doc_norm.items()},
        },
        "pd_scores": {k: round(v, 4) if v is not None else None for k, v in pd_final.items()},
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nWrote {out_path}")
    print("\nP_d scores (higher = better pre-training coverage):")
    for api, score in sorted(pd_final.items(), key=lambda x: -(x[1] or 0)):
        bar = "█" * int((score or 0) * 30)
        print(f"  {api:20s} {score:.3f}  {bar}")


if __name__ == "__main__":
    main()
