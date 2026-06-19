import os
import requests
from typing import Optional, Dict, Any

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {"Authorization": f"Bearer {STRIPE_API_KEY}"}

def create_charge(amount: int, currency: str, source: str, **kwargs) -> Dict[str, Any]:
    """
    Create a Charge object.
    Args:
        amount: Amount to charge (in the smallest currency unit).
        currency: Three-letter ISO currency code.
        source: Payment source (e.g. token or card ID).
        kwargs: Additional Stripe parameters (e.g. customer, description, etc.)
    Returns:
        JSON response from Stripe or error dict.
    """
    data = {"amount": amount, "currency": currency, "source": source}
    data.update(kwargs)
    try:
        resp = requests.post(f"{BASE_URL}/charges", data=data, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def retrieve_charge(charge_id: str) -> Dict[str, Any]:
    """
    Retrieve a Charge object.
    Args:
        charge_id: The ID of the Charge.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.get(f"{BASE_URL}/charges/{charge_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def refund_charge(charge_id: str, amount: Optional[int] = None) -> Dict[str, Any]:
    """
    Refund a Charge object.
    Args:
        charge_id: The ID of the Charge.
        amount: Amount to refund (optional, in the smallest currency unit).
    Returns:
        JSON response from Stripe or error dict.
    """
    data = {"charge": charge_id}
    if amount:
        data["amount"] = amount
    try:
        resp = requests.post(f"{BASE_URL}/refunds", data=data, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
