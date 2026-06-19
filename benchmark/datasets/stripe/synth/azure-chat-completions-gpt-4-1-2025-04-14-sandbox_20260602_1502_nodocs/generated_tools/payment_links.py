import os
import requests
from typing import Optional, Dict, Any

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {"Authorization": f"Bearer {STRIPE_API_KEY}"}

def create_payment_link(line_items: list, **kwargs) -> Dict[str, Any]:
    """
    Create a Payment Link.
    Args:
        line_items: List of dicts, each with at least 'price' and 'quantity'.
        kwargs: Additional Stripe parameters.
    Returns:
        JSON response from Stripe or error dict.
    """
    data = {}
    for idx, item in enumerate(line_items):
        for k, v in item.items():
            data[f"line_items[{idx}][{k}]"] = v
    data.update(kwargs)
    try:
        resp = requests.post(f"{BASE_URL}/payment_links", data=data, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def retrieve_payment_link(payment_link_id: str) -> Dict[str, Any]:
    """
    Retrieve a Payment Link.
    Args:
        payment_link_id: The ID of the Payment Link.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.get(f"{BASE_URL}/payment_links/{payment_link_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
