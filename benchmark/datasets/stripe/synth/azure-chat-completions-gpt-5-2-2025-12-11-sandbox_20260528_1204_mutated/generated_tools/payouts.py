from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_payout(
    amount: int,
    currency: str,
    *,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    statement_descriptor: Optional[str] = None,
    destination: Optional[str] = None,
    method: Optional[str] = None,
    payout_method: Optional[str] = None,
    source_type: Optional[str] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payouts

    Doc: docs/payouts.md (Create a payout)
    """
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "description": description,
        "metadata": metadata,
        "statement_descriptor": statement_descriptor,
        "destination": destination,
        "method": method,
        "payout_method": payout_method,
        "source_type": source_type,
        "expand": expand,
    }
    return stripe_request(
        "POST",
        "/v1/payouts",
        params,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )


def retrieve_payout(
    payout_id: str,
    *,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payouts/{payout_id}

    Doc: docs/payouts.md (Retrieve a payout)
    """
    params: Dict[str, Any] = {"expand": expand}
    return stripe_request(
        "GET",
        f"/v1/payouts/{payout_id}",
        params,
        stripe_account=stripe_account,
    )


def update_payout(
    payout_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payouts/{payout_id}

    Doc: docs/payouts.md (Update a payout)
    """
    params: Dict[str, Any] = {"metadata": metadata}
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}",
        params,
        stripe_account=stripe_account,
    )


def cancel_payout(
    payout_id: str,
    *,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payouts/{payout_id}/cancel

    Doc: docs/payouts.md (Cancel a payout)
    """
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/cancel",
        None,
        stripe_account=stripe_account,
    )


def reverse_payout(
    payout_id: str,
    *,
    metadata: Optional[Dict[str, str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/payouts/{payout_id}/reverse

    Doc: docs/payouts.md (Reverse a payout)
    """
    params: Dict[str, Any] = {"metadata": metadata}
    return stripe_request(
        "POST",
        f"/v1/payouts/{payout_id}/reverse",
        params,
        stripe_account=stripe_account,
    )


def list_payouts(
    *,
    status: Optional[str] = None,
    destination: Optional[str] = None,
    created: Optional[Dict[str, Any]] = None,
    ending_before: Optional[str] = None,
    starting_after: Optional[str] = None,
    limit: Optional[int] = None,
    expand: Optional[list[str]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /v1/payouts

    Doc: docs/payouts.md (List all payouts)
    """
    params: Dict[str, Any] = {
        "status": status,
        "destination": destination,
        "created": created,
        "ending_before": ending_before,
        "starting_after": starting_after,
        "limit": limit,
        "expand": expand,
    }
    return stripe_request(
        "GET",
        "/v1/payouts",
        params,
        stripe_account=stripe_account,
    )
