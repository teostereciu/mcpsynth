from typing import Any, Dict

from .browse import _get


def get_item_feed(limit: int = 10, offset: int = 0, **kwargs):
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    params.update(kwargs)
    return _get("/buy/feed/v1/item_feed", params)


def get_item_group_feed(limit: int = 10, offset: int = 0, **kwargs):
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    params.update(kwargs)
    return _get("/buy/feed/v1/item_group_feed", params)


def get_item_priority_feed(limit: int = 10, offset: int = 0, **kwargs):
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    params.update(kwargs)
    return _get("/buy/feed/v1/item_priority_feed", params)


def get_item_snapshot_feed(limit: int = 10, offset: int = 0, **kwargs):
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    params.update(kwargs)
    return _get("/buy/feed/v1/item_snapshot_feed", params)
