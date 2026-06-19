"""Tools for HubSpot CRM Companies (v3 objects API)."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import hubspot_delete, hubspot_get, hubspot_patch, hubspot_post, hubspot_put


def companies_create(
    properties: Dict[str, Any],
    associations: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any] | list | str:
    payload: Dict[str, Any] = {"properties": properties}
    if associations is not None:
        payload["associations"] = associations
    return hubspot_post("/crm/v3/objects/companies", payload)


def companies_get(
    company_id: str,
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
    return hubspot_get(f"/crm/v3/objects/companies/{company_id}", params)


def companies_list(
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
    return hubspot_get("/crm/v3/objects/companies", params)


def companies_update(company_id: str, properties: Dict[str, Any]) -> Dict[str, Any] | list | str:
    return hubspot_patch(f"/crm/v3/objects/companies/{company_id}", {"properties": properties})


def companies_delete(company_id: str) -> Dict[str, Any] | list | str:
    return hubspot_delete(f"/crm/v3/objects/companies/{company_id}")


def companies_batch_create(inputs: List[Dict[str, Any]]) -> Dict[str, Any] | list | str:
    return hubspot_post("/crm/v3/objects/companies/batch/create", {"inputs": inputs})


def companies_batch_read(
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
    return hubspot_post("/crm/v3/objects/companies/batch/read", payload)


def companies_batch_update(inputs: List[Dict[str, Any]]) -> Dict[str, Any] | list | str:
    return hubspot_post("/crm/v3/objects/companies/batch/update", {"inputs": inputs})


def companies_batch_archive(inputs: List[Dict[str, Any]]) -> Dict[str, Any] | list | str:
    return hubspot_post("/crm/v3/objects/companies/batch/archive", {"inputs": inputs})


def companies_associate(
    company_id: str,
    to_object_type: str,
    to_object_id: str,
    association_type_id: int,
) -> Dict[str, Any] | list | str:
    return hubspot_put(
        f"/crm/v3/objects/companies/{company_id}/associations/{to_object_type}/{to_object_id}/{association_type_id}",
        None,
    )


def companies_disassociate(
    company_id: str,
    to_object_type: str,
    to_object_id: str,
    association_type_id: int,
) -> Dict[str, Any] | list | str:
    return hubspot_delete(
        f"/crm/v3/objects/companies/{company_id}/associations/{to_object_type}/{to_object_id}/{association_type_id}"
    )
