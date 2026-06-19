from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def create_invoice(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices"""
    return stripe_request(
        "POST",
        "/v1/invoices",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_invoice(
    invoice_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/invoices/{id}"""
    return stripe_request("GET", f"/v1/invoices/{invoice_id}", None, stripe_account=stripe_account)


def update_invoice(
    invoice_id: str,
    *,
    params: Dict[str, Any],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices/{id}"""
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def finalize_invoice(
    invoice_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices/{id}/finalize"""
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/finalize",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def pay_invoice(
    invoice_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices/{id}/pay"""
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/pay",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def void_invoice(
    invoice_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices/{id}/void"""
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/void",
        None,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def create_preview_invoice(
    *,
    params: Dict[str, Any],
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices/create_preview"""
    return stripe_request(
        "POST",
        "/v1/invoices/create_preview",
        params,
        stripe_account=stripe_account,
    )


def list_invoices(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/invoices"""
    return stripe_request("GET", "/v1/invoices", params, stripe_account=stripe_account)
