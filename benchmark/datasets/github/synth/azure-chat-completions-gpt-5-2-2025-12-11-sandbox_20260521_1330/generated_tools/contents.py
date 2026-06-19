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
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/contents/{path}"""
    return client.request(
        "GET",
        f"/repos/{owner}/{repo}/contents/{path}",
        params={"ref": ref},
        accept=accept,
    )


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
) -> Dict[str, Any]:
    """PUT /repos/{owner}/{repo}/contents/{path}"""
    payload: Dict[str, Any] = {"message": message, "content": content_base64}
    for k, v in {"sha": sha, "branch": branch, "committer": committer, "author": author}.items():
        if v is not None:
            payload[k] = v
    return client.request("PUT", f"/repos/{owner}/{repo}/contents/{path}", json=payload)


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
) -> Dict[str, Any]:
    """DELETE /repos/{owner}/{repo}/contents/{path}"""
    payload: Dict[str, Any] = {"message": message, "sha": sha}
    for k, v in {"branch": branch, "committer": committer, "author": author}.items():
        if v is not None:
            payload[k] = v
    return client.request("DELETE", f"/repos/{owner}/{repo}/contents/{path}", json=payload)
