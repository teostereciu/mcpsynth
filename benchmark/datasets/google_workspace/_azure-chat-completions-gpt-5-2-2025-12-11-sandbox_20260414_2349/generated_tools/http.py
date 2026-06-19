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


def _headers(extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    h = {"Authorization": f"Bearer {_get_access_token()}"}
    if extra:
        h.update(extra)
    return h


def request_json(method: str, url: str, *, params: Optional[dict] = None, json_body: Any = None, headers: Optional[dict] = None, timeout: int = 60) -> Any:
    try:
        resp = requests.request(
            method,
            url,
            params=params or {},
            json=json_body,
            headers=_headers(headers),
            timeout=timeout,
        )
        if resp.status_code >= 400:
            try:
                err = resp.json()
            except Exception:
                err = {"message": resp.text}
            return {"error": err, "status": resp.status_code, "url": url}
        if resp.status_code == 204:
            return {"status": 204}
        ctype = resp.headers.get("Content-Type", "")
        if "application/json" in ctype:
            return resp.json()
        # fallback
        return {"data": resp.text}
    except requests.RequestException as e:
        return {"error": str(e), "status": "request_exception", "url": url}


def request_bytes(method: str, url: str, *, params: Optional[dict] = None, headers: Optional[dict] = None, timeout: int = 60) -> Any:
    try:
        resp = requests.request(
            method,
            url,
            params=params or {},
            headers=_headers(headers),
            timeout=timeout,
        )
        if resp.status_code >= 400:
            try:
                err = resp.json()
            except Exception:
                err = {"message": resp.text}
            return {"error": err, "status": resp.status_code, "url": url}
        return {"content": resp.content.decode("latin1"), "status": resp.status_code}
    except requests.RequestException as e:
        return {"error": str(e), "status": "request_exception", "url": url}
