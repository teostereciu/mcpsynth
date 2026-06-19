import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Polygon
import numpy as np

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica Neue', 'Helvetica', 'DejaVu Sans'],
})

W, H = 22, 12.0
fig, ax = plt.subplots(figsize=(W, H))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')

# Academic palette: bold headers, very muted box backgrounds
BLUE   = '#1D4ED8'; BLUE_L   = '#EEF2FF'; BLUE_M = '#BFDBFE'
GREEN  = '#047857'; GREEN_L  = '#ECFDF5'
PURPLE = '#6D28D9'; PURPLE_L = '#F5F3FF'; PURPLE_M = '#C4B5FD'
AMBER  = '#B45309'; AMBER_L  = '#FFFBEB'
PINK   = '#BE185D'; PINK_L   = '#FDF2F8'
DARK   = '#111827'; GRAY = '#6B7280'; LGRAY = '#E5E7EB'; XLGRAY = '#F9FAFB'

COLS  = [2.1, 6.5, 10.9, 15.3, 19.7]
BOX_W = 3.6; BOX_Y = 3.00; BOX_H = 7.20; HDR_H = 0.92
ICON_CY = 6.70

COLORS = [BLUE, GREEN, PURPLE, AMBER, PINK]
LIGHTS = [BLUE_L, GREEN_L, PURPLE_L, AMBER_L, PINK_L]
LABELS = ['INPUT', 'SYNTHESIS', 'GENERATED TOOLS', 'AGENT EVALUATION', 'LLM JUDGE']

# ── Phase boxes ────────────────────────────────────────────────────────────────
def phase_box(cx, color, light, num, label):
    x = cx - BOX_W/2
    # Main box – very light tinted background, clean border
    ax.add_patch(FancyBboxPatch((x, BOX_Y), BOX_W, BOX_H,
        boxstyle="round,pad=0,rounding_size=0.20", fc=light, ec=color, lw=1.6, zorder=2))
    # Header band
    ax.add_patch(FancyBboxPatch((x, BOX_Y+BOX_H-HDR_H), BOX_W, HDR_H,
        boxstyle="round,pad=0,rounding_size=0.20", fc=color, ec='none', zorder=3))
    ax.add_patch(mpatches.Rectangle((x, BOX_Y+BOX_H-HDR_H), BOX_W, HDR_H*0.50,
        fc=color, ec='none', zorder=3))
    # Number circle
    ax.add_patch(plt.Circle((x+0.50, BOX_Y+BOX_H-HDR_H/2), 0.26,
        fc='white', ec='none', alpha=0.20, zorder=4))
    ax.text(x+0.50, BOX_Y+BOX_H-HDR_H/2, num,
        ha='center', va='center', fontsize=13, fontweight='bold', color='white', zorder=5)
    ax.text(cx+0.16, BOX_Y+BOX_H-HDR_H/2, label,
        ha='center', va='center', fontsize=16, fontweight='bold', color='white', zorder=5)
    # Thin separator between description and content area
    sx = x + 0.18
    ax.plot([sx, sx+BOX_W-0.36], [BOX_Y+1.12, BOX_Y+1.12],
        color=color, lw=0.8, alpha=0.30, zorder=3)

for cx, c, l, n, lab in zip(COLS, COLORS, LIGHTS, ['1','2','3','4','5'], LABELS):
    phase_box(cx, c, l, n, lab)

# ── Arrows between phases ───────────────────────────────────────────────────────
for i, lbl in enumerate(['API docs + tasks', 'synthesizes', 'spawns server', 'eval trace']):
    x0 = COLS[i] + BOX_W/2 + 0.08
    x1 = COLS[i+1] - BOX_W/2 - 0.08
    ax.annotate('', xy=(x1, ICON_CY), xytext=(x0, ICON_CY),
        arrowprops=dict(arrowstyle='->', color=DARK, lw=2.2, mutation_scale=20), zorder=10)
    ax.text((x0+x1)/2, ICON_CY+0.28, lbl,
        ha='center', va='bottom', fontsize=9, color=GRAY, style='italic', zorder=11)

