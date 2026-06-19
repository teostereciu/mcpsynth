from typing import Any, Dict

from .http_client import adyen_base_urls, request_json, with_merchant_account


def payment_authorise(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Payment API (classic): POST /authorise (v68)"""
    base = adyen_base_urls()["payment"]
    url = f"{base}/authorise"
    return request_json("POST", url, json_body=with_merchant_account(payload))


def payment_capture(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Payment API (classic): POST /capture (v68)"""
    base = adyen_base_urls()["payment"]
    url = f"{base}/capture"
    return request_json("POST", url, json_body=with_merchant_account(payload))


def payment_refund(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Payment API (classic): POST /refund (v68)"""
    base = adyen_base_urls()["payment"]
    url = f"{base}/refund"
    return request_json("POST", url, json_body=with_merchant_account(payload))


def payment_cancel(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Payment API (classic): POST /cancel (v68)"""
    base = adyen_base_urls()["payment"]
    url = f"{base}/cancel"
    return request_json("POST", url, json_body=with_merchant_account(payload))


def payment_cancel_or_refund(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Payment API (classic): POST /cancelOrRefund (v68)"""
    base = adyen_base_urls()["payment"]
    url = f"{base}/cancelOrRefund"
    return request_json("POST", url, json_body=with_merchant_account(payload))


def payment_adjust_authorisation(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Payment API (classic): POST /adjustAuthorisation (v68)"""
    base = adyen_base_urls()["payment"]
    url = f"{base}/adjustAuthorisation"
    return request_json("POST", url, json_body=with_merchant_account(payload))


def payment_technical_cancel(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Payment API (classic): POST /technicalCancel (v68)"""
    base = adyen_base_urls()["payment"]
    url = f"{base}/technicalCancel"
    return request_json("POST", url, json_body=with_merchant_account(payload))
