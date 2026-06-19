"""Stripe Disputes, Balance, and Balance Transactions tools."""
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


# ── Balance ───────────────────────────────────────────────────────────────────

def get_balance():
    """Retrieve the current account Balance."""
    return _req("GET", "/balance")


def list_balance_transactions(
    type: str = None,
    source: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
):
    """List Balance Transactions. type: 'charge','refund','transfer', etc."""
    params = {}
    if type:
        params["type"] = type
    if source:
        params["source"] = source
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    return _req("GET", "/balance_transactions", params=params)


def get_balance_transaction(transaction_id: str):
    """Retrieve a Balance Transaction by ID."""
    return _req("GET", f"/balance_transactions/{transaction_id}")


# ── Disputes ──────────────────────────────────────────────────────────────────

def get_dispute(dispute_id: str):
    """Retrieve a Dispute by ID."""
    return _req("GET", f"/disputes/{dispute_id}")


def update_dispute(
    dispute_id: str,
    evidence: dict = None,
    submit: bool = None,
    metadata: dict = None,
):
    """Update a Dispute with evidence."""
    data = {}
    if evidence:
        for k, v in evidence.items():
            data[f"evidence[{k}]"] = v
    if submit is not None:
        data["submit"] = str(submit).lower()
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/disputes/{dispute_id}", data=data)


def close_dispute(dispute_id: str):
    """Close a Dispute (accept it)."""
    return _req("POST", f"/disputes/{dispute_id}/close")


def list_disputes(
    charge: str = None,
    payment_intent: str = None,
    status: str = None,
    limit: int = None,
    starting_after: str = None,
):
    """List Disputes."""
    params = {}
    if charge:
        params["charge"] = charge
    if payment_intent:
        params["payment_intent"] = payment_intent
    if status:
        params["status"] = status
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    return _req("GET", "/disputes", params=params)


# ── Events ────────────────────────────────────────────────────────────────────

def get_event(event_id: str):
    """Retrieve an Event by ID."""
    return _req("GET", f"/events/{event_id}")


def list_events(
    type: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
):
    """List Events. type: e.g. 'payment_intent.succeeded'."""
    params = {}
    if type:
        params["type"] = type
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    return _req("GET", "/events", params=params)
