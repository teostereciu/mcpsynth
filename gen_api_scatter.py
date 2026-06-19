"""
API familiarity × complexity scatter plot for thesis.
"""
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

matplotlib.rcParams.update({
    'font.family':  'serif',
    'font.serif':   ['CMU Serif', 'Computer Modern', 'Palatino',
                     'Georgia', 'DejaVu Serif', 'Times New Roman'],
    'pdf.fonttype': 42,
    'ps.fonttype':  42,
})

# ── Data ──────────────────────────────────────────────────────────────────────
# familiarity: 1 (very low) → 5 (very high), with jitter for readability
# complexity : doc file count (log-scaled on plot)
# category   : for colour grouping

apis = [
    # name                   fam   doc_files  category
    ('GitHub',               4.8,  181,       'developer'),
    ('Slack',                4.6,  445,       'productivity'),
    ('Stripe',               3.9,  120,       'commerce'),
    ('Notion',               3.6,   94,       'productivity'),
    ('Jira',                 3.5,  101,       'productivity'),
    ('Confluence',           2.8,   47,       'productivity'),
    ('Zulip',                2.7,  165,       'developer'),
    ('Mastodon',             2.5,   35,       'developer'),
    ('OpenWeatherMap',       2.4,    7,       'data'),
    ('Spoonacular',          1.9,    7,       'data'),
    ('Alpha Vantage',        1.8,    9,       'data'),
    ('eBay Buy',             1.4,   28,       'commerce'),
    ('eBay Commerce',        1.3,   48,       'commerce'),
    ('eBay Sell',            1.2,  192,       'commerce'),
    ('Adyen',                1.0,  593,       'commerce'),
]

cat_colors = {
    'developer':   '#3A80B0',
    'productivity':'#2A9478',
    'commerce':    '#B8703A',
    'data':        '#7A4E96',
}
cat_labels = {
    'developer':   'Developer tooling',
    'productivity':'Productivity',
    'commerce':    'E-commerce / payments',
    'data':        'Data / financial',
}

names   = [a[0] for a in apis]
fam     = np.array([a[1] for a in apis])
docs    = np.array([a[2] for a in apis])
cats    = [a[3] for a in apis]
colors  = [cat_colors[c] for c in cats]

# ── Figure ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8.5, 5.2))
fig.patch.set_facecolor('white')
ax.set_facecolor('#F8F8FB')
ax.grid(axis='both', color='white', linewidth=0.9, zorder=0)
for spine in ax.spines.values():
    spine.set_visible(False)

sc = ax.scatter(fam, docs, c=colors, s=90, zorder=3,
                edgecolors='white', linewidths=0.8)

# ── Labels ────────────────────────────────────────────────────────────────────
# manual offsets to avoid overlaps: (dx, dy, ha, va)
offsets = {
    'GitHub':        ( 0.06,  12,  'left',  'center'),
    'Slack':         ( 0.06,  16,  'left',  'center'),
    'Stripe':        ( 0.06,   8,  'left',  'center'),
    'Notion':        (-0.06,  -18, 'right', 'center'),
    'Jira':          ( 0.06,  10,  'left',  'center'),
    'Confluence':    (-0.06,  -14, 'right', 'center'),
    'Zulip':         ( 0.06,  10,  'left',  'center'),
    'Mastodon':      (-0.06,  -13, 'right', 'center'),
    'OpenWeatherMap':( 0.06,  10,  'left',  'center'),
    'Spoonacular':   (-0.06,  -13, 'right', 'center'),
    'Alpha Vantage': ( 0.06,   8,  'left',  'center'),
    'eBay Buy':      (-0.06,  -14, 'right', 'center'),
    'eBay Commerce': ( 0.06,   8,  'left',  'center'),
    'eBay Sell':     ( 0.06,  12,  'left',  'center'),
    'Adyen':         ( 0.06,  16,  'left',  'center'),
}

for name, fx, dy_raw, cat in zip(names, fam, docs, cats):
    dx, dy, ha, va = offsets.get(name, (0.06, 10, 'left', 'center'))
    ax.annotate(name, xy=(fx, dy_raw), xytext=(fx + dx, dy_raw + dy),
                fontsize=7.8, color='#333333', ha=ha, va=va,
                arrowprops=None)

# ── Axes ──────────────────────────────────────────────────────────────────────
ax.set_yscale('log')
ax.set_yticks([5, 10, 20, 50, 100, 200, 500])
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.set_ylim(4, 900)

ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xticklabels(['Very low', 'Low', 'Medium', 'High', 'Very high'],
                   fontsize=8.5)
ax.set_xlim(0.6, 5.4)

ax.set_xlabel('Pre-training familiarity', fontsize=10, labelpad=8)
ax.set_ylabel('Complexity  (documentation files, log scale)', fontsize=10, labelpad=8)
ax.tick_params(axis='both', labelsize=8.2, length=0)

# shaded quadrants (faint)
ax.axvline(3.0, color='#CCCCCC', lw=0.8, ls='--', zorder=1)
ax.axhline(50,  color='#CCCCCC', lw=0.8, ls='--', zorder=1)

# quadrant labels
quad_kw = dict(fontsize=7.2, color='#AAAAAA', style='italic', zorder=1)
ax.text(1.8, 700, 'Low familiarity\nHigh complexity', ha='center', **quad_kw)
ax.text(4.2, 700, 'High familiarity\nHigh complexity', ha='center', **quad_kw)
ax.text(1.8, 5.2, 'Low familiarity\nLow complexity',  ha='center', **quad_kw)
ax.text(4.2, 5.2, 'High familiarity\nLow complexity', ha='center', **quad_kw)

# ── Legend ────────────────────────────────────────────────────────────────────
handles = [mpatches.Patch(color=v, label=cat_labels[k])
           for k, v in cat_colors.items()]
ax.legend(handles=handles, fontsize=7.8, frameon=True, framealpha=0.9,
          edgecolor='#DDDDDD', loc='upper left',
          bbox_to_anchor=(0.01, 0.99))

ax.set_title('API selection: familiarity × complexity', fontsize=11,
             fontweight='bold', pad=10)

plt.tight_layout()
for ext in ('png', 'pdf'):
    fname = f'api_familiarity_complexity.{ext}'
    dpi = 300 if ext == 'png' else None
    plt.savefig(fname, dpi=dpi, bbox_inches='tight', facecolor='white')
    print(f'Saved {fname}')

plt.savefig('api_familiarity_complexity_transparent.png', dpi=300,
            bbox_inches='tight', facecolor='none', transparent=True)
print('Saved api_familiarity_complexity_transparent.png')
