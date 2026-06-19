from typing import Any, Dict, List, Optional

from ._client import JiraClient


def create_filter(
    client: JiraClient,
    filter_obj: Dict[str, Any],
    *,
    expand: Optional[str] = None,
    override_share_permissions: Optional[bool] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if override_share_permissions is not None:
        params["overrideSharePermissions"] = str(override_share_permissions).lower()
    return client.request("POST", "/filter", params=params or None, json=filter_obj)


def get_filter(client: JiraClient, filter_id: str, *, expand: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/filter/{filter_id}", params=params or None)


def update_filter(client: JiraClient, filter_id: str, filter_obj: Dict[str, Any]) -> Any:
    return client.request("PUT", f"/filter/{filter_id}", json=filter_obj)


def delete_filter(client: JiraClient, filter_id: str) -> Any:
    return client.request("DELETE", f"/filter/{filter_id}")


def search_filters(
    client: JiraClient,
    *,
    filter_name: Optional[str] = None,
    account_id: Optional[str] = None,
    owner: Optional[str] = None,
    group_name: Optional[str] = None,
    group_id: Optional[str] = None,
    project_id: Optional[int] = None,
    ids: Optional[List[int]] = None,
    order_by: Optional[str] = None,
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if filter_name is not None:
        params["filterName"] = filter_name
    if account_id is not None:
        params["accountId"] = account_id
    if owner is not None:
        params["owner"] = owner
    if group_name is not None:
        params["groupname"] = group_name
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


def get_my_filters(client: JiraClient, *, expand: Optional[str] = None, include_favourites: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if include_favourites is not None:
        params["includeFavourites"] = str(include_favourites).lower()
    return client.request("GET", "/filter/my", params=params or None)


def get_favourite_filters(client: JiraClient, *, expand: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", "/filter/favourite", params=params or None)


def get_filter_columns(client: JiraClient, filter_id: str) -> Any:
    return client.request("GET", f"/filter/{filter_id}/columns")


def set_filter_columns(client: JiraClient, filter_id: str, columns: List[str]) -> Any:
    return client.request("PUT", f"/filter/{filter_id}/columns", json=columns)


def reset_filter_columns(client: JiraClient, filter_id: str) -> Any:
    return client.request("DELETE", f"/filter/{filter_id}/columns")


def set_filter_favourite(client: JiraClient, filter_id: str) -> Any:
    return client.request("PUT", f"/filter/{filter_id}/favourite")


def remove_filter_favourite(client: JiraClient, filter_id: str) -> Any:
    return client.request("DELETE", f"/filter/{filter_id}/favourite")
