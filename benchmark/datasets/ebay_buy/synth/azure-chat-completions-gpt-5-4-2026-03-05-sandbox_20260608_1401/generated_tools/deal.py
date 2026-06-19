from typing import Any, Dict, Optional

from generated_tools.common import client


def get_events(limit: Optional[int] = None, offset: Optional[int] = None, marketplace_id: Optional[str] = None, enduserctx: Optional[str] = None) -> Dict[str, Any]:
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request("GET", "/buy/deal/v1/event", params={"limit": limit, "offset": offset}, headers=headers or None)


def get_event(event_id: str, marketplace_id: str, enduserctx: Optional[str] = None) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request("GET", f"/buy/deal/v1/event/{event_id}", headers=headers)


def get_event_items(
    event_ids: str,
    category_ids: Optional[str] = None,
    delivery_country: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request(
        "GET",
        "/buy/deal/v1/event_item",
        params={
            "event_ids": event_ids,
            "category_ids": category_ids,
            "delivery_country": delivery_country,
            "limit": limit,
            "offset": offset,
        },
        headers=headers,
    )


def get_deal_items(
    category_ids: Optional[str] = None,
    commissionable: Optional[bool] = None,
    delivery_country: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request(
        "GET",
        "/buy/deal/v1/deal_item",
        params={
            "category_ids": category_ids,
            "commissionable": str(commissionable).lower() if commissionable is not None else None,
            "delivery_country": delivery_country,
            "limit": limit,
            "offset": offset,
        },
        headers=headers,
    )
