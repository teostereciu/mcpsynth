"""
Thesis pipeline figure v3 — uses Bootstrap Icons (MIT) SVG paths directly
in matplotlib, so the output is fully vector (scales to any DPI, prints crisply).

Icon loading strategy:
  1. Fetch SVG from Bootstrap Icons GitHub CDN (cached locally as .svg)
  2. Parse all <path d="..."> elements with xml.etree
  3. Convert SVG path strings → matplotlib Path via svgpathtools-style mini-parser
     (handles M, L, H, V, C, S, Q, T, A, Z — sufficient for Bootstrap Icons)
  4. Place with AffineTransform to scale/translate into figure coordinates

All icons are MIT licensed (Bootstrap Icons v1.11.3).
"""

import os, re, io, math
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.path as mpath
import matplotlib.transforms as mtransforms
from matplotlib.patches import FancyBboxPatch, PathPatch
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import requests
from PIL import Image, ImageDraw

matplotlib.rcParams.update({
    'font.family':     'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Arial', 'DejaVu Sans'],
    'pdf.fonttype':    42,
    'ps.fonttype':     42,
})

# ── Icon cache ───────────────────────────────────────────────────────────────
ICON_CACHE = os.path.join(os.path.dirname(__file__), '.icon_cache')
os.makedirs(ICON_CACHE, exist_ok=True)

BI_BASE = 'https://raw.githubusercontent.com/twbs/icons/v1.11.3/icons/{name}.svg'

def fetch_svg(name: str) -> str:
    path = os.path.join(ICON_CACHE, f'{name}.svg')
    if not os.path.exists(path):
        url = BI_BASE.format(name=name)
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        with open(path, 'w') as f:
            f.write(r.text)
    with open(path) as f:
        return f.read()


# ── SVG path → matplotlib Path ───────────────────────────────────────────────
# Lightweight parser for the subset of SVG path commands used in Bootstrap Icons.

def _tok(d: str):
    """Tokenise an SVG path 'd' attribute into (cmd, args) pairs."""
    tokens = re.findall(r'[MLHVCSQTAZmlhvcsqtaz]|[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?', d)
    out, cmd, nums = [], None, []
    def flush():
        if cmd is not None:
            out.append((cmd, nums[:]))
    for t in tokens:
        if t.isalpha():
            flush(); cmd = t; nums = []
        else:
            nums.append(float(t))
    flush()
    return out

