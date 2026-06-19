from typing import Any, Dict, Optional

from .http_client import EbayClient


client = EbayClient()


def deal_get_events(
    *,
    marketplace_id: str,
    limit: Optional[int] = 20,
    offset: Optional[int] = 0,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = int(limit)
    if offset is not None:
        params["offset"] = int(offset)

    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/deal/v1/event", params=params, headers=headers)


def deal_get_event(
    event_id: str,
    *,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request("GET", f"/buy/deal/v1/event/{event_id}", headers=headers)


def deal_get_deal_items(
    *,
    marketplace_id: str,
    limit: Optional[int] = 20,
    offset: Optional[int] = 0,
    filter: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = int(limit)
    if offset is not None:
        params["offset"] = int(offset)
    if filter is not None:
        params["filter"] = filter

    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/deal/v1/deal_item", params=params, headers=headers)


def deal_get_event_items(
    *,
    marketplace_id: str,
    limit: Optional[int] = 20,
    offset: Optional[int] = 0,
    filter: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = int(limit)
    if offset is not None:
        params["offset"] = int(offset)
    if filter is not None:
        params["filter"] = filter

    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/deal/v1/event_item", params=params, headers=headers)
