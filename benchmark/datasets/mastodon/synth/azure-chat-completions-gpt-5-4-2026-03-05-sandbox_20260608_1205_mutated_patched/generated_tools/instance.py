from typing import Any

import requests

from .common import BASE_URL


def get_instance_info() -> Any:
    if not BASE_URL:
        return {"error": "MASTODON_BASE_URL is not set"}
    try:
        response = requests.get(f"{BASE_URL}/api/v2/instance", headers={"Accept": "application/json"}, timeout=60)
        payload = response.json()
    except Exception as exc:
        return {"error": str(exc)}
    if not response.ok:
        return {"error": f"HTTP {response.status_code}", "details": payload}
    return payload
