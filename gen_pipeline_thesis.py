"""
Thesis-quality benchmark pipeline figure.

Design goals:
  · Fits a standard thesis page at full width (~17 cm / 6.7 in at 100%)
  · Pure white background — drops cleanly into LaTeX with \\includegraphics
  · Single-hue accent (dark navy #1B2E5E) — all other fills are white or
    light grays; fully readable when printed in greyscale
  · Consistent typographic hierarchy:
      Stage headers  — 9pt bold, tracked caps via string upper()
      Sub-labels     — 8pt regular
      Annotations    — 6.5–7pt italic, grey
  · Thin rules (0.6pt), hairline borders (0.5pt), no drop shadows
  · Three synthesis conditions shown in the Input stage as stacked variant
    tags — makes the experimental design legible at a glance
  · A/B/C/D rubric dimensions shown in the Judge stage
  · Arrow labels for inter-stage data flows

Output: benchmark_pipeline_thesis.png  (300 dpi, 15×5 in canvas)
        benchmark_pipeline_thesis.pdf  (vector, for direct LaTeX import)
"""

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe

matplotlib.rcParams.update({
    'font.family':      'sans-serif',
    'font.sans-serif':  ['Helvetica Neue', 'Arial', 'DejaVu Sans'],
    'pdf.fonttype':     42,
    'ps.fonttype':      42,
    'figure.dpi':       300,
})

# ── Canvas ─────────────────────────────────────────────────────────────────
FIG_W, FIG_H = 15.0, 5.0
fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, FIG_W)
ax.set_ylim(0, FIG_H)
ax.axis('off')

# ── Palette ────────────────────────────────────────────────────────────────
NAVY   = '#1B2E5E'   # primary accent — stage headers, key labels
RULE   = '#C5CBD6'   # internal dividers
BORDER = '#8C96A8'   # box edges
SUB    = '#5A6172'   # secondary text
ANNOT  = '#7A8395'   # annotation / italic notes
FILL_A = '#F0F2F6'   # light fill for artifact boxes
FILL_B = '#E4E8F0'   # slightly deeper fill (conditions, rubric cells)
WHITE  = '#FFFFFF'

# ── Stage geometry ─────────────────────────────────────────────────────────
# 5 stages, left-to-right, uniform width except stage 1 is slightly narrower
# Outer frame for each stage: full-height card with header strip at top
#   and caption strip at bottom.

MARGIN_L = 0.32   # extra left room for the "condition" brace label
MARGIN_R = 0.18
STAGE_GAP = 0.20        # gap between stage cards
CARD_H  = 4.52
CARD_Y  = (FIG_H - CARD_H) / 2      # = 0.24

# Stage widths (total = FIG_W - MARGIN_L - MARGIN_R - 4*STAGE_GAP)
AVAIL = FIG_W - MARGIN_L - MARGIN_R - 4 * STAGE_GAP   # 13.62
W = [2.52, 2.42, 2.52, 2.72, 3.44]   # hand-tuned; total adjusted to AVAIL
# Scale widths to exactly fill available space
_scale = AVAIL / sum(W)
W = [w * _scale for w in W]

# Compute left edges
xs = []
x = MARGIN_L
for i, w in enumerate(W):
    xs.append(x)
    x += w + STAGE_GAP

cx = [xs[i] + W[i] / 2 for i in range(5)]  # centre x per stage

HDR_H  = 0.46   # header strip height
CAP_H  = 0.46   # caption strip height

BODY_TOP = CARD_Y + CARD_H - HDR_H      # y of top of body region
BODY_BOT = CARD_Y + CAP_H               # y of bottom of body region
MID_Y    = (BODY_TOP + BODY_BOT) / 2

# Inter-stage arrow y (centre of body)
ARR_Y = MID_Y

PAD = 0.14   # internal horizontal padding inside cards


