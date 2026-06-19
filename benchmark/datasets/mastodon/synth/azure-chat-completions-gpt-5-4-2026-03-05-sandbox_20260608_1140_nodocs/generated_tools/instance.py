from typing import Any

from generated_tools.common import mastodon_request


def get_instance_info() -> Any:
    return mastodon_request("GET", "/api/v2/instance")


def get_instance_activity() -> Any:
    return mastodon_request("GET", "/api/v1/instance/activity")
