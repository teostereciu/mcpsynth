import os
import requests
from typing import Any, Dict

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_invoice_preview(customer: str = None, subscription: str = None, **kwargs) -> Dict[str, Any]:
    """
    Preview the upcoming invoice for a subscription or customer.
    At least one of customer or subscription must be provided.
    Optional: automatic_tax (dict), customer_account (str), currency (str), customer_details (dict), discounts (list), invoice_items (list), issuer (dict), on_behalf_of (str), preview_mode (str), schedule (str), schedule_details (dict), subscription_details (dict)
    Returns: Invoice object or error dict
    """
    url = f"{BASE_URL}/invoices/create_preview"
    data = {}
    if customer is not None:
        data["customer"] = customer
    if subscription is not None:
        data["subscription"] = subscription
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
