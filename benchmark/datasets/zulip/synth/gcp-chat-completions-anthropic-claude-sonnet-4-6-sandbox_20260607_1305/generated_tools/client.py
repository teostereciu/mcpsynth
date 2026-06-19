"""Shared HTTP client for Zulip API requests."""
import os
from typing import Optional
import requests


def zulip_request(
    method: str,
    endpoint: str,
    params: Optional[dict] = None,
    data: Optional[dict] = None,
    files: Optional[dict] = None,
) -> dict:
    """Make an authenticated request to the Zulip API.

    This is an internal helper — not exposed as an MCP tool.

    Args:
        method: HTTP method (GET, POST, PATCH, DELETE).
        endpoint: API endpoint path (without /api/v1/ prefix).
        params: Query parameters for GET requests.
        data: Form data for POST/PATCH/DELETE requests.
        files: Files to upload (multipart/form-data).

    Returns:
        Parsed JSON response as a dict.
    """
    email = os.environ.get("ZULIP_EMAIL", "")
    api_key = os.environ.get("ZULIP_API_KEY", "")
    site = os.environ.get("ZULIP_SITE", "").rstrip("/")

    if not email or not api_key or not site:
        return {
            "error": "Missing required environment variables: ZULIP_EMAIL, ZULIP_API_KEY, ZULIP_SITE"
        }

    url = f"{site}/api/v1/{endpoint}"
    auth = (email, api_key)

    try:
        if method == "GET":
            response = requests.get(url, auth=auth, params=params, timeout=30)
        elif method == "POST":
            if files:
                response = requests.post(url, auth=auth, data=data, files=files, timeout=60)
            else:
                response = requests.post(url, auth=auth, data=data, timeout=30)
        elif method == "PATCH":
            response = requests.patch(url, auth=auth, data=data, timeout=30)
        elif method == "DELETE":
            response = requests.delete(url, auth=auth, data=data, timeout=30)
        elif method == "PUT":
            response = requests.put(url, auth=auth, data=data, timeout=30)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}

        try:
            result = response.json()
        except Exception:
            result = {"error": f"Non-JSON response: {response.text[:500]}"}

        return result

    except requests.exceptions.ConnectionError as e:
        return {"error": f"Connection error: {str(e)}"}
    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}
