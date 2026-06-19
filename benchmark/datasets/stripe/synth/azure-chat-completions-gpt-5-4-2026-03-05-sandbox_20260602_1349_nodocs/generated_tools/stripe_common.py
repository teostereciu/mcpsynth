import os
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://api.stripe.com"


def _clean_params(params: Dict[str, Any]) -> Dict[str, Any]:
    cleaned: Dict[str, Any] = {}
    for key, value in params.items():
        if value is None:
            continue
        if isinstance(value, bool):
            cleaned[key] = "true" if value else "false"
        elif isinstance(value, (list, tuple)):
            for i, item in enumerate(value):
                cleaned[f"{key}[{i}]"] = item
        elif isinstance(value, dict):
            for sub_key, sub_value in value.items():
                if sub_value is not None:
                    cleaned[f"{key}[{sub_key}]"] = sub_value
        else:
            cleaned[key] = value
    return cleaned


def stripe_request(method: str, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
    api_key = os.getenv("STRIPE_API_KEY")
    if not api_key:
        return {"error": "Missing STRIPE_API_KEY environment variable"}

    url = f"{BASE_URL}{path}"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=headers, params=_clean_params(params or {}), timeout=60)
        elif method.upper() == "DELETE":
            response = requests.delete(url, headers=headers, data=_clean_params(params or {}), timeout=60)
        else:
            response = requests.request(
                method.upper(),
                url,
                headers=headers,
                data=_clean_params(params or {}),
                timeout=60,
            )
    except requests.RequestException as exc:
        return {"error": str(exc)}

    try:
        data = response.json()
    except ValueError:
        return {"error": f"Stripe returned non-JSON response with status {response.status_code}", "status_code": response.status_code, "text": response.text}

    if response.status_code >= 400:
        if isinstance(data, dict) and "error" in data:
            err = data["error"]
            if isinstance(err, dict):
                return {
                    "error": err.get("message", "Stripe API error"),
                    "type": err.get("type"),
                    "code": err.get("code"),
                    "param": err.get("param"),
                    "status_code": response.status_code,
                }
        return {"error": "Stripe API error", "status_code": response.status_code, "details": data}

    return data
