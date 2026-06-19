from typing import Any, Dict, Optional

from .http_client import adyen_base_urls, request_json, with_merchant_account


def checkout_create_session(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Checkout API: POST /sessions (v71)

    Creates a payment session for Drop-in/Components/Hosted Checkout.
    If merchantAccount is not provided, uses ADYEN_MERCHANT_ACCOUNT.
    """
    base = adyen_base_urls()["checkout"]
    url = f"{base}/sessions"
    return request_json("POST", url, json_body=with_merchant_account(payload))


def checkout_get_session(session_id: str) -> Dict[str, Any]:
    """Checkout API: GET /sessions/{sessionId} (v71)"""
    base = adyen_base_urls()["checkout"]
    url = f"{base}/sessions/{session_id}"
    return request_json("GET", url)


def checkout_payment_methods(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Checkout API: POST /paymentMethods (v71)

    Returns available payment methods for a shopper/context.
    """
    base = adyen_base_urls()["checkout"]
    url = f"{base}/paymentMethods"
    return request_json("POST", url, json_body=with_merchant_account(payload))


def checkout_payments(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Checkout API: POST /payments (v71)

    Starts a payment. For redirects/additional actions, response contains action.
    """
    base = adyen_base_urls()["checkout"]
    url = f"{base}/payments"
    return request_json("POST", url, json_body=with_merchant_account(payload))


def checkout_payments_details(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Checkout API: POST /payments/details (v71)

    Submits additional payment details (redirect result, 3DS, etc.).
    """
    base = adyen_base_urls()["checkout"]
    url = f"{base}/payments/details"
    return request_json("POST", url, json_body=payload)


def checkout_payments_capture(payment_psp_reference: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Checkout API: POST /payments/{paymentPspReference}/captures (v71)"""
    base = adyen_base_urls()["checkout"]
    url = f"{base}/payments/{payment_psp_reference}/captures"
    return request_json("POST", url, json_body=with_merchant_account(payload))


def checkout_payments_refund(payment_psp_reference: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Checkout API: POST /payments/{paymentPspReference}/refunds (v71)"""
    base = adyen_base_urls()["checkout"]
    url = f"{base}/payments/{payment_psp_reference}/refunds"
    return request_json("POST", url, json_body=with_merchant_account(payload))


def checkout_payments_cancel(payment_psp_reference: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Checkout API: POST /payments/{paymentPspReference}/cancels (v71)"""
    base = adyen_base_urls()["checkout"]
    url = f"{base}/payments/{payment_psp_reference}/cancels"
    return request_json("POST", url, json_body=with_merchant_account(payload))


def checkout_payment_links_create(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Checkout API: POST /paymentLinks (v71)"""
    base = adyen_base_urls()["checkout"]
    url = f"{base}/paymentLinks"
    return request_json("POST", url, json_body=with_merchant_account(payload))


def checkout_payment_links_get(link_id: str) -> Dict[str, Any]:
    """Checkout API: GET /paymentLinks/{linkId} (v71)"""
    base = adyen_base_urls()["checkout"]
    url = f"{base}/paymentLinks/{link_id}"
    return request_json("GET", url)


def checkout_payment_links_update(link_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Checkout API: PATCH /paymentLinks/{linkId} (v71)"""
    base = adyen_base_urls()["checkout"]
    url = f"{base}/paymentLinks/{link_id}"
    return request_json("PATCH", url, json_body=payload)


def checkout_stored_payment_methods_list(shopper_reference: Optional[str] = None) -> Dict[str, Any]:
    """Checkout API: GET /storedPaymentMethods (v71)

    If shopperReference is provided, filters stored payment methods.
    """
    base = adyen_base_urls()["checkout"]
    url = f"{base}/storedPaymentMethods"
    params = {}
    if shopper_reference:
        params["shopperReference"] = shopper_reference
    return request_json("GET", url, params=params or None)


def checkout_stored_payment_method_delete(stored_payment_method_id: str) -> Dict[str, Any]:
    """Checkout API: DELETE /storedPaymentMethods/{storedPaymentMethodId} (v71)"""
    base = adyen_base_urls()["checkout"]
    url = f"{base}/storedPaymentMethods/{stored_payment_method_id}"
    return request_json("DELETE", url)