# ── Loop arrow ─────────────────────────────────────────────────────────────────
def loop_arrow(cx, cy, r, color):
    theta = np.linspace(np.deg2rad(50), np.deg2rad(310), 160)
    ax.plot(cx+r*np.cos(theta), cy+r*np.sin(theta), color=color, lw=2.0, zorder=6)
    et = np.deg2rad(310)
    ax.annotate('', xy=(cx+r*np.cos(et), cy+r*np.sin(et)),
        xytext=(cx+r*np.cos(et)-0.001*np.sin(et), cy+r*np.sin(et)+0.001*np.cos(et)),
        arrowprops=dict(arrowstyle='->', color=color, lw=2.0, mutation_scale=14), zorder=7)

# ── LLM circle ─────────────────────────────────────────────────────────────────
def llm_circle(cx, cy, r_loop, r_circ, color, top_label, bot_label):
    loop_arrow(cx, cy, r_loop, color)
    ax.add_patch(plt.Circle((cx, cy), r_circ, fc='white', ec=color, lw=2.0, zorder=6))
    for a0, span in [(50, 100), (175, 90), (270, 80)]:
        t = np.linspace(np.deg2rad(a0), np.deg2rad(a0+span), 40)
        ax.plot(cx+r_circ*0.55*np.cos(t), cy+r_circ*0.55*np.sin(t),
            color=color, lw=1.4, alpha=0.20, zorder=7)
    ax.text(cx, cy+r_circ*0.22, top_label, ha='center', va='center',
        fontsize=14 if r_circ > 0.7 else 12, fontweight='bold', color=color, zorder=8)
    ax.text(cx, cy-r_circ*0.30, bot_label, ha='center', va='center',
        fontsize=10 if r_circ > 0.7 else 9, color=color, zorder=8)

# ── Doc icon ───────────────────────────────────────────────────────────────────
def draw_doc(ox, oy, w, h, fc, ec, fold_c, show_lines=True):
    corner = h * 0.20
    ax.add_patch(Polygon([(ox,oy),(ox+w-corner,oy),(ox+w,oy+corner),(ox+w,oy+h),(ox,oy+h)],
        closed=True, fc=fc, ec=ec, lw=1.3, zorder=5))
    ax.add_patch(Polygon([(ox+w-corner,oy),(ox+w,oy+corner),(ox+w-corner,oy+corner)],
        closed=True, fc=fold_c, ec=ec, lw=1, zorder=6, alpha=0.45))
    if show_lines:
        for j in range(4):
            ly = oy + corner + 0.10 + j*(h-corner-0.18)/4
            ax.plot([ox+0.12, ox+w-0.12], [ly, ly], color=ec, lw=1.0, alpha=0.45, zorder=6)

# ══════════════════════════════════════════════════════════════════════════════
# 1  INPUT
# ══════════════════════════════════════════════════════════════════════════════
cx = COLS[0]
for i, (dx, dy) in enumerate([(-0.22, -0.25), (-0.10, -0.12), (0.02, 0.0)]):
    draw_doc(cx-0.72+dx, ICON_CY-0.82+dy, 1.38, 1.70,
        fc='white' if i==2 else '#F1F5F9', ec=BLUE, fold_c=BLUE_M,
        show_lines=(i == 2))
ax.add_patch(FancyBboxPatch((cx-0.32, ICON_CY-1.22), 0.64, 0.30,
    boxstyle="round,pad=0,rounding_size=0.08", fc=BLUE, ec='none', zorder=7))
ax.text(cx, ICON_CY-1.07, '.md', ha='center', va='center',
    fontsize=10, fontweight='bold', color='white', zorder=8)
