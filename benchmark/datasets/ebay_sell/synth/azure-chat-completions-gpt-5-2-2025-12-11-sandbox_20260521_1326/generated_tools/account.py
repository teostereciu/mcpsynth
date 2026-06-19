from typing import Any, Dict, Optional

from .client import EbayClient


def create_payment_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    """POST /payment_policy

    Creates a payment business policy.

    Doc: docs/api_account_create-payment-policy.md
    """

    client = EbayClient()
    return client.request_json(
        "POST",
        "/sell/account/v1/payment_policy",
        json=policy,
        content_type="application/json",
    )


def update_payment_policy(payment_policy_id: str, policy: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /payment_policy/{payment_policy_id}

    Updates (replaces) a payment policy.

    Doc: docs/api_account_update-payment-policy.md
    """

    client = EbayClient()
    return client.request_json(
        "PUT",
        f"/sell/account/v1/payment_policy/{payment_policy_id}",
        json=policy,
        content_type="application/json",
    )


def delete_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
    """DELETE /payment_policy/{payment_policy_id}

    Deletes a payment policy.

    Doc: docs/api_account_delete-payment-policy.md
    """

    client = EbayClient()
    return client.request_json("DELETE", f"/sell/account/v1/payment_policy/{payment_policy_id}")


def get_payment_policy(payment_policy_id: str) -> Dict[str, Any]:
    """GET /payment_policy/{payment_policy_id}

    Retrieves a payment policy by id.

    Doc: docs/api_account_get-payment-policy.md
    """

    client = EbayClient()
    return client.request_json("GET", f"/sell/account/v1/payment_policy/{payment_policy_id}")


def get_payment_policies(marketplace_id: str, *, content_language: Optional[str] = None) -> Dict[str, Any]:
    """GET /payment_policy

    Retrieves payment business policies for a marketplace.

    Doc: docs/api_account_get-payment-policies.md
    """

    client = EbayClient()
    headers = {}
    if content_language:
        headers["Content-Language"] = content_language
    return client.request_json(
        "GET",
        "/sell/account/v1/payment_policy",
        params={"marketplace_id": marketplace_id},
        headers=headers or None,
    )
