from typing import Any, Dict, List, Optional

from ._client import get_client


def list_users(page: Optional[int] = None, per_page: Optional[int] = None, role: Optional[str] = None) -> Dict[str, Any]:
    """GET /api/v2/users"""
    client = get_client()
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if per_page is not None:
        params["per_page"] = per_page
    if role is not None:
        params["role"] = role
    return client.request("GET", f"{client.base_support}/users", params=params)  # type: ignore


def show_user(user_id: int) -> Dict[str, Any]:
    """GET /api/v2/users/{user_id}"""
    client = get_client()
    return client.request("GET", f"{client.base_support}/users/{user_id}")  # type: ignore


def show_many_users(ids: List[int]) -> Dict[str, Any]:
    """GET /api/v2/users/show_many?ids=..."""
    client = get_client()
    params = {"ids": ",".join(str(i) for i in ids)}
    return client.request("GET", f"{client.base_support}/users/show_many", params=params)  # type: ignore


def show_self() -> Dict[str, Any]:
    """GET /api/v2/users/me"""
    client = get_client()
    return client.request("GET", f"{client.base_support}/users/me")  # type: ignore


def search_users(query: str) -> Dict[str, Any]:
    """GET /api/v2/users/search?query=..."""
    client = get_client()
    return client.request("GET", f"{client.base_support}/users/search", params={"query": query})  # type: ignore


def create_user(user: Dict[str, Any]) -> Dict[str, Any]:
    """POST /api/v2/users

    Body: {"user": {...}}
    """
    client = get_client()
    return client.request("POST", f"{client.base_support}/users", json={"user": user})  # type: ignore


def update_user(user_id: int, user: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /api/v2/users/{user_id}

    Body: {"user": {...}}
    """
    client = get_client()
    return client.request("PUT", f"{client.base_support}/users/{user_id}", json={"user": user})  # type: ignore


def delete_user(user_id: int) -> Dict[str, Any]:
    """DELETE /api/v2/users/{user_id}"""
    client = get_client()
    return client.request("DELETE", f"{client.base_support}/users/{user_id}")  # type: ignore


def list_organization_users(organization_id: int, page: Optional[int] = None, per_page: Optional[int] = None) -> Dict[str, Any]:
    """GET /api/v2/organizations/{organization_id}/users"""
    client = get_client()
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if per_page is not None:
        params["per_page"] = per_page
    return client.request(
        "GET", f"{client.base_support}/organizations/{organization_id}/users", params=params
    )  # type: ignore


def list_users_by_group(group_id: int, page: Optional[int] = None, per_page: Optional[int] = None) -> Dict[str, Any]:
    """GET /api/v2/groups/{group_id}/users"""
    client = get_client()
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if per_page is not None:
        params["per_page"] = per_page
    return client.request("GET", f"{client.base_support}/groups/{group_id}/users", params=params)  # type: ignore
