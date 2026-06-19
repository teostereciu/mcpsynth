import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica Neue', 'Helvetica', 'DejaVu Sans'],
    'font.size': 10,
})

# Data from eval_results_20260415.md
# (dataset_label, passed, total, mock)
raw = [
    # Mock datasets
    ('Google\nWorkspace', 29, 30, True),
    ('Shopify',           17, 20, True),
    ('TikTok Shop',       17, 20, True),
    ('Twilio',            15, 15, True),
    ('HubSpot',            1, 15, True),
    ('Adyen',              1, 29, True),
    ('Zendesk',            1, 15, True),
    ('Slack',              0, 15, True),
    ('Jira',               0, 15, True),
    # Real API datasets
    ('OpenWeatherMap',     9, 10, False),
    ('eBay Commerce',      9, 11, False),
    ('Notion',            15, 25, False),
    ('GitHub',             6, 20, False),
    ('Stripe',             9, 34, False),
    ('eBay Buy',           0, 10, False),
    ('eBay Sell',          0, 17, False),
    ('Zulip',              0, 30, False),
]

# Sort by pass rate descending (left = highest)
raw.sort(key=lambda x: x[1] / x[2], reverse=True)

labels  = [d[0] for d in raw]
passing = [d[1] for d in raw]
failing = [d[2] - d[1] for d in raw]
pcts    = [round(100 * d[1] / d[2]) for d in raw]

GREEN = '#5DBB63'
RED   = '#D9534F'

fig, ax = plt.subplots(figsize=(16, 6))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

x = range(len(labels))
bar_w = 0.55

ax.bar(x, passing, width=bar_w, color=GREEN, label='Passing', zorder=3)
ax.bar(x, failing, width=bar_w, bottom=passing, color=RED, label='Failing', zorder=3)

# Pass rate % on top of each bar
for i, (p, f, pct) in enumerate(zip(passing, failing, pcts)):
    ax.text(i, p + f + 0.4, f'{pct}%', ha='center', va='bottom',
            fontsize=8.5, fontweight='bold', color='#222222')

ax.set_xticks(list(x))
ax.set_xticklabels(labels, rotation=35, ha='right', fontsize=9)
ax.set_ylabel('Number of Scenarios', fontsize=10, labelpad=8)
ax.set_xlabel('API', fontsize=10, labelpad=8)
ax.set_title('Scenario Outcomes by API', fontweight='bold', fontsize=13, pad=14)

ax.set_xlim(-0.6, len(labels) - 0.4)
ax.set_ylim(0, max(p + f for p, f in zip(passing, failing)) * 1.2)
ax.yaxis.set_major_locator(plt.MultipleLocator(5))
ax.grid(axis='y', linestyle='--', alpha=0.45, color='#bbbbbb', zorder=0)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#cccccc')
ax.spines['bottom'].set_color('#cccccc')
ax.tick_params(left=False)

ax.legend(
    handles=[mpatches.Patch(color=GREEN, label='Passing'),
             mpatches.Patch(color=RED,   label='Failing')],
    loc='upper right', frameon=True, framealpha=1,
    edgecolor='#cccccc', fontsize=9,
)

plt.tight_layout()
out = 'benchmark_outcomes.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f"Saved to {out}")
