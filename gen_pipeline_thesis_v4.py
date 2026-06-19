"""
Benchmark pipeline figure v4 — revised.

Design:
  - No numbered badges.
  - INSTRUCTIONS.md as external dashed artifact above Tool-Maker (mirrors
    Test-task above Agent LLM).
  - Pastel card-header palette (lighter, softer than v4.0).
  - Compact canvas: 13.0 × 4.9 in.
  - Phase regions: tinted bg + colored border + bold title.
  - Every active component = card (solid colored header + white body).
"""

import os, re, math
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, PathPatch, Circle
import requests

matplotlib.rcParams.update({
    'font.family':  'serif',
    'font.serif':   ['CMU Serif', 'Computer Modern', 'Palatino',
                     'Georgia', 'DejaVu Serif', 'Times New Roman'],
    'pdf.fonttype': 42,
    'ps.fonttype':  42,
})

# ── Icons ─────────────────────────────────────────────────────────────────────
ICON_CACHE = os.path.join(os.path.dirname(__file__), '.icon_cache')
os.makedirs(ICON_CACHE, exist_ok=True)

def fetch_svg(name):
    p = os.path.join(ICON_CACHE, f'{name}.svg')
    if not os.path.exists(p):
        r = requests.get(
            f'https://raw.githubusercontent.com/twbs/icons/v1.11.3/icons/{name}.svg',
            timeout=15)
        r.raise_for_status()
        open(p, 'w').write(r.text)
    return open(p).read()

def _tok(d):
    toks = re.findall(
        r'[MLHVCSQTAZmlhvcsqtaz]|[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?', d)
    out, cmd, nums = [], None, []
    def flush():
        if cmd: out.append((cmd, nums[:]))
    for tk in toks:
        if tk.isalpha(): flush(); cmd = tk; nums = []
        else: nums.append(float(tk))
    flush()
    return out

def _arc_to_beziers(x1, y1, rx, ry, x_rot, fa, fs, x2, y2):
    """Convert one SVG elliptical-arc segment to cubic Bézier triples."""
    if rx == 0 or ry == 0 or (x1 == x2 and y1 == y2):
        return [(x2, y2, x2, y2, x2, y2)]
    phi = math.radians(x_rot % 360)
    cp, sp = math.cos(phi), math.sin(phi)
    dx2, dy2 = (x1 - x2) / 2, (y1 - y2) / 2
    x1p =  cp*dx2 + sp*dy2
    y1p = -sp*dx2 + cp*dy2
    rx, ry = abs(rx), abs(ry)
    x1ps, y1ps, rxs, rys = x1p*x1p, y1p*y1p, rx*rx, ry*ry
    lam = x1ps/rxs + y1ps/rys
    if lam > 1:
        s = math.sqrt(lam); rx*=s; ry*=s; rxs*=lam; rys*=lam
    num = max(0, rxs*rys - rxs*y1ps - rys*x1ps)
    den = rxs*y1ps + rys*x1ps
    sq = (math.sqrt(num/den) if den else 0) * (-1 if fa == fs else 1)
    cxp =  sq*rx*y1p/ry
    cyp = -sq*ry*x1p/rx
    mx, my = (x1+x2)/2, (y1+y2)/2
    cx = cp*cxp - sp*cyp + mx
    cy = sp*cxp + cp*cyp + my

    def ang(ux,uy,vx,vy):
        n = math.sqrt((ux*ux+uy*uy)*(vx*vx+vy*vy))
        c = max(-1., min(1., (ux*vx+uy*vy)/n)) if n else 1.
        a = math.acos(c)
        return -a if (ux*vy - uy*vx < 0) else a

    theta = ang(1,0,(x1p-cxp)/rx,(y1p-cyp)/ry)
    dth   = ang((x1p-cxp)/rx,(y1p-cyp)/ry,(-x1p-cxp)/rx,(-y1p-cyp)/ry)
    if not fs and dth > 0: dth -= 2*math.pi
    elif fs and dth < 0:   dth += 2*math.pi

    n_seg = max(1, int(math.ceil(abs(dth)/(math.pi/2))))
    dt = dth/n_seg
    out = []
    for i in range(n_seg):
        t0, t1 = theta+i*dt, theta+(i+1)*dt
        a = math.sin(t1-t0)*(math.sqrt(4+3*math.tan((t1-t0)/2)**2)-1)/3
        def pt(t):
            return (cx+cp*rx*math.cos(t)-sp*ry*math.sin(t),
                    cy+sp*rx*math.cos(t)+cp*ry*math.sin(t))
        def dp(t):
            return (-cp*rx*math.sin(t)-sp*ry*math.cos(t),
                    -sp*rx*math.sin(t)+cp*ry*math.cos(t))
        p0=pt(t0); p1_=pt(t1); d0=dp(t0); d1=dp(t1)
        out.append((p0[0]+a*d0[0], p0[1]+a*d0[1],
                    p1_[0]-a*d1[0], p1_[1]-a*d1[1],
                    p1_[0], p1_[1]))
    return out


