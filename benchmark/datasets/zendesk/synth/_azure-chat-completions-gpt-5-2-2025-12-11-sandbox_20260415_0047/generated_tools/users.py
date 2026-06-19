"""Ticketing: Users tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import zendesk_delete, zendesk_get, zendesk_post, zendesk_put


def _unwrap(obj: Dict[str, Any], key: str) -> Dict[str, Any]:
    if not isinstance(obj, dict):
        return {"error": "invalid_response", "description": "Expected dict response"}
    if "error" in obj and "status" in obj:
        return obj
    return obj.get(key) or obj


def users_list(per_page: int = 25, page: Optional[int] = None) -> Dict[str, Any]:
    """List users.

    Maps to GET /api/v2/users
    """
    params: Dict[str, Any] = {"per_page": per_page}
    if page is not None:
        params["page"] = page
    return zendesk_get("/users", params=params)


def users_show(user_id: int) -> Dict[str, Any]:
    """Show a user.

    Maps to GET /api/v2/users/{id}
    """
    return _unwrap(zendesk_get(f"/users/{user_id}"), "user")


def users_create(name: str, email: str, role: str = "end-user", additional_fields: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Create a user.

    Maps to POST /api/v2/users
    """
    user: Dict[str, Any] = {"name": name, "email": email, "role": role}
    if additional_fields:
        user.update(additional_fields)
    return _unwrap(zendesk_post("/users", {"user": user}), "user")


def users_update(user_id: int, fields: Dict[str, Any]) -> Dict[str, Any]:
    """Update a user.

    Maps to PUT /api/v2/users/{id}
    """
    return _unwrap(zendesk_put(f"/users/{user_id}", {"user": fields}), "user")


def users_delete(user_id: int) -> Dict[str, Any]:
    """Delete a user.

    Maps to DELETE /api/v2/users/{id}
    """
    return zendesk_delete(f"/users/{user_id}")


def users_search(query: str, per_page: int = 25, page: Optional[int] = None) -> Dict[str, Any]:
    """Search users.

    Maps to GET /api/v2/users/search?query=...
    """
    params: Dict[str, Any] = {"query": query, "per_page": per_page}
    if page is not None:
        params["page"] = page
    return zendesk_get("/users/search", params=params)
