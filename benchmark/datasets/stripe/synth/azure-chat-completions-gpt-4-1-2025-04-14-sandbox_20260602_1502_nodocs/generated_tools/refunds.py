import os
import requests
from typing import Optional, Dict, Any

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {"Authorization": f"Bearer {STRIPE_API_KEY}"}

def create_refund(charge: str, amount: Optional[int] = None, **kwargs) -> Dict[str, Any]:
    """
    Create a Refund object.
    Args:
        charge: The ID of the charge to refund.
        amount: Amount to refund (optional, in the smallest currency unit).
        kwargs: Additional Stripe parameters.
    Returns:
        JSON response from Stripe or error dict.
    """
    data = {"charge": charge}
    if amount:
        data["amount"] = amount
    data.update(kwargs)
    try:
        resp = requests.post(f"{BASE_URL}/refunds", data=data, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def retrieve_refund(refund_id: str) -> Dict[str, Any]:
    """
    Retrieve a Refund object.
    Args:
        refund_id: The ID of the Refund.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.get(f"{BASE_URL}/refunds/{refund_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
