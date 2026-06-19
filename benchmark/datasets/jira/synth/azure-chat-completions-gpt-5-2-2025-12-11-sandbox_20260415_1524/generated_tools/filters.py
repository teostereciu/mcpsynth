from typing import Any, Dict, List, Optional

from .jira_client import JiraClient, clean_params


def filter_create(name: str, jql: str, description: Optional[str] = None, expand: Optional[str] = None, override_share_permissions: Optional[bool] = None, share_permissions: Optional[List[Dict[str, Any]]] = None, edit_permissions: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """POST /filter - Create filter."""
    client = JiraClient()
    params = clean_params({"expand": expand, "overrideSharePermissions": override_share_permissions})
    body: Dict[str, Any] = {"name": name, "jql": jql}
    if description is not None:
        body["description"] = description
    if share_permissions is not None:
        body["sharePermissions"] = share_permissions
    if edit_permissions is not None:
        body["editPermissions"] = edit_permissions
    return client.request("POST", "/filter", params=params, json_body=body)  # type: ignore[return-value]


def filter_get(filter_id: str, expand: Optional[str] = None) -> Dict[str, Any]:
    """GET /filter/{id} - Get filter."""
    client = JiraClient()
    params = clean_params({"expand": expand})
    return client.request("GET", f"/filter/{filter_id}", params=params)  # type: ignore[return-value]


def filter_update(filter_id: str, payload: Dict[str, Any], expand: Optional[str] = None, override_share_permissions: Optional[bool] = None) -> Dict[str, Any]:
    """PUT /filter/{id} - Update filter."""
    client = JiraClient()
    params = clean_params({"expand": expand, "overrideSharePermissions": override_share_permissions})
    return client.request("PUT", f"/filter/{filter_id}", params=params, json_body=payload)  # type: ignore[return-value]


def filter_delete(filter_id: str) -> Dict[str, Any]:
    """DELETE /filter/{id} - Delete filter."""
    client = JiraClient()
    return client.request("DELETE", f"/filter/{filter_id}")  # type: ignore[return-value]


def filters_favourite(expand: Optional[str] = None) -> Any:
    """GET /filter/favourite - Get favorite filters."""
    client = JiraClient()
    params = clean_params({"expand": expand})
    return client.request("GET", "/filter/favourite", params=params)


def filters_my(expand: Optional[str] = None, include_favourites: Optional[bool] = None) -> Any:
    """GET /filter/my - Get my filters."""
    client = JiraClient()
    params = clean_params({"expand": expand, "includeFavourites": include_favourites})
    return client.request("GET", "/filter/my", params=params)


def filters_search(
    filter_name: Optional[str] = None,
    account_id: Optional[str] = None,
    owner: Optional[str] = None,
    groupname: Optional[str] = None,
    group_id: Optional[str] = None,
    project_id: Optional[int] = None,
    ids: Optional[List[int]] = None,
    order_by: Optional[str] = None,
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /filter/search - Search for filters."""
    client = JiraClient()
    params = clean_params(
        {
            "filterName": filter_name,
            "accountId": account_id,
            "owner": owner,
            "groupname": groupname,
            "groupId": group_id,
            "projectId": project_id,
            "id": ids,
            "orderBy": order_by,
            "startAt": start_at,
            "maxResults": max_results,
        }
    )
    return client.request("GET", "/filter/search", params=params)  # type: ignore[return-value]


def filter_favourite_set(filter_id: str) -> Dict[str, Any]:
    """PUT /filter/{id}/favourite - Set filter as favourite."""
    client = JiraClient()
    return client.request("PUT", f"/filter/{filter_id}/favourite")  # type: ignore[return-value]


def filter_favourite_unset(filter_id: str) -> Dict[str, Any]:
    """DELETE /filter/{id}/favourite - Remove filter from favourites."""
    client = JiraClient()
    return client.request("DELETE", f"/filter/{filter_id}/favourite")  # type: ignore[return-value]
