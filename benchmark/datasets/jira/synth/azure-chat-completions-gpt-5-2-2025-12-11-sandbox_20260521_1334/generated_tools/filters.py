from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def create_filter(name: str, jql: str, description: Optional[str] = None,
                  share_permissions: Optional[List[Dict[str, Any]]] = None,
                  edit_permissions: Optional[List[Dict[str, Any]]] = None,
                  favourite: Optional[bool] = None,
                  expand: Optional[str] = None,
                  override_share_permissions: Optional[bool] = None) -> Any:
    """POST /filter"""
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if override_share_permissions is not None:
        params["overrideSharePermissions"] = str(override_share_permissions).lower()

    body: Dict[str, Any] = {"name": name, "jql": jql}
    if description is not None:
        body["description"] = description
    if share_permissions is not None:
        body["sharePermissions"] = share_permissions
    if edit_permissions is not None:
        body["editPermissions"] = edit_permissions
    if favourite is not None:
        body["favourite"] = favourite

    return JiraClient().request("POST", "/filter", params=params or None, json_body=body)


def get_filter(filter_id: str, expand: Optional[str] = None) -> Any:
    """GET /filter/{id}"""
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return JiraClient().request("GET", f"/filter/{filter_id}", params=params or None)


def update_filter(filter_id: str, payload: Dict[str, Any], expand: Optional[str] = None) -> Any:
    """PUT /filter/{id}"""
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return JiraClient().request("PUT", f"/filter/{filter_id}", params=params or None, json_body=payload)


def delete_filter(filter_id: str) -> Any:
    """DELETE /filter/{id}"""
    return JiraClient().request("DELETE", f"/filter/{filter_id}")


def get_favorite_filters(expand: Optional[str] = None) -> Any:
    """GET /filter/favourite"""
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return JiraClient().request("GET", "/filter/favourite", params=params or None)


def get_my_filters(expand: Optional[str] = None, include_favourites: Optional[bool] = None) -> Any:
    """GET /filter/my"""
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if include_favourites is not None:
        params["includeFavourites"] = str(include_favourites).lower()
    return JiraClient().request("GET", "/filter/my", params=params or None)


def search_filters(start_at: int = 0, max_results: int = 50, filter_name: Optional[str] = None,
                   account_id: Optional[str] = None, owner: Optional[str] = None,
                   groupname: Optional[str] = None, group_id: Optional[str] = None,
                   project_id: Optional[int] = None, ids: Optional[List[int]] = None,
                   order_by: Optional[str] = None) -> Any:
    """GET /filter/search"""
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if filter_name is not None:
        params["filterName"] = filter_name
    if account_id is not None:
        params["accountId"] = account_id
    if owner is not None:
        params["owner"] = owner
    if groupname is not None:
        params["groupname"] = groupname
    if group_id is not None:
        params["groupId"] = group_id
    if project_id is not None:
        params["projectId"] = project_id
    if ids is not None:
        params["id"] = ids
    if order_by is not None:
        params["orderBy"] = order_by
    return JiraClient().request("GET", "/filter/search", params=params)


def get_filter_columns(filter_id: str) -> Any:
    """GET /filter/{id}/columns"""
    return JiraClient().request("GET", f"/filter/{filter_id}/columns")


def set_filter_columns(filter_id: str, columns: List[str]) -> Any:
    """PUT /filter/{id}/columns"""
    return JiraClient().request("PUT", f"/filter/{filter_id}/columns", json_body=columns)


def reset_filter_columns(filter_id: str) -> Any:
    """DELETE /filter/{id}/columns"""
    return JiraClient().request("DELETE", f"/filter/{filter_id}/columns")


def set_filter_favourite(filter_id: str) -> Any:
    """PUT /filter/{id}/favourite"""
    return JiraClient().request("PUT", f"/filter/{filter_id}/favourite")


def remove_filter_favourite(filter_id: str) -> Any:
    """DELETE /filter/{id}/favourite"""
    return JiraClient().request("DELETE", f"/filter/{filter_id}/favourite")
