"""
Stripe Tokens tools.
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


def create_card_token(
    card_number: str,
    card_exp_month: int,
    card_exp_year: int,
    card_cvc: str,
    card_name: str = None,
    card_address_line1: str = None,
    card_address_city: str = None,
    card_address_state: str = None,
    card_address_zip: str = None,
    card_address_country: str = None,
) -> dict:
    """Create a Token for a card (for use in test environments)."""
    data = {
        "card[number]": card_number,
        "card[exp_month]": card_exp_month,
        "card[exp_year]": card_exp_year,
        "card[cvc]": card_cvc,
    }
    if card_name:
        data["card[name]"] = card_name
    if card_address_line1:
        data["card[address_line1]"] = card_address_line1
    if card_address_city:
        data["card[address_city]"] = card_address_city
    if card_address_state:
        data["card[address_state]"] = card_address_state
    if card_address_zip:
        data["card[address_zip]"] = card_address_zip
    if card_address_country:
        data["card[address_country]"] = card_address_country
    resp = requests.post(f"{BASE_URL}/tokens", data=data, auth=_auth())
    return _handle(resp)


def create_bank_account_token(
    bank_account_country: str,
    bank_account_currency: str,
    bank_account_account_holder_name: str,
    bank_account_account_holder_type: str,
    bank_account_routing_number: str,
    bank_account_account_number: str,
) -> dict:
    """Create a Token for a bank account."""
    data = {
        "bank_account[country]": bank_account_country,
        "bank_account[currency]": bank_account_currency,
        "bank_account[account_holder_name]": bank_account_account_holder_name,
        "bank_account[account_holder_type]": bank_account_account_holder_type,
        "bank_account[routing_number]": bank_account_routing_number,
        "bank_account[account_number]": bank_account_account_number,
    }
    resp = requests.post(f"{BASE_URL}/tokens", data=data, auth=_auth())
    return _handle(resp)


def get_token(token_id: str) -> dict:
    """Retrieve a Token by ID."""
    resp = requests.get(f"{BASE_URL}/tokens/{token_id}", auth=_auth())
    return _handle(resp)
