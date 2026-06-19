"""
Stripe Events tools.
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


def get_event(event_id: str) -> dict:
    """Retrieve an Event by ID."""
    resp = requests.get(f"{BASE_URL}/events/{event_id}", auth=_auth())
    return _handle(resp)


def list_events(
    type: str = None,
    object_id: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    created_gte: int = None,
    created_lte: int = None,
    delivery_success: bool = None,
) -> dict:
    """List Events."""
    params = {}
    if type:
        params["type"] = type
    if object_id:
        params["object_id"] = object_id
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
    if delivery_success is not None:
        params["delivery_success"] = str(delivery_success).lower()
    resp = requests.get(f"{BASE_URL}/events", params=params, auth=_auth())
    return _handle(resp)
