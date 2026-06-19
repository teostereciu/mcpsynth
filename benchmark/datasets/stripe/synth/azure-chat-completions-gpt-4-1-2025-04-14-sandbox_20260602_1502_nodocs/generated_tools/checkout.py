import os
import requests
from typing import Optional, Dict, Any

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {"Authorization": f"Bearer {STRIPE_API_KEY}"}

def create_checkout_session(success_url: str, cancel_url: str, line_items: list, mode: str = "payment", **kwargs) -> Dict[str, Any]:
    """
    Create a Checkout Session.
    Args:
        success_url: The URL to which Stripe should redirect when payment is successful.
        cancel_url: The URL to which Stripe should redirect when payment is canceled.
        line_items: List of dicts, each with at least 'price' and 'quantity'.
        mode: payment, setup, or subscription.
        kwargs: Additional Stripe parameters.
    Returns:
        JSON response from Stripe or error dict.
    """
    data = {"success_url": success_url, "cancel_url": cancel_url, "mode": mode}
    for idx, item in enumerate(line_items):
        for k, v in item.items():
            data[f"line_items[{idx}][{k}]"] = v
    data.update(kwargs)
    try:
        resp = requests.post(f"{BASE_URL}/checkout/sessions", data=data, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def retrieve_checkout_session(session_id: str) -> Dict[str, Any]:
    """
    Retrieve a Checkout Session.
    Args:
        session_id: The ID of the Checkout Session.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.get(f"{BASE_URL}/checkout/sessions/{session_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
