import os
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://api.spoonacular.com"
TIMEOUT = 30


def _clean_params(params: Dict[str, Any]) -> Dict[str, Any]:
    cleaned: Dict[str, Any] = {}
    for key, value in params.items():
        if value is None:
            continue
        if isinstance(value, bool):
            cleaned[key] = str(value).lower()
        else:
            cleaned[key] = value
    return cleaned


def spoonacular_request(method: str, path: str, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None) -> Any:
    api_key = os.getenv("SPOONACULAR_API_KEY")
    if not api_key:
        return {"error": "Missing SPOONACULAR_API_KEY environment variable"}

    query = _clean_params(params or {})
    query["apiKey"] = api_key

    try:
        response = requests.request(
            method=method,
            url=f"{BASE_URL}{path}",
            params=query,
            data=data,
            timeout=TIMEOUT,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        detail = None
        response = getattr(exc, "response", None)
        if response is not None:
            try:
                detail = response.json()
            except ValueError:
                detail = response.text
        return {"error": str(exc), "details": detail}

    content_type = response.headers.get("Content-Type", "")
    if "application/json" in content_type:
        try:
            return response.json()
        except ValueError:
            return {"error": "Invalid JSON response", "text": response.text}
    return {"content": response.text, "content_type": content_type}
