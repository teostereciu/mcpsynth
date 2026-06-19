import os
import requests
from typing import Any, Dict

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_payment_intent(amount: int, currency: str, **kwargs) -> Dict[str, Any]:
    """
    Creates a PaymentIntent object.
    Required: amount (int), currency (str)
    Optional: automatic_payment_methods (dict), confirm (bool), customer (str), description (str), metadata (dict),
              off_session (bool or str), payment_method (str), receipt_email (str), setup_future_usage (str),
              shipping (dict), statement_descriptor (str), statement_descriptor_suffix (str), etc.
    Returns: PaymentIntent object or error dict
    """
    url = f"{BASE_URL}/payment_intents"
    data = {
        "amount": amount,
        "currency": currency
    }
    # Add optional parameters
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
