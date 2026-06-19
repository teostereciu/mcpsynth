from typing import Any, Dict

from .ebay_common import client


def get_user() -> Dict[str, Any]:
    return client.request(
        "GET",
        "/commerce/identity/v1/user/",
        token_type="user",
    )
