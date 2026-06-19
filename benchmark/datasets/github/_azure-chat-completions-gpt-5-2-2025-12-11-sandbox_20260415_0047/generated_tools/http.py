from __future__ import annotations

import base64
import json
import os
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple, Union

import requests


Json = Union[dict, list, str, int, float, bool, None]


@dataclass
class GitHubClient:
    """Small GitHub REST client with consistent error handling."""

    token: str
    base_url: str = "https://api.github.com"
    api_version: str = "2022-11-28"

    @classmethod
    def from_env(cls) -> "GitHubClient":
        token = os.environ.get("GITHUB_TOKEN")
        if not token:
            raise RuntimeError("GITHUB_TOKEN is required")
        base_url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")
        return cls(token=token, base_url=base_url)

    def headers(self, accept: str = "application/vnd.github+json") -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": accept,
            "X-GitHub-Api-Version": self.api_version,
        }

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        data: Any = None,
        headers: Optional[Dict[str, str]] = None,
        stream: bool = False,
    ) -> Tuple[int, Union[Json, bytes]]:
        url = f"{self.base_url}{path}"
        h = self.headers()
        if headers:
            h.update(headers)
        resp = requests.request(
            method,
            url,
            headers=h,
            params=params,
            json=json_body,
            data=data,
            stream=stream,
        )
        if stream:
            return resp.status_code, resp.content
        ctype = resp.headers.get("content-type", "")
        if "application/json" in ctype:
            try:
                return resp.status_code, resp.json()
            except Exception:
                return resp.status_code, {"error": "Invalid JSON response", "status": resp.status_code}
        if resp.status_code == 204:
            return resp.status_code, {"ok": True}
        return resp.status_code, resp.text

    def ok_or_error(self, status: int, payload: Union[Json, bytes]) -> Json:
        if 200 <= status < 300:
            if isinstance(payload, (bytes, bytearray)):
                return {"data_base64": base64.b64encode(payload).decode("ascii")}
            return payload
        # Normalize errors
        if isinstance(payload, (bytes, bytearray)):
            return {"error": "HTTP error", "status": status, "data_base64": base64.b64encode(payload).decode("ascii")}
        if isinstance(payload, dict):
            msg = payload.get("message") or payload.get("error") or "HTTP error"
            return {"error": msg, "status": status, "details": payload}
        return {"error": str(payload), "status": status}


def split_repo(full_name: str) -> Tuple[str, str]:
    if "/" not in full_name:
        raise ValueError("repo must be in 'owner/repo' format")
    owner, repo = full_name.split("/", 1)
    return owner, repo
