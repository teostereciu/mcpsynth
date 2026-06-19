"""Tools for HubSpot CRM Search API (v3)."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import hubspot_post


def crm_search(
    object_type: str,
    *,
    filter_groups: Optional[List[Dict[str, Any]]] = None,
    query: Optional[str] = None,
    sorts: Optional[List[Dict[str, Any]]] = None,
    properties: Optional[List[str]] = None,
    limit: Optional[int] = None,
    after: Optional[str] = None,
) -> Dict[str, Any] | list | str:
    """Search CRM objects.

    Args:
        object_type: e.g. "contacts", "companies", "deals", "tickets".
        filter_groups: Search filterGroups array.
        query: Free-text query.
        sorts: Sort rules.
        properties: Properties to return.
        limit: Page size.
        after: Paging cursor.
    """
    payload: Dict[str, Any] = {}
    if filter_groups is not None:
        payload["filterGroups"] = filter_groups
    if query is not None:
        payload["query"] = query
    if sorts is not None:
        payload["sorts"] = sorts
    if properties is not None:
        payload["properties"] = properties
    if limit is not None:
        payload["limit"] = limit
    if after is not None:
        payload["after"] = after

    return hubspot_post(f"/crm/v3/objects/{object_type}/search", payload)
