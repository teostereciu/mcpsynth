from typing import Any, Dict, Optional

from . import client as _shared
from .client import SCOPE_INVENTORY
from . import mcp

API = "/sell/inventory/v1"


@mcp.tool()
def inventory_create_or_replace_inventory_item(
    sku: str,
    inventory_item: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
    content_language: str = "en-US",
) -> Any:
    """PUT /inventory_item/{sku}

    Creates a new inventory item record or replaces an existing one.
    """
    return _shared.client.request(
        "PUT",
        API,
        f"/inventory_item/{sku}",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
        json=inventory_item,
        headers={"Content-Language": content_language},
    )


@mcp.tool()
def inventory_get_inventory_item(
    sku: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /inventory_item/{sku}"""
    return _shared.client.request(
        "GET",
        API,
        f"/inventory_item/{sku}",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def inventory_delete_inventory_item(
    sku: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """DELETE /inventory_item/{sku}"""
    return _shared.client.request(
        "DELETE",
        API,
        f"/inventory_item/{sku}",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def inventory_get_inventory_items(
    *,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /inventory_item

    Retrieves a paginated list of inventory items.
    """
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return _shared.client.request(
        "GET",
        API,
        "/inventory_item",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
        params=params or None,
    )


@mcp.tool()
def inventory_create_offer(
    offer: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /offer

    Creates an offer for an inventory item.
    """
    return _shared.client.request(
        "POST",
        API,
        "/offer",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
        json=offer,
    )


@mcp.tool()
def inventory_update_offer(
    offer_id: str,
    offer: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """PUT /offer/{offerId}"""
    return _shared.client.request(
        "PUT",
        API,
        f"/offer/{offer_id}",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
        json=offer,
    )


@mcp.tool()
def inventory_get_offer(
    offer_id: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /offer/{offerId}"""
    return _shared.client.request(
        "GET",
        API,
        f"/offer/{offer_id}",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def inventory_get_offers(
    *,
    sku: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Any:
    """GET /offer

    Retrieves offers; can filter by sku.
    """
    params: Dict[str, Any] = {}
    if sku is not None:
        params["sku"] = sku
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return _shared.client.request(
        "GET",
        API,
        "/offer",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
        params=params or None,
    )


@mcp.tool()
def inventory_publish_offer(
    offer_id: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /offer/{offerId}/publish"""
    return _shared.client.request(
        "POST",
        API,
        f"/offer/{offer_id}/publish",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def inventory_withdraw_offer(
    offer_id: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /offer/{offerId}/withdraw"""
    return _shared.client.request(
        "POST",
        API,
        f"/offer/{offer_id}/withdraw",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def inventory_bulk_update_price_quantity(
    requests: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /bulk_update_price_quantity"""
    return _shared.client.request(
        "POST",
        API,
        "/bulk_update_price_quantity",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
        json=requests,
    )


@mcp.tool()
def inventory_create_inventory_location(
    merchant_location_key: str,
    location: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /location/{merchantLocationKey}"""
    return _shared.client.request(
        "POST",
        API,
        f"/location/{merchant_location_key}",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
        json=location,
    )


@mcp.tool()
def inventory_update_inventory_location(
    merchant_location_key: str,
    location: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """PUT /location/{merchantLocationKey}"""
    return _shared.client.request(
        "PUT",
        API,
        f"/location/{merchant_location_key}",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
        json=location,
    )


@mcp.tool()
def inventory_get_inventory_location(
    merchant_location_key: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /location/{merchantLocationKey}"""
    return _shared.client.request(
        "GET",
        API,
        f"/location/{merchant_location_key}",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def inventory_get_inventory_locations(
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /location"""
    return _shared.client.request(
        "GET",
        API,
        "/location",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def inventory_enable_inventory_location(
    merchant_location_key: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /location/{merchantLocationKey}/enable"""
    return _shared.client.request(
        "POST",
        API,
        f"/location/{merchant_location_key}/enable",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def inventory_disable_inventory_location(
    merchant_location_key: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /location/{merchantLocationKey}/disable"""
    return _shared.client.request(
        "POST",
        API,
        f"/location/{merchant_location_key}/disable",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def inventory_create_or_replace_sku_location_mapping(
    sku: str,
    mapping: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """PUT /sku/{sku}/location"""
    return _shared.client.request(
        "PUT",
        API,
        f"/sku/{sku}/location",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
        json=mapping,
    )


@mcp.tool()
def inventory_get_sku_location_mapping(
    sku: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /sku/{sku}/location"""
    return _shared.client.request(
        "GET",
        API,
        f"/sku/{sku}/location",
        scope=SCOPE_INVENTORY,
        marketplace_id=marketplace_id,
    )
