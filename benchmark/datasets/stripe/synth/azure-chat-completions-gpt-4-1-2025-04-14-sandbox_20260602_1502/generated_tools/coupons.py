import os
import requests
from typing import Any, Dict

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_coupon(**kwargs) -> Dict[str, Any]:
    """
    Create a coupon.
    Optional: amount_off (int), currency (str), duration (str), metadata (dict), name (str), percent_off (float), applies_to (dict), currency_options (dict), duration_in_months (int), id (str), max_redemptions (int), redeem_by (int)
    Returns: Coupon object or error dict
    """
    url = f"{BASE_URL}/coupons"
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

def update_coupon(coupon_id: str, metadata: dict = None, name: str = None, **kwargs) -> Dict[str, Any]:
    """
    Update a coupon's metadata or name.
    Returns: Coupon object or error dict
    """
    url = f"{BASE_URL}/coupons/{coupon_id}"
    data = {}
    if metadata is not None:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if name is not None:
        data["name"] = name
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

def get_coupon(coupon_id: str) -> Dict[str, Any]:
    """
    Retrieve a coupon by ID.
    Returns: Coupon object or error dict
    """
    url = f"{BASE_URL}/coupons/{coupon_id}"
    try:
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
