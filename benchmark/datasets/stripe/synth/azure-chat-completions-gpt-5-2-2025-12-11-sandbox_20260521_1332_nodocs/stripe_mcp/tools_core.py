from typing import Any, Dict, Optional

from .http import stripe_request


def _ok(data: Any) -> Any:
    return data


def _err(e: Dict[str, Any]) -> Dict[str, Any]:
    return e


# Customers
async def create_customer(
    *,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Any:
    data = {
        "email": email,
        "name": name,
        "phone": phone,
        "description": description,
        "metadata": metadata,
    }
    res, err = stripe_request("POST", "/v1/customers", data=data)
    return _ok(res) if not err else _err(err)


async def get_customer(*, customer_id: str) -> Any:
    res, err = stripe_request("GET", f"/v1/customers/{customer_id}")
    return _ok(res) if not err else _err(err)


async def update_customer(
    *,
    customer_id: str,
    email: Optional[str] = None,
    name: Optional[str] = None,
    phone: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Any:
    data = {
        "email": email,
        "name": name,
        "phone": phone,
        "description": description,
        "metadata": metadata,
    }
    res, err = stripe_request("POST", f"/v1/customers/{customer_id}", data=data)
    return _ok(res) if not err else _err(err)


async def delete_customer(*, customer_id: str) -> Any:
    res, err = stripe_request("DELETE", f"/v1/customers/{customer_id}")
    return _ok(res) if not err else _err(err)


async def list_customers(
    *,
    email: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
) -> Any:
    query = {
        "email": email,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    res, err = stripe_request("GET", "/v1/customers", query=query)
    return _ok(res) if not err else _err(err)


# Payment Intents
async def create_payment_intent(
    *,
    amount: int,
    currency: str,
    customer: Optional[str] = None,
    description: Optional[str] = None,
    receipt_email: Optional[str] = None,
    payment_method: Optional[str] = None,
    confirm: Optional[bool] = None,
    off_session: Optional[bool] = None,
    capture_method: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    automatic_payment_methods: Optional[Dict[str, Any]] = None,
) -> Any:
    data = {
        "amount": amount,
        "currency": currency,
        "customer": customer,
        "description": description,
        "receipt_email": receipt_email,
        "payment_method": payment_method,
        "confirm": confirm,
        "off_session": off_session,
        "capture_method": capture_method,
        "metadata": metadata,
        "automatic_payment_methods": automatic_payment_methods,
    }
    res, err = stripe_request("POST", "/v1/payment_intents", data=data)
    return _ok(res) if not err else _err(err)


async def get_payment_intent(*, payment_intent_id: str) -> Any:
    res, err = stripe_request("GET", f"/v1/payment_intents/{payment_intent_id}")
    return _ok(res) if not err else _err(err)


async def update_payment_intent(
    *,
    payment_intent_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Any:
    data = {"description": description, "metadata": metadata}
    res, err = stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}", data=data)
    return _ok(res) if not err else _err(err)


async def confirm_payment_intent(
    *,
    payment_intent_id: str,
    payment_method: Optional[str] = None,
    return_url: Optional[str] = None,
) -> Any:
    data = {"payment_method": payment_method, "return_url": return_url}
    res, err = stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/confirm", data=data)
    return _ok(res) if not err else _err(err)


async def cancel_payment_intent(*, payment_intent_id: str) -> Any:
    res, err = stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/cancel")
    return _ok(res) if not err else _err(err)


async def capture_payment_intent(*, payment_intent_id: str, amount_to_capture: Optional[int] = None) -> Any:
    data = {"amount_to_capture": amount_to_capture}
    res, err = stripe_request("POST", f"/v1/payment_intents/{payment_intent_id}/capture", data=data)
    return _ok(res) if not err else _err(err)


async def list_payment_intents(
    *,
    customer: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
) -> Any:
    query = {"customer": customer, "limit": limit, "starting_after": starting_after}
    res, err = stripe_request("GET", "/v1/payment_intents", query=query)
    return _ok(res) if not err else _err(err)


# Charges
async def list_charges(*, customer: Optional[str] = None, payment_intent: Optional[str] = None, limit: int = 10) -> Any:
    query = {"customer": customer, "payment_intent": payment_intent, "limit": limit}
    res, err = stripe_request("GET", "/v1/charges", query=query)
    return _ok(res) if not err else _err(err)


async def get_charge(*, charge_id: str) -> Any:
    res, err = stripe_request("GET", f"/v1/charges/{charge_id}")
    return _ok(res) if not err else _err(err)


# Refunds
async def create_refund(
    *,
    charge: Optional[str] = None,
    payment_intent: Optional[str] = None,
    amount: Optional[int] = None,
    reason: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Any:
    data = {
        "charge": charge,
        "payment_intent": payment_intent,
        "amount": amount,
        "reason": reason,
        "metadata": metadata,
    }
    res, err = stripe_request("POST", "/v1/refunds", data=data)
    return _ok(res) if not err else _err(err)


async def get_refund(*, refund_id: str) -> Any:
    res, err = stripe_request("GET", f"/v1/refunds/{refund_id}")
    return _ok(res) if not err else _err(err)


async def list_refunds(*, charge: Optional[str] = None, payment_intent: Optional[str] = None, limit: int = 10) -> Any:
    query = {"charge": charge, "payment_intent": payment_intent, "limit": limit}
    res, err = stripe_request("GET", "/v1/refunds", query=query)
    return _ok(res) if not err else _err(err)
