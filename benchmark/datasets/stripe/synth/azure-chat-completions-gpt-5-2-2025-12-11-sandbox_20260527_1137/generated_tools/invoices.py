from typing import Any, Dict, List, Optional

from .http_client import stripe_request, _maybe_expand


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


def create_preview_invoice(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices/create_preview"""
    return stripe_request("POST", "/v1/invoices/create_preview", params or {}, stripe_account=stripe_account)


def update_invoice(
    invoice_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices/{invoice}"""
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_invoice(
    invoice_id: str,
    *,
    expand: Optional[List[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/invoices/{invoice}"""
    return stripe_request(
        "GET",
        f"/v1/invoices/{invoice_id}",
        _maybe_expand({}, expand),
        stripe_account=stripe_account,
    )


def list_invoices(
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/invoices"""
    return stripe_request("GET", "/v1/invoices", params or {}, stripe_account=stripe_account)


def finalize_invoice(
    invoice_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices/{invoice}/finalize"""
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/finalize",
        params or {},
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
    """POST /v1/invoices/{invoice}/pay"""
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/pay",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def void_invoice(
    invoice_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/invoices/{invoice}/void"""
    return stripe_request(
        "POST",
        f"/v1/invoices/{invoice_id}/void",
        params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def search_invoices(
    query: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/invoices/search"""
    p = {"query": query}
    p.update(params or {})
    return stripe_request("GET", "/v1/invoices/search", p, stripe_account=stripe_account)
