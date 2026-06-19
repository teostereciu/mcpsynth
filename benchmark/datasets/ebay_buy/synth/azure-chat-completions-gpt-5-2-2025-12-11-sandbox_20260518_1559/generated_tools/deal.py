from typing import Any, Dict, Optional

from .client import EbayClient


def get_events(
    client: EbayClient,
    *,
    marketplace_id: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/deal/v1/event"""
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    return client.request("GET", "/buy/deal/v1/event", params=params, headers=headers)


def get_event(
    client: EbayClient,
    *,
    marketplace_id: str,
    event_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/deal/v1/event/{event_id}"""
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", f"/buy/deal/v1/event/{event_id}", headers=headers)


def get_deal_items(
    client: EbayClient,
    *,
    marketplace_id: str,
    category_ids: Optional[str] = None,
    commissionable: Optional[bool] = None,
    delivery_country: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/deal/v1/deal_item"""
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    params: Dict[str, Any] = {}
    if category_ids is not None:
        params["category_ids"] = category_ids
    if commissionable is not None:
        params["commissionable"] = str(commissionable).lower()
    if delivery_country is not None:
        params["delivery_country"] = delivery_country
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    return client.request("GET", "/buy/deal/v1/deal_item", params=params, headers=headers)


def get_event_items(
    client: EbayClient,
    *,
    marketplace_id: str,
    event_ids: str,
    category_ids: Optional[str] = None,
    delivery_country: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/deal/v1/event_item"""
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    params: Dict[str, Any] = {"event_ids": event_ids}
    if category_ids is not None:
        params["category_ids"] = category_ids
    if delivery_country is not None:
        params["delivery_country"] = delivery_country
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    return client.request("GET", "/buy/deal/v1/event_item", params=params, headers=headers)