def svg_path_to_mpl(d: str, sx=1, sy=-1, tx=0, ty=16):
    """
    Convert SVG path string to matplotlib Path.
    Default sy=-1, ty=16 flips the y-axis (SVG y goes down, matplotlib up).
    sx,sy,tx,ty define the linear transform applied to each coordinate.
    """
    MOVETO  = mpath.Path.MOVETO
    LINETO  = mpath.Path.LINETO
    CURVE4  = mpath.Path.CURVE4
    CURVE3  = mpath.Path.CURVE3
    CLOSEPOLY = mpath.Path.CLOSEPOLY

    verts, codes = [], []
    cx, cy = 0.0, 0.0   # current point
    lx, ly = 0.0, 0.0   # last control point (for S/T reflection)
    last_cmd = ''

    def T(x, y):
        return tx + sx*x, ty + sy*y

    for cmd, args in _tok(d):
        rel = cmd.islower()
        C = cmd.upper()

        def abs_xy(i):
            x, y = args[i], args[i+1]
            if rel: x += cx; y += cy
            return x, y

        if C == 'M':
            for i in range(0, len(args), 2):
                x, y = abs_xy(i)
                verts.append(T(x, y)); codes.append(MOVETO if i == 0 else LINETO)
                cx, cy = x, y
        elif C == 'L':
            for i in range(0, len(args), 2):
                x, y = abs_xy(i)
                verts.append(T(x, y)); codes.append(LINETO)
                cx, cy = x, y
        elif C == 'H':
            for v in args:
                x = (cx + v) if rel else v
                verts.append(T(x, cy)); codes.append(LINETO)
                cx = x
        elif C == 'V':
            for v in args:
                y = (cy + v) if rel else v
                verts.append(T(cx, y)); codes.append(LINETO)
                cy = y
        elif C == 'C':
            for i in range(0, len(args), 6):
                x1, y1 = abs_xy(i);   x2, y2 = abs_xy(i+2);  x, y = abs_xy(i+4)
                verts += [T(x1,y1), T(x2,y2), T(x,y)]
                codes += [CURVE4, CURVE4, CURVE4]
                lx, ly = x2, y2; cx, cy = x, y
        elif C == 'S':
            for i in range(0, len(args), 4):
                # reflect last control point
                x1 = 2*cx - lx; y1 = 2*cy - ly
                x2, y2 = abs_xy(i);  x, y = abs_xy(i+2)
                verts += [T(x1,y1), T(x2,y2), T(x,y)]
                codes += [CURVE4, CURVE4, CURVE4]
                lx, ly = x2, y2; cx, cy = x, y
        elif C == 'Q':
            for i in range(0, len(args), 4):
                x1, y1 = abs_xy(i);  x, y = abs_xy(i+2)
                verts += [T(x1,y1), T(x,y)]
                codes += [CURVE3, CURVE3]
                lx, ly = x1, y1; cx, cy = x, y
        elif C == 'T':
            for i in range(0, len(args), 2):
                x1 = 2*cx - lx; y1 = 2*cy - ly
                x, y = abs_xy(i)
                verts += [T(x1,y1), T(x,y)]
                codes += [CURVE3, CURVE3]
                lx, ly = x1, y1; cx, cy = x, y
        elif C == 'A':
            # Approximate arc with a line-to for simplicity
            for i in range(0, len(args), 7):
                x, y = abs_xy(i+5)
                verts.append(T(x, y)); codes.append(LINETO)
                cx, cy = x, y
        elif C == 'Z':
            verts.append((0, 0)); codes.append(CLOSEPOLY)

        last_cmd = C

    if not verts:
        return None
    return mpath.Path(np.array(verts), codes)


def place_icon(ax, svg_name, cx, cy, size, color, z=10, alpha=1.0):
    """
    Fetch the Bootstrap Icon SVG, parse its paths, and render at (cx, cy)
    in data coordinates, scaled so the icon fits in a box of `size` units.
    The SVG viewBox is 0..16 × 0..16.
    """
    svg = fetch_svg(svg_name)
    root = ET.fromstring(svg)
    ns = {'svg': 'http://www.w3.org/2000/svg'}

    # Collect all <path d="..."> elements (direct children and nested)
    paths_d = [el.get('d') for el in root.iter() if el.tag.endswith('}path') or el.tag == 'path']
    paths_d = [p for p in paths_d if p]

    # Scale: SVG is 16×16 units → we want `size` data units
    scale = size / 16.0
    # Offset: centre at (cx, cy) — SVG origin is top-left
    tx = cx - size/2
    ty = cy + size/2   # flipped because we negate y

    for d in paths_d:
        mp = svg_path_to_mpl(d, sx=scale, sy=-scale, tx=tx, ty=ty)
        if mp is not None:
            ax.add_patch(PathPatch(mp, fc=color, ec='none',
                                   alpha=alpha, zorder=z))


# ══════════════════════════════════════════════════════════════════════════════
# Figure
# ══════════════════════════════════════════════════════════════════════════════

W, H = 12.0, 4.6
fig, ax = plt.subplots(figsize=(W, H))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')

# ── Palette ──────────────────────────────────────────────────────────────────
NAVY    = '#1B2E5E'
RULE    = '#B8C2D0'
BORDER  = '#8C9BAD'
SUB     = '#4A5568'
ANNOT   = '#718096'
WHITE   = '#FFFFFF'

# Semantic role colours
AMBER   = '#B45309'   # Tool-Maker LLM (synthesis / creation)
TEAL    = '#065F46'   # Agent LLM + Live API (active / real-world)
VIOLET  = '#5B21B6'   # Judge LLM (evaluation / judgment)
GREEN   = '#059669'   # PASS / SERVER_SUFFICIENT
RED     = '#B91C1C'   # FAIL / failure causes

