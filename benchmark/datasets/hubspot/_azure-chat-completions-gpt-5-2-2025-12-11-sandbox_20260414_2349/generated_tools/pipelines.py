"""Tools for HubSpot CRM Pipelines (v3)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import hubspot_request


def pipelines_list(object_type: str) -> Dict[str, Any]:
    """List pipelines for an object type.

    GET /crm/v3/pipelines/{objectType}

    object_type examples: 'deals', 'tickets'
    """
    return hubspot_request("GET", f"/crm/v3/pipelines/{object_type}")


def pipelines_get(object_type: str, pipeline_id: str) -> Dict[str, Any]:
    """Get a pipeline.

    GET /crm/v3/pipelines/{objectType}/{pipelineId}
    """
    return hubspot_request("GET", f"/crm/v3/pipelines/{object_type}/{pipeline_id}")


def pipelines_create(object_type: str, pipeline: Dict[str, Any]) -> Dict[str, Any]:
    """Create a pipeline.

    POST /crm/v3/pipelines/{objectType}
    """
    return hubspot_request("POST", f"/crm/v3/pipelines/{object_type}", json=pipeline)


def pipelines_update(object_type: str, pipeline_id: str, pipeline_patch: Dict[str, Any]) -> Dict[str, Any]:
    """Update a pipeline.

    PATCH /crm/v3/pipelines/{objectType}/{pipelineId}
    """
    return hubspot_request("PATCH", f"/crm/v3/pipelines/{object_type}/{pipeline_id}", json=pipeline_patch)


def pipelines_replace(object_type: str, pipeline_id: str, pipeline: Dict[str, Any]) -> Dict[str, Any]:
    """Replace a pipeline.

    PUT /crm/v3/pipelines/{objectType}/{pipelineId}
    """
    return hubspot_request("PUT", f"/crm/v3/pipelines/{object_type}/{pipeline_id}", json=pipeline)


def pipelines_delete(object_type: str, pipeline_id: str, *, validate_references_before_delete: bool = False) -> Dict[str, Any]:
    """Delete a pipeline.

    DELETE /crm/v3/pipelines/{objectType}/{pipelineId}
    """
    params: Dict[str, Any] = {}
    if validate_references_before_delete:
        params["validateReferencesBeforeDelete"] = "true"
    return hubspot_request("DELETE", f"/crm/v3/pipelines/{object_type}/{pipeline_id}", params=params)


def pipeline_stages_list(object_type: str, pipeline_id: str) -> Dict[str, Any]:
    """List stages in a pipeline.

    GET /crm/v3/pipelines/{objectType}/{pipelineId}/stages
    """
    return hubspot_request("GET", f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages")


def pipeline_stages_get(object_type: str, pipeline_id: str, stage_id: str) -> Dict[str, Any]:
    """Get a stage.

    GET /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}
    """
    return hubspot_request("GET", f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}")


def pipeline_stages_create(object_type: str, pipeline_id: str, stage: Dict[str, Any]) -> Dict[str, Any]:
    """Create a stage.

    POST /crm/v3/pipelines/{objectType}/{pipelineId}/stages
    """
    return hubspot_request("POST", f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages", json=stage)


def pipeline_stages_update(object_type: str, pipeline_id: str, stage_id: str, stage_patch: Dict[str, Any]) -> Dict[str, Any]:
    """Update a stage.

    PATCH /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}
    """
    return hubspot_request(
        "PATCH",
        f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
        json=stage_patch,
    )


def pipeline_stages_replace(object_type: str, pipeline_id: str, stage_id: str, stage: Dict[str, Any]) -> Dict[str, Any]:
    """Replace a stage.

    PUT /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}
    """
    return hubspot_request(
        "PUT",
        f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
        json=stage,
    )


def pipeline_stages_delete(object_type: str, pipeline_id: str, stage_id: str) -> Dict[str, Any]:
    """Delete a stage.

    DELETE /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}
    """
    return hubspot_request("DELETE", f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}")


def pipeline_audit(object_type: str, pipeline_id: str) -> Dict[str, Any]:
    """Audit pipeline changes.

    GET /crm/v3/pipelines/{objectType}/{pipelineId}/audit
    """
    return hubspot_request("GET", f"/crm/v3/pipelines/{object_type}/{pipeline_id}/audit")


def pipeline_stage_audit(object_type: str, pipeline_id: str, stage_id: str) -> Dict[str, Any]:
    """Audit stage changes.

    GET /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}/audit
    """
    return hubspot_request("GET", f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}/audit")
