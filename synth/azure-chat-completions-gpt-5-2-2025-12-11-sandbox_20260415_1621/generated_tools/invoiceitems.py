from typing import Any, Dict, List, Optional

from .stripe_client import stripe_request


def invoiceitems_create(
    *,
    customer: str,
    amount: Optional[int] = None,
    currency: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    period: Optional[Dict[str, Any]] = None,
    pricing: Optional[Dict[str, Any]] = None,
    invoice: Optional[str] = None,
    subscription: Optional[str] = None,
    quantity: Optional[int] = None,
    discountable: Optional[bool] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    tax_rates: Optional[List[str]] = None,
    tax_behavior: Optional[str] = None,
    tax_code: Optional[str] = None,
    price_data: Optional[Dict[str, Any]] = None,
    unit_amount_decimal: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"customer": customer}
    if amount is not None:
        data["amount"] = amount
    if currency is not None:
        data["currency"] = currency
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    if period is not None:
        data["period"] = period
    if pricing is not None:
        data["pricing"] = pricing
    if invoice is not None:
        data["invoice"] = invoice
    if subscription is not None:
        data["subscription"] = subscription
    if quantity is not None:
        data["quantity"] = quantity
    if discountable is not None:
        data["discountable"] = discountable
    if discounts is not None:
        data["discounts"] = discounts
    if tax_rates is not None:
        data["tax_rates"] = tax_rates
    if tax_behavior is not None:
        data["tax_behavior"] = tax_behavior
    if tax_code is not None:
        data["tax_code"] = tax_code
    if price_data is not None:
        data["price_data"] = price_data
    if unit_amount_decimal is not None:
        data["unit_amount_decimal"] = unit_amount_decimal
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        "/v1/invoiceitems",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def invoiceitems_retrieve(*, invoiceitem_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/invoiceitems/{invoiceitem_id}", stripe_account=stripe_account)


def invoiceitems_update(
    *,
    invoiceitem_id: str,
    amount: Optional[int] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    period: Optional[Dict[str, Any]] = None,
    pricing: Optional[Dict[str, Any]] = None,
    quantity: Optional[int] = None,
    discountable: Optional[bool] = None,
    discounts: Optional[List[Dict[str, Any]]] = None,
    tax_rates: Optional[List[str]] = None,
    tax_behavior: Optional[str] = None,
    tax_code: Optional[str] = None,
    price_data: Optional[Dict[str, Any]] = None,
    unit_amount_decimal: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    if amount is not None:
        data["amount"] = amount
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata
    if period is not None:
        data["period"] = period
    if pricing is not None:
        data["pricing"] = pricing
    if quantity is not None:
        data["quantity"] = quantity
    if discountable is not None:
        data["discountable"] = discountable
    if discounts is not None:
        data["discounts"] = discounts
    if tax_rates is not None:
        data["tax_rates"] = tax_rates
    if tax_behavior is not None:
        data["tax_behavior"] = tax_behavior
    if tax_code is not None:
        data["tax_code"] = tax_code
    if price_data is not None:
        data["price_data"] = price_data
    if unit_amount_decimal is not None:
        data["unit_amount_decimal"] = unit_amount_decimal
    if extra:
        data.update(extra)

    return stripe_request(
        "POST",
        f"/v1/invoiceitems/{invoiceitem_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def invoiceitems_delete(
    *,
    invoiceitem_id: str,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request("DELETE", f"/v1/invoiceitems/{invoiceitem_id}", stripe_account=stripe_account)


def invoiceitems_list(
    *,
    limit: Optional[int] = 10,
    customer: Optional[str] = None,
    invoice: Optional[str] = None,
    pending: Optional[bool] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_query: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    query: Dict[str, Any] = {}
    if limit is not None:
        query["limit"] = limit
    if customer is not None:
        query["customer"] = customer
    if invoice is not None:
        query["invoice"] = invoice
    if pending is not None:
        query["pending"] = pending
    if starting_after is not None:
        query["starting_after"] = starting_after
    if ending_before is not None:
        query["ending_before"] = ending_before
    if extra_query:
        query.update(extra_query)

    return stripe_request("GET", "/v1/invoiceitems", params=query, stripe_account=stripe_account)
