"""Ticketing: Groups tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import zendesk_delete, zendesk_get, zendesk_post, zendesk_put


def _unwrap(obj: Dict[str, Any], key: str) -> Dict[str, Any]:
    if not isinstance(obj, dict):
        return {"error": "invalid_response", "description": "Expected dict response"}
    if "error" in obj and "status" in obj:
        return obj
    return obj.get(key) or obj


def groups_list(per_page: int = 100, page: Optional[int] = None, exclude_deleted: Optional[bool] = None, sort: Optional[str] = None) -> Dict[str, Any]:
    """List groups.

    Maps to GET /api/v2/groups
    """
    params: Dict[str, Any] = {"per_page": per_page}
    if page is not None:
        params["page"] = page
    if exclude_deleted is not None:
        params["exclude_deleted"] = str(exclude_deleted).lower()
    if sort:
        params["sort"] = sort
    return zendesk_get("/groups", params=params)


def groups_show(group_id: int) -> Dict[str, Any]:
    """Show a group.

    Maps to GET /api/v2/groups/{id}
    """
    return _unwrap(zendesk_get(f"/groups/{group_id}"), "group")


def groups_create(name: str, additional_fields: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Create a group.

    Maps to POST /api/v2/groups
    """
    group: Dict[str, Any] = {"name": name}
    if additional_fields:
        group.update(additional_fields)
    return _unwrap(zendesk_post("/groups", {"group": group}), "group")


def groups_update(group_id: int, fields: Dict[str, Any]) -> Dict[str, Any]:
    """Update a group.

    Maps to PUT /api/v2/groups/{id}
    """
    return _unwrap(zendesk_put(f"/groups/{group_id}", {"group": fields}), "group")


def groups_delete(group_id: int) -> Dict[str, Any]:
    """Delete a group.

    Maps to DELETE /api/v2/groups/{id}
    """
    return zendesk_delete(f"/groups/{group_id}")
