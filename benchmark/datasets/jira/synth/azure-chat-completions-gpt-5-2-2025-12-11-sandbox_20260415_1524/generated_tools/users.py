from typing import Any, Dict, List, Optional

from .jira_client import JiraClient, clean_params


def user_get(account_id: Optional[str] = None, username: Optional[str] = None, key: Optional[str] = None, expand: Optional[str] = None) -> Dict[str, Any]:
    """GET /user - Get user."""
    client = JiraClient()
    params = clean_params({"accountId": account_id, "username": username, "key": key, "expand": expand})
    return client.request("GET", "/user", params=params)  # type: ignore[return-value]


def user_create(email_address: str, products: List[str], display_name: Optional[str] = None, application_keys: Optional[List[str]] = None) -> Dict[str, Any]:
    """POST /user - Create user (legacy)."""
    client = JiraClient()
    body: Dict[str, Any] = {"emailAddress": email_address, "products": products}
    if display_name is not None:
        body["displayName"] = display_name
    if application_keys is not None:
        body["applicationKeys"] = application_keys
    return client.request("POST", "/user", json_body=body)  # type: ignore[return-value]


def user_delete(account_id: str) -> Dict[str, Any]:
    """DELETE /user - Delete user."""
    client = JiraClient()
    params = clean_params({"accountId": account_id})
    return client.request("DELETE", "/user", params=params)  # type: ignore[return-value]


def users_bulk_get(account_ids: List[str], start_at: Optional[int] = None, max_results: Optional[int] = None) -> Dict[str, Any]:
    """GET /user/bulk - Bulk get users by accountId."""
    client = JiraClient()
    params = clean_params({"accountId": account_ids, "startAt": start_at, "maxResults": max_results})
    return client.request("GET", "/user/bulk", params=params)  # type: ignore[return-value]


def user_groups_get(account_id: str) -> Any:
    """GET /user/groups - Get groups for a user."""
    client = JiraClient()
    params = clean_params({"accountId": account_id})
    return client.request("GET", "/user/groups", params=params)


def users_get_all(start_at: Optional[int] = None, max_results: Optional[int] = None) -> Any:
    """GET /users - Get all users (admin)."""
    client = JiraClient()
    params = clean_params({"startAt": start_at, "maxResults": max_results})
    return client.request("GET", "/users", params=params)


def users_search(query: str, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Any:
    """GET /users/search - Search users."""
    client = JiraClient()
    params = clean_params({"query": query, "startAt": start_at, "maxResults": max_results})
    return client.request("GET", "/users/search", params=params)
