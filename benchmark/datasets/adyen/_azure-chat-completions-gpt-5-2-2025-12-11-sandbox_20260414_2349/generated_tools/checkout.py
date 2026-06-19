"""Adyen Checkout API (v71) tools."""

from __future__ import annotations

import os
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP

from .http import adyen_request

mcp = FastMCP("adyen")


def _default_merchant_account(merchant_account: Optional[str]) -> Optional[str]:
    return merchant_account or os.environ.get("ADYEN_MERCHANT_ACCOUNT")


@mcp.tool()
def checkout_payment_methods(
    country_code: str,
    amount_value: int,
    currency: str,
    merchant_account: Optional[str] = None,
    shopper_locale: Optional[str] = None,
    shopper_reference: Optional[str] = None,
    shopper_ip: Optional[str] = None,
    shopper_email: Optional[str] = None,
    allowed_payment_methods: Optional[List[str]] = None,
    blocked_payment_methods: Optional[List[str]] = None,
    channel: Optional[str] = None,
    additional_data: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Get available payment methods.

    Maps to POST /paymentMethods
    """

    ma = _default_merchant_account(merchant_account)
    if not ma:
        return {"error": {"message": "merchant_account is required (or set ADYEN_MERCHANT_ACCOUNT)"}}

    payload: Dict[str, Any] = {
        "merchantAccount": ma,
        "countryCode": country_code,
        "amount": {"currency": currency, "value": amount_value},
    }
    if shopper_locale:
        payload["shopperLocale"] = shopper_locale
    if shopper_reference:
        payload["shopperReference"] = shopper_reference
    if shopper_ip:
        payload["shopperIP"] = shopper_ip
    if shopper_email:
        payload["shopperEmail"] = shopper_email
    if allowed_payment_methods:
        payload["allowedPaymentMethods"] = allowed_payment_methods
    if blocked_payment_methods:
        payload["blockedPaymentMethods"] = blocked_payment_methods
    if channel:
        payload["channel"] = channel
    if additional_data:
        payload["additionalData"] = additional_data

    return adyen_request("checkout", "POST", "/paymentMethods", json=payload)


@mcp.tool()
def checkout_create_session(
    amount_value: int,
    currency: str,
    reference: str,
    return_url: str,
    merchant_account: Optional[str] = None,
    country_code: Optional[str] = None,
    shopper_locale: Optional[str] = None,
    shopper_reference: Optional[str] = None,
    shopper_email: Optional[str] = None,
    shopper_ip: Optional[str] = None,
    store_payment_method: Optional[bool] = None,
    recurring_processing_model: Optional[str] = None,
    line_items: Optional[List[Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, str]] = None,
    installments: Optional[Dict[str, Any]] = None,
    risk_data: Optional[Dict[str, Any]] = None,
    additional_data: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Create a Checkout session.

    Maps to POST /sessions
    """

    ma = _default_merchant_account(merchant_account)
    if not ma:
        return {"error": {"message": "merchant_account is required (or set ADYEN_MERCHANT_ACCOUNT)"}}

    payload: Dict[str, Any] = {
        "merchantAccount": ma,
        "amount": {"currency": currency, "value": amount_value},
        "reference": reference,
        "returnUrl": return_url,
    }
    if country_code:
        payload["countryCode"] = country_code
    if shopper_locale:
        payload["shopperLocale"] = shopper_locale
    if shopper_reference:
        payload["shopperReference"] = shopper_reference
    if shopper_email:
        payload["shopperEmail"] = shopper_email
    if shopper_ip:
        payload["shopperIP"] = shopper_ip
    if store_payment_method is not None:
        payload["storePaymentMethod"] = store_payment_method
    if recurring_processing_model:
        payload["recurringProcessingModel"] = recurring_processing_model
    if line_items:
        payload["lineItems"] = line_items
    if metadata:
        payload["metadata"] = metadata
    if installments:
        payload["installments"] = installments
    if risk_data:
        payload["riskData"] = risk_data
    if additional_data:
        payload["additionalData"] = additional_data

    return adyen_request("checkout", "POST", "/sessions", json=payload)


@mcp.tool()
def checkout_get_session(session_id: str) -> Dict[str, Any]:
    """Get session details.

    Maps to GET /sessions/{sessionId}
    """

    return adyen_request("checkout", "GET", f"/sessions/{session_id}")


@mcp.tool()
def checkout_get_payment_link(link_id: str) -> Dict[str, Any]:
    """Get a payment link.

    Maps to GET /paymentLinks/{linkId}
    """

    return adyen_request("checkout", "GET", f"/paymentLinks/{link_id}")


@mcp.tool()
def checkout_create_payment_link(
    amount_value: int,
    currency: str,
    reference: str,
    return_url: Optional[str] = None,
    merchant_account: Optional[str] = None,
    country_code: Optional[str] = None,
    shopper_locale: Optional[str] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a payment link.

    Maps to POST /paymentLinks
    """

    ma = _default_merchant_account(merchant_account)
    if not ma:
        return {"error": {"message": "merchant_account is required (or set ADYEN_MERCHANT_ACCOUNT)"}}

    payload: Dict[str, Any] = {
        "merchantAccount": ma,
        "amount": {"currency": currency, "value": amount_value},
        "reference": reference,
    }
    if return_url:
        payload["returnUrl"] = return_url
    if country_code:
        payload["countryCode"] = country_code
    if shopper_locale:
        payload["shopperLocale"] = shopper_locale
    if description:
        payload["description"] = description

    return adyen_request("checkout", "POST", "/paymentLinks", json=payload)


@mcp.tool()
def checkout_list_stored_payment_methods(
    shopper_reference: str,
    merchant_account: Optional[str] = None,
) -> Dict[str, Any]:
    """List stored payment methods for a shopper.

    Maps to GET /storedPaymentMethods
    """

    ma = _default_merchant_account(merchant_account)
    if not ma:
        return {"error": {"message": "merchant_account is required (or set ADYEN_MERCHANT_ACCOUNT)"}}

    params = {"merchantAccount": ma, "shopperReference": shopper_reference}
    return adyen_request("checkout", "GET", "/storedPaymentMethods", params=params)


@mcp.tool()
def checkout_delete_stored_payment_method(stored_payment_method_id: str) -> Dict[str, Any]:
    """Delete a stored payment method.

    Maps to DELETE /storedPaymentMethods/{storedPaymentMethodId}
    """

    return adyen_request("checkout", "DELETE", f"/storedPaymentMethods/{stored_payment_method_id}")
