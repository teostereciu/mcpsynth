from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

API_ROOT = "/sell/inventory/v1"
SCOPE = "https://api.ebay.com/oauth/api_scope/sell.inventory"


def register(mcp):
    @mcp.tool()
    def inventory_create_or_replace_inventory_item(
        sku: str,
        inventory_item: Dict[str, Any],
        *,
        content_language: str = "en-US",
    ) -> Dict[str, Any]:
        """PUT /inventory_item/{sku} - Create or replace an inventory item."""
        return request_json(
            "PUT",
            API_ROOT,
            f"/inventory_item/{sku}",
            scope=SCOPE,
            headers={
                "Content-Type": "application/json",
                "Content-Language": content_language,
            },
            json_body=inventory_item,
        )

    @mcp.tool()
    def inventory_get_inventory_item(sku: str) -> Dict[str, Any]:
        """GET /inventory_item/{sku} - Get an inventory item."""
        return request_json("GET", API_ROOT, f"/inventory_item/{sku}", scope=SCOPE)

    @mcp.tool()
    def inventory_delete_inventory_item(sku: str) -> Dict[str, Any]:
        """DELETE /inventory_item/{sku} - Delete an inventory item."""
        return request_json("DELETE", API_ROOT, f"/inventory_item/{sku}", scope=SCOPE)

    @mcp.tool()
    def inventory_get_inventory_items(
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """GET /inventory_item - Get inventory items."""
        params: Dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return request_json("GET", API_ROOT, "/inventory_item", scope=SCOPE, params=params or None)

    @mcp.tool()
    def inventory_create_offer(offer: Dict[str, Any]) -> Dict[str, Any]:
        """POST /offer - Create an offer."""
        return request_json(
            "POST",
            API_ROOT,
            "/offer",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=offer,
        )

    @mcp.tool()
    def inventory_update_offer(offer_id: str, offer: Dict[str, Any]) -> Dict[str, Any]:
        """PUT /offer/{offerId} - Update an offer."""
        return request_json(
            "PUT",
            API_ROOT,
            f"/offer/{offer_id}",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=offer,
        )

    @mcp.tool()
    def inventory_get_offer(offer_id: str) -> Dict[str, Any]:
        """GET /offer/{offerId} - Get an offer."""
        return request_json("GET", API_ROOT, f"/offer/{offer_id}", scope=SCOPE)

    @mcp.tool()
    def inventory_get_offers(
        *,
        sku: Optional[str] = None,
        marketplace_id: Optional[str] = None,
        format: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """GET /offer - Get offers (optionally by SKU)."""
        params: Dict[str, Any] = {}
        if sku is not None:
            params["sku"] = sku
        if marketplace_id is not None:
            params["marketplace_id"] = marketplace_id
        if format is not None:
            params["format"] = format
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return request_json("GET", API_ROOT, "/offer", scope=SCOPE, params=params or None)

    @mcp.tool()
    def inventory_delete_offer(offer_id: str) -> Dict[str, Any]:
        """DELETE /offer/{offerId} - Delete an offer."""
        return request_json("DELETE", API_ROOT, f"/offer/{offer_id}", scope=SCOPE)

    @mcp.tool()
    def inventory_publish_offer(offer_id: str) -> Dict[str, Any]:
        """POST /offer/{offerId}/publish - Publish an offer."""
        return request_json(
            "POST",
            API_ROOT,
            f"/offer/{offer_id}/publish",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body={},
        )

    @mcp.tool()
    def inventory_withdraw_offer(offer_id: str) -> Dict[str, Any]:
        """POST /offer/{offerId}/withdraw - Withdraw an offer."""
        return request_json(
            "POST",
            API_ROOT,
            f"/offer/{offer_id}/withdraw",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body={},
        )

    @mcp.tool()
    def inventory_bulk_update_price_quantity(payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /bulk_update_price_quantity - Bulk update price/quantity."""
        return request_json(
            "POST",
            API_ROOT,
            "/bulk_update_price_quantity",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def inventory_create_inventory_location(merchant_location_key: str, location: Dict[str, Any]) -> Dict[str, Any]:
        """POST /location/{merchantLocationKey} - Create an inventory location."""
        return request_json(
            "POST",
            API_ROOT,
            f"/location/{merchant_location_key}",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=location,
        )

    @mcp.tool()
    def inventory_get_inventory_locations(
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """GET /location - Get inventory locations."""
        params: Dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return request_json("GET", API_ROOT, "/location", scope=SCOPE, params=params or None)

    @mcp.tool()
    def inventory_get_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
        """GET /location/{merchantLocationKey} - Get an inventory location."""
        return request_json("GET", API_ROOT, f"/location/{merchant_location_key}", scope=SCOPE)

    @mcp.tool()
    def inventory_update_inventory_location(merchant_location_key: str, location_details: Dict[str, Any]) -> Dict[str, Any]:
        """POST /location/{merchantLocationKey}/update_location_details - Update location details."""
        return request_json(
            "POST",
            API_ROOT,
            f"/location/{merchant_location_key}/update_location_details",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=location_details,
        )

    @mcp.tool()
    def inventory_disable_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
        """POST /location/{merchantLocationKey}/disable - Disable a location."""
        return request_json(
            "POST",
            API_ROOT,
            f"/location/{merchant_location_key}/disable",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body={},
        )

    @mcp.tool()
    def inventory_enable_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
        """POST /location/{merchantLocationKey}/enable - Enable a location."""
        return request_json(
            "POST",
            API_ROOT,
            f"/location/{merchant_location_key}/enable",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body={},
        )

    @mcp.tool()
    def inventory_delete_inventory_location(merchant_location_key: str) -> Dict[str, Any]:
        """DELETE /location/{merchantLocationKey} - Delete a location."""
        return request_json("DELETE", API_ROOT, f"/location/{merchant_location_key}", scope=SCOPE)

    @mcp.tool()
    def inventory_create_or_replace_sku_location_mapping(listing_id: str, sku: str, locations: Dict[str, Any]) -> Dict[str, Any]:
        """PUT /listing/{listingId}/sku/{sku}/locations - Create/replace SKU location mapping."""
        return request_json(
            "PUT",
            API_ROOT,
            f"/listing/{listing_id}/sku/{sku}/locations",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=locations,
        )

    @mcp.tool()
    def inventory_get_sku_location_mapping(listing_id: str, sku: str) -> Dict[str, Any]:
        """GET /listing/{listingId}/sku/{sku}/locations - Get SKU location mapping."""
        return request_json("GET", API_ROOT, f"/listing/{listing_id}/sku/{sku}/locations", scope=SCOPE)

    @mcp.tool()
    def inventory_delete_sku_location_mapping(listing_id: str, sku: str) -> Dict[str, Any]:
        """DELETE /listing/{listingId}/sku/{sku}/locations - Delete SKU location mapping."""
        return request_json("DELETE", API_ROOT, f"/listing/{listing_id}/sku/{sku}/locations", scope=SCOPE)
