"""Tools for HubSpot CRM Associations APIs (v3 and v4).

Note: For the scenarios, v3 object association endpoints are sufficient.
This module adds broader coverage: v3 association types + batch create/read/archive,
plus v4 labels lookup and default association endpoints.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import hubspot_delete, hubspot_get, hubspot_post, hubspot_put


def associations_v3_types(from_object_type: str, to_object_type: str) -> Dict[str, Any] | list | str:
    """List association types between two object types (v3)."""
    return hubspot_get(f"/crm/v3/associations/{from_object_type}/{to_object_type}/types")


def associations_v3_batch_create(
    from_object_type: str,
    to_object_type: str,
    inputs: List[Dict[str, Any]],
) -> Dict[str, Any] | list | str:
    """Batch create associations (v3).

    inputs example item:
      {"from": {"id": "53628"}, "to": {"id": "12726"}, "type": "contact_to_company"}
    """
    return hubspot_post(
        f"/crm/v3/associations/{from_object_type}/{to_object_type}/batch/create",
        {"inputs": inputs},
    )


def associations_v3_batch_read(
    from_object_type: str,
    to_object_type: str,
    inputs: List[Dict[str, Any]],
) -> Dict[str, Any] | list | str:
    """Batch read associations (v3)."""
    return hubspot_post(
        f"/crm/v3/associations/{from_object_type}/{to_object_type}/batch/read",
        {"inputs": inputs},
    )


def associations_v3_batch_archive(
    from_object_type: str,
    to_object_type: str,
    inputs: List[Dict[str, Any]],
) -> Dict[str, Any] | list | str:
    """Batch archive associations (v3)."""
    return hubspot_post(
        f"/crm/v3/associations/{from_object_type}/{to_object_type}/batch/archive",
        {"inputs": inputs},
    )


def associations_v4_labels(from_object_type: str, to_object_type: str) -> Dict[str, Any] | list | str:
    """List association labels/types between objects (v4)."""
    return hubspot_get(f"/crm/v4/associations/{from_object_type}/{to_object_type}/labels")


def associations_v4_associate_default(
    from_object_type: str,
    from_object_id: str,
    to_object_type: str,
    to_object_id: str,
) -> Dict[str, Any] | list | str:
    """Create a default (unlabeled) association between two records (v4)."""
    return hubspot_put(
        f"/crm/v4/objects/{from_object_type}/{from_object_id}/associations/default/{to_object_type}/{to_object_id}",
        None,
    )


def associations_v4_get_associations(
    from_object_type: str,
    object_id: str,
    to_object_type: str,
) -> Dict[str, Any] | list | str:
    """Get associations of a specific type for a record (v4)."""
    return hubspot_get(f"/crm/v4/objects/{from_object_type}/{object_id}/associations/{to_object_type}")


def associations_v4_delete_all_between(
    object_type: str,
    object_id: str,
    to_object_type: str,
    to_object_id: str,
) -> Dict[str, Any] | list | str:
    """Delete all associations between two records (v4)."""
    return hubspot_delete(f"/crm/v4/objects/{object_type}/{object_id}/associations/{to_object_type}/{to_object_id}")


def associations_v4_batch_read(
    from_object_type: str,
    to_object_type: str,
    inputs: List[Dict[str, Any]],
) -> Dict[str, Any] | list | str:
    """Batch read associated records (v4)."""
    return hubspot_post(
        f"/crm/v4/associations/{from_object_type}/{to_object_type}/batch/read",
        {"inputs": inputs},
    )


def associations_v4_batch_associate_default(
    from_object_type: str,
    to_object_type: str,
    inputs: List[Dict[str, Any]],
) -> Dict[str, Any] | list | str:
    """Batch create default associations (v4)."""
    return hubspot_post(
        f"/crm/v4/associations/{from_object_type}/{to_object_type}/batch/associate/default",
        {"inputs": inputs},
    )