def svg_to_mpl(d, sx=1, sy=-1, tx=0, ty=16):
    MO,LI,C4,C3,CP = (mpath.Path.MOVETO, mpath.Path.LINETO,
                       mpath.Path.CURVE4, mpath.Path.CURVE3, mpath.Path.CLOSEPOLY)
    verts, codes, cx, cy, lx, ly = [], [], 0., 0., 0., 0.
    def T(x,y): return tx+sx*x, ty+sy*y
    def Ap(args,i,rel):
        x,y=args[i],args[i+1]
        if rel: x+=cx; y+=cy
        return x,y
    for cmd, args in _tok(d):
        rel=cmd.islower(); C=cmd.upper()
        if C=='M':
            for i in range(0,len(args),2):
                x,y=Ap(args,i,rel); verts.append(T(x,y))
                codes.append(MO if i==0 else LI); cx,cy=x,y
        elif C=='L':
            for i in range(0,len(args),2):
                x,y=Ap(args,i,rel); verts.append(T(x,y)); codes.append(LI); cx,cy=x,y
        elif C=='H':
            for v in args:
                x=cx+v if rel else v; verts.append(T(x,cy)); codes.append(LI); cx=x
        elif C=='V':
            for v in args:
                y=cy+v if rel else v; verts.append(T(cx,y)); codes.append(LI); cy=y
        elif C=='C':
            for i in range(0,len(args),6):
                x1,y1=Ap(args,i,rel); x2,y2=Ap(args,i+2,rel); x,y=Ap(args,i+4,rel)
                verts+=[T(x1,y1),T(x2,y2),T(x,y)]; codes+=[C4,C4,C4]
                lx,ly=x2,y2; cx,cy=x,y
        elif C=='S':
            for i in range(0,len(args),4):
                x1,y1=2*cx-lx,2*cy-ly; x2,y2=Ap(args,i,rel); x,y=Ap(args,i+2,rel)
                verts+=[T(x1,y1),T(x2,y2),T(x,y)]; codes+=[C4,C4,C4]
                lx,ly=x2,y2; cx,cy=x,y
        elif C=='Q':
            for i in range(0,len(args),4):
                x1,y1=Ap(args,i,rel); x,y=Ap(args,i+2,rel)
                verts+=[T(x1,y1),T(x,y)]; codes+=[C3,C3]; lx,ly=x1,y1; cx,cy=x,y
        elif C=='T':
            for i in range(0,len(args),2):
                x1,y1=2*cx-lx,2*cy-ly; x,y=Ap(args,i,rel)
                verts+=[T(x1,y1),T(x,y)]; codes+=[C3,C3]; lx,ly=x1,y1; cx,cy=x,y
        elif C=='A':
            for i in range(0,len(args),7):
                rx_,ry_,xr,fa,fs = args[i],args[i+1],args[i+2],int(args[i+3]),int(args[i+4])
                ex,ey = Ap(args,i+5,rel)
                for cp1x,cp1y,cp2x,cp2y,epx,epy in _arc_to_beziers(
                        cx,cy,rx_,ry_,xr,fa,fs,ex,ey):
                    verts+=[T(cp1x,cp1y),T(cp2x,cp2y),T(epx,epy)]
                    codes+=[C4,C4,C4]
                cx,cy=ex,ey; lx,ly=cx,cy
        elif C=='Z':
            verts.append((0,0)); codes.append(CP)
    if not verts: return None
    return mpath.Path(np.array(verts), codes)

