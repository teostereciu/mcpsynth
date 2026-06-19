"""
compute_rp.py — Protocol Rigidity Score (R_p): composite of three sub-signals

R_p measures how precisely a synthesizer must follow the docs to produce a
correct server. Three orthogonal intrinsic signals, each targeting a distinct
failure mode observed in the residuals:

  1. idiosyncrasy (weight 0.50)
     Fraction of extracted param names NOT in the standard REST vocabulary.
     Captures: non-standard naming that the model can't guess from conventions.
     Failure mode: model uses `api_key` instead of `appid`, `max_results`
     instead of `maxResults`, etc.

  2. camelCase fraction (weight 0.30)
     Fraction of extracted param names in camelCase (vs snake_case).
     Captures: naming convention mismatch — the REST default is snake_case,
     so camelCase APIs (Jira's `maxResults`, eBay's `fieldgroups`) cause the
     model to generate the wrong convention without docs.
     Failure mode: model writes `max_results` when API requires `maxResults`.

  3. enum value density (weight 0.20)
     Total distinct enum values mentioned in docs / param count.
     Captures: APIs where exact value strings must be right, not just the
     param name (AlphaVantage `interval=TIME_SERIES_INTRADAY`, OWM
     `units=standard|metric|imperial`, eBay `fieldgroups=COMPACT|PRODUCT`).
     Failure mode: model guesses plausible but wrong enum values.

R_p = 0.50·norm(idiosyncrasy) + 0.30·norm(camelCase_fraction)
     + 0.20·norm(enum_density)

All weights are recorded in the output for transparency.

Outputs: pgi/rp_scores.json

Usage:
    python compute_rp.py [--datasets-root PATH] [--debug API]
"""

import argparse
import json
import re
from pathlib import Path

DATASETS_ROOT = Path(__file__).parents[2] / "datasets"

APIS = [
    "stripe", "github", "zulip", "notion", "confluence", "jira",
    "shopify", "mastodon", "openweathermap", "alphavantage",
    "spoonacular", "ebay_buy", "ebay_sell", "ebay_commerce",
]

# ---------------------------------------------------------------------------
# Standard REST parameter vocabulary
# Parameters a model is statistically certain to know from training data.
# Deliberately broad: false inclusions only shrink R_p, making the
# idiosyncrasy estimate conservative (biased against our hypothesis).
# ---------------------------------------------------------------------------
STANDARD_VOCAB: set[str] = {
    # Pagination
    "page", "per_page", "page_size", "limit", "offset", "cursor",
    "next_cursor", "page_token", "after", "before", "first", "last",
    "skip", "take", "start", "end", "max_results", "count",
    # Search / filtering / sorting
    "filter", "q", "query", "search", "sort", "order", "direction",
    "order_by", "sort_by", "fields", "expand", "include", "exclude",
    "select", "where",
    # Status / type / state
    "status", "type", "state", "kind", "category", "tag", "label",
    "labels", "tags", "flag", "active", "enabled", "public", "private",
    "visible", "archived",
    # Identity / reference
    "id", "name", "slug", "key", "token", "code", "ref", "sha",
    "hash", "uuid", "guid", "number", "index",
    # Timestamps
    "created_at", "updated_at", "start_date", "end_date", "since",
    "until", "date", "timestamp", "time", "from", "to",
    # Content / text
    "title", "body", "content", "text", "description", "message",
    "summary", "note", "notes", "comment", "subject",
    # User / ownership
    "user_id", "user", "email", "username", "owner", "author",
    "creator", "assignee", "repo", "repository", "organization",
    "org", "team", "member", "account",
    # Media / files
    "url", "path", "file", "image", "icon", "color", "size",
    "format", "encoding", "mime_type", "filename",
    # Auth
    "api_key", "access_token", "client_id", "client_secret",
    "scope", "grant_type", "redirect_uri", "refresh_token",
    # Numeric
    "amount", "price", "quantity", "weight", "width", "height",
    "total", "position", "rank", "score", "level", "version",
    # Misc common
    "language", "locale", "timezone", "currency", "country",
    "region", "city", "address", "phone", "website",
    "recursive", "force", "dry_run", "verbose", "debug",
    "callback", "webhook", "event",
}

# ---------------------------------------------------------------------------
# Extraction patterns (order matters — apply all, union the results)
# ---------------------------------------------------------------------------

# Pattern 1: Stripe/Notion attribute lines
# e.g. "- payment_methodnullablestring..." or "- idsstring..."
# Captures the snake_case/camelCase identifier before a type keyword
RE_ATTR_LINE = re.compile(
    r'^-\s+([a-zA-Z][a-zA-Z0-9_]*)(?:nullable|optional|required)?'
    r'(?:string|integer|int|boolean|bool|number|float|object|array|enum|hash)\b',
    re.MULTILINE
)

