import os
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://api.spoonacular.com"
API_KEY_ENV = "SPOONACULAR_API_KEY"


def _clean_params(params: Dict[str, Any]) -> Dict[str, Any]:
    cleaned: Dict[str, Any] = {}
    for key, value in params.items():
        if value is None:
            continue
        if isinstance(value, list):
            cleaned[key] = ",".join(str(v) for v in value)
        elif isinstance(value, bool):
            cleaned[key] = str(value).lower()
        else:
            cleaned[key] = value
    return cleaned


def spoonacular_request(method: str, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
    api_key = os.getenv(API_KEY_ENV)
    if not api_key:
        return {"error": f"Missing environment variable: {API_KEY_ENV}"}

    query = _clean_params(params or {})
    query["apiKey"] = api_key

    try:
        response = requests.request(method=method, url=f"{BASE_URL}{path}", params=query, timeout=30)
        response.raise_for_status()
        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type:
            return response.json()
        return {"content": response.text}
    except requests.HTTPError:
        try:
            detail = response.json()
        except Exception:
            detail = response.text
        return {
            "error": f"HTTP {response.status_code}",
            "details": detail,
        }
    except requests.RequestException as exc:
        return {"error": str(exc)}
