#!/usr/bin/env python3
"""
gen_api_overview.py

Generates a 2×7 card-grid figure showing all 14 benchmark APIs with logos,
domain colour strips, documentation file counts, task counts, and familiarity
badges.

Output: api_overview.pdf + api_overview.png (300 dpi)
"""

import io
import warnings
import requests
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from pathlib import Path
from PIL import Image

warnings.filterwarnings("ignore")

mpl.rcParams.update({
    "font.family":      "sans-serif",
    "font.sans-serif":  ["Helvetica Neue", "Arial", "DejaVu Sans"],
    "pdf.fonttype":     42,
    "ps.fonttype":      42,
    "figure.facecolor": "white",
})

# Serif font used selectively for figure-level titles/labels
SERIF = ["CMU Serif", "Computer Modern", "Palatino", "Georgia", "DejaVu Serif"]

# ── Paths ──────────────────────────────────────────────────────────────────────

LOGO_DIR = Path("/Users/tstereciu/Documents/agent-tooling/benchmark/logos")

# ── Data ───────────────────────────────────────────────────────────────────────
# (key, display_name, domain, doc_files, n_tasks, familiarity, endpoints)
# Ordered by domain. Familiarity = degree of LLM pre-training representation:
#   high   — major platforms with extensive Python library ecosystems
#   medium — used in tutorials / integrations but less pervasive
#   low    — niche / specialised APIs with limited pre-training coverage
# Endpoint counts are approximate (extraction method varies across APIs).

APIS = [
    # Developer Tooling
    ("github",         "GitHub",          "Developer\nTooling",   180, 23, "high",   341),
    ("jira",           "Jira",            "Developer\nTooling",   100, 16, "high",   601),
    # Productivity
    ("notion",         "Notion",          "Productivity",          93, 22, "high",    93),
    ("confluence",     "Confluence",      "Productivity",          47, 21, "high",   212),
    # E-commerce
    ("ebay_buy",       "eBay Buy",        "E-commerce",            28, 17, "medium",  23),
    ("ebay_commerce",  "eBay Commerce",   "E-commerce",            47, 13, "medium",  41),
    ("ebay_sell",      "eBay Sell",       "E-commerce",           190, 14, "medium", 190),
    ("shopify",        "Shopify",         "E-commerce",            57, 18, "high",   247),
    # Communication
    ("mastodon",       "Mastodon",        "Communication",         35, 15, "medium", 145),
    ("zulip",          "Zulip",           "Communication",        164, 25, "medium", 240),
    # Data & Finance
    ("stripe",         "Stripe",          "Data &\nFinance",      120, 22, "high",   152),
    ("alphavantage",   "AlphaVantage",    "Data &\nFinance",        9, 19, "low",    122),
    ("spoonacular",    "Spoonacular",     "Data &\nFinance",        7, 17, "medium", 140),
    ("openweathermap", "OpenWeatherMap",  "Data &\nFinance",        4, 23, "medium",   8),
]

DOMAIN_COLORS = {
    "Developer\nTooling":  "#1B2E5E",
    "Productivity":        "#059669",
    "E-commerce":          "#D97706",
    "Communication":       "#7C3AED",
    "Data &\nFinance":     "#DC2626",
}

# (text colour, background colour) for familiarity badge
FAMILIARITY_STYLE = {
    "high":   ("#14532D", "#DCFCE7"),
    "medium": ("#78350F", "#FEF3C7"),
    "low":    ("#7F1D1D", "#FEE2E2"),
}

# Clearbit logo API for the four APIs that have no local SVG
CLEARBIT = {
    "alphavantage":   "alphavantage.co",
    "confluence":     "confluence.atlassian.com",
    "mastodon":       "mastodon.social",
    "spoonacular":    "spoonacular.com",
}

MAX_DOCS = 190  # normalisation anchor for the doc-files progress bar

# ── Logo loading ───────────────────────────────────────────────────────────────

def _svg_to_array(path: Path, size: int = 96) -> np.ndarray | None:
    try:
        import cairosvg
        png = cairosvg.svg2png(url=str(path), output_width=size, output_height=size)
        img = Image.open(io.BytesIO(png)).convert("RGBA")
        return np.array(img)
    except Exception as e:
        print(f"  cairosvg failed for {path}: {e}")
        return None


def _url_to_array(url: str, size: int = 96) -> np.ndarray | None:
    try:
        r = requests.get(url, timeout=8)
        if r.status_code == 200:
            img = Image.open(io.BytesIO(r.content)).convert("RGBA")
            img = img.resize((size, size), Image.LANCZOS)
            return np.array(img)
    except Exception as e:
        print(f"  download failed for {url}: {e}")
    return None


def _raster_to_array(path: Path, size: int = 96) -> np.ndarray | None:
    """Load any PIL-supported raster format (webp, png, jpg …) → RGBA array."""
    try:
        img = Image.open(path).convert("RGBA").resize((size, size), Image.LANCZOS)
        return np.array(img)
    except Exception as e:
        print(f"  PIL failed for {path}: {e}")
        return None


def load_logo(key: str, size: int = 96) -> np.ndarray | None:
    """Return RGBA logo array, or None to trigger the initials fallback.

    Priority: webp → svg (via cairosvg) → Clearbit (network) → None
    eBay sub-APIs use ebay.webp.
    """
    logo_key = "ebay" if key.startswith("ebay") else key

    # 1. webp (preferred — no external dependency beyond PIL)
    webp_path = LOGO_DIR / f"{logo_key}.webp"
    if webp_path.exists():
        arr = _raster_to_array(webp_path, size)
        if arr is not None:
            return arr

    # 2. svg via cairosvg
    svg_path = LOGO_DIR / f"{logo_key}.svg"
    if svg_path.exists():
        arr = _svg_to_array(svg_path, size)
        if arr is not None:
            return arr

    # 3. Clearbit fallback (requires network)
    if key in CLEARBIT:
        url = f"https://logo.clearbit.com/{CLEARBIT[key]}?size={size}"
        print(f"  fetching {url}")
        arr = _url_to_array(url, size)
        if arr is not None:
            return arr

    return None


