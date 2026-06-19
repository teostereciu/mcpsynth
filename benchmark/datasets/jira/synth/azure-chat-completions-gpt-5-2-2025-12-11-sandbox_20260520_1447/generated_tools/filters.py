from typing import Any, Dict, List, Optional, Union

from .http_client import JiraClient


def create_filter(filter_obj: Dict[str, Any], expand: Optional[str] = None, override_share_permissions: Optional[bool] = None) -> Union[Dict[str, Any], list, str]:
    """POST /filter"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if override_share_permissions is not None:
        params["overrideSharePermissions"] = str(override_share_permissions).lower()
    return client.request("POST", "/filter", params=params or None, json=filter_obj)


def get_favourite_filters(expand: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """GET /filter/favourite"""
    client = JiraClient()
    params = {"expand": expand} if expand is not None else None
    return client.request("GET", "/filter/favourite", params=params)


def get_my_filters(expand: Optional[str] = None, include_favourites: Optional[bool] = None) -> Union[Dict[str, Any], list, str]:
    """GET /filter/my"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if include_favourites is not None:
        params["includeFavourites"] = str(include_favourites).lower()
    return client.request("GET", "/filter/my", params=params or None)


def search_filters(filter_name: Optional[str] = None, account_id: Optional[str] = None, owner: Optional[str] = None, groupname: Optional[str] = None, group_id: Optional[str] = None, project_id: Optional[int] = None, ids: Optional[List[int]] = None, order_by: Optional[str] = None, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Union[Dict[str, Any], list, str]:
    """GET /filter/search"""
    client = JiraClient()
    params: Dict[str, Any] = {}
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
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    return client.request("GET", "/filter/search", params=params or None)


def get_filter(filter_id: str, expand: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """GET /filter/{id}"""
    client = JiraClient()
    params = {"expand": expand} if expand is not None else None
    return client.request("GET", f"/filter/{filter_id}", params=params)


def update_filter(filter_id: str, filter_obj: Dict[str, Any], expand: Optional[str] = None, override_share_permissions: Optional[bool] = None) -> Union[Dict[str, Any], list, str]:
    """PUT /filter/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if override_share_permissions is not None:
        params["overrideSharePermissions"] = str(override_share_permissions).lower()
    return client.request("PUT", f"/filter/{filter_id}", params=params or None, json=filter_obj)


def delete_filter(filter_id: str) -> Union[Dict[str, Any], list, str]:
    """DELETE /filter/{id}"""
    client = JiraClient()
    return client.request("DELETE", f"/filter/{filter_id}")


def get_filter_columns(filter_id: str) -> Union[Dict[str, Any], list, str]:
    """GET /filter/{id}/columns"""
    client = JiraClient()
    return client.request("GET", f"/filter/{filter_id}/columns")


def set_filter_columns(filter_id: str, columns: List[str]) -> Union[Dict[str, Any], list, str]:
    """PUT /filter/{id}/columns"""
    client = JiraClient()
    return client.request("PUT", f"/filter/{filter_id}/columns", json=columns)


def reset_filter_columns(filter_id: str) -> Union[Dict[str, Any], list, str]:
    """DELETE /filter/{id}/columns"""
    client = JiraClient()
    return client.request("DELETE", f"/filter/{filter_id}/columns")


def favourite_filter(filter_id: str) -> Union[Dict[str, Any], list, str]:
    """PUT /filter/{id}/favourite"""
    client = JiraClient()
    return client.request("PUT", f"/filter/{filter_id}/favourite")


def unfavourite_filter(filter_id: str) -> Union[Dict[str, Any], list, str]:
    """DELETE /filter/{id}/favourite"""
    client = JiraClient()
    return client.request("DELETE", f"/filter/{filter_id}/favourite")