ax.add_patch(FancyBboxPatch((cx-0.80, ICON_CY-2.02), 1.60, 0.54,
    boxstyle="round,pad=0,rounding_size=0.09", fc='white', ec=BLUE, lw=1.3, zorder=5))
ax.text(cx, ICON_CY-1.7, 'TASK', ha='center', va='center',
    fontsize=10.5, fontweight='bold', color=BLUE, zorder=6)
for j in range(2):
    ax.plot([cx-0.62, cx+0.62], [ICON_CY-1.94+j*0.14]*2, color=BLUE_M, lw=0.9, zorder=6)

ax.text(cx, BOX_Y+0.82, 'API Docs  +  Task Brief', ha='center',
    fontsize=11, fontweight='bold', color=DARK, zorder=6)
ax.text(cx, BOX_Y+0.38, '17 APIs · 330 scenarios', ha='center',
    fontsize=10, color=GRAY, zorder=6)

# ══════════════════════════════════════════════════════════════════════════════
# 2  SYNTHESIS  — Synthesis LLM
# ══════════════════════════════════════════════════════════════════════════════
cx = COLS[1]
llm_circle(cx, ICON_CY, 1.15, 0.82, GREEN, 'Synthesis', 'LLM')

for k, tool in enumerate(['read', 'glob', 'write']):
    px = cx - 0.78 + k*0.78
    ax.add_patch(FancyBboxPatch((px-0.32, ICON_CY-1.72), 0.64, 0.34,
        boxstyle="round,pad=0,rounding_size=0.09",
        fc=GREEN_L, ec=GREEN, lw=1.1, zorder=6))
    ax.text(px, ICON_CY-1.55, tool, ha='center', va='center',
        fontsize=9, fontweight='bold', color=GREEN, zorder=7)

ax.text(cx, BOX_Y+0.82, 'Agentic Tool-Calling Loop', ha='center',
    fontsize=11, fontweight='bold', color=DARK, zorder=6)
ax.text(cx, BOX_Y+0.38, 'reads docs · writes tools', ha='center',
    fontsize=10, color=GRAY, zorder=6)

# ══════════════════════════════════════════════════════════════════════════════
# 3  GENERATED TOOLS  — server rack
# ══════════════════════════════════════════════════════════════════════════════
cx = COLS[2]
ax.add_patch(FancyBboxPatch((cx-0.95, ICON_CY-1.20), 1.90, 2.35,
    boxstyle="round,pad=0,rounding_size=0.14",
    fc='white', ec=PURPLE, lw=1.8, zorder=5))

SLOT_DATA = [
    ('MCP Protocol',   'FastMCP'),
    ('API Client',     'auth + HTTP'),
    ('Tool Functions', '@mcp.tool()'),
]
for j, (label, sub) in enumerate(SLOT_DATA):
    sy = ICON_CY - 0.94 + j*0.70
    ax.add_patch(FancyBboxPatch((cx-0.78, sy), 1.56, 0.50,
        boxstyle="round,pad=0,rounding_size=0.08",
        fc=PURPLE_L, ec=PURPLE, lw=1.0, zorder=6))
    ax.text(cx, sy+0.31, label, ha='center', va='center',
        fontsize=9, fontweight='bold', color=PURPLE, zorder=7)
    ax.text(cx, sy+0.12, sub, ha='center', va='center',
        fontsize=8, color=GRAY, zorder=7)

ax.add_patch(FancyBboxPatch((cx-0.56, ICON_CY+1.18), 1.12, 0.36,
    boxstyle="round,pad=0,rounding_size=0.10", fc=PURPLE, ec='none', zorder=7))
ax.text(cx, ICON_CY+1.36, 'via stdio / MCP', ha='center', va='center',
    fontsize=9.5, fontweight='bold', color='white', zorder=8)

ax.text(cx, BOX_Y+0.82, 'Generated MCP Server', ha='center',
    fontsize=11, fontweight='bold', color=DARK, zorder=6)
