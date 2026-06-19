from __future__ import annotations

from typing import Any, Dict, Optional

from .github_client import GitHubClient


def get_content(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    path: str,
    ref: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    params = {"ref": ref} if ref else None
    headers = {"Accept": accept} if accept else None
    return client.request("GET", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}" , params=params, headers=headers)


def create_or_update_file(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    path: str,
    message: str,
    content_base64: str,
    sha: Optional[str] = None,
    branch: Optional[str] = None,
    committer: Optional[Dict[str, Any]] = None,
    author: Optional[Dict[str, Any]] = None,
) -> Any:
    payload: Dict[str, Any] = {
        "message": message,
        "content": content_base64,
        "sha": sha,
        "branch": branch,
        "committer": committer,
        "author": author,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    return client.request("PUT", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}" , json=payload)


def delete_file(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    path: str,
    message: str,
    sha: str,
    branch: Optional[str] = None,
    committer: Optional[Dict[str, Any]] = None,
    author: Optional[Dict[str, Any]] = None,
) -> Any:
    payload: Dict[str, Any] = {
        "message": message,
        "sha": sha,
        "branch": branch,
        "committer": committer,
        "author": author,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    return client.request("DELETE", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}" , json=payload)
