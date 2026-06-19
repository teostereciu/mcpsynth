"""Tools for eBay Buy Feed API.

Note: Successful responses are TSV_GZIP binary files. These tools return metadata
and/or a small JSON error payload if the API returns JSON.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

import requests

from .http import EbayApiError, get_application_token, get_base_url, request_json


FEED_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.item.feed"


def _download_url(path: str) -> str:
    return f"{get_base_url()}{path}"


def get_item_feed(
    *,
    category_id: str,
    feed_scope: str = "NEWLY_LISTED",
    date: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    """Download an item feed file (TSV_GZIP).

    Wraps: GET /buy/feed/v1/item?category_id=...&feed_scope=...&date=...

    Returns JSON with download metadata. If range_header is provided, downloads a
    chunk and returns base64-encoded bytes.
    """

    params: Dict[str, Any] = {"category_id": category_id, "feed_scope": feed_scope}
    if date:
        params["date"] = date

    token = get_application_token(scope=FEED_SCOPE)
    headers = {
        "Authorization": f"Bearer {token}",
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
    }
    if range_header:
        headers["Range"] = range_header

    url = _download_url("/buy/feed/v1/item")

    resp = requests.get(url, headers=headers, params=params, timeout=60)

    # Errors are JSON
    ctype = resp.headers.get("Content-Type", "")
    if resp.status_code >= 400:
        try:
            return {"error": f"HTTP {resp.status_code}", "details": resp.json()}
        except Exception:
            return {"error": f"HTTP {resp.status_code}", "details": resp.text}

    if "application/json" in ctype:
        return resp.json()

    # Binary
    out: Dict[str, Any] = {
        "status": resp.status_code,
        "content_type": ctype,
        "content_length": resp.headers.get("Content-Length"),
        "content_range": resp.headers.get("Content-Range"),
        "accept_ranges": resp.headers.get("Accept-Ranges"),
        "download_url": str(resp.url),
    }

    if range_header:
        import base64

        out["chunk_base64"] = base64.b64encode(resp.content).decode("ascii")

    return out


def get_item_group_feed(
    *,
    category_id: str,
    feed_scope: str = "NEWLY_LISTED",
    date: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get item group feed metadata.

    Wraps: GET /buy/feed/v1/item_group
    """

    params: Dict[str, Any] = {"category_id": category_id, "feed_scope": feed_scope}
    if date:
        params["date"] = date

    return request_json(
        "GET",
        "/buy/feed/v1/item_group",
        params=params,
        marketplace_id=marketplace_id,
        scope=FEED_SCOPE,
    )


def get_item_snapshot_feed(
    *,
    feed_type: str,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get snapshot feed metadata.

    Wraps: GET /buy/feed/v1/item_snapshot?feed_type=...
    """

    params = {"feed_type": feed_type}
    return request_json(
        "GET",
        "/buy/feed/v1/item_snapshot",
        params=params,
        marketplace_id=marketplace_id,
        scope=FEED_SCOPE,
    )


def get_item_priority_feed(
    *,
    feed_type: str,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get priority feed metadata.

    Wraps: GET /buy/feed/v1/item_priority?feed_type=...
    """

    params = {"feed_type": feed_type}
    return request_json(
        "GET",
        "/buy/feed/v1/item_priority",
        params=params,
        marketplace_id=marketplace_id,
        scope=FEED_SCOPE,
    )
