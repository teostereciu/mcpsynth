"""Shared HTTP client for Notion API requests."""
import os
import requests

NOTION_API_KEY = os.environ.get("NOTION_API_KEY", "")
BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2026-03-11"


def _headers() -> dict:
    return {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def notion_request(
    method: str,
    path: str,
    params: dict | None = None,
    json: dict | list | None = None,
) -> dict:
    """Make an authenticated request to the Notion API.

    This is an internal helper — not exposed as an MCP tool.

    Args:
        method: HTTP method (GET, POST, PATCH, DELETE).
        path: API path starting with / (e.g. /pages/123).
        params: Query parameters.
        json: Request body as a dict or list.

    Returns:
        Parsed JSON response as a dict, or an error dict.
    """
    url = f"{BASE_URL}{path}"
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=_headers(),
            params=params,
            json=json,
            timeout=30,
        )
        try:
            data = response.json()
        except Exception:
            data = {"error": response.text, "status_code": response.status_code}
            return data

        if not response.ok:
            # Return the Notion error object as-is (it has "object": "error", "code", "message")
            return data

        return data
    except requests.exceptions.Timeout:
        return {"error": "Request timed out", "status_code": 408}
    except requests.exceptions.ConnectionError as e:
        return {"error": f"Connection error: {str(e)}", "status_code": 503}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}", "status_code": 500}
