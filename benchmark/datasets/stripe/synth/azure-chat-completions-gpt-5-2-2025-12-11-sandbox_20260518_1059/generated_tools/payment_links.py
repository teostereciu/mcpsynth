from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_payment_link(
    line_items: list[Dict[str, Any]],
    *,
    metadata: Optional[Dict[str, str]] = None,
    active: Optional[bool] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "line_items": line_items,
        "metadata": metadata,
        "active": active,
        "allow_promotion_codes": allow_promotion_codes,
        "automatic_tax": automatic_tax,
    }
    params.update(extra_params)
    return stripe_request(
        "POST",
        "/v1/payment_links",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_payment_link(
    payment_link_id: str,
    *,
    active: Optional[bool] = None,
    line_items: Optional[list[Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra_params: Any,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "line_items": line_items,
        "metadata": metadata,
    }
    params.update(extra_params)
    return stripe_request(
        "POST",
        f"/v1/payment_links/{payment_link_id}",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_payment_link_line_items(
    payment_link_id: str,
    *,
    limit: Optional[int] = None,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request(
        "GET",
        f"/v1/payment_links/{payment_link_id}/line_items",
        params,
        stripe_account=stripe_account,
    )
