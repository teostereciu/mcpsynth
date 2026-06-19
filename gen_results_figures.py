"""
Consolidated benchmark results figures.

Produces:
  fig1_primary_heatmap.pdf/.png   — 14×3 CURRENT/SYNTH heatmap
  fig2_condition_slopes.pdf/.png  — docs→nodocs→mutated slope chart
  fig3_model_comparison.pdf/.png  — synthesis model comparison (3-panel)
  fig4_synth_scatter.pdf/.png     — SYNTH vs CURRENT scatter
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
def pearsonr(x, y):
    """Minimal Pearson r implementation (avoids scipy dependency)."""
    x, y = np.array(x), np.array(y)
    xm, ym = x - x.mean(), y - y.mean()
    r = (xm * ym).sum() / (np.sqrt((xm**2).sum()) * np.sqrt((ym**2).sum()))
    n = len(x)
    t = r * np.sqrt((n - 2) / (1 - r**2 + 1e-15))
    from math import erfc, sqrt
    p = erfc(abs(t) / sqrt(2))
    return float(r), float(p)

# ── rcParams ──────────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Arial', 'DejaVu Sans'],
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    # NeurIPS-style defaults
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'axes.grid': True,
    'grid.color': '#F0F0F0',
    'grid.linewidth': 0.7,
    'axes.axisbelow': True,
    'legend.fontsize': 8.5,
    'legend.title_fontsize': 9,
    'legend.framealpha': 0.92,
    'legend.edgecolor': '#CCCCCC',
})

nan = np.nan

# ── Palette ───────────────────────────────────────────────────────────────────
NAVY   = '#1B2E5E'
SKY    = '#38BDF8'
VIOLET = '#7C3AED'
TEAL   = '#059669'
RED    = '#DC2626'
AMBER  = '#F59E0B'
GREEN  = '#16A34A'
ANNOT  = '#718096'

CORAL = '#F97316'   # Gemini 3.1 Pro

COND_COLORS  = {'docs': NAVY, 'nodocs': SKY, 'mutated': VIOLET}
LIME   = '#84CC16'   # Haiku 4.5

MODEL_COLORS = {'GPT-5.2': NAVY, 'GPT-5.4': TEAL, 'Sonnet 4.6': VIOLET,
                'Gemini 3.1 Pro': CORAL, 'Qwen3-Coder-Next': RED,
                'Qwen3-Coder-Next-Base': '#EF4444',
                'Haiku 4.5': LIME, 'GPT-5.4-mini': '#94A3B8'}

# Heatmap colormap anchored at 0, 40, 60, 80, 100%
HMAP_CMAP = LinearSegmentedColormap.from_list(
    'rg', ['#C62828', '#EF6C00', '#F9A825', '#7CB342', '#2E7D32'], N=256)

# ── Semantic API category palette — used consistently across fig2, fig7, fig9 ──
# Five categories, same colors everywhere.
CAT_NAVY   = '#1B3A6B'   # Dev tools       (GitHub, Jira)
CAT_TEAL   = '#1A7A68'   # Productivity    (Confluence, Notion)
CAT_RED    = '#C0392B'   # Commerce        (eBay ×3, Shopify, Stripe)
CAT_VIOLET = '#6B3AAD'   # Comms           (Zulip, Mastodon)
CAT_AMBER  = '#B87820'   # Data APIs       (Alphavantage, OWM, Spoonacular)

API_CAT_COLOR = {
    'Alphavantage': CAT_AMBER, 'Confluence': CAT_TEAL,
    'eBay Buy': CAT_RED,       'eBay Commerce': CAT_RED,  'eBay Sell': CAT_RED,
    'GitHub': CAT_NAVY,        'Jira': CAT_NAVY,
    'Mastodon': CAT_VIOLET,    'Notion': CAT_TEAL,
    'OpenWeatherMap': CAT_AMBER, 'Shopify': CAT_RED,
    'Spoonacular': CAT_AMBER,  'Stripe': CAT_RED,         'Zulip': CAT_VIOLET,
}
# Indexed version for positional access (DATASETS order)
DS_COLORS = [API_CAT_COLOR[d] for d in [
    'Alphavantage', 'Confluence', 'eBay Buy', 'eBay Commerce', 'eBay Sell',
    'GitHub', 'Jira', 'Mastodon', 'Notion', 'OpenWeatherMap',
    'Shopify', 'Spoonacular', 'Stripe', 'Zulip',
]]

# ── Data ──────────────────────────────────────────────────────────────────────
DATASETS = [
    'Alphavantage', 'Confluence', 'eBay Buy', 'eBay Commerce', 'eBay Sell',
    'GitHub', 'Jira', 'Mastodon', 'Notion', 'OpenWeatherMap',
    'Shopify', 'Spoonacular', 'Stripe', 'Zulip',
]

#                    docs  nodocs  mutated
CURRENT = np.array([
    [ 86,  90,  88],   # alphavantage  ← corrected from NaN
    [ 92,  93,  91],   # confluence
    [ 73,  67,  80],   # ebay_buy
    [100,  89,  55],   # ebay_commerce
    [ 38,  50,  43],   # ebay_sell
    [ 62,  83,  76],   # github
    [ 50,  25,  50],   # jira
    [100, 100, 100],   # mastodon
    [ 78, 100, 100],   # notion
    [100,  86, 100],   # openweathermap
    [ 87,  92,  62],   # shopify
    [100,  90,  78],   # spoonacular
    [ 72,  62,  57],   # stripe
    [ 80,  60,  62],   # zulip
], dtype=float)

SYNTH = np.array([
    [ 84,  89,  89],
    [ 95,  95,  95],
    [ 88,  94,  88],
    [100,  85,  54],
    [ 43,  50,  43],
    [ 61,  87,  61],
    [ 56,  44,  56],
    [ 93, 100, 100],
    [ 91, 100, 100],
    [100,  83, 100],
    [ 89,  94,  61],
    [ 75,  75,  75],
    [ 77,  68,  73],
    [ 84,  48,  64],
], dtype=float)

CONDITIONS  = ['docs', 'nodocs', 'mutated']
COND_LABELS = ['With docs', 'No docs', 'Mutated params']

# Model comparison data: [docs, nodocs, mutated]
# Models ordered by approximate capability (ascending)
MODEL_DATA = {
    'github': {
        'GPT-5.4-mini':        np.array([ 38,  32,  30], dtype=float),
        'Qwen3-Coder-Next-Base':np.array([nan, nan, nan], dtype=float),  # all: no server.py
        'Qwen3-Coder-Next':    np.array([ 58,  60,  57], dtype=float),
        'Gemini 3.1 Pro':      np.array([ 78,  71,  36], dtype=float),
        'GPT-5.2':             np.array([ 62,  83,  76], dtype=float),
        'GPT-5.4':             np.array([ 58,  89,  73], dtype=float),
        'Haiku 4.5':           np.array([ 95,  90,  86], dtype=float),
        'Sonnet 4.6':          np.array([ 90, 100, 100], dtype=float),
    },
    'stripe': {
        'GPT-5.4-mini':        np.array([ 14,   0,  19], dtype=float),
        'Qwen3-Coder-Next-Base':np.array([nan,  56, nan], dtype=float),  # nodocs only
        'Qwen3-Coder-Next':    np.array([nan,  62, nan], dtype=float),
        'Gemini 3.1 Pro':      np.array([ 47,  50,  59], dtype=float),
        'GPT-5.2':             np.array([ 72,  62,  57], dtype=float),
        'GPT-5.4':             np.array([  8,  62,  12], dtype=float),
        'Haiku 4.5':           np.array([ 57,  75,  86], dtype=float),
        'Sonnet 4.6':          np.array([ 77, 100, 100], dtype=float),
    },
    'zulip': {
        'GPT-5.4-mini':        np.array([ 40,  14,  29], dtype=float),
        'Qwen3-Coder-Next-Base':np.array([nan, nan,   0], dtype=float),  # mutated only
        'Qwen3-Coder-Next':    np.array([nan, nan,  64], dtype=float),
        'Gemini 3.1 Pro':      np.array([ 76,  84,  62], dtype=float),
        'GPT-5.2':             np.array([ 80,  60,  62], dtype=float),
        'GPT-5.4':             np.array([ 90,  85,  71], dtype=float),
        'Haiku 4.5':           np.array([ 55,  36,  26], dtype=float),
        'Sonnet 4.6':          np.array([100,  43, nan], dtype=float),   # nodocs=43 confirmed; mutated: stream error
    },
}

N = len(DATASETS)

# ── Full model comparison data ────────────────────────────────────────────────
# Rows indexed in DATASETS order; nan = broken synth / env-dominated / not run
# Columns: [docs, nodocs, mutated]
MODELS_FULL = ['GPT-5.2', 'GPT-5.4', 'Gemini 3.1 Pro', 'Sonnet 4.6', 'Qwen3-Coder-Next', 'Qwen3-Coder-Next-Base', 'Haiku 4.5']

#                          docs  nodocs  mutated
MODEL_DATA_FULL = {
    'GPT-5.2': np.array([
        [ 86,  90,  88],   # alphavantage
        [ 92,  93,  91],   # confluence
        [ 73,  67,  80],   # ebay_buy
        [100,  89,  55],   # ebay_commerce
        [ 38,  50,  43],   # ebay_sell
        [ 62,  83,  76],   # github
        [ 50,  25,  50],   # jira
        [100, 100, 100],   # mastodon
        [ 78, 100, 100],   # notion
        [100,  86, 100],   # openweathermap
        [ 87,  92,  62],   # shopify
        [100,  90,  78],   # spoonacular
        [ 72,  62,  57],   # stripe
        [ 80,  60,  62],   # zulip
    ], dtype=float),
    'GPT-5.4': np.array([
        [ 80,  92,  78],   # alphavantage
        [ 69, 100,  85],   # confluence
        [ 69,  92, 100],   # ebay_buy
        [ 88,  40,  62],   # ebay_commerce
        [ 29,  45,  44],   # ebay_sell
        [ 58,  89,  73],   # github
        [ 57,  50,  57],   # jira
        [ 91,  90, 100],   # mastodon
        [ 62, 100, nan],   # notion     (mutated: no server.py)
        [100,  95, 100],   # openweathermap
        [ 83,  92,  53],   # shopify
        [ 80,  82,  60],   # spoonacular
        [  8,  62,  12],   # stripe
        [ 90,  85,  71],   # zulip
    ], dtype=float),
    'Gemini 3.1 Pro': np.array([
        [100, 100,  90],   # alphavantage   (small N, but reported as valid)
        [nan, 100, 100],   # confluence     (docs: 0 tools registered → nan)
        [ 90,  67,   0],   # ebay_buy       (mutated: SYNTH=0% 0 tools, 0 scoreable → 0)
        [ 83,  44,  45],   # ebay_commerce
        [ 38,   8,  23],   # ebay_sell
        [ 78,  71,  36],   # github
        [ 58,  44,  31],   # jira
        [100,  92,  87],   # mastodon
        [ 94,  94, 100],   # notion
        [ 85,  90,  95],   # openweathermap
        [ 80,  70,  93],   # shopify
        [ 83,  91,  90],   # spoonacular
        [ 47,  50,  59],   # stripe
        [ 76,  84,  62],   # zulip
    ], dtype=float),
    'Sonnet 4.6': np.array([
        [nan, nan, nan],   # alphavantage   (docs: quota/ENVIRONMENT; nodocs: no server.py; mutated: eval excluded — rate-limited)
        [nan,  94,  47],   # confluence     (docs: no server.py; nodocs=94; mutated=47 re-synth)
        [  0,  79,  33],   # ebay_buy       (docs: no server.py; nodocs=79; mutated: 3 scoreable)
        [100,   0, nan],   # ebay_commerce  (nodocs: 0% server crash; mutated: not run)
        [nan,  73, nan],   # ebay_sell      (docs: no server.py; nodocs=73 re-synth; mutated: stream error)
        [ 90, 100, 100],   # github
        [ 73,  58,  79],   # jira
        [  0,   0,  92],   # mastodon       (docs: no server.py; nodocs: FastMCP crash; mutated=92 5/5 iface)
        [100,  87,  85],   # notion
        [nan,  90, nan],   # openweathermap (docs/mutated: FastMCP crash; nodocs=90%)
        [100,   0, nan],   # shopify        (nodocs: FastMCP crash; mutated: not run)
        [ 93,   0,  92],   # spoonacular    (docs=93 re-eval; nodocs: FastMCP crash; mutated=92)
        [ 77, 100, 100],   # stripe
        [100,  43, nan],   # zulip          (nodocs=43 re-synth 10/23; mutated: stream error)
    ], dtype=float),
    'Qwen3-Coder-Next': np.array([
        [nan, nan, nan],   # alphavantage   (not run)
        [ 39, nan,  50],   # confluence     (nodocs: tiny N → nan)
        [ 12,  80,   6],   # ebay_buy
        [100, nan,  11],   # ebay_commerce  (nodocs: crash)
        [100, nan, nan],   # ebay_sell      (nodocs/mutated: crash; docs: small N kept)
        [ 58,  60,  57],   # github
        [ 71, nan,  42],   # jira           (nodocs: crash)
        [ 87,  80,  54],   # mastodon
        [ 69,   5, nan],   # notion         (mutated: FastMCP crash)
        [100,  86, 100],   # openweathermap
        [ 94,  82,  67],   # shopify
        [nan, nan, nan],   # spoonacular    (not run)
        [nan,  62, nan],   # stripe         (docs/mutated: crash)
        [nan, nan,  64],   # zulip          (docs/nodocs: crash)
    ], dtype=float),
    'Qwen3-Coder-Next-Base': np.array([
        [ 92, nan, nan],   # alphavantage   (docs only; nodocs/mutated: no server.py)
        [ 64, nan, nan],   # confluence     (docs only)
        [  6, nan, nan],   # ebay_buy       (docs only)
        [ 45, nan, nan],   # ebay_commerce  (docs only)
        [nan,   0, nan],   # ebay_sell      (nodocs only; docs/mutated: no server.py)
        [nan, nan, nan],   # github         (all: no server.py)
        [nan, nan, nan],   # jira           (all: no server.py)
        [  0, nan,   0],   # mastodon       (docs/mutated both 0%; nodocs: no server.py)
        [nan,   0, nan],   # notion         (nodocs only; docs/mutated: no server.py)
        [nan, nan, nan],   # openweathermap (all: no server.py)
        [nan,   0,   0],   # shopify        (nodocs/mutated both 0%; docs: no server.py)
        [nan,  60, nan],   # spoonacular    (nodocs only)
        [nan,  56, nan],   # stripe         (nodocs only; docs/mutated: no server.py)
        [nan, nan,   0],   # zulip          (mutated only; docs/nodocs: no server.py)
    ], dtype=float),
    'Haiku 4.5': np.array([
        [nan, nan, nan],   # alphavantage   (rate-limited; shared key exhausted)
        [ 80,  33,  33],   # confluence
        [ 80,  67, 100],   # ebay_buy
        [ 30,  10,  50],   # ebay_commerce
        [ 17,   9,  36],   # ebay_sell
        [ 95,  90,  86],   # github
        [ 62,   7,  64],   # jira
        [ 93,  40,  86],   # mastodon
        [ 56,   5,  50],   # notion
        [ 95,  65,  60],   # openweathermap
        [ 93,  75,  94],   # shopify
        [  0,  79,  86],   # spoonacular    (docs=0% confirmed Jun 17 — server covers no tasks)
        [ 57,  75,  86],   # stripe
        [ 55,  36,  26],   # zulip
    ], dtype=float),
}

# ── Tier definitions ──────────────────────────────────────────────────────────
TIERS = {
    'Frontier': ['GPT-5.2', 'GPT-5.4', 'Sonnet 4.6'],
    'Mid':      ['Haiku 4.5', 'Gemini 3.1 Pro', 'Qwen3-Coder-Next'],
    'Base':     ['GPT-5.4-mini', 'Qwen3-Coder-Next-Base'],
}
TIER_COLORS = {'Frontier': NAVY, 'Mid': TEAL, 'Base': '#94A3B8'}

# GPT-5.4-mini full 14-API data (no alphavantage)
GPT54MINI_FULL = np.array([
    [nan, nan, nan],  # alphavantage  (not run)
    [ 33,  80,  43],  # confluence
    [  0,   0,  82],  # ebay_buy      (docs/nodocs collapse; mutated=82% 9/11 scoreable)
    [  0,   0,   0],  # ebay_commerce
    [  7,   8,   8],  # ebay_sell
    [ 38,  32,  30],  # github
    [  0,   0,  25],  # jira          (mutated N=4, treat with caution)
    [ 57,  79,  73],  # mastodon
    [ 60,   0,  17],  # notion        (docs=60%; nodocs collapse; mutated ENVIRONMENT-dominated)
    [100, 100, 100],  # openweathermap
    [ 62,   0,   0],  # shopify
    [ 94,  82, 100],  # spoonacular   (mutated N=1, treat with caution)
    [ 14,   0,  19],  # stripe        (nodocs: startup crash)
    [ 40,  14,  29],  # zulip
], dtype=float)

MODEL_DATA_FULL['GPT-5.4-mini'] = GPT54MINI_FULL

# ── SYNTH data for all models ─────────────────────────────────────────────────
# Rows indexed in DATASETS order: Alphavantage, Confluence, eBay Buy, eBay Commerce,
#   eBay Sell, GitHub, Jira, Mastodon, Notion, OpenWeatherMap, Shopify, Spoonacular,
#   Stripe, Zulip
# Columns: [docs, nodocs, mutated]
# Source: RESULTS.md parentheticals, e.g. "38% (35%)" → SYNTH=35
SYNTH_DATA_FULL = {
    'GPT-5.2': np.array([
        [ 84,  89,  89],   # alphavantage
        [ 95,  95,  95],   # confluence
        [ 88,  94,  88],   # ebay_buy
        [100,  85,  54],   # ebay_commerce
        [ 43,  50,  43],   # ebay_sell
        [ 61,  87,  61],   # github
        [ 56,  44,  56],   # jira
        [ 93, 100, 100],   # mastodon
        [ 91, 100, 100],   # notion
        [100,  83, 100],   # openweathermap
        [ 89,  94,  61],   # shopify
        [ 75,  75,  75],   # spoonacular
        [ 77,  68,  73],   # stripe
        [ 84,  48,  64],   # zulip
    ], dtype=float),

    'GPT-5.4': np.array([
        [ 95,  89,  89],   # alphavantage
        [ 76,  89,  89],   # confluence
        [ 71,  88, 100],   # ebay_buy
        [ 92,  38,  77],   # ebay_commerce
        [ 29,  50,  57],   # ebay_sell
        [ 57,  91,  65],   # github
        [ 56,  62,  62],   # jira
        [ 92,  92,  93],   # mastodon
        [ 61, 100, nan],   # notion (mutated: no server.py)
        [100,  96, 100],   # openweathermap
        [ 87,  93,  56],   # shopify
        [ 88,  88,  88],   # spoonacular
        [ 48,  73,  27],   # stripe
        [ 88,  88,  76],   # zulip
    ], dtype=float),

    'Sonnet 4.6': np.array([
        [ 95,  89,  84],   # alphavantage (mutated only valid for rate; others partial)
        [nan, nan, nan],   # confluence (docs: no server.py; nodocs/mutated: SYNTH not extracted)
        [nan, nan,  29],   # ebay_buy (docs: no server.py; nodocs: SYNTH not extracted; mutated=29%)
        [100, nan, nan],   # ebay_commerce (nodocs: crash; mutated: not run)
        [nan, nan, nan],   # ebay_sell
        [ 91, 100, 100],   # github
        [nan, nan, nan],   # jira (SYNTH not extracted)
        [nan, nan, nan],   # mastodon (docs/nodocs: crash; mutated: SYNTH not extracted)
        [nan, nan, nan],   # notion (SYNTH not extracted)
        [nan, nan, nan],   # openweathermap (crash docs/mutated; nodocs: not extracted)
        [nan, nan, nan],   # shopify (nodocs: crash; SYNTH not extracted)
        [ 94,  89,  94],   # spoonacular (docs=94%, nodocs server crashed but synth ran; mutated=94%)
        [ 86, 100, 100],   # stripe
        [100, nan, nan],   # zulip (nodocs: degenerate; mutated: stream error)
    ], dtype=float),

    'Haiku 4.5': np.array([
        [nan, nan, nan],   # alphavantage (rate-limited)
        [ 86,  15,  32],   # confluence
        [ 94,  76,  94],   # ebay_buy
        [ 46,  31,  69],   # ebay_commerce
        [ 29,  29,  50],   # ebay_sell
        [ 96,  87,  86],   # github
        [ 67,  13,  69],   # jira
        [ 93,  33,  87],   # mastodon
        [ 82,   0,  67],   # notion
        [ 96,  65,  61],   # openweathermap
        [ 94,  83,  94],   # shopify
        [  0,  82,  76],   # spoonacular (docs: pending → 0 placeholder)
        [ 73,  82,  95],   # stripe
        [ 61,  40,  29],   # zulip
    ], dtype=float),

    'Gemini 3.1 Pro': np.array([
        [nan, nan, nan],   # alphavantage (not extracted from RESULTS.md)
        [nan, nan, nan],   # confluence (docs: 0 tools → nan)
        [nan, nan, nan],   # ebay_buy (mutated: 0 tools → nan)
        [nan, nan, nan],   # ebay_commerce
        [nan, nan, nan],   # ebay_sell
        [nan, nan, nan],   # github
        [nan, nan, nan],   # jira
        [nan, nan, nan],   # mastodon
        [nan, nan, nan],   # notion
        [nan, nan, nan],   # openweathermap
        [nan, nan, nan],   # shopify
        [nan, nan, nan],   # spoonacular
        [nan, nan, nan],   # stripe
        [nan, nan, nan],   # zulip
    ], dtype=float),

    'Qwen3-Coder-Next': np.array([
        [nan, nan, nan],   # alphavantage (not run)
        [ 43,  21,  38],   # confluence
        [  7,  76,   6],   # ebay_buy
        [ 92, nan,  31],   # ebay_commerce (nodocs: crash)
        [ 71, nan, nan],   # ebay_sell (nodocs/mutated: crash)
        [ 52,  52,  57],   # github
        [ 69, nan,  56],   # jira (nodocs: crash)
        [nan,  73,  60],   # mastodon
        [ 82,   0, nan],   # notion (mutated: crash)
        [100,  78, 100],   # openweathermap
        [nan,  83,  72],   # shopify (docs: crash)
        [nan, nan, nan],   # spoonacular (not run)
        [nan,  73, nan],   # stripe (docs/mutated: crash)
        [nan, nan,  80],   # zulip (docs/nodocs: crash)
    ], dtype=float),

    'Qwen3-Coder-Next-Base': np.array([
        [ 95, nan, nan],   # alphavantage (docs only)
        [ 81, nan, nan],   # confluence (docs only)
        [  6, nan, nan],   # ebay_buy (docs only)
        [ 46, nan, nan],   # ebay_commerce (docs only)
        [nan,   0, nan],   # ebay_sell (nodocs only)
        [nan, nan, nan],   # github (all: no server.py)
        [nan, nan, nan],   # jira (all: no server.py)
        [  0, nan,   0],   # mastodon
        [nan,   0, nan],   # notion (nodocs only)
        [nan, nan, nan],   # openweathermap (all: no server.py)
        [nan,   0,   0],   # shopify
        [nan,  29, nan],   # spoonacular (nodocs only)
        [nan,  68, nan],   # stripe (nodocs only)
        [nan, nan,   0],   # zulip (mutated only)
    ], dtype=float),

    'GPT-5.4-mini': np.array([
        [nan, nan, nan],   # alphavantage (not run)
        [ 17,  95,  69],   # confluence
        [ 10,   0,  88],   # ebay_buy (mutated=88% synth)
        [  0,   8,   0],   # ebay_commerce
        [  7,  14,  14],   # ebay_sell
        [ 35,  26,  35],   # github
        [  6,   0,  11],   # jira
        [ 60,  80,  73],   # mastodon
        [ 73,   0,  11],   # notion (docs=73%; nodocs=0%; mutated=11%)
        [100,  87, 100],   # openweathermap
        [ 67,   0,   0],   # shopify
        [ 94,  88,  41],   # spoonacular
        [ 14, nan,  23],   # stripe (nodocs: crash)
        [ 48,  24,  40],   # zulip
    ], dtype=float),
}


def tier_avg(tier_name, cond_idx=None):
    """Return per-dataset nanmean across models in a tier.
    If cond_idx is None, returns shape (14, 3); else shape (14,)."""
    arrays = [MODEL_DATA_FULL[m] for m in TIERS[tier_name]
              if m in MODEL_DATA_FULL]
    stacked = np.stack(arrays, axis=0)  # (n_models, 14, 3)
    avg = np.nanmean(stacked, axis=0)   # (14, 3)
    if cond_idx is not None:
        return avg[:, cond_idx]
    return avg


def tier_best(tier_name, cond_idx=None):
    """Return per-dataset nanmax across models in a tier."""
    arrays = [MODEL_DATA_FULL[m] for m in TIERS[tier_name]
              if m in MODEL_DATA_FULL]
    stacked = np.stack(arrays, axis=0)
    best = np.nanmax(stacked, axis=0)
    if cond_idx is not None:
        return best[:, cond_idx]
    return best


# ── Helpers ───────────────────────────────────────────────────────────────────
def _spine_clean(ax, keep=('bottom', 'left')):
    for sp in ax.spines:
        ax.spines[sp].set_visible(sp in keep)
        if sp in keep:
            ax.spines[sp].set_color('#CCCCCC')


def _save(fig, stem):
    fig.savefig(f'{stem}.pdf', bbox_inches='tight', dpi=300)
    fig.savefig(f'{stem}.png', bbox_inches='tight', dpi=300)
    print(f'  saved {stem}.pdf / .png')


# ══════════════════════════════════════════════════════════════════════════════
# Figure — Tier Grouped Bar Chart (benchmark-style primary results)
# ══════════════════════════════════════════════════════════════════════════════
def fig_tier_bars():
    TEXT = '#1A1A1A'
    SUB  = '#555555'

    tier_names = ['Frontier', 'Mid', 'Base']
    tier_labels = ['Frontier\n(Sonnet 4.6, GPT-5.4, GPT-5.2)',
                   'Mid\n(Haiku 4.5, Gemini 3.1 Pro, Qwen3-Next)',
                   'Base\n(GPT-5.4-mini, Qwen3-Next-Base)']

    # Sort APIs by frontier docs avg descending
    frontier_docs = tier_avg('Frontier', cond_idx=0)
    order = np.argsort(frontier_docs)[::-1]
    ds_sorted = [DATASETS[i] for i in order]

    # Two-panel figure: docs (left), nodocs (right)
    fig, axes = plt.subplots(1, 2, figsize=(14.0, 5.5), sharey=False)
    fig.patch.set_facecolor('white')

    cond_indices = [0, 1]
    cond_titles  = ['With documentation', 'Without documentation (no-docs)']

    bar_w   = 0.22
    gap     = 0.05
    group_w = len(tier_names) * bar_w + (len(tier_names) - 1) * gap
    spacing = 0.18
    xs = np.arange(len(ds_sorted)) * (group_w + spacing)

    for ax, ci, ctitle in zip(axes, cond_indices, cond_titles):
        ax.set_facecolor('white')

        for ti, tname in enumerate(tier_names):
            avgs = tier_avg(tname, cond_idx=ci)[order]
            bests = tier_best(tname, cond_idx=ci)[order]
            x_bars = xs + ti * (bar_w + gap)
            color  = TIER_COLORS[tname]

            bars = ax.bar(x_bars, avgs, bar_w,
                          color=color, alpha=0.85, zorder=3,
                          label=tier_labels[ti])

            # Best marker as horizontal tick above bar
            for xb, avg, best in zip(x_bars, avgs, bests):
                if not np.isnan(best) and not np.isnan(avg):
                    ax.plot([xb - bar_w * 0.35, xb + bar_w * 0.35],
                            [best, best], color=color, lw=1.5, zorder=4)

            # Value labels on top of bars (frontier only, to avoid clutter)
            if tname == 'Frontier':
                for xb, avg in zip(x_bars, avgs):
                    if not np.isnan(avg):
                        ax.text(xb, avg + 1.5, f'{avg:.0f}',
                                ha='center', va='bottom',
                                fontsize=7, color=color, fontweight='bold')

        ax.axhline(50, color='#EEEEEE', lw=1.0, zorder=0)
        ax.set_xticks(xs + group_w / 2 - bar_w / 2)
        ax.set_xticklabels(ds_sorted, rotation=40, ha='right',
                           fontsize=9, color=TEXT)
        ax.set_ylabel('Agent pass rate (%)')
        ax.set_ylim(0, 115)
        ax.set_title(ctitle, fontsize=10, color=SUB, pad=6)
        ax.yaxis.grid(True, color='#F0F0F0', lw=0.7)
        ax.xaxis.grid(False)
        _spine_clean(ax, keep=('left',))
        ax.tick_params(colors=SUB, length=0)

    # Shared legend below
    handles = [mpatches.Patch(color=TIER_COLORS[t], alpha=0.85, label=tier_labels[i])
               for i, t in enumerate(tier_names)]
    handles.append(plt.Line2D([0], [0], color='#555555', lw=1.5,
                               label='Tier best (tick)'))
    fig.legend(handles=handles, loc='lower center', ncol=4,
               fontsize=9, frameon=False, bbox_to_anchor=(0.5, -0.08))
    fig.tight_layout()
    _save(fig, 'fig_tier_bars')
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# Figure 1 — Primary Results Heatmap
# ══════════════════════════════════════════════════════════════════════════════
def fig1_primary_heatmap():
    # Sort rows by mean PASS descending
    means = np.nanmean(CURRENT, axis=1)
    order = np.argsort(means)[::-1]
    cur   = CURRENT[order]
    syn   = SYNTH[order]
    dsets = [DATASETS[i] for i in order]

    N    = len(dsets)
    TEXT = '#1A1A1A'
    SUB  = '#555555'

    fig, ax = plt.subplots(figsize=(8.5, 7.5))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    for ri, dataset in enumerate(dsets):
        for ci in range(3):
            val  = cur[ri, ci]
            sval = syn[ri, ci]
            y = N - 1 - ri
            x = ci

            if np.isnan(val):
                fc       = '#D4D8DE'
                main_str = '—'
                sub_str  = ''
                tc       = '#888888'
            else:
                fc = HMAP_CMAP(val / 100)
                main_str = f'{val:.0f}%'
                sub_str  = f'synth {sval:.0f}%' if not np.isnan(sval) else ''
                r, g, b, _ = fc
                lum = 0.299*r + 0.587*g + 0.114*b
                tc  = 'white' if lum < 0.45 else TEXT

            ax.add_patch(mpatches.Rectangle((x, y), 1, 1,
                         fc=fc, ec='white', lw=2.5, zorder=3))
            y_main = y + 0.56 if sub_str else y + 0.5
            ax.text(x + 0.5, y_main, main_str,
                    ha='center', va='center',
                    fontsize=12, fontweight='bold', color=tc, zorder=4)
            if sub_str:
                sub_tc = tc if lum < 0.45 else SUB
                ax.text(x + 0.5, y + 0.28, sub_str,
                        ha='center', va='center',
                        fontsize=8.5, color=sub_tc, alpha=0.85, zorder=4)

    ax.set_xlim(0, 3)
    ax.set_ylim(0, N)
    ax.set_xticks([0.5, 1.5, 2.5])
    ax.set_xticklabels(COND_LABELS, fontsize=12, fontweight='bold', color=TEXT)
    ax.set_yticks([N - 1 - i + 0.5 for i in range(N)])
    ax.set_yticklabels(dsets, fontsize=11, color=TEXT)
    ax.tick_params(length=0)
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    for sp in ax.spines.values():
        sp.set_visible(False)

    ax.set_title('Pass rate (large) + server synthesis quality (small)',
                 fontsize=12, color=SUB, pad=36, style='italic')

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=HMAP_CMAP, norm=plt.Normalize(0, 100))
    sm.set_array([])
    cb = fig.colorbar(sm, ax=ax, fraction=0.025, pad=0.02)
    cb.set_ticks([0, 25, 50, 75, 100])
    cb.ax.tick_params(labelsize=10)
    cb.outline.set_visible(False)

    fig.tight_layout()
    _save(fig, 'fig1_primary_heatmap')
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# Figure 2 — Condition Slope Chart (docs → nodocs → mutated)
# ══════════════════════════════════════════════════════════════════════════════
def fig2_condition_slopes():
    TEXT = '#1A1A1A'
    SUB  = '#555555'

    # Alphavantage nodocs/mutated not evaluated
    data = CURRENT.copy()
    data[0, 1] = np.nan
    data[0, 2] = np.nan

    # APIs to annotate directly (notable position changes or persistent floor)
    ANNOTATE = {'eBay Sell', 'Jira', 'GitHub', 'Mastodon', 'OpenWeatherMap', 'Notion'}
    # Annotation offsets: (dx, dy) in data units — spread colliding 100% labels
    OFFSETS = {
        'eBay Sell':      (-0.22,  -7),
        'Jira':           ( 0.22,  -7),
        'GitHub':         ( 0.22,   3),
        'Notion':         ( 0.30,   5),    # pull right+up to clear Mastodon
        'Mastodon':       ( 0.22,  -8),    # pull down
        'OpenWeatherMap': (-0.28,   3),    # pull left
    }

    fig, ax = plt.subplots(figsize=(6.5, 6.0))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    # Track (ci, rank, val, name) for annotation
    positions = {}   # (ci, name) -> (x, y)

    for ci in range(3):
        vals  = data[:, ci]
        valid = sorted([(v, di) for di, v in enumerate(vals) if not np.isnan(v)])
        n     = len(valid)
        for rank, (val, di) in enumerate(valid):
            xoff = (rank / max(n - 1, 1) - 0.5) * 0.50
            name = DATASETS[di]
            color = API_CAT_COLOR[name]
            alpha = 0.9
            ax.scatter(ci + xoff, val,
                       color=color, s=72, zorder=4, alpha=alpha,
                       edgecolors='white', linewidths=0.7)
            positions[(ci, name)] = (ci + xoff, val)

    # Annotate selected APIs from their rightmost condition column
    for name in ANNOTATE:
        # Pick best column for annotation (prefer mutated, fall back to earlier)
        for ci in [2, 1, 0]:
            if (ci, name) in positions:
                x, y = positions[(ci, name)]
                dx, dy = OFFSETS.get(name, (0.15, 3))
                ax.annotate(
                    name,
                    xy=(x, y), xytext=(x + dx, y + dy),
                    fontsize=7.5, color=API_CAT_COLOR[name],
                    va='center',
                    arrowprops=dict(arrowstyle='-', color=API_CAT_COLOR[name],
                                    lw=0.6, shrinkA=3, shrinkB=2)
                    if abs(dx) > 0.1 or abs(dy) > 2 else None,
                )
                break

    # Per-tier median lines
    for tname in ['Frontier', 'Mid', 'Base']:
        tavg = tier_avg(tname)
        for ci in range(3):
            med = np.nanmedian(tavg[:, ci])
            ax.hlines(med, ci - 0.32, ci + 0.32,
                      color=TIER_COLORS[tname], lw=1.8, zorder=5, ls='--',
                      alpha=0.9)

    ax.axhline(50, color='#DDDDDD', lw=0.8, zorder=0)

    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(COND_LABELS, fontsize=10, fontweight='semibold', color=TEXT)
    ax.set_ylabel('Agent pass rate (%)')
    ax.set_ylim(10, 116)
    ax.set_xlim(-0.50, 2.50)
    ax.tick_params(colors=SUB, length=0, bottom=False)
    ax.grid(axis='y', color='#F0F0F0', linewidth=0.7)
    ax.grid(axis='x', visible=False)
    _spine_clean(ax, keep=('left',))

    # Compact legend: only category colors + tier medians — inside upper right
    cat_handles = [
        mpatches.Patch(color=CAT_NAVY,   label='Dev tools'),
        mpatches.Patch(color=CAT_TEAL,   label='Productivity'),
        mpatches.Patch(color=CAT_RED,    label='Commerce'),
        mpatches.Patch(color=CAT_VIOLET, label='Comms'),
        mpatches.Patch(color=CAT_AMBER,  label='Data APIs'),
    ]
    tier_handles = [plt.Line2D([0], [0], color=TIER_COLORS[t], lw=1.8,
                                ls='--', label=f'{t} median')
                    for t in ['Frontier', 'Mid', 'Base']]
    ax.legend(handles=cat_handles + tier_handles, frameon=True,
              loc='lower center', ncol=4, fontsize=8,
              labelspacing=0.3, handlelength=1.2, columnspacing=0.9,
              bbox_to_anchor=(0.5, -0.13))

    fig.tight_layout()
    fig.subplots_adjust(bottom=0.18)
    _save(fig, 'fig2_condition_slopes')
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# Figure 3 — Synthesis Model Comparison (3-panel)
# ══════════════════════════════════════════════════════════════════════════════
def fig3_model_comparison():
    TEXT = '#1A1A1A'
    SUB  = '#555555'

    fig, axes = plt.subplots(1, 3, figsize=(14.0, 5.2), sharey=True)
    fig.patch.set_facecolor('white')

    datasets_order = ['github', 'stripe', 'zulip']
    dataset_titles = {'github': 'GitHub', 'stripe': 'Stripe', 'zulip': 'Zulip'}
    models = ['GPT-5.4-mini', 'Qwen3-Coder-Next-Base', 'Qwen3-Coder-Next',
              'Gemini 3.1 Pro', 'GPT-5.2', 'GPT-5.4', 'Haiku 4.5', 'Sonnet 4.6']
    bar_w    = 0.14
    gap      = 0.03
    group_w  = 3 * bar_w + 2 * gap
    group_gap = 0.12
    alphas   = [0.92, 0.58, 0.35]   # docs / nodocs / mutated

    DISPLAY_NAMES = {
        'GPT-5.4-mini':          'GPT-5.4\nmini',
        'Qwen3-Coder-Next-Base': 'Qwen3\nNext-Base',
        'Qwen3-Coder-Next':      'Qwen3\nNext',
        'Gemini 3.1 Pro':        'Gemini\n3.1 Pro',
        'GPT-5.2':               'GPT-5.2',
        'GPT-5.4':               'GPT-5.4',
        'Haiku 4.5':             'Haiku 4.5',
        'Sonnet 4.6':            'Sonnet 4.6',
    }

    for ax, dset in zip(axes, datasets_order):
        ax.set_facecolor('white')
        data = MODEL_DATA[dset]

        for mi, model in enumerate(models):
            vals = data[model]
            x_center = mi * (group_w + group_gap)
            color = MODEL_COLORS[model]

            for ci in range(3):
                x = x_center + ci * (bar_w + gap)
                v = vals[ci]
                if np.isnan(v):
                    # Flat light bar — no hatch, no label, no noise
                    ax.bar(x, 6, width=bar_w, color='#DEDEDE',
                           edgecolor='white', lw=0.4, zorder=2)
                else:
                    ax.bar(x, v, width=bar_w, color=color,
                           alpha=alphas[ci], edgecolor='white', lw=0.4, zorder=3)
                    # Only annotate the Stripe GPT-5.4 docs collapse — meaningful outlier
                    if dset == 'stripe' and model == 'GPT-5.4' and ci == 0:
                        ax.text(x + bar_w / 2, v + 2, '!', ha='center', va='bottom',
                                fontsize=8, color=RED, fontweight='bold')

        x_ticks = [mi * (group_w + group_gap) + group_w / 2 - bar_w / 2
                   for mi in range(len(models))]
        ax.set_xticks(x_ticks)
        ax.set_xticklabels([DISPLAY_NAMES[m] for m in models],
                           fontsize=8, rotation=0, ha='center', color=TEXT)
        ax.set_title(dataset_titles[dset], fontsize=11,
                     fontstyle='italic', color=TEXT, pad=6)
        ax.set_ylim(0, 108)
        ax.yaxis.grid(True, color='#EBEBEB', lw=0.6, zorder=0)
        ax.set_axisbelow(True)
        _spine_clean(ax, keep=('left',))
        ax.tick_params(colors=SUB, length=0)

    axes[0].set_ylabel('PASS rate (%)', fontsize=10, color=SUB)

    # Legend below panels: model colours (row 1) + condition shading (row 2)
    model_patches = [mpatches.Patch(color=MODEL_COLORS[m], alpha=0.85,
                                    label=m) for m in models]
    cond_patches = [
        mpatches.Patch(color='#555555', alpha=0.92, label='With docs'),
        mpatches.Patch(color='#555555', alpha=0.58, label='No docs'),
        mpatches.Patch(color='#555555', alpha=0.35, label='Mutated params'),
        mpatches.Patch(color='#DEDEDE', label='No result'),
    ]
    fig.legend(handles=model_patches + cond_patches, fontsize=8.5,
               loc='lower center', ncol=12,
               bbox_to_anchor=(0.5, -0.06),
               frameon=False)

    fig.suptitle('Synthesis model comparison  (GitHub · Stripe · Zulip)',
                 fontsize=11, color=SUB, style='italic', y=1.01)
    fig.tight_layout()
    _save(fig, 'fig3_model_comparison')
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# Figure 4 — SYNTH vs CURRENT Scatter
# ══════════════════════════════════════════════════════════════════════════════
def fig4_synth_scatter():
    fig, ax = plt.subplots(figsize=(7.0, 7.0))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    # Condition → marker
    COND_MARKER = ['o', 's', '^']

    # Diagonal ± 10pp band — light, so it frames without dominating
    diag = np.array([0, 105])
    ax.fill_between(diag, diag - 10, diag + 10,
                    color='#F0F0F0', alpha=0.35, zorder=0)
    ax.plot(diag, diag, color=ANNOT, lw=1.0, linestyle='--',
            alpha=0.5, zorder=1, label='y = x')

    # Collect all points for Pearson r; colour by synthesis model
    xs_all, ys_all = [], []

    # Models to include — all with SYNTH data available
    _MODELS_SYNTH = [m for m in MODEL_DATA_FULL if m in SYNTH_DATA_FULL]

    rng = np.random.default_rng(42)

    for model in _MODELS_SYNTH:
        color  = MODEL_COLORS[model]
        pass_arr  = MODEL_DATA_FULL[model]   # (14, 3)
        synth_arr = SYNTH_DATA_FULL[model]   # (14, 3)

        for ri in range(len(DATASETS)):
            for ci, marker in enumerate(COND_MARKER):
                sx = synth_arr[ri, ci]
                cy = pass_arr[ri, ci]
                if np.isnan(sx) or np.isnan(cy):
                    continue
                xs_all.append(sx)
                ys_all.append(cy)
                # Small jitter to separate overlapping points
                jx = rng.uniform(-1.5, 1.5)
                jy = rng.uniform(-1.5, 1.5)
                ax.scatter(sx + jx, cy + jy, c=color, marker=marker,
                           s=58, alpha=0.60, zorder=3,
                           edgecolors='white', linewidths=0.5)

    # Pearson r across all models
    r, p = pearsonr(xs_all, ys_all)
    n = len(xs_all)
    print(f'SYNTH–PASS Pearson r = {r:.3f}  (p={p:.4f}, n={n})')
    # r annotation bottom-right, above condition legend
    ax.text(0.97, 0.04, f'Pearson $r$ = {r:.2f},  $n$ = {n}',
            transform=ax.transAxes, fontsize=9.5,
            va='bottom', ha='right', color=NAVY, fontweight='semibold')

    # OLS regression line
    xs_np, ys_np = np.array(xs_all), np.array(ys_all)
    m_ols, b_ols = np.polyfit(xs_np, ys_np, 1)
    x_fit = np.array([0, 105])
    ax.plot(x_fit, m_ols * x_fit + b_ols, color=NAVY, lw=1.2,
            linestyle='-', alpha=0.35, zorder=2)

    ax.set_xlim(0, 105)
    ax.set_ylim(0, 105)
    ax.set_xlabel('SYNTH — server tool coverage (%)')
    ax.set_ylabel('PASS — agent task success (%)')
    _spine_clean(ax)

    # Condition legend (markers) — compact, upper right inside plot
    cond_handles = [
        plt.scatter([], [], marker=m, c='#555555', s=40, label=l)
        for m, l in zip(COND_MARKER, COND_LABELS)
    ]
    leg1 = ax.legend(handles=cond_handles, title='Condition', title_fontsize=8.5,
                     fontsize=8, loc='upper right',
                     framealpha=0.92, edgecolor='#CCCCCC',
                     handletextpad=0.4, labelspacing=0.3)
    ax.add_artist(leg1)

    # Model legend — below the plot as a single horizontal strip
    model_handles = [
        mpatches.Patch(color=MODEL_COLORS[m], alpha=0.82, label=m)
        for m in _MODELS_SYNTH
    ]
    fig.legend(handles=model_handles, title='Synthesis model', title_fontsize=8.5,
               fontsize=8, loc='lower center', ncol=4,
               frameon=True, framealpha=0.92, edgecolor='#CCCCCC',
               bbox_to_anchor=(0.5, -0.13),
               handlelength=1.0, handletextpad=0.4, columnspacing=1.0)

    fig.tight_layout()
    fig.subplots_adjust(bottom=0.18)
    _save(fig, 'fig4_synth_scatter')
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# Figure 5 — Full Model Comparison Heatmap (14 datasets × 5 models × 3 conditions)
# ══════════════════════════════════════════════════════════════════════════════
def fig5_model_heatmap():
    """3-panel heatmap: docs | nodocs | mutated, rows=datasets, cols=models."""
    fig, axes = plt.subplots(1, 3, figsize=(16.0, 8.0),
                             gridspec_kw={'wspace': 0.08})
    fig.patch.set_facecolor('white')

    nrows = len(DATASETS)
    ncols = len(MODELS_FULL)

    # Build array: [condition][dataset][model]
    data = np.zeros((3, nrows, ncols))
    for mi, model in enumerate(MODELS_FULL):
        arr = MODEL_DATA_FULL[model]   # shape (14, 3)
        for ci in range(3):
            data[ci, :, mi] = arr[:, ci]

    # Sort rows by GPT-5.2 docs descending (same order as fig1)
    order = np.argsort(MODEL_DATA_FULL['GPT-5.2'][:, 0])[::-1]
    dsets_sorted = [DATASETS[i] for i in order]

    for ci, (ax, cond_label) in enumerate(zip(axes, COND_LABELS)):
        ax.set_facecolor('white')
        mat = data[ci][order]   # (14, 5)

        im = ax.imshow(mat, cmap=HMAP_CMAP, norm=plt.Normalize(0, 100),
                       aspect='auto', origin='upper',
                       extent=[-0.5, ncols - 0.5, nrows - 0.5, -0.5])

        # Cell annotations
        for ri in range(nrows):
            for mi in range(ncols):
                v = mat[ri, mi]
                if np.isnan(v):
                    ax.text(mi, ri, 'n/a', ha='center', va='center',
                            fontsize=6.5, color='#AAAAAA', fontstyle='italic')
                else:
                    tc = 'white' if v < 45 or v > 85 else '#1A1A1A'
                    ax.text(mi, ri, f'{v:.0f}', ha='center', va='center',
                            fontsize=8, color=tc,
                            fontweight='bold' if v == np.nanmax(mat[ri]) else 'normal')

        # Grid
        for x in np.arange(-0.5, ncols, 1):
            ax.axvline(x, color='white', lw=1.2)
        for y in np.arange(-0.5, nrows, 1):
            ax.axhline(y, color='white', lw=1.2)

        ax.set_xticks(range(ncols))
        ax.set_xticklabels(MODELS_FULL, fontsize=8, rotation=30, ha='right')
        ax.tick_params(length=0)

        if ci == 0:
            ax.set_yticks(range(nrows))
            ax.set_yticklabels(dsets_sorted, fontsize=9)
        else:
            ax.set_yticks([])

        ax.set_title(cond_label, fontsize=10, fontweight='semibold', pad=6)

    # Shared colorbar
    cbar = fig.colorbar(im, ax=axes, fraction=0.015, pad=0.02, shrink=0.85)
    cbar.set_label('PASS rate (%)', fontsize=9, color=ANNOT)
    cbar.ax.tick_params(labelsize=8)

    fig.suptitle('PASS rate by synthesis model, dataset, and condition',
                 fontsize=12, color='#555555', style='italic', y=1.01)

    # Footnote
    fig.text(0.5, -0.02,
             'n/a = broken synth (no server.py, startup crash) or condition not run. '
             'Bold = highest PASS in row.',
             ha='center', fontsize=8, color=ANNOT)

    fig.tight_layout()
    _save(fig, 'fig5_model_heatmap')
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# Figure 6 — Mutation Sensitivity (docs → mutated delta) + Adherence
# ══════════════════════════════════════════════════════════════════════════════
def fig6_mutation_sensitivity():
    """
    Heatmap: interface adherence rate (% of renamed params adopted) per API × model.
    APIs sorted by GPT-5.2 ΔPASS (most hurt at top); models ordered base→frontier.
    ΔPASS value annotated on right margin for reference.

    Message: parametric gravity — well-known APIs (GitHub, Stripe) hit 0% across all
    models; GPT-5.4 reads mutated docs most faithfully for unfamiliar APIs.
    """
    # ── Adherence data (interface %) per model per API ─────────────────────────
    # Source: RESULTS.md mutation adherence tables. nan = not measured.
    MODELS_ADH = ['GPT-5.4-mini', 'Qwen3-Next', 'Gem~3.1~Pro',
                  'Haiku~4.5', 'GPT-5.2', 'GPT-5.4', 'Sonnet~4.6']
    MODELS_ADH_LABELS = ['GPT-5.4-mini', 'Qwen3-Next', 'Gem 3.1 Pro',
                         'Haiku 4.5', 'GPT-5.2', 'GPT-5.4', 'Sonnet 4.6']

    # Rows = API order defined below, cols = MODELS_ADH order
    API_LABELS = ['Alphavantage', 'Confluence', 'eBay Buy', 'eBay Commerce', 'eBay Sell',
                  'GitHub', 'Jira', 'Mastodon', 'Notion', 'OpenWeatherMap',
                  'Shopify', 'Spoonacular', 'Stripe', 'Zulip']

    IFACE = {
        # Interface adherence % (iface level: renamed param adopted in Python signature)
        # Source: RESULTS.md mutation adherence tables. nan = not measured (no server produced
        # or model not run on that API in mutated condition).
        # Cols: Alph  Conf  EBuy  EBCom EBSel  GH   Jira  Mast  Noti  OWM   Shop  Spon  Stri  Zulip
        'GPT-5.4-mini': [nan,   60,    0,  100,   40,    0,   80,  100,   40,   60,    0,   25,   20,   17],
        # Qwen3-Next: full adherence data from synthesized code (measurable even when eval crashed)
        'Qwen3-Next':   [100,  100,   80,  100,   20,   60,  100,  100,    0,   40,    0,  nan,   60,  100],
        'Gem 3.1 Pro':  [  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,   14,    0,    0],
        'Haiku 4.5':    [100,   60,   20,  100,   40,   20,   80,    0,   80,   80,   20,   75,   20,   50],
        'GPT-5.2':      [100,   80,   60,   40,   60,    0,   40,  100,   80,   80,   20,   75,   20,   17],
        'GPT-5.4':      [ 80,  100,   60,  100,   80,    0,   60,  100,  nan,   60,   20,   75,    0,   17],
        # Sonnet 4.6: zulip=nan (no server produced); eBay Buy=60; Spoonacular=25
        'Sonnet 4.6':   [100,  100,   60,  nan,  nan,    0,   20,  100,   60,  nan,  nan,   25,    0,  nan],
    }

    # ΔPASS (mutated − docs, GPT-5.2 reference) — for sorting and right-margin annotation
    DPASS = {
        'Alphavantage':   2,   'Confluence':  -1,  'eBay Buy':    7,
        'eBay Commerce': -45,  'eBay Sell':    5,  'GitHub':     14,
        'Jira':           0,   'Mastodon':     0,  'Notion':     22,
        'OpenWeatherMap': 0,   'Shopify':    -25,  'Spoonacular':-22,
        'Stripe':        -15,  'Zulip':      -18,
    }

    # Sort APIs: most hurt by mutation at top
    sorted_apis = sorted(API_LABELS, key=lambda a: DPASS[a])
    n_api = len(sorted_apis)
    n_mod = len(MODELS_ADH_LABELS)
    api_idx = {a: i for i, a in enumerate(API_LABELS)}

    heat = np.full((n_api, n_mod), np.nan)
    for mi, model in enumerate(MODELS_ADH_LABELS):
        for ai, api in enumerate(sorted_apis):
            heat[ai, mi] = IFACE[model][api_idx[api]]

    # ── Figure ─────────────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 5.8))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    from matplotlib.colors import LinearSegmentedColormap
    adh_cmap = LinearSegmentedColormap.from_list(
        'adh', ['#F7F7F7', '#FDE68A', '#F59E0B', '#92400E'], N=256)

    im = ax.imshow(heat, aspect='auto', cmap=adh_cmap, vmin=0, vmax=100,
                   interpolation='nearest')

    # Cell annotations
    for ai in range(n_api):
        for mi in range(n_mod):
            v = heat[ai, mi]
            if not np.isnan(v):
                textcolor = 'white' if v >= 72 else '#333333'
                ax.text(mi, ai, f'{int(v)}', ha='center', va='center',
                        fontsize=8.5, color=textcolor, fontweight='bold')
            else:
                ax.text(mi, ai, '—', ha='center', va='center',
                        fontsize=8, color='#BBBBBB')

    ax.set_xticks(range(n_mod))
    ax.set_xticklabels(MODELS_ADH_LABELS, rotation=30, ha='right', fontsize=9)
    ax.set_yticks(range(n_api))
    ax.set_yticklabels(sorted_apis, fontsize=9)
    ax.tick_params(axis='both', length=0)

    # ΔPASS margin annotation
    dpass_vals = [DPASS[a] for a in sorted_apis]
    ax2 = ax.twinx()
    ax2.set_ylim(ax.get_ylim())
    ax2.set_yticks(range(n_api))
    dpass_labels = [f'{v:+d} pp' for v in dpass_vals]
    ax2.set_yticklabels(dpass_labels, fontsize=8)
    ax2.tick_params(axis='y', length=0, labelcolor='#555555')
    ax2.set_ylabel('ΔPASS (mutated − docs, GPT-5.2)', fontsize=8.5, color='#555555', labelpad=8)

    # Tier separator lines (vertical dashed)
    for x in [1.5, 3.5]:
        ax.axvline(x, color='#888888', lw=1.0, ls='--', zorder=5)

    # Tier labels below x-axis
    for xpos, label in [(0.5, 'Base'), (2.5, 'Mid'), (5.0, 'Frontier')]:
        ax.text(xpos, n_api - 0.05, label, ha='center', va='bottom', fontsize=8,
                color='#666666', transform=ax.transData, style='italic')

    cbar = fig.colorbar(im, ax=ax2, fraction=0.03, pad=0.18, shrink=0.85)
    cbar.set_label('Interface adherence (%)', fontsize=8.5)
    cbar.ax.tick_params(labelsize=8)

    # No title — caption carries it

    fig.tight_layout()
    _save(fig, 'fig6_mutation_sensitivity')
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# Figure 7 — Documentation Effect Scatter (docs vs no-docs)
# ══════════════════════════════════════════════════════════════════════════════
def fig7_docs_effect():
    """
    Scatter: x = CURRENT(docs), y = CURRENT(nodocs).
    Points above the diagonal → nodocs >= docs (docs add noise or are redundant).
    Points below → docs help the agent.
    """
    fig, ax = plt.subplots(figsize=(7.5, 7.5))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    # API categories — shared palette
    CAT_COLOR = API_CAT_COLOR

    # Quadrant fills — very subtle
    ax.fill_between([0, 105], [0, 105], [105, 105],
                    color='#2A9D8F', alpha=0.04, zorder=0)   # no-docs ≥ docs
    ax.fill_between([0, 105], [0, 0], [0, 105],
                    color='#E76F51', alpha=0.04, zorder=0)   # docs ≥ no-docs

    # Diagonal
    diag = np.array([0, 105])
    ax.plot(diag, diag, color=ANNOT, lw=1.2, linestyle='--', alpha=0.7, zorder=1)

    # ± 5pp band
    ax.fill_between(diag, diag - 5, diag + 5,
                    color='#EEEEEE', alpha=0.5, zorder=0)

    # Quadrant labels
    ax.text(3, 103, r'No-docs $\geq$ docs', fontsize=8, color='#2A9D8F',
            fontstyle='italic', va='top')
    ax.text(78, 3, r'Docs $\geq$ no-docs', fontsize=8, color='#C0392B',
            fontstyle='italic', va='bottom')

    # Notable labels
    LABEL_APIS = {'GitHub', 'Jira', 'eBay Commerce', 'Notion', 'Zulip', 'eBay Buy',
                  'Spoonacular', 'eBay Sell'}
    OFFSETS = {
        'GitHub':       (3,  2),
        'Jira':         (3, -8),
        'eBay Commerce':(-3, 4),
        'Notion':       (3,  2),
        'Zulip':        (-3,-8),
        'eBay Buy':     (3,  2),
        'Spoonacular':  (3, -8),
        'eBay Sell':    (3,  2),
    }

    for ri, name in enumerate(DATASETS):
        xv = CURRENT[ri, 0]   # docs
        yv = CURRENT[ri, 1]   # nodocs
        if np.isnan(xv) or np.isnan(yv):
            continue
        color = CAT_COLOR[name]
        ax.scatter(xv, yv, c=color, s=80, zorder=3,
                   edgecolors='white', linewidths=0.6, alpha=0.88)
        if name in LABEL_APIS:
            dx, dy = OFFSETS.get(name, (3, 3))
            ax.annotate(name, xy=(xv, yv), xytext=(xv + dx, yv + dy),
                        fontsize=8, color=color,
                        arrowprops=dict(arrowstyle='->', color=color,
                                        lw=0.7, shrinkA=4)
                        if abs(dx) > 5 or abs(dy) > 5 else None)

    # Category legend — lower left, where the plot is empty (all APIs score > 40%)
    cat_handles = [
        mpatches.Patch(color=CAT_NAVY,   label='Dev tools'),
        mpatches.Patch(color=CAT_TEAL,   label='Productivity'),
        mpatches.Patch(color=CAT_RED,    label='Commerce'),
        mpatches.Patch(color=CAT_VIOLET, label='Comms'),
        mpatches.Patch(color=CAT_AMBER,  label='Data APIs'),
    ]
    ax.legend(handles=cat_handles, fontsize=8.5, title='API category',
              title_fontsize=9, loc='lower right',
              framealpha=0.9, edgecolor='#CCCCCC',
              handlelength=1.0, handletextpad=0.4, labelspacing=0.3)

    ax.set_xlim(0, 105)
    ax.set_ylim(0, 105)
    ax.set_xlabel('PASS — With docs (%)')
    ax.set_ylabel('PASS — No docs (%)')
    _spine_clean(ax)
    fig.tight_layout()
    _save(fig, 'fig7_docs_effect')
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# Figure 8 — API Complexity vs Agent Performance
# ══════════════════════════════════════════════════════════════════════════════
def fig8_api_complexity():
    """
    Scatter: x = number of endpoint doc files (log scale), y = mean CURRENT(docs).
    Marker size ∝ synthesis input tokens (doc context size).
    Tests whether API complexity (as seen by the synthesizer) predicts agent success.
    """
    # Endpoint doc file counts (from TASK.md)
    ENDPOINT_DOCS = {
        'Alphavantage':   9,
        'Confluence':    47,
        'eBay Buy':      28,
        'eBay Commerce': 48,
        'eBay Sell':    192,
        'GitHub':       181,
        'Jira':         101,
        'Mastodon':      35,
        'Notion':        94,
        'OpenWeatherMap': 5,
        'Shopify':       58,
        'Spoonacular':    7,
        'Stripe':       120,
        'Zulip':        165,
    }

    # Synthesis input tokens (from RESULTS.md synthesis cost table; GPT-5.2 docs run)
    # Missing entries use a rough estimate from endpoint count × avg token/file
    SYNTH_TOKENS = {
        'Alphavantage':   50_000,   # not listed, small API
        'Confluence':    200_000,   # not listed, medium
        'eBay Buy':      224_374,
        'eBay Commerce': 530_739,
        'eBay Sell':     198_711,
        'GitHub':      1_027_940,
        'Jira':        2_075_565,
        'Mastodon':      150_000,   # not listed, similar to confluence
        'Notion':        320_685,
        'OpenWeatherMap': 30_000,   # tiny
        'Shopify':     1_298_659,
        'Spoonacular':    30_000,   # tiny
        'Stripe':      2_423_904,
        'Zulip':       1_539_668,
    }

    COMMS_C = '#9333EA'
    CAT_COLOR = {
        'GitHub': NAVY, 'Jira': NAVY,
        'Confluence': TEAL, 'Notion': TEAL,
        'eBay Buy': RED, 'eBay Commerce': RED, 'eBay Sell': RED,
        'Shopify': RED, 'Stripe': RED,
        'Zulip': COMMS_C, 'Mastodon': COMMS_C,
        'Alphavantage': AMBER, 'OpenWeatherMap': AMBER, 'Spoonacular': AMBER,
    }

    fig, ax = plt.subplots(figsize=(8.5, 6.5))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    xs, ys, szs, colors, labels = [], [], [], [], []
    for name in DATASETS:
        ri = DATASETS.index(name)
        xv = ENDPOINT_DOCS[name]
        yv = float(CURRENT[ri, 0])        # docs CURRENT
        tok = SYNTH_TOKENS[name]
        sz = 40 + (tok / 2_423_904) * 280  # scale 40–320
        xs.append(xv); ys.append(yv); szs.append(sz)
        colors.append(CAT_COLOR[name]); labels.append(name)

    # Scatter
    sc = ax.scatter(xs, ys, s=szs, c=colors, alpha=0.78, zorder=3,
                    edgecolors='white', linewidths=0.8)

    # Correlation line (log-space x)
    log_xs = np.log10(xs)
    m, b = np.polyfit(log_xs, ys, 1)
    x_fit = np.logspace(np.log10(min(xs)) * 0.95, np.log10(max(xs)) * 1.02, 100)
    ax.plot(x_fit, np.polyval([m, b], np.log10(x_fit)),
            color=ANNOT, lw=1.2, linestyle='--', alpha=0.6, zorder=2)
    r, _ = pearsonr(log_xs, ys)
    ax.text(0.04, 0.06, f'Pearson $r$ = {r:.2f}  (log endpoint count vs PASS)',
            transform=ax.transAxes, fontsize=8.5, color=ANNOT, va='bottom')

    # Labels
    LABEL_ALL = set(DATASETS)
    for i, name in enumerate(labels):
        ax.annotate(name, xy=(xs[i], ys[i]),
                    xytext=(xs[i] * 1.08, ys[i] + 1.5),
                    fontsize=7.5, color=colors[i],
                    va='center')

    # Size legend (token scale)
    for label, tok in [('~30 K tokens', 30_000),
                       ('~500 K tokens', 500_000),
                       ('~2.4 M tokens', 2_423_904)]:
        sz = 40 + (tok / 2_423_904) * 280
        ax.scatter([], [], s=sz, c='#AAAAAA', alpha=0.6, label=label)
    ax.legend(title='Synthesis input\n(doc context size)',
              title_fontsize=8, fontsize=8, loc='lower left',
              framealpha=0.9, edgecolor='#CCCCCC')

    ax.set_xscale('log')
    ax.set_xlim(3, 350)
    ax.set_ylim(20, 115)
    ax.set_xlabel('Endpoint documentation files (log scale)', fontsize=10)
    ax.set_ylabel('PASS — With docs (%)', fontsize=10)
    ax.set_title('',  # no title — caption carries it; was:
                 fontsize=11, color='#555555', style='italic')
    ax.xaxis.grid(True, color='#EEEEEE', lw=0.7, which='both')
    ax.yaxis.grid(True, color='#EEEEEE', lw=0.7)
    ax.set_axisbelow(True)
    _spine_clean(ax)
    fig.tight_layout()
    _save(fig, 'fig8_api_complexity')
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# Figure 9 — Synthesis Model Capability vs Agent Performance
# ══════════════════════════════════════════════════════════════════════════════
def fig9_model_capability():
    """
    For each synthesis model, plot individual CURRENT scores for all
    (dataset, condition) pairs on the 3 core datasets (GitHub, Stripe, Zulip) —
    the only datasets where ALL 6 models have been evaluated.

    Using the same dataset population for every model is essential: other models
    include easy APIs (Mastodon 100%, OWM 95%) that inflate their distributions
    relative to GPT-5.4-mini which was only tested on harder datasets.

    Capability ordering (rough, based on publicly reported benchmarks):
      GPT-5.4-mini  <  Qwen3-Coder-Next-Base  <  Qwen3-Coder-Next  <  Gemini 3.1 Pro  <  GPT-5.2  <  GPT-5.4  <  Haiku 4.5  <  Sonnet 4.6
    """
    # Core datasets: the 3 evaluated for all models including GPT-5.4-mini
    CORE = ['GitHub', 'Stripe', 'Zulip']
    CORE_MARKERS = {'GitHub': 'o', 'Stripe': 's', 'Zulip': '^'}
    # Dataset colors — shared semantic palette, not model colors
    CORE_DS_COLORS = {
        'GitHub': CAT_NAVY,
        'Stripe': CAT_RED,
        'Zulip':  CAT_VIOLET,
    }

    # Raw [docs, nodocs, mutated] for each model × core dataset
    # Pull from MODEL_DATA_FULL (keyed by dataset name matching DATASETS list)
    _CORE_IDX = {d: DATASETS.index(d) for d in CORE}
    RAW = {
        'GPT-5.4-mini': {
            'GitHub': np.array([38., 32., 30.]),
            'Stripe': np.array([14.,  0., 19.]),
            'Zulip':  np.array([40., 14., 29.]),
        },
        **{
            model: {dset: MODEL_DATA_FULL[model][_CORE_IDX[dset]] for dset in CORE}
            for model in ['Qwen3-Coder-Next-Base', 'Qwen3-Coder-Next',
                          'Gemini 3.1 Pro', 'GPT-5.2',
                          'GPT-5.4', 'Haiku 4.5', 'Sonnet 4.6']
        },
    }

    ORDERED_MODELS = [
        'GPT-5.4-mini', 'Qwen3-Coder-Next-Base', 'Qwen3-Coder-Next',
        'Gemini 3.1 Pro', 'GPT-5.2', 'GPT-5.4', 'Haiku 4.5', 'Sonnet 4.6',
    ]
    MODEL_DISPLAY = {
        'GPT-5.4-mini':         'GPT-5.4\nmini',
        'Qwen3-Coder-Next-Base':'Qwen3\nNext-Base',
        'Qwen3-Coder-Next':     'Qwen3\nNext',
        'Gemini 3.1 Pro':       'Gemini\n3.1 Pro',
        'GPT-5.2':              'GPT-5.2',
        'GPT-5.4':              'GPT-5.4',
        'Haiku 4.5':            'Haiku\n4.5',
        'Sonnet 4.6':           'Sonnet\n4.6',
    }

    fig, ax = plt.subplots(figsize=(10.0, 5.5))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    rng = np.random.default_rng(42)
    xticks, xlabels = [], []

    for xi, model in enumerate(ORDERED_MODELS):
        # Collect all valid (dataset, condition) points
        all_pts = []
        pts_by_dset = {d: [] for d in CORE}
        for dset in CORE:
            for ci, v in enumerate(RAW[model][dset]):
                if not np.isnan(v):
                    all_pts.append(v)
                    pts_by_dset[dset].append(v)

        vals = np.array(all_pts)
        n = len(vals)

        BOX_FILL = '#E8E8E8'
        BOX_EDGE = '#888888'
        if n >= 2:
            ax.boxplot(vals, positions=[xi], widths=0.42,
                       patch_artist=True, notch=False,
                       boxprops=dict(facecolor=BOX_FILL, alpha=0.85, lw=1.0,
                                     edgecolor=BOX_EDGE),
                       medianprops=dict(color='#333333', lw=2.0),
                       whiskerprops=dict(color=BOX_EDGE, lw=0.9, linestyle='--'),
                       capprops=dict(color=BOX_EDGE, lw=1.0),
                       flierprops=dict(marker='', markersize=0))   # hide outliers; shown as jitter

        # Jittered scatter, shaped+colored by dataset (not model)
        for dset in CORE:
            dpts = np.array(pts_by_dset[dset])
            if len(dpts) == 0:
                continue
            j = rng.uniform(-0.14, 0.14, len(dpts))
            ax.scatter(xi + j, dpts,
                       c=CORE_DS_COLORS[dset], marker=CORE_MARKERS[dset],
                       s=52, alpha=0.85, zorder=4,
                       edgecolors='white', linewidths=0.6)

        # Mean annotation — above the box top (Q3 + 1.5×IQR whisker cap, or Q3 if n<4)
        if n > 0:
            mean_v = float(np.nanmean(vals))
            q3 = float(np.percentile(vals, 75))
            iqr = float(np.percentile(vals, 75) - np.percentile(vals, 25))
            whisker_top = min(float(np.nanmax(vals)), q3 + 1.5 * iqr)
            ax.text(xi, whisker_top + 3, f'{mean_v:.0f}%', ha='center', va='bottom',
                    fontsize=7.5, color='#555555', fontweight='semibold')


        xticks.append(xi)
        xlabels.append(MODEL_DISPLAY[model])

    # Reference lines
    ax.axhline(50, color=ANNOT, lw=0.8, linestyle='--', alpha=0.5)
    ax.axhline(80, color=ANNOT, lw=0.6, linestyle=':', alpha=0.35)
    ax.text(-0.52, 80.5, '80%', fontsize=7.5, color=ANNOT, va='bottom')
    ax.text(-0.52, 50.5, '50%', fontsize=7.5, color=ANNOT, va='bottom')

    # Dataset shape+color legend
    dset_handles = [
        plt.scatter([], [], marker=CORE_MARKERS[d], c=CORE_DS_COLORS[d], s=48, label=d)
        for d in CORE
    ]
    ax.legend(handles=dset_handles, title='Dataset', title_fontsize=8.5,
              fontsize=8.5, loc='upper left', framealpha=0.9, edgecolor='#CCCCCC')

    n_models = len(ORDERED_MODELS)

    # Capability tier arrow
    ax.annotate('', xy=(n_models - 0.5, -18), xytext=(-0.5, -18),
                xycoords=('data', 'data'),
                textcoords=('data', 'data'),
                arrowprops=dict(arrowstyle='->', color=ANNOT, lw=1.0),
                annotation_clip=False)
    ax.text((n_models - 1) / 2, -0.13, 'Increasing synthesis model capability (approximate)',
            ha='center', va='top', transform=ax.get_xaxis_transform(),
            fontsize=8.5, color=ANNOT, fontstyle='italic')

    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels, fontsize=9)
    ax.set_xlim(-0.6, n_models - 0.4)
    ax.set_ylim(-5, 115)
    ax.set_ylabel('PASS rate (%)')
    ax.yaxis.grid(True, color='#F0F0F0', lw=0.7)
    ax.xaxis.grid(False)
    ax.set_axisbelow(True)
    _spine_clean(ax, keep=('bottom', 'left'))
    fig.tight_layout()
    _save(fig, 'fig9_model_capability')
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# Figure 10 — Parametric Knowledge vs Context: docs/nodocs/mutated deltas by model
# ══════════════════════════════════════════════════════════════════════════════
def fig10_parametric_knowledge():
    """
    For each of the 3 core datasets (GitHub, Stripe, Zulip) show two deltas
    per synthesis model:
      - docs_delta  = CURRENT(nodocs) − CURRENT(docs)   [+ve → model knows API without docs]
      - mut_delta   = CURRENT(mutated) − CURRENT(docs)  [+ve → mutation hurts; −ve → immune]

    Also overlays mutation adherence rate as a third signal (how much the
    synthesis model actually adopted renamed params).
    """
    CORE = ['GitHub', 'Stripe', 'Zulip']
    MODELS = ['GPT-5.4-mini', 'Qwen3-Coder', 'Gemini 3.1 Pro', 'GPT-5.2', 'GPT-5.4', 'Sonnet 4.6']
    MODEL_DISPLAY = {
        'GPT-5.4-mini':   'GPT-5.4-mini',
        'Qwen3-Coder':          'Qwen3-Coder',
        'Gemini 3.1 Pro': 'Gemini 3.1 Pro',
        'GPT-5.2':        'GPT-5.2',
        'GPT-5.4':        'GPT-5.4',
        'Sonnet 4.6':     'Sonnet 4.6',
    }
    _COLORS = {
        'GPT-5.4-mini':   '#94A3B8',
        'Qwen3-Coder':          RED,
        'Gemini 3.1 Pro': CORAL,
        'GPT-5.2':        NAVY,
        'GPT-5.4':        TEAL,
        'Sonnet 4.6':     VIOLET,
    }

    # Raw docs/nodocs/mutated per model per core dataset
    RAW = {
        'GPT-5.4-mini': {'GitHub': [38., 32., 30.], 'Stripe': [14., 0., 19.], 'Zulip': [40., 14., 29.]},
        'Qwen3-Coder':        {'GitHub': [58., 60., 57.], 'Stripe': [nan, 62., nan], 'Zulip': [nan, nan, 64.]},
        'Gemini 3.1 Pro': {'GitHub': [78., 71., 36.], 'Stripe': [47., 50., 59.], 'Zulip': [76., 84., 62.]},
        'GPT-5.2':      {'GitHub': [62., 83., 76.], 'Stripe': [72., 62., 57.], 'Zulip': [80., 60., 62.]},
        'GPT-5.4':      {'GitHub': [58., 89., 73.], 'Stripe': [8.,  62., 12.], 'Zulip': [90., 85., 71.]},
        'Sonnet 4.6':   {'GitHub': [90., 100., 100.], 'Stripe': [77., 100., 100.], 'Zulip': [100., 43., nan]},
    }

    # Mutation adherence (iface %) per model per core dataset — GPT-5.2 & G3.1P from main matrix
    # Sonnet/GPT-5.4 all 0% on these APIs; Qwen3 from new data; mini assumed 0%
    ADHER = {
        'GPT-5.4-mini': {'GitHub': 0.,  'Stripe': 0.,  'Zulip': 0.},
        'Qwen3-Coder':        {'GitHub': 60., 'Stripe': 60., 'Zulip': 100.},
        'Gemini 3.1 Pro':{'GitHub': 0., 'Stripe': 0.,  'Zulip': 0.},
        'GPT-5.2':      {'GitHub': 0.,  'Stripe': 20., 'Zulip': 17.},
        'GPT-5.4':      {'GitHub': 0.,  'Stripe': 0.,  'Zulip': 0.},
        'Sonnet 4.6':   {'GitHub': 0.,  'Stripe': 0.,  'Zulip': nan},
    }

    fig, axes = plt.subplots(1, 3, figsize=(14.0, 5.5), sharey=False)
    fig.patch.set_facecolor('white')

    x = np.arange(len(MODELS))
    bar_w = 0.30
    gap   = 0.06

    for ai, (ax, dset) in enumerate(zip(axes, CORE)):
        ax.set_facecolor('white')
        ax.axhline(0, color='#AAAAAA', lw=0.9, zorder=2)

        docs_deltas, mut_deltas, adhers = [], [], []
        valid_mask_d, valid_mask_m = [], []

        for model in MODELS:
            d, n, m = RAW[model][dset]
            dd = (n - d) if not (np.isnan(n) or np.isnan(d)) else nan
            md = (m - d) if not (np.isnan(m) or np.isnan(d)) else nan
            docs_deltas.append(dd)
            mut_deltas.append(md)
            adhers.append(ADHER[model][dset])
            valid_mask_d.append(not np.isnan(dd))
            valid_mask_m.append(not np.isnan(md))

        for mi, model in enumerate(MODELS):
            color = _COLORS[model]
            xd = x[mi] - bar_w/2 - gap/2
            xm = x[mi] + bar_w/2 + gap/2

            # docs delta bar
            if valid_mask_d[mi]:
                dd = docs_deltas[mi]
                ax.bar(xd, dd, width=bar_w, color=color, alpha=0.85,
                       edgecolor='white', lw=0.5, zorder=3)
                ax.text(xd, dd + (2 if dd >= 0 else -3.5), f'{dd:+.0f}',
                        ha='center', va='bottom' if dd >= 0 else 'top',
                        fontsize=7, color=color)
            else:
                ax.bar(xd, 0, width=bar_w, color='#DDDDDD',
                       edgecolor='#AAAAAA', lw=0.5, hatch='///', zorder=3)

            # mutation delta bar (hatched for distinction)
            if valid_mask_m[mi]:
                md = mut_deltas[mi]
                ax.bar(xm, md, width=bar_w, color=color, alpha=0.45,
                       edgecolor=color, lw=0.8, zorder=3)
                ax.text(xm, md + (2 if md >= 0 else -3.5), f'{md:+.0f}',
                        ha='center', va='bottom' if md >= 0 else 'top',
                        fontsize=7, color=color, alpha=0.8)
            else:
                ax.bar(xm, 0, width=bar_w, color='#DDDDDD',
                       edgecolor='#AAAAAA', lw=0.5, hatch='///', zorder=3)

            # Adherence dot (on secondary y-axis line height)
            adh = adhers[mi]
            if not np.isnan(adh) and adh > 0:
                ax.scatter(x[mi], -38 + adh * 0.25, marker='D',
                           c=AMBER, s=32, zorder=5, edgecolors='white', lw=0.4)

        ax.set_xticks(x)
        ax.set_xticklabels([MODEL_DISPLAY[m] for m in MODELS],
                           fontsize=7.5, rotation=30, ha='right')
        ax.set_title(dset, fontsize=11, fontweight='bold', pad=6)
        ax.set_ylim(-65, 65)
        ax.set_yticks([-60, -40, -20, 0, 20, 40, 60])

        if ai == 0:
            ax.set_ylabel('Delta PASS (pp)', fontsize=10)
        else:
            ax.set_yticklabels([])

        # Zero label
        ax.text(-0.55, 1.5, '0', fontsize=7.5, color=ANNOT, va='bottom')

        ax.yaxis.grid(True, color='#EEEEEE', lw=0.7)
        ax.set_axisbelow(True)
        _spine_clean(ax, keep=('bottom', 'left'))

    # Legend
    legend_els = [
        mpatches.Patch(color='#555555', alpha=0.85, label='nodocs − docs  (solid)'),
        mpatches.Patch(color='#555555', alpha=0.40,
                       edgecolor='#555555', lw=0.8, label='mutated − docs  (faded)'),
        mpatches.Patch(facecolor='#DDDDDD', hatch='///', edgecolor='#AAAAAA',
                       label='no data'),
        plt.scatter([], [], marker='D', c=AMBER, s=32, label='Mutation adherence > 0%'),
    ]
    fig.legend(handles=legend_els, fontsize=8.5, loc='upper center',
               ncol=4, bbox_to_anchor=(0.5, 1.02),
               framealpha=0.9, edgecolor='#CCCCCC')

    fig.suptitle('Parametric knowledge vs context: documentation and mutation effects by model',
                 fontsize=11, color='#555555', style='italic', y=1.07)
    fig.tight_layout()
    _save(fig, 'fig10_parametric_knowledge')
    plt.close(fig)


# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print('Generating figures...')
    fig_tier_bars()
    fig1_primary_heatmap()
    fig4_synth_scatter()
    fig2_condition_slopes()
    fig3_model_comparison()
    fig5_model_heatmap()
    fig6_mutation_sensitivity()
    fig7_docs_effect()
    fig8_api_complexity()
    fig9_model_capability()
    fig10_parametric_knowledge()
    print('Done.')