# ── Low-level helpers ───────────────────────────────────────────────────────
def rrect(x, y, w, h, fc=WHITE, ec=BORDER, lw=0.55, r=0.06, z=4):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={r}",
        fc=fc, ec=ec, lw=lw, zorder=z,
        clip_on=False))


def txt(x, y, s, size=8, weight='normal', color=SUB, ha='center',
        va='center', z=8, style='normal', family=None):
    kw = dict(ha=ha, va=va, fontsize=size, fontweight=weight,
              color=color, zorder=z, style=style)
    if family:
        kw['fontfamily'] = family
    ax.text(x, y, s, **kw)


def hrule(x0, x1, y, lw=0.5, color=RULE, z=5):
    ax.plot([x0, x1], [y, y], color=color, lw=lw, zorder=z, solid_capstyle='butt')


def arrow(x0, x1, y, label=None, label_above=True):
    """Draw a simple right-pointing arrow between stage boxes."""
    ax.annotate(
        '', xy=(x1, y), xytext=(x0, y),
        arrowprops=dict(
            arrowstyle='->', color=NAVY,
            lw=0.8, mutation_scale=8,
            connectionstyle='arc3,rad=0'),
        zorder=12)
    if label:
        ly = y + (0.09 if label_above else -0.09)
        va = 'bottom' if label_above else 'top'
        txt((x0 + x1) / 2, ly, label, size=5.8, color=ANNOT,
            style='italic', va=va, z=12)


def double_arrow(x0, x1, y, gap=0.07, label=None):
    """Bidirectional arrows (agent ↔ API)."""
    ax.annotate('', xy=(x1, y + gap), xytext=(x0, y + gap),
                arrowprops=dict(arrowstyle='->', color=NAVY, lw=0.7,
                                mutation_scale=7), zorder=12)
    ax.annotate('', xy=(x0, y - gap), xytext=(x1, y - gap),
                arrowprops=dict(arrowstyle='->', color=NAVY, lw=0.7,
                                mutation_scale=7), zorder=12)
    if label:
        txt((x0 + x1) / 2, y, label, size=5.6, color=ANNOT,
            style='italic', z=12)


# ── Stage cards ─────────────────────────────────────────────────────────────
STAGE_LABELS = [
    'INPUT',
    'SYNTHESIS',
    'MCP SERVER',
    'AGENT EVALUATION',
    'SCORING',
]
STAGE_CAPTIONS = [
    ('API Documentation', '14 APIs · 265 evaluation tasks'),
    ('Agentic Tool-Calling Loop', 'reads docs · writes server code'),
    ('Generated MCP Server', '@mcp.tool() decorated functions'),
    ('LLM Evaluation Agent', 'ReAct loop · ≤15 turns per task'),
    ('LLM-as-Judge', 'task verdict · failure cause · server quality'),
]

for i in range(5):
    x0, w = xs[i], W[i]
    # Outer card
    rrect(x0, CARD_Y, w, CARD_H, fc=WHITE, ec=BORDER, lw=0.6, r=0.08, z=2)

    # Header strip fill
    rrect(x0, CARD_Y + CARD_H - HDR_H, w, HDR_H,
          fc=NAVY, ec=NAVY, lw=0, r=0.08, z=3)
    # Square off the bottom corners of the header (overlay rect)
    ax.add_patch(mpatches.Rectangle(
        (x0, CARD_Y + CARD_H - HDR_H),
        w, HDR_H / 2,
        fc=NAVY, ec='none', zorder=3))

    # Stage number (top-left of header)
    txt(x0 + 0.16, CARD_Y + CARD_H - HDR_H / 2,
        str(i + 1), size=6.5, weight='bold', color='#9BAEC4',
        ha='center', va='center', z=6)

    # Stage title
    txt(cx[i] + 0.07, CARD_Y + CARD_H - HDR_H / 2,
        STAGE_LABELS[i], size=8.5, weight='bold', color=WHITE,
        ha='center', va='center', z=6)

    # Divider above caption
    hrule(x0 + 0.12, x0 + w - 0.12, CARD_Y + CAP_H, lw=0.5)

    # Caption
    cap_title, cap_sub = STAGE_CAPTIONS[i]
    txt(cx[i], CARD_Y + CAP_H * 0.66, cap_title,
        size=6.8, weight='bold', color=SUB,
        ha='center', va='center', z=6)
    txt(cx[i], CARD_Y + CAP_H * 0.22, cap_sub,
        size=5.8, color=ANNOT, ha='center', va='center', z=6)


