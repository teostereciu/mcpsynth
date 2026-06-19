"""Shared HTTP client for GitHub REST API."""
import os
import requests

GITHUB_API_BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

def _headers(extra: dict | None = None) -> dict:
    h = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if GITHUB_TOKEN:
        h["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    if extra:
        h.update(extra)
    return h

def gh_get(path: str, params: dict | None = None) -> dict | list:
    url = f"{GITHUB_API_BASE_URL}{path}"
    r = requests.get(url, headers=_headers(), params=params, timeout=30)
    return _parse(r)

def gh_post(path: str, json: dict | None = None) -> dict | list:
    url = f"{GITHUB_API_BASE_URL}{path}"
    r = requests.post(url, headers=_headers(), json=json, timeout=30)
    return _parse(r)

def gh_patch(path: str, json: dict | None = None) -> dict | list:
    url = f"{GITHUB_API_BASE_URL}{path}"
    r = requests.patch(url, headers=_headers(), json=json, timeout=30)
    return _parse(r)

def gh_put(path: str, json: dict | None = None) -> dict | list:
    url = f"{GITHUB_API_BASE_URL}{path}"
    r = requests.put(url, headers=_headers(), json=json, timeout=30)
    return _parse(r)

def gh_delete(path: str, json: dict | None = None) -> dict | list:
    url = f"{GITHUB_API_BASE_URL}{path}"
    r = requests.delete(url, headers=_headers(), json=json, timeout=30)
    return _parse(r)

def _parse(r: requests.Response) -> dict | list:
    if r.status_code == 204:
        return {"status": "success", "http_status": 204}
    try:
        data = r.json()
    except Exception:
        data = {"raw": r.text}
    if not r.ok:
        return {"error": data if isinstance(data, str) else data, "http_status": r.status_code}
    return data
