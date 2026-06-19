"""Classic Payments API (PAL Payment v68) tools."""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

from fastmcp import FastMCP

from ._http import adyen_base_urls, adyen_request

mcp = FastMCP("adyen")


def _merchant_account(merchant_account: Optional[str] = None) -> Optional[str]:
    return merchant_account or os.environ.get("ADYEN_MERCHANT_ACCOUNT")


@mcp.tool
def payments_authorise(*, payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /authorise - authorise a payment (classic integration)."""
    if "merchantAccount" not in payload:
        ma = _merchant_account(None)
        if ma:
            payload = {**payload, "merchantAccount": ma}
    return adyen_request(method="POST", base_url=adyen_base_urls()["payment"], path="/authorise", json=payload)


@mcp.tool
def payments_capture(
    *,
    payment_psp_reference: str,
    modification_reference: str,
    amount: Optional[Dict[str, Any]] = None,
    merchant_account: Optional[str] = None,
    additional_data: Optional[Dict[str, Any]] = None,
    splits: Optional[list[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """POST /capture - capture an authorisation (classic integration)."""
    ma = _merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant_account (or ADYEN_MERCHANT_ACCOUNT env var)"}

    payload: Dict[str, Any] = {
        "merchantAccount": ma,
        "originalReference": payment_psp_reference,
        "reference": modification_reference,
    }
    if amount is not None:
        payload["modificationAmount"] = amount
    if additional_data:
        payload["additionalData"] = additional_data
    if splits:
        payload["splits"] = splits

    return adyen_request(method="POST", base_url=adyen_base_urls()["payment"], path="/capture", json=payload)


@mcp.tool
def payments_refund(
    *,
    payment_psp_reference: str,
    modification_reference: str,
    amount: Optional[Dict[str, Any]] = None,
    merchant_account: Optional[str] = None,
    additional_data: Optional[Dict[str, Any]] = None,
    splits: Optional[list[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """POST /refund - refund a captured payment (classic integration)."""
    ma = _merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant_account (or ADYEN_MERCHANT_ACCOUNT env var)"}

    payload: Dict[str, Any] = {
        "merchantAccount": ma,
        "originalReference": payment_psp_reference,
        "reference": modification_reference,
    }
    if amount is not None:
        payload["modificationAmount"] = amount
    if additional_data:
        payload["additionalData"] = additional_data
    if splits:
        payload["splits"] = splits

    return adyen_request(method="POST", base_url=adyen_base_urls()["payment"], path="/refund", json=payload)


@mcp.tool
def payments_cancel(*, payment_psp_reference: str, modification_reference: str, merchant_account: Optional[str] = None) -> Dict[str, Any]:
    """POST /cancel - cancel an authorisation (classic integration)."""
    ma = _merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant_account (or ADYEN_MERCHANT_ACCOUNT env var)"}
    payload = {"merchantAccount": ma, "originalReference": payment_psp_reference, "reference": modification_reference}
    return adyen_request(method="POST", base_url=adyen_base_urls()["payment"], path="/cancel", json=payload)


@mcp.tool
def payments_cancel_or_refund(
    *, payment_psp_reference: str, modification_reference: str, merchant_account: Optional[str] = None
) -> Dict[str, Any]:
    """POST /cancelOrRefund - cancel if not captured, otherwise refund."""
    ma = _merchant_account(merchant_account)
    if not ma:
        return {"error": "Missing merchant_account (or ADYEN_MERCHANT_ACCOUNT env var)"}
    payload = {"merchantAccount": ma, "originalReference": payment_psp_reference, "reference": modification_reference}
    return adyen_request(method="POST", base_url=adyen_base_urls()["payment"], path="/cancelOrRefund", json=payload)
