"""
eBay Sell Logistics API tools.
Covers: shipment quotes, shipment creation, shipping rates, carrier accounts.
"""

from typing import Optional
from auth import api_get, api_post, api_delete


# ---------------------------------------------------------------------------
# Shipment Quotes
# ---------------------------------------------------------------------------

def create_shipment_quote(body: dict) -> dict:
    """
    Request a shipment quote (rate shopping).

    body fields:
      packageSpecification: dict with dimensions and weight
      shippingAddressFrom: dict with address fields
      shippingAddressTo: dict with address fields
      orders: list of dicts with orderId and orderLineItems
    """
    return api_post("/sell/logistics/v1_beta/shipment_quote", body=body)


# ---------------------------------------------------------------------------
# Shipments
# ---------------------------------------------------------------------------

def create_shipment(body: dict) -> dict:
    """
    Create a shipment (purchase a label).

    body fields:
      packageSpecification: dict with dimensions and weight
      rateId: str (from shipment quote)
      returnTo: dict with address
      shippingAddressFrom: dict
      shippingAddressTo: dict
      orders: list of dicts with orderId and orderLineItems
    """
    return api_post("/sell/logistics/v1_beta/shipment", body=body)


def get_shipment(shipment_id: str) -> dict:
    """Get a shipment by ID."""
    return api_get(f"/sell/logistics/v1_beta/shipment/{shipment_id}")


def cancel_shipment(shipment_id: str) -> dict:
    """Cancel a shipment and void the label."""
    return api_post(f"/sell/logistics/v1_beta/shipment/{shipment_id}/cancel")


def download_label_file(shipment_id: str) -> dict:
    """Get the label download URL for a shipment."""
    return api_get(f"/sell/logistics/v1_beta/shipment/{shipment_id}/download_label_file")
