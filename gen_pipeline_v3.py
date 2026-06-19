"""
Conference-ready benchmark pipeline figure (v3).

Design principles:
  - Single neutral accent color for all phase headers (slate #2D3F5C)
  - Very light per-phase tints for backgrounds (near-white)
  - MCP / CLI conditions shown as continuous horizontal lanes with
    left-margin lane labels spanning phases 1, 3, 4
  - Clean, minimal content in each phase cell
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

# ── Canvas ─────────────────────────────────────────────────────────────────────
W, H = 22, 7.6
fig, ax = plt.subplots(figsize=(W, H))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')

# ── Palette ────────────────────────────────────────────────────────────────────
# Single neutral accent for all phase chrome
ACCENT   = '#2D3F5C'      # slate navy — headers, borders
ACCENT_L = '#F0F2F5'      # near-white tint — box backgrounds

DARK     = '#1F2937'
GRAY     = '#6B7280'
LGRAY    = '#D1D5DB'
MGRAY    = '#9CA3AF'

# Condition colours — used only for lane labels and content accents
MCP_C = '#3B6EA5'         # muted blue
CLI_C = '#8B5E3C'         # muted sienna/brown

MCP_L = '#EEF3FB'         # MCP lane background tint
CLI_L = '#FBF6F1'         # CLI lane background tint

# ── Layout ─────────────────────────────────────────────────────────────────────
BOX_W  = 3.60
GAP    = 0.54
MAR    = (W - 5*BOX_W - 4*GAP) / 2   # left/right margin

CXS = [MAR + BOX_W/2 + i*(BOX_W+GAP) for i in range(5)]
BXS = [cx - BOX_W/2 for cx in CXS]   # left edge of each box

BOX_Y  = 0.42
BOX_H  = 6.76
HDR_H  = 0.62
DESC_H = 0.80

CONT_BOT = BOX_Y + DESC_H
CONT_TOP = BOX_Y + BOX_H - HDR_H

SPLIT_Y   = (CONT_BOT + CONT_TOP) / 2   # ≈ 3.84 — condition split line
UPPER_MID = (SPLIT_Y + CONT_TOP) / 2    # MCP lane centre
LOWER_MID = (CONT_BOT + SPLIT_Y) / 2   # CLI lane centre

ARROW_Y = SPLIT_Y   # inter-phase arrows sit at split line

# ── Drawing helpers ────────────────────────────────────────────────────────────
def rrect(bx, by, bw, bh, fc, ec, lw=1.0, r=0.12, zorder=3, alpha=1.0):
    ax.add_patch(FancyBboxPatch(
        (bx, by), bw, bh,
        boxstyle=f"round,pad=0,rounding_size={r}",
        fc=fc, ec=ec, lw=lw, zorder=zorder, alpha=alpha))

def pill(cx, cy, w, h, fc, ec, lw=0.8, zorder=5):
    rrect(cx - w/2, cy - h/2, w, h, fc, ec, lw=lw, r=h/2, zorder=zorder)

def chip(cx, cy, text, fc, tc, fs=7.6, zorder=6):
    tw = len(text) * 0.072 + 0.28
    pill(cx, cy, tw, 0.26, fc, tc, lw=0.7, zorder=zorder)
    ax.text(cx, cy, text, ha='center', va='center',
            fontsize=fs, fontweight='bold', color=tc, zorder=zorder+1)

def llm_circle(cx, cy, r, color, line1, line2=None):
    ax.add_patch(plt.Circle((cx, cy), r, fc='white', ec=color, lw=1.5, zorder=5))
    if line2:
        ax.text(cx, cy + r*0.20, line1, ha='center', va='center',
                fontsize=7.8, fontweight='bold', color=color, zorder=6)
        ax.text(cx, cy - r*0.30, line2, ha='center', va='center',
                fontsize=6.8, color=GRAY, zorder=6)
    else:
        ax.text(cx, cy, line1, ha='center', va='center',
                fontsize=7.8, fontweight='bold', color=color, zorder=6)

def input_box(cx, cy, w, h, title, subtitle, color, light):
    """A simple labelled input box."""
    rrect(cx - w/2, cy - h/2, w, h, light, color, lw=1.0, r=0.10, zorder=5)
    ax.text(cx, cy + h*0.16, title, ha='center', va='center',
            fontsize=8.2, fontweight='bold', color=color, zorder=6)
    ax.text(cx, cy - h*0.22, subtitle, ha='center', va='center',
            fontsize=7.0, color=GRAY, zorder=6)

def slot_card(cx, cy, w, h, title, subtitle, color, zorder=5):
    rrect(cx - w/2, cy - h/2, w, h, 'white', color, lw=0.8, r=0.08, zorder=zorder)
    ax.text(cx, cy + h*0.15, title, ha='center', va='center',
            fontsize=7.8, fontweight='bold', color=color, zorder=zorder+1)
    ax.text(cx, cy - h*0.25, subtitle, ha='center', va='center',
            fontsize=6.8, color=GRAY, zorder=zorder+1)

def condition_divider(phase_idx):
    """Draw dashed split line + MCP/CLI labels inside a split-phase box."""
    bx = BXS[phase_idx]
    # Dashed line
    ax.plot([bx + 0.16, bx + BOX_W - 0.16], [SPLIT_Y, SPLIT_Y],
            color=LGRAY, lw=0.9, ls='--', zorder=4)
    # Labels flush with left edge, inside the box
    label_x = bx + 0.16
    label_w = 0.52
    for label, cy_lbl, fc, tc in [
        ('MCP', SPLIT_Y + 0.24, MCP_L, MCP_C),
        ('CLI', SPLIT_Y - 0.24, CLI_L, CLI_C),
    ]:
        rrect(label_x, cy_lbl - 0.13, label_w, 0.26,
              fc, tc, lw=0.9, r=0.13, zorder=6)
        ax.text(label_x + label_w/2, cy_lbl, label,
                ha='center', va='center', fontsize=7.2, fontweight='bold',
                color=tc, zorder=7)

# ══════════════════════════════════════════════════════════════════════════════
# Phase boxes
# ══════════════════════════════════════════════════════════════════════════════
NUMS  = ['1', '2', '3', '4', '5']
HEADS = ['INPUT', 'SYNTHESIS', 'GENERATED\nTOOLS', 'AGENT\nEVALUATION', 'LLM JUDGE']
DESCS = [
    ('API Docs  ·  Source Code',    '17 APIs · 330 scenarios · 2 conditions'),
    ('Agentic Tool-Calling Loop',   'reads docs or source · writes tool code'),
    ('MCP Server  ·  CLI Script',   '@mcp.tool() or argparse subcommands'),
    ('LLM Evaluation Agent',        'ReAct loop · up to 20 turns per scenario'),
    ('Automated Scoring',           '4-dim. rubric · 0–8 points'),
]

for i, cx in enumerate(CXS):
    bx = BXS[i]

    # Box background
    rrect(bx, BOX_Y, BOX_W, BOX_H, ACCENT_L, ACCENT, lw=1.1, r=0.18, zorder=2)

    # Header band
    rrect(bx, BOX_Y+BOX_H-HDR_H, BOX_W, HDR_H, ACCENT, 'none', lw=0, r=0.18, zorder=3)
    ax.add_patch(mpatches.Rectangle(
        (bx, BOX_Y+BOX_H-HDR_H), BOX_W, HDR_H*0.50, fc=ACCENT, ec='none', zorder=3))

    # Phase number (subtle)
    ax.text(bx + 0.36, BOX_Y+BOX_H-HDR_H/2, NUMS[i],
            ha='center', va='center', fontsize=10, fontweight='bold',
            color='white', alpha=0.30, zorder=5)
    ax.text(cx + 0.14, BOX_Y+BOX_H-HDR_H/2, HEADS[i],
            ha='center', va='center', fontsize=10, fontweight='bold',
            color='white', zorder=5, linespacing=1.15)

    # Separator above description
    ax.plot([bx+0.22, bx+BOX_W-0.22], [BOX_Y+DESC_H-0.04]*2,
            color=ACCENT, lw=0.5, alpha=0.22, zorder=4)
    d_title, d_sub = DESCS[i]
    ax.text(cx, BOX_Y + DESC_H*0.64, d_title,
            ha='center', va='center', fontsize=8.4, fontweight='bold',
            color=DARK, zorder=4)
    ax.text(cx, BOX_Y + DESC_H*0.22, d_sub,
            ha='center', va='center', fontsize=7.0, color=GRAY, zorder=4)

# ── Arrows between phases ──────────────────────────────────────────────────────
ALABS = ['', 'synthesizes', '', 'eval trace']
for i, lbl in enumerate(ALABS):
    x0 = BXS[i]   + BOX_W + 0.08
    x1 = BXS[i+1] - 0.08
    xm = (x0 + x1) / 2
    ax.annotate('', xy=(x1, ARROW_Y), xytext=(x0, ARROW_Y),
                arrowprops=dict(arrowstyle='->', color=DARK, lw=1.6,
                                mutation_scale=14), zorder=10)
    if lbl:
        ax.text(xm, ARROW_Y + 0.15, lbl, ha='center', va='bottom',
                fontsize=6.8, color=GRAY, style='italic', zorder=11,
                bbox=dict(boxstyle='square,pad=0.06', fc='white', ec='none', zorder=1))

# ══════════════════════════════════════════════════════════════════════════════
# 1  INPUT  (split)
# ══════════════════════════════════════════════════════════════════════════════
condition_divider(0)
cx = CXS[0]

# MCP half: doc input box
input_box(cx, UPPER_MID, 2.90, 0.88,
          'API Docs  (docs/*.md)',
          'endpoint specs per API',
          MCP_C, MCP_L)

# CLI half: source input box
input_box(cx, LOWER_MID, 2.90, 0.88,
          'Source Code  (source/)',
          'full repository tree',
          CLI_C, CLI_L)

# ══════════════════════════════════════════════════════════════════════════════
# 2  SYNTHESIS  (common)
#    Tools: read_file, list_directory, glob, grep, write_file, edit_file
# ══════════════════════════════════════════════════════════════════════════════
cx = CXS[1]

r2 = 0.90
row2_y  = CONT_BOT + 0.42
row1_y  = row2_y + 0.40
circ_cy = row1_y + 0.135 + 0.36 + r2

llm_circle(cx, circ_cy, r2, ACCENT, 'Synthesis', 'LLM')

TOOLS_ROW1 = ['read', 'list', 'glob']
TOOLS_ROW2 = ['grep', 'write', 'edit']
for k, tool in enumerate(TOOLS_ROW1):
    chip(cx - 0.82 + k*0.82, row1_y, tool, ACCENT_L, ACCENT, fs=7.6)
for k, tool in enumerate(TOOLS_ROW2):
    chip(cx - 0.82 + k*0.82, row2_y, tool, ACCENT_L, ACCENT, fs=7.6)

# ══════════════════════════════════════════════════════════════════════════════
# 3  GENERATED TOOLS  (split)
# ══════════════════════════════════════════════════════════════════════════════
condition_divider(2)
cx = CXS[2]

# MCP half: layered stack — bottom card subtitle carries the "N tools" note
SLOTS = [('Tool Functions', 'N named tools via MCP'),
         ('API Client',     'auth + HTTP'),
         ('MCP Protocol',   'FastMCP')]
sw, sh, sgap = 3.10, 0.46, 0.09
top_card_cy = CONT_TOP - 0.28 - sh/2
for j, (lbl, sub) in enumerate(SLOTS):
    slot_card(cx, top_card_cy - j*(sh+sgap), sw, sh, lbl, sub, MCP_C, zorder=5)

# CLI half: single card
cli_card_cy = LOWER_MID + 0.10
slot_card(cx, cli_card_cy, 3.00, 0.58,
          'CLI Script  (*_cli.py)',
          'argparse · subcommands', CLI_C, zorder=5)
ax.text(cx, cli_card_cy - 0.46, 'interface discoverable via  --help',
        ha='center', va='center', fontsize=6.8, color=CLI_C,
        style='italic', zorder=6)

# ══════════════════════════════════════════════════════════════════════════════
# 4  AGENT EVALUATION  (split)
# ══════════════════════════════════════════════════════════════════════════════
condition_divider(3)
cx = CXS[3]

# Common radius for both eval circles
r_eval = 0.56

# MCP half: Eval LLM ↔ Live API
ecx_m = cx - 0.76
llm_circle(ecx_m, UPPER_MID, r_eval, MCP_C, 'Eval.', 'LLM')

api_bx = cx + 0.08
arrow_x0 = ecx_m + r_eval + 0.10
arrow_x1 = api_bx - 0.02
# Two one-way arrows to ensure both heads render
ax.annotate('', xy=(arrow_x1, UPPER_MID + 0.04), xytext=(arrow_x0, UPPER_MID + 0.04),
            arrowprops=dict(arrowstyle='->', color=MCP_C, lw=1.2,
                            mutation_scale=11), zorder=8)
ax.annotate('', xy=(arrow_x0, UPPER_MID - 0.04), xytext=(arrow_x1, UPPER_MID - 0.04),
            arrowprops=dict(arrowstyle='->', color=MCP_C, lw=1.2,
                            mutation_scale=11), zorder=8)
rrect(api_bx, UPPER_MID - 0.36, 1.06, 0.72, MCP_L, MCP_C, lw=0.9, r=0.10, zorder=5)
ax.text(api_bx + 0.53, UPPER_MID + 0.07, 'Live', ha='center', va='center',
        fontsize=7.8, fontweight='bold', color=MCP_C, zorder=7)
ax.text(api_bx + 0.53, UPPER_MID - 0.11, 'API', ha='center', va='center',
        fontsize=7.8, fontweight='bold', color=MCP_C, zorder=7)

ax.text(cx + 0.02, UPPER_MID - r_eval - 0.24, 'N specific tools',
        ha='center', va='center', fontsize=6.8, color=MCP_C,
        style='italic', zorder=6)

# CLI half: Eval LLM → run_command (mirror layout)
ecx_c = cx - 0.76
llm_circle(ecx_c, LOWER_MID, r_eval, CLI_C, 'Eval.', 'LLM')

# chip half-width ≈ (11*0.072 + 0.28)/2 ≈ 0.54
rc_cx = cx + 0.56
chip_left = rc_cx - 0.54
ax.annotate('', xy=(chip_left, LOWER_MID),
            xytext=(ecx_c + r_eval + 0.10, LOWER_MID),
            arrowprops=dict(arrowstyle='->', color=CLI_C, lw=1.2,
                            mutation_scale=11), zorder=8)
chip(rc_cx, LOWER_MID, 'run_command', CLI_L, CLI_C, fs=7.4, zorder=6)
ax.text(cx - 0.06, LOWER_MID - r_eval - 0.24, 'single  run_command  tool',
        ha='center', va='center', fontsize=6.8, color=CLI_C,
        style='italic', zorder=6)

# ══════════════════════════════════════════════════════════════════════════════
# 5  LLM JUDGE  (common)
# ══════════════════════════════════════════════════════════════════════════════
cx = CXS[4]

# Rubric grid: 2×2
DIMS = [
    [('A.  Tool Selection',  '0 – 2'), ('B.  Param Quality',   '0 – 2')],
    [('C.  Result Interp.',  '0 – 2'), ('D.  Task Completion', '0 – 2')],
]
dw, dh, dgx, dgy = 1.62, 0.50, 0.08, 0.08
grid_r1_cy = CONT_TOP - 0.35

for r, row in enumerate(DIMS):
    cy_row = grid_r1_cy - r*(dh + dgy)
    for c, (dim, rng) in enumerate(row):
        dx = cx - dw - dgx/2 + c*(dw + dgx)
        rrect(dx, cy_row - dh/2, dw, dh, 'white', ACCENT, lw=0.8, r=0.08, zorder=5)
        ax.text(dx + dw/2, cy_row + dh*0.14, dim, ha='center', va='center',
                fontsize=7.4, fontweight='bold', color=ACCENT, zorder=6)
        ax.text(dx + dw/2, cy_row - dh*0.28, rng, ha='center', va='center',
                fontsize=6.6, color=GRAY, zorder=6)

# Score bar
grid_r2_cy = grid_r1_cy - (dh + dgy)
bar_x = cx - 1.42; bar_w = 2.84; bar_h = 0.22
bar_y = grid_r2_cy - dh/2 - 0.50
rrect(bar_x, bar_y, bar_w, bar_h, LGRAY, MGRAY, lw=0.6, r=0.05, zorder=5)
for f0, f1, fc in [(0, 4/8, '#F5C6C6'), (4/8, 5/8, '#F5E6A0'), (5/8, 1, '#B8E8C8')]:
    ax.add_patch(mpatches.Rectangle(
        (bar_x + f0*bar_w, bar_y), (f1-f0)*bar_w, bar_h,
        fc=fc, ec='none', zorder=6))
tx = bar_x + (5/8)*bar_w
ax.plot([tx, tx], [bar_y - 0.04, bar_y + bar_h + 0.04],
        color=DARK, lw=1.1, ls='--', zorder=8)
ax.text(bar_x + 0.04, bar_y + bar_h + 0.07, '0',
        ha='left', fontsize=6.8, color=GRAY, zorder=8)
ax.text(bar_x + bar_w - 0.04, bar_y + bar_h + 0.07, '8',
        ha='right', fontsize=6.8, color=GRAY, zorder=8)
ax.text(tx, bar_y + bar_h + 0.07, 'pass ≥ 5',
        ha='center', fontsize=6.8, fontweight='bold', color=DARK, zorder=8)

# Verdict pills — muted tones
VERD = [
    ('PASS',     'score ≥ 5',          '#C9EDD8', '#4A9E6E', '#1E5C3A'),
    ('FAIL',     'score < 5',          '#F5CECE', '#C45757', '#7A2020'),
    ('CONFOUND', 'agent / env / task', '#F5E9C0', '#C49A30', '#6B5010'),
]
v_top_cy = bar_y - 0.28
for k, (lbl, sub, bfc, bec, tc) in enumerate(VERD):
    vy = v_top_cy - k*0.38
    rrect(cx - 1.42, vy - 0.15, 2.84, 0.30, bfc, bec, lw=0.9, r=0.15, zorder=5)
    ax.text(cx - 1.24, vy, lbl, ha='left', va='center',
            fontsize=7.4, fontweight='bold', color=tc, zorder=7)
    ax.text(cx + 1.24, vy, sub, ha='right', va='center',
            fontsize=7.0, color=tc, zorder=7)

# ── Save ───────────────────────────────────────────────────────────────────────
plt.tight_layout(pad=0.1)
plt.savefig('benchmark_pipeline_v3.png', dpi=200, bbox_inches='tight',
            facecolor='white')
print("Saved benchmark_pipeline_v3.png")
