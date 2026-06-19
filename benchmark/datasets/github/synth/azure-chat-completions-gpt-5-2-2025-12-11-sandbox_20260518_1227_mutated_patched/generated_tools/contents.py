import base64
from typing import Any, Dict, Optional

from .github_client import GitHubClient


def get_repo_content(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    path: str,
    ref: Optional[str] = None,
    accept: str = "application/vnd.github.object+json",
) -> Any:
    params: Dict[str, Any] = {}
    if ref is not None:
        params["ref"] = ref
    return client.request("GET", f"/repos/{owner}/{repo}/contents/{path}", params=params, accept=accept)


def create_or_update_file(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    path: str,
    message: str,
    content_base64: Optional[str] = None,
    content_text: Optional[str] = None,
    sha: Optional[str] = None,
    branch: Optional[str] = None,
    committer_name: Optional[str] = None,
    committer_email: Optional[str] = None,
    author_name: Optional[str] = None,
    author_email: Optional[str] = None,
) -> Any:
    if content_base64 is None and content_text is None:
        return {"error": "Provide either content_base64 or content_text"}

    if content_base64 is None:
        content_base64 = base64.b64encode(content_text.encode("utf-8")).decode("ascii")

    payload: Dict[str, Any] = {"message": message, "content": content_base64}
    if sha is not None:
        payload["sha"] = sha
    if branch is not None:
        payload["branch"] = branch
    if committer_name is not None or committer_email is not None:
        if not (committer_name and committer_email):
            return {"error": "committer_name and committer_email must both be provided"}
        payload["committer"] = {"name": committer_name, "email": committer_email}
    if author_name is not None or author_email is not None:
        if not (author_name and author_email):
            return {"error": "author_name and author_email must both be provided"}
        payload["author"] = {"name": author_name, "email": author_email}

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
    committer_name: Optional[str] = None,
    committer_email: Optional[str] = None,
    author_name: Optional[str] = None,
    author_email: Optional[str] = None,
) -> Any:
    payload: Dict[str, Any] = {"message": message, "sha": sha}
    if branch is not None:
        payload["branch"] = branch
    if committer_name is not None or committer_email is not None:
        if not (committer_name and committer_email):
            return {"error": "committer_name and committer_email must both be provided"}
        payload["committer"] = {"name": committer_name, "email": committer_email}
    if author_name is not None or author_email is not None:
        if not (author_name and author_email):
            return {"error": "author_name and author_email must both be provided"}
        payload["author"] = {"name": author_name, "email": author_email}

    return client.request("DELETE", f"/repos/{owner}/{repo}/contents/{path}", json=payload)
