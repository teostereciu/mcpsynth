from typing import Any, Dict, Optional

from generated_tools.stripe_common import stripe_request


def create_invoice(customer: str, auto_advance: Optional[bool] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> Any:
    return stripe_request("POST", "/v1/invoices", {"customer": customer, "auto_advance": auto_advance, "description": description, "metadata": metadata})


def retrieve_invoice(invoice_id: str) -> Any:
    return stripe_request("GET", f"/v1/invoices/{invoice_id}")


def update_invoice(invoice_id: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> Any:
    return stripe_request("POST", f"/v1/invoices/{invoice_id}", {"description": description, "metadata": metadata})


def list_invoices(customer: Optional[str] = None, subscription: Optional[str] = None, status: Optional[str] = None, limit: Optional[int] = 10) -> Any:
    return stripe_request("GET", "/v1/invoices", {"customer": customer, "subscription": subscription, "status": status, "limit": limit})


def finalize_invoice(invoice_id: str) -> Any:
    return stripe_request("POST", f"/v1/invoices/{invoice_id}/finalize")


def pay_invoice(invoice_id: str) -> Any:
    return stripe_request("POST", f"/v1/invoices/{invoice_id}/pay")


def void_invoice(invoice_id: str) -> Any:
    return stripe_request("POST", f"/v1/invoices/{invoice_id}/void")