def place_icon(ax, name, cx, cy, size, color, z=10):
    svg  = fetch_svg(name)
    root = ET.fromstring(svg)
    sc   = size / 16.0
    for el in root.iter():
        if el.tag.endswith('}path') or el.tag == 'path':
            d = el.get('d')
            if d:
                mp = svg_to_mpl(d, sx=sc, sy=-sc, tx=cx-size/2, ty=cy+size/2)
                if mp:
                    ax.add_patch(PathPatch(mp, fc=color, ec='none', zorder=z))


# ══════════════════════════════════════════════════════════════════════════════
# Pastel palette
# ══════════════════════════════════════════════════════════════════════════════
# Card header fills — medium-toned pastels (white text readable, but soft)
AMBER  = '#B8703A'   # dusty terracotta / warm amber
BLUE   = '#3A80B0'   # cornflower / steel blue
TEAL   = '#2A9478'   # seafoam teal
PURPLE = '#7A4E96'   # soft violet

NAVY   = '#2E4E72'   # slate navy (API docs border, arrows)

WHITE  = '#FFFFFF'
GRAY   = '#4A5568'
DIM    = '#8895A8'
RULE   = '#C8D4E0'
LIGHT  = '#F2F5F9'

# Phase region tints & borders
SYNTH_BG = '#FEF5ED'; SYNTH_EC = '#D4906A'
EVAL_BG  = '#EEF4FD'; EVAL_EC  = '#7AAAD6'

# Verdict row colors
G_EC='#2E7A50'; G_BG='#EDF7F2'
R_EC='#9A3A3A'; R_BG='#FEF0F0'
A_EC='#8A7020'; A_BG='#FDFAEE'


# ══════════════════════════════════════════════════════════════════════════════
# Canvas
# ══════════════════════════════════════════════════════════════════════════════
W, H = 13.0, 4.9
fig, ax = plt.subplots(figsize=(W, H))
fig.patch.set_facecolor(WHITE)
ax.set_facecolor(WHITE)
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')

MID   = H / 2        # 2.45
PAD   = 0.20
SPLIT = 4.90         # synthesis | evaluation boundary

# ── Phase regions ─────────────────────────────────────────────────────────────
PH_Y = PAD * 0.7                # 0.14
PH_H = H - PAD * 1.4            # 4.62

for x, w, bg, ec, label, lc in [
    (PAD,        SPLIT-PAD-0.10,   SYNTH_BG, SYNTH_EC,
     'SYNTHESIS  (offline, per API)',  AMBER),
    (SPLIT+0.10, W-SPLIT-0.10-PAD, EVAL_BG,  EVAL_EC,
     'EVALUATION  (online, per task)', BLUE),
]:
    ax.add_patch(FancyBboxPatch((x, PH_Y), w, PH_H,
        boxstyle='round,pad=0,rounding_size=0.14',
        fc=bg, ec=ec, lw=1.1, zorder=1))
    ax.text(x+0.20, PH_Y+PH_H-0.16, label,
            ha='left', va='top', fontsize=9.5, fontweight='bold',
            color=lc, alpha=0.85, zorder=2)


# ══════════════════════════════════════════════════════════════════════════════
# Drawing helpers
# ══════════════════════════════════════════════════════════════════════════════
BAR = 0.44   # card header height

def card(x, y, w, h, title, icon_name, hcolor, z=4):
    r = 0.09
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle=f'round,pad=0,rounding_size={r}',
        fc=hcolor, ec='none', lw=0, zorder=z))
    ax.add_patch(FancyBboxPatch((x, y), w, h-BAR,
        boxstyle=f'round,pad=0,rounding_size={r}',
        fc=WHITE, ec='none', lw=0, zorder=z+1))
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle=f'round,pad=0,rounding_size={r}',
        fc='none', ec=hcolor, lw=1.3, zorder=z+6))
    sz = BAR * 0.70
    place_icon(ax, icon_name, x+BAR*0.52, y+h-BAR/2, sz, WHITE, z=z+7)
    ax.text(x+BAR*0.96, y+h-BAR/2, title,
            ha='left', va='center', fontsize=10.5, fontweight='bold',
            color=WHITE, zorder=z+7)

def pbox(x, y, w, h, fc=LIGHT, ec=GRAY, lw=0.7, r=0.06, z=4, ls='solid'):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle=f'round,pad=0,rounding_size={r}',
        fc=fc, ec=ec, lw=lw, zorder=z, clip_on=False, linestyle=ls))

