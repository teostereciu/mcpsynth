import os
import requests
from typing import Any, Dict

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_charge(amount: int, currency: str, **kwargs) -> Dict[str, Any]:
    """
    Creates a charge (deprecated, use PaymentIntents for new integrations).
    Required: amount (int), currency (str)
    Optional: customer (str), description (str), metadata (dict), receipt_email (str), shipping (dict), source (str),
              statement_descriptor (str), statement_descriptor_suffix (str), etc.
    Returns: Charge object or error dict
    """
    url = f"{BASE_URL}/charges"
    data = {
        "amount": amount,
        "currency": currency
    }
    for k, v in kwargs.items():
        if v is not None:
            if isinstance(v, dict):
                for subk, subv in v.items():
                    data[f"{k}[{subk}]"] = subv
            else:
                data[k] = v
    try:
        resp = requests.post(url, data=data, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def update_charge(charge_id: str, **kwargs) -> Dict[str, Any]:
    """
    Updates the specified charge by setting the values of the parameters passed.
    Optional: customer (str), description (str), metadata (dict), receipt_email (str), shipping (dict), fraud_details (dict), transfer_group (str)
    Returns: Charge object or error dict
    """
    url = f"{BASE_URL}/charges/{charge_id}"
    data = {}
    for k, v in kwargs.items():
        if v is not None:
            if isinstance(v, dict):
                for subk, subv in v.items():
                    data[f"{k}[{subk}]"] = subv
            else:
                data[k] = v
    try:
        resp = requests.post(url, data=data, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
