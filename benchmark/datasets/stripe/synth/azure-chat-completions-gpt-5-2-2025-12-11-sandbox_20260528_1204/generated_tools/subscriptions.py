from typing import Any, Dict, Optional

from .http_client import stripe_request


# POST /v1/subscriptions
# GET /v1/subscriptions/{subscription}
# POST /v1/subscriptions/{subscription}
# DELETE /v1/subscriptions/{subscription}
# GET /v1/subscriptions


def create_subscription(
    customer: str,
    items: list[Dict[str, Any]],
    *,
    default_payment_method: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_behavior: Optional[str] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    trial_end: Optional[Any] = None,
    trial_period_days: Optional[int] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "items": items,
        "default_payment_method": default_payment_method,
        "description": description,
        "metadata": metadata,
        "payment_behavior": payment_behavior,
        "automatic_tax": automatic_tax,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "trial_end": trial_end,
        "trial_period_days": trial_period_days,
    }
    params.update(kwargs)
    return stripe_request(
        "POST",
        "/v1/subscriptions",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_subscription(subscription_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/subscriptions/{subscription_id}", stripe_account=stripe_account)


def update_subscription(
    subscription_id: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/subscriptions/{subscription_id}",
        params=params or {},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def cancel_subscription(
    subscription_id: str,
    *,
    invoice_now: Optional[bool] = None,
    prorate: Optional[bool] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"invoice_now": invoice_now, "prorate": prorate}
    return stripe_request(
        "DELETE",
        f"/v1/subscriptions/{subscription_id}",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_subscriptions(
    *,
    customer: Optional[str] = None,
    status: Optional[str] = None,
    price: Optional[str] = None,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "status": status,
        "price": price,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/subscriptions", params=params, stripe_account=stripe_account)