ax.text(cx, BOX_Y+0.38, '@mcp.tool() · real HTTP calls', ha='center',
    fontsize=10, color=GRAY, zorder=6)

# ══════════════════════════════════════════════════════════════════════════════
# 4  AGENT EVALUATION  — Evaluation LLM
# ══════════════════════════════════════════════════════════════════════════════
cx = COLS[3]
ecx, ecy = cx - 0.80, ICON_CY
llm_circle(ecx, ecy, 0.85, 0.62, AMBER, 'Evaluation', 'LLM')

api_bx = cx + 0.42
ax.annotate('', xy=(api_bx, ecy), xytext=(ecx+0.68, ecy),
    arrowprops=dict(arrowstyle='<->', color=AMBER, lw=1.8, mutation_scale=16), zorder=8)

ax.add_patch(FancyBboxPatch((api_bx, ecy-0.50), 1.14, 1.00,
    boxstyle="round,pad=0,rounding_size=0.13",
    fc=AMBER_L, ec=AMBER, lw=1.6, zorder=6))
ax.text(api_bx+0.57, ecy+0.16, 'Live', ha='center', va='center',
    fontsize=11, fontweight='bold', color=AMBER, zorder=7)
ax.text(api_bx+0.57, ecy-0.16, 'API', ha='center', va='center',
    fontsize=11, fontweight='bold', color=AMBER, zorder=7)

ax.text(cx+0.04, ecy-1.18, 'ReAct loop  ·  up to 20 turns', ha='center',
    fontsize=9.5, color=AMBER, style='italic', zorder=8)

ax.text(cx, BOX_Y+0.82, 'LLM Evaluation Agent', ha='center',
    fontsize=11, fontweight='bold', color=DARK, zorder=6)
ax.text(cx, BOX_Y+0.38, 'real HTTP calls to live API', ha='center',
    fontsize=10, color=GRAY, zorder=6)

# ══════════════════════════════════════════════════════════════════════════════
# 5  LLM JUDGE
# ══════════════════════════════════════════════════════════════════════════════
cx = COLS[4]
jcy = ICON_CY + 1.55

llm_circle(cx, jcy, 0.65, 0.48, PINK, 'Judge', 'LLM')

rubric_dims = ['tool selection', 'param quality', 'result interp.', 'task completion']
rub_w, rub_h = 1.50, 0.32
rub_gap_x, rub_gap_y = 0.10, 0.10
rub_top = jcy - 0.76
for k, dim in enumerate(rubric_dims):
    col_k = k % 2; row_k = k // 2
    rx = cx - rub_w - rub_gap_x/2 + col_k*(rub_w + rub_gap_x)
    ry = rub_top - row_k*(rub_h + rub_gap_y)
    ax.add_patch(FancyBboxPatch((rx, ry-rub_h), rub_w, rub_h,
        boxstyle="round,pad=0,rounding_size=0.08",
        fc=PINK_L, ec=PINK, lw=0.9, zorder=6))
    ax.text(rx + rub_w/2, ry - rub_h/2, dim, ha='center', va='center',
        fontsize=8, color=PINK, fontweight='bold', zorder=7)

bar_y_top = rub_top - 2*(rub_h + rub_gap_y) - 0.36
bar_x, bar_w, bar_h = cx-1.30, 2.60, 0.30
bar_y = bar_y_top - bar_h
ax.add_patch(FancyBboxPatch((bar_x, bar_y), bar_w, bar_h,
    boxstyle="round,pad=0,rounding_size=0.07", fc=LGRAY, ec=GRAY, lw=0.9, zorder=5))
for f0, f1, fc in [(0, 4/8, '#FEE2E2'), (4/8, 5/8, '#FEF3C7'), (5/8, 1, '#D1FAE5')]:
    ax.add_patch(mpatches.Rectangle((bar_x+f0*bar_w, bar_y),
        (f1-f0)*bar_w, bar_h, fc=fc, ec='none', zorder=6))
