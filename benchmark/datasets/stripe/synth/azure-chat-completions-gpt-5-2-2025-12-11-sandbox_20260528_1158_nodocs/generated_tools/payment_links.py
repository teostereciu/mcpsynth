from typing import Any, Dict, List, Optional

from .stripe_client import stripe_request


def payment_links_create(
    *,
    line_items: List[Dict[str, Any]],
    after_completion: Optional[Dict[str, Any]] = None,
    allow_promotion_codes: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "line_items": line_items,
        "after_completion": after_completion,
        "allow_promotion_codes": allow_promotion_codes,
        "metadata": metadata,
    }
    return stripe_request("POST", "/v1/payment_links", params=params, stripe_account=stripe_account)


def payment_links_retrieve(*, payment_link_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payment_links/{payment_link_id}", stripe_account=stripe_account)


def payment_links_update(
    *,
    payment_link_id: str,
    active: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"active": active, "metadata": metadata}
    return stripe_request("POST", f"/v1/payment_links/{payment_link_id}", params=params, stripe_account=stripe_account)


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
    return stripe_request("GET", "/v1/payment_links", params=params, stripe_account=stripe_account)
