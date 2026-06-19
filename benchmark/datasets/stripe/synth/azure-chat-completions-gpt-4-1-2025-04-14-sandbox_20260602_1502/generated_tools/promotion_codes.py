import os
import requests
from typing import Any, Dict

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_promotion_code(promotion: dict, code: str = None, **kwargs) -> Dict[str, Any]:
    """
    Create a promotion code for a promotion.
    Required: promotion (dict)
    Optional: code (str), metadata (dict), active (bool), customer (str), customer_account (str), expires_at (int), max_redemptions (int), restrictions (dict)
    Returns: Promotion Code object or error dict
    """
    url = f"{BASE_URL}/promotion_codes"
    data = {}
    for k, v in promotion.items():
        data[f"promotion[{k}]"] = v
    if code is not None:
        data["code"] = code
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

def update_promotion_code(promotion_code_id: str, metadata: dict = None, active: bool = None, restrictions: dict = None) -> Dict[str, Any]:
    """
    Update a promotion code's metadata, active status, or restrictions.
    Returns: Promotion Code object or error dict
    """
    url = f"{BASE_URL}/promotion_codes/{promotion_code_id}"
    data = {}
    if metadata is not None:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if active is not None:
        data["active"] = active
    if restrictions is not None:
        for k, v in restrictions.items():
            data[f"restrictions[{k}]"] = v
    try:
        resp = requests.post(url, data=data, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def get_promotion_code(promotion_code_id: str) -> Dict[str, Any]:
    """
    Retrieve a promotion code by ID.
    Returns: Promotion Code object or error dict
    """
    url = f"{BASE_URL}/promotion_codes/{promotion_code_id}"
    try:
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
