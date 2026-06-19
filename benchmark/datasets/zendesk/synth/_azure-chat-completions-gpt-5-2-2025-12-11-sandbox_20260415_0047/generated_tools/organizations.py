"""Ticketing: Organizations tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import zendesk_delete, zendesk_get, zendesk_post, zendesk_put


def _unwrap(obj: Dict[str, Any], key: str) -> Dict[str, Any]:
    if not isinstance(obj, dict):
        return {"error": "invalid_response", "description": "Expected dict response"}
    if "error" in obj and "status" in obj:
        return obj
    return obj.get(key) or obj


def organizations_list(per_page: int = 25, page: Optional[int] = None, sort: Optional[str] = None) -> Dict[str, Any]:
    """List organizations.

    Maps to GET /api/v2/organizations
    """
    params: Dict[str, Any] = {"per_page": per_page}
    if page is not None:
        params["page"] = page
    if sort:
        params["sort"] = sort
    return zendesk_get("/organizations", params=params)


def organizations_show(organization_id: int) -> Dict[str, Any]:
    """Show an organization.

    Maps to GET /api/v2/organizations/{id}
    """
    return _unwrap(zendesk_get(f"/organizations/{organization_id}"), "organization")


def organizations_create(name: str, additional_fields: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Create an organization.

    Maps to POST /api/v2/organizations
    """
    org: Dict[str, Any] = {"name": name}
    if additional_fields:
        org.update(additional_fields)
    return _unwrap(zendesk_post("/organizations", {"organization": org}), "organization")


def organizations_update(organization_id: int, fields: Dict[str, Any]) -> Dict[str, Any]:
    """Update an organization.

    Maps to PUT /api/v2/organizations/{id}
    """
    return _unwrap(zendesk_put(f"/organizations/{organization_id}", {"organization": fields}), "organization")


def organizations_delete(organization_id: int) -> Dict[str, Any]:
    """Delete an organization.

    Maps to DELETE /api/v2/organizations/{id}
    """
    return zendesk_delete(f"/organizations/{organization_id}")
