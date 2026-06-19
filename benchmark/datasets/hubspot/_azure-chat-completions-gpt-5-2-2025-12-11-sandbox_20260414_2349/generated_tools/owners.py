"""Tools for HubSpot CRM Owners (v3)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import hubspot_request


def owners_list(*, email: Optional[str] = None, after: Optional[str] = None, limit: Optional[int] = None, archived: bool = False) -> Dict[str, Any]:
    """List CRM owners.

    GET /crm/v3/owners

    Note: HubSpot supports optional query params like email, after, limit, archived.
    """
    params: Dict[str, Any] = {"archived": str(archived).lower()}
    if email is not None:
        params["email"] = email
    if after is not None:
        params["after"] = after
    if limit is not None:
        params["limit"] = limit
    return hubspot_request("GET", "/crm/v3/owners", params=params)


def owners_get(owner_id: str, *, archived: bool = False) -> Dict[str, Any]:
    """Get an owner by ID.

    GET /crm/v3/owners/{ownerId}
    """
    return hubspot_request("GET", f"/crm/v3/owners/{owner_id}", params={"archived": str(archived).lower()})
