import os
import requests
from typing import Optional, Dict, Any

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {"Authorization": f"Bearer {STRIPE_API_KEY}"}

def create_subscription(customer: str, items: list, **kwargs) -> Dict[str, Any]:
    """
    Create a Subscription object.
    Args:
        customer: Customer ID to subscribe.
        items: List of dicts, each with at least a 'price' key.
        kwargs: Additional Stripe parameters (e.g. trial_period_days, etc.)
    Returns:
        JSON response from Stripe or error dict.
    """
    data = {"customer": customer}
    for idx, item in enumerate(items):
        for k, v in item.items():
            data[f"items[{idx}][{k}]"] = v
    data.update(kwargs)
    try:
        resp = requests.post(f"{BASE_URL}/subscriptions", data=data, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def retrieve_subscription(subscription_id: str) -> Dict[str, Any]:
    """
    Retrieve a Subscription object.
    Args:
        subscription_id: The ID of the Subscription.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.get(f"{BASE_URL}/subscriptions/{subscription_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def cancel_subscription(subscription_id: str) -> Dict[str, Any]:
    """
    Cancel a Subscription object.
    Args:
        subscription_id: The ID of the Subscription.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.delete(f"{BASE_URL}/subscriptions/{subscription_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
