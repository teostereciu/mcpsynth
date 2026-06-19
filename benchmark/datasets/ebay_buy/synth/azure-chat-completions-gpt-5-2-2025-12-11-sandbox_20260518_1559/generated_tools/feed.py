from typing import Any, Dict, Optional

from .client import EbayClient


def get_item_feed(
    client: EbayClient,
    *,
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/feed/v1_beta/item

    Note: Successful response is a TSV_GZIP binary. This tool returns JSON for errors,
    or a dict with a download URL and request details for clients to fetch.
    """
    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if range_header:
        headers["Range"] = range_header

    params: Dict[str, Any] = {"feed_scope": feed_scope, "category_id": category_id}
    if date is not None:
        params["date"] = date

    # We can't stream binary over MCP reliably; return the URL and let caller download.
    return {
        "download": {
            "method": "GET",
            "url": f"{client.base_url}/buy/feed/v1_beta/item",
            "params": params,
            "headers": headers,
            "note": "This endpoint returns a TSV_GZIP binary. Use the provided URL/params/headers to download.",
        }
    }


def get_item_snapshot_feed(
    client: EbayClient,
    *,
    category_id: str,
    snapshot_date: str,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/feed/v1_beta/item_snapshot

    Returns a TSV_GZIP binary; this tool returns download instructions.
    """
    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if range_header:
        headers["Range"] = range_header

    params: Dict[str, Any] = {"category_id": category_id, "snapshot_date": snapshot_date}

    return {
        "download": {
            "method": "GET",
            "url": f"{client.base_url}/buy/feed/v1_beta/item_snapshot",
            "params": params,
            "headers": headers,
            "note": "This endpoint returns a TSV_GZIP binary. Use the provided URL/params/headers to download.",
        }
    }


def get_item_priority_feed(
    client: EbayClient,
    *,
    category_id: str,
    date: str,
    marketplace_id: str,
    range_header: str,
) -> Dict[str, Any]:
    """GET /buy/feed/v1_beta/item_priority

    Returns a TSV_GZIP binary; this tool returns download instructions.
    """
    headers: Dict[str, str] = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Range": range_header,
        "Accept": "application/json,text/tab-separated-values",
    }

    params: Dict[str, Any] = {"category_id": category_id, "date": date}

    return {
        "download": {
            "method": "GET",
            "url": f"{client.base_url}/buy/feed/v1_beta/item_priority",
            "params": params,
            "headers": headers,
            "note": "This endpoint returns a TSV_GZIP binary. Use the provided URL/params/headers to download.",
        }
    }


def get_item_group_feed(
    client: EbayClient,
    *,
    feed_scope: str,
    category_id: str,
    marketplace_id: str,
    range_header: Optional[str] = None,
    date: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/feed/v1_beta/item_group

    Returns a TSV_GZIP binary; this tool returns download instructions.
    """
    headers: Dict[str, str] = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Accept": "application/json,text/tab-separated-values",
    }
    if range_header:
        headers["Range"] = range_header

    params: Dict[str, Any] = {"feed_scope": feed_scope, "category_id": category_id}
    if date is not None:
        params["date"] = date

    return {
        "download": {
            "method": "GET",
            "url": f"{client.base_url}/buy/feed/v1_beta/item_group",
            "params": params,
            "headers": headers,
            "note": "This endpoint returns a TSV_GZIP binary. Use the provided URL/params/headers to download.",
        }
    }
