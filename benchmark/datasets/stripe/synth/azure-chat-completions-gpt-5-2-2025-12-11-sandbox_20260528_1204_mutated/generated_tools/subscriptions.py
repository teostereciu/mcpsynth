from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_subscription(
    customer: str,
    items: list[Dict[str, Any]],
    *,
    currency: Optional[str] = None,
    customer_account: Optional[str] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    payment_behavior: Optional[str] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    add_invoice_items: Optional[list[Dict[str, Any]]] = None,
    application_fee_percent: Optional[float] = None,
    backdate_start_date: Optional[int] = None,
    billing_cycle_anchor: Optional[int] = None,
    billing_cycle_anchor_config: Optional[Dict[str, Any]] = None,
    billing_mode: Optional[Dict[str, Any]] = None,
    billing_thresholds: Optional[Dict[str, Any]] = None,
    cancel_at: Optional[Any] = None,
    cancel_at_period_end: Optional[bool] = None,
    collection_method: Optional[str] = None,
    days_until_due: Optional[int] = None,
    default_tax_rates: Optional[list[str]] = None,
    discounts: Optional[list[Dict[str, Any]]] = None,
    invoice_settings: Optional[Dict[str, Any]] = None,
    off_session: Optional[bool] = None,
    on_behalf_of: Optional[str] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    pending_invoice_item_interval: Optional[Dict[str, Any]] = None,
    proration_behavior: Optional[str] = None,
    transfer_data: Optional[Dict[str, Any]] = None,
    trial_end: Optional[Any] = None,
    trial_from_plan: Optional[bool] = None,
    trial_period_days: Optional[int] = None,
    trial_settings: Optional[Dict[str, Any]] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/subscriptions

    Doc: docs/subscriptions.md (Create a subscription)
    """
    params: Dict[str, Any] = {
        "customer": customer,
        "items": items,
        "currency": currency,
        "customer_account": customer_account,
        "default_payment_method": default_payment_method,
        "default_source": default_source,
        "description": description,
        "metadata": metadata,
        "payment_behavior": payment_behavior,
        "automatic_tax": automatic_tax,
        "add_invoice_items": add_invoice_items,
        "application_fee_percent": application_fee_percent,
        "backdate_start_date": backdate_start_date,
        "billing_cycle_anchor": billing_cycle_anchor,
        "billing_cycle_anchor_config": billing_cycle_anchor_config,
        "billing_mode": billing_mode,
        "billing_thresholds": billing_thresholds,
        "cancel_at": cancel_at,
        "cancel_at_period_end": cancel_at_period_end,
        "collection_method": collection_method,
        "days_until_due": days_until_due,
        "default_tax_rates": default_tax_rates,
        "discounts": discounts,
        "invoice_settings": invoice_settings,
        "off_session": off_session,
        "on_behalf_of": on_behalf_of,
        "payment_settings": payment_settings,
        "pending_invoice_item_interval": pending_invoice_item_interval,
        "proration_behavior": proration_behavior,
        "transfer_data": transfer_data,
        "trial_end": trial_end,
        "trial_from_plan": trial_from_plan,
        "trial_period_days": trial_period_days,
        "trial_settings": trial_settings,
        "expand": expand,
    }
    return stripe_request(
        "POST",
        "/v1/subscriptions",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_subscription(
    subscription_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/subscriptions/{subscription_id}

    Doc: docs/subscriptions.md (Retrieve a subscription)
    """
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request(
        "GET",
        f"/v1/subscriptions/{subscription_id}",
        params,
        stripe_account=stripe_account,
    )


def update_subscription(
    subscription_id: str,
    *,
    items: Optional[list[Dict[str, Any]]] = None,
    cancel_at_period_end: Optional[bool] = None,
    cancel_at: Optional[Any] = None,
    default_payment_method: Optional[str] = None,
    default_source: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    proration_behavior: Optional[str] = None,
    payment_behavior: Optional[str] = None,
    payment_settings: Optional[Dict[str, Any]] = None,
    pause_collection: Optional[Dict[str, Any]] = None,
    trial_end: Optional[Any] = None,
    trial_from_plan: Optional[bool] = None,
    trial_settings: Optional[Dict[str, Any]] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/subscriptions/{subscription_id}

    Doc: docs/subscriptions.md (Update a subscription)
    """
    params: Dict[str, Any] = {
        "items": items,
        "cancel_at_period_end": cancel_at_period_end,
        "cancel_at": cancel_at,
        "default_payment_method": default_payment_method,
        "default_source": default_source,
        "description": description,
        "metadata": metadata,
        "proration_behavior": proration_behavior,
        "payment_behavior": payment_behavior,
        "payment_settings": payment_settings,
        "pause_collection": pause_collection,
        "trial_end": trial_end,
        "trial_from_plan": trial_from_plan,
        "trial_settings": trial_settings,
        "expand": expand,
    }
    return stripe_request(
        "POST",
        f"/v1/subscriptions/{subscription_id}",
        params,
        stripe_account=stripe_account,
    )


def cancel_subscription(
    subscription_id: str,
    *,
    invoice_now: Optional[bool] = None,
    prorate: Optional[bool] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """DELETE /v1/subscriptions/{subscription_id}

    Doc: docs/subscriptions.md (Cancel a subscription)
    """
    params: Dict[str, Any] = {"invoice_now": invoice_now, "prorate": prorate}
    return stripe_request(
        "DELETE",
        f"/v1/subscriptions/{subscription_id}",
        params,
        stripe_account=stripe_account,
    )


def list_subscriptions(
    *,
    customer: Optional[str] = None,
    price: Optional[str] = None,
    status: Optional[str] = None,
    collection_method: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/subscriptions

    Doc: docs/subscriptions.md (List all subscriptions)
    """
    params: Dict[str, Any] = {
        "customer": customer,
        "price": price,
        "status": status,
        "collection_method": collection_method,
        "created": created,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request(
        "GET",
        "/v1/subscriptions",
        params,
        stripe_account=stripe_account,
    )
