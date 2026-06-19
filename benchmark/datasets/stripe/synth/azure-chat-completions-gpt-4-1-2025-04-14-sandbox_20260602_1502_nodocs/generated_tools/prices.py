import os
import requests
from typing import Optional, Dict, Any

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {"Authorization": f"Bearer {STRIPE_API_KEY}"}

def create_price(unit_amount: int, currency: str, product: str, **kwargs) -> Dict[str, Any]:
    """
    Create a Price object.
    Args:
        unit_amount: Amount in the smallest currency unit.
        currency: Three-letter ISO currency code.
        product: Product ID this price is for.
        kwargs: Additional Stripe parameters (e.g. recurring, nickname, etc.)
    Returns:
        JSON response from Stripe or error dict.
    """
    data = {"unit_amount": unit_amount, "currency": currency, "product": product}
    data.update(kwargs)
    try:
        resp = requests.post(f"{BASE_URL}/prices", data=data, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def retrieve_price(price_id: str) -> Dict[str, Any]:
    """
    Retrieve a Price object.
    Args:
        price_id: The ID of the Price.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.get(f"{BASE_URL}/prices/{price_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
