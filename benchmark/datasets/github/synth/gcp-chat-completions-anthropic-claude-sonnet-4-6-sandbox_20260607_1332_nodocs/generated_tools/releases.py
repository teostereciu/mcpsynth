"""MCP tools for GitHub Releases."""
from mcp.server.fastmcp import FastMCP
from .client import gh_get, gh_post, gh_patch, gh_delete

def register(mcp: FastMCP):

    @mcp.tool()
    def list_releases(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List releases for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/releases",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_release(owner: str, repo: str, release_id: int) -> dict | list:
        """Get a release by ID."""
        return gh_get(f"/repos/{owner}/{repo}/releases/{release_id}")

    @mcp.tool()
    def get_latest_release(owner: str, repo: str) -> dict | list:
        """Get the latest release for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/releases/latest")

    @mcp.tool()
    def get_release_by_tag(owner: str, repo: str, tag: str) -> dict | list:
        """Get a release by tag name."""
        return gh_get(f"/repos/{owner}/{repo}/releases/tags/{tag}")

    @mcp.tool()
    def create_release(
        owner: str,
        repo: str,
        tag_name: str,
        name: str = "",
        body: str = "",
        target_commitish: str = "",
        draft: bool = False,
        prerelease: bool = False,
        generate_release_notes: bool = False,
    ) -> dict | list:
        """Create a release for a repository."""
        payload: dict = {"tag_name": tag_name, "draft": draft, "prerelease": prerelease,
                         "generate_release_notes": generate_release_notes}
        if name:
            payload["name"] = name
        if body:
            payload["body"] = body
        if target_commitish:
            payload["target_commitish"] = target_commitish
        return gh_post(f"/repos/{owner}/{repo}/releases", json=payload)

    @mcp.tool()
    def update_release(
        owner: str,
        repo: str,
        release_id: int,
        tag_name: str = "",
        name: str = "",
        body: str = "",
        draft: bool | None = None,
        prerelease: bool | None = None,
    ) -> dict | list:
        """Update a release."""
        payload: dict = {}
        if tag_name:
            payload["tag_name"] = tag_name
        if name:
            payload["name"] = name
        if body:
            payload["body"] = body
        if draft is not None:
            payload["draft"] = draft
        if prerelease is not None:
            payload["prerelease"] = prerelease
        return gh_patch(f"/repos/{owner}/{repo}/releases/{release_id}", json=payload)

    @mcp.tool()
    def delete_release(owner: str, repo: str, release_id: int) -> dict | list:
        """Delete a release."""
        return gh_delete(f"/repos/{owner}/{repo}/releases/{release_id}")

    @mcp.tool()
    def list_release_assets(owner: str, repo: str, release_id: int, per_page: int = 30, page: int = 1) -> dict | list:
        """List assets for a release."""
        return gh_get(f"/repos/{owner}/{repo}/releases/{release_id}/assets",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_release_asset(owner: str, repo: str, asset_id: int) -> dict | list:
        """Get a release asset by ID."""
        return gh_get(f"/repos/{owner}/{repo}/releases/assets/{asset_id}")

    @mcp.tool()
    def update_release_asset(
        owner: str, repo: str, asset_id: int, name: str = "", label: str = ""
    ) -> dict | list:
        """Update a release asset name or label."""
        payload: dict = {}
        if name:
            payload["name"] = name
        if label:
            payload["label"] = label
        return gh_patch(f"/repos/{owner}/{repo}/releases/assets/{asset_id}", json=payload)

    @mcp.tool()
    def delete_release_asset(owner: str, repo: str, asset_id: int) -> dict | list:
        """Delete a release asset."""
        return gh_delete(f"/repos/{owner}/{repo}/releases/assets/{asset_id}")

    @mcp.tool()
    def generate_release_notes(
        owner: str, repo: str, tag_name: str, target_commitish: str = "", previous_tag_name: str = ""
    ) -> dict | list:
        """Generate release notes content for a release."""
        payload: dict = {"tag_name": tag_name}
        if target_commitish:
            payload["target_commitish"] = target_commitish
        if previous_tag_name:
            payload["previous_tag_name"] = previous_tag_name
        return gh_post(f"/repos/{owner}/{repo}/releases/generate-notes", json=payload)
