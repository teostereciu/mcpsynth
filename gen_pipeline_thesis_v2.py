"""
Benchmark pipeline — thesis figure, v2.

Structure: two-phase layout instead of five equal cards.
  Left band  (SYNTHESIS):  API docs → Synthesis LLM → MCP Server
  Right band (EVALUATION): Task prompt → Agent LLM ↔ MCP Server ↔ Live API
                           → Judge LLM → Verdict + SERVER_SUFFICIENT

Accurate eval model:
  · Agent receives: task prompt + MCP tool schemas
  · Agent issues tool calls → MCP server executes real HTTP requests → Live API
  · Full trajectory (steps + final answer) → Judge LLM
  · Judge outputs: OUTCOME (PASS/FAIL/UNDEF) · FAILURE_CAUSE · SERVER_SUFFICIENT
  · CURRENT metric  = PASS / (PASS+FAIL)           [excludes UNDEF]
  · SYNTH  metric   = SERVER_SUFFICIENT / total     [independent of agent]

Design:
  · Two shaded phase regions (no tall cards)
  · LLMs as circles (ML convention)
  · Artifacts as light rectangles
  · Single dark-navy accent, gray fills, white background
  · ~14 × 4.8 in — fits full-width thesis page at 1:1 or scales down cleanly
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family':     'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Arial', 'DejaVu Sans'],
    'pdf.fonttype':    42,
    'ps.fonttype':     42,
})

# ── Canvas ──────────────────────────────────────────────────────────────────
W, H = 15.6, 5.0
fig, ax = plt.subplots(figsize=(W, H))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')

# ── Palette ─────────────────────────────────────────────────────────────────
NAVY    = '#1B2E5E'
NAVY_LT = '#2E4A8A'
RULE    = '#B8C2D0'
BORDER  = '#8C9BAD'
SUB     = '#4A5568'
ANNOT   = '#718096'
SYNTH_BG = '#EDF1F8'   # light blue tint — synthesis phase
EVAL_BG  = '#F5F6F8'   # light gray — evaluation phase
FILL_A  = '#DDE3EF'    # slightly deeper blue — highlighted artifacts
FILL_N  = '#ECEEF2'    # neutral fill
WHITE   = '#FFFFFF'

# ── Phase regions ────────────────────────────────────────────────────────────
PHASE_Y   = 0.52          # leave room for footer below
PHASE_H   = 4.18
SPLIT_X   = 5.80          # synthesis | evaluation split
MARG_X    = 0.22
MARG_R    = 0.22

def phase_box(x, y, w, h, fc, label, label_color):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0,rounding_size=0.12",
        fc=fc, ec=RULE, lw=0.5, zorder=1))
    # Phase label — upper-left corner, small caps style
    ax.text(x + 0.18, y + h - 0.20,
            label, ha='left', va='top',
            fontsize=6.8, fontweight='bold', color=label_color,
            fontstyle='normal', zorder=4,
            alpha=0.65)

SYNTH_W = SPLIT_X - MARG_X - 0.10
EVAL_W  = W - SPLIT_X - 0.10 - MARG_R

phase_box(MARG_X, PHASE_Y, SYNTH_W, PHASE_H,
          SYNTH_BG, 'SYNTHESIS  (offline, per API)', NAVY)
phase_box(SPLIT_X + 0.10, PHASE_Y, EVAL_W, PHASE_H,
          EVAL_BG,  'EVALUATION  (online, per task)', SUB)

# ── Helper functions ─────────────────────────────────────────────────────────
def rrect(x, y, w, h, fc=WHITE, ec=BORDER, lw=0.6, r=0.08, z=4):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={r}",
        fc=fc, ec=ec, lw=lw, zorder=z, clip_on=False))

def circle(cx, cy, r, fc=WHITE, ec=NAVY, lw=0.9, z=5):
    ax.add_patch(plt.Circle((cx, cy), r, fc=fc, ec=ec, lw=lw, zorder=z))

def robot_icon(cx, cy, r, ec=NAVY, lw=0.8, z=5):
    """
    Minimal robot glyph that fits in a bounding box of ±r around (cx, cy).

    Anatomy (all sizes relative to r):
      antenna  : thin vertical stem + small ball on top
      head     : rounded rectangle, ~0.72r wide × 0.52r tall
                 two small circular 'eyes' inside
      neck     : short connector
      body     : wider rounded rectangle, ~0.88r wide × 0.52r tall
                 three small horizontal lines (ventilation / chest panel)
    """
    FILL = '#EDF1F8'     # very light blue fill — robot body
    EYE  = ec            # eyes + details same as border

    # ── Antenna ────────────────────────────────────────────────────────────
    ant_base_y = cy + r * 0.50
    ant_tip_y  = cy + r * 0.90
    ant_ball_r = r * 0.055
    ax.plot([cx, cx], [ant_base_y, ant_tip_y - ant_ball_r],
            color=ec, lw=lw * 0.9, zorder=z, solid_capstyle='round')
    ax.add_patch(plt.Circle((cx, ant_tip_y),
                            ant_ball_r, fc=ec, ec='none', zorder=z+1))

    # ── Head ───────────────────────────────────────────────────────────────
    hd_w = r * 0.72; hd_h = r * 0.52
    hd_x = cx - hd_w/2; hd_y = cy + r * 0.50 - hd_h
    ax.add_patch(FancyBboxPatch(
        (hd_x, hd_y), hd_w, hd_h,
        boxstyle="round,pad=0,rounding_size=0.06",
        fc=FILL, ec=ec, lw=lw, zorder=z))

    # Eyes
    eye_r = r * 0.075
    eye_y = hd_y + hd_h * 0.52
    for ex in [cx - hd_w*0.22, cx + hd_w*0.22]:
        ax.add_patch(plt.Circle((ex, eye_y), eye_r,
                                fc=ec, ec='none', zorder=z+1))

    # ── Neck ───────────────────────────────────────────────────────────────
    nk_w = r * 0.22; nk_h = r * 0.10
    ax.add_patch(mpatches.Rectangle(
        (cx - nk_w/2, hd_y - nk_h), nk_w, nk_h,
        fc=FILL, ec=ec, lw=lw*0.7, zorder=z))

    # ── Body ───────────────────────────────────────────────────────────────
    bd_w = r * 0.88; bd_h = r * 0.54
    bd_x = cx - bd_w/2; bd_y = hd_y - nk_h - bd_h
    ax.add_patch(FancyBboxPatch(
        (bd_x, bd_y), bd_w, bd_h,
        boxstyle="round,pad=0,rounding_size=0.05",
        fc=FILL, ec=ec, lw=lw, zorder=z))

    # Chest panel: three horizontal lines
    pan_w = bd_w * 0.52; pan_x = cx - pan_w/2
    for k, py_frac in enumerate([0.68, 0.48, 0.28]):
        py = bd_y + bd_h * py_frac
        ax.plot([pan_x, pan_x + pan_w], [py, py],
                color=ec, lw=lw * 0.65, alpha=0.6,
                zorder=z+1, solid_capstyle='round')

def txt(x, y, s, size=7.8, weight='normal', color=SUB,
        ha='center', va='center', z=8, style='normal', family=None):
    kw = dict(ha=ha, va=va, fontsize=size, fontweight=weight,
              color=color, zorder=z, fontstyle=style)
    if family:
        kw['fontfamily'] = family
    ax.text(x, y, s, **kw)

def arrow(x0, x1, y0, y1=None, label=None, label_side='top', color=NAVY,
          lw=0.9, mutation=8, z=10, rad=0):
    if y1 is None:
        y1 = y0
    style = f'arc3,rad={rad}'
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                mutation_scale=mutation,
                                connectionstyle=style), zorder=z)
    if label:
        mx, my = (x0+x1)/2, (y0+y1)/2
        dy = 0.10 if label_side == 'top' else -0.10
        va = 'bottom' if label_side == 'top' else 'top'
        txt(mx, my + dy, label, size=5.8, color=ANNOT, style='italic',
            va=va, z=z)

def double_arrow(x0, x1, y, gap=0.08, color=NAVY, lw=0.75, label=None):
    ax.annotate('', xy=(x1, y + gap), xytext=(x0, y + gap),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                mutation_scale=7), zorder=10)
    ax.annotate('', xy=(x0, y - gap), xytext=(x1, y - gap),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                mutation_scale=7), zorder=10)
    if label:
        txt((x0+x1)/2, y, label, size=5.6, color=ANNOT, style='italic', z=10)

# ══════════════════════════════════════════════════════════════════════════════
# SYNTHESIS PHASE
# Layout (left → right):  [API Docs]  →  (Synthesis LLM)  →  [MCP Server]
# ══════════════════════════════════════════════════════════════════════════════

MID_Y = PHASE_Y + PHASE_H / 2    # vertical centre

# ── API Docs artifact ────────────────────────────────────────────────────────
DOCS_X = MARG_X + 0.26
DOCS_W = 1.84
DOCS_H = 2.80
DOCS_Y = MID_Y - DOCS_H / 2

rrect(DOCS_X, DOCS_Y, DOCS_W, DOCS_H,
      fc=FILL_A, ec=NAVY, lw=0.7, r=0.07, z=4)

txt(DOCS_X + DOCS_W/2, DOCS_Y + DOCS_H - 0.26,
    'API Documentation', size=7.6, weight='bold', color=NAVY, z=6)

# Three condition rows inside
cond_info = [
    ('docs',    'Full endpoint docs',    FILL_A,  NAVY,   0.65),
    ('nodocs',  'Task prompt only',      WHITE,   BORDER, 0.50),
    ('mutated', 'Renamed parameters',    WHITE,   BORDER, 0.50),
]
row_h = 0.44; row_gap = 0.09
block_h = 3*row_h + 2*row_gap
block_bot = DOCS_Y + (DOCS_H - block_h) / 2 - 0.10
ix = DOCS_X + 0.10; iw = DOCS_W - 0.20

for ri, (tag, desc, fc, ec, tag_alpha) in enumerate(cond_info):
    ry = block_bot + (2-ri)*(row_h + row_gap)
    rrect(ix, ry, iw, row_h, fc=fc, ec=ec, lw=0.5, r=0.05, z=5)
    ax.text(ix + 0.11, ry + row_h/2, tag,
            ha='left', va='center', fontsize=6.8, fontweight='bold',
            color=NAVY if ri == 0 else SUB,
            fontfamily='monospace', zorder=7, alpha=tag_alpha)
    ax.text(ix + iw - 0.09, ry + row_h/2, desc,
            ha='right', va='center', fontsize=6.0, color=ANNOT, zorder=7)

# "condition" bracket on the left
bx = DOCS_X + 0.02
btop = block_bot + 3*row_h + 2*row_gap
bbot = block_bot
bmid = (btop + bbot) / 2
ax.plot([bx - 0.08, bx - 0.13, bx - 0.13, bx - 0.08],
        [btop, btop, bbot, bbot],
        color=RULE, lw=0.8, zorder=6, solid_capstyle='round')
txt(bx - 0.17, bmid, 'condition', size=5.5, color=ANNOT,
    style='italic', ha='right', va='center', z=6)

# ── Arrow: docs → synthesis LLM ──────────────────────────────────────────────
SYNTH_CX = 4.00
# ── Synthesis LLM ─────────────────────────────────────────────────────────────
SYNTH_R = 0.70
SYNTH_ICY = MID_Y + 0.18   # icon centre y
arrow(DOCS_X + DOCS_W + 0.06, SYNTH_CX - SYNTH_R * 0.46, MID_Y, label='reads', z=9)
robot_icon(SYNTH_CX, SYNTH_ICY, SYNTH_R, ec=NAVY, lw=0.8, z=6)
# Label below robot body
SYNTH_BOT = SYNTH_ICY - SYNTH_R * 0.50   # bottom of body
txt(SYNTH_CX, SYNTH_BOT - 0.20, 'Synthesis LLM',
    size=7.4, weight='bold', color=NAVY, z=8)

# Tool calls label further below
tool_y = SYNTH_BOT - 0.52
txt(SYNTH_CX, tool_y + 0.10,
    'read  ·  list  ·  glob', size=6.2, color=ANNOT,
    family='monospace', z=6)
txt(SYNTH_CX, tool_y - 0.10,
    'grep  ·  write  ·  edit', size=6.2, color=ANNOT,
    family='monospace', z=6)
txt(SYNTH_CX, tool_y - 0.30,
    'file tools · ≤100 turns', size=5.6, color=ANNOT,
    style='italic', z=6)

# ── Arrow: synthesis → MCP Server ─────────────────────────────────────────────
# MCP Server lives inside the eval phase, just right of the split
MCP_W = 1.62; MCP_H = 1.96
MCP_X = SPLIT_X + 0.22
MCP_CX = MCP_X + MCP_W/2
MCP_Y  = MID_Y - MCP_H/2

arrow(SYNTH_CX + SYNTH_R * 0.46 + 0.04, MCP_X - 0.04, MID_Y,
      label='synthesizes', z=9)

# ══════════════════════════════════════════════════════════════════════════════
# MCP SERVER  — inside eval phase, left anchor of the agent loop
# ══════════════════════════════════════════════════════════════════════════════
rrect(MCP_X, MCP_Y, MCP_W, MCP_H,
      fc=FILL_A, ec=NAVY, lw=0.75, r=0.07, z=4)

txt(MCP_CX, MCP_Y + MCP_H - 0.24,
    'MCP Server', size=7.8, weight='bold', color=NAVY, z=6)
ax.plot([MCP_X + 0.10, MCP_X + MCP_W - 0.10],
        [MCP_Y + MCP_H - 0.42]*2, color=RULE, lw=0.5, zorder=5)

sub_items = [
    ('N tool functions', '@mcp.tool()'),
    ('API client',       'auth + HTTP'),
]
si_h = 0.40; si_gap = 0.10
si_block_h = len(sub_items)*si_h + (len(sub_items)-1)*si_gap
si_bot = MCP_Y + (MCP_H - 0.42 - si_block_h) / 2 - 0.02

for si, (title, sub) in enumerate(sub_items):
    sy = si_bot + (len(sub_items)-1-si)*( si_h + si_gap)
    rrect(MCP_X + 0.10, sy, MCP_W - 0.20, si_h,
          fc=WHITE, ec=BORDER, lw=0.45, r=0.04, z=5)
    txt(MCP_CX, sy + si_h*0.64, title,
        size=6.8, weight='bold', color=SUB, z=7)
    txt(MCP_CX, sy + si_h*0.24, sub,
        size=6.0, color=ANNOT, z=7)

# ══════════════════════════════════════════════════════════════════════════════
# EVALUATION PHASE
# Layout:
#   [Task]  →  (Agent LLM) ←→ [MCP Server] ←→ [Live API]
#                   ↓  trajectory
#              (Judge LLM)  →  [Verdict]
# ══════════════════════════════════════════════════════════════════════════════

# Eval phase geometry — keep everything inside EVAL_BG region
# Horizontal zones: [MCP Server] | [Agent loop] | [Verdict panel]
# Vertical zones: top = agent row, bottom = judge row

AGENT_Y  = MID_Y + 0.06    # centre of agent robot
JUDGE_Y  = MID_Y - 1.14    # centre of judge robot  — more vertical separation
AGENT_R  = 0.58
JUDGE_R  = 0.52

# Agent sits to the right of MCP Server
AGENT_CX = MCP_X + MCP_W + 1.00

# ── Task artifact — floats above / beside agent ───────────────────────────────
TASK_W = 1.22; TASK_H = 0.86
TASK_X = AGENT_CX - TASK_W/2
TASK_Y = AGENT_Y + AGENT_R + 0.22   # gap from top of robot antenna

rrect(TASK_X, TASK_Y, TASK_W, TASK_H,
      fc=FILL_N, ec=BORDER, lw=0.55, r=0.06, z=4)
txt(TASK_X + TASK_W/2, TASK_Y + TASK_H*0.68,
    'Task prompt', size=7.0, weight='bold', color=SUB, z=6)
txt(TASK_X + TASK_W/2, TASK_Y + TASK_H*0.26,
    'tasks.yaml · N per API', size=5.8, color=ANNOT, z=6)

# Arrow: task → agent (downward)
arrow(AGENT_CX, AGENT_CX,
      TASK_Y - 0.04, AGENT_Y + AGENT_R * 0.92,
      label='prompt + tool schemas', label_side='top', z=9)

# ── Agent LLM robot ───────────────────────────────────────────────────────────
robot_icon(AGENT_CX, AGENT_Y, AGENT_R, ec=NAVY, lw=0.8, z=6)
AGENT_BOT = AGENT_Y - AGENT_R * 0.50
txt(AGENT_CX, AGENT_BOT - 0.18, 'Agent LLM',
    size=7.4, weight='bold', color=NAVY, z=8)

# ── Double arrow: MCP Server ↔ Agent ─────────────────────────────────────────
# Arrows connect at horizontal mid-body of robot (AGENT_Y + small offset)
double_arrow(MCP_X + MCP_W + 0.05, AGENT_CX - AGENT_R * 0.46,
             AGENT_Y + 0.05, gap=0.08, label='tool calls / results')

# ── Live API — below Agent, connected via MCP server internals ────────────────
LAPI_W = 1.10; LAPI_H = 0.72
LAPI_CX = MCP_CX
LAPI_Y  = MCP_Y - 0.22 - LAPI_H

rrect(LAPI_CX - LAPI_W/2, LAPI_Y, LAPI_W, LAPI_H,
      fc=FILL_A, ec=NAVY, lw=0.65, r=0.06, z=4)
txt(LAPI_CX, LAPI_Y + LAPI_H*0.65,
    'Live API', size=7.2, weight='bold', color=NAVY, z=6)
txt(LAPI_CX, LAPI_Y + LAPI_H*0.26,
    'real HTTP calls', size=6.0, color=ANNOT, z=6)

# Arrow: MCP Server ↔ Live API (vertical, bidirectional)
# Vertical bidirectional arrow: Live API ↔ MCP Server
_vx0, _vx1 = LAPI_CX - 0.06, LAPI_CX + 0.06
ax.annotate('', xy=(_vx0, MCP_Y - 0.04), xytext=(_vx0, LAPI_Y + LAPI_H + 0.04),
            arrowprops=dict(arrowstyle='->', color=NAVY, lw=0.7, mutation_scale=7), zorder=10)
ax.annotate('', xy=(_vx1, LAPI_Y + LAPI_H + 0.04), xytext=(_vx1, MCP_Y - 0.04),
            arrowprops=dict(arrowstyle='->', color=NAVY, lw=0.7, mutation_scale=7), zorder=10)
txt(LAPI_CX + 0.18, (LAPI_Y + LAPI_H + MCP_Y) / 2,
    'HTTP req/resp', size=5.6, color=ANNOT, style='italic', ha='left', z=9)

# ── Trajectory arrow: agent body bottom → judge robot top ────────────────────
arrow(AGENT_CX, AGENT_CX,
      AGENT_BOT - 0.22, JUDGE_Y + JUDGE_R * 0.94,
      label='full trajectory', label_side='top', z=9)

# ── Judge LLM robot ────────────────────────────────────────────────────────────
robot_icon(AGENT_CX, JUDGE_Y, JUDGE_R, ec=NAVY, lw=0.8, z=6)
JUDGE_BOT = JUDGE_Y - JUDGE_R * 0.50
txt(AGENT_CX, JUDGE_BOT - 0.16, 'Judge LLM',
    size=7.4, weight='bold', color=NAVY, z=8)

# ── Verdict panel — to the right of judge ─────────────────────────────────────
VERD_X = AGENT_CX + JUDGE_R * 0.46 + 0.30
VERD_W = W - MARG_R - VERD_X - 0.30   # keep inside canvas + eval bg
VERD_H = PHASE_H - 0.50
VERD_Y = PHASE_Y + 0.25

rrect(VERD_X, VERD_Y, VERD_W, VERD_H,
      fc=WHITE, ec=BORDER, lw=0.55, r=0.08, z=4)

# Arrow: judge → verdict
arrow(AGENT_CX + JUDGE_R + 0.05, VERD_X - 0.04, JUDGE_Y, z=9)

# Section: OUTCOME
sec_y = VERD_Y + VERD_H - 0.20
txt(VERD_X + VERD_W/2, sec_y - 0.05,
    'Task Verdict (OUTCOME)', size=6.2, color=ANNOT, style='italic', z=6)
ax.plot([VERD_X + 0.10, VERD_X + VERD_W - 0.10],
        [sec_y - 0.20]*2, color=RULE, lw=0.4, zorder=5)

verdicts = [
    ('PASS',   'agent completed task correctly',   '#E4EBF5', NAVY),
    ('FAIL',   'tool-side failure (see cause)',     FILL_N,   BORDER),
    ('UNDEF',  'agent / env / task confound',       FILL_N,   BORDER),
]
vr_h = 0.34; vr_gap = 0.06
vr_top = sec_y - 0.26
vr_x = VERD_X + 0.10; vr_w = VERD_W - 0.20

for vi, (label, desc, fc, ec) in enumerate(verdicts):
    vy = vr_top - vi*(vr_h + vr_gap) - vr_h
    rrect(vr_x, vy, vr_w, vr_h, fc=fc, ec=ec, lw=0.45, r=0.04, z=5)
    ax.text(vr_x + 0.12, vy + vr_h/2, label,
            ha='left', va='center', fontsize=6.8, fontweight='bold',
            color=NAVY if vi == 0 else SUB,
            fontfamily='monospace', zorder=7)
    ax.text(vr_x + vr_w - 0.10, vy + vr_h/2, desc,
            ha='right', va='center', fontsize=5.8, color=ANNOT, zorder=7)

fail_sep = vr_top - 3*(vr_h + vr_gap) + vr_gap
ax.plot([VERD_X + 0.10, VERD_X + VERD_W - 0.10],
        [fail_sep - 0.04]*2, color=RULE, lw=0.4, zorder=5)

# Section: FAILURE_CAUSE
fc_label_y = fail_sep - 0.18
txt(VERD_X + VERD_W/2, fc_label_y,
    'Failure cause (when FAIL)', size=6.0, color=ANNOT, style='italic', z=6)

causes = ['TOOL_COVERAGE', 'TOOL_SCHEMA', 'TOOL_IMPLEMENTATION', 'TOOL_DOCUMENTATION']
fc_h = 0.26; fc_gap_x = 0.07; fc_gap_y = 0.06
fc_cw = (vr_w - fc_gap_x) / 2
fc_top = fc_label_y - 0.14

for ci, cause in enumerate(causes):
    col = ci % 2; row = ci // 2
    cx_fc = vr_x + col*(fc_cw + fc_gap_x)
    cy_fc = fc_top - row*(fc_h + fc_gap_y) - fc_h
    rrect(cx_fc, cy_fc, fc_cw, fc_h,
          fc=FILL_N, ec=BORDER, lw=0.40, r=0.03, z=5)
    ax.text(cx_fc + fc_cw/2, cy_fc + fc_h/2, cause,
            ha='center', va='center', fontsize=5.3, color=SUB,
            fontfamily='monospace', zorder=7)

fc_bot = fc_top - 2*(fc_h + fc_gap_y)
ax.plot([VERD_X + 0.10, VERD_X + VERD_W - 0.10],
        [fc_bot - 0.04]*2, color=RULE, lw=0.4, zorder=5)

# Section: SERVER_SUFFICIENT
ss_label_y = fc_bot - 0.18
txt(VERD_X + VERD_W/2, ss_label_y,
    'Server quality (independent of agent)', size=6.0, color=ANNOT, style='italic', z=6)

ss_h = 0.34; ss_y = ss_label_y - 0.14 - ss_h
rrect(vr_x, ss_y, vr_w, ss_h,
      fc='#E4EBF5', ec=NAVY, lw=0.55, r=0.04, z=5)
txt(vr_x + vr_w/2, ss_y + ss_h*0.64,
    'SERVER_SUFFICIENT  (SYNTH metric)',
    size=6.5, weight='bold', color=NAVY, z=7)
txt(vr_x + vr_w/2, ss_y + ss_h*0.26,
    'did the server provide a usable, correct tool?  ·  YES / NO / UNKNOWN',
    size=5.6, color=ANNOT, z=7)

# ── "≤15 turns" annotation on the trajectory arrow ───────────────────────────
txt(AGENT_CX + 0.14, (AGENT_BOT + JUDGE_Y + JUDGE_R * 0.94) / 2,
    '≤15 turns', size=5.8, color=ANNOT, style='italic', ha='left', z=6)

# ── Metrics footer ────────────────────────────────────────────────────────────
metrics_y = PHASE_Y - 0.02
metric_strs = [
    ('CURRENT', 'PASS / (PASS + FAIL)   [scoreable tasks]'),
    ('SYNTH',   'SERVER_SUFFICIENT / total   [server quality]'),
    ('E2E',     '(SERVER_SUFFICIENT AND PASS) / total'),
]
mx_start = MARG_X + 0.10
for mi, (name, formula) in enumerate(metric_strs):
    mx = mx_start + mi * 4.50
    ax.text(mx, metrics_y, name + '  =  ',
            ha='left', va='top', fontsize=6.2, fontweight='bold',
            color=NAVY, zorder=4)
    ax.text(mx + 0.80, metrics_y, formula,
            ha='left', va='top', fontsize=6.2, color=ANNOT, zorder=4)

ax.plot([MARG_X, W - MARG_R], [PHASE_Y - 0.10]*2,
        color=RULE, lw=0.4, zorder=3)

# ── Save ─────────────────────────────────────────────────────────────────────
plt.tight_layout(pad=0)
for ext in ('png', 'pdf'):
    fname = f'benchmark_pipeline_thesis_v2.{ext}'
    dpi = 300 if ext == 'png' else None
    plt.savefig(fname, dpi=dpi, bbox_inches='tight', facecolor='white')
    print(f'Saved {fname}')
