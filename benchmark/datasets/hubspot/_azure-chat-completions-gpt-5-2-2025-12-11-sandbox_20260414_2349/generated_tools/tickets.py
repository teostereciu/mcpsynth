"""Tools for HubSpot CRM Tickets (v3)."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import hubspot_request


def tickets_create(properties: Dict[str, Any], associations: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """Create a ticket.

    POST /crm/v3/objects/tickets
    """
    payload: Dict[str, Any] = {"properties": properties}
    if associations is not None:
        payload["associations"] = associations
    return hubspot_request("POST", "/crm/v3/objects/tickets", json=payload)


def tickets_get(
    ticket_id: str,
    *,
    properties: Optional[List[str]] = None,
    properties_with_history: Optional[List[str]] = None,
    associations: Optional[List[str]] = None,
    archived: bool = False,
) -> Dict[str, Any]:
    """Get a ticket by ID.

    GET /crm/v3/objects/tickets/{ticketId}
    """
    params: Dict[str, Any] = {"archived": str(archived).lower()}
    if properties:
        params["properties"] = ",".join(properties)
    if properties_with_history:
        params["propertiesWithHistory"] = ",".join(properties_with_history)
    if associations:
        params["associations"] = ",".join(associations)
    return hubspot_request("GET", f"/crm/v3/objects/tickets/{ticket_id}", params=params)


def tickets_list(
    *,
    limit: int = 100,
    after: Optional[str] = None,
    properties: Optional[List[str]] = None,
    properties_with_history: Optional[List[str]] = None,
    associations: Optional[List[str]] = None,
    archived: bool = False,
) -> Dict[str, Any]:
    """List tickets.

    GET /crm/v3/objects/tickets
    """
    params: Dict[str, Any] = {"limit": limit, "archived": str(archived).lower()}
    if after is not None:
        params["after"] = after
    if properties:
        params["properties"] = ",".join(properties)
    if properties_with_history:
        params["propertiesWithHistory"] = ",".join(properties_with_history)
    if associations:
        params["associations"] = ",".join(associations)
    return hubspot_request("GET", "/crm/v3/objects/tickets", params=params)


def tickets_update(ticket_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    """Update a ticket.

    PATCH /crm/v3/objects/tickets/{ticketId}
    """
    return hubspot_request("PATCH", f"/crm/v3/objects/tickets/{ticket_id}", json={"properties": properties})


def tickets_archive(ticket_id: str) -> Dict[str, Any]:
    """Archive (delete) a ticket.

    DELETE /crm/v3/objects/tickets/{ticketId}
    """
    return hubspot_request("DELETE", f"/crm/v3/objects/tickets/{ticket_id}")


def tickets_batch_create(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Batch create tickets.

    POST /crm/v3/objects/tickets/batch/create
    """
    normalized = []
    for item in inputs:
        if "properties" in item:
            normalized.append(item)
        else:
            normalized.append({"properties": item})
    return hubspot_request("POST", "/crm/v3/objects/tickets/batch/create", json={"inputs": normalized})


def tickets_batch_read(
    inputs: List[Dict[str, str]],
    *,
    id_property: Optional[str] = None,
    properties: Optional[List[str]] = None,
    properties_with_history: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Batch read tickets.

    POST /crm/v3/objects/tickets/batch/read
    """
    payload: Dict[str, Any] = {"inputs": inputs}
    if id_property:
        payload["idProperty"] = id_property
    if properties:
        payload["properties"] = properties
    if properties_with_history:
        payload["propertiesWithHistory"] = properties_with_history
    return hubspot_request("POST", "/crm/v3/objects/tickets/batch/read", json=payload)


def tickets_batch_update(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Batch update tickets.

    POST /crm/v3/objects/tickets/batch/update
    """
    return hubspot_request("POST", "/crm/v3/objects/tickets/batch/update", json={"inputs": inputs})


def tickets_batch_archive(inputs: List[Dict[str, str]]) -> Dict[str, Any]:
    """Batch archive tickets.

    POST /crm/v3/objects/tickets/batch/archive
    """
    return hubspot_request("POST", "/crm/v3/objects/tickets/batch/archive", json={"inputs": inputs})


def tickets_search(
    filter_groups: List[Dict[str, Any]],
    *,
    query: Optional[str] = None,
    sorts: Optional[List[str]] = None,
    properties: Optional[List[str]] = None,
    limit: int = 10,
    after: Optional[str] = None,
) -> Dict[str, Any]:
    """Search tickets.

    POST /crm/v3/objects/tickets/search
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
    return hubspot_request("POST", "/crm/v3/objects/tickets/search", json=payload)
