from typing import Any, Dict, Optional

from .client import EbayBuyApiClient


FEED_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_item_snapshot_feed(
    client: EbayBuyApiClient,
    *,
    feed_scope: str,
    marketplace_id: str,
    date: Optional[str] = None,
    category_id: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"feed_scope": feed_scope, "marketplace_id": marketplace_id}
    if date is not None:
        params["date"] = date
    if category_id is not None:
        params["category_id"] = category_id
    return client.request("GET", "/buy/feed/v1/item_snapshot_feed", scope=FEED_SCOPE, params=params)


def get_item_snapshot_feed_file(client: EbayBuyApiClient, *, file_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/feed/v1/item_snapshot_feed/{file_id}", scope=FEED_SCOPE)


def get_item_feed(
    client: EbayBuyApiClient,
    *,
    feed_type: str,
    marketplace_id: str,
    date: Optional[str] = None,
    category_id: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"feed_type": feed_type, "marketplace_id": marketplace_id}
    if date is not None:
        params["date"] = date
    if category_id is not None:
        params["category_id"] = category_id
    return client.request("GET", "/buy/feed/v1/item_feed", scope=FEED_SCOPE, params=params)


def get_item_feed_file(client: EbayBuyApiClient, *, file_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/feed/v1/item_feed/{file_id}", scope=FEED_SCOPE)
