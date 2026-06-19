"""
eBay Sell Logistics API tools.
Covers: shipping quotes, shipment creation, and label management.
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get, api_post, api_delete

mcp = FastMCP("ebay-logistics")


@mcp.tool()
def create_shipping_quote(order_id: str,
                           package_specification: dict,
                           ship_from: dict,
                           ship_to: dict | None = None) -> dict:
    """
    Create a shipping quote to get available shipping rates.

    Args:
        order_id: The eBay order ID to ship.
        package_specification: Dict with dimensions and weight.
        ship_from: Dict with contact name and address.
        ship_to: Optional override for ship-to address (defaults to buyer address).
    """
    body: dict = {
        "orderId": order_id,
        "packageSpecification": package_specification,
        "shipFrom": ship_from,
    }
    if ship_to:
        body["shipTo"] = ship_to
    return api_post("/sell/logistics/v1_beta/shipping_quote", body=body)


@mcp.tool()
def get_shipping_quote(shipping_quote_id: str) -> dict:
    """
    Retrieve a shipping quote by ID.

    Args:
        shipping_quote_id: The shipping quote ID.
    """
    return api_get(f"/sell/logistics/v1_beta/shipping_quote/{shipping_quote_id}")


@mcp.tool()
def create_shipment(shipping_quote_id: str,
                    rate_id: str,
                    return_to: dict | None = None,
                    additional_options: list[dict] | None = None) -> dict:
    """
    Create a shipment and purchase a shipping label using a quote rate.

    Args:
        shipping_quote_id: The shipping quote ID.
        rate_id: The selected rate ID from the quote.
        return_to: Optional return address override.
        additional_options: Optional list of additional service options.
    """
    body: dict = {
        "shippingQuoteId": shipping_quote_id,
        "rateId": rate_id,
    }
    if return_to:
        body["returnTo"] = return_to
    if additional_options:
        body["additionalOptions"] = additional_options
    return api_post("/sell/logistics/v1_beta/shipment", body=body)


@mcp.tool()
def get_shipment(shipment_id: str) -> dict:
    """
    Retrieve a shipment by ID.

    Args:
        shipment_id: The shipment ID.
    """
    return api_get(f"/sell/logistics/v1_beta/shipment/{shipment_id}")


@mcp.tool()
def cancel_shipment(shipment_id: str) -> dict:
    """
    Cancel a shipment and void the shipping label.

    Args:
        shipment_id: The shipment ID to cancel.
    """
    return api_post(f"/sell/logistics/v1_beta/shipment/{shipment_id}/cancel")


@mcp.tool()
def download_label_file(shipment_id: str) -> dict:
    """
    Download the shipping label for a shipment.

    Args:
        shipment_id: The shipment ID.
    """
    import requests
    from .auth import auth_headers, get_base_url
    url = get_base_url() + f"/sell/logistics/v1_beta/shipment/{shipment_id}/download_label_file"
    try:
        r = requests.get(url, headers=auth_headers(), timeout=30)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {
            "content_type": r.headers.get("Content-Type"),
            "size_bytes": len(r.content),
            "label_base64": __import__("base64").b64encode(r.content).decode(),
        }
    except Exception as e:
        return {"error": str(e)}
