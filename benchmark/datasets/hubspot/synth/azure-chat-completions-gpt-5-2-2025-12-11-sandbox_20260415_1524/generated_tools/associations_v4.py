from typing import Any, Dict, List, Optional

from .http import hubspot_request


def associations_v4_associate_default(
    from_object_type: str,
    from_object_id: str,
    to_object_type: str,
    to_object_id: str,
) -> Dict[str, Any]:
    return hubspot_request(
        "PUT",
        f"/crm/objects/2026-03/{from_object_type}/{from_object_id}/associations/default/{to_object_type}/{to_object_id}",
    )


def associations_v4_batch_associate_default(
    from_object_type: str,
    to_object_type: str,
    inputs: List[Dict[str, Any]],
) -> Dict[str, Any]:
    return hubspot_request(
        "POST",
        f"/crm/associations/2026-03/{from_object_type}/{to_object_type}/batch/associate/default",
        json_body={"inputs": inputs},
    )


def associations_v4_associate_labeled(
    from_object_type: str,
    from_object_id: str,
    to_object_type: str,
    to_object_id: str,
    types: List[Dict[str, Any]],
) -> Dict[str, Any]:
    return hubspot_request(
        "PUT",
        f"/crm/objects/2026-03/{from_object_type}/{from_object_id}/associations/{to_object_type}/{to_object_id}",
        json_body=types,
    )


def associations_v4_batch_create_labeled(
    from_object_type: str,
    to_object_type: str,
    inputs: List[Dict[str, Any]],
) -> Dict[str, Any]:
    return hubspot_request(
        "POST",
        f"/crm/associations/2026-03/{from_object_type}/{to_object_type}/batch/create",
        json_body={"inputs": inputs},
    )


def associations_v4_get(
    from_object_type: str,
    object_id: str,
    to_object_type: str,
) -> Dict[str, Any]:
    return hubspot_request(
        "GET",
        f"/crm/objects/2026-03/{from_object_type}/{object_id}/associations/{to_object_type}",
    )


def associations_v4_batch_read(
    from_object_type: str,
    to_object_type: str,
    inputs: List[Dict[str, Any]],
) -> Dict[str, Any]:
    return hubspot_request(
        "POST",
        f"/crm/associations/2026-03/{from_object_type}/{to_object_type}/batch/read",
        json_body={"inputs": inputs},
    )


def associations_v4_delete_all_between(
    from_object_type: str,
    from_object_id: str,
    to_object_type: str,
    to_object_id: str,
) -> Dict[str, Any]:
    return hubspot_request(
        "DELETE",
        f"/crm/objects/2026-03/{from_object_type}/{from_object_id}/associations/{to_object_type}/{to_object_id}",
    )


def associations_v4_batch_archive_all(
    from_object_type: str,
    to_object_type: str,
    inputs: List[Dict[str, Any]],
) -> Dict[str, Any]:
    return hubspot_request(
        "POST",
        f"/crm/associations/2026-03/{from_object_type}/{to_object_type}/batch/archive",
        json_body={"inputs": inputs},
    )


def associations_v4_batch_archive_labels(
    from_object_type: str,
    to_object_type: str,
    inputs: List[Dict[str, Any]],
) -> Dict[str, Any]:
    return hubspot_request(
        "POST",
        f"/crm/associations/2026-03/{from_object_type}/{to_object_type}/batch/labels/archive",
        json_body={"inputs": inputs},
    )


def associations_v4_get_labels(from_object_type: str, to_object_type: str) -> Dict[str, Any]:
    return hubspot_request(
        "GET",
        f"/crm/associations/2026-03/{from_object_type}/{to_object_type}/labels",
    )
