from __future__ import annotations

from typing import Any, Dict, Optional

from .client import EbayClient


_DEAL_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.deal"


def get_events(
    client: EbayClient,
    *,
    max_results: Optional[int] = None,
    skip: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if max_results is not None:
        params["limit"] = max_results
    if skip is not None:
        params["offset"] = skip

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/deal/v1/event", params=params, headers=headers, scope=_DEAL_SCOPE)


def get_event(
    client: EbayClient,
    *,
    event_id: str,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", f"/buy/deal/v1/event/{event_id}", headers=headers, scope=_DEAL_SCOPE)


def get_deal_items(
    client: EbayClient,
    *,
    max_results: Optional[int] = None,
    skip: Optional[int] = None,
    category_ids: Optional[str] = None,
    commissionable: Optional[bool] = None,
    delivery_country: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if max_results is not None:
        params["limit"] = max_results
    if skip is not None:
        params["offset"] = skip
    if category_ids is not None:
        params["category_ids"] = category_ids
    if commissionable is not None:
        params["commissionable"] = str(commissionable).lower()
    if delivery_country is not None:
        params["delivery_country"] = delivery_country

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/deal/v1/deal_item", params=params, headers=headers, scope=_DEAL_SCOPE)


def get_event_items(
    client: EbayClient,
    *,
    event_ids: str,
    max_results: Optional[int] = None,
    skip: Optional[int] = None,
    category_ids: Optional[str] = None,
    delivery_country: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"event_ids": event_ids}
    if max_results is not None:
        params["limit"] = max_results
    if skip is not None:
        params["offset"] = skip
    if category_ids is not None:
        params["category_ids"] = category_ids
    if delivery_country is not None:
        params["delivery_country"] = delivery_country

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/deal/v1/event_item", params=params, headers=headers, scope=_DEAL_SCOPE)
