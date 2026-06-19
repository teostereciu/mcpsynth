from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def payment_intents_create(
    *,
    amount: int,
    currency: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    payment_method: Optional[str] = None,
    confirm: Optional[bool] = None,
    off_session: Optional[bool] = None,
    capture_method: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "customer": customer,
        "description": description,
        "receipt_email": receipt_email,
        "payment_method": payment_method,
        "confirm": confirm,
        "off_session": off_session,
        "capture_method": capture_method,
        "metadata": metadata,
        "automatic_payment_methods": automatic_payment_methods,
    }
    return stripe_request("POST", "/v1/payment_intents", params=params, stripe_account=stripe_account)


def payment_intents_retrieve(*, payment_intent_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}", stripe_account=stripe_account)


def payment_intents_update(
    *,
    payment_intent_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    receipt_email: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "description": description,
        "metadata": metadata,
        "receipt_email": receipt_email,
    }
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}", params=params, stripe_account=stripe_account)


def payment_intents_confirm(
    *,
    payment_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"payment_method": payment_method, "return_url": return_url}
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/confirm", params=params, stripe_account=stripe_account)


def payment_intents_capture(
    *,
    payment_intent_id: str,
    amount_to_capture: Optional[int] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"amount_to_capture": amount_to_capture}
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/capture", params=params, stripe_account=stripe_account)


def payment_intents_cancel(*, payment_intent_id: str, cancellation_reason: Optional[str] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"cancellation_reason": cancellation_reason}
    return stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/cancel", params=params, stripe_account=stripe_account)


def payment_intents_list(
    *,
    customer: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/payment_intents", params=params, stripe_account=stripe_account)
