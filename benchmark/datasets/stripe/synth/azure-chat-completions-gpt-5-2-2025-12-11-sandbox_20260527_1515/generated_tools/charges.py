from typing import Any, Dict, Optional

from .http_client import stripe_request


def retrieve_charge(
    charge_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request("GET", f"/v1/charges/{charge_id}", params=params, stripe_account=stripe_account)


def update_charge(
    charge_id: str,
    *,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    shipping: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "description": description,
        "receipt_email": receipt_email,
        "metadata": metadata,
        "shipping": shipping,
    }
    return stripe_request("POST", f"/v1/charges/{charge_id}", params=params, stripe_account=stripe_account)


def list_charges(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_intent": payment_intent,
        "created": created,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request("GET", "/v1/charges", params=params, stripe_account=stripe_account)
