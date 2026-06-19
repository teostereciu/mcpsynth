"""MCP tools for GitHub Gists."""
from mcp.server.fastmcp import FastMCP
from .client import gh_get, gh_post, gh_patch, gh_delete, gh_put

def register(mcp: FastMCP):

    @mcp.tool()
    def list_gists(username: str = "", since: str = "", per_page: int = 30, page: int = 1) -> dict | list:
        """List gists. Leave username empty for authenticated user's gists."""
        params: dict = {"per_page": per_page, "page": page}
        if since:
            params["since"] = since
        if username:
            return gh_get(f"/users/{username}/gists", params=params)
        return gh_get("/gists", params=params)

    @mcp.tool()
    def list_public_gists(since: str = "", per_page: int = 30, page: int = 1) -> dict | list:
        """List all public gists."""
        params: dict = {"per_page": per_page, "page": page}
        if since:
            params["since"] = since
        return gh_get("/gists/public", params=params)

    @mcp.tool()
    def list_starred_gists(since: str = "", per_page: int = 30, page: int = 1) -> dict | list:
        """List starred gists for the authenticated user."""
        params: dict = {"per_page": per_page, "page": page}
        if since:
            params["since"] = since
        return gh_get("/gists/starred", params=params)

    @mcp.tool()
    def get_gist(gist_id: str) -> dict | list:
        """Get a gist by ID."""
        return gh_get(f"/gists/{gist_id}")

    @mcp.tool()
    def get_gist_revision(gist_id: str, sha: str) -> dict | list:
        """Get a specific revision of a gist."""
        return gh_get(f"/gists/{gist_id}/{sha}")

    @mcp.tool()
    def create_gist(
        files: dict,
        description: str = "",
        public: bool = False,
    ) -> dict | list:
        """Create a gist. files is a dict of {filename: {content: str}}."""
        payload: dict = {"files": files, "public": public}
        if description:
            payload["description"] = description
        return gh_post("/gists", json=payload)

    @mcp.tool()
    def update_gist(
        gist_id: str,
        description: str = "",
        files: dict | None = None,
    ) -> dict | list:
        """Update a gist. files is a dict of {filename: {content: str}} or {filename: null} to delete."""
        payload: dict = {}
        if description:
            payload["description"] = description
        if files is not None:
            payload["files"] = files
        return gh_patch(f"/gists/{gist_id}", json=payload)

    @mcp.tool()
    def delete_gist(gist_id: str) -> dict | list:
        """Delete a gist."""
        return gh_delete(f"/gists/{gist_id}")

    @mcp.tool()
    def fork_gist(gist_id: str) -> dict | list:
        """Fork a gist."""
        return gh_post(f"/gists/{gist_id}/forks")

    @mcp.tool()
    def list_gist_forks(gist_id: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List forks of a gist."""
        return gh_get(f"/gists/{gist_id}/forks", params={"per_page": per_page, "page": page})

    @mcp.tool()
    def star_gist(gist_id: str) -> dict | list:
        """Star a gist."""
        return gh_put(f"/gists/{gist_id}/star")

    @mcp.tool()
    def unstar_gist(gist_id: str) -> dict | list:
        """Unstar a gist."""
        return gh_delete(f"/gists/{gist_id}/star")

    @mcp.tool()
    def check_gist_starred(gist_id: str) -> dict | list:
        """Check if a gist is starred."""
        return gh_get(f"/gists/{gist_id}/star")

    @mcp.tool()
    def list_gist_comments(gist_id: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List comments on a gist."""
        return gh_get(f"/gists/{gist_id}/comments", params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_gist_comment(gist_id: str, comment_id: int) -> dict | list:
        """Get a comment on a gist."""
        return gh_get(f"/gists/{gist_id}/comments/{comment_id}")

    @mcp.tool()
    def create_gist_comment(gist_id: str, body: str) -> dict | list:
        """Create a comment on a gist."""
        return gh_post(f"/gists/{gist_id}/comments", json={"body": body})

    @mcp.tool()
    def update_gist_comment(gist_id: str, comment_id: int, body: str) -> dict | list:
        """Update a comment on a gist."""
        return gh_patch(f"/gists/{gist_id}/comments/{comment_id}", json={"body": body})

    @mcp.tool()
    def delete_gist_comment(gist_id: str, comment_id: int) -> dict | list:
        """Delete a comment on a gist."""
        return gh_delete(f"/gists/{gist_id}/comments/{comment_id}")

    @mcp.tool()
    def list_gist_commits(gist_id: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List commits for a gist."""
        return gh_get(f"/gists/{gist_id}/commits", params={"per_page": per_page, "page": page})
