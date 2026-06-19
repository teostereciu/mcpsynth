from __future__ import annotations

from typing import Any, Dict, Optional

from .http import adyen_request, default_merchant_account


def payment_authorise(
    *,
    merchant_account: Optional[str] = None,
    amount_value: int,
    currency: str,
    reference: str,
    payment_method: Dict[str, Any],
    shopper_reference: Optional[str] = None,
    shopper_email: Optional[str] = None,
    shopper_ip: Optional[str] = None,
    shopper_interaction: Optional[str] = None,
    recurring: Optional[Dict[str, Any]] = None,
    additional_data: Optional[Dict[str, Any]] = None,
    browser_info: Optional[Dict[str, Any]] = None,
    billing_address: Optional[Dict[str, Any]] = None,
    delivery_address: Optional[Dict[str, Any]] = None,
    installments: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /authorise (Payment v68 - classic integration)."""

    ma = default_merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant account. Provide merchant_account or set ADYEN_MERCHANT_ACCOUNT."}

    payload: Dict[str, Any] = {
        "merchantAccount": ma,
        "amount": {"currency": currency, "value": amount_value},
        "reference": reference,
        "paymentMethod": payment_method,
    }
    if shopper_reference:
        payload["shopperReference"] = shopper_reference
    if shopper_email:
        payload["shopperEmail"] = shopper_email
    if shopper_ip:
        payload["shopperIP"] = shopper_ip
    if shopper_interaction:
        payload["shopperInteraction"] = shopper_interaction
    if recurring:
        payload["recurring"] = recurring
    if additional_data:
        payload["additionalData"] = additional_data
    if browser_info:
        payload["browserInfo"] = browser_info
    if billing_address:
        payload["billingAddress"] = billing_address
    if delivery_address:
        payload["deliveryAddress"] = delivery_address
    if installments:
        payload["installments"] = installments

    return adyen_request(service="payment", method="POST", path="/authorise", json=payload)


def payment_capture(*, merchant_account: Optional[str] = None, psp_reference: str, amount: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /capture (Payment v68)"""

    ma = default_merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant account. Provide merchant_account or set ADYEN_MERCHANT_ACCOUNT."}

    payload: Dict[str, Any] = {"merchantAccount": ma, "originalReference": psp_reference}
    if amount:
        payload["modificationAmount"] = amount
    return adyen_request(service="payment", method="POST", path="/capture", json=payload)


def payment_refund(*, merchant_account: Optional[str] = None, psp_reference: str, amount: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /refund (Payment v68)"""

    ma = default_merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant account. Provide merchant_account or set ADYEN_MERCHANT_ACCOUNT."}

    payload: Dict[str, Any] = {"merchantAccount": ma, "originalReference": psp_reference}
    if amount:
        payload["modificationAmount"] = amount
    return adyen_request(service="payment", method="POST", path="/refund", json=payload)


def payment_cancel(*, merchant_account: Optional[str] = None, psp_reference: str) -> Dict[str, Any]:
    """POST /cancel (Payment v68)"""

    ma = default_merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant account. Provide merchant_account or set ADYEN_MERCHANT_ACCOUNT."}

    payload: Dict[str, Any] = {"merchantAccount": ma, "originalReference": psp_reference}
    return adyen_request(service="payment", method="POST", path="/cancel", json=payload)


def payment_cancel_or_refund(*, merchant_account: Optional[str] = None, psp_reference: str) -> Dict[str, Any]:
    """POST /cancelOrRefund (Payment v68)"""

    ma = default_merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant account. Provide merchant_account or set ADYEN_MERCHANT_ACCOUNT."}

    payload: Dict[str, Any] = {"merchantAccount": ma, "originalReference": psp_reference}
    return adyen_request(service="payment", method="POST", path="/cancelOrRefund", json=payload)
