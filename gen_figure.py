import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica Neue', 'Helvetica', 'DejaVu Sans'],
    'font.size': 10,
    'axes.titlesize': 13,
    'axes.titleweight': 'bold',
    'axes.labelsize': 10,
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
fig.patch.set_facecolor('white')
ax1.set_facecolor('white')
ax2.set_facecolor('white')

# ── PIE CHART ────────────────────────────────────────────────────────────────
# Domain order clockwise from top-right, matching reference layout
domains = [
    ('Weather/Data',            10),
    ('Developer\nTools',        35),
    ('Productivity/Collab',    100),   # google_workspace+slack+notion+zulip
    ('Financial/Payments',      62),
    ('E-Commerce',              78),
    ('Customer\nSupport/Comms', 45),   # zendesk + twilio + hubspot
]
labels = [d[0] for d in domains]
sizes  = [d[1] for d in domains]
colors_pie = ['#B0CC72', '#6DC4D8', '#9B52C0', '#D46E6B', '#6090D8', '#EA9460']

wedges, texts, autotexts = ax1.pie(
    sizes,
    labels=labels,
    autopct=lambda p: f'{p:.1f}%',
    colors=colors_pie,
    startangle=90,
    pctdistance=0.68,
    labeldistance=1.25,
    wedgeprops=dict(linewidth=1.5, edgecolor='black'),
    textprops={'fontsize': 10},
)
for at in autotexts:
    at.set_color('white')
    at.set_fontsize(10)
    at.set_fontweight('bold')
for t in texts:
    t.set_fontsize(10)
    t.set_fontweight('bold')

ax1.set_title('Scenario Distribution by Domain', fontweight='bold', fontsize=13, pad=15)

# ── HORIZONTAL BAR CHART ─────────────────────────────────────────────────────
bar_data = [
    ('OpenWeatherMap',    5),
    ('eBay Buy',         28),
    ('eBay Commerce',    47),
    ('Shopify',          57),
    ('Notion',           93),
    ('Jira',            100),
    ('Google Workspace',115),
    ('Twilio',          117),
    ('Stripe',          120),
    ('Zendesk',         149),
    ('Zulip',           164),
    ('HubSpot',         174),
    ('GitHub',          180),
    ('eBay Sell',       190),
    ('Slack',           444),
    ('TikTok Shop',     494),
    ('Adyen',           591),
]
bar_data_sorted = sorted(bar_data, key=lambda x: x[1])  # ascending → largest at top

apis   = [d[0] for d in bar_data_sorted]
values = [d[1] for d in bar_data_sorted]
# Domain-based colors
domain_color = {
    'OpenWeatherMap':    '#B0CC72',  # Weather/Data
    'eBay Buy':          '#6090D8',  # E-Commerce
    'eBay Commerce':     '#6090D8',
    'Shopify':           '#6090D8',
    'eBay Sell':         '#6090D8',
    'TikTok Shop':       '#6090D8',
    'Notion':            '#9B52C0',  # Productivity/Collab
    'Google Workspace':  '#9B52C0',
    'Slack':             '#9B52C0',
    'Zulip':             '#9B52C0',
    'HubSpot':           '#EA9460',  # Customer Support/Comms
    'Jira':              '#6DC4D8',  # Developer Tools
    'GitHub':            '#6DC4D8',
    'Twilio':            '#EA9460',  # Customer Support/Comms
    'Zendesk':           '#EA9460',
    'Stripe':            '#D46E6B',  # Financial/Payments
    'Adyen':             '#D46E6B',
}
bcolors = [domain_color[a] for a in apis]

bars = ax2.barh(apis, values, color=bcolors, height=0.65, edgecolor='white', linewidth=0.8)

for bar, val in zip(bars, values):
    ax2.text(
        val + 7, bar.get_y() + bar.get_height() / 2,
        str(val),
        va='center', ha='left', fontsize=8.5, fontweight='bold', color='#333333',
    )

ax2.set_xlabel('Number of API Endpoints', fontsize=10, labelpad=8)
ax2.set_title('API Endpoint Count by API', fontweight='bold', fontsize=13, pad=22)
ax2.set_xlim(0, max(values) * 1.15)
ax2.grid(axis='x', linestyle='--', alpha=0.45, color='#bbbbbb', zorder=0)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_color('#cccccc')
ax2.tick_params(left=False, bottom=False)
ax2.set_axisbelow(True)

plt.tight_layout(pad=2.5)
out = 'benchmark_figure.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='white')
print(f"Saved to {out}")
