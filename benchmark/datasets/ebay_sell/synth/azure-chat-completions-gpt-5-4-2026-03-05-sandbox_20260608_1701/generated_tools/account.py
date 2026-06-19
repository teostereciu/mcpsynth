from typing import Any, Optional

from generated_tools.ebay_common import client


def get_payment_policies(marketplace_id: str, content_language: Optional[str] = None) -> Any:
    headers = {"Content-Language": content_language} if content_language else None
    return client.request(
        "GET",
        "/payment_policy",
        api_group="account",
        params={"marketplace_id": marketplace_id},
        headers=headers,
    )


def create_payment_policy(body: dict) -> Any:
    return client.request(
        "POST",
        "/payment_policy",
        api_group="account",
        json_body=body,
        headers={"Content-Type": "application/json"},
    )
