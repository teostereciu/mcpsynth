"""
pgi_regression.py — Parametric Gravity Index: regression + visualization

Loads P_d and R_p scores, runs a multiple linear regression predicting the
docs-vs-nodocs CURRENT gap, and produces:

  1. pgi_quadrant.png  — 2D scatter of (P_d, R_p) with gap as bubble size/color
  2. pgi_predicted.png — predicted vs actual gap scatter with R² annotation
  3. pgi_components.png — bar chart of normalized sub-signal contributions

Prints a full regression summary including coefficients, p-values (via
permutation test, since n=14 is too small for F-distribution assumptions),
and per-API residuals.

Usage:
    python pgi_regression.py [--pd pd_scores.json] [--rp rp_scores.json]

Dependencies: numpy, matplotlib, scipy (optional, for scipy permutation)
"""

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ---------------------------------------------------------------------------
# Ground truth: docs vs nodocs SYNTH scores (%) from RESULTS.md
# SYNTH = SERVER_SUFFICIENT tasks / (sufficient + insufficient), excluding
# UNKNOWN verdicts. Measures server quality independent of agent behaviour,
# avoiding agent noise (AGENT_REASONING failures, implementation bugs in the
# docs server, etc.).
# Gap = docs_synth - nodocs_synth (positive = docs improve server quality,
#       negative = nodocs produces a better-quality server).
# Values taken from the parenthesised SYNTH column in the 14-dataset matrix.
# ---------------------------------------------------------------------------
SCORES: dict[str, dict] = {
    "stripe":         {"docs": 77, "nodocs": 68},
    "github":         {"docs": 61, "nodocs": 87},
    "zulip":          {"docs": 84, "nodocs": 48},
    "notion":         {"docs": 91, "nodocs": 100},
    "confluence":     {"docs": 95, "nodocs": 95},
    "jira":           {"docs": 56, "nodocs": 44},
    "shopify":        {"docs": 89, "nodocs": 94},
    "mastodon":       {"docs": 93, "nodocs": 100},
    "openweathermap": {"docs": 100, "nodocs": 83},
    "alphavantage":   {"docs": 84, "nodocs": 89},
    "spoonacular":    {"docs": 75, "nodocs": 75},
    "ebay_buy":       {"docs": 88, "nodocs": 94},
    "ebay_sell":      {"docs": 43, "nodocs": 50},
    "ebay_commerce":  {"docs": 100, "nodocs": 85},
}

# Standard error on gap estimate for the 3 variance-studied APIs.
# SYNTH is more stable than CURRENT (agent excluded), so SEs are tighter.
# Approximated from cross-run SYNTH variance where available.
GAP_SE: dict[str, float] = {
    "shopify": 4.5,   # SYNTH locked at 94% nodocs across all runs; docs 61–94% → SEM≈6
    "github":  3.0,   # docs SYNTH 57–70% (3 valid); nodocs SYNTH 83–91% (3 runs)
    "stripe":  5.0,   # docs SYNTH 68–77% (4 valid); nodocs SYNTH 57–73% (4 valid)
}

DV_LABEL = "SYNTH gap: docs − nodocs server quality (pp)"
DV_SHORT = "SYNTH gap (pp)"

# Display labels (shorter for crowded plots)
LABELS: dict[str, str] = {
    "stripe": "Stripe", "github": "GitHub", "zulip": "Zulip",
    "notion": "Notion", "confluence": "Confluence", "jira": "Jira",
    "shopify": "Shopify", "mastodon": "Mastodon",
    "openweathermap": "OWM", "alphavantage": "AlphaVantage",
    "spoonacular": "Spoonacular", "ebay_buy": "eBay Buy",
    "ebay_sell": "eBay Sell", "ebay_commerce": "eBay Commerce",
}

DEFAULT_PD = Path(__file__).parent / "pd_scores.json"
DEFAULT_RP = Path(__file__).parent / "rp_scores.json"


def load_json(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found. Run compute_pd.py / compute_rp.py first."
        )
    return json.loads(path.read_text())


