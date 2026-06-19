from typing import Any, Dict, Optional

from .http import stripe_request


# Subscriptions

def create_subscription(customer: str, items: list, default_payment_method: Optional[str] = None, trial_period_days: Optional[int] = None, metadata: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {"customer": customer, "items": items}
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if trial_period_days is not None:
        data["trial_period_days"] = trial_period_days
    if metadata is not None:
        data["metadata"] = metadata
    data.update(kwargs)
    res, err = stripe_request("POST", "/v1/subscriptions", data=data)
    return err or res  # type: ignore


def get_subscription(subscription_id: str) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/subscriptions/{subscription_id}")
    return err or res  # type: ignore


def update_subscription(subscription_id: str, **kwargs: Any) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/subscriptions/{subscription_id}", data=kwargs)
    return err or res  # type: ignore


def cancel_subscription(subscription_id: str, invoice_now: Optional[bool] = None, prorate: Optional[bool] = None) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if invoice_now is not None:
        data["invoice_now"] = invoice_now
    if prorate is not None:
        data["prorate"] = prorate
    res, err = stripe_request("DELETE", f"/v1/subscriptions/{subscription_id}", data=data)
    return err or res  # type: ignore


def list_subscriptions(limit: int = 10, customer: Optional[str] = None, status: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    if starting_after:
        params["starting_after"] = starting_after
    res, err = stripe_request("GET", "/v1/subscriptions", params=params)
    return err or res  # type: ignore


# Invoices

def create_invoice(customer: str, auto_advance: Optional[bool] = None, collection_method: Optional[str] = None, days_until_due: Optional[int] = None, metadata: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {"customer": customer}
    if auto_advance is not None:
        data["auto_advance"] = auto_advance
    if collection_method:
        data["collection_method"] = collection_method
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if metadata is not None:
        data["metadata"] = metadata
    data.update(kwargs)
    res, err = stripe_request("POST", "/v1/invoices", data=data)
    return err or res  # type: ignore


def get_invoice(invoice_id: str) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/invoices/{invoice_id}")
    return err or res  # type: ignore


def update_invoice(invoice_id: str, **kwargs: Any) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/invoices/{invoice_id}", data=kwargs)
    return err or res  # type: ignore


def finalize_invoice(invoice_id: str, **kwargs: Any) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/invoices/{invoice_id}/finalize", data=kwargs)
    return err or res  # type: ignore


def pay_invoice(invoice_id: str, paid_out_of_band: Optional[bool] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if paid_out_of_band is not None:
        data["paid_out_of_band"] = paid_out_of_band
    data.update(kwargs)
    res, err = stripe_request("POST", f"/v1/invoices/{invoice_id}/pay", data=data)
    return err or res  # type: ignore


def void_invoice(invoice_id: str) -> Dict[str, Any]:
    res, err = stripe_request("POST", f"/v1/invoices/{invoice_id}/void")
    return err or res  # type: ignore


def list_invoices(limit: int = 10, customer: Optional[str] = None, status: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if customer:
        params["customer"] = customer
    if status:
        params["status"] = status
    if starting_after:
        params["starting_after"] = starting_after
    res, err = stripe_request("GET", "/v1/invoices", params=params)
    return err or res  # type: ignore


# Invoice Items

def create_invoice_item(customer: str, price: Optional[str] = None, amount: Optional[int] = None, currency: Optional[str] = None, invoice: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, str]] = None, **kwargs: Any) -> Dict[str, Any]:
    data: Dict[str, Any] = {"customer": customer}
    if price:
        data["price"] = price
    if amount is not None:
        data["amount"] = amount
    if currency:
        data["currency"] = currency
    if invoice:
        data["invoice"] = invoice
    if description:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    data.update(kwargs)
    res, err = stripe_request("POST", "/v1/invoiceitems", data=data)
    return err or res  # type: ignore


def list_invoice_items(limit: int = 10, customer: Optional[str] = None, invoice: Optional[str] = None, starting_after: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if customer:
        params["customer"] = customer
    if invoice:
        params["invoice"] = invoice
    if starting_after:
        params["starting_after"] = starting_after
    res, err = stripe_request("GET", "/v1/invoiceitems", params=params)
    return err or res  # type: ignore
