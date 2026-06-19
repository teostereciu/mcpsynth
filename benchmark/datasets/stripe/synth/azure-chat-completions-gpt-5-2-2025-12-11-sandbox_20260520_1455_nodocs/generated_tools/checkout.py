from typing import Any, Dict, Optional

from .http import stripe_request


# Checkout Sessions

def create_checkout_session(mode: str, success_url: str, cancel_url: str, line_items: list, customer: Optional[str] = None, customer_email: Optional[str] = None, metadata: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "mode": mode,
        "success_url": success_url,
        "cancel_url": cancel_url,
        "line_items": line_items,
    }
    if customer:
        data["customer"] = customer
    if customer_email:
        data["customer_email"] = customer_email
    if metadata is not None:
        data["metadata"] = metadata
    data.update(kwargs)
    res, err = stripe_request("POST", "/v1/checkout/sessions", data=data)
    return err or res  # type: ignore


def get_checkout_session(session_id: str) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/checkout/sessions/{session_id}")
    return err or res  # type: ignore


def list_checkout_sessions(limit: int = 10, customer: Optional[str] = None, payment_intent: Optional[str] = None, subscription: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if customer:
        params["customer"] = customer
    if payment_intent:
        params["payment_intent"] = payment_intent
    if subscription:
        params["subscription"] = subscription
    if starting_after:
        params["starting_after"] = starting_after
    res, err = stripe_request("GET", "/v1/checkout/sessions", params=params)
    return err or res  # type: ignore


# Payment Links

def create_payment_link(line_items: list, after_completion: Optional[Dict[str, Any]] = None, metadata: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {"line_items": line_items}
    if after_completion is not None:
        data["after_completion"] = after_completion
    if metadata is not None:
        data["metadata"] = metadata
    data.update(kwargs)
    res, err = stripe_request("POST", "/v1/payment_links", data=data)
    return err or res  # type: ignore


def get_payment_link(payment_link_id: str) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/payment_links/{payment_link_id}")
    return err or res  # type: ignore


def update_payment_link(payment_link_id: str, **kwargs: Any) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/payment_links/{payment_link_id}", data=kwargs)
    return err or res  # type: ignore


def list_payment_links(limit: int = 10, active: Optional[bool] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if active is not None:
        params["active"] = active
    if starting_after:
        params["starting_after"] = starting_after
    res, err = stripe_request("GET", "/v1/payment_links", params=params)
    return err or res  # type: ignore
