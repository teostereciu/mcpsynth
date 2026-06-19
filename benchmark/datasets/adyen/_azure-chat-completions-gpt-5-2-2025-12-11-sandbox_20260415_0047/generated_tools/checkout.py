from __future__ import annotations

from typing import Any, Dict, Optional

from .http import adyen_request, default_merchant_account


def checkout_payment_methods(
    *,
    country_code: str,
    amount_value: int,
    currency: str,
    merchant_account: Optional[str] = None,
    shopper_locale: Optional[str] = None,
    shopper_reference: Optional[str] = None,
    channel: Optional[str] = None,
    additional_data: Optional[Dict[str, Any]] = None,
    allowed_payment_methods: Optional[list[str]] = None,
    blocked_payment_methods: Optional[list[str]] = None,
    store: Optional[str] = None,
    store_payment_method: Optional[bool] = None,
    shopper_ip: Optional[str] = None,
    shopper_email: Optional[str] = None,
    telephone_number: Optional[str] = None,
    browser_info: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /paymentMethods (Checkout v71)

    Retrieves available payment methods for a transaction.
    """

    ma = default_merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant account. Provide merchant_account or set ADYEN_MERCHANT_ACCOUNT."}

    payload: Dict[str, Any] = {
        "merchantAccount": ma,
        "countryCode": country_code,
        "amount": {"currency": currency, "value": amount_value},
    }
    if shopper_locale:
        payload["shopperLocale"] = shopper_locale
    if shopper_reference:
        payload["shopperReference"] = shopper_reference
    if channel:
        payload["channel"] = channel
    if additional_data:
        payload["additionalData"] = additional_data
    if allowed_payment_methods:
        payload["allowedPaymentMethods"] = allowed_payment_methods
    if blocked_payment_methods:
        payload["blockedPaymentMethods"] = blocked_payment_methods
    if store:
        payload["store"] = store
    if store_payment_method is not None:
        payload["storePaymentMethod"] = store_payment_method
    if shopper_ip:
        payload["shopperIP"] = shopper_ip
    if shopper_email:
        payload["shopperEmail"] = shopper_email
    if telephone_number:
        payload["telephoneNumber"] = telephone_number
    if browser_info:
        payload["browserInfo"] = browser_info

    return adyen_request(service="checkout", method="POST", path="/paymentMethods", json=payload)


def checkout_create_session(
    *,
    amount_value: int,
    currency: str,
    reference: str,
    return_url: str,
    merchant_account: Optional[str] = None,
    country_code: Optional[str] = None,
    shopper_locale: Optional[str] = None,
    shopper_reference: Optional[str] = None,
    store_payment_method: Optional[bool] = None,
    shopper_ip: Optional[str] = None,
    shopper_email: Optional[str] = None,
    risk_data: Optional[Dict[str, Any]] = None,
    line_items: Optional[list[Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    installments: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /sessions (Checkout v71)

    Creates a Checkout session.
    """

    ma = default_merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant account. Provide merchant_account or set ADYEN_MERCHANT_ACCOUNT."}

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
    if store_payment_method is not None:
        payload["storePaymentMethod"] = store_payment_method
    if shopper_ip:
        payload["shopperIP"] = shopper_ip
    if shopper_email:
        payload["shopperEmail"] = shopper_email
    if risk_data:
        payload["riskData"] = risk_data
    if line_items:
        payload["lineItems"] = line_items
    if metadata:
        payload["metadata"] = metadata
    if installments:
        payload["installments"] = installments

    return adyen_request(service="checkout", method="POST", path="/sessions", json=payload)


def checkout_get_session(*, session_id: str) -> Dict[str, Any]:
    """GET /sessions/{sessionId} (Checkout v71)"""

    return adyen_request(service="checkout", method="GET", path=f"/sessions/{session_id}")


def checkout_get_payment_link(*, link_id: str) -> Dict[str, Any]:
    """GET /paymentLinks/{linkId} (Checkout v71)"""

    return adyen_request(service="checkout", method="GET", path=f"/paymentLinks/{link_id}")


def checkout_create_payment_link(
    *,
    amount_value: int,
    currency: str,
    reference: str,
    return_url: str,
    merchant_account: Optional[str] = None,
    country_code: Optional[str] = None,
    shopper_locale: Optional[str] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /paymentLinks (Checkout v71)"""

    ma = default_merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant account. Provide merchant_account or set ADYEN_MERCHANT_ACCOUNT."}

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
    if description:
        payload["description"] = description

    return adyen_request(service="checkout", method="POST", path="/paymentLinks", json=payload)


def checkout_update_payment_link(*, link_id: str, patch: Dict[str, Any]) -> Dict[str, Any]:
    """PATCH /paymentLinks/{linkId} (Checkout v71)"""

    return adyen_request(service="checkout", method="PATCH", path=f"/paymentLinks/{link_id}", json=patch)


def checkout_list_stored_payment_methods(
    *,
    shopper_reference: str,
    merchant_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /storedPaymentMethods (Checkout v71)"""

    ma = default_merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant account. Provide merchant_account or set ADYEN_MERCHANT_ACCOUNT."}

    return adyen_request(
        service="checkout",
        method="GET",
        path="/storedPaymentMethods",
        params={"merchantAccount": ma, "shopperReference": shopper_reference},
    )


def checkout_delete_stored_payment_method(*, stored_payment_method_id: str) -> Dict[str, Any]:
    """DELETE /storedPaymentMethods/{storedPaymentMethodId} (Checkout v71)"""

    return adyen_request(
        service="checkout",
        method="DELETE",
        path=f"/storedPaymentMethods/{stored_payment_method_id}",
    )
