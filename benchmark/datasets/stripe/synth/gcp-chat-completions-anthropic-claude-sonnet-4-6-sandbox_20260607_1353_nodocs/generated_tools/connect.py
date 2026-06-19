"""Stripe Connect tools: Accounts, Transfers, Payouts."""
import os
import requests

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "")
BASE_URL = "https://api.stripe.com/v1"


def _headers(stripe_account: str = None):
    h = {"Authorization": f"Bearer {STRIPE_API_KEY}"}
    if stripe_account:
        h["Stripe-Account"] = stripe_account
    return h


def _req(method: str, path: str, params: dict = None, data: dict = None, stripe_account: str = None):
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.request(
            method,
            url,
            headers=_headers(stripe_account),
            params=params if method == "GET" else None,
            data=data if method != "GET" else None,
            timeout=30,
        )
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


# ── Accounts ──────────────────────────────────────────────────────────────────

def create_account(
    type: str = "express",
    country: str = None,
    email: str = None,
    capabilities: dict = None,
    metadata: dict = None,
):
    """Create a connected Account. type: 'standard','express','custom'."""
    data = {"type": type}
    if country:
        data["country"] = country
    if email:
        data["email"] = email
    if capabilities:
        for cap, settings in capabilities.items():
            for k, v in settings.items():
                data[f"capabilities[{cap}][{k}]"] = v
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/accounts", data=data)


def get_account(account_id: str):
    """Retrieve a connected Account by ID."""
    return _req("GET", f"/accounts/{account_id}")


def update_account(
    account_id: str,
    email: str = None,
    metadata: dict = None,
):
    """Update a connected Account."""
    data = {}
    if email:
        data["email"] = email
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/accounts/{account_id}", data=data)


def delete_account(account_id: str):
    """Delete a connected Account."""
    return _req("DELETE", f"/accounts/{account_id}")


def list_accounts(limit: int = None, starting_after: str = None):
    """List connected Accounts."""
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    return _req("GET", "/accounts", params=params)


def create_account_link(
    account: str,
    refresh_url: str,
    return_url: str,
    type: str = "account_onboarding",
):
    """Create an Account Link for onboarding a connected account."""
    data = {
        "account": account,
        "refresh_url": refresh_url,
        "return_url": return_url,
        "type": type,
    }
    return _req("POST", "/account_links", data=data)


def create_login_link(account_id: str):
    """Create a Login Link for an Express connected account."""
    return _req("POST", f"/accounts/{account_id}/login_links")


# ── Transfers ─────────────────────────────────────────────────────────────────

def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    description: str = None,
    source_transaction: str = None,
    metadata: dict = None,
):
    """Create a Transfer to a connected account."""
    data = {"amount": amount, "currency": currency, "destination": destination}
    if description:
        data["description"] = description
    if source_transaction:
        data["source_transaction"] = source_transaction
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/transfers", data=data)


def get_transfer(transfer_id: str):
    """Retrieve a Transfer by ID."""
    return _req("GET", f"/transfers/{transfer_id}")


def update_transfer(transfer_id: str, description: str = None, metadata: dict = None):
    """Update a Transfer."""
    data = {}
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/transfers/{transfer_id}", data=data)


def list_transfers(
    destination: str = None,
    limit: int = None,
    starting_after: str = None,
):
    """List Transfers."""
    params = {}
    if destination:
        params["destination"] = destination
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    return _req("GET", "/transfers", params=params)


def create_transfer_reversal(
    transfer_id: str,
    amount: int = None,
    metadata: dict = None,
):
    """Reverse a Transfer."""
    data = {}
    if amount is not None:
        data["amount"] = amount
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/transfers/{transfer_id}/reversals", data=data)


# ── Payouts ───────────────────────────────────────────────────────────────────

def create_payout(
    amount: int,
    currency: str,
    description: str = None,
    method: str = None,
    metadata: dict = None,
    stripe_account: str = None,
):
    """Create a Payout to a bank account or debit card."""
    data = {"amount": amount, "currency": currency}
    if description:
        data["description"] = description
    if method:
        data["method"] = method
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/payouts", data=data, stripe_account=stripe_account)


def get_payout(payout_id: str, stripe_account: str = None):
    """Retrieve a Payout by ID."""
    return _req("GET", f"/payouts/{payout_id}", stripe_account=stripe_account)


def cancel_payout(payout_id: str, stripe_account: str = None):
    """Cancel a pending Payout."""
    return _req("POST", f"/payouts/{payout_id}/cancel", stripe_account=stripe_account)


def list_payouts(
    status: str = None,
    limit: int = None,
    starting_after: str = None,
    stripe_account: str = None,
):
    """List Payouts. status: 'pending','paid','failed','canceled'."""
    params = {}
    if status:
        params["status"] = status
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    return _req("GET", "/payouts", params=params, stripe_account=stripe_account)
