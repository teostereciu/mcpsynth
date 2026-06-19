"""Tools for HubSpot CRM Contacts (v3 objects API)."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import hubspot_delete, hubspot_get, hubspot_patch, hubspot_post, hubspot_put


def contacts_create(
    properties: Dict[str, Any],
    associations: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any] | list | str:
    """Create a contact.

    Args:
        properties: Contact properties (e.g., email, firstname, lastname).
        associations: Optional associations array per HubSpot objects API.
    """
    payload: Dict[str, Any] = {"properties": properties}
    if associations is not None:
        payload["associations"] = associations
    return hubspot_post("/crm/v3/objects/contacts", payload)


def contacts_get(
    contact_id: str,
    properties: Optional[List[str]] = None,
    properties_with_history: Optional[List[str]] = None,
    associations: Optional[List[str]] = None,
    archived: bool = False,
    id_property: Optional[str] = None,
) -> Dict[str, Any] | list | str:
    """Get a contact by record ID or by unique property (via idProperty)."""
    params: Dict[str, Any] = {"archived": str(archived).lower()}
    if properties:
        params["properties"] = ",".join(properties)
    if properties_with_history:
        params["propertiesWithHistory"] = ",".join(properties_with_history)
    if associations:
        params["associations"] = ",".join(associations)
    if id_property:
        params["idProperty"] = id_property
    return hubspot_get(f"/crm/v3/objects/contacts/{contact_id}", params)


def contacts_list(
    limit: int = 100,
    after: Optional[str] = None,
    properties: Optional[List[str]] = None,
    associations: Optional[List[str]] = None,
    archived: bool = False,
) -> Dict[str, Any] | list | str:
    """List contacts."""
    params: Dict[str, Any] = {"limit": limit, "archived": str(archived).lower()}
    if after is not None:
        params["after"] = after
    if properties:
        params["properties"] = ",".join(properties)
    if associations:
        params["associations"] = ",".join(associations)
    return hubspot_get("/crm/v3/objects/contacts", params)


def contacts_update(
    contact_id: str,
    properties: Dict[str, Any],
    id_property: Optional[str] = None,
) -> Dict[str, Any] | list | str:
    """Update a contact by record ID or unique property."""
    params: Dict[str, Any] = {}
    if id_property:
        params["idProperty"] = id_property
    path = f"/crm/v3/objects/contacts/{contact_id}"
    if params:
        # requests handles params separately; our helper doesn't for PATCH.
        # Use GET-style query string for simplicity.
        from urllib.parse import urlencode

        path = f"{path}?{urlencode(params)}"
    return hubspot_patch(path, {"properties": properties})


def contacts_delete(contact_id: str) -> Dict[str, Any] | list | str:
    """Archive (delete) a contact by record ID."""
    return hubspot_delete(f"/crm/v3/objects/contacts/{contact_id}")


def contacts_batch_create(inputs: List[Dict[str, Any]]) -> Dict[str, Any] | list | str:
    """Batch create contacts.

    Args:
        inputs: List of objects with at least a `properties` dict.
            Example: {"properties": {"email": "a@b.com"}}
    """
    return hubspot_post("/crm/v3/objects/contacts/batch/create", {"inputs": inputs})


def contacts_batch_read(
    inputs: List[Dict[str, Any]],
    properties: Optional[List[str]] = None,
    properties_with_history: Optional[List[str]] = None,
    id_property: Optional[str] = None,
) -> Dict[str, Any] | list | str:
    payload: Dict[str, Any] = {"inputs": inputs}
    if properties:
        payload["properties"] = properties
    if properties_with_history:
        payload["propertiesWithHistory"] = properties_with_history
    if id_property:
        payload["idProperty"] = id_property
    return hubspot_post("/crm/v3/objects/contacts/batch/read", payload)


def contacts_batch_update(inputs: List[Dict[str, Any]]) -> Dict[str, Any] | list | str:
    """Batch update contacts by record ID."""
    return hubspot_post("/crm/v3/objects/contacts/batch/update", {"inputs": inputs})


def contacts_batch_archive(inputs: List[Dict[str, Any]]) -> Dict[str, Any] | list | str:
    """Batch archive contacts by record ID."""
    return hubspot_post("/crm/v3/objects/contacts/batch/archive", {"inputs": inputs})


def contacts_associate(
    contact_id: str,
    to_object_type: str,
    to_object_id: str,
    association_type_id: int,
) -> Dict[str, Any] | list | str:
    """Associate a contact to another object via v3 objects associations endpoint."""
    return hubspot_put(
        f"/crm/v3/objects/contacts/{contact_id}/associations/{to_object_type}/{to_object_id}/{association_type_id}",
        None,
    )


def contacts_disassociate(
    contact_id: str,
    to_object_type: str,
    to_object_id: str,
    association_type_id: int,
) -> Dict[str, Any] | list | str:
    """Remove association between a contact and another object."""
    return hubspot_delete(
        f"/crm/v3/objects/contacts/{contact_id}/associations/{to_object_type}/{to_object_id}/{association_type_id}"
    )
