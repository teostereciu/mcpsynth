from typing import Any

from .http import request_json


# Docs: docs/api_instance.md


def get_instance() -> Any:
    """GET /api/v2/instance"""
    return request_json("GET", "/api/v2/instance")
