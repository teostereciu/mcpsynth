import os
import requests
from typing import Any, Dict

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_subscription(customer: str = None, items: list = None, **kwargs) -> Dict[str, Any]:
    """
    Create a new subscription for a customer.
    Required: customer (str), items (list of dicts with at least price)
    Optional: automatic_tax (dict), currency (str), customer_account (str), default_payment_method (str), description (str), metadata (dict), payment_behavior (str), etc.
    Returns: Subscription object or error dict
    """
    url = f"{BASE_URL}/subscriptions"
    data = {}
    if customer is not None:
        data["customer"] = customer
    if items is not None:
        for idx, item in enumerate(items):
            for k, v in item.items():
                data[f"items[{idx}][{k}]"] = v
    for k, v in kwargs.items():
        if v is not None:
            if isinstance(v, dict):
                for subk, subv in v.items():
                    data[f"{k}[{subk}]"] = subv
            elif isinstance(v, list):
                for idx, subv in enumerate(v):
                    data[f"{k}[{idx}]"] = subv
            else:
                data[k] = v
    try:
        resp = requests.post(url, data=data, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