tx = bar_x + (5/8)*bar_w
ax.plot([tx, tx], [bar_y, bar_y+bar_h], color=DARK, lw=1.8, ls='--', zorder=8)
ax.text(bar_x+0.04, bar_y+bar_h+0.07, '0', ha='left', fontsize=8.5, color=GRAY, zorder=8)
ax.text(bar_x+bar_w-0.04, bar_y+bar_h+0.07, '8', ha='right', fontsize=8.5, color=GRAY, zorder=8)
ax.text(tx, bar_y+bar_h+0.07, '5*', ha='center', fontsize=8.5,
    fontweight='bold', color=DARK, zorder=8)
ax.text(cx, bar_y-0.12, 'pass threshold  (score ≥ 5)', ha='center',
    fontsize=8, color=GRAY, style='italic', zorder=9)

verd_top = bar_y - 0.36
ax.text(cx, verd_top+0.12, 'Verdict', ha='center',
    fontsize=10, fontweight='bold', color=DARK, zorder=7)
for i, (label, sub, fc, ec, tc) in enumerate([
    ('PASS',       'score ≥ 5',       '#D1FAE5', '#059669', '#065F46'),
    ('FAIL',       'score < 5',       '#FEE2E2', '#DC2626', '#991B1B'),
    ('CONFOUND',   'agent/env/task',  '#FEF3C7', '#D97706', '#92400E'),
]):
    yp = verd_top - 0.22 - i*0.50
    ax.add_patch(FancyBboxPatch((cx-1.30, yp-0.19), 2.60, 0.40,
        boxstyle="round,pad=0,rounding_size=0.20",
        fc=fc, ec=ec, lw=1.5, zorder=6))
    ax.text(cx-1.12, yp-0.01, label, ha='left', va='center',
        fontsize=9.5, fontweight='bold', color=tc, zorder=7)
    ax.text(cx+1.12, yp-0.01, sub, ha='right', va='center',
        fontsize=9, color=tc, zorder=7)

ax.text(cx, BOX_Y+0.82, 'Automated LLM Judging', ha='center',
    fontsize=11, fontweight='bold', color=DARK, zorder=6)
ax.text(cx, BOX_Y+0.38, '4-dimension rubric · 0–8 score', ha='center',
    fontsize=10, color=GRAY, zorder=6)

# ══════════════════════════════════════════════════════════════════════════════
# EXAMPLE TRACE STRIP
# ══════════════════════════════════════════════════════════════════════════════
EX_Y = 0.20; EX_H = 2.60; EX_W = BOX_W

# Strip background
ax.add_patch(mpatches.Rectangle((0.30, EX_Y), W-0.60, EX_H,
    fc=XLGRAY, ec=LGRAY, lw=1.0, zorder=2))

# Left label — "Example Trace" rotated vertically
ax.text(COLS[0]-BOX_W/2-0.30, EX_Y+EX_H/2, 'Example\nTrace',
    ha='center', va='center', fontsize=10, color=GRAY,
    style='italic', fontweight='bold', zorder=5, linespacing=1.4)

# Per-cell type labels and contents
EX_CELLS = [
    (BLUE,   'API Specification',  False, [
        'ebay_buy/search_items.md',
        'GET /buy/browse/v1/',
        '    /item_summary/search',
        'params:  q,  limit,  ...',
    ]),
    (GREEN,  'Synthesized Tool',   True, [
        'def search_items(',
        '    q: str,',
        '    limit: int = 10,',
        ') -> list[Item]: ...',
    ]),
    (PURPLE, 'MCP Tool Call',      True, [
        'search_items(',
        '    q="laptop",',
        '    limit=5',
        ')',
    ]),
    (AMBER,  'Evaluation Task',    False, [
        '"Find the 5 cheapest',
        'laptops on eBay.',
        'Return title and',
        'current price."',
    ]),
    (PINK,   'Score:  7 / 8',      True, [
        'tool selection    2 / 2',
        'param quality     2 / 2',
        'result interp.    2 / 2',
        'task completion   1 / 2',
    ]),
]

