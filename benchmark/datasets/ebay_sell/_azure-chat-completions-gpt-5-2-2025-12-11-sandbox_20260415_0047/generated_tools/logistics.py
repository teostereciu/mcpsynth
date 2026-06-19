from __future__ import annotations

from typing import Any, Dict

from .http import request_json

API_ROOT = "/sell/logistics/v1"
SCOPE = "https://api.ebay.com/oauth/api_scope/sell.logistics"


def register(mcp):
    @mcp.tool()
    def logistics_create_shipping_quote(marketplace_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /shipping_quote - Create a shipping quote."""
        return request_json(
            "POST",
            API_ROOT,
            "/shipping_quote",
            scope=SCOPE,
            marketplace_id=marketplace_id,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def logistics_get_shipping_quote(shipping_quote_id: str, marketplace_id: str) -> Dict[str, Any]:
        """GET /shipping_quote/{shippingQuoteId} - Get a shipping quote."""
        return request_json(
            "GET",
            API_ROOT,
            f"/shipping_quote/{shipping_quote_id}",
            scope=SCOPE,
            marketplace_id=marketplace_id,
        )

    @mcp.tool()
    def logistics_create_from_shipping_quote(marketplace_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /shipment/create_from_shipping_quote - Create shipment from quote."""
        return request_json(
            "POST",
            API_ROOT,
            "/shipment/create_from_shipping_quote",
            scope=SCOPE,
            marketplace_id=marketplace_id,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def logistics_get_shipment(shipment_id: str, marketplace_id: str) -> Dict[str, Any]:
        """GET /shipment/{shipmentId} - Get shipment."""
        return request_json(
            "GET",
            API_ROOT,
            f"/shipment/{shipment_id}",
            scope=SCOPE,
            marketplace_id=marketplace_id,
        )

    @mcp.tool()
    def logistics_cancel_shipment(shipment_id: str, marketplace_id: str) -> Dict[str, Any]:
        """POST /shipment/{shipmentId}/cancel - Cancel shipment."""
        return request_json(
            "POST",
            API_ROOT,
            f"/shipment/{shipment_id}/cancel",
            scope=SCOPE,
            marketplace_id=marketplace_id,
            headers={"Content-Type": "application/json"},
            json_body={},
        )

    @mcp.tool()
    def logistics_download_label_file(shipment_id: str, marketplace_id: str) -> Dict[str, Any]:
        """GET /shipment/{shipmentId}/download_label_file - Download label file."""
        return request_json(
            "GET",
            API_ROOT,
            f"/shipment/{shipment_id}/download_label_file",
            scope=SCOPE,
            marketplace_id=marketplace_id,
        )
