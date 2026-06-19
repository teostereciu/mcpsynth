from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def get_statuses(ids: List[str]):
    """GET /statuses"""
    client = JiraClient()
    return client.request("GET", "/statuses", params={"id": ids})


def get_statuses_by_names(names: List[str], projectId: Optional[str] = None):
    """GET /statuses/byNames"""
    client = JiraClient()
    params: Dict[str, Any] = {"name": names}
    if projectId is not None:
        params["projectId"] = projectId
    return client.request("GET", "/statuses/byNames", params=params)


def search_statuses(projectId: Optional[str] = None, start_index: int = 0, page_size: int = 50, searchString: Optional[str] = None, statusCategory: Optional[str] = None):
    """GET /statuses/search"""
    client = JiraClient()
    params: Dict[str, Any] = {"startAt": start_index, "maxResults": page_size}
    if projectId is not None:
        params["projectId"] = projectId
    if searchString is not None:
        params["searchString"] = searchString
    if statusCategory is not None:
        params["statusCategory"] = statusCategory
    return client.request("GET", "/statuses/search", params=params)