# Background fills
SYNTH_BG  = '#EDF1F8'   # synthesis phase
EVAL_BG   = '#F5F6F8'   # eval phase
FILL_A    = '#DDE3EF'   # input docs / MCP server
FILL_N    = '#ECEEF2'   # neutral boxes
AMBER_BG  = '#FFF7ED'   # mutated condition row
VIOLET_BG = '#F5F3FF'   # nodocs condition row
GREEN_BG  = '#ECFDF5'   # PASS / MCP / Live API / SERVER_SUFFICIENT
RED_BG    = '#FEF2F2'   # FAIL / failure causes
AMBER_V   = '#FFFBEB'   # UNDEF verdict

# ── Phase geometry ────────────────────────────────────────────────────────────
PHASE_Y  = 0.32
PHASE_H  = 3.96
SPLIT_X  = 5.30
MARG_X   = 0.22
MARG_R   = 0.22
MID_Y    = PHASE_Y + PHASE_H / 2

def phase_box(x, y, w, h, fc, label, lc):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle="round,pad=0,rounding_size=0.12",
        fc=fc, ec=RULE, lw=0.5, zorder=1))
    ax.text(x + 0.18, y + h - 0.20, label,
            ha='left', va='top', fontsize=8.5,
            fontweight='bold', color=lc, alpha=0.65, zorder=4)

phase_box(MARG_X, PHASE_Y,
          SPLIT_X - MARG_X - 0.10, PHASE_H, SYNTH_BG,
          'SYNTHESIS  (offline, per API)', NAVY)
phase_box(SPLIT_X + 0.10, PHASE_Y,
          W - SPLIT_X - 0.10 - MARG_R, PHASE_H, EVAL_BG,
          'EVALUATION  (online, per task)', SUB)

# Eval content is shifted up relative to MID_Y to give bottom breathing room
EVAL_MID_Y = MID_Y + 0.14

# ── Helpers ───────────────────────────────────────────────────────────────────
def rrect(x, y, w, h, fc=WHITE, ec=BORDER, lw=0.6, r=0.08, z=4):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={r}",
        fc=fc, ec=ec, lw=lw, zorder=z, clip_on=False))

def txt(x, y, s, size=7.8, weight='normal', color=SUB,
        ha='center', va='center', z=8, style='normal', family=None):
    kw = dict(ha=ha, va=va, fontsize=size, fontweight=weight,
              color=color, zorder=z, fontstyle=style)
    if family: kw['fontfamily'] = family
    ax.text(x, y, s, **kw)

def hrule(x0, x1, y, lw=0.5, color=RULE, z=5):
    ax.plot([x0, x1], [y, y], color=color, lw=lw, zorder=z, solid_capstyle='butt')

def arrow(x0, x1, y0, y1=None, label=None, label_side='top', color=NAVY,
          lw=0.9, mutation=8, z=10):
    if y1 is None: y1 = y0
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                mutation_scale=mutation,
                                connectionstyle='arc3,rad=0'), zorder=z)
    if label:
        mx, my = (x0+x1)/2, (y0+y1)/2
        dy = 0.09 if label_side == 'top' else -0.09
        va = 'bottom' if label_side == 'top' else 'top'
        txt(mx, my+dy, label, size=5.8, color=ANNOT, style='italic', va=va, z=z)

def double_arrow(x0, x1, y, gap=0.08, color=NAVY, lw=0.75, label=None):
    ax.annotate('', xy=(x1, y+gap), xytext=(x0, y+gap),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                mutation_scale=7), zorder=10)
    ax.annotate('', xy=(x0, y-gap), xytext=(x1, y-gap),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                mutation_scale=7), zorder=10)
    if label:
        txt((x0+x1)/2, y, label, size=5.6, color=ANNOT, style='italic', z=10)

def varrow_bi(x, y_bot, y_top, gap=0.06, color=NAVY, lw=0.72, label=None):
    """Vertical bidirectional arrow."""
    ax.annotate('', xy=(x-gap, y_top), xytext=(x-gap, y_bot),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                mutation_scale=7), zorder=10)
    ax.annotate('', xy=(x+gap, y_bot), xytext=(x+gap, y_top),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                mutation_scale=7), zorder=10)
    if label:
        txt(x + 0.68, (y_bot+y_top)/2, label, size=5.6,
            color=ANNOT, style='italic', ha='left', z=10)


