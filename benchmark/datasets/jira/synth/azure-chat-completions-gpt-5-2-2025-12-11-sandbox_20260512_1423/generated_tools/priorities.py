from typing import Any, Dict, List, Optional

from ._client import get_client


def get_priorities() -> Any:
    """GET /priority"""
    return get_client().request("GET", "/priority")


def get_priority(priority_id: str) -> Any:
    """GET /priority/{id}"""
    return get_client().request("GET", f"/priority/{priority_id}")


def search_priorities(start_at: int = 0, max_results: int = 50, ids: Optional[List[str]] = None,
                      project_ids: Optional[List[str]] = None, priority_name: Optional[str] = None,
                      only_default: Optional[bool] = None, expand: Optional[str] = None) -> Any:
    """GET /priority/search"""
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if ids:
        params["id"] = ids
    if project_ids:
        params["projectId"] = project_ids
    if priority_name is not None:
        params["priorityName"] = priority_name
    if only_default is not None:
        params["onlyDefault"] = str(bool(only_default)).lower()
    if expand is not None:
        params["expand"] = expand
    return get_client().request("GET", "/priority/search", params=params)
