from typing import Any, Dict

from .http_client import stripe_request, stripe_list_all


def invoices_create(customer: str, **kwargs) -> Dict[str, Any]:
    params = {"customer": customer}
    params.update(kwargs)
    return stripe_request("POST", "/v1/invoices", params)


def invoices_retrieve(invoice_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/invoices/{invoice_id}", kwargs or None)


def invoices_update(invoice_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/invoices/{invoice_id}", kwargs)


def invoices_finalize(invoice_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/invoices/{invoice_id}/finalize", kwargs)


def invoices_pay(invoice_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/invoices/{invoice_id}/pay", kwargs)


def invoices_void(invoice_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/invoices/{invoice_id}/void", kwargs)


def invoices_mark_uncollectible(invoice_id: str, **kwargs) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/invoices/{invoice_id}/mark_uncollectible", kwargs)


def invoices_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/invoices", params)


def invoices_list_all(limit: int = 100, **kwargs) -> Dict[str, Any]:
    return stripe_list_all("/v1/invoices", kwargs, limit=limit)


def invoiceitems_create(customer: str, **kwargs) -> Dict[str, Any]:
    params = {"customer": customer}
    params.update(kwargs)
    return stripe_request("POST", "/v1/invoiceitems", params)


def invoiceitems_list(limit: int = 10, **kwargs) -> Dict[str, Any]:
    params = {"limit": limit}
    params.update(kwargs)
    return stripe_request("GET", "/v1/invoiceitems", params)