# ══════════════════════════════════════════════════════════════════════════════
# 1. INPUT — API Documentation with 3 condition variants
# ══════════════════════════════════════════════════════════════════════════════
DOCS_X, DOCS_W, DOCS_H = MARG_X + 0.20, 1.88, 2.90
DOCS_Y = MID_Y - DOCS_H / 2

rrect(DOCS_X, DOCS_Y, DOCS_W, DOCS_H, fc=FILL_A, ec=NAVY, lw=0.7, r=0.07)

# Book-fill icon at top
place_icon(ax, 'book-fill', DOCS_X + 0.36, DOCS_Y + DOCS_H - 0.32, 0.40, NAVY, z=7)
txt(DOCS_X + DOCS_W/2 + 0.20, DOCS_Y + DOCS_H - 0.32,
    'API Documentation', size=9.0, weight='bold', color=NAVY, z=6, ha='center')
hrule(DOCS_X+0.12, DOCS_X+DOCS_W-0.12, DOCS_Y + DOCS_H - 0.58, lw=0.4)

cond_info = [
    ('docs',    'Full endpoint docs',  WHITE,  NAVY,   True,  NAVY),
    ('no docs', 'Zero API context',    FILL_N, BORDER, False, SUB),
    ('mutated', 'Renamed parameters',  FILL_N, BORDER, False, SUB),
]
row_h=0.46; row_gap=0.09
block_h = 3*row_h + 2*row_gap
block_bot = DOCS_Y + (DOCS_H - 0.58 - block_h)/2

for ri, (tag, desc, fc, ec, bold, tc) in enumerate(cond_info):
    ry = block_bot + (2-ri)*(row_h + row_gap)
    rrect(DOCS_X+0.10, ry, DOCS_W-0.20, row_h, fc=fc, ec=ec, lw=0.5, r=0.05)
    ax.text(DOCS_X+0.22, ry+row_h/2, tag,
            ha='left', va='center', fontsize=6.8,
            fontweight='bold' if bold else 'normal',
            color=tc, fontfamily='monospace', zorder=7)
    ax.text(DOCS_X+DOCS_W-0.20, ry+row_h/2, desc,
            ha='right', va='center', fontsize=6.0, color=ANNOT, zorder=7)

# condition bracket
bx = DOCS_X + 0.08
btop = block_bot + 3*row_h + 2*row_gap; bbot = block_bot
ax.plot([bx-0.06, bx-0.11, bx-0.11, bx-0.06],
        [btop, btop, bbot, bbot], color=RULE, lw=0.8, zorder=6)
ax.text(bx-0.18, (btop+bbot)/2, 'condition', size=6.5, color=ANNOT,
        fontstyle='italic', ha='center', va='center', rotation=90, zorder=6)

txt(DOCS_X + DOCS_W/2, DOCS_Y + 0.14,
    '14 REST APIs · high-impact domains', size=5.5, color=ANNOT, style='italic', z=6)


# ══════════════════════════════════════════════════════════════════════════════
# 2. SYNTHESIS LLM — robot icon + label
# ══════════════════════════════════════════════════════════════════════════════
SYNTH_CX = 3.80
SYNTH_ICY = MID_Y - 0.20   # moved down to fill synthesis phase bottom space
ICON_SZ_LG = 0.78    # robot icon size for synthesis
ICON_SZ_MD = 0.66    # for agent/judge

# TASK.md artifact above Tool-Maker LLM
TASKMD_W=1.44; TASKMD_H=0.76
TASKMD_X = SYNTH_CX - TASKMD_W/2
TASKMD_Y = SYNTH_ICY + ICON_SZ_LG*0.50 + 0.26

rrect(TASKMD_X, TASKMD_Y, TASKMD_W, TASKMD_H, fc=FILL_N, ec=BORDER, lw=0.55, r=0.06)
txt(SYNTH_CX, TASKMD_Y + TASKMD_H*0.78,
    'INSTRUCTIONS.md', size=7.0, weight='bold', color=SUB, z=6, family='monospace')
txt(SYNTH_CX, TASKMD_Y + TASKMD_H*0.50,
    'server specs & requirements', size=5.8, color=ANNOT, z=6)
txt(SYNTH_CX, TASKMD_Y + TASKMD_H*0.22,
    'key endpoints to cover', size=5.8, color=ANNOT, z=6)

