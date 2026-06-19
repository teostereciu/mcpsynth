from typing import Any, Dict, Optional

from .client import EbayClient


def deal_get_events(
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
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/deal/v1/event", params=params, headers=headers)


def deal_get_event(
    client: EbayClient,
    event_id: str,
    *,
    marketplace_id: str,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", f"/buy/deal/v1/event/{event_id}", headers=headers)


def deal_get_event_items(
    client: EbayClient,
    event_id: str,
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
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", f"/buy/deal/v1/event/{event_id}/item", params=params, headers=headers)


def deal_get_deal_items(
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
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/deal/v1/deal_item", params=params, headers=headers)
