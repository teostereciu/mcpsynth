from typing import Any, Dict, Optional

from .client import EbaySellClient


def get_payment_policies(marketplace_id: str, *, content_language: Optional[str] = None) -> Dict[str, Any]:
    """GET /payment_policy"""
    client = EbaySellClient()
    headers: Dict[str, str] = {}
    if content_language:
        headers["Content-Language"] = content_language
    return client.request(
        "GET",
        "/sell/account/v1/payment_policy",
        params={"marketplace_id": marketplace_id},
        headers=headers or None,
    )


def create_payment_policy(payment_policy: Dict[str, Any]) -> Dict[str, Any]:
    """POST /payment_policy"""
    client = EbaySellClient()
    return client.request(
        "POST",
        "/sell/account/v1/payment_policy",
        json=payment_policy,
        headers={"Content-Type": "application/json"},
    )
