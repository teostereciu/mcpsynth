from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def create_filter(name: str, jql_query: str, description: Optional[str] = None, sharePermissions: Optional[List[Dict[str, Any]]] = None, editPermissions: Optional[List[Dict[str, Any]]] = None, favourite: Optional[bool] = None, expand: Optional[str] = None, overrideSharePermissions: Optional[bool] = None):
    """POST /filter"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if overrideSharePermissions is not None:
        params["overrideSharePermissions"] = str(overrideSharePermissions).lower()
    body: Dict[str, Any] = {"name": name, "jql": jql_query}
    if description is not None:
        body["description"] = description
    if sharePermissions is not None:
        body["sharePermissions"] = sharePermissions
    if editPermissions is not None:
        body["editPermissions"] = editPermissions
    if favourite is not None:
        body["favourite"] = favourite
    return client.request("POST", "/filter", params=params or None, json=body)


def get_filter(id: str, expand: Optional[str] = None):
    """GET /filter/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/filter/{id}", params=params or None)


def update_filter(id: str, payload: Dict[str, Any], expand: Optional[str] = None, overrideSharePermissions: Optional[bool] = None):
    """PUT /filter/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if overrideSharePermissions is not None:
        params["overrideSharePermissions"] = str(overrideSharePermissions).lower()
    return client.request("PUT", f"/filter/{id}", params=params or None, json=payload)


def delete_filter(id: str):
    """DELETE /filter/{id}"""
    client = JiraClient()
    return client.request("DELETE", f"/filter/{id}")


def my_filters(includeFavourites: bool = False, expand: Optional[str] = None):
    """GET /filter/my"""
    client = JiraClient()
    params: Dict[str, Any] = {"includeFavourites": str(includeFavourites).lower()}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", "/filter/my", params=params)


def favourite_filters(expand: Optional[str] = None):
    """GET /filter/favourite"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", "/filter/favourite", params=params or None)


def search_filters(start_index: int = 0, page_size: int = 50, filterName: Optional[str] = None, owner: Optional[str] = None, user_id: Optional[str] = None, groupname: Optional[str] = None, groupId: Optional[str] = None, projectId: Optional[int] = None, ids: Optional[List[int]] = None, orderBy: Optional[str] = None):
    """GET /filter/search"""
    client = JiraClient()
    params: Dict[str, Any] = {"startAt": start_index, "maxResults": page_size}
    if filterName is not None:
        params["filterName"] = filterName
    if owner is not None:
        params["owner"] = owner
    if user_id is not None:
        params["accountId"] = user_id
    if groupname is not None:
        params["groupname"] = groupname
    if groupId is not None:
        params["groupId"] = groupId
    if projectId is not None:
        params["projectId"] = projectId
    if ids is not None:
        params["id"] = ids
    if orderBy is not None:
        params["orderBy"] = orderBy
    return client.request("GET", "/filter/search", params=params)
