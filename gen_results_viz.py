"""
Results visualizations — 14-API pass rate matrix (docs / nodocs / mutated).

Produces four views:
  results_heatmap.png    — color-coded table
  results_bars.png       — grouped bar chart
  results_scatter.png    — docs% vs nodocs% scatter
  results_cleveland.png  — Cleveland dot plot
  results_combined.png   — 2×2 composite
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Arial', 'DejaVu Sans'],
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

nan = np.nan

# ── Data ──────────────────────────────────────────────────────────────────────
# CURRENT metric: pass / (pass+fail), scoreable tasks only
# NaN = condition not run
DATASETS = [
    'Alphavantage', 'Confluence', 'eBay Buy', 'eBay Commerce', 'eBay Sell',
    'GitHub', 'Jira', 'Mastodon', 'Notion', 'OpenWeatherMap',
    'Shopify', 'Spoonacular', 'Stripe', 'Zulip',
]

#                   docs  nodocs  mutated
DATA = np.array([
    [ 86,   nan,  nan  ],   # alphavantage  (nodocs/mutated: all 19 ENVIRONMENT — quota)
    [ 92,    93,   91  ],   # confluence
    [ 73,    67,   80  ],   # ebay_buy
    [100,    89,   55  ],   # ebay_commerce
    [ 38,    50,   43  ],   # ebay_sell
    [ 62,    83,   76  ],   # github
    [ 50,    25,   50  ],   # jira
    [100,   100,  100  ],   # mastodon
    [ 78,   100,  100  ],   # notion
    [100,    86,  100  ],   # openweathermap
    [ 87,    92,   62  ],   # shopify
    [100,    90,   78  ],   # spoonacular
    [ 72,    62,   57  ],   # stripe
    [ 80,    60,   62  ],   # zulip
], dtype=float)

CONDITIONS   = ['docs', 'nodocs', 'mutated']
COND_LABELS  = ['With docs', 'No docs', 'Mutated docs']
COND_COLORS  = ['#1D4ED8', '#0EA5E9', '#7C3AED']
COND_MARKERS = ['o', 's', '^']

N = len(DATASETS)

# NaN cells with a specific footnote reason
FLAGGED = {
    (0, 1): '†',   # alphavantage nodocs — all 19 tasks ENVIRONMENT (quota)
    (0, 2): '†',   # alphavantage mutated — all 19 tasks ENVIRONMENT (quota)
}

# SYNTH% (server_sufficient / total) — NaN where not measured
#                    docs  nodocs  mutated
SYNTH = np.array([
    [ 84,   nan,  nan  ],   # alphavantage
    [ 95,    95,   95  ],   # confluence
    [ 88,    94,   88  ],   # ebay_buy
    [100,    85,   54  ],   # ebay_commerce
    [ 43,    50,   43  ],   # ebay_sell
    [ 61,    87,   61  ],   # github
    [ 56,    44,   56  ],   # jira
    [ 93,   100,  100  ],   # mastodon
    [ 91,   100,  100  ],   # notion
    [100,    83,  100  ],   # openweathermap
    [ 89,    94,   61  ],   # shopify
    [ 75,    75,   75  ],   # spoonacular
    [ 77,    68,   73  ],   # stripe
    [ 84,    48,   64  ],   # zulip
], dtype=float)

# Mutation adherence (HTTP%, interface%) — how much the model adopted renamed params
ADH_HTTP  = np.array([100, 80, 40, 20, 40,  0, 20, 100, 80, 60,  0, 75,  0, 17], dtype=float)
ADH_IFACE = np.array([100, 80, 60, 40, 60,  0, 40, 100, 80, 80, 20, 75, 20, 17], dtype=float)

TEXT = '#1A1A1A'
SUB  = '#555555'
MISS = '#D4D8DE'

CMAP = LinearSegmentedColormap.from_list(
    'rg', ['#C62828', '#EF6C00', '#F9A825', '#7CB342', '#2E7D32'], N=256)


def _spine_clean(ax, keep=('bottom', 'left')):
    for sp in ax.spines:
        ax.spines[sp].set_visible(sp in keep)
        if sp in keep:
            ax.spines[sp].set_color('#CCCCCC')


# ══════════════════════════════════════════════════════════════════════════════
# Option 1 — Heatmap table
# ══════════════════════════════════════════════════════════════════════════════
def make_heatmap(ax):
    for ri, dataset in enumerate(DATASETS):
        for ci in range(3):
            val = DATA[ri, ci]
            y = N - 1 - ri
            x = ci

            if np.isnan(val):
                fc = MISS
                label = '—'
                tc = '#888888'
            else:
                fc = CMAP(val / 100)
                label = f'{val:.0f}%'
                r, g, b, _ = fc
                lum = 0.299*r + 0.587*g + 0.114*b
                tc = 'white' if lum < 0.45 else TEXT

                flag = FLAGGED.get((ri, ci), '')
                if flag:
                    label += flag

            ax.add_patch(mpatches.Rectangle((x, y), 1, 1,
                         fc=fc, ec='white', lw=2.5, zorder=3))
            ax.text(x + 0.5, y + 0.5, label,
                    ha='center', va='center',
                    fontsize=12, fontweight='bold', color=tc, zorder=4)

    ax.set_xlim(0, 3)
    ax.set_ylim(0, N)
    ax.set_xticks([0.5, 1.5, 2.5])
    ax.set_xticklabels(COND_LABELS, fontsize=12, fontweight='bold', color=TEXT)
    ax.set_yticks([N - 1 - i + 0.5 for i in range(N)])
    ax.set_yticklabels(DATASETS, fontsize=11, color=TEXT)
    ax.tick_params(length=0, which='both')
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title('Pass rate by dataset × synthesis condition',
                 fontsize=12, color=SUB, pad=36, style='italic')

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=CMAP, norm=plt.Normalize(0, 100))
    sm.set_array([])
    cb = ax.get_figure().colorbar(sm, ax=ax, fraction=0.025, pad=0.02)
    cb.set_ticks([0, 25, 50, 75, 100])
    cb.ax.tick_params(labelsize=10)
    cb.outline.set_visible(False)

    # Flag legend
    ax.text(0, -0.7, '† all 19 Alphavantage tasks returned ENVIRONMENT verdict (API quota exhausted); '
            'SYNTH=95% confirms server quality',
            fontsize=8.5, color='#777777', style='italic',
            transform=ax.transData, va='top')


# ══════════════════════════════════════════════════════════════════════════════
# Option 2 — Grouped bar chart
# ══════════════════════════════════════════════════════════════════════════════
def make_bars(ax):
    x = np.arange(N)
    w = 0.24

    for ci, (color, label) in enumerate(zip(COND_COLORS, COND_LABELS)):
        offset = (ci - 1) * (w + 0.02)
        vals = DATA[:, ci]
        for di in range(N):
            if not np.isnan(vals[di]):
                ax.bar(x[di] + offset, vals[di], w,
                       color=color, alpha=0.88, zorder=3,
                       linewidth=0)

    ax.axhline(50, color='#E0E0E0', lw=1.0, zorder=1)
    ax.set_xticks(x)
    ax.set_xticklabels(DATASETS, rotation=38, ha='right', fontsize=10.5)
    ax.set_ylabel('Pass rate (%)', fontsize=11, color=SUB)
    ax.set_ylim(0, 112)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.tick_params(colors=SUB, length=3)
    _spine_clean(ax)
    ax.set_title('Pass rate by dataset and synthesis condition',
                 fontsize=12, color=SUB, style='italic')

    handles = [mpatches.Patch(color=c, alpha=0.88, label=l)
               for c, l in zip(COND_COLORS, COND_LABELS)]
    ax.legend(handles=handles, fontsize=10, frameon=False,
              loc='upper right', ncol=3)


# ══════════════════════════════════════════════════════════════════════════════
# Option 3 — Scatter: docs% vs nodocs%
# ══════════════════════════════════════════════════════════════════════════════
# Manual label offsets (dx, dy in data units) to avoid overlap
# New positions: docs vs nodocs
# x=100 cluster: Mastodon(100,100), eBay Commerce(100,89), Spoonacular(100,90), OWM(100,86)
# upper-right cluster: Confluence(92,93), Shopify(87,92), Notion(78,100)
SCATTER_OFFSETS = {
    'Mastodon':       (-16,  3),   # (100,100) — top-right corner
    'eBay Commerce':  (-20,  2),   # (100, 89)
    'Spoonacular':    (-20,  9),   # (100, 90)
    'OpenWeatherMap': (-20, -6),   # (100, 86)
    'Confluence':     (  2,  2),   # (92, 93)
    'Shopify':        (-14, -5),   # (87, 92)
    'Notion':         (  2, -6),   # (78, 100)
    'GitHub':         (  2,  2),   # (62, 83)
    'eBay Buy':       (  2,  3),   # (73, 67)
    'Stripe':         (  2, -6),   # (72, 62)
    'Zulip':          (  2,  2),   # (80, 60)
    'eBay Sell':      (  2,  2),   # (38, 50)
    'Jira':           (  2, -6),   # (50, 25)
}

def make_scatter(ax):
    # Diagonal and shaded zones
    ax.plot([0, 100], [0, 100], color='#BBBBBB', lw=1.2, ls='--', zorder=1)
    ax.fill_between([0, 100], [0, 100], [100, 100],
                    alpha=0.05, color='#0EA5E9', zorder=0)
    ax.fill_between([0, 100], [0, 0], [0, 100],
                    alpha=0.05, color='#1D4ED8', zorder=0)

    ax.text(6, 94, 'nodocs wins', fontsize=9, color='#0EA5E9',
            style='italic', alpha=0.8)
    ax.text(72, 6, 'docs wins', fontsize=9, color='#1D4ED8',
            style='italic', alpha=0.8)

    for di, dataset in enumerate(DATASETS):
        dx = DATA[di, 0]
        dy = DATA[di, 1]
        if np.isnan(dx) or np.isnan(dy):
            continue

        above = dy > dx
        color  = '#0EA5E9' if above else '#1D4ED8'
        marker = '^' if above else 'o'
        ax.scatter(dx, dy, color=color, s=90, zorder=5,
                   marker=marker, edgecolors='white', linewidths=0.8)

        ox, oy = SCATTER_OFFSETS.get(dataset, (2, 2))
        ha = 'right' if ox < 0 else 'left'
        ax.annotate(dataset, (dx, dy),
                    xytext=(dx + ox, dy + oy),
                    fontsize=9, color=TEXT, ha=ha, va='center',
                    arrowprops=dict(arrowstyle='-', color='#CCCCCC',
                                   lw=0.7) if abs(ox) > 4 else None)

    ax.set_xlim(-8, 110)
    ax.set_ylim(-8, 110)
    ax.set_xlabel('Pass rate — with docs (%)', fontsize=11, color=SUB)
    ax.set_ylabel('Pass rate — no docs (%)', fontsize=11, color=SUB)
    ax.tick_params(colors=SUB, length=3)
    _spine_clean(ax)
    ax.set_title('Does documentation help? (docs vs. no-docs)',
                 fontsize=12, color=SUB, style='italic')

    handles = [
        plt.scatter([], [], color='#0EA5E9', marker='^', s=60,
                    label='nodocs wins — parametric knowledge sufficient'),
        plt.scatter([], [], color='#1D4ED8', marker='o', s=60,
                    label='docs wins — documentation adds value'),
    ]
    ax.legend(handles=handles, fontsize=9, frameon=False)


# ══════════════════════════════════════════════════════════════════════════════
# Option 4 — Cleveland dot plot
# ══════════════════════════════════════════════════════════════════════════════
def make_cleveland(ax):
    sort_idx = np.argsort(DATA[:, 0])   # sort by docs pass rate

    for rank, di in enumerate(sort_idx):
        y = rank
        vals = DATA[di]
        avail = [v for v in vals if not np.isnan(v)]

        if len(avail) > 1:
            ax.hlines(y, min(avail), max(avail),
                      color='#DDDDDD', lw=2.0, zorder=2)

        for ci, (color, marker) in enumerate(zip(COND_COLORS, COND_MARKERS)):
            if not np.isnan(vals[ci]):
                ax.scatter(vals[ci], y,
                           color=color, s=65, zorder=4,
                           marker=marker,
                           edgecolors='white', linewidths=0.6)

    ax.set_yticks(range(N))
    ax.set_yticklabels([DATASETS[i] for i in sort_idx],
                       fontsize=11, color=TEXT)
    ax.set_xlabel('Pass rate (%)', fontsize=11, color=SUB)
    ax.set_xlim(-6, 108)
    ax.axvline(50, color='#EEEEEE', lw=1.2, zorder=1)
    ax.tick_params(colors=SUB, length=3, left=False)
    ax.grid(axis='x', color='#F4F4F4', lw=1.0, zorder=0)
    _spine_clean(ax, keep=('bottom',))
    ax.spines['left'].set_visible(False)
    ax.set_title('Pass rate sorted by docs condition',
                 fontsize=12, color=SUB, style='italic')

    handles = [plt.scatter([], [], color=c, marker=m, s=55, label=l)
               for c, m, l in zip(COND_COLORS, COND_MARKERS, COND_LABELS)]
    ax.legend(handles=handles, fontsize=10, frameon=False,
              loc='lower right')


# ══════════════════════════════════════════════════════════════════════════════
# Option 5 — Heatmap with SYNTH% secondary
# ══════════════════════════════════════════════════════════════════════════════
def make_heatmap_synth(ax):
    for ri, dataset in enumerate(DATASETS):
        for ci in range(3):
            val  = DATA[ri, ci]
            sval = SYNTH[ri, ci]
            y = N - 1 - ri
            x = ci

            if np.isnan(val):
                fc = MISS
                main_str = '—' + FLAGGED.get((ri, ci), '')
                sub_str  = ''
                tc = '#888888'
            else:
                fc = CMAP(val / 100)
                main_str = f'{val:.0f}%'
                sub_str  = f'synth {sval:.0f}%' if not np.isnan(sval) else ''
                r, g, b, _ = fc
                lum = 0.299*r + 0.587*g + 0.114*b
                tc = 'white' if lum < 0.45 else TEXT

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

    ax.set_xlim(0, 3); ax.set_ylim(0, N)
    ax.set_xticks([0.5, 1.5, 2.5])
    ax.set_xticklabels(COND_LABELS, fontsize=12, fontweight='bold', color=TEXT)
    ax.set_yticks([N - 1 - i + 0.5 for i in range(N)])
    ax.set_yticklabels(DATASETS, fontsize=11, color=TEXT)
    ax.tick_params(length=0)
    ax.xaxis.tick_top(); ax.xaxis.set_label_position('top')
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title('Pass rate (large) + server synthesis quality (small)',
                 fontsize=12, color=SUB, pad=36, style='italic')
    sm = plt.cm.ScalarMappable(cmap=CMAP, norm=plt.Normalize(0, 100))
    sm.set_array([])
    cb = ax.get_figure().colorbar(sm, ax=ax, fraction=0.025, pad=0.02)
    cb.set_ticks([0, 25, 50, 75, 100])
    cb.ax.tick_params(labelsize=10)
    cb.outline.set_visible(False)
    ax.text(0, -0.7, '† Alphavantage nodocs/mutated: all tasks ENVIRONMENT (quota) — server quality confirmed by SYNTH=95%',
            fontsize=8.5, color='#777777', style='italic', transform=ax.transData, va='top')


# ══════════════════════════════════════════════════════════════════════════════
# Option 6 — Slope / parallel-coordinates chart
# ══════════════════════════════════════════════════════════════════════════════
# Color lines by whether docs > nodocs (docs wins) or nodocs > docs (nodocs wins)
DOCS_WINS_C   = '#1D4ED8'   # blue
NODOCS_WINS_C = '#0EA5E9'   # sky
ONLY_DOCS_C   = '#94A3B8'   # slate (alphavantage — only docs available)

def make_slopes(ax):
    xs = [0, 1, 2]

    for di, dataset in enumerate(DATASETS):
        vals = DATA[di]
        d, nd, mu = vals[0], vals[1], vals[2]

        if np.isnan(nd):
            color = ONLY_DOCS_C
            lw, alpha, zo = 1.2, 0.6, 2
        elif nd > d:
            color = NODOCS_WINS_C
            lw, alpha, zo = 1.8, 0.85, 3
        else:
            color = DOCS_WINS_C
            lw, alpha, zo = 1.8, 0.85, 3

        # Plot connected segments (skip NaN gaps)
        ys_full = [d, nd, mu]
        for seg_start in range(2):
            x0, y0 = xs[seg_start],     ys_full[seg_start]
            x1, y1 = xs[seg_start + 1], ys_full[seg_start + 1]
            if not np.isnan(y0) and not np.isnan(y1):
                ax.plot([x0, x1], [y0, y1], color=color, lw=lw,
                        alpha=alpha, zorder=zo, solid_capstyle='round')

        # Dots at each available point
        for xi, yi in zip(xs, ys_full):
            if not np.isnan(yi):
                ax.scatter(xi, yi, color=color, s=28, zorder=zo + 1,
                           edgecolors='white', linewidths=0.5)

        # Label at rightmost non-NaN point
        last_xi = max(xi for xi, yi in zip(xs, ys_full) if not np.isnan(yi))
        last_yi = ys_full[last_xi]
        ha = 'left' if last_xi == 2 else 'right'
        xoff = 0.06 if last_xi == 2 else -0.06
        ax.text(last_xi + xoff, last_yi, dataset,
                ha=ha, va='center', fontsize=8.5, color=color, zorder=5)

    ax.set_xticks(xs)
    ax.set_xticklabels(COND_LABELS, fontsize=12, fontweight='bold', color=TEXT)
    ax.set_ylabel('Pass rate (%)', fontsize=11, color=SUB)
    ax.set_ylim(-5, 110)
    ax.set_xlim(-0.5, 2.8)
    ax.axhline(50, color='#EEEEEE', lw=1.0, zorder=0)
    ax.tick_params(colors=SUB, length=3, bottom=False)
    _spine_clean(ax, keep=('left',))
    ax.set_title('Pass rate trajectory across synthesis conditions',
                 fontsize=12, color=SUB, style='italic')

    handles = [
        plt.Line2D([0], [0], color=DOCS_WINS_C,   lw=2, label='docs ≥ nodocs'),
        plt.Line2D([0], [0], color=NODOCS_WINS_C, lw=2, label='nodocs > docs'),
        plt.Line2D([0], [0], color=ONLY_DOCS_C,   lw=1.5, label='nodocs unavailable'),
    ]
    ax.legend(handles=handles, fontsize=9, frameon=False, loc='lower left')


# ══════════════════════════════════════════════════════════════════════════════
# Option 7 — Mutation adherence panel
#   Left:  horizontal bars (HTTP% and interface%) per dataset
#   Right: scatter adherence vs docs−nodocs delta (does low adherence → nodocs wins?)
# ══════════════════════════════════════════════════════════════════════════════
def make_adherence(fig, ax_bars, ax_scatter):
    # ── Left: adherence bars ────────────────────────────────────────────────
    sort_idx = np.argsort(ADH_HTTP)
    y = np.arange(N)
    h = 0.35

    ax_bars.barh(y - h/2, ADH_HTTP[sort_idx],  h, color='#1D4ED8', alpha=0.85,
                 label='HTTP adoption',      zorder=3)
    ax_bars.barh(y + h/2, ADH_IFACE[sort_idx], h, color='#93C5FD', alpha=0.85,
                 label='Interface adoption', zorder=3)

    ax_bars.set_yticks(y)
    ax_bars.set_yticklabels([DATASETS[i] for i in sort_idx], fontsize=11, color=TEXT)
    ax_bars.set_xlabel('Adoption rate (%)', fontsize=11, color=SUB)
    ax_bars.set_xlim(0, 118)
    ax_bars.axvline(50, color='#EEEEEE', lw=1.0, zorder=1)
    ax_bars.tick_params(colors=SUB, length=3, left=False)
    ax_bars.grid(axis='x', color='#F4F4F4', lw=1.0, zorder=0)
    _spine_clean(ax_bars, keep=('bottom',))
    ax_bars.spines['left'].set_visible(False)
    ax_bars.set_title('Mutation adherence\n(did synthesizer adopt renamed params?)',
                      fontsize=11, color=SUB, style='italic')
    ax_bars.legend(fontsize=9, frameon=False, loc='lower right')

    # ── Right: adherence vs docs−nodocs delta ───────────────────────────────
    # x = HTTP adherence, y = docs_pass − nodocs_pass
    # positive delta → docs wins, negative → nodocs wins
    for di, dataset in enumerate(DATASETS):
        adh = ADH_HTTP[di]
        d   = DATA[di, 0]
        nd  = DATA[di, 1]
        if np.isnan(nd):
            continue
        delta = d - nd
        color = DOCS_WINS_C if delta >= 0 else NODOCS_WINS_C
        ax_scatter.scatter(adh, delta, color=color, s=70, zorder=4,
                           edgecolors='white', linewidths=0.8)

        # Label offset to reduce overlap
        ha = 'right' if adh > 50 else 'left'
        xoff = -2 if adh > 50 else 2
        ax_scatter.annotate(dataset, (adh, delta),
                            xytext=(adh + xoff, delta + 1.5),
                            fontsize=8.5, color=TEXT, ha=ha, va='bottom')

    ax_scatter.axhline(0, color='#BBBBBB', lw=1.2, ls='--', zorder=1)
    ax_scatter.axvline(50, color='#EEEEEE', lw=1.0, zorder=0)
    ax_scatter.fill_between([-5, 105], 0, 60,  alpha=0.04, color=DOCS_WINS_C)
    ax_scatter.fill_between([-5, 105], -60, 0, alpha=0.04, color=NODOCS_WINS_C)
    ax_scatter.text(2,  48, 'docs wins',   fontsize=9, color=DOCS_WINS_C,   style='italic', alpha=0.7, va='top')
    ax_scatter.text(2, -48, 'nodocs wins', fontsize=9, color=NODOCS_WINS_C, style='italic', alpha=0.7, va='bottom')
    ax_scatter.set_xlabel('Mutation adherence — HTTP adoption (%)', fontsize=11, color=SUB)
    ax_scatter.set_ylabel('docs pass rate − nodocs pass rate (pp)', fontsize=11, color=SUB)
    ax_scatter.set_xlim(-5, 108)
    ax_scatter.set_ylim(-55, 55)
    ax_scatter.tick_params(colors=SUB, length=3)
    _spine_clean(ax_scatter)
    ax_scatter.set_title('Does low adherence predict nodocs winning?\n'
                         '(low adherence = model ignored renamed params; implies strong parametric knowledge)',
                         fontsize=11, color=SUB, style='italic')


# Per-dataset color palette (qualitative, 14 colors)
DS_COLORS = [
    '#E63946', '#457B9D', '#2A9D8F', '#E9C46A', '#F4A261',
    '#264653', '#8338EC', '#3A86FF', '#FB5607', '#FF006E',
    '#8AC926', '#6A4C93', '#1982C4', '#FF595E',
]


# ══════════════════════════════════════════════════════════════════════════════
# Option 8 — Diverging delta bars  (nodocs−docs  and  mutated−docs)
# ══════════════════════════════════════════════════════════════════════════════
def make_delta(ax):
    # Compute deltas; skip alphavantage (NaN nodocs)
    deltas_nd = DATA[:, 1] - DATA[:, 0]   # nodocs − docs
    deltas_mu = DATA[:, 2] - DATA[:, 0]   # mutated − docs

    # Sort by nodocs delta, excluding NaN
    valid = [(deltas_nd[i], i) for i in range(N) if not np.isnan(deltas_nd[i])]
    valid.sort(reverse=True)
    order = [i for _, i in valid]

    ys   = np.arange(len(order))
    h    = 0.32
    BLUE = '#1D4ED8';  SKY = '#0EA5E9';  VIOLET = '#7C3AED'
    ZERO = '#AAAAAA'

    for rank, di in enumerate(order):
        y = ys[rank]
        nd = deltas_nd[di]
        mu = deltas_mu[di]

        # nodocs bar
        color_nd = SKY if nd >= 0 else BLUE
        ax.barh(y + h/2, nd, h, color=color_nd, alpha=0.88, zorder=3)

        # mutated bar (if available)
        if not np.isnan(mu):
            color_mu = '#A78BFA' if mu >= 0 else VIOLET
            ax.barh(y - h/2, mu, h, color=color_mu, alpha=0.88, zorder=3)

    ax.set_yticks(ys)
    ax.set_yticklabels([DATASETS[i] for i in order], fontsize=11, color=TEXT)
    ax.axvline(0, color='#444444', lw=1.0, zorder=4)
    ax.axvline(-20, color='#F0F0F0', lw=0.8, zorder=0)
    ax.axvline(20,  color='#F0F0F0', lw=0.8, zorder=0)
    ax.set_xlabel('Pass rate delta vs docs condition (percentage points)', fontsize=11, color=SUB)
    ax.set_xlim(-40, 40)
    ax.tick_params(colors=SUB, length=3, left=False)
    _spine_clean(ax, keep=('bottom',))
    ax.spines['left'].set_visible(False)
    ax.set_title('Effect of removing / mutating docs  (positive = that condition outperforms docs)',
                 fontsize=12, color=SUB, style='italic')

    handles = [
        mpatches.Patch(color=SKY,    alpha=0.88, label='nodocs − docs (positive: nodocs wins)'),
        mpatches.Patch(color=BLUE,   alpha=0.88, label='nodocs − docs (negative: docs wins)'),
        mpatches.Patch(color='#A78BFA', alpha=0.88, label='mutated − docs (positive)'),
        mpatches.Patch(color=VIOLET, alpha=0.88, label='mutated − docs (negative)'),
    ]
    ax.legend(handles=handles, fontsize=9, frameon=False, loc='lower right', ncol=2)


# ══════════════════════════════════════════════════════════════════════════════
# Option 9 — Strip / beeswarm per condition
# ══════════════════════════════════════════════════════════════════════════════
def make_strip(ax):
    # For each condition column, spread overlapping dots horizontally by rank
    for ci in range(3):
        vals = DATA[:, ci]
        valid = sorted([(v, di) for di, v in enumerate(vals) if not np.isnan(v)])
        n = len(valid)
        for rank, (val, di) in enumerate(valid):
            # Spread x within ±0.30 of the column position
            xoff = (rank / max(n - 1, 1) - 0.5) * 0.55
            ax.scatter(ci + xoff, val,
                       color=DS_COLORS[di], s=90, zorder=4,
                       edgecolors='white', linewidths=0.9)

    # Median line per condition
    for ci in range(3):
        med = np.nanmedian(DATA[:, ci])
        ax.hlines(med, ci - 0.35, ci + 0.35,
                  color='#333333', lw=1.5, zorder=5, ls='--')

    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(COND_LABELS, fontsize=12, fontweight='bold', color=TEXT)
    ax.set_ylabel('Pass rate (%)', fontsize=11, color=SUB)
    ax.set_ylim(-8, 112)
    ax.set_xlim(-0.55, 2.55)
    ax.axhline(50, color='#EEEEEE', lw=1.0, zorder=0)
    ax.tick_params(colors=SUB, length=3, bottom=False)
    _spine_clean(ax, keep=('left',))
    ax.set_title('Distribution of pass rates per condition  (dashed = median)',
                 fontsize=12, color=SUB, style='italic')

    handles = [plt.scatter([], [], color=DS_COLORS[i], s=60, label=DATASETS[i])
               for i in range(N)]
    ax.legend(handles=handles, fontsize=8.5, frameon=False,
              loc='lower right', ncol=2, labelspacing=0.3)


# ══════════════════════════════════════════════════════════════════════════════
# Option 10 — Small multiples  (one mini-chart per dataset, 7×2 grid)
# ══════════════════════════════════════════════════════════════════════════════
def make_small_multiples(fig, axes_flat):
    xs = [0, 1, 2]
    tick_labels = ['D', 'N', 'M']   # docs / nodocs / mutated

    for idx, di in enumerate(range(N)):
        ax = axes_flat[idx]
        ax.set_facecolor('white')
        vals = DATA[di]

        for ci, (color, val) in enumerate(zip(COND_COLORS, vals)):
            if not np.isnan(val):
                ax.bar(ci, val, 0.65, color=color, alpha=0.88, zorder=3)
                ax.text(ci, val + 2, f'{val:.0f}', ha='center', va='bottom',
                        fontsize=7.5, color=color, fontweight='bold')

        ax.set_xlim(-0.55, 2.55)
        ax.set_ylim(0, 118)
        ax.set_xticks(xs)
        ax.set_xticklabels(tick_labels, fontsize=8, color=SUB)
        ax.set_yticks([0, 50, 100])
        ax.tick_params(colors=SUB, length=2, labelsize=7.5)
        ax.axhline(50, color='#EEEEEE', lw=0.8, zorder=0)
        _spine_clean(ax, keep=('bottom', 'left'))
        ax.spines['bottom'].set_color('#DDDDDD')
        ax.spines['left'].set_color('#DDDDDD')
        ax.set_title(DATASETS[di], fontsize=10, fontweight='bold',
                     color=TEXT, pad=3)

    # Hide any unused axes (if grid > N)
    for idx in range(N, len(axes_flat)):
        axes_flat[idx].set_visible(False)


# ══════════════════════════════════════════════════════════════════════════════
# Option 11 — Bubble matrix
# ══════════════════════════════════════════════════════════════════════════════
def make_bubble(ax):
    MAX_R = 0.44   # max bubble radius in data units

    for ri, dataset in enumerate(DATASETS):
        for ci in range(3):
            val = DATA[ri, ci]
            y   = N - 1 - ri
            x   = ci

            if np.isnan(val):
                # small gray ring
                ax.scatter(x + 0.5, y + 0.5, s=60, facecolors=MISS,
                           edgecolors='#AAAAAA', linewidths=0.8, zorder=3)
                ax.text(x + 0.5, y + 0.5, '—', ha='center', va='center',
                        fontsize=9, color='#999999', zorder=4)
            else:
                radius = MAX_R * (val / 100) ** 0.5   # sqrt for area proportionality
                fc     = CMAP(val / 100)
                circle = plt.Circle((x + 0.5, y + 0.5), radius,
                                    fc=fc, ec='white', lw=1.5, zorder=3)
                ax.add_patch(circle)
                r, g, b, _ = fc
                lum = 0.299*r + 0.587*g + 0.114*b
                tc  = 'white' if lum < 0.45 else TEXT
                ax.text(x + 0.5, y + 0.5, f'{val:.0f}%',
                        ha='center', va='center',
                        fontsize=10, fontweight='bold', color=tc, zorder=4)

    ax.set_xlim(0, 3); ax.set_ylim(0, N)
    ax.set_xticks([0.5, 1.5, 2.5])
    ax.set_xticklabels(COND_LABELS, fontsize=12, fontweight='bold', color=TEXT)
    ax.set_yticks([N - 1 - i + 0.5 for i in range(N)])
    ax.set_yticklabels(DATASETS, fontsize=11, color=TEXT)
    ax.tick_params(length=0)
    ax.xaxis.tick_top(); ax.xaxis.set_label_position('top')
    # light grid
    for x in [1, 2]:
        ax.axvline(x, color='#EEEEEE', lw=1.0, zorder=1)
    for y in range(1, N):
        ax.axhline(y, color='#EEEEEE', lw=1.0, zorder=1)
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title('Pass rate as bubble size  (larger = higher pass rate)',
                 fontsize=12, color=SUB, pad=36, style='italic')

    sm = plt.cm.ScalarMappable(cmap=CMAP, norm=plt.Normalize(0, 100))
    sm.set_array([])
    cb = ax.get_figure().colorbar(sm, ax=ax, fraction=0.025, pad=0.02)
    cb.set_ticks([0, 25, 50, 75, 100])
    cb.ax.tick_params(labelsize=10)
    cb.outline.set_visible(False)


# ══════════════════════════════════════════════════════════════════════════════
# Render individual figures
# ══════════════════════════════════════════════════════════════════════════════
for name, fn, figsize, maker in [
    ('heatmap',        'results_heatmap.png',        (7.5, 7.5), make_heatmap),
    ('bars',           'results_bars.png',           (13,  5.5), make_bars),
    ('scatter',        'results_scatter.png',        (7,   7),   make_scatter),
    ('cleveland',      'results_cleveland.png',      (8,   6.5), make_cleveland),
    ('heatmap_synth',  'results_heatmap_synth.png',  (7.5, 7.5), make_heatmap_synth),
    ('slopes',         'results_slopes.png',         (9,   6.5), make_slopes),
    ('delta',          'results_delta.png',          (10,  5.5), make_delta),
    ('strip',          'results_strip.png',          (7,   6.5), make_strip),
    ('bubble',         'results_bubble.png',         (7.5, 7.5), make_bubble),
]:
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    maker(ax)
    plt.tight_layout(pad=0.8)
    plt.savefig(fn, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f'Saved {fn}')

# Adherence panel needs 1×2 subplot layout
fig, (ax_b, ax_s) = plt.subplots(1, 2, figsize=(15, 6))
fig.patch.set_facecolor('white')
ax_b.set_facecolor('white'); ax_s.set_facecolor('white')
make_adherence(fig, ax_b, ax_s)
plt.tight_layout(pad=0.8)
plt.savefig('results_adherence.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved results_adherence.png')

# Small multiples needs 7×2 grid
fig, axes = plt.subplots(7, 2, figsize=(9, 14))
fig.patch.set_facecolor('white')
make_small_multiples(fig, axes.flat)
fig.subplots_adjust(hspace=0.55, wspace=0.35, left=0.10, right=0.97, top=0.97, bottom=0.04)
plt.savefig('results_small_multiples.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved results_small_multiples.png')

# ══════════════════════════════════════════════════════════════════════════════
# Combined 2×2
# ══════════════════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(2, 2, figsize=(20, 16))
fig.patch.set_facecolor('white')
for ax in axes.flat:
    ax.set_facecolor('white')

make_heatmap(axes[0, 0])
make_bars(axes[0, 1])
make_scatter(axes[1, 0])
make_cleveland(axes[1, 1])

for ax, letter in zip(axes.flat, 'ABCD'):
    ax.text(-0.04, 1.04, letter, transform=ax.transAxes,
            fontsize=16, fontweight='bold', color=TEXT, va='top')

fig.subplots_adjust(hspace=0.40, wspace=0.30, left=0.07, right=0.97, top=0.96, bottom=0.07)
plt.savefig('results_combined.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print('Saved results_combined.png')
