"""Checkout API (v71) tools."""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

from fastmcp import FastMCP

from ._http import adyen_base_urls, adyen_request

mcp = FastMCP("adyen")


def _merchant_account(merchant_account: Optional[str] = None) -> Optional[str]:
    return merchant_account or os.environ.get("ADYEN_MERCHANT_ACCOUNT")


@mcp.tool
def checkout_payment_methods(
    *,
    country_code: str,
    amount: Dict[str, Any],
    merchant_account: Optional[str] = None,
    channel: Optional[str] = None,
    locale: Optional[str] = None,
    shopper_reference: Optional[str] = None,
    shopper_email: Optional[str] = None,
    shopper_ip: Optional[str] = None,
    store_payment_method: Optional[bool] = None,
    additional_data: Optional[Dict[str, Any]] = None,
    allowed_payment_methods: Optional[list[str]] = None,
    blocked_payment_methods: Optional[list[str]] = None,
) -> Dict[str, Any]:
    """POST /paymentMethods - list available payment methods."""

    ma = _merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant_account (or ADYEN_MERCHANT_ACCOUNT env var)"}

    payload: Dict[str, Any] = {
        "merchantAccount": ma,
        "countryCode": country_code,
        "amount": amount,
    }
    if channel:
        payload["channel"] = channel
    if locale:
        payload["shopperLocale"] = locale
    if shopper_reference:
        payload["shopperReference"] = shopper_reference
    if shopper_email:
        payload["shopperEmail"] = shopper_email
    if shopper_ip:
        payload["shopperIP"] = shopper_ip
    if store_payment_method is not None:
        payload["storePaymentMethod"] = store_payment_method
    if additional_data:
        payload["additionalData"] = additional_data
    if allowed_payment_methods:
        payload["allowedPaymentMethods"] = allowed_payment_methods
    if blocked_payment_methods:
        payload["blockedPaymentMethods"] = blocked_payment_methods

    return adyen_request(method="POST", base_url=adyen_base_urls()["checkout"], path="/paymentMethods", json=payload)


@mcp.tool
def checkout_sessions_create(
    *,
    amount: Dict[str, Any],
    reference: str,
    return_url: str,
    merchant_account: Optional[str] = None,
    country_code: Optional[str] = None,
    locale: Optional[str] = None,
    line_items: Optional[list[Dict[str, Any]]] = None,
    shopper_reference: Optional[str] = None,
    shopper_email: Optional[str] = None,
    shopper_ip: Optional[str] = None,
    store_payment_method: Optional[bool] = None,
    risk_data: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    installments: Optional[Dict[str, Any]] = None,
    additional_data: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /sessions - create a Checkout session."""

    ma = _merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant_account (or ADYEN_MERCHANT_ACCOUNT env var)"}

    payload: Dict[str, Any] = {
        "merchantAccount": ma,
        "amount": amount,
        "reference": reference,
        "returnUrl": return_url,
    }
    if country_code:
        payload["countryCode"] = country_code
    if locale:
        payload["shopperLocale"] = locale
    if line_items:
        payload["lineItems"] = line_items
    if shopper_reference:
        payload["shopperReference"] = shopper_reference
    if shopper_email:
        payload["shopperEmail"] = shopper_email
    if shopper_ip:
        payload["shopperIP"] = shopper_ip
    if store_payment_method is not None:
        payload["storePaymentMethod"] = store_payment_method
    if risk_data:
        payload["riskData"] = risk_data
    if metadata:
        payload["metadata"] = metadata
    if installments:
        payload["installments"] = installments
    if additional_data:
        payload["additionalData"] = additional_data

    return adyen_request(method="POST", base_url=adyen_base_urls()["checkout"], path="/sessions", json=payload)


@mcp.tool
def checkout_sessions_get(*, session_id: str) -> Dict[str, Any]:
    """GET /sessions/{sessionId} - retrieve a session."""
    return adyen_request(method="GET", base_url=adyen_base_urls()["checkout"], path=f"/sessions/{session_id}")


@mcp.tool
def checkout_payment_links_create(
    *,
    amount: Dict[str, Any],
    reference: str,
    return_url: str,
    merchant_account: Optional[str] = None,
    country_code: Optional[str] = None,
    shopper_locale: Optional[str] = None,
    description: Optional[str] = None,
    expires_at: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /paymentLinks - create a payment link."""

    ma = _merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant_account (or ADYEN_MERCHANT_ACCOUNT env var)"}

    payload: Dict[str, Any] = {
        "merchantAccount": ma,
        "amount": amount,
        "reference": reference,
        "returnUrl": return_url,
    }
    if country_code:
        payload["countryCode"] = country_code
    if shopper_locale:
        payload["shopperLocale"] = shopper_locale
    if description:
        payload["description"] = description
    if expires_at:
        payload["expiresAt"] = expires_at

    return adyen_request(method="POST", base_url=adyen_base_urls()["checkout"], path="/paymentLinks", json=payload)


@mcp.tool
def checkout_payment_links_get(*, link_id: str) -> Dict[str, Any]:
    """GET /paymentLinks/{linkId} - retrieve a payment link."""
    return adyen_request(method="GET", base_url=adyen_base_urls()["checkout"], path=f"/paymentLinks/{link_id}")


@mcp.tool
def checkout_payment_links_update(*, link_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """PATCH /paymentLinks/{linkId} - update a payment link."""
    return adyen_request(method="PATCH", base_url=adyen_base_urls()["checkout"], path=f"/paymentLinks/{link_id}", json=payload)


@mcp.tool
def checkout_stored_payment_methods_list(*, merchant_account: Optional[str] = None, shopper_reference: Optional[str] = None) -> Dict[str, Any]:
    """GET /storedPaymentMethods - list stored payment methods."""
    ma = _merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant_account (or ADYEN_MERCHANT_ACCOUNT env var)"}
    params: Dict[str, Any] = {"merchantAccount": ma}
    if shopper_reference:
        params["shopperReference"] = shopper_reference
    return adyen_request(method="GET", base_url=adyen_base_urls()["checkout"], path="/storedPaymentMethods", params=params)


@mcp.tool
def checkout_stored_payment_methods_delete(*, stored_payment_method_id: str) -> Dict[str, Any]:
    """DELETE /storedPaymentMethods/{storedPaymentMethodId} - delete stored payment method."""
    return adyen_request(
        method="DELETE",
        base_url=adyen_base_urls()["checkout"],
        path=f"/storedPaymentMethods/{stored_payment_method_id}",
    )
