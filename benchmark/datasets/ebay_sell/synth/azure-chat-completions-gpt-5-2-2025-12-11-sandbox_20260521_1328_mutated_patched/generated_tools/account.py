from typing import Any, Dict, Optional

from .client import EbayClient


def get_payment_policies(
    market_id: str,
    *,
    content_language: Optional[str] = None,
    client: Optional[EbayClient] = None,
) -> Dict[str, Any]:
    """GET /payment_policy

    Retrieve all payment policies for a marketplace.
    """
    c = client or EbayClient()
    params = {"marketplace_id": market_id}
    return c.request(
        "GET",
        "/sell/account/v1/payment_policy",
        params=params,
        content_language=content_language,
    )


def create_payment_policy(
    payment_policy: Dict[str, Any],
    *,
    client: Optional[EbayClient] = None,
) -> Dict[str, Any]:
    """POST /payment_policy

    Create a new payment policy.
    """
    c = client or EbayClient()
    return c.request(
        "POST",
        "/sell/account/v1/payment_policy",
        json=payment_policy,
    )


def get_fulfillment_policies(
    market_id: str,
    *,
    content_language: Optional[str] = None,
    client: Optional[EbayClient] = None,
) -> Dict[str, Any]:
    """GET /fulfillment_policy

    Retrieve all fulfillment policies for a marketplace.
    """
    c = client or EbayClient()
    params = {"marketplace_id": market_id}
    return c.request(
        "GET",
        "/sell/account/v1/fulfillment_policy",
        params=params,
        content_language=content_language,
    )