# ── Inter-stage arrows ───────────────────────────────────────────────────────
for i in range(4):
    x0 = xs[i] + W[i] + 0.02
    x1 = xs[i + 1] - 0.02
    labels = [None, 'synthesizes', None, 'eval. trace']
    arrow(x0, x1, ARR_Y, label=labels[i])


# ══════════════════════════════════════════════════════════════════════════════
# Stage 1 — INPUT
# Three synthesis conditions as stacked variant tags
# ══════════════════════════════════════════════════════════════════════════════
i = 0
x0, w = xs[i], W[i]
bw = w - 2 * PAD
bx = x0 + PAD

# Three condition boxes
conditions = [
    ('docs',    'Full API documentation',   '#DDE3EF', NAVY),
    ('nodocs',  'Task description only',    '#EEF0F5', BORDER),
    ('mutated', 'Renamed param. docs',      '#EEF0F5', BORDER),
]
cond_h = 0.54
cond_gap = 0.12
stack_h = 3 * cond_h + 2 * cond_gap
stack_bot = MID_Y - stack_h / 2 + 0.10

for ci, (tag, desc, fill, ec) in enumerate(conditions):
    cy = stack_bot + (2 - ci) * (cond_h + cond_gap)
    rrect(bx, cy, bw, cond_h, fc=fill, ec=ec, lw=0.6, r=0.05, z=5)
    txt(bx + 0.12, cy + cond_h / 2,
        tag, size=7.2, weight='bold', color=NAVY if ci == 0 else SUB,
        ha='left', va='center', z=7, family='monospace')
    txt(bx + bw - 0.10, cy + cond_h / 2,
        desc, size=6.4, color=ANNOT,
        ha='right', va='center', z=7)

# Brace-style label
brace_x = bx - 0.06
brace_top = stack_bot + 3 * cond_h + 2 * cond_gap
brace_bot = stack_bot
brace_mid = (brace_top + brace_bot) / 2
ax.plot([brace_x, brace_x - 0.06, brace_x - 0.06, brace_x],
        [brace_top, brace_top, brace_bot, brace_bot],
        color=RULE, lw=0.7, zorder=6)
txt(brace_x - 0.10, brace_mid, 'condition',
    size=5.8, color=ANNOT, style='italic',
    ha='right', va='center', z=7)

# ══════════════════════════════════════════════════════════════════════════════
# Stage 2 — SYNTHESIS
# Circle (LLM) + tool labels below
# ══════════════════════════════════════════════════════════════════════════════
i = 1
x0, w = xs[i], W[i]
circle_r = 0.72
circle_cy = MID_Y + 0.22

ax.add_patch(plt.Circle(
    (cx[i], circle_cy), circle_r,
    fc=WHITE, ec=NAVY, lw=0.85, zorder=5))
txt(cx[i], circle_cy + 0.13, 'Synthesis', size=8.0, weight='bold',
    color=NAVY, z=7)
txt(cx[i], circle_cy - 0.16, 'LLM', size=6.8, color=SUB, z=7)

tool_y = circle_cy - circle_r - 0.24
txt(cx[i], tool_y + 0.12, 'read  ·  list  ·  glob',
    size=6.5, color=ANNOT, family='monospace', z=6)
txt(cx[i], tool_y - 0.10, 'grep  ·  write  ·  edit',
    size=6.5, color=ANNOT, family='monospace', z=6)

