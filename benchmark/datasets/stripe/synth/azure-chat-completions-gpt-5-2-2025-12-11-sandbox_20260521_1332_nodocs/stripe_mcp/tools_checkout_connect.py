from typing import Any, Dict, Optional

from .http import stripe_request


def _ok(x: Any) -> Any:
    return x


def _err(e: Dict[str, Any]) -> Dict[str, Any]:
    return e


# Checkout Sessions
async def create_checkout_session(
    *,
    mode: str,
    success_url: str,
    cancel_url: str,
    line_items: list,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    allow_promotion_codes: Optional[bool] = None,
) -> Any:
    data = {
        "mode": mode,
        "success_url": success_url,
        "cancel_url": cancel_url,
        "line_items": line_items,
        "customer": customer,
        "customer_email": customer_email,
        "metadata": metadata,
        "allow_promotion_codes": allow_promotion_codes,
    }
    res, err = stripe_request("POST", "/v1/checkout/sessions", data=data)
    return _ok(res) if not err else _err(err)


async def get_checkout_session(*, session_id: str) -> Any:
    res, err = stripe_request("GET", f"/v1/checkout/sessions/{session_id}")
    return _ok(res) if not err else _err(err)


async def list_checkout_sessions(*, limit: int = 10, customer: Optional[str] = None) -> Any:
    query = {"limit": limit, "customer": customer}
    res, err = stripe_request("GET", "/v1/checkout/sessions", query=query)
    return _ok(res) if not err else _err(err)


# Payment Links
async def create_payment_link(*, line_items: list, after_completion: Optional[Dict[str, Any]] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data = {"line_items": line_items, "after_completion": after_completion, "metadata": metadata}
    res, err = stripe_request("POST", "/v1/payment_links", data=data)
    return _ok(res) if not err else _err(err)


async def get_payment_link(*, payment_link_id: str) -> Any:
    res, err = stripe_request("GET", f"/v1/payment_links/{payment_link_id}")
    return _ok(res) if not err else _err(err)


async def list_payment_links(*, active: Optional[bool] = None, limit: int = 10) -> Any:
    query = {"active": active, "limit": limit}
    res, err = stripe_request("GET", "/v1/payment_links", query=query)
    return _ok(res) if not err else _err(err)


# Setup Intents
async def create_setup_intent(*, customer: Optional[str] = None, payment_method_types: Optional[list] = None, usage: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data = {"customer": customer, "payment_method_types": payment_method_types, "usage": usage, "metadata": metadata}
    res, err = stripe_request("POST", "/v1/setup_intents", data=data)
    return _ok(res) if not err else _err(err)


async def get_setup_intent(*, setup_intent_id: str) -> Any:
    res, err = stripe_request("GET", f"/v1/setup_intents/{setup_intent_id}")
    return _ok(res) if not err else _err(err)


async def confirm_setup_intent(*, setup_intent_id: str, payment_method: Optional[str] = None, return_url: Optional[str] = None) -> Any:
    data = {"payment_method": payment_method, "return_url": return_url}
    res, err = stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/confirm", data=data)
    return _ok(res) if not err else _err(err)


# Connect: Accounts, Transfers, Payouts
async def create_connect_account(*, type: str = "express", country: Optional[str] = None, email: Optional[str] = None, capabilities: Optional[Dict[str, Any]] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data = {"type": type, "country": country, "email": email, "capabilities": capabilities, "metadata": metadata}
    res, err = stripe_request("POST", "/v1/accounts", data=data)
    return _ok(res) if not err else _err(err)


async def get_connect_account(*, account_id: str) -> Any:
    res, err = stripe_request("GET", f"/v1/accounts/{account_id}")
    return _ok(res) if not err else _err(err)


async def update_connect_account(*, account_id: str, metadata: Optional[Dict[str, str]] = None, business_profile: Optional[Dict[str, Any]] = None) -> Any:
    data = {"metadata": metadata, "business_profile": business_profile}
    res, err = stripe_request("POST", f"/v1/accounts/{account_id}", data=data)
    return _ok(res) if not err else _err(err)


async def list_connect_accounts(*, limit: int = 10) -> Any:
    res, err = stripe_request("GET", "/v1/accounts", query={"limit": limit})
    return _ok(res) if not err else _err(err)


async def create_transfer(*, amount: int, currency: str, destination: str, source_transaction: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data = {"amount": amount, "currency": currency, "destination": destination, "source_transaction": source_transaction, "metadata": metadata}
    res, err = stripe_request("POST", "/v1/transfers", data=data)
    return _ok(res) if not err else _err(err)


async def get_transfer(*, transfer_id: str) -> Any:
    res, err = stripe_request("GET", f"/v1/transfers/{transfer_id}")
    return _ok(res) if not err else _err(err)


async def list_transfers(*, limit: int = 10, destination: Optional[str] = None) -> Any:
    query = {"limit": limit, "destination": destination}
    res, err = stripe_request("GET", "/v1/transfers", query=query)
    return _ok(res) if not err else _err(err)


async def create_payout(*, amount: int, currency: str, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None, stripe_account: Optional[str] = None) -> Any:
    data = {"amount": amount, "currency": currency, "description": description, "metadata": metadata}
    res, err = stripe_request("POST", "/v1/payouts", data=data, stripe_account=stripe_account)
    return _ok(res) if not err else _err(err)


async def get_payout(*, payout_id: str, stripe_account: Optional[str] = None) -> Any:
    res, err = stripe_request("GET", f"/v1/payouts/{payout_id}", stripe_account=stripe_account)
    return _ok(res) if not err else _err(err)


async def list_payouts(*, limit: int = 10, stripe_account: Optional[str] = None) -> Any:
    res, err = stripe_request("GET", "/v1/payouts", query={"limit": limit}, stripe_account=stripe_account)
    return _ok(res) if not err else _err(err)


# Coupons & Promotion Codes
async def create_coupon(*, duration: str, percent_off: Optional[float] = None, amount_off: Optional[int] = None, currency: Optional[str] = None, name: Optional[str] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data = {"duration": duration, "percent_off": percent_off, "amount_off": amount_off, "currency": currency, "name": name, "metadata": metadata}
    res, err = stripe_request("POST", "/v1/coupons", data=data)
    return _ok(res) if not err else _err(err)


async def get_coupon(*, coupon_id: str) -> Any:
    res, err = stripe_request("GET", f"/v1/coupons/{coupon_id}")
    return _ok(res) if not err else _err(err)


async def list_coupons(*, limit: int = 10) -> Any:
    res, err = stripe_request("GET", "/v1/coupons", query={"limit": limit})
    return _ok(res) if not err else _err(err)


async def create_promotion_code(*, coupon: str, code: Optional[str] = None, active: Optional[bool] = None, max_redemptions: Optional[int] = None, metadata: Optional[Dict[str, str]] = None) -> Any:
    data = {"coupon": coupon, "code": code, "active": active, "max_redemptions": max_redemptions, "metadata": metadata}
    res, err = stripe_request("POST", "/v1/promotion_codes", data=data)
    return _ok(res) if not err else _err(err)


async def get_promotion_code(*, promotion_code_id: str) -> Any:
    res, err = stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}")
    return _ok(res) if not err else _err(err)


async def list_promotion_codes(*, limit: int = 10, coupon: Optional[str] = None, active: Optional[bool] = None, code: Optional[str] = None) -> Any:
    query = {"limit": limit, "coupon": coupon, "active": active, "code": code}
    res, err = stripe_request("GET", "/v1/promotion_codes", query=query)
    return _ok(res) if not err else _err(err)
