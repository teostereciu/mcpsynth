from typing import Any, Dict, Optional

from generated_tools.auth import client


def get_item_feed(date: str, feed_scope: str = "NEWLY_LISTED", category_id: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"date": date, "feed_scope": feed_scope}
    if category_id:
        params["category_id"] = category_id
    return client.request("GET", "/buy/feed/v1/item", params=params)


def get_item_snapshot(feed_scope: str = "ALL_ACTIVE", limit: int = 100, offset: int = 0, category_id: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"feed_scope": feed_scope, "limit": limit, "offset": offset}
    if category_id:
        params["category_id"] = category_id
    return client.request("GET", "/buy/feed/v1/item_snapshot", params=params)


def get_item_snapshot_file(task_id: str, file_name: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/feed/v1/item_snapshot/{task_id}/{file_name}")
