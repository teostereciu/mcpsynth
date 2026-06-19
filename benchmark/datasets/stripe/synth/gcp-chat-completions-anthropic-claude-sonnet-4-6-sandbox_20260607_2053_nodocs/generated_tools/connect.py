"""
Stripe Connect tools: Accounts, Transfers, Payouts, Account Links, External Accounts.
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


# ── Connected Accounts ───────────────────────────────────────────────────────

def create_account(
    type: str = "express",
    country: str = None,
    email: str = None,
    capabilities: dict = None,
    business_type: str = None,
    business_profile_url: str = None,
    business_profile_mcc: str = None,
    metadata: dict = None,
    tos_acceptance_date: int = None,
    tos_acceptance_ip: str = None,
) -> dict:
    """Create a connected Account. type: 'standard', 'express', or 'custom'."""
    data = {"type": type}
    if country:
        data["country"] = country
    if email:
        data["email"] = email
    if business_type:
        data["business_type"] = business_type
    if business_profile_url:
        data["business_profile[url]"] = business_profile_url
    if business_profile_mcc:
        data["business_profile[mcc]"] = business_profile_mcc
    if tos_acceptance_date is not None:
        data["tos_acceptance[date]"] = tos_acceptance_date
    if tos_acceptance_ip:
        data["tos_acceptance[ip]"] = tos_acceptance_ip
    if capabilities:
        for cap, settings in capabilities.items():
            for setting_key, setting_val in settings.items():
                data[f"capabilities[{cap}][{setting_key}]"] = setting_val
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/accounts", data=data, auth=_auth())
    return _handle(resp)


def get_account(account_id: str) -> dict:
    """Retrieve a connected Account by ID."""
    resp = requests.get(f"{BASE_URL}/accounts/{account_id}", auth=_auth())
    return _handle(resp)


def update_account(
    account_id: str,
    email: str = None,
    business_profile_url: str = None,
    business_profile_name: str = None,
    metadata: dict = None,
    tos_acceptance_date: int = None,
    tos_acceptance_ip: str = None,
) -> dict:
    """Update a connected Account."""
    data = {}
    if email:
        data["email"] = email
    if business_profile_url:
        data["business_profile[url]"] = business_profile_url
    if business_profile_name:
        data["business_profile[name]"] = business_profile_name
    if tos_acceptance_date is not None:
        data["tos_acceptance[date]"] = tos_acceptance_date
    if tos_acceptance_ip:
        data["tos_acceptance[ip]"] = tos_acceptance_ip
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(
        f"{BASE_URL}/accounts/{account_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def delete_account(account_id: str) -> dict:
    """Delete a connected Account."""
    resp = requests.delete(f"{BASE_URL}/accounts/{account_id}", auth=_auth())
    return _handle(resp)


def list_accounts(
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    created_gte: int = None,
    created_lte: int = None,
) -> dict:
    """List connected Accounts."""
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
    resp = requests.get(f"{BASE_URL}/accounts", params=params, auth=_auth())
    return _handle(resp)


def reject_account(account_id: str, reason: str) -> dict:
    """Reject a connected Account. reason: 'fraud', 'terms_of_service', or 'other'."""
    data = {"reason": reason}
    resp = requests.post(
        f"{BASE_URL}/accounts/{account_id}/reject", data=data, auth=_auth()
    )
    return _handle(resp)


# ── Account Links ────────────────────────────────────────────────────────────

def create_account_link(
    account: str,
    refresh_url: str,
    return_url: str,
    type: str = "account_onboarding",
    collect: str = None,
) -> dict:
    """Create an Account Link for onboarding a connected account."""
    data = {
        "account": account,
        "refresh_url": refresh_url,
        "return_url": return_url,
        "type": type,
    }
    if collect:
        data["collect"] = collect
    resp = requests.post(f"{BASE_URL}/account_links", data=data, auth=_auth())
    return _handle(resp)


# ── Transfers ────────────────────────────────────────────────────────────────

def create_transfer(
    amount: int,
    currency: str,
    destination: str,
    description: str = None,
    source_transaction: str = None,
    transfer_group: str = None,
    metadata: dict = None,
) -> dict:
    """Create a Transfer to a connected account."""
    data = {
        "amount": amount,
        "currency": currency,
        "destination": destination,
    }
    if description:
        data["description"] = description
    if source_transaction:
        data["source_transaction"] = source_transaction
    if transfer_group:
        data["transfer_group"] = transfer_group
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/transfers", data=data, auth=_auth())
    return _handle(resp)


def get_transfer(transfer_id: str) -> dict:
    """Retrieve a Transfer by ID."""
    resp = requests.get(f"{BASE_URL}/transfers/{transfer_id}", auth=_auth())
    return _handle(resp)


def update_transfer(
    transfer_id: str,
    description: str = None,
    metadata: dict = None,
) -> dict:
    """Update a Transfer."""
    data = {}
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(
        f"{BASE_URL}/transfers/{transfer_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def list_transfers(
    destination: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    created_gte: int = None,
    created_lte: int = None,
    transfer_group: str = None,
) -> dict:
    """List Transfers."""
    params = {}
    if destination:
        params["destination"] = destination
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
    if transfer_group:
        params["transfer_group"] = transfer_group
    resp = requests.get(f"{BASE_URL}/transfers", params=params, auth=_auth())
    return _handle(resp)


def create_transfer_reversal(
    transfer_id: str,
    amount: int = None,
    description: str = None,
    metadata: dict = None,
    refund_application_fee: bool = None,
) -> dict:
    """Reverse a Transfer."""
    data = {}
    if amount is not None:
        data["amount"] = amount
    if description:
        data["description"] = description
    if refund_application_fee is not None:
        data["refund_application_fee"] = str(refund_application_fee).lower()
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(
        f"{BASE_URL}/transfers/{transfer_id}/reversals", data=data, auth=_auth()
    )
    return _handle(resp)


# ── Payouts ──────────────────────────────────────────────────────────────────

def create_payout(
    amount: int,
    currency: str,
    description: str = None,
    method: str = None,
    source_type: str = None,
    statement_descriptor: str = None,
    metadata: dict = None,
    stripe_account: str = None,
) -> dict:
    """Create a Payout to a bank account or debit card."""
    data = {"amount": amount, "currency": currency}
    if description:
        data["description"] = description
    if method:
        data["method"] = method
    if source_type:
        data["source_type"] = source_type
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    headers = {}
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    resp = requests.post(
        f"{BASE_URL}/payouts", data=data, auth=_auth(), headers=headers
    )
    return _handle(resp)


def get_payout(payout_id: str, stripe_account: str = None) -> dict:
    """Retrieve a Payout by ID."""
    headers = {}
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    resp = requests.get(
        f"{BASE_URL}/payouts/{payout_id}", auth=_auth(), headers=headers
    )
    return _handle(resp)


def update_payout(
    payout_id: str, metadata: dict = None, stripe_account: str = None
) -> dict:
    """Update a Payout."""
    data = {}
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    headers = {}
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    resp = requests.post(
        f"{BASE_URL}/payouts/{payout_id}", data=data, auth=_auth(), headers=headers
    )
    return _handle(resp)


def cancel_payout(payout_id: str, stripe_account: str = None) -> dict:
    """Cancel a Payout."""
    headers = {}
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    resp = requests.post(
        f"{BASE_URL}/payouts/{payout_id}/cancel",
        data={},
        auth=_auth(),
        headers=headers,
    )
    return _handle(resp)


def list_payouts(
    status: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    arrival_date_gte: int = None,
    arrival_date_lte: int = None,
    stripe_account: str = None,
) -> dict:
    """List Payouts."""
    params = {}
    if status:
        params["status"] = status
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if arrival_date_gte is not None:
        params["arrival_date[gte]"] = arrival_date_gte
    if arrival_date_lte is not None:
        params["arrival_date[lte]"] = arrival_date_lte
    headers = {}
    if stripe_account:
        headers["Stripe-Account"] = stripe_account
    resp = requests.get(
        f"{BASE_URL}/payouts", params=params, auth=_auth(), headers=headers
    )
    return _handle(resp)
