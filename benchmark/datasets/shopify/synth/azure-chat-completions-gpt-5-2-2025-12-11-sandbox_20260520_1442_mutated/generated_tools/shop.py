from typing import Any, Dict, Optional

from .http_client import request_json


def get_shop(*, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /shop.json

    Doc: docs/api_shop.md
    """
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", "/shop.json", params=params)