def txt(x, y, s, size=8.8, weight='normal', color=GRAY,
        ha='center', va='center', z=8, style='normal', mono=False):
    kw = dict(ha=ha, va=va, fontsize=size, fontweight=weight,
              color=color, zorder=z, fontstyle=style)
    if mono: kw['fontfamily'] = 'monospace'
    ax.text(x, y, s, **kw)

def hrule(x0, x1, y, lw=0.45, color=RULE, z=5):
    ax.plot([x0, x1], [y, y], color=color, lw=lw, zorder=z, solid_capstyle='butt')

def arrow(x0, x1, y0, y1=None, label=None, side='top',
          color=NAVY, lw=1.1, ms=9, z=10):
    if y1 is None: y1 = y0
    ax.annotate('', xy=(x1,y1), xytext=(x0,y0),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                mutation_scale=ms,
                                connectionstyle='arc3,rad=0'), zorder=z)
    if label:
        mx,my = (x0+x1)/2, (y0+y1)/2
        dy = 0.11 if side=='top' else -0.11
        va = 'bottom' if side=='top' else 'top'
        txt(mx, my+dy, label, size=7.2, color=DIM, style='italic', va=va, z=z)

def dblarrow(x0, x1, y, gap=0.08, color=NAVY, lw=1.0, ms=8,
             label_top=None, label_bot=None, z=10):
    """Double arrow: x0→x1 on top rail, x1→x0 on bottom rail.
    label_top sits above the top arrow; label_bot sits below the bottom arrow.
    """
    ax.annotate('', xy=(x1,y+gap), xytext=(x0,y+gap),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                mutation_scale=ms), zorder=z)
    ax.annotate('', xy=(x0,y-gap), xytext=(x1,y-gap),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                mutation_scale=ms), zorder=z)
    mx = (x0+x1)/2
    if label_top:
        txt(mx, y+gap+0.10, label_top, size=7.2, color=DIM,
            style='italic', va='bottom', z=z)
    if label_bot:
        txt(mx, y-gap-0.10, label_bot, size=7.2, color=DIM,
            style='italic', va='top', z=z)

def vdblarrow(x, y0, y1, gap=0.055, color=NAVY, lw=1.0, ms=8,
              label_left=None, label_right=None, z=10):
    """Vertical double arrow: y0→y1 on left rail, y1→y0 on right rail."""
    ax.annotate('', xy=(x-gap,y1), xytext=(x-gap,y0),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                mutation_scale=ms), zorder=z)
    ax.annotate('', xy=(x+gap,y0), xytext=(x+gap,y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                mutation_scale=ms), zorder=z)
    my = (y0+y1)/2
    if label_left:
        txt(x-gap-0.08, my, label_left, size=7.2, color=DIM,
            style='italic', ha='right', z=z)
    if label_right:
        txt(x+gap+0.08, my, label_right, size=7.2, color=DIM,
            style='italic', ha='left', z=z)


# ══════════════════════════════════════════════════════════════════════════════
# 1.  API Documentation block
# ══════════════════════════════════════════════════════════════════════════════
DW, DH = 1.92, 2.92
DX = PAD + 0.20
DY = MID - DH/2 - 0.06
DCX = DX + DW/2

pbox(DX, DY, DW, DH, fc=WHITE, ec=NAVY, lw=1.1, r=0.09, z=4)

HDR_Y = DY + DH - 0.34
# Hand-drawn document icon: clean at any scale, no SVG parsing
_ic_cx, _ic_cy, _ic_sz = DX+0.255, HDR_Y, 0.36
_iw, _ih = _ic_sz*0.62, _ic_sz*0.82
ax.add_patch(FancyBboxPatch((_ic_cx-_iw/2, _ic_cy-_ih/2), _iw, _ih,
    boxstyle='round,pad=0,rounding_size=0.014',
    fc='none', ec=NAVY, lw=1.2, zorder=8))
for _frac in [0.68, 0.47, 0.26]:
    _ly = _ic_cy - _ih/2 + _ih*_frac
    ax.add_patch(FancyBboxPatch((_ic_cx-_iw*0.34, _ly-_ih*0.04),
        _iw*0.68, _ih*0.08, boxstyle='square,pad=0',
        fc=NAVY, ec='none', lw=0, zorder=8))
