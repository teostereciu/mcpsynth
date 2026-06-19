"""eBay Sell Metadata API tools."""
from typing import Optional
from .client import get_client


def get_item_condition_policies(market_id: str, filter: Optional[str] = None) -> dict:
    """Return item condition metadata for eBay categories on a marketplace."""
    client = get_client()
    params = {}
    if filter:
        params["filter"] = filter
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_item_condition_policies", params=params)


def get_category_policies(market_id: str, filter: Optional[str] = None) -> dict:
    """Return eBay category policy metadata for all leaf categories on a marketplace."""
    client = get_client()
    params = {}
    if filter:
        params["filter"] = filter
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_category_policies", params=params)


def get_listing_structure_policies(market_id: str, filter: Optional[str] = None) -> dict:
    """Return listing structure policy metadata for eBay categories on a marketplace."""
    client = get_client()
    params = {}
    if filter:
        params["filter"] = filter
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_listing_structure_policies", params=params)


def get_listing_type_policies(market_id: str, filter: Optional[str] = None) -> dict:
    """Return listing type policy metadata for eBay categories on a marketplace."""
    client = get_client()
    params = {}
    if filter:
        params["filter"] = filter
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_listing_type_policies", params=params)


def get_automotive_parts_compatibility_policies(market_id: str, filter: Optional[str] = None) -> dict:
    """Return automotive parts compatibility policy metadata for eBay categories."""
    client = get_client()
    params = {}
    if filter:
        params["filter"] = filter
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_automotive_parts_compatibility_policies", params=params)


def get_motors_listing_policies(market_id: str, filter: Optional[str] = None) -> dict:
    """Return motors listing policy metadata for eBay categories on a marketplace."""
    client = get_client()
    params = {}
    if filter:
        params["filter"] = filter
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_motors_listing_policies", params=params)


def get_classified_ad_policies(market_id: str, filter: Optional[str] = None) -> dict:
    """Return classified ad policy metadata for eBay categories on a marketplace."""
    client = get_client()
    params = {}
    if filter:
        params["filter"] = filter
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_classified_ad_policies", params=params)


def get_extended_producer_responsibility_policies(market_id: str, filter: Optional[str] = None) -> dict:
    """Return extended producer responsibility policy metadata for eBay categories."""
    client = get_client()
    params = {}
    if filter:
        params["filter"] = filter
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_extended_producer_responsibility_policies", params=params)


def get_hazardous_materials_labels(market_id: str, filter: Optional[str] = None) -> dict:
    """Return hazardous materials label metadata for eBay categories on a marketplace."""
    client = get_client()
    params = {}
    if filter:
        params["filter"] = filter
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_hazardous_materials_labels", params=params)


def get_currencies(market_id: str) -> dict:
    """Return currency metadata for a specific eBay marketplace."""
    client = get_client()
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_currencies")


def get_compatibilities_by_specification(body: dict) -> dict:
    """Retrieve compatibilities by specification for automotive parts."""
    client = get_client()
    return client.request("POST", "/sell/metadata/v1/compatibilities/get_compatibilities_by_specification", json=body)


def get_compatibility_property_names(body: dict) -> dict:
    """Retrieve compatibility property names for automotive parts."""
    client = get_client()
    return client.request("POST", "/sell/metadata/v1/compatibilities/get_compatibility_property_names", json=body)


def get_compatibility_property_values(body: dict) -> dict:
    """Retrieve compatibility property values for automotive parts."""
    client = get_client()
    return client.request("POST", "/sell/metadata/v1/compatibilities/get_compatibility_property_values", json=body)


def get_product_compatibilities(body: dict) -> dict:
    """Retrieve product compatibilities for automotive parts."""
    client = get_client()
    return client.request("POST", "/sell/metadata/v1/compatibilities/get_product_compatibilities", json=body)


def get_multi_compatibility_property_values(body: dict) -> dict:
    """Retrieve multiple compatibility property values for automotive parts."""
    client = get_client()
    return client.request("POST", "/sell/metadata/v1/compatibilities/get_multi_compatibility_property_values", json=body)
