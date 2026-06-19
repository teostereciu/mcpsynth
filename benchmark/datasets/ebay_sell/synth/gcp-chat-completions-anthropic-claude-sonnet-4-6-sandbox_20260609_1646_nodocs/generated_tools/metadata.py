"""
eBay Sell Metadata API tools.
Covers: marketplace return policies, sales tax jurisdictions,
        automotive compatibility properties, hazmat substances.
"""

from typing import Optional
from auth import api_get


def get_return_policies_metadata(marketplace_id: str) -> dict:
    """Get the return policy metadata (allowed values) for a marketplace."""
    return api_get(f"/sell/metadata/v1/marketplace/{marketplace_id}/get_return_policies")


def get_listing_structure_policies(
    marketplace_id: str,
    filter: Optional[str] = None,
) -> dict:
    """Get listing structure policies for a marketplace."""
    params: dict = {"marketplace_id": marketplace_id}
    if filter:
        params["filter"] = filter
    return api_get("/sell/metadata/v1/listing_structure_policy", params=params)


def get_negotiated_price_policies(marketplace_id: str) -> dict:
    """Get negotiated price policies for a marketplace."""
    return api_get("/sell/metadata/v1/negotiated_price_policy",
                   params={"marketplace_id": marketplace_id})


def get_item_condition_policies(
    marketplace_id: str,
    filter: Optional[str] = None,
) -> dict:
    """Get item condition policies (allowed conditions per category) for a marketplace."""
    params: dict = {"marketplace_id": marketplace_id}
    if filter:
        params["filter"] = filter
    return api_get("/sell/metadata/v1/item_condition_policy", params=params)


def get_automotive_parts_compatibility_policies(
    marketplace_id: str,
    filter: Optional[str] = None,
) -> dict:
    """Get automotive parts compatibility policies for a marketplace."""
    params: dict = {"marketplace_id": marketplace_id}
    if filter:
        params["filter"] = filter
    return api_get("/sell/metadata/v1/automotive_parts_compatibility_policy", params=params)


def get_hazmat_substances(
    marketplace_id: str,
    locale: Optional[str] = None,
) -> dict:
    """Get hazardous material (hazmat) substance information for a marketplace."""
    params: dict = {"marketplace_id": marketplace_id}
    if locale:
        params["locale"] = locale
    return api_get("/sell/metadata/v1/hazmat/substance", params=params)


def get_extended_producer_responsibility_policies(
    marketplace_id: str,
    filter: Optional[str] = None,
) -> dict:
    """Get Extended Producer Responsibility (EPR) policies for a marketplace."""
    params: dict = {"marketplace_id": marketplace_id}
    if filter:
        params["filter"] = filter
    return api_get("/sell/metadata/v1/extended_producer_responsibility_policy", params=params)
