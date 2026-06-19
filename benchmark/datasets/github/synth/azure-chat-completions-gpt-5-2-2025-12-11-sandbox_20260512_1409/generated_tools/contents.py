from typing import Any, Dict, Optional

from .github_client import GitHubClient


def get_content(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    path: str,
    ref: Optional[str] = None,
    media: str = "object",
) -> Any:
    params: Dict[str, Any] = {}
    if ref is not None:
        params["ref"] = ref

    accept = None
    if media == "raw":
        accept = "application/vnd.github.raw+json"
    elif media == "html":
        accept = "application/vnd.github.html+json"
    elif media == "object":
        accept = "application/vnd.github.object+json"

    return client.request("GET", f"/repos/{owner}/{repo}/contents/{path}", params=params, accept=accept)


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
    payload: Dict[str, Any] = {"message": message, "content": content_base64}
    if sha is not None:
        payload["sha"] = sha
    if branch is not None:
        payload["branch"] = branch
    if committer is not None:
        payload["committer"] = committer
    if author is not None:
        payload["author"] = author
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
) -> Any:
    payload: Dict[str, Any] = {"message": message, "sha": sha}
    if branch is not None:
        payload["branch"] = branch
    if committer is not None:
        payload["committer"] = committer
    if author is not None:
        payload["author"] = author
    return client.request("DELETE", f"/repos/{owner}/{repo}/contents/{path}", json=payload)
