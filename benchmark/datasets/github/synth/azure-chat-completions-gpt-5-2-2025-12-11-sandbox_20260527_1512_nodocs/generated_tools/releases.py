from typing import Any, Dict, Optional

from ._client import GitHubClient, split_repo


def list_releases(repo: str, per_page: int = 30, page: int = 1) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/releases", params={"per_page": per_page, "page": page})


def get_release(repo: str, release_id: int) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/releases/{release_id}")


def create_release(repo: str, tag_name: str, name: Optional[str] = None, body: Optional[str] = None, target_commitish: Optional[str] = None, draft: bool = False, prerelease: bool = False, generate_release_notes: Optional[bool] = None) -> Any:
    owner, rname = split_repo(repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {"tag_name": tag_name, "draft": draft, "prerelease": prerelease}
    if name is not None:
        payload["name"] = name
    if body is not None:
        payload["body"] = body
    if target_commitish is not None:
        payload["target_commitish"] = target_commitish
    if generate_release_notes is not None:
        payload["generate_release_notes"] = generate_release_notes
    return client.request("POST", f"/repos/{owner}/{rname}/releases", json=payload, expected=(201,))


def update_release(repo: str, release_id: int, tag_name: Optional[str] = None, name: Optional[str] = None, body: Optional[str] = None, target_commitish: Optional[str] = None, draft: Optional[bool] = None, prerelease: Optional[bool] = None, make_latest: Optional[str] = None) -> Any:
    owner, rname = split_repo(repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if tag_name is not None:
        payload["tag_name"] = tag_name
    if name is not None:
        payload["name"] = name
    if body is not None:
        payload["body"] = body
    if target_commitish is not None:
        payload["target_commitish"] = target_commitish
    if draft is not None:
        payload["draft"] = draft
    if prerelease is not None:
        payload["prerelease"] = prerelease
    if make_latest is not None:
        payload["make_latest"] = make_latest
    return client.request("PATCH", f"/repos/{owner}/{rname}/releases/{release_id}", json=payload)


def delete_release(repo: str, release_id: int) -> Any:
    owner, rname = split_repo(repo)
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{owner}/{rname}/releases/{release_id}", expected=(204,))
