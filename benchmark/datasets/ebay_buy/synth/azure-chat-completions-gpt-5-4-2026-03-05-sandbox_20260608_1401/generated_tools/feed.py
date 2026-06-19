from typing import Any, Dict, Optional

from generated_tools.common import client


def get_item_feed(
    category_id: str,
    feed_scope: str,
    date: str,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if range_header:
        headers["Range"] = range_header
    return client.request(
        "GET",
        "/buy/feed/v1/item",
        params={"category_id": category_id, "feed_scope": feed_scope, "date": date},
        headers=headers or None,
    )


def get_item_snapshot_feed(
    category_id: str,
    snapshot_date: str,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if range_header:
        headers["Range"] = range_header
    return client.request(
        "GET",
        "/buy/feed/v1/item_snapshot",
        params={"category_id": category_id, "snapshot_date": snapshot_date},
        headers=headers or None,
    )


def get_item_priority_feed(category_id: str, date: str, marketplace_id: str, range_header: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/buy/feed/v1_beta/item_priority",
        params={"category_id": category_id, "date": date},
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Range": range_header},
    )


def get_item_group_feed(
    feed_scope: str,
    category_id: str,
    marketplace_id: str,
    date: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if range_header:
        headers["Range"] = range_header
    return client.request(
        "GET",
        "/buy/feed/v1_beta/item_group",
        params={"feed_scope": feed_scope, "category_id": category_id, "date": date},
        headers=headers,
    )
