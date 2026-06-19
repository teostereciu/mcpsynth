import os
import requests
from typing import Any, Dict, Optional, Tuple


def _base_url() -> str:
    return os.getenv("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")


def _headers(extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    token = os.getenv("GITHUB_TOKEN", "").strip()
    h = {
        "Accept": "application/vnd.github+json",
    }
    if token:
        h["Authorization"] = f"Bearer {token}"
    if extra:
        h.update({k: v for k, v in extra.items() if v is not None})
    return h


def gh_request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    extra_headers: Optional[Dict[str, str]] = None,
    timeout: float = 30.0,
) -> Any:
    url = f"{_base_url()}{path}"
    try:
        resp = requests.request(
            method,
            url,
            headers=_headers(extra_headers),
            params={k: v for k, v in (params or {}).items() if v is not None},
            json=json,
            timeout=timeout,
        )
    except requests.RequestException as e:
        return {"error": str(e), "url": url}

    if resp.status_code == 204:
        return {"ok": True, "status": 204}

    content_type = resp.headers.get("Content-Type", "")
    data: Any
    if "application/json" in content_type:
        try:
            data = resp.json()
        except ValueError:
            data = resp.text
    else:
        data = resp.text

    if resp.status_code >= 400:
        return {
            "error": "GitHub API error",
            "status": resp.status_code,
            "url": url,
            "response": data,
        }
    return data


def parse_owner_repo(owner: Optional[str], repo: Optional[str], owner_repo: Optional[str]) -> Tuple[Optional[str], Optional[str]]:
    if owner and repo:
        return owner, repo
    if owner_repo:
        if "/" in owner_repo:
            o, r = owner_repo.split("/", 1)
            return o, r
    test_repo = os.getenv("GITHUB_TEST_REPO")
    if test_repo and "/" in test_repo:
        o, r = test_repo.split("/", 1)
        return o, r
    return owner, repo
