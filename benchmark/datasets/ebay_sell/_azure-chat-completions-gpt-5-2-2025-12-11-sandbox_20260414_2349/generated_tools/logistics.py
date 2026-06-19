from typing import Any, Dict

from . import client as _shared
from .client import SCOPE_LOGISTICS
from . import mcp

API = "/sell/logistics/v1"


@mcp.tool()
def logistics_create_shipping_quote(
    request: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /shipping_quote"""
    return _shared.client.request(
        "POST",
        API,
        "/shipping_quote",
        scope=SCOPE_LOGISTICS,
        marketplace_id=marketplace_id,
        json=request,
    )


@mcp.tool()
def logistics_get_shipping_quote(
    shipping_quote_id: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /shipping_quote/{shippingQuoteId}"""
    return _shared.client.request(
        "GET",
        API,
        f"/shipping_quote/{shipping_quote_id}",
        scope=SCOPE_LOGISTICS,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def logistics_create_from_shipping_quote(
    request: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /shipment"""
    return _shared.client.request(
        "POST",
        API,
        "/shipment",
        scope=SCOPE_LOGISTICS,
        marketplace_id=marketplace_id,
        json=request,
    )


@mcp.tool()
def logistics_get_shipment(
    shipment_id: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /shipment/{shipmentId}"""
    return _shared.client.request(
        "GET",
        API,
        f"/shipment/{shipment_id}",
        scope=SCOPE_LOGISTICS,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def logistics_cancel_shipment(
    shipment_id: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /shipment/{shipmentId}/cancel"""
    return _shared.client.request(
        "POST",
        API,
        f"/shipment/{shipment_id}/cancel",
        scope=SCOPE_LOGISTICS,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def logistics_download_label_file(
    shipment_id: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /shipment/{shipmentId}/download_label_file"""
    return _shared.client.request(
        "GET",
        API,
        f"/shipment/{shipment_id}/download_label_file",
        scope=SCOPE_LOGISTICS,
        marketplace_id=marketplace_id,
        accept="application/octet-stream",
    )
