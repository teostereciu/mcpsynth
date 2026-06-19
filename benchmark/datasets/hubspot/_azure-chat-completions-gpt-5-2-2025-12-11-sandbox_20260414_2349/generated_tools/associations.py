"""Tools for HubSpot CRM Associations (v3 and v4).

Includes:
- v3 object association endpoints (simple, typeId in URL)
- v4 association labels and batch association endpoints
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import hubspot_request


def associations_v3_create(
    from_object_type: str,
    from_object_id: str,
    to_object_type: str,
    to_object_id: str,
    association_type_id: str,
) -> Dict[str, Any]:
    """Create an association using v3 objects endpoint.

    PUT /crm/v3/objects/{fromObjectType}/{fromObjectId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}

    Example association_type_id values (HubSpot-defined):
    - contact -> company (primary): 1
    - deal -> contact: 3
    - contact -> deal: 4
    """
    return hubspot_request(
        "PUT",
        f"/crm/v3/objects/{from_object_type}/{from_object_id}/associations/{to_object_type}/{to_object_id}/{association_type_id}",
    )


def associations_v3_delete(
    from_object_type: str,
    from_object_id: str,
    to_object_type: str,
    to_object_id: str,
    association_type_id: str,
) -> Dict[str, Any]:
    """Delete an association using v3 objects endpoint.

    DELETE /crm/v3/objects/{fromObjectType}/{fromObjectId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}
    """
    return hubspot_request(
        "DELETE",
        f"/crm/v3/objects/{from_object_type}/{from_object_id}/associations/{to_object_type}/{to_object_id}/{association_type_id}",
    )


def associations_v4_labels(from_object_type: str, to_object_type: str) -> Dict[str, Any]:
    """List association labels between two object types.

    GET /crm/v4/associations/{fromObjectType}/{toObjectType}/labels
    """
    return hubspot_request("GET", f"/crm/v4/associations/{from_object_type}/{to_object_type}/labels")


def associations_v4_batch_associate_default(
    from_object_type: str,
    to_object_type: str,
    inputs: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Batch associate records with the default (unlabeled) association.

    POST /crm/v4/associations/{fromObjectType}/{toObjectType}/batch/associate/default

    inputs: [{"from": {"id": "..."}, "to": {"id": "..."}}]
    """
    return hubspot_request(
        "POST",
        f"/crm/v4/associations/{from_object_type}/{to_object_type}/batch/associate/default",
        json={"inputs": inputs},
    )


def associations_v4_batch_create_labeled(
    from_object_type: str,
    to_object_type: str,
    inputs: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Batch create labeled associations.

    POST /crm/v4/associations/{fromObjectType}/{toObjectType}/batch/create

    inputs example:
    {
      "from": {"id": "1"},
      "to": {"id": "2"},
      "types": [{"associationCategory": "HUBSPOT_DEFINED", "associationTypeId": 1}]
    }
    """
    return hubspot_request(
        "POST",
        f"/crm/v4/associations/{from_object_type}/{to_object_type}/batch/create",
        json={"inputs": inputs},
    )


def associations_v4_batch_read(
    from_object_type: str,
    to_object_type: str,
    inputs: List[Dict[str, Any]],
    *,
    after: Optional[str] = None,
) -> Dict[str, Any]:
    """Batch read associations.

    POST /crm/v4/associations/{fromObjectType}/{toObjectType}/batch/read

    inputs: [{"id": "..."}, ...]
    """
    payload: Dict[str, Any] = {"inputs": inputs}
    if after is not None:
        payload["after"] = after
    return hubspot_request(
        "POST",
        f"/crm/v4/associations/{from_object_type}/{to_object_type}/batch/read",
        json=payload,
    )


def associations_v4_batch_archive(
    from_object_type: str,
    to_object_type: str,
    inputs: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Batch remove all associations between record pairs.

    POST /crm/v4/associations/{fromObjectType}/{toObjectType}/batch/archive

    inputs: [{"from": {"id": "..."}, "to": {"id": "..."}}]
    """
    return hubspot_request(
        "POST",
        f"/crm/v4/associations/{from_object_type}/{to_object_type}/batch/archive",
        json={"inputs": inputs},
    )
