from __future__ import annotations

from typing import Any, Dict, Optional

from .client import EbayClient


def get_payment_policies(*, marketplace_id: Optional[str] = None, client: Optional[EbayClient] = None) -> Any:
    """GET /payment_policy

    Doc: docs/api_account_get-payment-policies.md
    """
    c = client or EbayClient()
    params = {}
    if marketplace_id:
        params["marketplace_id"] = marketplace_id
    status, body, headers = c.request("GET", "/payment_policy", params=params or None)
    return c.ok_or_error(status, body, headers)


def create_payment_policy(
    policy: Dict[str, Any], *, content_language: str = "en-US", client: Optional[EbayClient] = None
) -> Any:
    """POST /payment_policy

    Doc: docs/api_account_create-payment-policy.md
    """
    c = client or EbayClient()
    status, body, headers = c.request(
        "POST",
        "/payment_policy",
        json=policy,
        headers={"Content-Language": content_language},
        content_type="application/json",
    )
    return c.ok_or_error(status, body, headers)


def get_fulfillment_policies(*, marketplace_id: Optional[str] = None, client: Optional[EbayClient] = None) -> Any:
    """GET /fulfillment_policy

    Doc: docs/api_account_get-fulfillment-policies.md
    """
    c = client or EbayClient()
    params = {}
    if marketplace_id:
        params["marketplace_id"] = marketplace_id
    status, body, headers = c.request("GET", "/fulfillment_policy", params=params or None)
    return c.ok_or_error(status, body, headers)


def create_fulfillment_policy(
    policy: Dict[str, Any], *, content_language: str = "en-US", client: Optional[EbayClient] = None
) -> Any:
    """POST /fulfillment_policy/

    Doc: docs/api_account_create-fulfillment-policy.md
    """
    c = client or EbayClient()
    status, body, headers = c.request(
        "POST",
        "/fulfillment_policy/",
        json=policy,
        headers={"Content-Language": content_language},
        content_type="application/json",
    )
    return c.ok_or_error(status, body, headers)


def get_return_policies(*, marketplace_id: Optional[str] = None, client: Optional[EbayClient] = None) -> Any:
    """GET /return_policy

    Doc: docs/api_account_get-return-policies.md
    """
    c = client or EbayClient()
    params = {}
    if marketplace_id:
        params["marketplace_id"] = marketplace_id
    status, body, headers = c.request("GET", "/return_policy", params=params or None)
    return c.ok_or_error(status, body, headers)


def create_return_policy(
    policy: Dict[str, Any], *, content_language: str = "en-US", client: Optional[EbayClient] = None
) -> Any:
    """POST /return_policy

    Doc: docs/api_account_create-return-policy.md
    """
    c = client or EbayClient()
    status, body, headers = c.request(
        "POST",
        "/return_policy",
        json=policy,
        headers={"Content-Language": content_language},
        content_type="application/json",
    )
    return c.ok_or_error(status, body, headers)
