from typing import Any, Dict, Optional

from .client import EbayBuyApiClient


DEAL_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_deals(
    client: EbayBuyApiClient,
    *,
    marketplace_id: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"marketplace_id": marketplace_id}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if category_ids is not None:
        params["category_ids"] = category_ids
    if filter is not None:
        params["filter"] = filter
    if sort is not None:
        params["sort"] = sort
    return client.request("GET", "/buy/deal/v1/deal_item", scope=DEAL_SCOPE, params=params)


def get_deal_item(client: EbayBuyApiClient, *, deal_id: str, marketplace_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/buy/deal/v1/deal_item/{deal_id}",
        scope=DEAL_SCOPE,
        params={"marketplace_id": marketplace_id},
    )


def get_deal_events(client: EbayBuyApiClient, *, marketplace_id: str, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"marketplace_id": marketplace_id}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return client.request("GET", "/buy/deal/v1/deal_event", scope=DEAL_SCOPE, params=params)


def get_deal_event(client: EbayBuyApiClient, *, event_id: str, marketplace_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/buy/deal/v1/deal_event/{event_id}",
        scope=DEAL_SCOPE,
        params={"marketplace_id": marketplace_id},
    )
