"""Tools for eBay Buy Feed API.

Note: Successful feed responses are TSV_GZIP binary. These tools return metadata
and (optionally) raw bytes base64-encoded for small downloads.
"""

from __future__ import annotations

import base64
from typing import Any, Dict, Optional

import requests

from .http import EbayApiError, get_application_token, get_config, tool_safe_call


_FEED_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.item.feed"


def _request_feed(
    path: str,
    *,
    params: Dict[str, Any],
    marketplace_id: Optional[str] = None,
    environment: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    config = get_config(marketplace_id=marketplace_id, environment=environment)
    token = get_application_token(config, scope=_FEED_SCOPE)

    url = f"{config.base_url}{path}"
    headers = {
        "Authorization": f"Bearer {token}",
        "X-EBAY-C-MARKETPLACE-ID": config.marketplace_id,
    }
    if range_header:
        headers["Range"] = range_header

    resp = requests.get(url, headers=headers, params=params, timeout=60)
    if resp.status_code >= 400:
        try:
            err = resp.json()
        except Exception:
            err = {"message": resp.text}
        raise EbayApiError(f"eBay Feed API error {resp.status_code} for GET {path}") from EbayApiError(str(err))

    content_type = resp.headers.get("Content-Type", "")
    result: Dict[str, Any] = {
        "status_code": resp.status_code,
        "content_type": content_type,
        "content_length": resp.headers.get("Content-Length"),
        "content_range": resp.headers.get("Content-Range"),
        "etag": resp.headers.get("ETag"),
        "last_modified": resp.headers.get("Last-Modified"),
    }

    # If response is JSON (error), parse it.
    if "application/json" in content_type:
        result["json"] = resp.json()
        return result

    # For small responses, include bytes as base64.
    if resp.headers.get("Content-Length") and int(resp.headers["Content-Length"]) <= 2_000_000:
        result["data_base64"] = base64.b64encode(resp.content).decode("ascii")
        result["data_bytes"] = len(resp.content)
    else:
        result["note"] = "Binary feed too large to inline; use Range header to download in chunks."

    return result


def feed_get_item_feed(
    *,
    feed_scope: str,
    category_id: str,
    date: str,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    """Download an item feed file.

    Wraps: GET /buy/feed/v1/item

    Args:
      feed_scope: NEWLY_LISTED (daily) or ALL_ACTIVE (weekly bootstrap)
      category_id: leaf category
      date: yyyyMMdd (daily) or yyyyMMdd (bootstrap week start per docs)
      range_header: optional HTTP Range header, e.g. "bytes=0-999999"

    Returns metadata and optionally base64 bytes.
    """

    params = {"feed_scope": feed_scope, "category_id": category_id, "date": date}
    return tool_safe_call(_request_feed, "/buy/feed/v1/item", params=params, marketplace_id=marketplace_id, range_header=range_header)


def feed_get_item_snapshot_feed(
    *,
    snapshot_date: str,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    """Download an item snapshot feed.

    Wraps: GET /buy/feed/v1/item_snapshot
    """

    params = {"snapshot_date": snapshot_date}
    return tool_safe_call(
        _request_feed,
        "/buy/feed/v1/item_snapshot",
        params=params,
        marketplace_id=marketplace_id,
        range_header=range_header,
    )


def feed_get_item_group_feed(
    *,
    feed_scope: str,
    category_id: str,
    date: str,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    """Download an item group feed.

    Wraps: GET /buy/feed/v1/item_group
    """

    params = {"feed_scope": feed_scope, "category_id": category_id, "date": date}
    return tool_safe_call(
        _request_feed,
        "/buy/feed/v1/item_group",
        params=params,
        marketplace_id=marketplace_id,
        range_header=range_header,
    )


def feed_get_item_priority_feed(
    *,
    category_id: str,
    date: str,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    """Download an item priority feed.

    Wraps: GET /buy/feed/v1/item_priority
    """

    params = {"category_id": category_id, "date": date}
    return tool_safe_call(
        _request_feed,
        "/buy/feed/v1/item_priority",
        params=params,
        marketplace_id=marketplace_id,
        range_header=range_header,
    )
