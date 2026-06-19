from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

API_ROOT = "/sell/metadata/v1"
SCOPE = "https://api.ebay.com/oauth/api_scope/sell.metadata"


def register(mcp):
    @mcp.tool()
    def metadata_get_category_policies(
        marketplace_id: str,
        *,
        filter: Optional[str] = None,
        accept_language: Optional[str] = None,
    ) -> Dict[str, Any]:
        """GET /marketplace/{marketplace_id}/get_category_policies"""
        params = {"filter": filter} if filter else None
        headers = {"Accept-Language": accept_language} if accept_language else None
        return request_json(
            "GET",
            API_ROOT,
            f"/marketplace/{marketplace_id}/get_category_policies",
            scope=SCOPE,
            params=params,
            headers=headers,
        )

    @mcp.tool()
    def metadata_get_item_condition_policies(
        marketplace_id: str,
        *,
        filter: Optional[str] = None,
        accept_language: Optional[str] = None,
    ) -> Dict[str, Any]:
        """GET /marketplace/{marketplace_id}/get_item_condition_policies"""
        params = {"filter": filter} if filter else None
        headers = {"Accept-Language": accept_language} if accept_language else None
        return request_json(
            "GET",
            API_ROOT,
            f"/marketplace/{marketplace_id}/get_item_condition_policies",
            scope=SCOPE,
            params=params,
            headers=headers,
        )

    @mcp.tool()
    def metadata_get_listing_structure_policies(marketplace_id: str, *, accept_language: Optional[str] = None) -> Dict[str, Any]:
        """GET /marketplace/{marketplace_id}/get_listing_structure_policies"""
        headers = {"Accept-Language": accept_language} if accept_language else None
        return request_json(
            "GET",
            API_ROOT,
            f"/marketplace/{marketplace_id}/get_listing_structure_policies",
            scope=SCOPE,
            headers=headers,
        )

    @mcp.tool()
    def metadata_get_listing_type_policies(marketplace_id: str, *, accept_language: Optional[str] = None) -> Dict[str, Any]:
        """GET /marketplace/{marketplace_id}/get_listing_type_policies"""
        headers = {"Accept-Language": accept_language} if accept_language else None
        return request_json(
            "GET",
            API_ROOT,
            f"/marketplace/{marketplace_id}/get_listing_type_policies",
            scope=SCOPE,
            headers=headers,
        )

    @mcp.tool()
    def metadata_get_motors_listing_policies(marketplace_id: str, *, accept_language: Optional[str] = None) -> Dict[str, Any]:
        """GET /marketplace/{marketplace_id}/get_motors_listing_policies"""
        headers = {"Accept-Language": accept_language} if accept_language else None
        return request_json(
            "GET",
            API_ROOT,
            f"/marketplace/{marketplace_id}/get_motors_listing_policies",
            scope=SCOPE,
            headers=headers,
        )

    @mcp.tool()
    def metadata_get_classified_ad_policies(marketplace_id: str, *, accept_language: Optional[str] = None) -> Dict[str, Any]:
        """GET /marketplace/{marketplace_id}/get_classified_ad_policies"""
        headers = {"Accept-Language": accept_language} if accept_language else None
        return request_json(
            "GET",
            API_ROOT,
            f"/marketplace/{marketplace_id}/get_classified_ad_policies",
            scope=SCOPE,
            headers=headers,
        )

    @mcp.tool()
    def metadata_get_currencies(marketplace_id: str, *, accept_language: Optional[str] = None) -> Dict[str, Any]:
        """GET /marketplace/{marketplace_id}/get_currencies"""
        headers = {"Accept-Language": accept_language} if accept_language else None
        return request_json(
            "GET",
            API_ROOT,
            f"/marketplace/{marketplace_id}/get_currencies",
            scope=SCOPE,
            headers=headers,
        )

    @mcp.tool()
    def metadata_get_hazardous_materials_labels(marketplace_id: str, *, accept_language: Optional[str] = None) -> Dict[str, Any]:
        """GET /marketplace/{marketplace_id}/get_hazardous_materials_labels"""
        headers = {"Accept-Language": accept_language} if accept_language else None
        return request_json(
            "GET",
            API_ROOT,
            f"/marketplace/{marketplace_id}/get_hazardous_materials_labels",
            scope=SCOPE,
            headers=headers,
        )

    @mcp.tool()
    def metadata_get_extended_producer_responsibility_policies(marketplace_id: str, *, accept_language: Optional[str] = None) -> Dict[str, Any]:
        """GET /marketplace/{marketplace_id}/get_extended_producer_responsibility_policies"""
        headers = {"Accept-Language": accept_language} if accept_language else None
        return request_json(
            "GET",
            API_ROOT,
            f"/marketplace/{marketplace_id}/get_extended_producer_responsibility_policies",
            scope=SCOPE,
            headers=headers,
        )

    # Compatibilities
    @mcp.tool()
    def metadata_get_compatibility_property_names(payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /compatibilities/get_compatibility_property_names"""
        return request_json(
            "POST",
            API_ROOT,
            "/compatibilities/get_compatibility_property_names",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def metadata_get_compatibility_property_values(payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /compatibilities/get_compatibility_property_values"""
        return request_json(
            "POST",
            API_ROOT,
            "/compatibilities/get_compatibility_property_values",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def metadata_get_multi_compatibility_property_values(payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /compatibilities/get_multi_compatibility_property_values"""
        return request_json(
            "POST",
            API_ROOT,
            "/compatibilities/get_multi_compatibility_property_values",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def metadata_get_compatibilities_by_specification(payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /compatibilities/get_compatibilities_by_specification"""
        return request_json(
            "POST",
            API_ROOT,
            "/compatibilities/get_compatibilities_by_specification",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def metadata_get_product_compatibilities(payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /compatibilities/get_product_compatibilities"""
        return request_json(
            "POST",
            API_ROOT,
            "/compatibilities/get_product_compatibilities",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )
