import os
import requests
from typing import Any, Dict

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_checkout_session(mode: str, line_items: list = None, **kwargs) -> Dict[str, Any]:
    """
    Create a Checkout Session.
    Required: mode (str), line_items (list of dicts) for payment/subscription mode
    Optional: automatic_tax (dict), client_reference_id (str), customer (str), customer_email (str), metadata (dict), return_url (str), success_url (str), ui_mode (str), and many more
    Returns: Checkout Session object or error dict
    """
    url = f"{BASE_URL}/checkout/sessions"
    data = {"mode": mode}
    if line_items is not None:
        for idx, item in enumerate(line_items):
            for k, v in item.items():
                data[f"line_items[{idx}][{k}]"] = v
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