# Pattern 2: Markdown section headers used as param names
# e.g. "#### payment_methodnullablestring" or "#### per_pageinteger"
RE_HEADER_PARAM = re.compile(
    r'^#{2,4}\s+([a-zA-Z][a-zA-Z0-9_]*)(?:nullable|optional|required)?'
    r'(?:string|integer|int|boolean|bool|number|float|object|array|enum|hash)\b',
    re.MULTILINE
)

# Pattern 3: GitHub-style [TABLE] blocks with "Name, Type, Description" header
# Rows look like: "per_pageintegerThe number of results..."
# After splitting by [TABLE]/[/TABLE] we look for identifier-like first tokens
RE_TABLE_BLOCK = re.compile(r'\[TABLE\](.*?)\[/TABLE\]', re.DOTALL)
RE_TABLE_ROW_PARAM = re.compile(
    r'^([a-zA-Z][a-zA-Z0-9_]*)(?:string|integer|int|boolean|bool|number|float|object|array)\b',
    re.MULTILINE
)

# Pattern 4: Zulip/Jira bold-param tables
# e.g. "**narrow** | object | ..." or "**jql** | string | ..."
RE_BOLD_PARAM = re.compile(r'\*\*([a-zA-Z][a-zA-Z0-9_]*)\*\*\s*\|')

# Pattern 5: Jira/bold standalone param names followed by type on next line
# e.g. "**query**\nstring\n..."
RE_QUERY_PARAM_BOLD = re.compile(r'\*\*([a-zA-Z][a-zA-Z0-9_]*)\*\*\s*\n+(?:string|integer|boolean|number|array|object)\b')

# Pattern 6: Mastodon format — bare snake_case identifier alone on a line,
# followed by indented "required/optional Type." or plain "Type."
# e.g. "in_reply_to_id\n    String. ..."
RE_MASTODON_PARAM = re.compile(
    r'^([a-z][a-z0-9_\[\]]*)\n\s+(?:required\s+|optional\s+)?'
    r'(?:String|Integer|Boolean|Array|Hash|Number)',
    re.MULTILINE
)

# Pattern 7: OWM/simple pipe-table rows where first cell is a bare param name
# e.g. "lat | required | Latitude..."
# (distinct from GitHub [TABLE] blocks — these have no [TABLE] wrapper)
RE_PIPE_TABLE_PARAM = re.compile(
    r'^\s*([a-z][a-z0-9_]*)\s*\|\s*(?:required|optional)',
    re.MULTILINE
)

# Pattern 8: AlphaVantage — **❚ Required:`symbol`** or ❚ Optional: `outputsize`
RE_ALPHAVANTAGE_PARAM = re.compile(
    r'(?:Required|Optional)[:`\s]*[`]([a-zA-Z][a-zA-Z0-9_]*)[`]',
    re.IGNORECASE
)

# Pattern 9: Spoonacular / markdown tables with backtick-wrapped param names
# e.g. "`query`" or "**`query`**" in a table row
RE_BACKTICK_PARAM = re.compile(r'[`]([a-zA-Z][a-zA-Z0-9_]*)[`]\s*\|')

# Pattern 10: eBay-style prose references to parameters, where the scraper
# collapsed the HTML table so param names are embedded in run-on sentences.
# Two sub-patterns cover the observed formats:
#   (a) "the{paramName}parameter" / "the{paramName}filter" / "the{paramName}field"
#       e.g. "thefieldgroupsparameter", "theaspect_filterparameter"
#   (b) URI template params: {item_id}, {item_group_id}
#   (c) Custom HTTP headers: X-EBAY-C-MARKETPLACE-ID
RE_EBAY_PROSE_PARAM = re.compile(
    r'the([a-z][a-zA-Z0-9_]*)(?:parameter|filter|field|container|query|URI)\b'
)
RE_URI_TEMPLATE_PARAM = re.compile(r'\{([a-zA-Z][a-zA-Z0-9_]+)\}')
RE_CUSTOM_HEADER = re.compile(r'\b(X-[A-Z][A-Z0-9-]{3,})\b')

# ---------------------------------------------------------------------------
# Enum value extraction — counts total distinct enum values across all docs.
# Targets phrases like "Can be one of: open, closed, all" or
# "Possible enum values: company, individual, non_profit"
# ---------------------------------------------------------------------------
RE_ENUM_INTRO = re.compile(
    r'(?:Possible (?:enum )?values?|Can be one of|Must be (?:one of|either)|'
    r'Valid [Vv]alues?|Allowed [Vv]alues?|Supported [Vv]alues?|'
    r'one of the following)[:\s]+([^\n.]{4,200})',
    re.IGNORECASE
)
# AlphaVantage inline backtick-quoted values: "`1min`, `5min`, `15min`"
RE_BACKTICK_ENUM = re.compile(r'`([a-zA-Z0-9_]+)`(?:\s*,\s*`([a-zA-Z0-9_]+)`)+')


