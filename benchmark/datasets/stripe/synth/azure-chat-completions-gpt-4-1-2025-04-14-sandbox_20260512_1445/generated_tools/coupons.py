import os
import requests
from fastmcp import tool

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

@tool("create_coupon")
def create_coupon(amount_off: int = None, currency: str = None, duration: str = None, metadata: dict = None, name: str = None, percent_off: float = None, applies_to: dict = None, currency_options: dict = None, duration_in_months: int = None, id: str = None, max_redemptions: int = None, redeem_by: int = None):
    """
    Create a Coupon object.
    """
    data = {}
    if amount_off is not None:
        data["amount_off"] = amount_off
    if currency:
        data["currency"] = currency
    if duration:
        data["duration"] = duration
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if name:
        data["name"] = name
    if percent_off is not None:
        data["percent_off"] = percent_off
    if applies_to:
        for k, v in applies_to.items():
            data[f"applies_to[{k}]"] = v
    if currency_options:
        for k, v in currency_options.items():
            data[f"currency_options[{k}]"] = v
    if duration_in_months is not None:
        data["duration_in_months"] = duration_in_months
    if id:
        data["id"] = id
    if max_redemptions is not None:
        data["max_redemptions"] = max_redemptions
    if redeem_by is not None:
        data["redeem_by"] = redeem_by
    try:
        resp = requests.post(f"{BASE_URL}/coupons", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("retrieve_coupon")
def retrieve_coupon(coupon_id: str):
    """
    Retrieve a Coupon object.
    """
    try:
        resp = requests.get(f"{BASE_URL}/coupons/{coupon_id}", headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("update_coupon")
def update_coupon(coupon_id: str, metadata: dict = None, name: str = None, currency_options: dict = None):
    """
    Update a Coupon object (metadata, name, currency_options).
    """
    data = {}
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if name:
        data["name"] = name
    if currency_options:
        for k, v in currency_options.items():
            data[f"currency_options[{k}]"] = v
    try:
        resp = requests.post(f"{BASE_URL}/coupons/{coupon_id}", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}
