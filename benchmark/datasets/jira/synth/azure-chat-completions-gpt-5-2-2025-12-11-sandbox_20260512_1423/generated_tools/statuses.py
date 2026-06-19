from typing import Any, Dict, List, Optional

from ._client import get_client


def get_statuses_by_ids(ids: List[str]) -> Any:
    """GET /statuses?id=..."""
    return get_client().request("GET", "/statuses", params={"id": ids})


def get_statuses_by_names(names: List[str], project_id: Optional[str] = None) -> Any:
    """GET /statuses/byNames"""
    params: Dict[str, Any] = {"name": names}
    if project_id is not None:
        params["projectId"] = project_id
    return get_client().request("GET", "/statuses/byNames", params=params)


def search_statuses(project_id: Optional[str] = None, start_at: int = 0, max_results: int = 50,
                    search_string: Optional[str] = None, status_category: Optional[str] = None) -> Any:
    """GET /statuses/search"""
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if project_id is not None:
        params["projectId"] = project_id
    if search_string is not None:
        params["searchString"] = search_string
    if status_category is not None:
        params["statusCategory"] = status_category
    return get_client().request("GET", "/statuses/search", params=params)
