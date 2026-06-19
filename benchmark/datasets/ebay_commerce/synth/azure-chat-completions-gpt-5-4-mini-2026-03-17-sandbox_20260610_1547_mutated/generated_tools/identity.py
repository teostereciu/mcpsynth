from typing import Any, Dict
from .common import get_base_url, get_token, request_json


def get_user() -> Dict[str, Any]:
    token = get_token("refresh_token").get("access_token")
    if not token:
        return {"error": "unable to obtain user token"}
    return request_json("GET", f"{get_base_url()}/commerce/identity/v1/user/", token)