# Arrow: TASK.md ↓ Tool-Maker LLM
arrow(SYNTH_CX, SYNTH_CX,
      TASKMD_Y - 0.04, SYNTH_ICY + ICON_SZ_LG*0.50 + 0.04, z=9)

arrow(DOCS_X + DOCS_W + 0.07, SYNTH_CX - ICON_SZ_LG*0.50, SYNTH_ICY, label='provided as context', z=9)

place_icon(ax, 'stars', SYNTH_CX, SYNTH_ICY, ICON_SZ_LG, AMBER, z=7)

SYNTH_BOT = SYNTH_ICY - ICON_SZ_LG*0.50
txt(SYNTH_CX, SYNTH_BOT - 0.20, 'Tool-Maker LLM',
    size=7.4, weight='bold', color=AMBER, z=8)

tool_y = SYNTH_BOT - 0.42
txt(SYNTH_CX, tool_y, 'via',
    size=6.0, color=ANNOT, style='italic', z=6)
txt(SYNTH_CX, tool_y - 0.20, 'read  ·  list  ·  glob',
    size=6.0, color=ANNOT, family='monospace', z=6)
txt(SYNTH_CX, tool_y - 0.40, 'grep  ·  write  ·  edit',
    size=6.0, color=ANNOT, family='monospace', z=6)


# ══════════════════════════════════════════════════════════════════════════════
# 3. MCP SERVER — inside eval phase
# ══════════════════════════════════════════════════════════════════════════════
MCP_W=1.62; MCP_H=1.86
MCP_X = SPLIT_X + 0.20
MCP_CX = MCP_X + MCP_W/2
MCP_Y  = EVAL_MID_Y - MCP_H/2

arrow(SYNTH_CX + ICON_SZ_LG*0.50, MCP_X - 0.05, SYNTH_ICY, label='synthesizes', z=9)

rrect(MCP_X, MCP_Y, MCP_W, MCP_H, fc=GREEN_BG, ec=TEAL, lw=0.75, r=0.07)

place_icon(ax, 'plug-fill', MCP_CX, MCP_Y+MCP_H-0.22, 0.34, TEAL, z=7)
txt(MCP_CX, MCP_Y+MCP_H-0.50,
    'MCP Server', size=7.6, weight='bold', color=TEAL, z=6)
hrule(MCP_X+0.10, MCP_X+MCP_W-0.10, MCP_Y+MCP_H-0.70, lw=0.4)

for si, (t, s) in enumerate([('N tool functions','@mcp.tool()'),
                               ('API client','auth + HTTP')]):
    sh = 0.42; sg = 0.10
    sy = MCP_Y + MCP_H - 0.80 - si*(sh+sg) - sh
    rrect(MCP_X+0.10, sy, MCP_W-0.20, sh, fc=GREEN_BG, ec=TEAL, lw=0.45, r=0.04)
    txt(MCP_CX, sy+sh*0.64, t, size=6.8, weight='bold', color=TEAL, z=7)
    txt(MCP_CX, sy+sh*0.24, s, size=6.0, color=ANNOT, z=7)


# ══════════════════════════════════════════════════════════════════════════════
# 4. AGENT LLM + LIVE API
# ══════════════════════════════════════════════════════════════════════════════
AGENT_Y  = EVAL_MID_Y + 0.08
AGENT_CX = MCP_X + MCP_W + 1.00

# Task prompt box (above agent)
TASK_W=1.10; TASK_H=0.72
TASK_X = AGENT_CX - TASK_W/2
TASK_Y = AGENT_Y + ICON_SZ_MD*0.92 + 0.20

rrect(TASK_X, TASK_Y, TASK_W, TASK_H, fc=FILL_N, ec=BORDER, lw=0.55, r=0.06)
txt(TASK_X + TASK_W/2, TASK_Y + TASK_H*0.68,
    'Test task', size=7.0, weight='bold', color=SUB, z=6)
txt(TASK_X + TASK_W/2, TASK_Y + TASK_H*0.30,
    'tasks.yaml  ·  M per API', size=5.8, color=ANNOT, z=6)

