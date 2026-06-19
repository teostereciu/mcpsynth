import os
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://api.spoonacular.com"


def _params(params: Dict[str, Any]) -> Dict[str, Any]:
    out = {k: v for k, v in params.items() if v is not None}
    api_key = os.getenv("SPOONACULAR_API_KEY")
    if api_key:
        out["apiKey"] = api_key
    return out


def request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    try:
        resp = requests.request(method, f"{BASE_URL}{path}", params=_params(params or {}), data=data, timeout=30)
        resp.raise_for_status()
        if resp.headers.get("content-type", "").startswith("application/json"):
            return resp.json()
        return {"text": resp.text}
    except Exception as e:
        return {"error": str(e)}
