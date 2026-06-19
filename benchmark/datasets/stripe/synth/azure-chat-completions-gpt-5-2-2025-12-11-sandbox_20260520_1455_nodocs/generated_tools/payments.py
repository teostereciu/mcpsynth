from typing import Any, Dict, Optional

from .http import stripe_request


# Payment Intents

def create_payment_intent(amount: int, currency: str = "usd", customer: Optional[str] = None, payment_method: Optional[str] = None, confirm: Optional[bool] = None, off_session: Optional[bool] = None, description: Optional[str] = None, receipt_email: Optional[str] = None, metadata: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {"amount": amount, "currency": currency}
    if customer is not None:
        data["customer"] = customer
    if payment_method is not None:
        data["payment_method"] = payment_method
    if confirm is not None:
        data["confirm"] = confirm
    if off_session is not None:
        data["off_session"] = off_session
    if description is not None:
        data["description"] = description
    if receipt_email is not None:
        data["receipt_email"] = receipt_email
    if metadata is not None:
        data["metadata"] = metadata
    data.update(kwargs)
    res, err = stripe_request("POST", "/v1/payment_intents", data=data)
    return err or res  # type: ignore


def get_payment_intent(payment_intent_id: str) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}")
    return err or res  # type: ignore


def update_payment_intent(payment_intent_id: str, **kwargs: Any) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}", data=kwargs)
    return err or res  # type: ignore


def confirm_payment_intent(payment_intent_id: str, payment_method: Optional[str] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if payment_method is not None:
        data["payment_method"] = payment_method
    data.update(kwargs)
    res, err = stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/confirm", data=data)
    return err or res  # type: ignore


def cancel_payment_intent(payment_intent_id: str, cancellation_reason: Optional[str] = None) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if cancellation_reason:
        data["cancellation_reason"] = cancellation_reason
    res, err = stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/cancel", data=data)
    return err or res  # type: ignore


def list_payment_intents(limit: int = 10, customer: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if customer:
        params["customer"] = customer
    if starting_after:
        params["starting_after"] = starting_after
    res, err = stripe_request("GET", "/v1/payment_intents", params=params)
    return err or res  # type: ignore


# Charges

def get_charge(charge_id: str) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/charges/{charge_id}")
    return err or res  # type: ignore


def list_charges(limit: int = 10, customer: Optional[str] = None, payment_intent: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if customer:
        params["customer"] = customer
    if payment_intent:
        params["payment_intent"] = payment_intent
    if starting_after:
        params["starting_after"] = starting_after
    res, err = stripe_request("GET", "/v1/charges", params=params)
    return err or res  # type: ignore


# Refunds

def create_refund(charge: Optional[str] = None, payment_intent: Optional[str] = None, amount: Optional[int] = None, reason: Optional[str] = None, metadata: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if charge:
        data["charge"] = charge
    if payment_intent:
        data["payment_intent"] = payment_intent
    if amount is not None:
        data["amount"] = amount
    if reason:
        data["reason"] = reason
    if metadata is not None:
        data["metadata"] = metadata
    data.update(kwargs)
    res, err = stripe_request("POST", "/v1/refunds", data=data)
    return err or res  # type: ignore


def get_refund(refund_id: str) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/refunds/{refund_id}")
    return err or res  # type: ignore


def update_refund(refund_id: str, **kwargs: Any) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/refunds/{refund_id}", data=kwargs)
    return err or res  # type: ignore


def list_refunds(limit: int = 10, charge: Optional[str] = None, payment_intent: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if charge:
        params["charge"] = charge
    if payment_intent:
        params["payment_intent"] = payment_intent
    if starting_after:
        params["starting_after"] = starting_after
    res, err = stripe_request("GET", "/v1/refunds", params=params)
    return err or res  # type: ignore


# Setup Intents

def create_setup_intent(customer: Optional[str] = None, payment_method_types: Optional[list] = None, usage: Optional[str] = None, metadata: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if customer:
        data["customer"] = customer
    if payment_method_types is not None:
        data["payment_method_types"] = payment_method_types
    if usage:
        data["usage"] = usage
    if metadata is not None:
        data["metadata"] = metadata
    data.update(kwargs)
    res, err = stripe_request("POST", "/v1/setup_intents", data=data)
    return err or res  # type: ignore


def get_setup_intent(setup_intent_id: str) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/setup_intents/{setup_intent_id}")
    return err or res  # type: ignore


def confirm_setup_intent(setup_intent_id: str, payment_method: Optional[str] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if payment_method:
        data["payment_method"] = payment_method
    data.update(kwargs)
    res, err = stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/confirm", data=data)
    return err or res  # type: ignore


def cancel_setup_intent(setup_intent_id: str) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/setup_intents/{setup_intent_id}/cancel")
    return err or res  # type: ignore


def list_setup_intents(limit: int = 10, customer: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if customer:
        params["customer"] = customer
    if starting_after:
        params["starting_after"] = starting_after
    res, err = stripe_request("GET", "/v1/setup_intents", params=params)
    return err or res  # type: ignore
