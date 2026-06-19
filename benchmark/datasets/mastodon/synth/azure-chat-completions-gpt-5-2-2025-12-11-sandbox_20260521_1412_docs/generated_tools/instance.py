from __future__ import annotations

from typing import Any, Dict

from .http_client import request_json


def get_instance_info() -> Dict[str, Any]:
    return request_json("GET", "/api/v2/instance", require_auth=False)
