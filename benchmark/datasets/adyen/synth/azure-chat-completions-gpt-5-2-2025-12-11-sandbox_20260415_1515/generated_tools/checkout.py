from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import checkout_url, merchant_account, request_json


def _with_merchant(body: Dict[str, Any], merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    ma = merchantAccount or merchant_account()
    if ma and "merchantAccount" not in body:
        body = dict(body)
        body["merchantAccount"] = ma
    return body


# Sessions

def checkout_create_session(body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /sessions (Checkout v71)

    Body should follow Adyen Checkout PaymentSessionRequest.
    """
    body2 = _with_merchant(body, merchantAccount)
    return request_json("POST", checkout_url("/sessions", "v71"), json_body=body2)


def checkout_get_session(sessionId: str) -> Dict[str, Any]:
    """GET /sessions/{sessionId} (Checkout v71)"""
    return request_json("GET", checkout_url(f"/sessions/{sessionId}", "v71"))


# Payment methods

def checkout_payment_methods(body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /paymentMethods (Checkout v71)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json("POST", checkout_url("/paymentMethods", "v71"), json_body=body2)


def checkout_payment_methods_balance(body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /paymentMethods/balance (Checkout v71)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json("POST", checkout_url("/paymentMethods/balance", "v71"), json_body=body2)


# Payments

def checkout_payments(body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /payments (Checkout v71)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json("POST", checkout_url("/payments", "v71"), json_body=body2)


def checkout_payments_details(body: Dict[str, Any]) -> Dict[str, Any]:
    """POST /payments/details (Checkout v71)"""
    return request_json("POST", checkout_url("/payments/details", "v71"), json_body=body)


def checkout_payments_amount_update(paymentPspReference: str, body: Dict[str, Any]) -> Dict[str, Any]:
    """POST /payments/{paymentPspReference}/amountUpdates (Checkout v71)"""
    return request_json(
        "POST",
        checkout_url(f"/payments/{paymentPspReference}/amountUpdates", "v71"),
        json_body=body,
    )


def checkout_payments_capture(paymentPspReference: str, body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /payments/{paymentPspReference}/captures (Checkout v71)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json(
        "POST",
        checkout_url(f"/payments/{paymentPspReference}/captures", "v71"),
        json_body=body2,
    )


def checkout_payments_refund(paymentPspReference: str, body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /payments/{paymentPspReference}/refunds (Checkout v71)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json(
        "POST",
        checkout_url(f"/payments/{paymentPspReference}/refunds", "v71"),
        json_body=body2,
    )


def checkout_payments_cancel(paymentPspReference: str, body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /payments/{paymentPspReference}/cancels (Checkout v71)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json(
        "POST",
        checkout_url(f"/payments/{paymentPspReference}/cancels", "v71"),
        json_body=body2,
    )


def checkout_payments_reversal(paymentPspReference: str, body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /payments/{paymentPspReference}/reversals (Checkout v71)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json(
        "POST",
        checkout_url(f"/payments/{paymentPspReference}/reversals", "v71"),
        json_body=body2,
    )


# Payment links

def checkout_create_payment_link(body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /paymentLinks (Checkout v71)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json("POST", checkout_url("/paymentLinks", "v71"), json_body=body2)


def checkout_get_payment_link(linkId: str) -> Dict[str, Any]:
    """GET /paymentLinks/{linkId} (Checkout v71)"""
    return request_json("GET", checkout_url(f"/paymentLinks/{linkId}", "v71"))


def checkout_update_payment_link(linkId: str, body: Dict[str, Any]) -> Dict[str, Any]:
    """PATCH /paymentLinks/{linkId} (Checkout v71)"""
    return request_json("PATCH", checkout_url(f"/paymentLinks/{linkId}", "v71"), json_body=body)


# Stored payment methods

def checkout_list_stored_payment_methods(*, shopperReference: str, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """GET /storedPaymentMethods?shopperReference=... (Checkout v71)"""
    params = {"shopperReference": shopperReference}
    ma = merchantAccount or merchant_account()
    if ma:
        params["merchantAccount"] = ma
    return request_json("GET", checkout_url("/storedPaymentMethods", "v71"), params=params)


def checkout_delete_stored_payment_method(storedPaymentMethodId: str) -> Dict[str, Any]:
    """DELETE /storedPaymentMethods/{storedPaymentMethodId} (Checkout v71)"""
    return request_json("DELETE", checkout_url(f"/storedPaymentMethods/{storedPaymentMethodId}", "v71"))
