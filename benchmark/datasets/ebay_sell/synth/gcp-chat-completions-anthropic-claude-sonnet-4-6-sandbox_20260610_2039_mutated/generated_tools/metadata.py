"""eBay Sell Metadata API tools."""
from typing import Any, Optional
from .client import get_client


def get_item_condition_policies(market_id: str, filter: Optional[str] = None) -> dict:
    """Return item condition metadata for eBay categories on a marketplace."""
    client = get_client()
    params = {}
    if filter is not None:
        params["filter"] = filter
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_item_condition_policies", params=params)


def get_listing_structure_policies(market_id: str, filter: Optional[str] = None) -> dict:
    """Return listing structure policies (e.g., variation support) for eBay categories."""
    client = get_client()
    params = {}
    if filter is not None:
        params["filter"] = filter
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_listing_structure_policies", params=params)


def get_category_policies(market_id: str, filter: Optional[str] = None) -> dict:
    """Return eBay category policy metadata for all leaf categories on a marketplace."""
    client = get_client()
    params = {}
    if filter is not None:
        params["filter"] = filter
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_category_policies", params=params)


def get_automotive_parts_compatibility_policies(market_id: str, filter: Optional[str] = None) -> dict:
    """Return automotive parts compatibility policies for eBay categories."""
    client = get_client()
    params = {}
    if filter is not None:
        params["filter"] = filter
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_automotive_parts_compatibility_policies", params=params)


def get_hazardous_materials_labels(market_id: str, filter: Optional[str] = None) -> dict:
    """Return hazardous materials label metadata for eBay categories."""
    client = get_client()
    params = {}
    if filter is not None:
        params["filter"] = filter
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_hazardous_materials_labels", params=params)


def get_listing_type_policies(market_id: str, filter: Optional[str] = None) -> dict:
    """Return listing type policies for eBay categories on a marketplace."""
    client = get_client()
    params = {}
    if filter is not None:
        params["filter"] = filter
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_listing_type_policies", params=params)


def get_motors_listing_policies(market_id: str, filter: Optional[str] = None) -> dict:
    """Return motors listing policies for eBay categories on a marketplace."""
    client = get_client()
    params = {}
    if filter is not None:
        params["filter"] = filter
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_motors_listing_policies", params=params)


def get_currencies(market_id: str) -> dict:
    """Return the currencies supported for a specific eBay marketplace."""
    client = get_client()
    return client.request("GET", f"/sell/metadata/v1/marketplace/{market_id}/get_currencies")
