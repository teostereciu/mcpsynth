import os
import requests
from typing import Optional, Dict, Any

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {"Authorization": f"Bearer {STRIPE_API_KEY}"}

def create_promotion_code(coupon: str, **kwargs) -> Dict[str, Any]:
    """
    Create a Promotion Code object.
    Args:
        coupon: Coupon ID to attach to the promotion code.
        kwargs: Additional Stripe parameters (e.g. code, max_redemptions, etc.)
    Returns:
        JSON response from Stripe or error dict.
    """
    data = {"coupon": coupon}
    data.update(kwargs)
    try:
        resp = requests.post(f"{BASE_URL}/promotion_codes", data=data, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def retrieve_promotion_code(promotion_code_id: str) -> Dict[str, Any]:
    """
    Retrieve a Promotion Code object.
    Args:
        promotion_code_id: The ID of the Promotion Code.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.get(f"{BASE_URL}/promotion_codes/{promotion_code_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
