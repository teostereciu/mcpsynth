from typing import Any, Dict

from .ebay_auth import request_json


# Identity API (user token)


def get_user() -> Dict[str, Any]:
    """GET /commerce/identity/v1/user/"""
    status, body = request_json(
        "GET",
        "/commerce/identity/v1/user/",
        user=True,
    )
    return {"status": status, "data": body}
