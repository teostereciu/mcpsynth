from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def invoices_create(
    *,
    customer: str,
    auto_advance: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "auto_advance": auto_advance,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "description": description,
        "metadata": metadata,
    }
    return stripe_request("POST", "/v1/invoices", params=params, stripe_account=stripe_account)


def invoices_retrieve(*, invoice_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/invoices/{invoice_id}", stripe_account=stripe_account)


def invoices_update(
    *,
    invoice_id: str,
    auto_advance: Optional[bool] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"auto_advance": auto_advance, "description": description, "metadata": metadata}
    return stripe_request("POST", f"/v1/invoices/{invoice_id}", params=params, stripe_account=stripe_account)


def invoices_finalize(*, invoice_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/invoices/{invoice_id}/finalize", stripe_account=stripe_account)


def invoices_pay(*, invoice_id: str, paid_out_of_band: Optional[bool] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"paid_out_of_band": paid_out_of_band}
    return stripe_request("POST", f"/v1/invoices/{invoice_id}/pay", params=params, stripe_account=stripe_account)


def invoices_void(*, invoice_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("POST", f"/v1/invoices/{invoice_id}/void", stripe_account=stripe_account)


def invoices_list(
    *,
    customer: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "status": status,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/invoices", params=params, stripe_account=stripe_account)
