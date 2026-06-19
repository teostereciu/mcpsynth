from typing import Any, Dict, Optional

from .common import client


def get_item_feed(
    category_id: str,
    date: Optional[str] = None,
    feed_scope: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Range": range_header,
    }
    return client.request(
        "GET",
        "/buy/feed/v1/item",
        params={"category_id": category_id, "date": date, "feed_scope": feed_scope},
        headers=headers,
    )


def get_item_group_feed(
    category_id: str,
    feed_scope: str,
    date: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Range": range_header,
    }
    return client.request(
        "GET",
        "/buy/feed/v1_beta/item_group",
        params={"category_id": category_id, "feed_scope": feed_scope, "date": date},
        headers=headers,
    )


def get_item_priority_feed(
    category_id: str,
    date: str,
    marketplace_id: str,
    range_header: str,
) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/buy/feed/v1_beta/item_priority",
        params={"category_id": category_id, "date": date},
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Range": range_header},
    )


def get_item_snapshot_feed(
    category_id: str,
    snapshot_date: str,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Range": range_header,
    }
    return client.request(
        "GET",
        "/buy/feed/v1/item_snapshot",
        params={"category_id": category_id, "snapshot_date": snapshot_date},
        headers=headers,
    )
