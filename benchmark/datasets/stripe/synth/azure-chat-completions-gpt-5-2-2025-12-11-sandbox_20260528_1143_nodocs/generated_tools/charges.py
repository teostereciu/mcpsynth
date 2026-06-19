from typing import Any, Dict, Optional

from .http import stripe_request


def charges_retrieve(*, charge_id: str, stripe_account: Optional[str] = None) -> Dict[str, Any]:
    res, err = stripe_request("GET", f"/v1/charges/{charge_id}", stripe_account=stripe_account)
    return err or res  # type: ignore[return-value]


def charges_update(
    *,
    charge_id: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
    receipt_email: Optional[str] = None,
    shipping: Optional[Dict[str, Any]] = None,
    stripe_account: Optional[str] = None,
) -> Dict[str, Any]:
    data: Dict[str, Any] = {
        "description": description,
        "metadata": metadata,
        "receipt_email": receipt_email,
        "shipping": shipping,
    }
    res, err = stripe_request("POST", f"/v1/charges/{charge_id}", data=data, stripe_account=stripe_account)
    return err or res  # type: ignore[return-value]


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
    res, err = stripe_request("GET", "/v1/charges", params=params, stripe_account=stripe_account)
    return err or res  # type: ignore[return-value]
