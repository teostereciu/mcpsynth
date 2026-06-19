"""Tools for HubSpot CRM Pipelines API (v3)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import hubspot_delete, hubspot_get, hubspot_patch, hubspot_post, hubspot_put


def pipelines_list(object_type: str) -> Dict[str, Any] | list | str:
    """List pipelines for an object type (e.g., 'deals', 'tickets')."""
    return hubspot_get(f"/crm/v3/pipelines/{object_type}")


def pipelines_get(object_type: str, pipeline_id: str) -> Dict[str, Any] | list | str:
    return hubspot_get(f"/crm/v3/pipelines/{object_type}/{pipeline_id}")


def pipelines_create(object_type: str, pipeline: Dict[str, Any]) -> Dict[str, Any] | list | str:
    return hubspot_post(f"/crm/v3/pipelines/{object_type}", pipeline)


def pipelines_replace(object_type: str, pipeline_id: str, pipeline: Dict[str, Any]) -> Dict[str, Any] | list | str:
    return hubspot_put(f"/crm/v3/pipelines/{object_type}/{pipeline_id}", pipeline)


def pipelines_update(object_type: str, pipeline_id: str, patch: Dict[str, Any]) -> Dict[str, Any] | list | str:
    return hubspot_patch(f"/crm/v3/pipelines/{object_type}/{pipeline_id}", patch)


def pipelines_delete(
    object_type: str,
    pipeline_id: str,
    *,
    validate_references_before_delete: Optional[bool] = None,
) -> Dict[str, Any] | list | str:
    path = f"/crm/v3/pipelines/{object_type}/{pipeline_id}"
    if validate_references_before_delete is None:
        return hubspot_delete(path)

    from urllib.parse import urlencode

    return hubspot_delete(f"{path}?{urlencode({'validateReferencesBeforeDelete': str(validate_references_before_delete).lower()})}")


def pipeline_stages_list(object_type: str, pipeline_id: str) -> Dict[str, Any] | list | str:
    return hubspot_get(f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages")


def pipeline_stages_get(object_type: str, pipeline_id: str, stage_id: str) -> Dict[str, Any] | list | str:
    return hubspot_get(f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}")


def pipeline_stages_create(object_type: str, pipeline_id: str, stage: Dict[str, Any]) -> Dict[str, Any] | list | str:
    return hubspot_post(f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages", stage)


def pipeline_stages_replace(
    object_type: str, pipeline_id: str, stage_id: str, stage: Dict[str, Any]
) -> Dict[str, Any] | list | str:
    return hubspot_put(f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}", stage)


def pipeline_stages_update(
    object_type: str, pipeline_id: str, stage_id: str, patch: Dict[str, Any]
) -> Dict[str, Any] | list | str:
    return hubspot_patch(f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}", patch)


def pipeline_stages_delete(object_type: str, pipeline_id: str, stage_id: str) -> Dict[str, Any] | list | str:
    return hubspot_delete(f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}")


def pipelines_audit(object_type: str, pipeline_id: str) -> Dict[str, Any] | list | str:
    return hubspot_get(f"/crm/v3/pipelines/{object_type}/{pipeline_id}/audit")


def pipeline_stages_audit(object_type: str, pipeline_id: str, stage_id: str) -> Dict[str, Any] | list | str:
    return hubspot_get(f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}/audit")
