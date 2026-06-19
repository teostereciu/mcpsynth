from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def transfers_create(
    *,
    amount: int,
    currency: str,
    destination: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "amount": amount,
        "currency": currency,
        "destination": destination,
        "description": description,
        "metadata": metadata,
    }
    return stripe_request("POST", "/v1/transfers", params=params, stripe_account=stripe_account)


def transfers_retrieve(*, transfer_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/transfers/{transfer_id}", stripe_account=stripe_account)


def transfers_list(
    *,
    destination: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "destination": destination,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/transfers", params=params, stripe_account=stripe_account)
