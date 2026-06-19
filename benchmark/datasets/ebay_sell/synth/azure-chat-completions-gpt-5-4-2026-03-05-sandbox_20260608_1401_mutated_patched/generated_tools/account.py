from typing import Any, Dict, Optional
from urllib.parse import quote

from generated_tools.common import clean_params, client


def get_payment_policies(market_id: str, content_language: Optional[str] = None) -> Any:
    headers = {"Content-Language": content_language} if content_language else None
    return client.request(
        "GET",
        "/sell/account/v1/payment_policy",
        params=clean_params(market_id=market_id),
        headers=headers,
    )


def create_payment_policy(body: Dict[str, Any]) -> Any:
    return client.request(
        "POST",
        "/sell/account/v1/payment_policy",
        json_body=body,
        headers={"Content-Type": "application/json"},
    )
