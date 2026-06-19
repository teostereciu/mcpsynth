from typing import Any, Dict, Optional

from generated_tools.auth import client


def get_deals(limit: int = 10, offset: int = 0, category_ids: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if category_ids:
        params["category_ids"] = category_ids
    return client.request("GET", "/buy/deal/v1/deal", params=params)


def get_deal_items(deal_id: str, limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    return client.request("GET", f"/buy/deal/v1/deal/{deal_id}", params={"limit": limit, "offset": offset})


def get_deal_events(limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    return client.request("GET", "/buy/deal/v1/deal_item", params={"limit": limit, "offset": offset})


def get_deal_event(event_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/deal/v1/event/{event_id}")