HDR_EX  = 0.38   # height of per-cell type label band
LINE_SP = 0.34   # line spacing for content

for i, (cx, (color, type_lbl, mono, lines)) in enumerate(zip(COLS, EX_CELLS)):
    bx = cx - EX_W/2
    inner_x = bx + 0.10
    inner_w = EX_W - 0.20
    inner_y = EX_Y + 0.12
    inner_h = EX_H - 0.24

    # Cell border
    ax.add_patch(FancyBboxPatch((inner_x, inner_y), inner_w, inner_h,
        boxstyle="round,pad=0,rounding_size=0.10",
        fc='white', ec=color, lw=1.4, zorder=4))

    # Type label band
    ax.add_patch(FancyBboxPatch((inner_x, inner_y+inner_h-HDR_EX), inner_w, HDR_EX,
        boxstyle="round,pad=0,rounding_size=0.10",
        fc=color, ec='none', lw=0, zorder=5, alpha=1.0))
    ax.add_patch(mpatches.Rectangle((inner_x, inner_y+inner_h-HDR_EX),
        inner_w, HDR_EX*0.5, fc=color, ec='none', zorder=5))
    ax.text(inner_x + inner_w/2, inner_y+inner_h-HDR_EX/2, type_lbl,
        ha='center', va='center',
        fontsize=16.5, fontweight='bold', color='white', zorder=6)

    # Divider line below header
    div_y = inner_y + inner_h - HDR_EX
    ax.plot([inner_x+0.08, inner_x+inner_w-0.08], [div_y, div_y],
        color=color, lw=0.6, alpha=0.4, zorder=6)

    # Content lines
    content_top = div_y - 0.18
    ff = 'monospace' if mono else 'sans-serif'
    for j, line in enumerate(lines):
        ax.text(inner_x+0.16, content_top - j*LINE_SP, line,
            ha='left', va='top', fontsize=11,
            color=DARK if mono else '#374151',
            fontfamily=ff, zorder=5)

    # Phase 5: PASS pill below the score lines
    if i == 4:
        pill_y = content_top - 4*LINE_SP - 0.274
        ax.add_patch(FancyBboxPatch((cx-0.55, pill_y-0.02), 1.10, 0.34,
            boxstyle="round,pad=0,rounding_size=0.17",
            fc='#D1FAE5', ec='#047857', lw=1.4, zorder=6))
        ax.text(cx, pill_y+0.15, 'PASS', ha='center', va='center',
            fontsize=9.5, fontweight='bold', color='#065F46', zorder=7)

# Strip arrows
for i in range(4):
    x0 = COLS[i]+EX_W/2+0.10; x1 = COLS[i+1]-EX_W/2-0.10
    ax.annotate('', xy=(x1, EX_Y+EX_H/2), xytext=(x0, EX_Y+EX_H/2),
        arrowprops=dict(arrowstyle='->', color=GRAY, lw=1.5, mutation_scale=13), zorder=8)

# ══════════════════════════════════════════════════════════════════════════════
# TITLE
# ══════════════════════════════════════════════════════════════════════════════
ax.text(W/2, 10.70, 'MCP Tool Synthesis & Evaluation Benchmark Pipeline',
    ha='center', va='center', fontsize=17, fontweight='bold', color=DARK, zorder=10)
#ax.text(W/2, 11.30,
#    'Three LLMs: a Synthesis LLM generates MCP tools from API docs; '
#    'an Evaluation LLM completes tasks using those tools against live APIs; '
#    'a Judge LLM scores the trajectory.',
#    ha='center', va='center', fontsize=10, color=GRAY, zorder=10)

plt.tight_layout(pad=0.2)
plt.savefig('benchmark_pipeline.png', dpi=200, bbox_inches='tight', facecolor='white')
print("Saved benchmark_pipeline.png")
