import os
from typing import Any, Dict

import httpx

BASE_URLS = {
    "SANDBOX": "https://api.sandbox.ebay.com",
    "PRODUCTION": "https://api.ebay.com",
}


def get_base_url() -> str:
    env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
    return BASE_URLS.get(env, BASE_URLS["SANDBOX"])


def get_access_token() -> str:
    return os.getenv("EBAY_ACCESS_TOKEN", "")


def headers(extra: Dict[str, str] | None = None) -> Dict[str, str]:
    h = {"Authorization": f"Bearer {get_access_token()}"}
    if extra:
        h.update(extra)
    return h


def request(method: str, path: str, *, params: Dict[str, Any] | None = None, json: Any = None, extra_headers: Dict[str, str] | None = None) -> Any:
    url = f"{get_base_url()}{path}"
    with httpx.Client(timeout=60.0) as client:
        resp = client.request(method, url, params=params, json=json, headers=headers(extra_headers))
        resp.raise_for_status()
        if resp.headers.get("content-type", "").startswith("application/json"):
            return resp.json()
        return {"content": resp.text}
