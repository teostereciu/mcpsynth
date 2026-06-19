import os
import requests
from typing import Any, Dict

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_setup_intent(**kwargs) -> Dict[str, Any]:
    """
    Create a SetupIntent object.
    Optional: automatic_payment_methods (dict), confirm (bool), customer (str), customer_account (str), description (str), metadata (dict), payment_method (str), usage (str), attach_to_self (bool), confirmation_token (str), excluded_payment_method_types (list), flow_directions (list), mandate_data (dict), on_behalf_of (str), payment_method_configuration (str), payment_method_data (dict), payment_method_options (dict), payment_method_types (list), return_url (str), single_use (dict), use_stripe_sdk (bool)
    Returns: SetupIntent object or error dict
    """
    url = f"{BASE_URL}/setup_intents"
    data = {}
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

def update_setup_intent(setup_intent_id: str, **kwargs) -> Dict[str, Any]:
    """
    Update a SetupIntent object.
    Optional: customer (str), customer_account (str), description (str), metadata (dict), payment_method (str), attach_to_self (bool), excluded_payment_method_types (list), flow_directions (list), payment_method_configuration (str), payment_method_data (dict), payment_method_options (dict), payment_method_types (list)
    Returns: SetupIntent object or error dict
    """
    url = f"{BASE_URL}/setup_intents/{setup_intent_id}"
    data = {}
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

def get_setup_intent(setup_intent_id: str, client_secret: str = None) -> Dict[str, Any]:
    """
    Retrieve a SetupIntent by ID.
    Optional: client_secret (str) if using publishable key
    Returns: SetupIntent object or error dict
    """
    url = f"{BASE_URL}/setup_intents/{setup_intent_id}"
    params = {}
    if client_secret is not None:
        params["client_secret"] = client_secret
    try:
        resp = requests.get(url, headers=HEADERS, params=params)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