# Arrow: task ↓ agent
arrow(AGENT_CX, AGENT_CX,
      TASK_Y - 0.04, AGENT_Y + ICON_SZ_MD*0.50, z=9)

# Agent icon
place_icon(ax, 'lightning-charge-fill', AGENT_CX, AGENT_Y, ICON_SZ_MD, TEAL, z=7)
AGENT_BOT = AGENT_Y - ICON_SZ_MD*0.50
txt(AGENT_CX, AGENT_BOT - 0.18, 'Agent LLM',
    size=7.4, weight='bold', color=TEAL, z=8)

# Double arrow: MCP ↔ Agent
double_arrow(MCP_X+MCP_W+0.05, AGENT_CX-ICON_SZ_MD*0.50,
             AGENT_Y, gap=0.08, label='tool calls / results')

# Live API (below MCP Server)
LAPI_W=1.14; LAPI_H=0.64
LAPI_CX = MCP_CX
LAPI_Y  = MCP_Y - 0.32 - LAPI_H

rrect(LAPI_CX-LAPI_W/2, LAPI_Y, LAPI_W, LAPI_H, fc=GREEN_BG, ec=TEAL, lw=0.65, r=0.06)
place_icon(ax, 'cloud-check', LAPI_CX, LAPI_Y+LAPI_H*0.72, 0.32, TEAL, z=6)
txt(LAPI_CX, LAPI_Y+LAPI_H*0.38, 'Live API',
    size=6.8, weight='bold', color=TEAL, z=6)
txt(LAPI_CX, LAPI_Y+LAPI_H*0.20, 'or sandbox when available',
    size=5.0, color=ANNOT, z=6)

# Vertical bidirectional: MCP ↔ Live API
varrow_bi(MCP_CX, LAPI_Y+LAPI_H+0.04, MCP_Y-0.04,
          gap=0.06, label='HTTP req/resp')


# ══════════════════════════════════════════════════════════════════════════════
# 5. JUDGE LLM + trajectory arrow
# ══════════════════════════════════════════════════════════════════════════════
JUDGE_Y  = EVAL_MID_Y - 1.35
JUDGE_R  = ICON_SZ_MD

_traj_y0 = AGENT_BOT - 0.26
_traj_y1 = JUDGE_Y + JUDGE_R*0.50 + 0.04
arrow(AGENT_CX, AGENT_CX, _traj_y0, _traj_y1, z=9)
txt(AGENT_CX, (_traj_y0 + _traj_y1) / 2,
    'trajectory  ·  ≤15 turns', size=5.8, color=ANNOT,
    style='italic', ha='center', va='center', z=9)

place_icon(ax, 'shield-fill-check', AGENT_CX, JUDGE_Y, JUDGE_R, VIOLET, z=7)
JUDGE_BOT = JUDGE_Y - JUDGE_R*0.50
txt(AGENT_CX, JUDGE_BOT - 0.16, 'Judge LLM',
    size=7.4, weight='bold', color=VIOLET, z=8)


# ══════════════════════════════════════════════════════════════════════════════
# 6. VERDICT PANEL
# ══════════════════════════════════════════════════════════════════════════════
VERD_X  = AGENT_CX + JUDGE_R*0.48 + 0.42   # shifted right
VERD_W  = W - MARG_R - VERD_X - 0.20
VERD_H  = PHASE_H - 0.50
VERD_Y  = PHASE_Y + 0.25

rrect(VERD_X, VERD_Y, VERD_W, VERD_H, fc=WHITE, ec=VIOLET, lw=1.1, r=0.08)

# Arrow: judge → verdict panel
arrow(AGENT_CX + JUDGE_R*0.50, VERD_X - 0.04, JUDGE_Y, z=9)

# ── Shared spacing constants for verdict panel ────────────────────────────────
_PAD  = 0.08   # uniform gap between sections and between shape-top and label
_HDR  = 0.26   # header text inset from top
_HR1  = 0.44   # first hrule from top
_VRT  = 0.52   # verdict rows start-from-top

# Header
txt(VERD_X + VERD_W/2, VERD_Y+VERD_H-_HDR,
    'Task Verdict', size=8.5, weight='bold', color=VIOLET,
    ha='center', z=7)
