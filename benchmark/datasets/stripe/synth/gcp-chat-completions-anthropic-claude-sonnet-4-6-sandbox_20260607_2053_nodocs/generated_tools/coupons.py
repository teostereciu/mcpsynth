"""
Stripe Coupons and Promotion Codes tools.
"""
import os
import requests

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "")
BASE_URL = "https://api.stripe.com/v1"


def _auth():
    return (STRIPE_API_KEY, "")


def _handle(resp: requests.Response) -> dict:
    try:
        return resp.json()
    except Exception:
        return {"error": resp.text}


# ── Coupons ──────────────────────────────────────────────────────────────────

def create_coupon(
    id: str = None,
    amount_off: int = None,
    percent_off: float = None,
    currency: str = None,
    duration: str = "once",
    duration_in_months: int = None,
    max_redemptions: int = None,
    name: str = None,
    redeem_by: int = None,
    metadata: dict = None,
) -> dict:
    """Create a Coupon. Provide either amount_off+currency or percent_off."""
    data = {"duration": duration}
    if id:
        data["id"] = id
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
    if redeem_by is not None:
        data["redeem_by"] = redeem_by
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/coupons", data=data, auth=_auth())
    return _handle(resp)


def get_coupon(coupon_id: str) -> dict:
    """Retrieve a Coupon by ID."""
    resp = requests.get(f"{BASE_URL}/coupons/{coupon_id}", auth=_auth())
    return _handle(resp)


def update_coupon(
    coupon_id: str,
    name: str = None,
    metadata: dict = None,
) -> dict:
    """Update a Coupon."""
    data = {}
    if name:
        data["name"] = name
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/coupons/{coupon_id}", data=data, auth=_auth())
    return _handle(resp)


def delete_coupon(coupon_id: str) -> dict:
    """Delete a Coupon."""
    resp = requests.delete(f"{BASE_URL}/coupons/{coupon_id}", auth=_auth())
    return _handle(resp)


def list_coupons(
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    created_gte: int = None,
    created_lte: int = None,
) -> dict:
    """List Coupons."""
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if created_gte is not None:
        params["created[gte]"] = created_gte
    if created_lte is not None:
        params["created[lte]"] = created_lte
    resp = requests.get(f"{BASE_URL}/coupons", params=params, auth=_auth())
    return _handle(resp)


# ── Promotion Codes ──────────────────────────────────────────────────────────

def create_promotion_code(
    coupon: str,
    code: str = None,
    active: bool = None,
    customer: str = None,
    expires_at: int = None,
    max_redemptions: int = None,
    metadata: dict = None,
    restrictions_first_time_transaction: bool = None,
    restrictions_minimum_amount: int = None,
    restrictions_minimum_amount_currency: str = None,
) -> dict:
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
    if restrictions_first_time_transaction is not None:
        data["restrictions[first_time_transaction]"] = str(
            restrictions_first_time_transaction
        ).lower()
    if restrictions_minimum_amount is not None:
        data["restrictions[minimum_amount]"] = restrictions_minimum_amount
    if restrictions_minimum_amount_currency:
        data["restrictions[minimum_amount_currency]"] = (
            restrictions_minimum_amount_currency
        )
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/promotion_codes", data=data, auth=_auth())
    return _handle(resp)


def get_promotion_code(promotion_code_id: str) -> dict:
    """Retrieve a Promotion Code by ID."""
    resp = requests.get(
        f"{BASE_URL}/promotion_codes/{promotion_code_id}", auth=_auth()
    )
    return _handle(resp)


def update_promotion_code(
    promotion_code_id: str,
    active: bool = None,
    metadata: dict = None,
) -> dict:
    """Update a Promotion Code."""
    data = {}
    if active is not None:
        data["active"] = str(active).lower()
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(
        f"{BASE_URL}/promotion_codes/{promotion_code_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def list_promotion_codes(
    active: bool = None,
    code: str = None,
    coupon: str = None,
    customer: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
) -> dict:
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
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    resp = requests.get(f"{BASE_URL}/promotion_codes", params=params, auth=_auth())
    return _handle(resp)
