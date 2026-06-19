from typing import Any, Dict, List, Optional

from .stripe_client import stripe_request


def checkout_sessions_create(
    *,
    mode: str,
    success_url: str,
    cancel_url: str,
    line_items: Optional[List[Dict[str, Any]]] = None,
    customer: Optional[str] = None,
    customer_email: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "mode": mode,
        "success_url": success_url,
        "cancel_url": cancel_url,
        "line_items": line_items,
        "customer": customer,
        "customer_email": customer_email,
        "metadata": metadata,
        "allow_promotion_codes": allow_promotion_codes,
    }
    return stripe_request("POST", "/v1/checkout/sessions", params=params, stripe_account=stripe_account)


def checkout_sessions_retrieve(*, session_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/checkout/sessions/{session_id}", stripe_account=stripe_account)


def checkout_sessions_list(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    subscription: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_intent": payment_intent,
        "subscription": subscription,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/checkout/sessions", params=params, stripe_account=stripe_account)
