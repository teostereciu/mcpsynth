from typing import Any

from ._client import request_json


def get_instance() -> Any:
    return request_json("GET", "/api/v2/instance")


def get_instance_activity() -> Any:
    return request_json("GET", "/api/v1/instance/activity")


def get_instance_peers() -> Any:
    return request_json("GET", "/api/v1/instance/peers")
