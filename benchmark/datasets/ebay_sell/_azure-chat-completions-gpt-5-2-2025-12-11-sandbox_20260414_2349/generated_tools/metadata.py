from typing import Any, Dict, Optional

from . import client as _shared
from .client import SCOPE_METADATA
from . import mcp

API = "/sell/metadata/v1"


@mcp.tool()
def metadata_get_category_policies(
    marketplace_id: str,
    *,
    filter: Optional[str] = None,
    accept_language: Optional[str] = None,
) -> Any:
    """GET /marketplace/{marketplace_id}/get_category_policies"""
    headers = {"Accept-Language": accept_language} if accept_language else None
    params: Optional[Dict[str, Any]] = {"filter": filter} if filter else None
    return _shared.client.request(
        "GET",
        API,
        f"/marketplace/{marketplace_id}/get_category_policies",
        scope=SCOPE_METADATA,
        marketplace_id=marketplace_id,
        params=params,
        headers=headers,
    )


@mcp.tool()
def metadata_get_item_condition_policies(
    marketplace_id: str,
    category_id: str,
    *,
    accept_language: Optional[str] = None,
) -> Any:
    """GET /marketplace/{marketplace_id}/get_item_condition_policies"""
    headers = {"Accept-Language": accept_language} if accept_language else None
    return _shared.client.request(
        "GET",
        API,
        f"/marketplace/{marketplace_id}/get_item_condition_policies",
        scope=SCOPE_METADATA,
        marketplace_id=marketplace_id,
        params={"category_id": category_id},
        headers=headers,
    )


@mcp.tool()
def metadata_get_listing_structure_policies(
    marketplace_id: str,
    category_id: str,
    *,
    accept_language: Optional[str] = None,
) -> Any:
    """GET /marketplace/{marketplace_id}/get_listing_structure_policies"""
    headers = {"Accept-Language": accept_language} if accept_language else None
    return _shared.client.request(
        "GET",
        API,
        f"/marketplace/{marketplace_id}/get_listing_structure_policies",
        scope=SCOPE_METADATA,
        marketplace_id=marketplace_id,
        params={"category_id": category_id},
        headers=headers,
    )


@mcp.tool()
def metadata_get_listing_type_policies(
    marketplace_id: str,
    category_id: str,
    *,
    accept_language: Optional[str] = None,
) -> Any:
    """GET /marketplace/{marketplace_id}/get_listing_type_policies"""
    headers = {"Accept-Language": accept_language} if accept_language else None
    return _shared.client.request(
        "GET",
        API,
        f"/marketplace/{marketplace_id}/get_listing_type_policies",
        scope=SCOPE_METADATA,
        marketplace_id=marketplace_id,
        params={"category_id": category_id},
        headers=headers,
    )


@mcp.tool()
def metadata_get_hazardous_materials_labels(
    marketplace_id: str,
    *,
    accept_language: Optional[str] = None,
) -> Any:
    """GET /marketplace/{marketplace_id}/get_hazardous_materials_labels"""
    headers = {"Accept-Language": accept_language} if accept_language else None
    return _shared.client.request(
        "GET",
        API,
        f"/marketplace/{marketplace_id}/get_hazardous_materials_labels",
        scope=SCOPE_METADATA,
        marketplace_id=marketplace_id,
        headers=headers,
    )


@mcp.tool()
def metadata_get_currencies(*, marketplace_id: str = "EBAY_US") -> Any:
    """GET /currency"""
    return _shared.client.request(
        "GET",
        API,
        "/currency",
        scope=SCOPE_METADATA,
        marketplace_id=marketplace_id,
    )
