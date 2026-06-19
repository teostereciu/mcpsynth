import os
import requests
from typing import Optional, Dict, Any

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {"Authorization": f"Bearer {STRIPE_API_KEY}"}

def create_payment_intent(amount: int, currency: str, **kwargs) -> Dict[str, Any]:
    """
    Create a PaymentIntent object.
    Args:
        amount: Amount intended to be collected by this PaymentIntent (in the smallest currency unit).
        currency: Three-letter ISO currency code.
        kwargs: Additional Stripe parameters (e.g. customer, payment_method_types, etc.)
    Returns:
        JSON response from Stripe or error dict.
    """
    data = {"amount": amount, "currency": currency}
    data.update(kwargs)
    try:
        resp = requests.post(f"{BASE_URL}/payment_intents", data=data, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def retrieve_payment_intent(payment_intent_id: str) -> Dict[str, Any]:
    """
    Retrieve a PaymentIntent object.
    Args:
        payment_intent_id: The ID of the PaymentIntent.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.get(f"{BASE_URL}/payment_intents/{payment_intent_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def cancel_payment_intent(payment_intent_id: str) -> Dict[str, Any]:
    """
    Cancel a PaymentIntent object.
    Args:
        payment_intent_id: The ID of the PaymentIntent.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.post(f"{BASE_URL}/payment_intents/{payment_intent_id}/cancel", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