def extract_enum_values(text: str) -> set[str]:
    """Return distinct enum value strings found in a doc file."""
    values: set[str] = set()

    for m in RE_ENUM_INTRO.finditer(text):
        # Split on commas, pipes, or "or" to get individual values
        raw = m.group(1)
        tokens = re.split(r'[,|]|\bor\b', raw)
        for tok in tokens:
            tok = tok.strip().strip('`"\'').strip()
            # Keep only short tokens that look like identifier/enum values
            if 1 <= len(tok) <= 40 and re.match(r'^[a-zA-Z0-9_\-]+$', tok):
                values.add(tok.lower())

    for m in RE_BACKTICK_ENUM.finditer(text):
        for g in m.groups():
            if g:
                values.add(g.lower())

    return values


# ---------------------------------------------------------------------------
# camelCase detection
# ---------------------------------------------------------------------------
_RE_HAS_INTERNAL_UPPER = re.compile(r'^[a-z][a-z0-9]*[A-Z][a-zA-Z0-9]*$')

def is_camelcase(name: str) -> bool:
    """True if name is camelCase: starts lowercase, has internal uppercase, no underscores."""
    return (
        '_' not in name
        and not name.startswith('X-')   # exclude custom headers
        and bool(_RE_HAS_INTERNAL_UPPER.match(name))
    )


_PROSE_STOPWORDS = {
    "above", "below", "following", "previous", "current", "next",
    "first", "last", "only", "same", "other", "each", "this",
    "any", "all", "new", "full", "main", "item", "list", "value",
    "response", "request", "method", "result", "data", "info",
}
_HTTP_VERBS = {"get", "post", "put", "patch", "delete", "head", "options"}


def extract_params(text: str) -> list[str]:
    """Return parameter name candidates preserving original case."""
    names: set[str] = set()

    for m in RE_ATTR_LINE.finditer(text):
        names.add(m.group(1))

    for m in RE_HEADER_PARAM.finditer(text):
        names.add(m.group(1))

    for block_m in RE_TABLE_BLOCK.finditer(text):
        block = block_m.group(1)
        for m in RE_TABLE_ROW_PARAM.finditer(block):
            candidate = m.group(1)
            if candidate.lower() not in {"name", "type", "description"} and len(candidate) >= 2:
                names.add(candidate)

    for m in RE_BOLD_PARAM.finditer(text):
        names.add(m.group(1))

    for m in RE_QUERY_PARAM_BOLD.finditer(text):
        names.add(m.group(1))

    for m in RE_MASTODON_PARAM.finditer(text):
        name = m.group(1).rstrip("[]").rstrip("[")
        names.add(name)

    for m in RE_PIPE_TABLE_PARAM.finditer(text):
        names.add(m.group(1))

    for m in RE_ALPHAVANTAGE_PARAM.finditer(text):
        names.add(m.group(1))

    for m in RE_BACKTICK_PARAM.finditer(text):
        names.add(m.group(1))

    for m in RE_EBAY_PROSE_PARAM.finditer(text):
        name = m.group(1)
        if name.lower() not in _PROSE_STOPWORDS and len(name) >= 3:
            names.add(name)

    for m in RE_URI_TEMPLATE_PARAM.finditer(text):
        names.add(m.group(1))

    for m in RE_CUSTOM_HEADER.finditer(text):
        names.add(m.group(1))

    names = {
        n for n in names
        if len(n) >= 2 and n.lower() not in _HTTP_VERBS
    }
    return sorted(names)


