"""
Conference pipeline figure (v4) — academic thesis style, MCP condition only.

Design principles:
  · Pure white canvas — blends into LaTeX page
  · Sharp rectangle corners (r=0.02)
  · Desaturated steel navy palette
  · Grayscale-safe score bar (hatching for pass zone)
  · Academic terminology throughout
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Arial', 'DejaVu Sans'],
    'pdf.fonttype': 42,
    'ps.fonttype':  42,
})

# ── Canvas ─────────────────────────────────────────────────────────────────────
W, H = 22, 6.4
fig, ax = plt.subplots(figsize=(W, H))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')

# ── Palette ─────────────────────────────────────────────────────────────────────
TEXT   = '#1A1A1A'
SUB    = '#555555'
BORDER = '#374151'
RULE   = '#C8D0DA'
LLM_EC = '#1F2937'

MCP_C  = '#2C3E6B'
MCP_L  = '#EDF0F7'

# ── Layout ─────────────────────────────────────────────────────────────────────
BOX_W  = 3.60
GAP    = 0.42
MAR    = (W - 5*BOX_W - 4*GAP) / 2
CXS    = [MAR + BOX_W/2 + i*(BOX_W+GAP) for i in range(5)]
BXS    = [cx - BOX_W/2 for cx in CXS]

BOX_Y  = 0.36
BOX_H  = 5.72
HDR_H  = 0.58
DESC_H = 0.64

CONT_BOT = BOX_Y + DESC_H
CONT_TOP = BOX_Y + BOX_H - HDR_H
MID_Y    = (CONT_BOT + CONT_TOP) / 2
ARROW_Y  = MID_Y

INNER_PAD = 0.18

# ── Helpers ────────────────────────────────────────────────────────────────────
def rrect(bx, by, bw, bh, fc='white', ec=BORDER, lw=0.75, r=0.02, zorder=3):
    ax.add_patch(FancyBboxPatch(
        (bx, by), bw, bh,
        boxstyle=f"round,pad=0,rounding_size={r}",
        fc=fc, ec=ec, lw=lw, zorder=zorder))

def llm_node(cx, cy, r, top, bot=None):
    ax.add_patch(plt.Circle((cx, cy), r, fc='white', ec=LLM_EC, lw=1.0, zorder=5))
    if bot:
        ax.text(cx, cy + r * 0.20, top, ha='center', va='center',
                fontsize=8.2, fontweight='bold', color=TEXT, zorder=6)
        ax.text(cx, cy - r * 0.28, bot, ha='center', va='center',
                fontsize=6.8, color=SUB, zorder=6)
    else:
        ax.text(cx, cy, top, ha='center', va='center',
                fontsize=8.2, fontweight='bold', color=TEXT, zorder=6)

def artifact_box(cx, cy, w, h, title, sub=None, fc='white', ec=BORDER,
                 title_color=None, zorder=5):
    rrect(cx - w/2, cy - h/2, w, h, fc=fc, ec=ec, lw=0.75, r=0.02, zorder=zorder)
    tc = title_color or ec
    if sub:
        ax.text(cx, cy + h * 0.15, title, ha='center', va='center',
                fontsize=7.8, fontweight='bold', color=tc, zorder=zorder + 1)
        ax.text(cx, cy - h * 0.25, sub, ha='center', va='center',
                fontsize=6.8, color=SUB, zorder=zorder + 1)
    else:
        ax.text(cx, cy, title, ha='center', va='center',
                fontsize=7.8, fontweight='bold', color=tc, zorder=zorder + 1)

# ══════════════════════════════════════════════════════════════════════════════
# Phase boxes
# ══════════════════════════════════════════════════════════════════════════════
HEADS = ['INPUT', 'SYNTHESIS', 'GENERATED\nTOOLS', 'AGENT\nEVALUATION',
         'LLM\nJUDGE']
DESCS = [
    ('API Documentation',         '14 APIs \u00b7 265 evaluation tasks'),
    ('Agentic Tool-Calling Loop', 'reads docs \u00b7 writes tool code'),
    ('MCP Server',                '@mcp.tool() decorated functions'),
    ('LLM Evaluation Agent',      'ReAct loop \u00b7 up to 15 turns per scenario'),
    ('LLM-as-Judge Scoring',      'binary PASS/FAIL \u00b7 failure cause \u00b7 server assessment'),
]

for i, cx in enumerate(CXS):
    bx = BXS[i]
    rrect(bx, BOX_Y, BOX_W, BOX_H, 'white', BORDER, lw=0.75, r=0.02)

    ax.text(bx + 0.20, BOX_Y + BOX_H - HDR_H / 2, str(i + 1),
            ha='center', va='center', fontsize=7.5, fontweight='bold',
            color=SUB, zorder=4)
    ax.text(cx + 0.10, BOX_Y + BOX_H - HDR_H / 2, HEADS[i],
            ha='center', va='center', fontsize=10.5, fontweight='bold',
            color=TEXT, zorder=4, linespacing=1.15)

    ax.plot([bx + 0.14, bx + BOX_W - 0.14], [BOX_Y + BOX_H - HDR_H] * 2,
            color=RULE, lw=0.8, zorder=3)
    ax.plot([bx + 0.14, bx + BOX_W - 0.14], [BOX_Y + DESC_H - 0.04] * 2,
            color=RULE, lw=0.6, zorder=3)

    d_title, d_sub = DESCS[i]
    ax.text(cx, BOX_Y + DESC_H * 0.66, d_title,
            ha='center', va='center', fontsize=8.2, fontweight='bold',
            color=TEXT, zorder=4)
    ax.text(cx, BOX_Y + DESC_H * 0.22, d_sub,
            ha='center', va='center', fontsize=6.8, color=SUB, zorder=4)

# ── Inter-phase arrows ──────────────────────────────────────────────────────────
for i in range(4):
    x0 = BXS[i] + BOX_W + 0.06
    x1 = BXS[i + 1] - 0.06
    ax.add_patch(mpatches.Rectangle(
        (x0 - 0.02, ARROW_Y - 0.10), (x1 - x0) + 0.04, 0.30,
        fc='white', ec='none', zorder=9))
    ax.annotate('', xy=(x1, ARROW_Y), xytext=(x0, ARROW_Y),
                arrowprops=dict(arrowstyle='->', color='#111827', lw=1.0,
                                mutation_scale=11), zorder=10)

# Label arrow 4 → 5 as "agent transcript"
x_a4 = BXS[3] + BOX_W + 0.06
x_a5 = BXS[4] - 0.06
ax.text((x_a4 + x_a5) / 2, ARROW_Y + 0.12, 'agent transcript',
        ha='center', va='bottom', fontsize=5.6, color=SUB, style='italic', zorder=10)

# ══════════════════════════════════════════════════════════════════════════════
# 1  INPUT
# ══════════════════════════════════════════════════════════════════════════════
cx = CXS[0]
artifact_box(cx, MID_Y, 3.10, 1.92,
             'API Docs  (docs/*.md)',
             'endpoint specifications',
             fc=MCP_L, ec=MCP_C, zorder=5)

# ══════════════════════════════════════════════════════════════════════════════
# 2  SYNTHESIS
# ══════════════════════════════════════════════════════════════════════════════
cx = CXS[1]

r2 = 0.84
circle_cy = MID_Y + 0.42
tool_y    = circle_cy - r2 - 0.28

llm_node(cx, circle_cy, r2, 'Synthesis', 'LLM')

for row_offset, row_text in [
    (+0.15, 'read  \u00b7  list  \u00b7  glob'),
    (-0.15, 'grep  \u00b7  write  \u00b7  edit'),
]:
    ax.text(cx, tool_y + row_offset, row_text,
            ha='center', va='center',
            fontsize=7.4, color=SUB,
            fontfamily='monospace', zorder=5)

# ══════════════════════════════════════════════════════════════════════════════
# 3  GENERATED TOOLS
# ══════════════════════════════════════════════════════════════════════════════
cx = CXS[2]

MCP_CARDS = [
    ('Tool Functions',  'Synthesized Toolset (N)  \u00b7  @mcp.tool()'),
    ('API Client',      'auth + HTTP'),
    ('MCP Protocol',    'FastMCP'),
]
cw, ch, cgap = 3.10, 0.52, 0.16
stack_h = len(MCP_CARDS) * ch + (len(MCP_CARDS) - 1) * cgap
top_cy = MID_Y + stack_h / 2 - ch / 2
for j, (title, sub) in enumerate(MCP_CARDS):
    artifact_box(cx, top_cy - j * (ch + cgap), cw, ch,
                 title, sub, fc=MCP_L, ec=MCP_C, title_color=MCP_C, zorder=5)

# ══════════════════════════════════════════════════════════════════════════════
# 4  AGENT EVALUATION  — Eval LLM  ←→  Live API
# ══════════════════════════════════════════════════════════════════════════════
cx = CXS[3]
r_e = 0.64

ecx = cx - 0.74
llm_node(ecx, MID_Y, r_e, 'Eval.', 'LLM')

api_left = ecx + r_e + 0.38
aw, ah = 1.14, 0.90
api_cx = api_left + aw / 2

arr_gap = 0.10
ax.annotate('', xy=(api_left - 0.02, MID_Y + arr_gap),
            xytext=(ecx + r_e + 0.06, MID_Y + arr_gap),
            arrowprops=dict(arrowstyle='->', color=MCP_C, lw=0.9,
                            mutation_scale=9), zorder=8)
ax.annotate('', xy=(ecx + r_e + 0.06, MID_Y - arr_gap),
            xytext=(api_left - 0.02, MID_Y - arr_gap),
            arrowprops=dict(arrowstyle='->', color=MCP_C, lw=0.9,
                            mutation_scale=9), zorder=8)

rrect(api_left, MID_Y - ah / 2, aw, ah, MCP_L, MCP_C, lw=0.75, r=0.02, zorder=5)
ax.text(api_cx, MID_Y + 0.09, 'Live', ha='center', va='center',
        fontsize=7.8, fontweight='bold', color=MCP_C, zorder=6)
ax.text(api_cx, MID_Y - 0.12, 'API',  ha='center', va='center',
        fontsize=7.8, fontweight='bold', color=MCP_C, zorder=6)

ax.text((ecx + api_cx) / 2, MID_Y - r_e - 0.30,
        'via synthesized MCP tools',
        ha='center', va='center', fontsize=6.6, color=SUB, style='italic', zorder=6)

# ══════════════════════════════════════════════════════════════════════════════
# 5  LLM JUDGE
# ══════════════════════════════════════════════════════════════════════════════
cx = CXS[4]
panel_x = cx - 1.44
panel_w  = 2.88

v_row_h = 0.50
VERD = [
    ('PASS',      'outcome = PASS',       '#F5F5F5'),
    ('FAIL',      'tool quality failure', '#E8E8E8'),
    ('INDETERM.', 'agent / env / task',   '#DCDCDC'),
]
verdict_h = len(VERD) * v_row_h   # 1.50

fc_row_h, fc_colgap, fc_rowgap = 0.28, 0.08, 0.10
FCAUSES = [
    ('TOOL_COVERAGE',       'TOOL_SCHEMA'),
    ('TOOL_IMPLEMENTATION', 'TOOL_DOCUMENTATION'),
]
fc_cw      = (panel_w - fc_colgap) / 2
fc_panel_h = len(FCAUSES) * fc_row_h + (len(FCAUSES) - 1) * fc_rowgap  # 0.66

sv_h = 0.34

# Centre the full block vertically
block_h5 = (
    0.22 + 0.06        # "Task Verdict" label + gap
    + verdict_h        # 1.50
    + 0.14             # gap
    + 0.18 + 0.06      # "Failure cause" label + gap
    + fc_panel_h       # 0.66
    + 0.26             # gap
    + 0.18 + 0.06      # "Server Assessment" label + gap
    + sv_h             # 0.34
)
margin5 = (CONT_TOP - CONT_BOT - block_h5) / 2
y = CONT_TOP - margin5   # draw-head, advances downward

# ── Task Verdict label + rule ─────────────────────────────────────────────────
ax.plot([panel_x + 0.10, panel_x + panel_w - 0.10], [y - 0.04] * 2,
        color=RULE, lw=0.6, zorder=6)
ax.text(cx, y - 0.11, 'Task Verdict',
        ha='center', va='center', fontsize=6.0, color=SUB, style='italic', zorder=6)
y -= 0.22 + 0.06

# ── Verdict panel ─────────────────────────────────────────────────────────────
v_top = y
for k, (lbl, sub, shade) in enumerate(VERD):
    vy = v_top - k * v_row_h - v_row_h / 2
    ax.add_patch(mpatches.Rectangle(
        (panel_x, vy - v_row_h / 2), panel_w, v_row_h,
        fc=shade, ec='none', zorder=5))
    if k < len(VERD) - 1:
        ax.plot([panel_x, panel_x + panel_w], [vy - v_row_h / 2] * 2,
                color=RULE, lw=0.5, zorder=6)

rrect(panel_x, v_top - verdict_h, panel_w, verdict_h,
      'none', BORDER, lw=0.75, r=0.02, zorder=7)

for k, (lbl, sub, shade) in enumerate(VERD):
    vy = v_top - k * v_row_h - v_row_h / 2
    ax.text(panel_x + 0.18, vy, lbl,
            ha='left', va='center', fontsize=7.4, fontweight='bold',
            color=TEXT, zorder=8)
    ax.text(panel_x + panel_w - 0.18, vy, sub,
            ha='right', va='center', fontsize=7.0, color=SUB, zorder=8)
y -= verdict_h + 0.14

# ── Failure cause taxonomy ────────────────────────────────────────────────────
ax.text(cx, y - 0.09, 'Failure cause (when FAIL)',
        ha='center', va='center', fontsize=5.8, color=SUB, style='italic', zorder=6)
y -= 0.18 + 0.06

for r_idx, row_pair in enumerate(FCAUSES):
    fc_y = y - r_idx * (fc_row_h + fc_rowgap) - fc_row_h / 2
    for c_idx, code in enumerate(row_pair):
        fx = panel_x + c_idx * (fc_cw + fc_colgap)
        rrect(fx, fc_y - fc_row_h / 2, fc_cw, fc_row_h,
              '#F8F8F8', BORDER, lw=0.5, r=0.02, zorder=5)
        ax.text(fx + fc_cw / 2, fc_y, code,
                ha='center', va='center',
                fontsize=5.6, color=SUB, fontfamily='monospace', zorder=6)
y -= fc_panel_h + 0.26

# ── Server Assessment label + box ─────────────────────────────────────────────
ax.plot([panel_x + 0.10, panel_x + panel_w - 0.10], [y - 0.04] * 2,
        color=RULE, lw=0.6, zorder=6)
ax.text(cx, y - 0.11, 'Server Assessment',
        ha='center', va='center', fontsize=6.0, color=SUB, style='italic', zorder=6)
y -= 0.18 + 0.06

sv_y = y - sv_h
rrect(panel_x, sv_y, panel_w, sv_h, '#F5F5F5', BORDER, lw=0.75, r=0.02, zorder=5)
ax.text(cx, sv_y + sv_h * 0.62, 'Server Sufficient',
        ha='center', va='center', fontsize=6.8, fontweight='bold',
        color=TEXT, zorder=6)
ax.text(cx, sv_y + sv_h * 0.22, 'YES  \u00b7  NO  \u00b7  UNKN.',
        ha='center', va='center', fontsize=6.4, color=SUB, zorder=6)

# ── Save ───────────────────────────────────────────────────────────────────────
plt.tight_layout(pad=0.1)
plt.savefig('benchmark_pipeline_v4.png', dpi=200, bbox_inches='tight',
            facecolor='white')
print("Saved benchmark_pipeline_v4.png")
