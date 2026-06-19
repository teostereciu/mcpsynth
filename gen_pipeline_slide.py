"""
Slide pipeline figure — MCP-only, updated eval strategy.
16:9 canvas optimised for presentation.

Theme: light steel-blue background, deep blue MCP accent.
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

# ── Canvas (16:9) ─────────────────────────────────────────────────────────────
W, H = 22, 12.375
fig, ax = plt.subplots(figsize=(W, H))
BG = '#EEF2F7'
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')

# ── Palette ───────────────────────────────────────────────────────────────────
TEXT   = '#0F172A'
SUB    = '#4B5E78'
BORDER = '#60748B'
RULE   = '#B0C0D0'
LLM_EC = '#1E293B'
MCP_C  = '#1D4ED8'   # blue-700
MCP_L  = '#EFF6FF'   # blue-50

# ── Layout ────────────────────────────────────────────────────────────────────
BOX_W  = 3.60
GAP    = 0.54
MAR    = (W - 5*BOX_W - 4*GAP) / 2
CXS    = [MAR + BOX_W/2 + i*(BOX_W+GAP) for i in range(5)]
BXS    = [cx - BOX_W/2 for cx in CXS]

BOX_Y  = 0.55
BOX_H  = 10.80
HDR_H  = 1.00
DESC_H = 1.10

CONT_BOT = BOX_Y + DESC_H          # 1.65
CONT_TOP = BOX_Y + BOX_H - HDR_H   # 10.35
MID_Y    = (CONT_BOT + CONT_TOP) / 2  # 6.00
ARROW_Y  = MID_Y

# ── Helpers ───────────────────────────────────────────────────────────────────
def rrect(bx, by, bw, bh, fc=BG, ec=BORDER, lw=1.4, r=0.14, zorder=3):
    ax.add_patch(FancyBboxPatch(
        (bx, by), bw, bh,
        boxstyle=f"round,pad=0,rounding_size={r}",
        fc=fc, ec=ec, lw=lw, zorder=zorder))

def llm_node(cx, cy, r, top, bot=None, lw=2.2):
    ax.add_patch(plt.Circle((cx, cy), r, fc='white', ec=LLM_EC, lw=lw, zorder=5))
    if bot:
        ax.text(cx, cy + r*0.20, top, ha='center', va='center',
                fontsize=24, fontweight='bold', color=TEXT, zorder=6)
        ax.text(cx, cy - r*0.28, bot, ha='center', va='center',
                fontsize=18, color=SUB, zorder=6)
    else:
        ax.text(cx, cy, top, ha='center', va='center',
                fontsize=18, fontweight='bold', color=TEXT, zorder=6)

def artifact_box(cx, cy, w, h, title, sub=None, fc='white', ec=BORDER,
                 title_color=None, zorder=5):
    rrect(cx - w/2, cy - h/2, w, h, fc=fc, ec=ec, lw=1.8, r=0.16, zorder=zorder)
    tc = title_color or ec
    if sub:
        ax.text(cx, cy + h*0.15, title, ha='center', va='center',
                fontsize=16, fontweight='bold', color=tc, zorder=zorder+1)
        ax.text(cx, cy - h*0.24, sub, ha='center', va='center',
                fontsize=11.5, color=SUB, zorder=zorder+1)
    else:
        ax.text(cx, cy, title, ha='center', va='center',
                fontsize=16, fontweight='bold', color=tc, zorder=zorder+1)

# ══════════════════════════════════════════════════════════════════════════════
# Phase boxes
# ══════════════════════════════════════════════════════════════════════════════
HEADS = ['INPUT', 'SYNTHESIS', 'GENERATED\nTOOLS', 'AGENT\nEVALUATION', 'LLM\nJUDGE']
DESCS = [
    ('API Documentation',         '14 APIs \u00b7 265 evaluation tasks'),
    ('Agentic Tool-Calling Loop', 'reads docs \u00b7 writes tool code \u00b7 up to 100 turns'),
    ('MCP Server',                '@mcp.tool() decorated functions'),
    ('LLM Evaluation Agent',      'ReAct loop \u00b7 up to 15 turns per scenario'),
    ('LLM-as-Judge Scoring',      'task pass \u00b7 failure cause \u00b7 server assessment'),
]

for i, cx in enumerate(CXS):
    bx = BXS[i]
    rrect(bx, BOX_Y, BOX_W, BOX_H, 'white', BORDER, lw=1.8, r=0.20)

    ax.text(bx + 0.34, BOX_Y + BOX_H - HDR_H/2, str(i+1),
            ha='center', va='center', fontsize=13, fontweight='bold',
            color=SUB, zorder=4)
    ax.text(cx + 0.17, BOX_Y + BOX_H - HDR_H/2, HEADS[i],
            ha='center', va='center', fontsize=19, fontweight='bold',
            color=TEXT, zorder=4, linespacing=1.15)

    ax.plot([bx + 0.22, bx + BOX_W - 0.22], [BOX_Y + BOX_H - HDR_H]*2,
            color=RULE, lw=1.4, zorder=3)
    ax.plot([bx + 0.22, bx + BOX_W - 0.22], [BOX_Y + DESC_H - 0.06]*2,
            color=RULE, lw=1.0, zorder=3)

    d_title, d_sub = DESCS[i]
    ax.text(cx, BOX_Y + DESC_H*0.66, d_title,
            ha='center', va='center', fontsize=14, fontweight='bold',
            color=TEXT, zorder=4)
    ax.text(cx, BOX_Y + DESC_H*0.24, d_sub,
            ha='center', va='center', fontsize=11.5, color=SUB, zorder=4)

# ── Inter-phase arrows ────────────────────────────────────────────────────────
for i in range(4):
    x0 = BXS[i] + BOX_W + 0.06
    x1 = BXS[i+1] - 0.06
    ax.add_patch(mpatches.Rectangle(
        (x0 - 0.02, ARROW_Y - 0.24), (x1 - x0) + 0.04, 0.64,
        fc=BG, ec='none', zorder=9))
    ax.annotate('', xy=(x1, ARROW_Y), xytext=(x0, ARROW_Y),
                arrowprops=dict(arrowstyle='->', color='#334155', lw=2.4,
                                mutation_scale=24), zorder=10)

# Label arrow 4 → 5
x_a4 = BXS[3] + BOX_W + 0.06
x_a5 = BXS[4] - 0.06
#ax.text((x_a4 + x_a5)/2, ARROW_Y + 0.24, 'agent\ntranscript',
#        ha='center', va='bottom', fontsize=10.0, color=SUB, style='italic',
#        linespacing=1.2, zorder=10)

# ══════════════════════════════════════════════════════════════════════════════
# 1  INPUT
# ══════════════════════════════════════════════════════════════════════════════
cx = CXS[0]
artifact_box(cx, MID_Y, 3.10, 3.60,
             'API Docs  (docs/*.md)',
             'scrapped endpoint specs\nfrom online docs',
             fc=MCP_L, ec=MCP_C, zorder=5)

# ══════════════════════════════════════════════════════════════════════════════
# 2  SYNTHESIS
# ══════════════════════════════════════════════════════════════════════════════
cx = CXS[1]

r2 = 1.35
circle_cy = MID_Y + 0.40
tool_y    = circle_cy - r2 - 0.52

llm_node(cx, circle_cy, r2, 'Synthesis', 'LLM')

for row_offset, row_text in [
    (+0.28, 'read  \u00b7  list  \u00b7  glob'),
    (-0.28, 'grep  \u00b7  write  \u00b7  edit'),
]:
    ax.text(cx, tool_y + row_offset, row_text,
            ha='center', va='center',
            fontsize=13, color=SUB, fontfamily='monospace', zorder=5)

# ══════════════════════════════════════════════════════════════════════════════
# 3  GENERATED TOOLS
# ══════════════════════════════════════════════════════════════════════════════
cx = CXS[2]

MCP_CARDS = [
    ('Tool Functions',  'Synthesized Toolset (N)  \u00b7  @mcp.tool()'),
    ('API Client',      'auth + HTTP'),
    ('MCP Protocol',    'FastMCP'),
]
cw, ch, cgap = 3.10, 1.00, 0.30
stack_h = len(MCP_CARDS)*ch + (len(MCP_CARDS)-1)*cgap
top_cy = MID_Y + stack_h/2 - ch/2
for j, (title, sub) in enumerate(MCP_CARDS):
    artifact_box(cx, top_cy - j*(ch+cgap), cw, ch,
                 title, sub, fc=MCP_L, ec=MCP_C, title_color=MCP_C, zorder=5)

# ══════════════════════════════════════════════════════════════════════════════
# 4  AGENT EVALUATION  — Eval LLM ↔ Live API
# ══════════════════════════════════════════════════════════════════════════════
cx = CXS[3]
r_e = 0.88

ecx = cx - 0.72
llm_node(ecx, MID_Y, r_e, 'Eval.', 'LLM')

api_left = ecx + r_e + 0.34
aw, ah = 1.10, 1.76
api_cx = api_left + aw/2

arr_gap = 0.18
ax.annotate('', xy=(api_left - 0.02, MID_Y + arr_gap),
            xytext=(ecx + r_e + 0.08, MID_Y + arr_gap),
            arrowprops=dict(arrowstyle='->', color=MCP_C, lw=1.6,
                            mutation_scale=18), zorder=8)
ax.annotate('', xy=(ecx + r_e + 0.08, MID_Y - arr_gap),
            xytext=(api_left - 0.02, MID_Y - arr_gap),
            arrowprops=dict(arrowstyle='->', color=MCP_C, lw=1.6,
                            mutation_scale=18), zorder=8)

rrect(api_left, MID_Y - ah/2, aw, ah, MCP_L, MCP_C, lw=1.8, r=0.14, zorder=5)
ax.text(api_cx, MID_Y + 0.18, 'Live', ha='center', va='center',
        fontsize=16, fontweight='bold', color=MCP_C, zorder=6)
ax.text(api_cx, MID_Y - 0.24, 'API', ha='center', va='center',
        fontsize=16, fontweight='bold', color=MCP_C, zorder=6)

ax.text((ecx + api_cx)/2, MID_Y - r_e - 0.56,
        'via synthesized MCP tools',
        ha='center', va='center', fontsize=12, color=SUB, style='italic', zorder=6)

# ══════════════════════════════════════════════════════════════════════════════
# 5  LLM JUDGE
# ══════════════════════════════════════════════════════════════════════════════
cx = CXS[4]
panel_x = cx - 1.44
panel_w  = 2.88

v_row_h = 0.86
VERD = [
    ('PASS',      'outcome = PASS',       '#E4EAF4'),
    ('FAIL',      'tool quality failure', '#D4DCE8'),
    ('INDETERM.', 'agent / env / task',   '#C4CEDC'),
]
verdict_h = len(VERD) * v_row_h   # 2.58

fc_row_h, fc_colgap, fc_rowgap = 0.50, 0.14, 0.18
FCAUSES = [
    ('TOOL_COVERAGE',  'TOOL_SCHEMA'),
    ('TOOL_IMPL.',     'TOOL_DOCS'),
]
fc_cw      = (panel_w - fc_colgap) / 2
fc_panel_h = len(FCAUSES)*fc_row_h + (len(FCAUSES)-1)*fc_rowgap   # 1.18

sv_h = 0.60

block_h5 = (
    0.38 + 0.16        # "Task Verdict" label + gap
    + verdict_h        # 2.58
    + 0.48             # gap
    + 0.36 + 0.14      # "Failure cause" label + gap
    + fc_panel_h       # 1.18
    + 0.76             # gap
    + 0.36 + 0.14      # "Server Assessment" label + gap
    + sv_h             # 0.60
)
margin5 = (CONT_TOP - CONT_BOT - block_h5) / 2
y = CONT_TOP - margin5

# ── Task Verdict label + rule ─────────────────────────────────────────────────
ax.plot([panel_x + 0.14, panel_x + panel_w - 0.14], [y - 0.08]*2,
        color=RULE, lw=1.0, zorder=6)
ax.text(cx, y + 0.16, 'Task Verdict',
        ha='center', va='center', fontsize=14, color=SUB, style='italic', zorder=6)
y -= 0.38 + 0.16

# ── Verdict panel ─────────────────────────────────────────────────────────────
v_top = y
for k, (lbl, sub, shade) in enumerate(VERD):
    vy = v_top - k*v_row_h - v_row_h/2
    ax.add_patch(mpatches.Rectangle(
        (panel_x, vy - v_row_h/2), panel_w, v_row_h,
        fc=shade, ec='none', zorder=5))
    if k < len(VERD) - 1:
        ax.plot([panel_x, panel_x + panel_w], [vy - v_row_h/2]*2,
                color=RULE, lw=0.8, zorder=6)

rrect(panel_x, v_top - verdict_h, panel_w, verdict_h,
      'none', BORDER, lw=1.6, r=0.14, zorder=7)

for k, (lbl, sub, shade) in enumerate(VERD):
    vy = v_top - k*v_row_h - v_row_h/2
    ax.text(panel_x + 0.22, vy, lbl,
            ha='left', va='center', fontsize=14, fontweight='bold',
            color=TEXT, zorder=8)
    ax.text(panel_x + panel_w - 0.22, vy, sub,
            ha='right', va='center', fontsize=12, color=SUB, zorder=8)
y -= verdict_h + 0.48

# ── Failure cause taxonomy ────────────────────────────────────────────────────
ax.text(cx, y - 0.18, 'Failure cause (when FAIL)',
        ha='center', va='center', fontsize=10.5, color=SUB, style='italic', zorder=6)
y -= 0.36 + 0.14

for r_idx, row_pair in enumerate(FCAUSES):
    fc_y = y - r_idx*(fc_row_h + fc_rowgap) - fc_row_h/2
    for c_idx, code in enumerate(row_pair):
        fx = panel_x + c_idx*(fc_cw + fc_colgap)
        rrect(fx, fc_y - fc_row_h/2, fc_cw, fc_row_h,
              'white', BORDER, lw=1.0, r=0.10, zorder=5)
        ax.text(fx + fc_cw/2, fc_y, code,
                ha='center', va='center',
                fontsize=10.5, color=SUB, fontfamily='monospace', zorder=6)
y -= fc_panel_h + 0.76

# ── Server Assessment label + box ─────────────────────────────────────────────
ax.plot([panel_x + 0.14, panel_x + panel_w - 0.14], [y - 0.08]*2,
        color=RULE, lw=1.0, zorder=6)
ax.text(cx, y + 0.16, 'Server Assessment',
        ha='center', va='center', fontsize=14, color=SUB, style='italic', zorder=6)
y -= 0.36 + 0.14

sv_y = y - sv_h
rrect(panel_x, sv_y, panel_w, sv_h, '#E4EAF4', BORDER, lw=1.6, r=0.14, zorder=5)
ax.text(cx, sv_y + sv_h*0.62, 'Server Sufficient',
        ha='center', va='center', fontsize=13, fontweight='bold',
        color=TEXT, zorder=6)
ax.text(cx, sv_y + sv_h*0.22, 'YES  \u00b7  NO  \u00b7  UNKN.',
        ha='center', va='center', fontsize=11.5, color=SUB, zorder=6)

# ── Save ──────────────────────────────────────────────────────────────────────
plt.tight_layout(pad=0.1)
plt.savefig('benchmark_pipeline_slide.png', dpi=150, bbox_inches='tight',
            facecolor=BG)
print("Saved benchmark_pipeline_slide.png")