# ── Logo normalisation ─────────────────────────────────────────────────────────

def _autocrop(img: Image.Image) -> Image.Image:
    """Crop transparent padding from an RGBA image."""
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    return img


def normalize_logo(img_array: np.ndarray,
                   max_w: int = 140, max_h: int = 64) -> np.ndarray:
    """Fit logo into max_w×max_h transparent canvas preserving aspect ratio.
    Wide canvas (140×64) lets landscape logos like OWM use their natural width.
    """
    img = _autocrop(Image.fromarray(img_array).convert("RGBA"))
    img.thumbnail((max_w, max_h), Image.LANCZOS)
    canvas = Image.new("RGBA", (max_w, max_h), (255, 255, 255, 0))
    offset = ((max_w - img.width) // 2, (max_h - img.height) // 2)
    canvas.paste(img, offset, mask=img)
    return np.array(canvas)


# ── Card drawing ───────────────────────────────────────────────────────────────

def draw_card(ax, key, name, domain, doc_files, n_tasks, endpoints):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    dc = DOMAIN_COLORS[domain]   # domain accent colour

    # ── 1. Card body ──
    ax.add_patch(FancyBboxPatch(
        (0.04, 0.03), 0.92, 0.94,
        boxstyle="round,pad=0.04",
        facecolor="white", edgecolor="#D1D5DB", linewidth=0.6,
        transform=ax.transAxes, zorder=1,
    ))

    # ── 2. Header strip — rounded top, squared bottom ──
    ax.add_patch(FancyBboxPatch(
        (0.04, 0.79), 0.92, 0.18,
        boxstyle="round,pad=0.04",
        facecolor=dc, edgecolor="none",
        transform=ax.transAxes, zorder=2,
    ))
    ax.add_patch(mpatches.Rectangle(
        (0.04, 0.79), 0.92, 0.07,
        facecolor=dc, edgecolor="none",
        transform=ax.transAxes, zorder=2,
    ))

    # ── 3. Logo ──
    logo_raw = load_logo(key)
    if logo_raw is not None:
        max_w = 160 if key == "openweathermap" else 140
        logo_norm = normalize_logo(logo_raw, max_w=max_w)
        imagebox = OffsetImage(logo_norm, zoom=0.48)
        ab = AnnotationBbox(
            imagebox, (0.5, 0.525),
            xycoords="axes fraction",
            frameon=False, zorder=3,
        )
        ax.add_artist(ab)
    else:
        circle = mpatches.Circle(
            (0.5, 0.525), 0.11,
            color=dc, transform=ax.transAxes, zorder=3,
        )
        ax.add_patch(circle)
        ax.text(
            0.5, 0.525, name[0].upper(),
            ha="center", va="center",
            transform=ax.transAxes,
            fontsize=12, fontweight="bold", color="white", zorder=4,
        )

    # ── 4. API name ──
    ax.text(
        0.5, 0.330, name,
        ha="center", va="center",
        transform=ax.transAxes,
        fontsize=6.6, fontweight="bold", color="#1F2937",
        multialignment="center", zorder=3,
    )

    # ── 5. Stats (two compact rows, no divider) ──
    stats = [
        (f"≈{endpoints}", "endpoints"),
        (f"{n_tasks}",    "tasks"),
    ]
    for idx, (val, label) in enumerate(stats):
        y = 0.205 - idx * 0.090
        ax.text(0.40, y, val,
                ha="right", va="center",
                transform=ax.transAxes,
                fontsize=5.8, fontweight="bold", color="#374151", zorder=3)
        ax.text(0.44, y, label,
                ha="left", va="center",
                transform=ax.transAxes,
                fontsize=5.2, color="#9CA3AF", zorder=3)


# ── Figure assembly ────────────────────────────────────────────────────────────

NROWS, NCOLS = 2, 7

fig = plt.figure(figsize=(14.5, 4.4))
gs = gridspec.GridSpec(
    NROWS, NCOLS, figure=fig,
    hspace=0.14, wspace=0.10,
    left=0.005, right=0.995,
    top=0.87, bottom=0.03,
)

print("Drawing cards...")
for i, (key, name, domain, docs, tasks, _fam, endpoints) in enumerate(APIS):
    row, col = divmod(i, NCOLS)
    ax = fig.add_subplot(gs[row, col])
    print(f"  {name} ...", end=" ", flush=True)
    draw_card(ax, key, name, domain, docs, tasks, endpoints)
    print("ok")

# ── Legend: domains ──
legend_handles = [
    mpatches.Patch(facecolor=c, label=d.replace("\n", " "))
    for d, c in DOMAIN_COLORS.items()
]
leg = fig.legend(
    handles=legend_handles,
    loc="upper center", ncol=5,
    fontsize=7, frameon=False,
    bbox_to_anchor=(0.5, 0.97),
    title="Domain",
    title_fontsize=8,
    handlelength=1.2, handleheight=0.9,
)
leg.get_title().set_fontfamily(SERIF)
leg.get_title().set_fontweight("bold")


out_pdf = Path("api_overview.pdf")
out_png = Path("api_overview.png")
fig.savefig(out_pdf, bbox_inches="tight")
fig.savefig(out_png, dpi=300, bbox_inches="tight")
print(f"\nSaved {out_pdf} and {out_png}")
