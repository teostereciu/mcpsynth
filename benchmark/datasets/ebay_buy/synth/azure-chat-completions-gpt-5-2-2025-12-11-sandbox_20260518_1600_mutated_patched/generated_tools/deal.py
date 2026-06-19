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
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/deal/v1/event", params=params, headers=headers)


def get_event(
    client: EbayClient,
    *,
    event_id: str,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", f"/buy/deal/v1/event/{event_id}", headers=headers)


def get_deal_items(
    client: EbayClient,
    *,
    marketplace_id: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    category_list: Optional[str] = None,
    commissionable: Optional[bool] = None,
    delivery_country: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if category_list is not None:
        params["category_list"] = category_list
    if commissionable is not None:
        params["commissionable"] = str(commissionable).lower()
    if delivery_country is not None:
        params["delivery_country"] = delivery_country

    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/deal/v1/deal_item", params=params, headers=headers)


def get_event_items(
    client: EbayClient,
    *,
    marketplace_id: str,
    event_ids: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    category_list: Optional[str] = None,
    delivery_country: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"event_ids": event_ids}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if category_list is not None:
        params["category_list"] = category_list
    if delivery_country is not None:
        params["delivery_country"] = delivery_country

    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/deal/v1/event_item", params=params, headers=headers)
