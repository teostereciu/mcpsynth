import os
import requests
from typing import Any, Dict

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_account(country: str = None, email: str = None, **kwargs) -> Dict[str, Any]:
    """
    Create a Stripe account (Connect).
    Optional: country (str), email (str), business_type (str), capabilities (dict), company (dict), controller (dict), individual (dict), metadata (dict), tos_acceptance (dict), type (str), account_token (str), business_profile (dict), default_currency (str), documents (dict), external_account (str), groups (dict), settings (dict)
    Returns: Account object or error dict
    """
    url = f"{BASE_URL}/accounts"
    data = {}
    if country is not None:
        data["country"] = country
    if email is not None:
        data["email"] = email
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
