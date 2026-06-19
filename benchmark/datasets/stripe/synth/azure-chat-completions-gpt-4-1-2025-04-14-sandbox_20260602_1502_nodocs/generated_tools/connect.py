import os
import requests
from typing import Optional, Dict, Any

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {"Authorization": f"Bearer {STRIPE_API_KEY}"}

def create_account(type: str, country: str, email: Optional[str] = None, **kwargs) -> Dict[str, Any]:
    """
    Create a Connect Account.
    Args:
        type: account type (custom, express, standard)
        country: country code
        email: email address (optional)
        kwargs: Additional Stripe parameters.
    Returns:
        JSON response from Stripe or error dict.
    """
    data = {"type": type, "country": country}
    if email:
        data["email"] = email
    data.update(kwargs)
    try:
        resp = requests.post(f"{BASE_URL}/accounts", data=data, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def retrieve_account(account_id: str) -> Dict[str, Any]:
    """
    Retrieve a Connect Account.
    Args:
        account_id: The ID of the Account.
    Returns:
        JSON response from Stripe or error dict.
    """
    try:
        resp = requests.get(f"{BASE_URL}/accounts/{account_id}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def create_transfer(amount: int, currency: str, destination: str, **kwargs) -> Dict[str, Any]:
    """
    Create a Transfer to a connected account.
    Args:
        amount: Amount to transfer (in the smallest currency unit).
        currency: Three-letter ISO currency code.
        destination: Account ID to transfer to.
        kwargs: Additional Stripe parameters.
    Returns:
        JSON response from Stripe or error dict.
    """
    data = {"amount": amount, "currency": currency, "destination": destination}
    data.update(kwargs)
    try:
        resp = requests.post(f"{BASE_URL}/transfers", data=data, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def create_payout(amount: int, currency: str, **kwargs) -> Dict[str, Any]:
    """
    Create a Payout.
    Args:
        amount: Amount to payout (in the smallest currency unit).
        currency: Three-letter ISO currency code.
        kwargs: Additional Stripe parameters.
    Returns:
        JSON response from Stripe or error dict.
    """
    data = {"amount": amount, "currency": currency}
    data.update(kwargs)
    try:
        resp = requests.post(f"{BASE_URL}/payouts", data=data, headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
