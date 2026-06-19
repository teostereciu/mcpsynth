"""Tools for HubSpot CRM Properties (v3)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import hubspot_request


def properties_list(object_type: str, *, data_sensitivity: Optional[str] = None) -> Dict[str, Any]:
    """List properties for an object type.

    GET /crm/v3/properties/{objectType}

    object_type examples: 'contacts', 'companies', 'deals', 'tickets'
    data_sensitivity: 'sensitive' to include sensitive properties (Enterprise only)
    """
    params: Dict[str, Any] = {}
    if data_sensitivity is not None:
        params["dataSensitivity"] = data_sensitivity
    return hubspot_request("GET", f"/crm/v3/properties/{object_type}", params=params)


def properties_get(object_type: str, property_name: str) -> Dict[str, Any]:
    """Get a property definition.

    GET /crm/v3/properties/{objectType}/{propertyName}
    """
    return hubspot_request("GET", f"/crm/v3/properties/{object_type}/{property_name}")


def properties_create(object_type: str, definition: Dict[str, Any]) -> Dict[str, Any]:
    """Create a property.

    POST /crm/v3/properties/{objectType}
    """
    return hubspot_request("POST", f"/crm/v3/properties/{object_type}", json=definition)


def properties_update(object_type: str, property_name: str, definition_patch: Dict[str, Any]) -> Dict[str, Any]:
    """Update a property.

    PATCH /crm/v3/properties/{objectType}/{propertyName}
    """
    return hubspot_request("PATCH", f"/crm/v3/properties/{object_type}/{property_name}", json=definition_patch)


def properties_archive(object_type: str, property_name: str) -> Dict[str, Any]:
    """Archive (delete) a property.

    DELETE /crm/v3/properties/{objectType}/{propertyName}
    """
    return hubspot_request("DELETE", f"/crm/v3/properties/{object_type}/{property_name}")
