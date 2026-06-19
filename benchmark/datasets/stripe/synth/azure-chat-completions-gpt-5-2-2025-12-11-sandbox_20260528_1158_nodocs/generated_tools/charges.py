from typing import Any, Dict, Optional

from .stripe_client import stripe_request


def charges_retrieve(*, charge_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", f"/v1/charges/{charge_id}", stripe_account=stripe_account)


def charges_list(
    *,
    customer: Optional[str] = None,
    payment_intent: Optional[str] = None,
    limit: int = 10,
    starting_after: Optional[str] = None,
    ending_before: Optional[str] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "customer": customer,
        "payment_intent": payment_intent,
        "limit": limit,
        "starting_after": starting_after,
        "ending_before": ending_before,
    }
    return stripe_request("GET", "/v1/charges", params=params, stripe_account=stripe_account)


def charges_update(
    *,
    charge_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"description": description, "metadata": metadata}
    return stripe_request("POST", f"/v1/charges/{charge_id}", params=params, stripe_account=stripe_account)
