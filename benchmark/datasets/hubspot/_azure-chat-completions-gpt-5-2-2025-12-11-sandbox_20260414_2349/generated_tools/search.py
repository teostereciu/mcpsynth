"""Generic CRM search tool for any object type (v3)."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import hubspot_request


def crm_search(
    object_type: str,
    filter_groups: List[Dict[str, Any]],
    *,
    query: Optional[str] = None,
    sorts: Optional[List[str]] = None,
    properties: Optional[List[str]] = None,
    limit: int = 10,
    after: Optional[str] = None,
) -> Dict[str, Any]:
    """Search CRM objects.

    POST /crm/v3/objects/{objectType}/search

    object_type examples: 'contacts', 'companies', 'deals', 'tickets'
    """
    payload: Dict[str, Any] = {"filterGroups": filter_groups, "limit": limit}
    if query is not None:
        payload["query"] = query
    if sorts is not None:
        payload["sorts"] = sorts
    if properties is not None:
        payload["properties"] = properties
    if after is not None:
        payload["after"] = after
    return hubspot_request("POST", f"/crm/v3/objects/{object_type}/search", json=payload)
