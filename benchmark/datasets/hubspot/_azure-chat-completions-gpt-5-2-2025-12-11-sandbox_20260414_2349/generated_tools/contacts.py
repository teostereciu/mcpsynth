"""Tools for HubSpot CRM Contacts (v3)."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import hubspot_request


def contacts_create(properties: Dict[str, Any], associations: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """Create a contact.

    POST /crm/v3/objects/contacts
    """
    payload: Dict[str, Any] = {"properties": properties}
    if associations is not None:
        payload["associations"] = associations
    return hubspot_request("POST", "/crm/v3/objects/contacts", json=payload)


def contacts_get(
    record_id_or_email: str,
    *,
    id_property: Optional[str] = None,
    properties: Optional[List[str]] = None,
    properties_with_history: Optional[List[str]] = None,
    associations: Optional[List[str]] = None,
    archived: bool = False,
) -> Dict[str, Any]:
    """Get a contact by record ID or by email (with id_property='email').

    GET /crm/v3/objects/contacts/{recordId}
    GET /crm/v3/objects/contacts/{email}?idProperty=email
    """
    params: Dict[str, Any] = {"archived": str(archived).lower()}
    if id_property:
        params["idProperty"] = id_property
    if properties:
        params["properties"] = ",".join(properties)
    if properties_with_history:
        params["propertiesWithHistory"] = ",".join(properties_with_history)
    if associations:
        params["associations"] = ",".join(associations)

    return hubspot_request("GET", f"/crm/v3/objects/contacts/{record_id_or_email}", params=params)


def contacts_list(
    *,
    limit: int = 100,
    after: Optional[str] = None,
    properties: Optional[List[str]] = None,
    properties_with_history: Optional[List[str]] = None,
    associations: Optional[List[str]] = None,
    archived: bool = False,
) -> Dict[str, Any]:
    """List contacts.

    GET /crm/v3/objects/contacts
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

    return hubspot_request("GET", "/crm/v3/objects/contacts", params=params)


def contacts_update(record_id_or_email: str, properties: Dict[str, Any], *, id_property: Optional[str] = None) -> Dict[str, Any]:
    """Update a contact by record ID or email.

    PATCH /crm/v3/objects/contacts/{contactId}
    """
    params: Dict[str, Any] = {}
    if id_property:
        params["idProperty"] = id_property
    payload = {"properties": properties}
    return hubspot_request("PATCH", f"/crm/v3/objects/contacts/{record_id_or_email}", params=params, json=payload)


def contacts_archive(record_id: str) -> Dict[str, Any]:
    """Archive (delete) a contact.

    DELETE /crm/v3/objects/contacts/{contactId}
    """
    return hubspot_request("DELETE", f"/crm/v3/objects/contacts/{record_id}")


def contacts_batch_create(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Batch create contacts.

    POST /crm/v3/objects/contacts/batch/create

    inputs: list of {"properties": {...}} or raw properties dicts.
    """
    normalized = []
    for item in inputs:
        if "properties" in item:
            normalized.append(item)
        else:
            normalized.append({"properties": item})
    return hubspot_request("POST", "/crm/v3/objects/contacts/batch/create", json={"inputs": normalized})


def contacts_batch_read(
    inputs: List[Dict[str, str]],
    *,
    id_property: Optional[str] = None,
    properties: Optional[List[str]] = None,
    properties_with_history: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Batch read contacts.

    POST /crm/v3/objects/contacts/batch/read

    inputs: list of {"id": "..."}
    """
    payload: Dict[str, Any] = {"inputs": inputs}
    if id_property:
        payload["idProperty"] = id_property
    if properties:
        payload["properties"] = properties
    if properties_with_history:
        payload["propertiesWithHistory"] = properties_with_history
    return hubspot_request("POST", "/crm/v3/objects/contacts/batch/read", json=payload)


def contacts_batch_update(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Batch update contacts.

    POST /crm/v3/objects/contacts/batch/update

    inputs: list of {"id": "...", "properties": {...}}
    """
    return hubspot_request("POST", "/crm/v3/objects/contacts/batch/update", json={"inputs": inputs})


def contacts_batch_archive(inputs: List[Dict[str, str]]) -> Dict[str, Any]:
    """Batch archive contacts.

    POST /crm/v3/objects/contacts/batch/archive

    inputs: list of {"id": "..."}
    """
    return hubspot_request("POST", "/crm/v3/objects/contacts/batch/archive", json={"inputs": inputs})


def contacts_search(
    filter_groups: List[Dict[str, Any]],
    *,
    query: Optional[str] = None,
    sorts: Optional[List[str]] = None,
    properties: Optional[List[str]] = None,
    limit: int = 10,
    after: Optional[str] = None,
) -> Dict[str, Any]:
    """Search contacts.

    POST /crm/v3/objects/contacts/search

    filter_groups: [{"filters": [{"propertyName": "email", "operator": "EQ", "value": "a@b.com"}]}]
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
    return hubspot_request("POST", "/crm/v3/objects/contacts/search", json=payload)
