"""
Conference-ready benchmark pipeline figure (v2).

Conditions shown:
  MCP condition:  docs/*.md  → Synthesis LLM → MCP server (@mcp.tool()) → N specific tools
  CLI condition:  source/    → Synthesis LLM → CLI script (*_cli.py)    → 1 run_command tool

Phases 1, 3, 4 are split horizontally (MCP top / CLI bottom).
Phases 2 and 5 are common to both conditions.

Synthesis tools (from advanced_agentic_chomsky.py TOOLS list):
  read_file, list_directory, glob, grep, write_file, edit_file  (+optional bash)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Polygon
import numpy as np

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Arial', 'DejaVu Sans'],
    'pdf.fonttype': 42,
    'ps.fonttype':  42,
})

# ── Canvas ────────────────────────────────────────────────────────────────────
W, H = 22, 7.2
fig, ax = plt.subplots(figsize=(W, H))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')

# ── Palette ───────────────────────────────────────────────────────────────────
C = ['#1C5FA4', '#1D7A52', '#5E38A6', '#A85910', '#962050']  # phase accents
L = ['#EEF3FB', '#EEF7F3', '#F2EFF9', '#FAF1EA', '#F9ECF2']  # box backgrounds
M = ['#BDD0EE', '#AAD9C5', '#C9BAF2', '#ECC89E', '#EBB8D0']  # mid tones

DARK   = '#1F2937'
GRAY   = '#6B7280'
LGRAY  = '#D1D5DB'
XLGRAY = '#F3F4F6'

# Condition colours — used for split-box labels and accent lines
MCP_C = '#1C5FA4'   # blue — MCP condition
CLI_C = '#A85910'   # sienna — CLI condition

# ── Layout ────────────────────────────────────────────────────────────────────
BOX_W  = 3.60
GAP    = 0.56
MAR    = (W - 5*BOX_W - 4*GAP) / 2   # ≈ 0.88
CXS    = [MAR + BOX_W/2 + i*(BOX_W+GAP) for i in range(5)]

BOX_Y  = 0.40
BOX_H  = 6.40
HDR_H  = 0.68
DESC_H = 0.88

CONT_BOT  = BOX_Y + DESC_H             # ≈ 1.28
CONT_TOP  = BOX_Y + BOX_H - HDR_H     # ≈ 6.12
SPLIT_Y   = (CONT_BOT + CONT_TOP) / 2 # ≈ 3.70  — condition split line

UPPER_MID = (SPLIT_Y + CONT_TOP) / 2  # ≈ 4.91  — MCP half centre
LOWER_MID = (CONT_BOT + SPLIT_Y) / 2  # ≈ 2.49  — CLI half centre

# Arrows flow at the split line so they lie between the two conditions
ARROW_Y = SPLIT_Y

# ── Drawing helpers ───────────────────────────────────────────────────────────
def rrect(bx, by, bw, bh, fc, ec, lw=1.1, r=0.14, zorder=3, alpha=1.0):
    ax.add_patch(FancyBboxPatch(
        (bx, by), bw, bh,
        boxstyle=f"round,pad=0,rounding_size={r}",
        fc=fc, ec=ec, lw=lw, zorder=zorder, alpha=alpha))

def pill(cx, cy, w, h, fc, ec, lw=0.9, zorder=5):
    rrect(cx - w/2, cy - h/2, w, h, fc, ec, lw=lw, r=h/2, zorder=zorder)

def chip(cx, cy, text, fc, tc, fs=7.8, zorder=6):
    tw = len(text) * 0.074 + 0.30
    pill(cx, cy, tw, 0.27, fc, tc, lw=0.8, zorder=zorder)
    ax.text(cx, cy, text, ha='center', va='center',
            fontsize=fs, fontweight='bold', color=tc, zorder=zorder+1)

def llm_circle(cx, cy, r, color, line1, line2=None):
    ax.add_patch(plt.Circle((cx, cy), r, fc='white', ec=color, lw=1.8, zorder=5))
    if line2:
        ax.text(cx, cy + r*0.22, line1, ha='center', va='center',
                fontsize=8.2, fontweight='bold', color=color, zorder=6)
        ax.text(cx, cy - r*0.28, line2, ha='center', va='center',
                fontsize=7.2, color=color, zorder=6)
    else:
        ax.text(cx, cy, line1, ha='center', va='center',
                fontsize=8.2, fontweight='bold', color=color, zorder=6)

def doc_icon(ox, oy, w, h, fc, ec, mid):
    fold = h * 0.22
    ax.add_patch(Polygon([
        (ox, oy), (ox+w-fold, oy), (ox+w, oy+fold),
        (ox+w, oy+h), (ox, oy+h)],
        closed=True, fc=fc, ec=ec, lw=1.0, zorder=5))
    ax.add_patch(Polygon([
        (ox+w-fold, oy), (ox+w, oy+fold), (ox+w-fold, oy+fold)],
        closed=True, fc=mid, ec=ec, lw=0.7, zorder=6, alpha=0.55))
    for j in range(3):
        ly = oy + fold + 0.08 + j*(h - fold - 0.14)/3
        ax.plot([ox+0.08, ox+w-0.08], [ly, ly],
                color=ec, lw=0.7, alpha=0.28, zorder=6)

def slot_card(cx, cy, w, h, title, subtitle, color, zorder=5):
    rrect(cx - w/2, cy - h/2, w, h, 'white', color, lw=0.9, r=0.09, zorder=zorder)
    ax.text(cx, cy + h*0.15, title, ha='center', va='center',
            fontsize=8.0, fontweight='bold', color=color, zorder=zorder+1)
    ax.text(cx, cy - h*0.25, subtitle, ha='center', va='center',
            fontsize=7.0, color=GRAY, zorder=zorder+1)

def condition_divider(i):
    """Draw the MCP/CLI split line inside phase box i."""
    cx = CXS[i]; bx = cx - BOX_W/2; color = C[i]
    ax.plot([bx + 0.18, bx + BOX_W - 0.18], [SPLIT_Y, SPLIT_Y],
            color=LGRAY, lw=0.9, ls='--', zorder=4)
    # Condition pills on the left edge of each half
    for label, cy_lbl, fc, tc in [
        ('MCP', SPLIT_Y + 0.17, L[0], MCP_C),
        ('CLI', SPLIT_Y - 0.17, '#FAF4EE', CLI_C),
    ]:
        tw = 0.54
        rrect(bx + 0.16, cy_lbl - 0.12, tw, 0.24, fc, tc, lw=0.9, r=0.12, zorder=6)
        ax.text(bx + 0.16 + tw/2, cy_lbl, label, ha='center', va='center',
                fontsize=6.4, fontweight='bold', color=tc, zorder=7)

# ══════════════════════════════════════════════════════════════════════════════
# Phase boxes
# ══════════════════════════════════════════════════════════════════════════════
NUMS  = ['1', '2', '3', '4', '5']
HEADS = ['INPUT', 'SYNTHESIS', 'GENERATED\nTOOLS', 'AGENT\nEVALUATION', 'LLM JUDGE']
DESCS = [
    ('API Docs  ·  Source Code',     '17 APIs · 330 scenarios · 2 conditions'),
    ('Agentic Tool-Calling Loop',    'reads docs or source · writes tool code'),
    ('MCP Server  ·  CLI Script',    '@mcp.tool() or argparse subcommands'),
    ('LLM Evaluation Agent',         'ReAct loop · up to 20 turns per scenario'),
    ('Automated Scoring',            '4-dim. rubric · 0–8 points'),
]

for i, cx in enumerate(CXS):
    bx = cx - BOX_W/2; color = C[i]; light = L[i]

    rrect(bx, BOX_Y, BOX_W, BOX_H, light, color, lw=1.3, r=0.20, zorder=2)

    # Header band
    rrect(bx, BOX_Y+BOX_H-HDR_H, BOX_W, HDR_H, color, 'none', lw=0, r=0.20, zorder=3)
    ax.add_patch(mpatches.Rectangle(
        (bx, BOX_Y+BOX_H-HDR_H), BOX_W, HDR_H*0.50, fc=color, ec='none', zorder=3))
    ax.text(bx + 0.38, BOX_Y+BOX_H-HDR_H/2, NUMS[i],
            ha='center', va='center', fontsize=11, fontweight='bold',
            color='white', alpha=0.38, zorder=5)
    ax.text(cx + 0.15, BOX_Y+BOX_H-HDR_H/2, HEADS[i],
            ha='center', va='center', fontsize=10.5, fontweight='bold',
            color='white', zorder=5, linespacing=1.15)

    # Separator above description
    ax.plot([bx+0.24, bx+BOX_W-0.24], [BOX_Y+DESC_H-0.05]*2,
            color=color, lw=0.6, alpha=0.28, zorder=4)
    d_title, d_sub = DESCS[i]
    ax.text(cx, BOX_Y + DESC_H*0.63, d_title,
            ha='center', va='center', fontsize=8.8, fontweight='bold',
            color=DARK, zorder=4)
    ax.text(cx, BOX_Y + DESC_H*0.20, d_sub,
            ha='center', va='center', fontsize=7.4, color=GRAY, zorder=4)

# ── Arrows between phases ──────────────────────────────────────────────────────
ALABS = ['docs or\nsource', 'synthesizes', 'server or\nscript', 'eval trace']
for i, lbl in enumerate(ALABS):
    x0 = CXS[i]   + BOX_W/2 + 0.07
    x1 = CXS[i+1] - BOX_W/2 - 0.07
    xm = (x0 + x1) / 2
    ax.annotate('', xy=(x1, ARROW_Y), xytext=(x0, ARROW_Y),
                arrowprops=dict(arrowstyle='->', color=DARK, lw=1.8,
                                mutation_scale=16), zorder=10)
    ax.text(xm, ARROW_Y + 0.16, lbl, ha='center', va='bottom',
            fontsize=7.2, color=GRAY, style='italic', zorder=11, linespacing=1.2,
            bbox=dict(boxstyle='square,pad=0.06', fc='white', ec='none', zorder=1))

# ══════════════════════════════════════════════════════════════════════════════
# 1  INPUT  (split: MCP top / CLI bottom)
# ══════════════════════════════════════════════════════════════════════════════
condition_divider(0)
cx = CXS[0]

# ── MCP half: small stacked doc icons ──
doc_top = UPPER_MID + 0.28   # centre of the front doc
for k, (dx, dy) in enumerate([(-0.10, -0.12), (0.0, 0.0)]):
    doc_icon(cx - 0.42 + dx, doc_top - 0.52 + dy,
             w=0.80, h=1.00,
             fc='white' if k == 1 else L[0], ec=C[0], mid=M[0])
# .md badge
rrect(cx - 0.22, doc_top - 0.60, 0.44, 0.22, C[0], 'none', lw=0, r=0.05, zorder=7)
ax.text(cx, doc_top - 0.49, '.md', ha='center', va='center',
        fontsize=6.8, fontweight='bold', color='white', zorder=8)
ax.text(cx, doc_top - 0.76, 'API docs/*.md', ha='center', va='center',
        fontsize=7.2, color=C[0], fontweight='bold', zorder=6)

# ── CLI half: source-tree card ──
src_cy = LOWER_MID + 0.04
src_w, src_h = 2.10, 1.02
rrect(cx - src_w/2, src_cy - src_h/2, src_w, src_h, 'white', CLI_C, lw=1.0, r=0.10, zorder=5)
# Folder tab header
rrect(cx - src_w/2, src_cy + src_h/2 - 0.30, src_w, 0.30, '#FAF4EE', 'none',
      lw=0, r=0.10, zorder=6)
ax.add_patch(mpatches.Rectangle(
    (cx - src_w/2, src_cy + src_h/2 - 0.30), src_w, 0.15,
    fc='#FAF4EE', ec='none', zorder=6))
ax.text(cx, src_cy + src_h/2 - 0.15, 'source/', ha='center', va='center',
        fontsize=7.8, fontweight='bold', color=CLI_C, zorder=7)
# Code lines
for j, line in enumerate(['▸  models.py', '▸  views.py', '▸  urls.py']):
    ax.text(cx - src_w/2 + 0.14, src_cy + src_h/2 - 0.38 - j*0.19, line,
            ha='left', va='top', fontsize=6.8, color=GRAY, fontfamily='monospace', zorder=6)
ax.text(cx, src_cy - src_h/2 - 0.14, 'full source tree', ha='center', va='top',
        fontsize=7.2, color=CLI_C, fontweight='bold', zorder=6)

# ══════════════════════════════════════════════════════════════════════════════
# 2  SYNTHESIS  (common — no split)
#    Tools: read_file, list_directory, glob, grep, write_file, edit_file
# ══════════════════════════════════════════════════════════════════════════════
cx = CXS[1]

r2 = 0.86
# Centre the circle + 2-row chip grid in the content area
row2_y   = CONT_BOT + 0.46
row1_y   = row2_y + 0.40
circ_bot = row1_y + 0.135 + 0.36   # chip top + gap
circ_cy  = circ_bot + r2

llm_circle(cx, circ_cy, r2, C[1], 'Synthesis', 'LLM')

TOOLS_ROW1 = ['read',   'list',  'glob']
TOOLS_ROW2 = ['grep',   'write', 'edit']
for k, tool in enumerate(TOOLS_ROW1):
    chip(cx - 0.80 + k*0.80, row1_y, tool, L[1], C[1], fs=7.8)
for k, tool in enumerate(TOOLS_ROW2):
    chip(cx - 0.80 + k*0.80, row2_y, tool, L[1], C[1], fs=7.8)

# ══════════════════════════════════════════════════════════════════════════════
# 3  GENERATED TOOLS  (split: MCP top / CLI bottom)
# ══════════════════════════════════════════════════════════════════════════════
condition_divider(2)
cx = CXS[2]

# ── MCP half: 3 stacked slot cards + via-MCP badge ──
SLOTS = [('Tool Functions', '@mcp.tool()'),
         ('API Client',     'auth + HTTP'),
         ('MCP Protocol',   'FastMCP')]
sw, sh, sgap = 3.02, 0.50, 0.10
# Stack from top, leave room for badge at bottom of MCP half
badge_mcp_y = SPLIT_Y + 0.22
top_card_cy = CONT_TOP - 0.24 - sh/2
for j, (lbl, sub) in enumerate(SLOTS):
    slot_card(cx, top_card_cy - j*(sh+sgap), sw, sh, lbl, sub, C[2], zorder=5)
pill(cx, badge_mcp_y, 1.76, 0.30, C[2], 'none', zorder=6)
ax.text(cx, badge_mcp_y, 'via stdio / MCP',
        ha='center', va='center', fontsize=7.6, fontweight='bold',
        color='white', zorder=7)

# ── CLI half: single CLI script card ──
cli_card_cy = LOWER_MID + 0.08
slot_card(cx, cli_card_cy, 2.90, 0.60, 'CLI Script  (*_cli.py)',
          'argparse · subcommands', CLI_C, zorder=5)
ax.text(cx, cli_card_cy - 0.48, 'agent discovers interface via --help',
        ha='center', va='center', fontsize=7.0, color=CLI_C,
        style='italic', zorder=6)

# ══════════════════════════════════════════════════════════════════════════════
# 4  AGENT EVALUATION  (split: MCP top / CLI bottom)
# ══════════════════════════════════════════════════════════════════════════════
condition_divider(3)
cx = CXS[3]

# ── MCP half: Eval LLM ↔ Live API ──
ecx_m = cx - 0.88; r_m = 0.54
llm_circle(ecx_m, UPPER_MID, r_m, C[3], 'Eval.', 'LLM')

api_bx = cx - 0.02
ax.annotate('', xy=(api_bx, UPPER_MID), xytext=(ecx_m + r_m + 0.12, UPPER_MID),
            arrowprops=dict(arrowstyle='<->', color=C[3], lw=1.5,
                            mutation_scale=13), zorder=8)
rrect(api_bx, UPPER_MID - 0.42, 1.16, 0.84, L[3], C[3], lw=1.1, r=0.11, zorder=5)
ax.text(api_bx + 0.58, UPPER_MID + 0.11, 'Live', ha='center', va='center',
        fontsize=8.8, fontweight='bold', color=C[3], zorder=7)
ax.text(api_bx + 0.58, UPPER_MID - 0.13, 'API',  ha='center', va='center',
        fontsize=8.8, fontweight='bold', color=C[3], zorder=7)
ax.text(cx + 0.08, UPPER_MID - r_m - 0.30, 'N specific tools',
        ha='center', va='center', fontsize=7.0, color=C[3], style='italic', zorder=6)

# ── CLI half: Eval LLM → single run_command tool ──
ecx_c = cx - 0.86; r_c = 0.42
llm_circle(ecx_c, LOWER_MID, r_c, CLI_C, 'Eval.', 'LLM')

rc_cx = cx + 0.22
ax.annotate('', xy=(rc_cx - 0.60, LOWER_MID), xytext=(ecx_c + r_c + 0.10, LOWER_MID),
            arrowprops=dict(arrowstyle='->', color=CLI_C, lw=1.3,
                            mutation_scale=12), zorder=8)
chip(rc_cx, LOWER_MID, 'run_command', '#FAF4EE', CLI_C, fs=7.5, zorder=6)
ax.text(cx - 0.12, LOWER_MID - r_c - 0.28, 'discovers interface via  --help',
        ha='center', va='center', fontsize=7.0, color=CLI_C,
        style='italic', zorder=6)

# ══════════════════════════════════════════════════════════════════════════════
# 5  LLM JUDGE  (common — no split)
#    Rubric: A tool_selection, B param_quality, C result_interpretation,
#            D task_completion  —  each 0-2, pass >= 5/8
#    CONFOUND = AGENT_REASONING | TASK_AMBIGUOUS | ENVIRONMENT
# ══════════════════════════════════════════════════════════════════════════════
cx = CXS[4]

DIMS = [
    [('A.  Tool Selection',  '0–2'), ('B.  Param Quality',   '0–2')],
    [('C.  Result Interp.',  '0–2'), ('D.  Task Completion', '0–2')],
]
dw, dh, dgx, dgy = 1.66, 0.52, 0.08, 0.10
grid_r1_cy = CONT_TOP - 0.38
grid_r2_cy = grid_r1_cy - (dh + dgy)

for r, row in enumerate(DIMS):
    cy_row = grid_r1_cy - r*(dh + dgy)
    for c, (dim, rng) in enumerate(row):
        dx = cx - dw - dgx/2 + c*(dw + dgx)
        rrect(dx, cy_row - dh/2, dw, dh, 'white', C[4], lw=0.9, r=0.09, zorder=5)
        ax.text(dx + dw/2, cy_row + dh*0.14, dim, ha='center', va='center',
                fontsize=7.6, fontweight='bold', color=C[4], zorder=6)
        ax.text(dx + dw/2, cy_row - dh*0.28, rng, ha='center', va='center',
                fontsize=6.8, color=GRAY, zorder=6)

# Score bar: red 0–4 / amber 4–5 / green 5–8, threshold at 5
bar_x = cx - 1.46; bar_w = 2.92; bar_h = 0.24
bar_y = grid_r2_cy - dh/2 - 0.52
rrect(bar_x, bar_y, bar_w, bar_h, LGRAY, '#9CA3AF', lw=0.7, r=0.06, zorder=5)
for f0, f1, fc in [(0, 4/8, '#FECACA'), (4/8, 5/8, '#FDE68A'), (5/8, 1, '#BBF7D0')]:
    ax.add_patch(mpatches.Rectangle(
        (bar_x + f0*bar_w, bar_y), (f1-f0)*bar_w, bar_h, fc=fc, ec='none', zorder=6))
tx = bar_x + (5/8)*bar_w
ax.plot([tx, tx], [bar_y - 0.05, bar_y + bar_h + 0.05],
        color=DARK, lw=1.3, ls='--', zorder=8)
ax.text(bar_x + 0.04,        bar_y + bar_h + 0.08, '0',
        ha='left',   fontsize=7.0, color=GRAY, zorder=8)
ax.text(bar_x + bar_w - 0.04, bar_y + bar_h + 0.08, '8',
        ha='right',  fontsize=7.0, color=GRAY, zorder=8)
ax.text(tx, bar_y + bar_h + 0.08, 'pass ≥ 5',
        ha='center', fontsize=7.0, fontweight='bold', color=DARK, zorder=8)

# Verdict pills
VERD = [
    ('PASS',     'score ≥ 5',          '#D1FAE5', '#059669', '#065F46'),
    ('FAIL',     'score < 5',          '#FEE2E2', '#DC2626', '#991B1B'),
    ('CONFOUND', 'agent / env / task', '#FEF3C7', '#D97706', '#92400E'),
]
v_top_cy = bar_y - 0.30
for k, (lbl, sub, bfc, bec, tc) in enumerate(VERD):
    vy = v_top_cy - k*0.40
    rrect(cx - 1.46, vy - 0.16, 2.92, 0.32, bfc, bec, lw=1.1, r=0.16, zorder=5)
    ax.text(cx - 1.28, vy, lbl, ha='left',  va='center',
            fontsize=7.8, fontweight='bold', color=tc, zorder=7)
    ax.text(cx + 1.28, vy, sub, ha='right', va='center',
            fontsize=7.4, color=tc, zorder=7)

# ── Save ──────────────────────────────────────────────────────────────────────
plt.tight_layout(pad=0.1)
plt.savefig('benchmark_pipeline_v2.png', dpi=200, bbox_inches='tight',
            facecolor='white')
print("Saved benchmark_pipeline_v2.png")