# ══════════════════════════════════════════════════════════════════════════════
# Stage 3 — MCP SERVER
# Stack of three component cards
# ══════════════════════════════════════════════════════════════════════════════
i = 2
x0, w = xs[i], W[i]
bw = w - 2 * PAD
bx = x0 + PAD

cards = [
    ('Tool Functions',  'N tools · @mcp.tool()'),
    ('API Client',      'auth + HTTP · Bearer/OAuth'),
    ('MCP Protocol',    'FastMCP · stdio transport'),
]
card_h = 0.58
card_gap = 0.13
stack_h = len(cards) * card_h + (len(cards) - 1) * card_gap
stack_bot = MID_Y - stack_h / 2 + 0.08

for ci, (title, sub) in enumerate(cards):
    cy = stack_bot + (len(cards) - 1 - ci) * (card_h + card_gap)
    fill = FILL_B if ci == 0 else FILL_A
    rrect(bx, cy, bw, card_h, fc=fill, ec=NAVY if ci == 0 else BORDER,
          lw=0.65 if ci == 0 else 0.5, r=0.05, z=5)
    txt(cx[i], cy + card_h * 0.62, title,
        size=7.4, weight='bold', color=NAVY if ci == 0 else SUB,
        ha='center', va='center', z=7)
    txt(cx[i], cy + card_h * 0.26, sub,
        size=6.0, color=ANNOT, ha='center', va='center', z=7)

# ══════════════════════════════════════════════════════════════════════════════
# Stage 4 — AGENT EVALUATION
# Eval LLM ↔ Live API
# ══════════════════════════════════════════════════════════════════════════════
i = 3
x0, w = xs[i], W[i]

r_e  = 0.60
ecx  = x0 + PAD + r_e + 0.04
ecy  = MID_Y + 0.06

ax.add_patch(plt.Circle(
    (ecx, ecy), r_e,
    fc=WHITE, ec=NAVY, lw=0.85, zorder=5))
txt(ecx, ecy + 0.12, 'Eval.', size=7.8, weight='bold', color=NAVY, z=7)
txt(ecx, ecy - 0.15, 'LLM',  size=6.5, color=SUB, z=7)

# API box
api_w, api_h = 1.00, 0.78
api_x = x0 + w - PAD - api_w
api_y = ecy - api_h / 2
rrect(api_x, api_y, api_w, api_h, fc=FILL_B, ec=NAVY, lw=0.65, r=0.05, z=5)
txt(api_x + api_w / 2, api_y + api_h * 0.62,
    'Live', size=7.4, weight='bold', color=NAVY, z=7)
txt(api_x + api_w / 2, api_y + api_h * 0.26,
    'API', size=7.4, weight='bold', color=NAVY, z=7)

double_arrow(ecx + r_e + 0.06, api_x - 0.04, ecy,
             gap=0.09, label='tool calls / results')

# Note below
txt(cx[i], ecy - r_e - 0.26,
    'via synthesized MCP tools',
    size=6.0, color=ANNOT, style='italic', z=6)

# ══════════════════════════════════════════════════════════════════════════════
# Stage 5 — SCORING (LLM-as-Judge)
# Rubric A/B/C/D grid  +  verdict rows  +  server quality pill
# ══════════════════════════════════════════════════════════════════════════════
i = 4
x0, w = xs[i], W[i]
bw = w - 2 * PAD
bx = x0 + PAD

# ── Rubric dimension 2×2 grid ───────────────────────────────────────────────
rubric = [
    ('A', 'Tool Selection',    '0–2'),
    ('B', 'Param. Quality',    '0–2'),
    ('C', 'Result Interp.',    '0–2'),
    ('D', 'Task Completion',   '0–2'),
]
rcw = (bw - 0.08) / 2
rch = 0.50
rcgap_x = 0.08
rcgap_y = 0.10
rubric_top = BODY_TOP - 0.18

