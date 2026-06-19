"""Shared authentication and HTTP helpers for Google Workspace APIs."""

import os
import requests
from typing import Any, Optional


GMAIL_BASE = "https://gmail.googleapis.com/gmail/v1/users"
CALENDAR_BASE = "https://www.googleapis.com/calendar/v3"
DRIVE_BASE = "https://www.googleapis.com/drive/v3"
DOCS_BASE = "https://docs.googleapis.com/v1/documents"
SLIDES_BASE = "https://slides.googleapis.com/v1/presentations"
SHEETS_BASE = "https://sheets.googleapis.com/v4/spreadsheets"

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/presentations",
    "https://www.googleapis.com/auth/spreadsheets",
]


def get_access_token() -> str:
    """Get OAuth2 access token from environment variables.

    Checks GOOGLE_ACCESS_TOKEN first, then falls back to service account
    credentials from GOOGLE_WORKSPACE_CREDENTIALS or GOOGLE_SHEETS_CREDENTIALS.
    """
    token = os.environ.get("GOOGLE_ACCESS_TOKEN")
    if token:
        return token

    creds_path = os.environ.get("GOOGLE_WORKSPACE_CREDENTIALS") or os.environ.get(
        "GOOGLE_SHEETS_CREDENTIALS"
    )
    if not creds_path:
        raise RuntimeError(
            "Set GOOGLE_ACCESS_TOKEN or GOOGLE_WORKSPACE_CREDENTIALS environment variable."
        )

    from google.oauth2 import service_account
    import google.auth.transport.requests

    creds = service_account.Credentials.from_service_account_file(
        creds_path, scopes=SCOPES
    )
    request = google.auth.transport.requests.Request()
    creds.refresh(request)
    return creds.token


def _auth_headers() -> dict:
    """Return Authorization headers with Bearer token."""
    return {
        "Authorization": f"Bearer {get_access_token()}",
        "Content-Type": "application/json",
    }


def api_get(url: str, params: Optional[dict] = None) -> Any:
    """Perform an authenticated GET request and return parsed JSON."""
    response = requests.get(url, headers=_auth_headers(), params=params or {})
    response.raise_for_status()
    return response.json()


def api_post(url: str, payload: Optional[dict] = None, params: Optional[dict] = None) -> Any:
    """Perform an authenticated POST request and return parsed JSON."""
    response = requests.post(
        url,
        headers=_auth_headers(),
        json=payload or {},
        params=params or {},
    )
    response.raise_for_status()
    return response.json()


def api_put(url: str, payload: Optional[dict] = None, params: Optional[dict] = None) -> Any:
    """Perform an authenticated PUT request and return parsed JSON."""
    response = requests.put(
        url,
        headers=_auth_headers(),
        json=payload or {},
        params=params or {},
    )
    response.raise_for_status()
    return response.json()


def api_patch(url: str, payload: Optional[dict] = None, params: Optional[dict] = None) -> Any:
    """Perform an authenticated PATCH request and return parsed JSON."""
    response = requests.patch(
        url,
        headers=_auth_headers(),
        json=payload or {},
        params=params or {},
    )
    response.raise_for_status()
    return response.json()


def api_delete(url: str, params: Optional[dict] = None) -> Optional[dict]:
    """Perform an authenticated DELETE request. Returns None on 204, else JSON."""
    response = requests.delete(url, headers=_auth_headers(), params=params or {})
    response.raise_for_status()
    if response.status_code == 204 or not response.content:
        return {"status": "deleted"}
    return response.json()


def handle_http_error(e: requests.HTTPError) -> dict:
    """Convert an HTTPError into a structured error dict."""
    status = e.response.status_code if e.response is not None else 0
    try:
        detail = e.response.json() if e.response is not None else {}
        message = detail.get("error", {}).get("message", str(e))
    except Exception:
        message = str(e)
    return {"error": message, "status": status}
