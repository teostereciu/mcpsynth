"""eBay Sell Logistics API tools."""
from typing import Any, Optional
from .client import get_client


def create_shipping_quote(body: dict, marketplace_id: str = "EBAY_US") -> dict:
    """Create a shipping quote containing live carrier rates for a package."""
    client = get_client()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("POST", "/sell/logistics/v1/shipping_quote", json=body, headers=headers)


def get_shipping_quote(shipping_quote_id: str) -> dict:
    """Retrieve the complete details of a shipping quote by ID."""
    client = get_client()
    return client.request("GET", f"/sell/logistics/v1/shipping_quote/{shipping_quote_id}")


def create_shipment_from_quote(body: dict, marketplace_id: str = "EBAY_US") -> dict:
    """Create a shipment and generate a shipping label from a shipping quote."""
    client = get_client()
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    return client.request("POST", "/sell/logistics/v1/shipment/create_from_shipping_quote", json=body, headers=headers)


def get_shipment(shipment_id: str) -> dict:
    """Retrieve shipment details for the specified shipment ID."""
    client = get_client()
    return client.request("GET", f"/sell/logistics/v1/shipment/{shipment_id}")


def cancel_shipment(shipment_id: str) -> dict:
    """Cancel the shipment associated with the specified shipment ID."""
    client = get_client()
    return client.request("POST", f"/sell/logistics/v1/shipment/{shipment_id}/cancel")


def download_label_file(shipment_id: str) -> dict:
    """Download the shipping label file for the specified shipment ID."""
    client = get_client()
    return client.request("GET", f"/sell/logistics/v1/shipment/{shipment_id}/download_label_file")
