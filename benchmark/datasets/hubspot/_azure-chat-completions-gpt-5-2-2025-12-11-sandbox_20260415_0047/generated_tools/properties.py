"""Tools for HubSpot CRM Properties API (v3)."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import hubspot_get, hubspot_post


def properties_list(object_type: str, *, data_sensitivity: Optional[str] = None) -> Dict[str, Any] | list | str:
    """List properties for an object type (e.g., 'contacts', 'companies')."""
    params: Dict[str, Any] = {}
    if data_sensitivity is not None:
        params["dataSensitivity"] = data_sensitivity
    return hubspot_get(f"/crm/v3/properties/{object_type}", params)


def properties_get(object_type: str, property_name: str) -> Dict[str, Any] | list | str:
    return hubspot_get(f"/crm/v3/properties/{object_type}/{property_name}")


def properties_create(object_type: str, definition: Dict[str, Any]) -> Dict[str, Any] | list | str:
    """Create a property for an object type."""
    return hubspot_post(f"/crm/v3/properties/{object_type}", definition)
