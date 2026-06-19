from typing import Any, Dict, List, Optional

from .http import hubspot_request, parse_csv_param


def meetings_create(properties: Dict[str, Any], associations: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    body: Dict[str, Any] = {"properties": properties}
    if associations is not None:
        body["associations"] = associations
    return hubspot_request("POST", "/crm/v3/objects/meetings", json_body=body)


def meetings_get(
    meeting_id: str,
    *,
    properties: Optional[str] = None,
    associations: Optional[str] = None,
    archived: Optional[bool] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if parse_csv_param(properties):
        params["properties"] = parse_csv_param(properties)
    if parse_csv_param(associations):
        params["associations"] = parse_csv_param(associations)
    if archived is not None:
        params["archived"] = str(bool(archived)).lower()
    return hubspot_request("GET", f"/crm/v3/objects/meetings/{meeting_id}", params=params)


def meetings_list(
    *,
    limit: int = 100,
    after: Optional[str] = None,
    properties: Optional[str] = None,
    associations: Optional[str] = None,
    archived: bool = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "archived": str(bool(archived)).lower()}
    if after is not None:
        params["after"] = after
    if parse_csv_param(properties):
        params["properties"] = parse_csv_param(properties)
    if parse_csv_param(associations):
        params["associations"] = parse_csv_param(associations)
    return hubspot_request("GET", "/crm/v3/objects/meetings", params=params)


def meetings_update(meeting_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    return hubspot_request("PATCH", f"/crm/v3/objects/meetings/{meeting_id}", json_body={"properties": properties})


def meetings_archive(meeting_id: str) -> Dict[str, Any]:
    return hubspot_request("DELETE", f"/crm/v3/objects/meetings/{meeting_id}")


def meetings_batch_create(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    return hubspot_request("POST", "/crm/v3/objects/meetings/batch/create", json_body={"inputs": inputs})


def meetings_batch_read(
    inputs: List[Dict[str, Any]],
    *,
    id_property: Optional[str] = None,
    properties: Optional[List[str]] = None,
) -> Dict[str, Any]:
    body: Dict[str, Any] = {"inputs": inputs}
    if id_property:
        body["idProperty"] = id_property
    if properties is not None:
        body["properties"] = properties
    return hubspot_request("POST", "/crm/v3/objects/meetings/batch/read", json_body=body)


def meetings_batch_update(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    return hubspot_request("POST", "/crm/v3/objects/meetings/batch/update", json_body={"inputs": inputs})


def meetings_batch_archive(inputs: List[Dict[str, Any]]) -> Dict[str, Any]:
    return hubspot_request("POST", "/crm/v3/objects/meetings/batch/archive", json_body={"inputs": inputs})


def meetings_associate(meeting_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    return hubspot_request(
        "PUT",
        f"/crm/v3/objects/meetings/{meeting_id}/associations/{to_object_type}/{to_object_id}/{association_type_id}",
    )


def meetings_disassociate(meeting_id: str, to_object_type: str, to_object_id: str, association_type_id: int) -> Dict[str, Any]:
    return hubspot_request(
        "DELETE",
        f"/crm/v3/objects/meetings/{meeting_id}/associations/{to_object_type}/{to_object_id}/{association_type_id}",
    )
