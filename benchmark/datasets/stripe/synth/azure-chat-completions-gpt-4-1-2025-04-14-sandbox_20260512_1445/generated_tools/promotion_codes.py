import os
import requests
from fastmcp import tool

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

@tool("create_promotion_code")
def create_promotion_code(promotion: dict, code: str = None, metadata: dict = None, active: bool = None, customer: str = None, customer_account: str = None, expires_at: int = None, max_redemptions: int = None, restrictions: dict = None):
    """
    Create a Promotion Code object.
    """
    data = {}
    for k, v in promotion.items():
        data[f"promotion[{k}]"] = v
    if code:
        data["code"] = code
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if active is not None:
        data["active"] = "true" if active else "false"
    if customer:
        data["customer"] = customer
    if customer_account:
        data["customer_account"] = customer_account
    if expires_at:
        data["expires_at"] = expires_at
    if max_redemptions:
        data["max_redemptions"] = max_redemptions
    if restrictions:
        for k, v in restrictions.items():
            data[f"restrictions[{k}]"] = v
    try:
        resp = requests.post(f"{BASE_URL}/promotion_codes", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("retrieve_promotion_code")
def retrieve_promotion_code(promotion_code_id: str):
    """
    Retrieve a Promotion Code object.
    """
    try:
        resp = requests.get(f"{BASE_URL}/promotion_codes/{promotion_code_id}", headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("update_promotion_code")
def update_promotion_code(promotion_code_id: str, metadata: dict = None, active: bool = None, restrictions: dict = None):
    """
    Update a Promotion Code object.
    """
    data = {}
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if active is not None:
        data["active"] = "true" if active else "false"
    if restrictions:
        for k, v in restrictions.items():
            data[f"restrictions[{k}]"] = v
    try:
        resp = requests.post(f"{BASE_URL}/promotion_codes/{promotion_code_id}", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}
