from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def get_item_feed(
    client: EbayClient,
    feed_type: str,
    *,
    date: Optional[str] = None,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if date is not None:
        params["date"] = date
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", f"/buy/feed/v1/item_feed", params={**params, "feed_type": feed_type}, headers=headers)


def get_item_snapshot_feed(
    client: EbayClient,
    snapshot_id: str,
    *,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", f"/buy/feed/v1/item_snapshot/{snapshot_id}", headers=headers)


def get_item_snapshot_status(
    client: EbayClient,
    snapshot_id: str,
    *,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", f"/buy/feed/v1/item_snapshot/{snapshot_id}/status", headers=headers)


def get_item_snapshot_download(
    client: EbayClient,
    snapshot_id: str,
    *,
    range_header: Optional[str] = None,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    if range_header:
        headers["Range"] = range_header
    return client.request("GET", f"/buy/feed/v1/item_snapshot/{snapshot_id}/download", headers=headers)
