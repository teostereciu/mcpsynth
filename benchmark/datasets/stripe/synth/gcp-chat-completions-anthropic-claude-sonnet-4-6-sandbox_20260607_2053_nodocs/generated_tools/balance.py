"""
Stripe Balance and Balance Transactions tools.
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


def get_balance(stripe_account: str = None) -> dict:
    """Retrieve the current account Balance."""
    headers = {}
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    resp = requests.get(f"{BASE_URL}/balance", auth=_auth(), headers=headers)
    return _handle(resp)


def get_balance_transaction(transaction_id: str) -> dict:
    """Retrieve a Balance Transaction by ID."""
    resp = requests.get(
        f"{BASE_URL}/balance_transactions/{transaction_id}", auth=_auth()
    )
    return _handle(resp)


def list_balance_transactions(
    type: str = None,
    source: str = None,
    payout: str = None,
    currency: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    created_gte: int = None,
    created_lte: int = None,
    available_on_gte: int = None,
    available_on_lte: int = None,
) -> dict:
    """List Balance Transactions."""
    params = {}
    if type:
        params["type"] = type
    if source:
        params["source"] = source
    if payout:
        params["payout"] = payout
    if currency:
        params["currency"] = currency
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
    if available_on_gte is not None:
        params["available_on[gte]"] = available_on_gte
    if available_on_lte is not None:
        params["available_on[lte]"] = available_on_lte
    resp = requests.get(
        f"{BASE_URL}/balance_transactions", params=params, auth=_auth()
    )
    return _handle(resp)