def compute_api_rp(api: str, datasets_root: Path, debug: bool = False) -> dict:
    docs_dir = datasets_root / api / "docs"
    if not docs_dir.exists():
        return {"error": f"docs dir not found: {docs_dir}"}

    doc_files = [f for f in docs_dir.glob("*.md") if not f.name.startswith("_")]
    if not doc_files:
        return {"error": "no .md files found"}

    all_params_orig: set[str] = set()
    all_enum_vals: set[str] = set()
    for f in doc_files:
        text = f.read_text(errors="replace")
        all_params_orig.update(extract_params(text))
        all_enum_vals.update(extract_enum_values(text))

    # Deduplicate by lowercase (keep one casing per unique name)
    seen_lower: set[str] = set()
    params_deduped: list[str] = []
    for p in sorted(all_params_orig):
        if p.lower() not in seen_lower:
            seen_lower.add(p.lower())
            params_deduped.append(p)

    n = max(len(params_deduped), 1)

    # Sub-signal 1: idiosyncrasy
    non_std = [p for p in params_deduped if p.lower() not in STANDARD_VOCAB]
    std     = [p for p in params_deduped if p.lower() in STANDARD_VOCAB]
    idiosync = len(non_std) / n

    # Sub-signal 2: camelCase fraction
    camel = [p for p in params_deduped if is_camelcase(p)]
    camel_frac = len(camel) / n

    # Sub-signal 3: enum value density
    enum_density = len(all_enum_vals) / n

    if debug:
        print(f"\n  === {api} ===")
        print(f"  Total params: {n}  |  camelCase: {camel}  |  enum values: {sorted(all_enum_vals)[:30]}")
        print(f"  Standard: {[p for p in params_deduped if p.lower() in STANDARD_VOCAB]}")
        print(f"  Non-standard (first 20): {non_std[:20]}")

    return {
        "n_docs": len(doc_files),
        "n_params_extracted": n,
        "n_standard": len(std),
        "n_non_standard": len(non_std),
        "n_camelcase": len(camel),
        "n_enum_values": len(all_enum_vals),
        "idiosyncrasy": round(idiosync, 4),
        "camelcase_fraction": round(camel_frac, 4),
        "enum_density": round(enum_density, 4),
        "non_standard_params": non_std,
        "camelcase_params": camel,
    }


def normalize(values: dict[str, float]) -> dict[str, float]:
    lo, hi = min(values.values()), max(values.values())
    if hi == lo:
        return {k: 0.5 for k in values}
    return {k: (v - lo) / (hi - lo) for k, v in values.items()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--datasets-root", default=DATASETS_ROOT, type=Path)
    parser.add_argument("--out", default=Path(__file__).parent / "rp_scores.json")
    parser.add_argument("--debug", metavar="API",
                        help="Print extracted params for a specific API")
    args = parser.parse_args()

    raw: dict[str, dict] = {}
    for api in APIS:
        result = compute_api_rp(api, args.datasets_root, debug=(args.debug == api))
        raw[api] = result
        if "error" not in result:
            print(
                f"  {api:20s}  params={result['n_params_extracted']:4d}  "
                f"idiosync={result['idiosyncrasy']:.3f}  "
                f"camel={result['camelcase_fraction']:.3f}({result['n_camelcase']:2d})  "
                f"enum_dens={result['enum_density']:.2f}({result['n_enum_values']:3d} vals)"
            )
        else:
            print(f"  {api:20s}  ERROR: {result['error']}")

    valid = {k: v for k, v in raw.items() if "error" not in v}

    # Normalize each sub-signal independently
    idiosync_norm   = normalize({k: v["idiosyncrasy"]        for k, v in valid.items()})
    camel_norm      = normalize({k: v["camelcase_fraction"]   for k, v in valid.items()})
    enum_norm       = normalize({k: v["enum_density"]         for k, v in valid.items()})

    W_IDX, W_CAM, W_ENUM = 0.50, 0.30, 0.20

    rp_composite = {
        api: W_IDX * idiosync_norm[api]
           + W_CAM * camel_norm[api]
           + W_ENUM * enum_norm[api]
        for api in valid
    }
    rp_final = normalize(rp_composite)

    out = {
        "description": (
            "Protocol Rigidity Score (R_p) — composite of three sub-signals: "
            "idiosyncrasy (0.50), camelCase fraction (0.30), enum density (0.20). "
            "All sub-signals normalized to [0,1] before weighting; composite re-normalized."
        ),
        "weights": {"idiosyncrasy": W_IDX, "camelcase_fraction": W_CAM, "enum_density": W_ENUM},
        "standard_vocab_size": len(STANDARD_VOCAB),
        "raw": {k: {ek: ev for ek, ev in v.items()
                    if ek not in ("non_standard_params", "camelcase_params")}
                for k, v in raw.items()},
        "normalized_components": {
            "idiosync_norm":  {k: round(v, 4) for k, v in idiosync_norm.items()},
            "camel_norm":     {k: round(v, 4) for k, v in camel_norm.items()},
            "enum_norm":      {k: round(v, 4) for k, v in enum_norm.items()},
        },
        "rp_scores": {k: round(v, 4) for k, v in rp_final.items()},
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nWrote {out_path}")
    print("\nR_p scores (higher = more idiosyncratic = docs more critical):")
    for api, score in sorted(rp_final.items(), key=lambda x: -x[1]):
        bar = "█" * int(score * 30)
        print(f"  {api:20s} {score:.3f}  {bar}")


if __name__ == "__main__":
    main()
