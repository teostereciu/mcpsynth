from typing import Any, Dict

from .common import client


def get_user() -> Dict[str, Any]:
    return client.request("GET", "/commerce/identity/v1/user/", "user")
