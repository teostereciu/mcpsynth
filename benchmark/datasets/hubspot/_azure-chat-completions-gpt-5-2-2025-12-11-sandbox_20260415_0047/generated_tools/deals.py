"""Tools for HubSpot CRM Deals (v3 objects API)."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import hubspot_delete, hubspot_get, hubspot_patch, hubspot_post, hubspot_put


def deals_create(
    properties: Dict[str, Any],
    associations: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any] | list | str:
    payload: Dict[str, Any] = {"properties": properties}
    if associations is not None:
        payload["associations"] = associations
    return hubspot_post("/crm/v3/objects/deals", payload)


def deals_get(
    deal_id: str,
    properties: Optional[List[str]] = None,
    properties_with_history: Optional[List[str]] = None,
    associations: Optional[List[str]] = None,
    archived: bool = False,
    id_property: Optional[str] = None,
) -> Dict[str, Any] | list | str:
    params: Dict[str, Any] = {"archived": str(archived).lower()}
    if properties:
        params["properties"] = ",".join(properties)
    if properties_with_history:
        params["propertiesWithHistory"] = ",".join(properties_with_history)
    if associations:
        params["associations"] = ",".join(associations)
    if id_property:
        params["idProperty"] = id_property
    return hubspot_get(f"/crm/v3/objects/deals/{deal_id}", params)


def deals_list(
    limit: int = 100,
    after: Optional[str] = None,
    properties: Optional[List[str]] = None,
    associations: Optional[List[str]] = None,
    archived: bool = False,
) -> Dict[str, Any] | list | str:
    params: Dict[str, Any] = {"limit": limit, "archived": str(archived).lower()}
    if after is not None:
        params["after"] = after
    if properties:
        params["properties"] = ",".join(properties)
    if associations:
        params["associations"] = ",".join(associations)
    return hubspot_get("/crm/v3/objects/deals", params)


def deals_update(deal_id: str, properties: Dict[str, Any]) -> Dict[str, Any] | list | str:
    return hubspot_patch(f"/crm/v3/objects/deals/{deal_id}", {"properties": properties})


def deals_delete(deal_id: str) -> Dict[str, Any] | list | str:
    return hubspot_delete(f"/crm/v3/objects/deals/{deal_id}")


def deals_batch_create(inputs: List[Dict[str, Any]]) -> Dict[str, Any] | list | str:
    return hubspot_post("/crm/v3/objects/deals/batch/create", {"inputs": inputs})


def deals_batch_read(
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
    return hubspot_post("/crm/v3/objects/deals/batch/read", payload)


def deals_batch_update(inputs: List[Dict[str, Any]]) -> Dict[str, Any] | list | str:
    return hubspot_post("/crm/v3/objects/deals/batch/update", {"inputs": inputs})


def deals_batch_archive(inputs: List[Dict[str, Any]]) -> Dict[str, Any] | list | str:
    return hubspot_post("/crm/v3/objects/deals/batch/archive", {"inputs": inputs})


def deals_associate(
    deal_id: str,
    to_object_type: str,
    to_object_id: str,
    association_type_id: int,
) -> Dict[str, Any] | list | str:
    return hubspot_put(
        f"/crm/v3/objects/deals/{deal_id}/associations/{to_object_type}/{to_object_id}/{association_type_id}",
        None,
    )


def deals_disassociate(
    deal_id: str,
    to_object_type: str,
    to_object_id: str,
    association_type_id: int,
) -> Dict[str, Any] | list | str:
    return hubspot_delete(
        f"/crm/v3/objects/deals/{deal_id}/associations/{to_object_type}/{to_object_id}/{association_type_id}"
    )
