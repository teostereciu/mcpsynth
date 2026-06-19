from typing import Any, Optional

from generated_tools.github_common import clean_params, github_request


def list_releases(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}/releases", params=clean_params(per_page=per_page, page=page))


def get_release(owner: str, repo: str, release_id: int) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}/releases/{release_id}")


def get_latest_release(owner: str, repo: str) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}/releases/latest")


def create_release(owner: str, repo: str, tag_name: str, target_commitish: Optional[str] = None, name: Optional[str] = None, body: Optional[str] = None, draft: Optional[bool] = None, prerelease: Optional[bool] = None, generate_release_notes: Optional[bool] = None) -> Any:
    payload = clean_params(tag_name=tag_name, target_commitish=target_commitish, name=name, body=body, draft=draft, prerelease=prerelease, generate_release_notes=generate_release_notes)
    return github_request("POST", f"/repos/{owner}/{repo}/releases", json_body=payload)


def update_release(owner: str, repo: str, release_id: int, tag_name: Optional[str] = None, target_commitish: Optional[str] = None, name: Optional[str] = None, body: Optional[str] = None, draft: Optional[bool] = None, prerelease: Optional[bool] = None, make_latest: Optional[str] = None) -> Any:
    payload = clean_params(tag_name=tag_name, target_commitish=target_commitish, name=name, body=body, draft=draft, prerelease=prerelease, make_latest=make_latest)
    return github_request("PATCH", f"/repos/{owner}/{repo}/releases/{release_id}", json_body=payload)


def delete_release(owner: str, repo: str, release_id: int) -> Any:
    return github_request("DELETE", f"/repos/{owner}/{repo}/releases/{release_id}")