txt(DCX+0.10, HDR_Y, 'API Documentation',
    size=10.5, weight='bold', color=NAVY, ha='center', z=8)
hrule(DX+0.14, DX+DW-0.14, HDR_Y-0.27)

COND = [
    ('docs',    'Full endpoint docs',   WHITE, NAVY,  True,  NAVY),
    ('no docs', 'Zero API context',     LIGHT, RULE,  False, GRAY),
    ('mutated', 'Renames params',        LIGHT, RULE,  False, GRAY),
]
RH, RG = 0.50, 0.09
block_h = 3*RH + 2*RG
BY = DY + (DH - 0.58 - block_h)/2 + 0.05

for ri, (tag, desc, fc, ec, bold, tc) in enumerate(COND):
    ry = BY + (2-ri)*(RH+RG)
    pbox(DX+0.12, ry, DW-0.24, RH, fc=fc, ec=ec, lw=0.55, r=0.05, z=6)
    ax.text(DX+0.26, ry+RH/2, tag,
            ha='left', va='center', fontsize=8.5,
            fontweight='bold' if bold else 'normal',
            color=tc, fontfamily='monospace', zorder=8)
    ax.text(DX+DW-0.17, ry+RH/2, desc,
            ha='right', va='center', fontsize=7.2, color=DIM, zorder=8)

txt(DCX, DY+0.17, '14 REST APIs  ·  high-impact domains',
    size=7.0, color=DIM, style='italic', z=6)


# ══════════════════════════════════════════════════════════════════════════════
# 2.  Tool-Maker LLM card  (INSTRUCTIONS.md is now an external artifact above)
# ══════════════════════════════════════════════════════════════════════════════
TW, TH = 1.96, 2.46
TX = DX + DW + 0.26
TY = MID - TH/2 - 0.06
TCX = TX + TW/2

card(TX, TY, TW, TH, 'Tool-Maker LLM', 'gear-wide-connected', AMBER, z=4)

# Body: what the LLM does
TBH = TH - BAR   # body height
T1 = TY + TBH*0.78
T2 = TY + TBH*0.56
T3 = TY + TBH*0.33
T4 = TY + TBH*0.13

txt(TCX, T1, 'generates MCP server code',   size=7.4, weight='bold', color=GRAY, z=7)
hrule(TX+0.18, TX+TW-0.18, T2+0.14)
txt(TCX, T2, 'via file-system tools',        size=7.2, color=DIM, z=7)
txt(TCX, T3, 'read · list · glob',           size=7.0, color=DIM, z=7, mono=True)
txt(TCX, T4, 'grep · write · edit',          size=7.0, color=DIM, z=7, mono=True)

# INSTRUCTIONS.md — external dashed artifact above Tool-Maker
INS_W, INS_H = 1.64, 0.65
INS_X = TCX - INS_W/2
INS_Y = TY + TH + 0.26           # bottom of INSTRUCTIONS box
pbox(INS_X, INS_Y, INS_W, INS_H,
     fc=WHITE, ec=DIM, lw=0.65, r=0.07, z=5, ls='dashed')
txt(TCX, INS_Y+INS_H*0.70, 'INSTRUCTIONS.md',
    size=8.2, weight='bold', color=GRAY, z=7, mono=True)
txt(TCX, INS_Y+INS_H*0.28, 'server spec  ·  key endpoints',
    size=7.0, color=DIM, z=7)

# Arrow: INSTRUCTIONS.md → Tool-Maker header (downward)
arrow(TCX, TCX, INS_Y-0.06, TY+TH+0.06, color=DIM, lw=0.9, ms=7, z=9)

# Arrow docs → Tool-Maker
arrow(DX+DW+0.02, TX-0.02, MID, color=NAVY, lw=1.1, ms=9, z=9)


# ══════════════════════════════════════════════════════════════════════════════
# 3.  MCP Server card
# ══════════════════════════════════════════════════════════════════════════════
EVAL_MID = MID - 0.16
MCX_L = SPLIT + 0.22
MCW, MCH = 1.76, 1.70
MCY   = EVAL_MID - MCH/2 + 0.30
MCCX  = MCX_L + MCW/2

arrow(TX+TW+0.02, MCX_L-0.02, MID, color=NAVY, lw=1.1, ms=9, z=9)

card(MCX_L, MCY, MCW, MCH, 'MCP Server', 'plug-fill', BLUE, z=4)

