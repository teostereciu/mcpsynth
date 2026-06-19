"""GitHub Releases tools."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_post, github_patch, github_delete


def list_releases(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List releases for a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/releases", {"per_page": per_page, "page": page})


def create_release(owner: str, repo: str, tag_name: str, name: Optional[str] = None,
                   body: Optional[str] = None, draft: bool = False, prerelease: bool = False,
                   target_commitish: Optional[str] = None,
                   generate_release_notes: bool = False) -> Any:
    """Create a release.

    Args:
        owner: Repository owner
        repo: Repository name
        tag_name: Tag name for the release
        name: Release name
        body: Release body text
        draft: Whether this is a draft release
        prerelease: Whether this is a prerelease
        target_commitish: Commitish value for the tag (branch or SHA)
        generate_release_notes: Auto-generate release notes
    """
    data = {"tag_name": tag_name, "draft": draft, "prerelease": prerelease,
            "generate_release_notes": generate_release_notes}
    if name:
        data["name"] = name
    if body:
        data["body"] = body
    if target_commitish:
        data["target_commitish"] = target_commitish
    return github_post(f"/repos/{owner}/{repo}/releases", data)


def get_release(owner: str, repo: str, release_id: int) -> Any:
    """Get a release.

    Args:
        owner: Repository owner
        repo: Repository name
        release_id: Release ID
    """
    return github_get(f"/repos/{owner}/{repo}/releases/{release_id}")


def get_latest_release(owner: str, repo: str) -> Any:
    """Get the latest release.

    Args:
        owner: Repository owner
        repo: Repository name
    """
    return github_get(f"/repos/{owner}/{repo}/releases/latest")


def get_release_by_tag(owner: str, repo: str, tag: str) -> Any:
    """Get a release by tag name.

    Args:
        owner: Repository owner
        repo: Repository name
        tag: Tag name
    """
    return github_get(f"/repos/{owner}/{repo}/releases/tags/{tag}")


def update_release(owner: str, repo: str, release_id: int, tag_name: Optional[str] = None,
                   name: Optional[str] = None, body: Optional[str] = None,
                   draft: Optional[bool] = None, prerelease: Optional[bool] = None,
                   target_commitish: Optional[str] = None) -> Any:
    """Update a release.

    Args:
        owner: Repository owner
        repo: Repository name
        release_id: Release ID
        tag_name: New tag name
        name: New release name
        body: New release body
        draft: Whether this is a draft
        prerelease: Whether this is a prerelease
        target_commitish: New target commitish
    """
    data = {}
    if tag_name:
        data["tag_name"] = tag_name
    if name is not None:
        data["name"] = name
    if body is not None:
        data["body"] = body
    if draft is not None:
        data["draft"] = draft
    if prerelease is not None:
        data["prerelease"] = prerelease
    if target_commitish:
        data["target_commitish"] = target_commitish
    return github_patch(f"/repos/{owner}/{repo}/releases/{release_id}", data)


def delete_release(owner: str, repo: str, release_id: int) -> Any:
    """Delete a release.

    Args:
        owner: Repository owner
        repo: Repository name
        release_id: Release ID
    """
    return github_delete(f"/repos/{owner}/{repo}/releases/{release_id}")


def generate_release_notes(owner: str, repo: str, tag_name: str,
                           target_commitish: Optional[str] = None,
                           previous_tag_name: Optional[str] = None,
                           configuration_file_path: Optional[str] = None) -> Any:
    """Generate release notes content for a release.

    Args:
        owner: Repository owner
        repo: Repository name
        tag_name: Tag name for the release
        target_commitish: Commitish value for the tag
        previous_tag_name: Previous tag to use as starting point
        configuration_file_path: Path to release notes config file
    """
    data = {"tag_name": tag_name}
    if target_commitish:
        data["target_commitish"] = target_commitish
    if previous_tag_name:
        data["previous_tag_name"] = previous_tag_name
    if configuration_file_path:
        data["configuration_file_path"] = configuration_file_path
    return github_post(f"/repos/{owner}/{repo}/releases/generate-notes", data)


def list_release_assets(owner: str, repo: str, release_id: int,
                        per_page: int = 30, page: int = 1) -> Any:
    """List release assets.

    Args:
        owner: Repository owner
        repo: Repository name
        release_id: Release ID
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/releases/{release_id}/assets",
                      {"per_page": per_page, "page": page})


def get_release_asset(owner: str, repo: str, asset_id: int) -> Any:
    """Get a release asset.

    Args:
        owner: Repository owner
        repo: Repository name
        asset_id: Asset ID
    """
    return github_get(f"/repos/{owner}/{repo}/releases/assets/{asset_id}")


def update_release_asset(owner: str, repo: str, asset_id: int, name: Optional[str] = None,
                         label: Optional[str] = None) -> Any:
    """Update a release asset.

    Args:
        owner: Repository owner
        repo: Repository name
        asset_id: Asset ID
        name: New asset name
        label: New asset label
    """
    data = {}
    if name:
        data["name"] = name
    if label is not None:
        data["label"] = label
    return github_patch(f"/repos/{owner}/{repo}/releases/assets/{asset_id}", data)


def delete_release_asset(owner: str, repo: str, asset_id: int) -> Any:
    """Delete a release asset.

    Args:
        owner: Repository owner
        repo: Repository name
        asset_id: Asset ID
    """
    return github_delete(f"/repos/{owner}/{repo}/releases/assets/{asset_id}")
