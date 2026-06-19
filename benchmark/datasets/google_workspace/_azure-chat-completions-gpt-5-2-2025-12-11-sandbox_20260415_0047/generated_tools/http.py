import os
import json
from typing import Any, Dict, Optional

import requests


def _get_access_token() -> str:
    token = os.environ.get("GOOGLE_ACCESS_TOKEN")
    if token:
        return token

    creds_path = os.environ.get("GOOGLE_WORKSPACE_CREDENTIALS") or os.environ.get(
        "GOOGLE_SHEETS_CREDENTIALS"
    )
    if not creds_path:
        raise RuntimeError("Set GOOGLE_ACCESS_TOKEN or GOOGLE_WORKSPACE_CREDENTIALS")

    from google.oauth2 import service_account
    import google.auth.transport.requests

    scopes = [
        "https://www.googleapis.com/auth/gmail.modify",
        "https://www.googleapis.com/auth/calendar",
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/documents",
        "https://www.googleapis.com/auth/presentations",
        "https://www.googleapis.com/auth/spreadsheets",
    ]

    creds = service_account.Credentials.from_service_account_file(creds_path, scopes=scopes)
    req = google.auth.transport.requests.Request()
    creds.refresh(req)
    return creds.token


def request_json(
    method: str,
    url: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 60,
) -> Dict[str, Any]:
    """Make an authenticated request and return JSON or an error dict.

    Never raises for HTTP errors; returns {"error": ..., "status": ..., "details": ...}.
    """

    try:
        token = _get_access_token()
        h = {"Authorization": f"Bearer {token}"}
        if headers:
            h.update(headers)
        if json_body is not None:
            h.setdefault("Content-Type", "application/json")

        resp = requests.request(
            method.upper(),
            url,
            params=params or {},
            json=json_body,
            headers=h,
            timeout=timeout,
        )

        if resp.status_code >= 400:
            details: Any
            try:
                details = resp.json()
            except Exception:
                details = {"text": resp.text}
            return {
                "error": "http_error",
                "status": resp.status_code,
                "details": details,
                "url": url,
            }

        if resp.status_code == 204:
            return {"status": 204}

        if not resp.content:
            return {}

        try:
            return resp.json()
        except json.JSONDecodeError:
            return {"data": resp.text}

    except Exception as e:
        return {"error": "exception", "message": str(e), "url": url}
