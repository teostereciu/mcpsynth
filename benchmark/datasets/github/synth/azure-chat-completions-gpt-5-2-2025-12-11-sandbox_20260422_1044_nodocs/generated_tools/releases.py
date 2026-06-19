from typing import Any, Dict, Optional

from .github_client import GitHubClient, parse_owner_repo


def list_releases(owner_repo: str, per_page: int = 100, max_pages: int = 5) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().paginate(f"/repos/{owner}/{repo}/releases", per_page=per_page, max_pages=max_pages)


def get_release(owner_repo: str, release_id: int) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/releases/{release_id}")


def get_latest_release(owner_repo: str) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/releases/latest")


def create_release(owner_repo: str, tag_name: str, name: Optional[str] = None, body: Optional[str] = None, target_commitish: Optional[str] = None, draft: bool = False, prerelease: bool = False, generate_release_notes: bool = False) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {
        "tag_name": tag_name,
        "draft": draft,
        "prerelease": prerelease,
        "generate_release_notes": generate_release_notes,
    }
    if name is not None:
        payload["name"] = name
    if body is not None:
        payload["body"] = body
    if target_commitish is not None:
        payload["target_commitish"] = target_commitish
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/releases", json=payload)


def update_release(owner_repo: str, release_id: int, tag_name: Optional[str] = None, name: Optional[str] = None, body: Optional[str] = None, draft: Optional[bool] = None, prerelease: Optional[bool] = None, target_commitish: Optional[str] = None, make_latest: Optional[str] = None) -> Dict[str, Any]:
    """make_latest: true | false | legacy"""
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {}
    if tag_name is not None:
        payload["tag_name"] = tag_name
    if name is not None:
        payload["name"] = name
    if body is not None:
        payload["body"] = body
    if draft is not None:
        payload["draft"] = draft
    if prerelease is not None:
        payload["prerelease"] = prerelease
    if target_commitish is not None:
        payload["target_commitish"] = target_commitish
    if make_latest is not None:
        payload["make_latest"] = make_latest
    return GitHubClient().request("PATCH", f"/repos/{owner}/{repo}/releases/{release_id}", json=payload)


def delete_release(owner_repo: str, release_id: int) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/releases/{release_id}")
