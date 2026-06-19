"""
Shared HTTP client for Stripe API calls.
All requests are authenticated via STRIPE_API_KEY env var.
Request bodies are form-encoded (application/x-www-form-urlencoded).
"""

import os
import requests

STRIPE_BASE_URL = "https://api.stripe.com"


def _get_api_key() -> str:
    key = os.environ.get("STRIPE_API_KEY", "")
    if not key:
        raise ValueError("STRIPE_API_KEY environment variable is not set.")
    return key


def stripe_request(
    method: str,
    path: str,
    params: dict = None,
    data: dict = None,
) -> dict:
    """
    Make an authenticated request to the Stripe API.

    Args:
        method:  HTTP method (GET, POST, DELETE, …)
        path:    API path, e.g. '/v1/customers'
        params:  URL query parameters (for GET requests)
        data:    Form-encoded body parameters (for POST/DELETE requests)

    Returns:
        Parsed JSON response as a dict, or an error dict on failure.
    """
    url = STRIPE_BASE_URL + path
    headers = {
        "Authorization": f"Bearer {_get_api_key()}",
        "Stripe-Version": "2024-04-10",
    }
    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=params,
            data=data,
            timeout=30,
        )
        try:
            result = response.json()
        except Exception:
            result = {"error": response.text}

        if not response.ok:
            # Surface Stripe error details without raising
            if isinstance(result, dict) and "error" in result:
                return {"error": result["error"]}
            return {"error": result, "status_code": response.status_code}

        return result
    except requests.exceptions.RequestException as exc:
        return {"error": str(exc)}
