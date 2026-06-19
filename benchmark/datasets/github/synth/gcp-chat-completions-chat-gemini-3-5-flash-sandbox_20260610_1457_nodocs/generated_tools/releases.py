from typing import Any, Dict, List, Optional, Union
from github_client import client

def list_releases(
    owner: str,
    repo: str,
    per_page: Optional[int] = 30,
    page: Optional[int] = 1
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """
    List releases in a repository.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - per_page: The number of results per page (max 100).
    - page: Page number of the results to fetch.
    """
    params = {"per_page": per_page, "page": page}
    return client.request("GET", f"/repos/{owner}/{repo}/releases", params=params)

def get_release(owner: str, repo: str, release_id: int) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Get a release.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - release_id: The unique identifier of the release.
    """
    return client.request("GET", f"/repos/{owner}/{repo}/releases/{release_id}")

def get_latest_release(owner: str, repo: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Get the latest release.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    """
    return client.request("GET", f"/repos/{owner}/{repo}/releases/latest")

def create_release(
    owner: str,
    repo: str,
    tag_name: str,
    target_commitish: Optional[str] = None,
    name: Optional[str] = None,
    body: Optional[str] = None,
    draft: Optional[bool] = False,
    prerelease: Optional[bool] = False,
    make_latest: Optional[str] = "true"
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Create a release.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - tag_name: The name of the tag.
    - target_commitish: Specifies the commitish value that determines where the Git tag is created from.
    - name: The name of the release.
    - body: Text describing the contents of the tag.
    - draft: true to create a draft (unpublished) release, false to create a published one.
    - prerelease: true to identify the release as a prerelease. false to identify the release as a full release.
    - make_latest: Specifies whether this release should be set as the latest release. Can be true, false, or legacy.
    """
    data = {
        "tag_name": tag_name,
        "draft": draft,
        "prerelease": prerelease,
        "make_latest": make_latest
    }
    if target_commitish is not None: data["target_commitish"] = target_commitish
    if name is not None: data["name"] = name
    if body is not None: data["body"] = body

    return client.request("POST", f"/repos/{owner}/{repo}/releases", json_data=data)

def update_release(
    owner: str,
    repo: str,
    release_id: int,
    tag_name: Optional[str] = None,
    target_commitish: Optional[str] = None,
    name: Optional[str] = None,
    body: Optional[str] = None,
    draft: Optional[bool] = None,
    prerelease: Optional[bool] = None,
    make_latest: Optional[str] = None
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Update a release.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - release_id: The unique identifier of the release.
    - tag_name: The name of the tag.
    - target_commitish: Specifies the commitish value that determines where the Git tag is created from.
    - name: The name of the release.
    - body: Text describing the contents of the tag.
    - draft: true to create a draft (unpublished) release, false to create a published one.
    - prerelease: true to identify the release as a prerelease. false to identify the release as a full release.
    - make_latest: Specifies whether this release should be set as the latest release. Can be true, false, or legacy.
    """
    data = {}
    if tag_name is not None: data["tag_name"] = tag_name
    if target_commitish is not None: data["target_commitish"] = target_commitish
    if name is not None: data["name"] = name
    if body is not None: data["body"] = body
    if draft is not None: data["draft"] = draft
    if prerelease is not None: data["prerelease"] = prerelease
    if make_latest is not None: data["make_latest"] = make_latest

    return client.request("PATCH", f"/repos/{owner}/{repo}/releases/{release_id}", json_data=data)

def delete_release(owner: str, repo: str, release_id: int) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Delete a release.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - release_id: The unique identifier of the release.
    """
    return client.request("DELETE", f"/repos/{owner}/{repo}/releases/{release_id}")
