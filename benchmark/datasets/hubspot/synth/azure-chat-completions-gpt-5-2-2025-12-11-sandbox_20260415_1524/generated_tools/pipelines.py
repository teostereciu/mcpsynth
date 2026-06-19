from typing import Any, Dict, Optional

from .http import hubspot_request


def pipelines_create(object_type: str, pipeline: Dict[str, Any]) -> Dict[str, Any]:
    return hubspot_request("POST", f"/crm/v3/pipelines/{object_type}", json_body=pipeline)


def pipelines_replace(object_type: str, pipeline_id: str, pipeline: Dict[str, Any]) -> Dict[str, Any]:
    return hubspot_request("PUT", f"/crm/v3/pipelines/{object_type}/{pipeline_id}", json_body=pipeline)


def pipelines_list(object_type: str) -> Dict[str, Any]:
    return hubspot_request("GET", f"/crm/v3/pipelines/{object_type}")


def pipelines_get(object_type: str, pipeline_id: str) -> Dict[str, Any]:
    return hubspot_request("GET", f"/crm/v3/pipelines/{object_type}/{pipeline_id}")


def pipelines_update(object_type: str, pipeline_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    return hubspot_request("PATCH", f"/crm/v3/pipelines/{object_type}/{pipeline_id}", json_body=properties)


def pipelines_delete(object_type: str, pipeline_id: str, *, validate_references_before_delete: bool = False) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if validate_references_before_delete:
        params["validateReferencesBeforeDelete"] = "true"
    return hubspot_request("DELETE", f"/crm/v3/pipelines/{object_type}/{pipeline_id}", params=params)


def pipeline_stages_create(object_type: str, pipeline_id: str, stage: Dict[str, Any]) -> Dict[str, Any]:
    return hubspot_request("POST", f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages", json_body=stage)


def pipeline_stages_replace(object_type: str, pipeline_id: str, stage_id: str, stage: Dict[str, Any]) -> Dict[str, Any]:
    return hubspot_request("PUT", f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}", json_body=stage)


def pipeline_stages_list(object_type: str, pipeline_id: str) -> Dict[str, Any]:
    return hubspot_request("GET", f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages")


def pipeline_stages_get(object_type: str, pipeline_id: str, stage_id: str) -> Dict[str, Any]:
    return hubspot_request("GET", f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}")


def pipeline_stages_update(object_type: str, pipeline_id: str, stage_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
    return hubspot_request("PATCH", f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}", json_body=properties)


def pipeline_stages_delete(object_type: str, pipeline_id: str, stage_id: str) -> Dict[str, Any]:
    return hubspot_request("DELETE", f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}")


def pipelines_audit(object_type: str, pipeline_id: str) -> Dict[str, Any]:
    return hubspot_request("GET", f"/crm/v3/pipelines/{object_type}/{pipeline_id}/audit")


def pipeline_stages_audit(object_type: str, pipeline_id: str, stage_id: str) -> Dict[str, Any]:
    return hubspot_request("GET", f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}/audit")
