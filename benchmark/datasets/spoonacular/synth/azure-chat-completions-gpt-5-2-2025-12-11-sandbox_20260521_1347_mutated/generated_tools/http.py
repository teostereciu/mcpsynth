import os
import requests
from typing import Any, Dict, Optional

BASE_URL = "https://api.spoonacular.com"


def _coerce_bool(v: Any) -> Any:
    if isinstance(v, bool) or v is None:
        return v
    if isinstance(v, str):
        if v.lower() in {"true", "1", "yes", "y"}:
            return True
        if v.lower() in {"false", "0", "no", "n"}:
            return False
    return v


def _clean_params(params: Dict[str, Any]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    for k, v in params.items():
        if v is None:
            continue
        v = _coerce_bool(v)
        out[k] = v
    return out


def request_json(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
    api_key = os.getenv("SPOONACULAR_API_KEY")
    if not api_key:
        return {"error": "Missing SPOONACULAR_API_KEY environment variable"}

    url = f"{BASE_URL}{path}"
    q = _clean_params(params or {})
    q["apiKey"] = api_key

    try:
        resp = requests.request(method.upper(), url, params=q, json=json, timeout=60)
    except Exception as e:
        return {"error": f"Request failed: {e}"}

    content_type = resp.headers.get("Content-Type", "")
    if resp.status_code >= 400:
        try:
            err = resp.json() if "application/json" in content_type else resp.text
        except Exception:
            err = resp.text
        return {"error": f"HTTP {resp.status_code}", "details": err}

    if "application/json" in content_type:
        try:
            return resp.json()
        except Exception as e:
            return {"error": f"Failed to parse JSON: {e}", "raw": resp.text}

    return resp.text
