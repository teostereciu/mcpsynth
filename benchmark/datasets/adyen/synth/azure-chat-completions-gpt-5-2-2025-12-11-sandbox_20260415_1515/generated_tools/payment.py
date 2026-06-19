from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import merchant_account, pal_url, request_json


def _with_merchant(body: Dict[str, Any], merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    ma = merchantAccount or merchant_account()
    if ma and "merchantAccount" not in body:
        body = dict(body)
        body["merchantAccount"] = ma
    return body


def payment_authorise(body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /authorise (Payment v68)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json("POST", pal_url("/authorise", "v68"), json_body=body2)


def payment_authorise3d(body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /authorise3d (Payment v68)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json("POST", pal_url("/authorise3d", "v68"), json_body=body2)


def payment_authorise3ds2(body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /authorise3ds2 (Payment v68)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json("POST", pal_url("/authorise3ds2", "v68"), json_body=body2)


def payment_get_authentication_result(body: Dict[str, Any]) -> Dict[str, Any]:
    """POST /getAuthenticationResult (Payment v68)"""
    return request_json("POST", pal_url("/getAuthenticationResult", "v68"), json_body=body)


def payment_retrieve_3ds2_result(body: Dict[str, Any]) -> Dict[str, Any]:
    """POST /retrieve3ds2Result (Payment v68)"""
    return request_json("POST", pal_url("/retrieve3ds2Result", "v68"), json_body=body)


def payment_adjust_authorisation(body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /adjustAuthorisation (Payment v68)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json("POST", pal_url("/adjustAuthorisation", "v68"), json_body=body2)


def payment_capture(body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /capture (Payment v68)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json("POST", pal_url("/capture", "v68"), json_body=body2)


def payment_refund(body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /refund (Payment v68)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json("POST", pal_url("/refund", "v68"), json_body=body2)


def payment_cancel(body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /cancel (Payment v68)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json("POST", pal_url("/cancel", "v68"), json_body=body2)


def payment_cancel_or_refund(body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /cancelOrRefund (Payment v68)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json("POST", pal_url("/cancelOrRefund", "v68"), json_body=body2)


def payment_technical_cancel(body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /technicalCancel (Payment v68)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json("POST", pal_url("/technicalCancel", "v68"), json_body=body2)


def payment_void_pending_refund(body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /voidPendingRefund (Payment v68)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json("POST", pal_url("/voidPendingRefund", "v68"), json_body=body2)


def payment_donate(body: Dict[str, Any], *, merchantAccount: Optional[str] = None) -> Dict[str, Any]:
    """POST /donate (Payment v68)"""
    body2 = _with_merchant(body, merchantAccount)
    return request_json("POST", pal_url("/donate", "v68"), json_body=body2)
