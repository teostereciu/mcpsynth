"""
Stripe Webhook Endpoints tools.
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


def create_webhook_endpoint(
    url: str,
    enabled_events: list,
    description: str = None,
    metadata: dict = None,
    api_version: str = None,
    connect: bool = None,
) -> dict:
    """Create a Webhook Endpoint. enabled_events: list of event type strings or ['*']."""
    data = {"url": url}
    for i, event in enumerate(enabled_events):
        data[f"enabled_events[{i}]"] = event
    if description:
        data["description"] = description
    if api_version:
        data["api_version"] = api_version
    if connect is not None:
        data["connect"] = str(connect).lower()
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/webhook_endpoints", data=data, auth=_auth())
    return _handle(resp)


def get_webhook_endpoint(webhook_endpoint_id: str) -> dict:
    """Retrieve a Webhook Endpoint by ID."""
    resp = requests.get(
        f"{BASE_URL}/webhook_endpoints/{webhook_endpoint_id}", auth=_auth()
    )
    return _handle(resp)


def update_webhook_endpoint(
    webhook_endpoint_id: str,
    url: str = None,
    enabled_events: list = None,
    description: str = None,
    disabled: bool = None,
    metadata: dict = None,
) -> dict:
    """Update a Webhook Endpoint."""
    data = {}
    if url:
        data["url"] = url
    if enabled_events:
        for i, event in enumerate(enabled_events):
            data[f"enabled_events[{i}]"] = event
    if description:
        data["description"] = description
    if disabled is not None:
        data["disabled"] = str(disabled).lower()
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(
        f"{BASE_URL}/webhook_endpoints/{webhook_endpoint_id}",
        data=data,
        auth=_auth(),
    )
    return _handle(resp)


def delete_webhook_endpoint(webhook_endpoint_id: str) -> dict:
    """Delete a Webhook Endpoint."""
    resp = requests.delete(
        f"{BASE_URL}/webhook_endpoints/{webhook_endpoint_id}", auth=_auth()
    )
    return _handle(resp)


def list_webhook_endpoints(
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
) -> dict:
    """List Webhook Endpoints."""
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    resp = requests.get(
        f"{BASE_URL}/webhook_endpoints", params=params, auth=_auth()
    )
    return _handle(resp)
