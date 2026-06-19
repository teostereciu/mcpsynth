from typing import Any, Dict, Optional

from .browse import _get


def get_deal_items(limit: int = 10, offset: int = 0, **kwargs):
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    params.update(kwargs)
    return _get("/buy/deal/v1/deal_item", params)


def get_event(event_id: str):
    return _get(f"/buy/deal/v1/event/{event_id}")


def get_events(limit: int = 10, offset: int = 0, **kwargs):
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    params.update(kwargs)
    return _get("/buy/deal/v1/event", params)


def get_event_items(event_id: str, limit: int = 10, offset: int = 0, **kwargs):
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    params.update(kwargs)
    return _get(f"/buy/deal/v1/event/{event_id}/item", params)
