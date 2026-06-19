from typing import Any, Dict, Optional

from .http import hubspot_request


def properties_create(object_type: str, definition: Dict[str, Any]) -> Dict[str, Any]:
    return hubspot_request("POST", f"/crm/v3/properties/{object_type}", json_body=definition)


def properties_list(object_type: str, *, data_sensitivity: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if data_sensitivity is not None:
        params["dataSensitivity"] = data_sensitivity
    return hubspot_request("GET", f"/crm/v3/properties/{object_type}", params=params)


def properties_get(object_type: str, property_name: str) -> Dict[str, Any]:
    return hubspot_request("GET", f"/crm/v3/properties/{object_type}/{property_name}")


def properties_update(object_type: str, property_name: str, updates: Dict[str, Any]) -> Dict[str, Any]:
    return hubspot_request("PATCH", f"/crm/v3/properties/{object_type}/{property_name}", json_body=updates)


def properties_archive(object_type: str, property_name: str) -> Dict[str, Any]:
    return hubspot_request("DELETE", f"/crm/v3/properties/{object_type}/{property_name}")