hrule(VERD_X+0.10, VERD_X+VERD_W-0.10, VERD_Y+VERD_H-_HR1, lw=0.4)

# Verdict rows
verdicts = [
    ('PASS',  'agent completed task correctly', GREEN_BG, GREEN,  GREEN),
    ('FAIL',  'tool-side failure  (see cause)', RED_BG,   RED,    RED),
    ('UNDEF', 'agent / env / task confound',    AMBER_V,  AMBER,  AMBER),
]
vr_h=0.36; vr_gap=_PAD
vr_top = VERD_Y + VERD_H - _VRT
vr_x = VERD_X+0.10; vr_w = VERD_W-0.20

for vi, (label, desc, fc, ec, tc) in enumerate(verdicts):
    vy = vr_top - vi*(vr_h+vr_gap) - vr_h
    rrect(vr_x, vy, vr_w, vr_h, fc=fc, ec=ec, lw=0.55, r=0.04)
    ax.text(vr_x+0.12, vy+vr_h/2, label,
            ha='left', va='center', fontsize=6.8, fontweight='bold',
            color=tc, fontfamily='monospace', zorder=7)
    ax.text(vr_x+vr_w-0.10, vy+vr_h/2, desc,
            ha='right', va='center', fontsize=5.8, color=ANNOT, zorder=7)

# Section divider after verdict rows
fc_top = vr_top - 3*(vr_h+vr_gap)
hrule(VERD_X+0.10, VERD_X+VERD_W-0.10, fc_top - _PAD, lw=0.4)

# Failure cause taxonomy
txt(VERD_X+VERD_W/2, fc_top - _PAD*2.2,
    'Failure cause (when FAIL)', size=6.0, color=ANNOT, style='italic', z=6)

causes = ['TOOL_COVERAGE', 'TOOL_SCHEMA', 'TOOL_IMPLEMENTATION', 'TOOL_DOCUMENTATION']
fc_h=0.24; fc_gx=0.07; fc_gy=_PAD*0.7
fc_cw = (vr_w - fc_gx)/2
fc_bot = fc_top - _PAD*3.2

for ci, cause in enumerate(causes):
    col=ci%2; row=ci//2
    cx_fc = vr_x + col*(fc_cw+fc_gx)
    cy_fc = fc_bot - row*(fc_h+fc_gy) - fc_h
    rrect(cx_fc, cy_fc, fc_cw, fc_h, fc=RED_BG, ec=RED, lw=0.40, r=0.03)
    ax.text(cx_fc+fc_cw/2, cy_fc+fc_h/2, cause,
            ha='center', va='center', fontsize=5.3,
            color=RED, fontfamily='monospace', zorder=7)

# Section divider before SERVER_SUFFICIENT
ss_sep = fc_bot - 2*(fc_h+fc_gy)
hrule(VERD_X+0.10, VERD_X+VERD_W-0.10, ss_sep - _PAD, lw=0.4)

txt(VERD_X+VERD_W/2, ss_sep - _PAD*2.2,
    'Server quality  (independent of agent)', size=6.0, color=ANNOT, style='italic', z=6)

ss_h=0.34; ss_y = ss_sep - _PAD*3.2 - ss_h
rrect(vr_x, ss_y, vr_w, ss_h, fc=GREEN_BG, ec=GREEN, lw=0.65, r=0.04)
txt(VERD_X+VERD_W/2, ss_y+ss_h*0.68,
    'SERVER_SUFFICIENT',
    size=6.6, weight='bold', color=GREEN, z=7)
txt(VERD_X+VERD_W/2, ss_y+ss_h*0.40,
    'did the server provide a usable, correct tool?',
    size=5.4, color=ANNOT, z=7)
txt(VERD_X+VERD_W/2, ss_y+ss_h*0.14,
    'YES / NO / UNKNOWN',
    size=5.4, color=ANNOT, z=7)


# ── Save ─────────────────────────────────────────────────────────────────────
plt.tight_layout(pad=0)
for ext in ('png', 'pdf'):
    fname = f'benchmark_pipeline_thesis_v3.{ext}'
    dpi = 300 if ext == 'png' else None
    plt.savefig(fname, dpi=dpi, bbox_inches='tight', facecolor='white')
    print(f'Saved {fname}')
