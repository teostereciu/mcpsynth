"""Shared HTTP client for Notion API requests."""
import os
import requests
from typing import Any, Optional

NOTION_API_KEY = os.environ.get("NOTION_API_KEY", "")
BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2026-03-11"


def notion_request(
    method: str,
    path: str,
    params: Optional[dict] = None,
    json: Optional[dict] = None,
) -> Any:
    """Make an authenticated request to the Notion API.

    This is an internal helper — it is NOT registered as an MCP tool.

    Args:
        method: HTTP method (GET, POST, PATCH, DELETE).
        path: API path (e.g. '/pages/abc123').
        params: Query parameters.
        json: JSON request body.

    Returns:
        Parsed JSON response as a dict, or an error dict on failure.
    """
    url = f"{BASE_URL}{path}"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json,
            timeout=30,
        )
        try:
            data = response.json()
        except Exception:
            data = {"raw": response.text}

        if not response.ok:
            return {
                "error": data.get("message", "Request failed"),
                "status": response.status_code,
                "code": data.get("code", "unknown"),
                "details": data,
            }
        return data
    except requests.exceptions.Timeout:
        return {"error": "Request timed out", "status": 408}
    except requests.exceptions.ConnectionError as e:
        return {"error": f"Connection error: {str(e)}", "status": 503}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}", "status": 500}
