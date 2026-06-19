from typing import Any

from .client import MastodonClient


def get_instance_info(client: MastodonClient) -> Any:
    return client.request("GET", "/api/v2/instance")
