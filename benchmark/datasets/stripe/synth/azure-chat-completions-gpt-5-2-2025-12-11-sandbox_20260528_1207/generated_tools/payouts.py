from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_payout(
    *,
    amount: int,
    currency: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    statement_descriptor: Optional[str] = None,
    destination: Optional[str] = None,
    method: Optional[str] = None,
    payout_method: Optional[str] = None,
    source_type: Optional[str] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"amount": amount, "currency": currency}
    if description is not None:
        params["description"] = description
    if metadata is not None:
        params["metadata"] = metadata
    if statement_descriptor is not None:
        params["statement_descriptor"] = statement_descriptor
    if destination is not None:
        params["destination"] = destination
    if method is not None:
        params["method"] = method
    if payout_method is not None:
        params["payout_method"] = payout_method
    if source_type is not None:
        params["source_type"] = source_type
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        "/v1/payouts",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def update_payout(
    payout_id: str,
    *,
    metadata: Dict[str, str],
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}",
        params={"metadata": metadata},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payout(payout_id: str, *, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payouts/{payout_id}", stripe_account=stripe_account)


def cancel_payout(
    payout_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/cancel",
        params={},
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def reverse_payout(
    payout_id: str,
    *,
    amount: Optional[int] = None,
    metadata: Optional[Dict[str, str]] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if amount is not None:
        params["amount"] = amount
    if metadata is not None:
        params["metadata"] = metadata
    if extra_params:
        params.update(extra_params)

    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/reverse",
        params=params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def list_payouts(
    *,
    status: Optional[str] = None,
    destination: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    extra_params: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if status is not None:
        params["status"] = status
    if destination is not None:
        params["destination"] = destination
    if starting_after is not None:
        params["starting_after"] = starting_after
    if ending_before is not None:
        params["ending_before"] = ending_before
    if extra_params:
        params.update(extra_params)

    return stripe_request("GET", "/v1/payouts", params=params, stripe_account=stripe_account)
