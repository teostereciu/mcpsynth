from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def payouts_create(
    *,
    amount: int,
    currency: str,
    description: Optional[str] = None,
    method: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "description": description,
        "method": method,
        "metadata": metadata,
    }
    return stripe_request("POST", "/v1/payouts", params=params, stripe_account=stripe_account)


def payouts_retrieve(*, payout_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/payouts/{payout_id}", stripe_account=stripe_account)


def payouts_update(
    *,
    payout_id: str,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"metadata": metadata}
    return stripe_request("POST", f"/v1/payouts/{payout_id}", params=params, stripe_account=stripe_account)


def payouts_list(
    *,
    status: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "status": status,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/payouts", params=params, stripe_account=stripe_account)
