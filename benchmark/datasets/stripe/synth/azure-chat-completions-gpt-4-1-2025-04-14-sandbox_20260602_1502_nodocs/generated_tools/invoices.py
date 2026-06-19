import os
import requests
from typing import Optional, Dict, Any

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {"Authorization": f"Bearer {STRIPE_API_KEY}"}

def create_invoice(customer: str, **kwargs) -> Dict[str, Any]:
    """
    Create an Invoice object.
    Args:
        customer: Customer ID to invoice.
        kwargs: Additional Stripe parameters (e.g. auto_advance, collection_method, etc.)
    Returns:
        JSON response from Stripe or error dict.
    """
    data = {"customer": customer}
    data.update(kwargs)
    try:
        resp = requests.post(f"{BASE_URL}/invoices", data=data, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def retrieve_invoice(invoice_id: str) -> Dict[str, Any]:
    """
    Retrieve an Invoice object.
    Args:
        invoice_id: The ID of the Invoice.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.get(f"{BASE_URL}/invoices/{invoice_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def finalize_invoice(invoice_id: str) -> Dict[str, Any]:
    """
    Finalize an Invoice object.
    Args:
        invoice_id: The ID of the Invoice.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.post(f"{BASE_URL}/invoices/{invoice_id}/finalize", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
