from typing import Any, Dict, List, Optional

from .http import hubspot_request


def crm_search(
    object_type: str,
    *,
    query: Optional[str] = None,
    filter_groups: Optional[List[Dict[str, Any]]] = None,
    sorts: Optional[List[Dict[str, Any]]] = None,
    properties: Optional[List[str]] = None,
    limit: Optional[int] = None,
    after: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /crm/v3/objects/{object_type}/search

    object_type examples: contacts, companies, deals, tickets, tasks, notes, calls, meetings.
    """
    body: Dict[str, Any] = {}
    if query is not None:
        body["query"] = query
    if filter_groups is not None:
        body["filterGroups"] = filter_groups
    if sorts is not None:
        body["sorts"] = sorts
    if properties is not None:
        body["properties"] = properties
    if limit is not None:
        body["limit"] = limit
    if after is not None:
        body["after"] = after

    return hubspot_request("POST", f"/crm/v3/objects/{object_type}/search", json_body=body)
