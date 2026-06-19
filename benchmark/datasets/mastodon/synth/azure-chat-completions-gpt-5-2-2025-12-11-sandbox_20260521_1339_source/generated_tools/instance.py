from typing import Any

from .client import MastodonClient


def instance_v1(client: MastodonClient) -> Any:
    return client.request("GET", "/api/v1/instance")


def instance_v2(client: MastodonClient) -> Any:
    return client.request("GET", "/api/v2/instance")
