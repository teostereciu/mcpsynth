"""Stripe Coupons, Promotion Codes, and Discounts tools."""
import os
import requests

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "")
BASE_URL = "https://api.stripe.com/v1"


def _headers():
    return {"Authorization": f"Bearer {STRIPE_API_KEY}"}


def _req(method: str, path: str, params: dict = None, data: dict = None):
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.request(
            method,
            url,
            headers=_headers(),
            params=params if method == "GET" else None,
            data=data if method != "GET" else None,
            timeout=30,
        )
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


# ── Coupons ───────────────────────────────────────────────────────────────────

def create_coupon(
    duration: str,
    amount_off: int = None,
    percent_off: float = None,
    currency: str = None,
    duration_in_months: int = None,
    max_redemptions: int = None,
    name: str = None,
    id: str = None,
    metadata: dict = None,
):
    """Create a Coupon. duration: 'forever','once','repeating'."""
    data = {"duration": duration}
    if amount_off is not None:
        data["amount_off"] = amount_off
    if percent_off is not None:
        data["percent_off"] = percent_off
    if currency:
        data["currency"] = currency
    if duration_in_months is not None:
        data["duration_in_months"] = duration_in_months
    if max_redemptions is not None:
        data["max_redemptions"] = max_redemptions
    if name:
        data["name"] = name
    if id:
        data["id"] = id
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/coupons", data=data)


def get_coupon(coupon_id: str):
    """Retrieve a Coupon by ID."""
    return _req("GET", f"/coupons/{coupon_id}")


def update_coupon(coupon_id: str, name: str = None, metadata: dict = None):
    """Update a Coupon."""
    data = {}
    if name:
        data["name"] = name
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/coupons/{coupon_id}", data=data)


def delete_coupon(coupon_id: str):
    """Delete a Coupon."""
    return _req("DELETE", f"/coupons/{coupon_id}")


def list_coupons(limit: int = None, starting_after: str = None):
    """List Coupons."""
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    return _req("GET", "/coupons", params=params)


# ── Promotion Codes ───────────────────────────────────────────────────────────

def create_promotion_code(
    coupon: str,
    code: str = None,
    active: bool = None,
    customer: str = None,
    expires_at: int = None,
    max_redemptions: int = None,
    metadata: dict = None,
):
    """Create a Promotion Code for a Coupon."""
    data = {"coupon": coupon}
    if code:
        data["code"] = code
    if active is not None:
        data["active"] = str(active).lower()
    if customer:
        data["customer"] = customer
    if expires_at is not None:
        data["expires_at"] = expires_at
    if max_redemptions is not None:
        data["max_redemptions"] = max_redemptions
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/promotion_codes", data=data)


def get_promotion_code(promotion_code_id: str):
    """Retrieve a Promotion Code by ID."""
    return _req("GET", f"/promotion_codes/{promotion_code_id}")


def update_promotion_code(
    promotion_code_id: str,
    active: bool = None,
    metadata: dict = None,
):
    """Update a Promotion Code."""
    data = {}
    if active is not None:
        data["active"] = str(active).lower()
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/promotion_codes/{promotion_code_id}", data=data)


def list_promotion_codes(
    active: bool = None,
    code: str = None,
    coupon: str = None,
    customer: str = None,
    limit: int = None,
):
    """List Promotion Codes."""
    params = {}
    if active is not None:
        params["active"] = str(active).lower()
    if code:
        params["code"] = code
    if coupon:
        params["coupon"] = coupon
    if customer:
        params["customer"] = customer
    if limit is not None:
        params["limit"] = limit
    return _req("GET", "/promotion_codes", params=params)


# ── Discounts ─────────────────────────────────────────────────────────────────

def delete_customer_discount(customer_id: str):
    """Remove a discount from a Customer."""
    return _req("DELETE", f"/customers/{customer_id}/discount")


def delete_subscription_discount(subscription_id: str):
    """Remove a discount from a Subscription."""
    return _req("DELETE", f"/subscriptions/{subscription_id}/discount")
