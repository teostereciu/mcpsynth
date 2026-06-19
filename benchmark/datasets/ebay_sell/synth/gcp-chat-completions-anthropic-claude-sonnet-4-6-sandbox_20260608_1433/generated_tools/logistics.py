"""eBay Sell Logistics API tools."""
from .client import get_client


def create_shipping_quote(body: dict, marketplace_id: str = "EBAY_US") -> dict:
    """Create a shipping quote containing live rates from shipping carriers."""
    client = get_client()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("POST", "/sell/logistics/v1/shipping_quote", json=body, headers=headers)


def get_shipping_quote(shipping_quote_id: str) -> dict:
    """Retrieve the complete details of a shipping quote."""
    client = get_client()
    return client.request("GET", f"/sell/logistics/v1/shipping_quote/{shipping_quote_id}")


def create_shipment_from_quote(body: dict, marketplace_id: str = "EBAY_US") -> dict:
    """Create a shipment and generate a shipping label based on a shipping quote rate."""
    client = get_client()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("POST", "/sell/logistics/v1/shipment/create_from_shipping_quote", json=body, headers=headers)


def get_shipment(shipment_id: str) -> dict:
    """Retrieve shipment details for a specified shipment ID."""
    client = get_client()
    return client.request("GET", f"/sell/logistics/v1/shipment/{shipment_id}")


def cancel_shipment(shipment_id: str) -> dict:
    """Cancel a shipment and delete the associated shipping label."""
    client = get_client()
    return client.request("POST", f"/sell/logistics/v1/shipment/{shipment_id}/cancel")


def download_label_file(shipment_id: str) -> dict:
    """Return the shipping label file for a specified shipment."""
    client = get_client()
    return client.request("GET", f"/sell/logistics/v1/shipment/{shipment_id}/download_label_file")
