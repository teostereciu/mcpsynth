"""Tools for HubSpot CRM Owners (v3)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import hubspot_get


def owners_list(
    *,
    email: Optional[str] = None,
    after: Optional[str] = None,
    limit: Optional[int] = None,
    archived: bool = False,
) -> Dict[str, Any] | list | str:
    """List CRM owners."""
    params: Dict[str, Any] = {"archived": str(archived).lower()}
    if email is not None:
        params["email"] = email
    if after is not None:
        params["after"] = after
    if limit is not None:
        params["limit"] = limit
    return hubspot_get("/crm/v3/owners", params)


def owners_get(owner_id: str, *, archived: bool = False) -> Dict[str, Any] | list | str:
    params = {"archived": str(archived).lower()}
    return hubspot_get(f"/crm/v3/owners/{owner_id}", params)
