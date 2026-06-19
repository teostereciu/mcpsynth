"""Shared HTTP client for Zulip API requests."""
import os
import requests
from typing import Optional, dict as DictType


def zulip_request(
    method: str,
    endpoint: str,
    params: Optional[dict] = None,
    data: Optional[dict] = None,
    files: Optional[dict] = None,
) -> dict:
    """Make an authenticated request to the Zulip API.

    Args:
        method: HTTP method (GET, POST, PATCH, DELETE).
        endpoint: API endpoint path (without /api/v1/ prefix).
        params: Query parameters for GET requests.
        data: Form data for POST/PATCH/DELETE requests.
        files: File uploads.

    Returns:
        Parsed JSON response as a dict.
    """
    email = os.environ.get("ZULIP_EMAIL", "")
    api_key = os.environ.get("ZULIP_API_KEY", "")
    site = os.environ.get("ZULIP_SITE", "").rstrip("/")

    if not email or not api_key or not site:
        return {"error": "Missing required environment variables: ZULIP_EMAIL, ZULIP_API_KEY, ZULIP_SITE"}

    url = f"{site}/api/v1/{endpoint}"
    auth = (email, api_key)

    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            auth=auth,
            params=params,
            data=data,
            files=files,
            timeout=30,
        )
        return response.json()
    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except requests.exceptions.ConnectionError as e:
        return {"error": f"Connection error: {str(e)}"}
    except Exception as e:
        return {"error": f"Request failed: {str(e)}"}