for ri, (letter, dim, pts) in enumerate(rubric):
    col = ri % 2
    row = ri // 2
    rx = bx + col * (rcw + rcgap_x)
    ry = rubric_top - (row + 1) * rch - row * rcgap_y
    rrect(rx, ry, rcw, rch, fc=FILL_A, ec=BORDER, lw=0.5, r=0.04, z=5)
    txt(rx + 0.12, ry + rch / 2,
        letter + '.', size=7.0, weight='bold', color=NAVY,
        ha='left', va='center', z=7)
    txt(rx + rcw / 2 + 0.06, ry + rch * 0.62,
        dim, size=6.5, weight='bold', color=SUB,
        ha='center', va='center', z=7)
    txt(rx + rcw / 2 + 0.06, ry + rch * 0.24,
        pts + ' pts', size=5.8, color=ANNOT,
        ha='center', va='center', z=7)

rubric_bot = rubric_top - 2 * rch - rcgap_y
hrule(bx, bx + bw, rubric_bot - 0.10, lw=0.4)

# ── Verdict rows ─────────────────────────────────────────────────────────────
verdicts = [
    ('PASS',   'score ≥ 5  (A+B ≥ 3)',   '#E8EFF8', NAVY),
    ('FAIL',   'score < 5  (or A+B < 3)', '#F4F4F4', BORDER),
    ('INDET.', 'agent / env / task',       '#F4F4F4', BORDER),
]
verd_h  = 0.40
verd_gap = 0.06
verd_top = rubric_bot - 0.22

for vi, (label, desc, fill, ec) in enumerate(verdicts):
    vy = verd_top - vi * (verd_h + verd_gap) - verd_h
    rrect(bx, vy, bw, verd_h, fc=fill, ec=ec, lw=0.5, r=0.04, z=5)
    txt(bx + 0.14, vy + verd_h / 2,
        label, size=7.2, weight='bold', color=NAVY if vi == 0 else SUB,
        ha='left', va='center', z=7, family='monospace')
    txt(bx + bw - 0.10, vy + verd_h / 2,
        desc, size=6.0, color=ANNOT,
        ha='right', va='center', z=7)

verd_bot = verd_top - 3 * verd_h - 2 * verd_gap
hrule(bx, bx + bw, verd_bot - 0.10, lw=0.4)

# ── Server sufficient pill ────────────────────────────────────────────────────
sv_h = 0.44
sv_y = verd_bot - 0.22 - sv_h
rrect(bx, sv_y, bw, sv_h, fc=FILL_B, ec=NAVY, lw=0.6, r=0.04, z=5)
txt(cx[i], sv_y + sv_h * 0.64,
    'Server Sufficient  (SYNTH metric)',
    size=6.8, weight='bold', color=NAVY, z=7)
txt(cx[i], sv_y + sv_h * 0.24,
    'A + B ≥ 3  ·  YES / NO / UNKN.',
    size=6.0, color=ANNOT, z=7)

# ── Section micro-labels ──────────────────────────────────────────────────────
txt(cx[i], rubric_top + 0.09,
    'Rubric Dimensions (0–8 pts total)',
    size=6.0, color=ANNOT, style='italic', z=6)
txt(cx[i], verd_top + 0.09,
    'Task Verdict',
    size=6.0, color=ANNOT, style='italic', z=6)
txt(cx[i], verd_bot - 0.10,
    'Server Quality',
    size=6.0, color=ANNOT, style='italic', z=6)


# ── Save ────────────────────────────────────────────────────────────────────
plt.tight_layout(pad=0)
for ext in ('png', 'pdf'):
    fname = f'benchmark_pipeline_thesis.{ext}'
    dpi = 300 if ext == 'png' else None
    plt.savefig(fname, dpi=dpi, bbox_inches='tight', facecolor='white')
    print(f'Saved {fname}')
