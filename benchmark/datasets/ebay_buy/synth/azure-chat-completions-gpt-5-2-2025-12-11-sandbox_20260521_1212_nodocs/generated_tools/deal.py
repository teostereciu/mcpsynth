from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def get_deals(
    client: EbayClient,
    *,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
    filter: Optional[str] = None,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if sort is not None:
        params["sort"] = sort
    if filter is not None:
        params["filter"] = filter
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", "/buy/deal/v1/deal_item", params=params, headers=headers)


def get_deal(
    client: EbayClient,
    deal_id: str,
    *,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", f"/buy/deal/v1/deal_item/{deal_id}", headers=headers)


def get_events(
    client: EbayClient,
    *,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", "/buy/deal/v1/event", params=params, headers=headers)


def get_event(
    client: EbayClient,
    event_id: str,
    *,
    x_ebay_c_marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": x_ebay_c_marketplace_id}
    return client.request("GET", f"/buy/deal/v1/event/{event_id}", headers=headers)
