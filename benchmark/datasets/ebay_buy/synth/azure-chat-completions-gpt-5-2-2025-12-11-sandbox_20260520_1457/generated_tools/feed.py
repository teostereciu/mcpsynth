from typing import Any, Dict, Optional

from .client import EbayClient


def feed_get_item_feed(
    client: EbayClient,
    *,
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"feed_scope": feed_scope, "category_id": category_id}
    if date is not None:
        params["date"] = date

    headers: Dict[str, str] = {}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if range_header is not None:
        headers["Range"] = range_header

    # Successful response is TSV_GZIP binary; client will return text if not JSON.
    return client.request("GET", "/buy/feed/v1/item", params=params, headers=headers)


def feed_get_item_group_feed(
    client: EbayClient,
    *,
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"feed_scope": feed_scope, "category_id": category_id}
    if date is not None:
        params["date"] = date

    headers: Dict[str, str] = {}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if range_header is not None:
        headers["Range"] = range_header

    return client.request("GET", "/buy/feed/v1/item_group", params=params, headers=headers)


def feed_get_item_priority_feed(
    client: EbayClient,
    *,
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"feed_scope": feed_scope, "category_id": category_id}
    if date is not None:
        params["date"] = date

    headers: Dict[str, str] = {}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if range_header is not None:
        headers["Range"] = range_header

    return client.request("GET", "/buy/feed/v1/item_priority", params=params, headers=headers)


def feed_get_item_snapshot_feed(
    client: EbayClient,
    *,
    snapshot_date: str,
    marketplace_id: str,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"snapshot_date": snapshot_date}

    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if range_header is not None:
        headers["Range"] = range_header

    return client.request("GET", "/buy/feed/v1/item_snapshot", params=params, headers=headers)


def feed_get_item_group_feed_beta(
    client: EbayClient,
    *,
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    # Some docs include item_group feed under /buy/feed/v1/item_group and also beta namespace.
    params: Dict[str, Any] = {"feed_scope": feed_scope, "category_id": category_id}
    if date is not None:
        params["date"] = date

    headers: Dict[str, str] = {}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if range_header is not None:
        headers["Range"] = range_header

    return client.request("GET", "/buy/feed/v1/item_group", params=params, headers=headers)