for si, (title, sub) in enumerate([('N tool functions', '@mcp.tool()'),
                                    ('API client',       'auth + HTTP')]):
    SH, SG = 0.46, 0.10
    sy = MCY + MCH - BAR - 0.13 - si*(SH+SG) - SH
    pbox(MCX_L+0.14, sy, MCW-0.28, SH, fc=LIGHT, ec=BLUE, lw=0.6, r=0.05, z=7)
    txt(MCCX, sy+SH*0.67, title, size=8.5, weight='bold', color=BLUE, z=8)
    txt(MCCX, sy+SH*0.27, sub,   size=7.2, color=DIM,    z=8, mono=True)


# ══════════════════════════════════════════════════════════════════════════════
# 4.  Agent LLM card  +  Test-task  +  Live API
# ══════════════════════════════════════════════════════════════════════════════
AX_L = MCX_L + MCW + 0.68
AW   = 1.76
ACX  = AX_L + AW/2
AH   = BAR + 0.72
ACY  = EVAL_MID + 0.70

card(AX_L, ACY-AH/2, AW, AH, 'Agent LLM', 'lightning-charge-fill', TEAL, z=4)
txt(ACX, ACY-AH/2+(AH-BAR)*0.66, 'uses MCP tool calls',         size=7.2, color=DIM, z=7)
txt(ACX, ACY-AH/2+(AH-BAR)*0.29, 'trajectory  \u2264 15 turns', size=7.2, color=DIM, z=7)

# Test-task — dashed artifact above Agent LLM (same height as INSTRUCTIONS.md)
TTW, TTH = 1.52, INS_H
TTX = ACX - TTW/2
TTY = INS_Y                        # top aligned with INSTRUCTIONS.md
pbox(TTX, TTY, TTW, TTH, fc=WHITE, ec=DIM, lw=0.65, r=0.07, z=5, ls='dashed')
txt(ACX, TTY+TTH*0.70, 'Test task',                size=8.5, weight='bold', color=GRAY, z=7)
txt(ACX, TTY+TTH*0.30, 'tasks.yaml  ·  M per API', size=7.0, color=DIM, z=7)
arrow(ACX, ACX, TTY-0.05, ACY+AH/2+0.06, color=NAVY, lw=1.0, ms=8, z=9)

# MCP ↔ Agent double arrow — label each direction separately
dblarrow(MCX_L+MCW+0.06, AX_L-0.06,
         ACY, gap=0.08, color=TEAL, lw=1.0, ms=8,
         label_top='results', label_bot='tool calls', z=10)

# Live API card below MCP
LAW = 1.44; LAH = BAR + 0.24
LAX = MCCX - LAW/2
LAY = MCY - 0.30 - LAH
card(LAX, LAY, LAW, LAH, 'Live API', 'cloud-check-fill', BLUE, z=4)
txt(MCCX, LAY+(LAH-BAR)/2, 'or sandbox when available', size=7.0, color=DIM, z=7)
vdblarrow(MCCX, LAY+LAH+0.06, MCY-0.06,
          gap=0.055, color=BLUE, lw=1.0, ms=8,
          label_left='HTTP resp', label_right='HTTP req', z=10)


# ══════════════════════════════════════════════════════════════════════════════
# 5.  Judge LLM card
# ══════════════════════════════════════════════════════════════════════════════
JH   = AH
JCY  = EVAL_MID - 0.82
JX_L = AX_L; JW = AW

arrow(ACX, ACX, ACY-AH/2-0.07, JCY+JH/2+0.07, color=NAVY, lw=1.0, ms=8, z=9)

card(JX_L, JCY-JH/2, JW, JH, 'Judge LLM', 'patch-check-fill', PURPLE, z=4)
txt(ACX+0.07, JCY-JH/2+(JH-BAR)*0.66, 'evaluates tool usage',  size=7.2, color=DIM, z=7)
txt(ACX+0.07, JCY-JH/2+(JH-BAR)*0.29, 'and task completion',   size=7.2, color=DIM, z=7)


# ══════════════════════════════════════════════════════════════════════════════
# 6.  Verdict panel
# ══════════════════════════════════════════════════════════════════════════════
VP_X  = AX_L + AW + 0.28
VP_W  = W - PAD - VP_X - 0.18
VP_H  = 4.10
VP_Y  = MID - VP_H/2

