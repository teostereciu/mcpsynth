from typing import Any, Dict, Optional

from .common import client


def get_events(max_results: Optional[int] = None, skip: Optional[int] = None, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id} if marketplace_id else None
    return client.request(
        "GET",
        "/buy/deal/v1/event",
        params={"max_results": max_results, "skip": skip},
        headers=headers,
    )


def get_deal_items(
    category_ids: Optional[str] = None,
    commissionable: Optional[bool] = None,
    delivery_country: Optional[str] = None,
    max_results: Optional[int] = None,
    skip: Optional[int] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id} if marketplace_id else None
    return client.request(
        "GET",
        "/buy/deal/v1/deal_item",
        params={
            "category_ids": category_ids,
            "commissionable": str(commissionable).lower() if commissionable is not None else None,
            "delivery_country": delivery_country,
            "max_results": max_results,
            "skip": skip,
        },
        headers=headers,
    )


def get_event(event_id: str, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id} if marketplace_id else None
    return client.request("GET", f"/buy/deal/v1/event/{event_id}", headers=headers)


def get_event_items(
    event_ids: str,
    category_ids: Optional[str] = None,
    delivery_country: Optional[str] = None,
    max_results: Optional[int] = None,
    skip: Optional[int] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id} if marketplace_id else None
    return client.request(
        "GET",
        "/buy/deal/v1/event_item",
        params={
            "event_ids": event_ids,
            "category_ids": category_ids,
            "delivery_country": delivery_country,
            "max_results": max_results,
            "skip": skip,
        },
        headers=headers,
    )
