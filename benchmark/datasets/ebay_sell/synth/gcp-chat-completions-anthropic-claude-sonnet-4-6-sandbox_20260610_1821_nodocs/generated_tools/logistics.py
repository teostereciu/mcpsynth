"""
eBay Sell Logistics API tools.
Covers: shipping quotes, shipment creation, and label management.
"""

from mcp.server.fastmcp import FastMCP
from .auth import ebay_request

mcp = FastMCP("ebay-logistics")

# ---------------------------------------------------------------------------
# Shipping Quotes
# ---------------------------------------------------------------------------

@mcp.tool()
def create_shipping_quote(quote_request: dict) -> dict:
    """
    Request shipping quotes for a package.

    Args:
        quote_request: Quote request object with:
                       - orderId: The eBay order ID.
                       - packageSpecification: Package dimensions and weight.
                       - shippingAddress: Destination address.
                       Example: {
                         "orderId": "12-34567-89012",
                         "packageSpecification": {
                           "dimensions": {
                             "height": {"value": "5", "unit": "INCH"},
                             "length": {"value": "10", "unit": "INCH"},
                             "width": {"value": "8", "unit": "INCH"}
                           },
                           "weight": {"value": "2", "unit": "POUND"}
                         }
                       }
    """
    return ebay_request(
        "POST",
        "/sell/logistics/v1_beta/shipping_quote",
        json=quote_request,
    )


@mcp.tool()
def get_shipping_quote(shipping_quote_id: str) -> dict:
    """
    Retrieve a previously created shipping quote.

    Args:
        shipping_quote_id: The unique identifier of the shipping quote.
    """
    return ebay_request(
        "GET",
        f"/sell/logistics/v1_beta/shipping_quote/{shipping_quote_id}",
    )


# ---------------------------------------------------------------------------
# Shipments
# ---------------------------------------------------------------------------

@mcp.tool()
def create_shipment(shipment: dict) -> dict:
    """
    Create a shipment and purchase a shipping label using a shipping quote.

    Args:
        shipment: Shipment object with:
                  - shippingQuoteId: ID from create_shipping_quote.
                  - rateId: The selected rate ID from the quote.
                  - returnTo: Return address object.
                  Example: {
                    "shippingQuoteId": "quote-id",
                    "rateId": "rate-id",
                    "returnTo": {
                      "fullName": "John Seller",
                      "contactAddress": {
                        "addressLine1": "123 Main St",
                        "city": "San Jose",
                        "stateOrProvince": "CA",
                        "postalCode": "95131",
                        "countryCode": "US"
                      }
                    }
                  }
    """
    return ebay_request(
        "POST",
        "/sell/logistics/v1_beta/shipment",
        json=shipment,
    )


@mcp.tool()
def get_shipment(shipment_id: str) -> dict:
    """
    Retrieve a specific shipment by its ID.

    Args:
        shipment_id: The unique identifier of the shipment.
    """
    return ebay_request(
        "GET",
        f"/sell/logistics/v1_beta/shipment/{shipment_id}",
    )


@mcp.tool()
def cancel_shipment(shipment_id: str) -> dict:
    """
    Cancel a shipment and void the shipping label.

    Args:
        shipment_id: The unique identifier of the shipment to cancel.
    """
    return ebay_request(
        "POST",
        f"/sell/logistics/v1_beta/shipment/{shipment_id}/cancel",
    )


@mcp.tool()
def download_label_file(shipment_id: str) -> dict:
    """
    Download the shipping label file for a shipment.

    Args:
        shipment_id: The unique identifier of the shipment.
    """
    return ebay_request(
        "GET",
        f"/sell/logistics/v1_beta/shipment/{shipment_id}/download_label_file",
    )
