from typing import Any

from ._client import request_json


def get_instance_info() -> Any:
    return request_json("GET", "/api/v2/instance")
