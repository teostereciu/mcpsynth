from typing import Any, Dict, Optional

from .http import stripe_request


def payment_links_create(
    *,
    line_items: list,
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    automatic_tax: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, str]] = None,
    customer_creation: Optional[str] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "line_items": line_items,
        "after_completion": after_completion,
        "allow_promotion_codes": allow_promotion_codes,
        "automatic_tax": automatic_tax,
        "metadata": metadata,
        "customer_creation": customer_creation,
    }
    data.update(extra)
    result, err = stripe_request(
        "POST",
        "/v1/payment_links",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def payment_links_retrieve(*, payment_link_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    result, err = stripe_request("GET", f"/v1/payment_links/{payment_link_id}", stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]


def payment_links_update(
    *,
    payment_link_id: str,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    **extra: Any,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {"active": active, "metadata": metadata}
    data.update(extra)
    result, err = stripe_request(
        "POST",
        f"/v1/payment_links/{payment_link_id}",
        data=data,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
    return err or result  # type: ignore[return-value]


def payment_links_list(
    *,
    active: Optional[bool] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "active": active,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    result, err = stripe_request("GET", "/v1/payment_links", params=params, stripe_account=stripe_account)
    return err or result  # type: ignore[return-value]