arrow(AX_L+AW+0.06, VP_X-0.06, JCY, color=PURPLE, lw=1.0, ms=8, z=9)

card(VP_X, VP_Y, VP_W, VP_H, 'Task Verdict', 'clipboard2-check-fill', PURPLE, z=4)

PI  = 0.14
VRX = VP_X + PI
VRW = VP_W - 2*PI
SG  = 0.10

VERTS = [
    ('PASS',  'agent completed task correctly', G_BG, G_EC, G_EC),
    ('FAIL',  'tool-side failure  (see cause)', R_BG, R_EC, R_EC),
    ('UNDEF', 'agent / env / task confound',    A_BG, A_EC, A_EC),
]
VRH = 0.36; VRG = 0.08
vr_top = VP_Y + VP_H - BAR - 0.13

for vi, (label, desc, fc, ec, tc) in enumerate(VERTS):
    vy = vr_top - vi*(VRH+VRG) - VRH
    pbox(VRX, vy, VRW, VRH, fc=fc, ec=ec, lw=0.65, r=0.05, z=6)
    ax.text(VRX+0.11, vy+VRH/2, label,
            ha='left', va='center', fontsize=8.2, fontweight='bold',
            color=tc, fontfamily='monospace', zorder=8)
    ax.text(VRX+VRW-0.10, vy+VRH/2, desc,
            ha='right', va='center', fontsize=7.2, color=DIM, zorder=8)

FC_TOP = vr_top - 3*(VRH+VRG)
hrule(VP_X+PI, VP_X+VP_W-PI, FC_TOP-SG*0.8)
txt(VP_X+VP_W/2, FC_TOP-SG*2.4,
    'Failure cause taxonomy', size=7.2, color=DIM, style='italic', z=6)

CAUSES = ['TOOL_COVERAGE', 'TOOL_SCHEMA', 'TOOL_IMPL.', 'TOOL_DOCS']
FCH=0.24; FCGX=0.07; FCGY=0.07
FCCW = (VRW-FCGX)/2
FC_BOT = FC_TOP - SG*3.8

for ci, cause in enumerate(CAUSES):
    col,row = ci%2, ci//2
    cx = VRX+col*(FCCW+FCGX)
    cy = FC_BOT-row*(FCH+FCGY)-FCH
    pbox(cx, cy, FCCW, FCH, fc=R_BG, ec=R_EC, lw=0.50, r=0.03, z=6)
    ax.text(cx+FCCW/2, cy+FCH/2, cause,
            ha='center', va='center', fontsize=6.8,
            color=R_EC, fontfamily='monospace', zorder=8)

SS_SEP = FC_BOT - 2*(FCH+FCGY)
hrule(VP_X+PI, VP_X+VP_W-PI, SS_SEP-SG*0.8)
txt(VP_X+VP_W/2, SS_SEP-SG*2.4,
    'Server quality  (indep. of agent)', size=7.2, color=DIM, style='italic', z=6)

SSH = 0.50
SSY = SS_SEP - SG*3.8 - SSH
pbox(VRX, SSY, VRW, SSH, fc=G_BG, ec=G_EC, lw=0.70, r=0.06, z=6)
txt(VP_X+VP_W/2, SSY+SSH*0.72,
    'SERVER_SUFFICIENT', size=8.5, weight='bold', color=G_EC, z=8, mono=True)
txt(VP_X+VP_W/2, SSY+SSH*0.44,
    'did the server provide a correct, usable tool?',
    size=6.8, color=DIM, z=8)
txt(VP_X+VP_W/2, SSY+SSH*0.18,
    'YES  /  NO  /  UNKNOWN', size=6.8, color=DIM, z=8)


# ── Save ──────────────────────────────────────────────────────────────────────
plt.tight_layout(pad=0)
for ext in ('png', 'pdf'):
    fname = f'benchmark_pipeline_thesis_v4.{ext}'
    dpi = 300 if ext == 'png' else None
    plt.savefig(fname, dpi=dpi, bbox_inches='tight', facecolor=WHITE)
    print(f'Saved {fname}')

# Transparent background version (PNG only)
plt.savefig('benchmark_pipeline_thesis_v4_transparent.png', dpi=300,
            bbox_inches='tight', facecolor='none', transparent=True)
print('Saved benchmark_pipeline_thesis_v4_transparent.png')
