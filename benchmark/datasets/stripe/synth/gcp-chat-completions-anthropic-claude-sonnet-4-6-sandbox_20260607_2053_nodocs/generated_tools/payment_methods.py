"""
Stripe Payment Methods tools.
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


def create_payment_method(
    type: str,
    card_number: str = None,
    card_exp_month: int = None,
    card_exp_year: int = None,
    card_cvc: str = None,
    card_token: str = None,
    billing_details_name: str = None,
    billing_details_email: str = None,
    billing_details_phone: str = None,
    metadata: dict = None,
) -> dict:
    """Create a PaymentMethod (e.g. type='card')."""
    data = {"type": type}
    if card_number:
        data["card[number]"] = card_number
    if card_exp_month is not None:
        data["card[exp_month]"] = card_exp_month
    if card_exp_year is not None:
        data["card[exp_year]"] = card_exp_year
    if card_cvc:
        data["card[cvc]"] = card_cvc
    if card_token:
        data["card[token]"] = card_token
    if billing_details_name:
        data["billing_details[name]"] = billing_details_name
    if billing_details_email:
        data["billing_details[email]"] = billing_details_email
    if billing_details_phone:
        data["billing_details[phone]"] = billing_details_phone
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/payment_methods", data=data, auth=_auth())
    return _handle(resp)


def get_payment_method(payment_method_id: str) -> dict:
    """Retrieve a PaymentMethod by ID."""
    resp = requests.get(
        f"{BASE_URL}/payment_methods/{payment_method_id}", auth=_auth()
    )
    return _handle(resp)


def update_payment_method(
    payment_method_id: str,
    billing_details_name: str = None,
    billing_details_email: str = None,
    billing_details_phone: str = None,
    card_exp_month: int = None,
    card_exp_year: int = None,
    metadata: dict = None,
) -> dict:
    """Update a PaymentMethod."""
    data = {}
    if billing_details_name:
        data["billing_details[name]"] = billing_details_name
    if billing_details_email:
        data["billing_details[email]"] = billing_details_email
    if billing_details_phone:
        data["billing_details[phone]"] = billing_details_phone
    if card_exp_month is not None:
        data["card[exp_month]"] = card_exp_month
    if card_exp_year is not None:
        data["card[exp_year]"] = card_exp_year
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(
        f"{BASE_URL}/payment_methods/{payment_method_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def attach_payment_method(payment_method_id: str, customer: str) -> dict:
    """Attach a PaymentMethod to a Customer."""
    data = {"customer": customer}
    resp = requests.post(
        f"{BASE_URL}/payment_methods/{payment_method_id}/attach",
        data=data,
        auth=_auth(),
    )
    return _handle(resp)


def detach_payment_method(payment_method_id: str) -> dict:
    """Detach a PaymentMethod from its Customer."""
    resp = requests.post(
        f"{BASE_URL}/payment_methods/{payment_method_id}/detach",
        data={},
        auth=_auth(),
    )
    return _handle(resp)


def list_payment_methods(
    customer: str = None,
    type: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
) -> dict:
    """List PaymentMethods (optionally filtered by customer and type)."""
    params = {}
    if customer:
        params["customer"] = customer
    if type:
        params["type"] = type
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    resp = requests.get(f"{BASE_URL}/payment_methods", params=params, auth=_auth())
    return _handle(resp)
