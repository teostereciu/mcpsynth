import os
import requests
from typing import Any, Dict

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_payment_link(line_items: list, **kwargs) -> Dict[str, Any]:
    """
    Create a payment link.
    Required: line_items (list of dicts)
    Optional: metadata (dict), after_completion (dict), allow_promotion_codes (bool), application_fee_amount (int), application_fee_percent (float), automatic_tax (dict), billing_address_collection (str), consent_collection (dict), currency (str), custom_fields (list), custom_text (dict), customer_creation (str), inactive_message (str), invoice_creation (dict), name_collection (dict), on_behalf_of (str), optional_items (list), payment_intent_data (dict), payment_method_collection (str), payment_method_types (list), phone_number_collection (dict), restrictions (dict), shipping_address_collection (dict), shipping_options (list), submit_type (str), subscription_data (dict), tax_id_collection (dict), transfer_data (dict)
    Returns: Payment Link object or error dict
    """
    url = f"{BASE_URL}/payment_links"
    data = {}
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
