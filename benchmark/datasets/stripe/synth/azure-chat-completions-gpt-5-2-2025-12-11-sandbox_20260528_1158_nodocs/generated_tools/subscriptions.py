from typing import Any, Dict, List, Optional

from .stripe_client import stripe_request


def subscriptions_create(
    *,
    customer: str,
    items: List[Dict[str, Any]],
    default_payment_method: Optional[str] = None,
    trial_period_days: Optional[int] = None,
    coupon: Optional[str] = None,
    promotion_code: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "items": items,
        "default_payment_method": default_payment_method,
        "trial_period_days": trial_period_days,
        "coupon": coupon,
        "promotion_code": promotion_code,
        "metadata": metadata,
    }
    return stripe_request("POST", "/v1/subscriptions", params=params, stripe_account=stripe_account)


def subscriptions_retrieve(*, subscription_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/subscriptions/{subscription_id}", stripe_account=stripe_account)


def subscriptions_update(
    *,
    subscription_id: str,
    cancel_at_period_end: Optional[bool] = None,
    items: Optional[List[Dict[str, Any]]] = None,
    default_payment_method: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    proration_behavior: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "cancel_at_period_end": cancel_at_period_end,
        "items": items,
        "default_payment_method": default_payment_method,
        "metadata": metadata,
        "proration_behavior": proration_behavior,
    }
    return stripe_request("POST", f"/v1/subscriptions/{subscription_id}", params=params, stripe_account=stripe_account)


def subscriptions_cancel(*, subscription_id: str, invoice_now: Optional[bool] = None, prorate: Optional[bool] = None, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"invoice_now": invoice_now, "prorate": prorate}
    return stripe_request("DELETE", f"/v1/subscriptions/{subscription_id}", params=params, stripe_account=stripe_account)


def subscriptions_list(
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
    return stripe_request("GET", "/v1/subscriptions", params=params, stripe_account=stripe_account)
