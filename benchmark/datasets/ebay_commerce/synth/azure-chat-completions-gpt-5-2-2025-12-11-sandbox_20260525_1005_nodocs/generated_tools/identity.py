from typing import Any, Dict

from .ebay_auth import auth_header, get_base_url, request_json


# Identity API (user token)


def get_user() -> Dict[str, Any]:
    """GET /commerce/identity/v1/user/"""
    url = get_base_url() + "/commerce/identity/v1/user/"
    res, err = request_json("GET", url, headers={**auth_header(user=True)})
    return err or res  # type: ignore
