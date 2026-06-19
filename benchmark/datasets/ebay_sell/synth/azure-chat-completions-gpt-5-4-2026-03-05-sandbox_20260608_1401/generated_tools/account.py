from typing import Any, Optional

from .common import client

API_PATH = "/sell/account/v1"


def get_fulfillment_policies(marketplace_id: str, content_language: Optional[str] = None) -> Any:
    headers = {"Content-Language": content_language} if content_language else None
    return client.request(API_PATH, "GET", "/fulfillment_policy", params={"marketplace_id": marketplace_id}, headers=headers)


def create_fulfillment_policy(body: dict) -> Any:
    return client.request(
        API_PATH,
        "POST",
        "/fulfillment_policy/",
        json_body=body,
        headers={"Content-Type": "application/json"},
    )


def get_payment_policies(marketplace_id: str, content_language: Optional[str] = None) -> Any:
    headers = {"Content-Language": content_language} if content_language else None
    return client.request(API_PATH, "GET", "/payment_policy", params={"marketplace_id": marketplace_id}, headers=headers)


def create_payment_policy(body: dict) -> Any:
    return client.request(
        API_PATH,
        "POST",
        "/payment_policy",
        json_body=body,
        headers={"Content-Type": "application/json"},
    )