def ols(X: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, float, np.ndarray]:
    """OLS regression. Returns (coefficients incl. intercept, R², residuals)."""
    X_aug = np.column_stack([np.ones(len(X)), X])
    beta, _, _, _ = np.linalg.lstsq(X_aug, y, rcond=None)
    y_hat = X_aug @ beta
    ss_res = np.sum((y - y_hat) ** 2)
    ss_tot = np.sum((y - y.mean()) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
    return beta, r2, y - y_hat


def permutation_pvalue(
    X: np.ndarray, y: np.ndarray, coef_idx: int, n_perm: int = 9999, seed: int = 42
) -> float:
    """
    Permutation test for the significance of predictor at coef_idx (0=pd, 1=rp).
    Returns p-value (two-tailed).
    """
    rng = np.random.default_rng(seed)
    beta_obs, _, _ = ols(X, y)
    observed = abs(beta_obs[coef_idx + 1])  # +1 because coef[0] is intercept

    count = 0
    for _ in range(n_perm):
        y_perm = rng.permutation(y)
        beta_perm, _, _ = ols(X, y_perm)
        if abs(beta_perm[coef_idx + 1]) >= observed:
            count += 1
    return (count + 1) / (n_perm + 1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pd", default=DEFAULT_PD, type=Path)
    parser.add_argument("--rp", default=DEFAULT_RP, type=Path)
    parser.add_argument("--out-dir", default=Path(__file__).parent, type=Path)
    args = parser.parse_args()

    pd_data = load_json(args.pd)
    rp_data = load_json(args.rp)

    pd_scores = pd_data["pd_scores"]
    rp_scores = rp_data["rp_scores"]

    # Align APIs present in all three datasets
    apis = [a for a in SCORES if a in pd_scores and a in rp_scores]
    n = len(apis)
    print(f"Running regression on {n} APIs: {', '.join(apis)}\n")

    pd_arr = np.array([pd_scores[a] for a in apis])
    rp_arr = np.array([rp_scores[a] for a in apis])
    gap_arr = np.array([SCORES[a]["docs"] - SCORES[a]["nodocs"] for a in apis], dtype=float)

    interaction = pd_arr * rp_arr

    # --- Model A: additive (P_d + R_p) ---
    X_add = np.column_stack([pd_arr, rp_arr])
    beta_a, r2_a, resid_a = ols(X_add, gap_arr)
    p_pd_a = permutation_pvalue(X_add, gap_arr, 0)
    p_rp_a = permutation_pvalue(X_add, gap_arr, 1)
    gap_hat_a = beta_a[0] + beta_a[1] * pd_arr + beta_a[2] * rp_arr

    # --- Model B: with interaction term (P_d + R_p + P_d×R_p) ---
    X_int = np.column_stack([pd_arr, rp_arr, interaction])
    beta_b, r2_b, resid_b = ols(X_int, gap_arr)
    p_pd_b  = permutation_pvalue(X_int, gap_arr, 0)
    p_rp_b  = permutation_pvalue(X_int, gap_arr, 1)
    p_int_b = permutation_pvalue(X_int, gap_arr, 2)
    gap_hat_b = beta_b[0] + beta_b[1]*pd_arr + beta_b[2]*rp_arr + beta_b[3]*interaction

    # Use the better-fitting model for plots
    beta, r2, residuals, gap_hat = beta_b, r2_b, resid_b, gap_hat_b
    intercept, beta_pd, beta_rp, beta_int = beta_b

    print("=" * 70)
    print("  PARAMETRIC GRAVITY INDEX — Regression Results")
    print("=" * 70)
    print(f"  n = {n} APIs\n")

    print(f"  MODEL A  (additive):  gap = β₀ + β_pd·P_d + β_rp·R_p")
    print(f"  β₀={beta_a[0]:+.2f}  β_pd={beta_a[1]:+.2f}(p={p_pd_a:.3f})  "
          f"β_rp={beta_a[2]:+.2f}(p={p_rp_a:.3f})  R²={r2_a:.3f}")
    print()
    print(f"  MODEL B  (interaction):  gap = β₀ + β_pd·P_d + β_rp·R_p + β_int·(P_d×R_p)")
    print(f"  β₀={beta_b[0]:+.2f}  β_pd={beta_b[1]:+.2f}(p={p_pd_b:.3f})  "
          f"β_rp={beta_b[2]:+.2f}(p={p_rp_b:.3f})  "
          f"β_int={beta_b[3]:+.2f}(p={p_int_b:.3f})  R²={r2_b:.3f}")
    print(f"  ΔR² from interaction term: {r2_b - r2_a:+.3f}")
    print()
    print("  Per-API predictions (Model B):")
    print(f"  {'API':18s}  {'P_d':>5}  {'R_p':>5}  {'P_d×R_p':>7}  "
          f"{'gap':>6}  {'pred':>6}  {'resid':>7}")
    print("  " + "-" * 68)
    for i, api in enumerate(apis):
        se_str = f" ±{GAP_SE[api]:.1f}" if api in GAP_SE else ""
        print(
            f"  {LABELS[api]:18s}  {pd_arr[i]:.3f}  {rp_arr[i]:.3f}  "
            f"{interaction[i]:.3f}    "
            f"{gap_arr[i]:+5.1f}{se_str:6s}  {gap_hat[i]:+6.1f}  {residuals[i]:+7.1f}"
        )
    print()
    print("  NOTE: p-values from 9999-iteration permutation test.")
    print("  With n=14, treat as hypothesis-generating, not validated.")
    print("=" * 70)

    # -----------------------------------------------------------------------
    # Plot 1: Quadrant scatter (P_d × R_p), bubble = |gap|, color = sign
    # -----------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(9, 7))

    colors = ["#d62728" if g > 0 else "#1f77b4" for g in gap_arr]  # red=docs wins, blue=nodocs wins
    sizes = np.abs(gap_arr) * 18 + 60  # min size 60 when gap=0

    sc = ax.scatter(pd_arr, rp_arr, s=sizes, c=colors, alpha=0.75, linewidths=0.8, edgecolors="white")

    for i, api in enumerate(apis):
        # Offset labels to avoid overlap
        dx, dy = 0.02, 0.015
        if api in ("mastodon", "openweathermap"):
            dx = -0.01
        ax.annotate(
            LABELS[api],
            (pd_arr[i], rp_arr[i]),
            xytext=(pd_arr[i] + dx, rp_arr[i] + dy),
            fontsize=8.5,
            ha="left",
        )

    # Quadrant lines at medians
    ax.axvline(np.median(pd_arr), color="gray", linewidth=0.8, linestyle="--", alpha=0.6)
    ax.axhline(np.median(rp_arr), color="gray", linewidth=0.8, linestyle="--", alpha=0.6)

    # Quadrant labels
    xm, ym = np.median(pd_arr), np.median(rp_arr)
    ax.text(0.02, 0.97, "Low P_d, High R_p\n(docs critical)", transform=ax.transAxes,
            fontsize=8, va="top", color="#555", style="italic")
    ax.text(0.60, 0.97, "High P_d, High R_p\n(priors may override docs)", transform=ax.transAxes,
            fontsize=8, va="top", color="#555", style="italic")
    ax.text(0.02, 0.05, "Low P_d, Low R_p\n(simple API, docs help)", transform=ax.transAxes,
            fontsize=8, va="bottom", color="#555", style="italic")
    ax.text(0.60, 0.05, "High P_d, Low R_p\n(nodocs sufficient)", transform=ax.transAxes,
            fontsize=8, va="bottom", color="#555", style="italic")

    red_patch = mpatches.Patch(color="#d62728", alpha=0.75, label="docs wins (gap > 0)")
    blue_patch = mpatches.Patch(color="#1f77b4", alpha=0.75, label="nodocs wins (gap < 0)")
    size_note = mpatches.Patch(color="white", label="bubble size ∝ |gap|")
    ax.legend(handles=[red_patch, blue_patch, size_note], loc="upper center",
              bbox_to_anchor=(0.5, -0.08), ncol=3, fontsize=9)

    ax.set_xlabel("Parametric Density Proxy ($P_d$) — pre-training coverage", fontsize=11)
    ax.set_ylabel("Protocol Rigidity Score ($R_p$) — parameter name idiosyncrasy", fontsize=11)
    ax.set_title(
        f"Parametric Gravity Index — PGI Quadrant (DV: SYNTH gap)\n"
        f"Model B: R²={r2:.3f}  β_pd={beta_pd:+.1f}  β_rp={beta_rp:+.1f}  "
        f"β_int={beta_int:+.1f}  n={n}",
        fontsize=11,
    )
    ax.set_xlim(-0.05, 1.10)
    ax.set_ylim(-0.05, 1.10)

    plt.tight_layout()
    q_path = args.out_dir / "pgi_quadrant.png"
    fig.savefig(q_path, dpi=150, bbox_inches="tight")
    print(f"\nSaved {q_path}")
    plt.close(fig)

    # -----------------------------------------------------------------------
    # Plot 2: Predicted vs actual gap
    # -----------------------------------------------------------------------
    fig2, ax2 = plt.subplots(figsize=(7, 6))

    ax2.scatter(gap_hat, gap_arr, s=80, c=colors, alpha=0.8, edgecolors="white", linewidths=0.8)

    for i, api in enumerate(apis):
        se = GAP_SE.get(api)
        if se:
            ax2.errorbar(gap_hat[i], gap_arr[i], yerr=se, fmt="none", color=colors[i], alpha=0.5, capsize=3)
        ax2.annotate(LABELS[api], (gap_hat[i], gap_arr[i]),
                     xytext=(gap_hat[i] + 0.5, gap_arr[i] + 0.5), fontsize=8)

    # Perfect prediction line
    lim = max(abs(gap_arr).max(), abs(gap_hat).max()) + 5
    ax2.plot([-lim, lim], [-lim, lim], "k--", linewidth=0.8, alpha=0.5, label="perfect fit")
    ax2.axhline(0, color="gray", linewidth=0.5, alpha=0.4)
    ax2.axvline(0, color="gray", linewidth=0.5, alpha=0.4)

    ax2.set_xlabel(f"Predicted {DV_SHORT}", fontsize=11)
    ax2.set_ylabel(f"Observed {DV_SHORT}", fontsize=11)
    ax2.set_title(
        f"PGI Model B (interaction): Predicted vs Observed SYNTH Gap\n"
        f"R²={r2_b:.3f} vs additive R²={r2_a:.3f}  |  n={n}  |  "
        f"p: β_pd={p_pd_b:.3f}  β_rp={p_rp_b:.3f}  β_int={p_int_b:.3f}",
        fontsize=10,
    )
    ax2.legend(fontsize=9)
    plt.tight_layout()
    p_path = args.out_dir / "pgi_predicted.png"
    fig2.savefig(p_path, dpi=150, bbox_inches="tight")
    print(f"Saved {p_path}")
    plt.close(fig2)

    # -----------------------------------------------------------------------
    # Plot 3: R_p sub-signal breakdown (stacked bars, sorted by R_p)
    # -----------------------------------------------------------------------
    nc  = rp_data["normalized_components"]
    W   = rp_data["weights"]

    fig3, ax3 = plt.subplots(figsize=(11, 5))
    api_order = sorted(apis, key=lambda a: rp_scores[a], reverse=True)
    x = np.arange(len(api_order))
    w = 0.6

    idiosync_contrib = [W["idiosyncrasy"]        * nc["idiosync_norm"][a] for a in api_order]
    camel_contrib    = [W["camelcase_fraction"]   * nc["camel_norm"][a]   for a in api_order]
    enum_contrib     = [W["enum_density"]         * nc["enum_norm"][a]    for a in api_order]

    ax3.bar(x, idiosync_contrib, w, label="Idiosyncrasy (w=0.50)", color="#4e79a7")
    ax3.bar(x, camel_contrib,    w, bottom=idiosync_contrib,
            label="camelCase fraction (w=0.30)", color="#f28e2b")
    bottom2 = [idiosync_contrib[i] + camel_contrib[i] for i in range(len(api_order))]
    ax3.bar(x, enum_contrib, w, bottom=bottom2,
            label="Enum density (w=0.20)", color="#59a14f")

    ax3.set_xticks(x)
    ax3.set_xticklabels([LABELS[a] for a in api_order], rotation=35, ha="right", fontsize=9)
    ax3.set_ylabel("Weighted sub-signal contribution (pre-normalization)", fontsize=10)
    ax3.set_title(
        "R_p Sub-signal Breakdown: Idiosyncrasy + camelCase + Enum Density\n"
        "(sorted by final R_p descending)",
        fontsize=11,
    )
    ax3.legend(fontsize=9, loc="upper right")

    plt.tight_layout()
    c_path = args.out_dir / "pgi_components.png"
    fig3.savefig(c_path, dpi=150, bbox_inches="tight")
    print(f"Saved {c_path}")
    plt.close(fig3)


if __name__ == "__main__":
    main()
