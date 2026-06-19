import os
import requests
from typing import Optional, Dict, Any

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {"Authorization": f"Bearer {STRIPE_API_KEY}"}

def create_coupon(**kwargs) -> Dict[str, Any]:
    """
    Create a Coupon object.
    Args:
        kwargs: Stripe coupon parameters (e.g. percent_off, amount_off, duration, etc.)
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.post(f"{BASE_URL}/coupons", data=kwargs, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def retrieve_coupon(coupon_id: str) -> Dict[str, Any]:
    """
    Retrieve a Coupon object.
    Args:
        coupon_id: The ID of the Coupon.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.get(f"{BASE_URL}/coupons/{coupon_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
