"""Tools for HubSpot CRM Companies (v3)."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import hubspot_request


def companies_create(properties: Dict[str, Any], associations: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """Create a company.

    POST /crm/v3/objects/companies
    """
    payload: Dict[str, Any] = {"properties": properties}
    if associations is not None:
        payload["associations"] = associations
    return hubspot_request("POST", "/crm/v3/objects/companies", json=payload)


def companies_get(
    company_id: str,
    *,
    properties: Optional[List[str]] = None,
    properties_with_history: Optional[List[str]] = None,
    associations: Optional[List[str]] = None,
    archived: bool = False,
) -> Dict[str, Any]:
    """Get a company by ID.

    GET /crm/v3/objects/companies/{companyId}
    """
    params: Dict[str, Any] = {"archived": str(archived).lower()}
    if properties:
        params["properties"] = ",".join(properties)
    if properties_with_history:
        params["propertiesWithHistory"] = ",".join(properties_with_history)
    if associations:
        params["associations"] = ",".join(associations)
    return hubspot_request("GET", f"/crm/v3/objects/companies/{company_id}", params=params)


def companies_list(
    *,
    limit: int = 100,
    after: Optional[str] = None,
    properties: Optional[List[str]] = None,
    properties_with_history: Optional[List[str]] = None,
    associations: Optional[List[str]] = None,
    archived: bool = False,
) -> Dict[str, Any]:
    """List companies.

    GET /crm/v3/objects/companies
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
    return hubspot_request("GET", "/crm/v3/objects/companies", params=params)


def companies_update(company_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    """Update a company.

    PATCH /crm/v3/objects/companies/{companyId}
    """
    return hubspot_request(
        "PATCH",
        f"/crm/v3/objects/companies/{company_id}",
        json={"properties": properties},
    )


def companies_archive(company_id: str) -> Dict[str, Any]:
    """Archive (delete) a company.

    DELETE /crm/v3/objects/companies/{companyId}
    """
    return hubspot_request("DELETE", f"/crm/v3/objects/companies/{company_id}")


def companies_batch_create(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Batch create companies.

    POST /crm/v3/objects/companies/batch/create

    inputs: list of {"properties": {...}} or raw properties dicts.
    """
    normalized = []
    for item in inputs:
        if "properties" in item:
            normalized.append(item)
        else:
            normalized.append({"properties": item})
    return hubspot_request("POST", "/crm/v3/objects/companies/batch/create", json={"inputs": normalized})


def companies_batch_read(
    inputs: List[Dict[str, str]],
    *,
    id_property: Optional[str] = None,
    properties: Optional[List[str]] = None,
    properties_with_history: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Batch read companies.

    POST /crm/v3/objects/companies/batch/read
    """
    payload: Dict[str, Any] = {"inputs": inputs}
    if id_property:
        payload["idProperty"] = id_property
    if properties:
        payload["properties"] = properties
    if properties_with_history:
        payload["propertiesWithHistory"] = properties_with_history
    return hubspot_request("POST", "/crm/v3/objects/companies/batch/read", json=payload)


def companies_batch_update(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Batch update companies.

    POST /crm/v3/objects/companies/batch/update
    """
    return hubspot_request("POST", "/crm/v3/objects/companies/batch/update", json={"inputs": inputs})


def companies_batch_archive(inputs: List[Dict[str, str]]) -> Dict[str, Any]:
    """Batch archive companies.

    POST /crm/v3/objects/companies/batch/archive
    """
    return hubspot_request("POST", "/crm/v3/objects/companies/batch/archive", json={"inputs": inputs})


def companies_search(
    filter_groups: List[Dict[str, Any]],
    *,
    query: Optional[str] = None,
    sorts: Optional[List[str]] = None,
    properties: Optional[List[str]] = None,
    limit: int = 10,
    after: Optional[str] = None,
) -> Dict[str, Any]:
    """Search companies.

    POST /crm/v3/objects/companies/search
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
    return hubspot_request("POST", "/crm/v3/objects/companies/search", json=payload)
