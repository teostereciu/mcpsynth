from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def setup_intents_create(
    *,
    customer: Optional[str] = None,
    payment_method_types: Optional[list[str]] = None,
    usage: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_method_types": payment_method_types,
        "usage": usage,
        "metadata": metadata,
    }
    return stripe_request("POST", "/v1/setup_intents", params=params, stripe_account=stripe_account)


def setup_intents_retrieve(*, setup_intent_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/setup_intents/{setup_intent_id}", stripe_account=stripe_account)


def setup_intents_confirm(
    *,
    setup_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"payment_method": payment_method, "return_url": return_url}
    return stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/confirm", params=params, stripe_account=stripe_account)


def setup_intents_list(
    *,
    customer: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"customer": customer, "limit": limit, "starting_after": starting_after, "ending_before": ending_before}
    return stripe_request("GET", "/v1/setup_intents", params=params, stripe_account=stripe_account)
