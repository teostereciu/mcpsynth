import os
import requests
from typing import Optional, Dict, Any

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {"Authorization": f"Bearer {STRIPE_API_KEY}"}

def create_setup_intent(customer: Optional[str] = None, **kwargs) -> Dict[str, Any]:
    """
    Create a SetupIntent object.
    Args:
        customer: Customer ID (optional).
        kwargs: Additional Stripe parameters.
    Returns:
        JSON response from Stripe or error dict.
    """
    data = {}
    if customer:
        data["customer"] = customer
    data.update(kwargs)
    try:
        resp = requests.post(f"{BASE_URL}/setup_intents", data=data, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def retrieve_setup_intent(setup_intent_id: str) -> Dict[str, Any]:
    """
    Retrieve a SetupIntent object.
    Args:
        setup_intent_id: The ID of the SetupIntent.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.get(f"{BASE_URL}/setup_intents/{setup_intent_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
