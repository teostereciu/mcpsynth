"""Shared HTTP/auth utilities for Google Workspace APIs."""

from __future__ import annotations

import os
from typing import Any, Dict, Optional

import requests


def _get_access_token() -> str:
    token = os.environ.get("GOOGLE_ACCESS_TOKEN")
    if token:
        return token

    creds_path = (
        os.environ.get("GOOGLE_WORKSPACE_CREDENTIALS")
        or os.environ.get("GOOGLE_SHEETS_CREDENTIALS")
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
    return str(creds.token)


def _headers(extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    h = {"Authorization": f"Bearer {_get_access_token()}"}
    if extra:
        h.update(extra)
    return h


def request_json(method: str, url: str, *, params: Optional[dict] = None, json: Any = None) -> Any:
    """Make an authenticated HTTP request and return JSON or an error dict.

    Never raises for HTTP errors; returns {"error": ..., "status": ...}.
    """

    try:
        resp = requests.request(
            method=method,
            url=url,
            headers=_headers({"Content-Type": "application/json"}),
            params=params or {},
            json=json,
            timeout=60,
        )
        if resp.status_code >= 400:
            try:
                payload = resp.json()
            except Exception:
                payload = {"message": resp.text}
            return {
                "error": payload,
                "status": resp.status_code,
                "url": url,
                "method": method,
            }
        if resp.status_code == 204:
            return {}
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e), "status": None, "url": url, "method": method}
