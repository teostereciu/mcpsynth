"""MCP tools for GitHub Meta, Rate Limit, Licenses, Gitignore, Emojis, Markdown."""
from mcp.server.fastmcp import FastMCP
from .client import gh_get, gh_post

def register(mcp: FastMCP):

    @mcp.tool()
    def get_rate_limit() -> dict | list:
        """Get the current rate limit status for the authenticated user."""
        return gh_get("/rate_limit")

    @mcp.tool()
    def get_github_meta() -> dict | list:
        """Get GitHub meta information (IP ranges, features, etc.)."""
        return gh_get("/meta")

    @mcp.tool()
    def get_octocat(s: str = "") -> dict | list:
        """Get the Octocat ASCII art, optionally with a custom message."""
        params: dict = {}
        if s:
            params["s"] = s
        return gh_get("/octocat", params=params)

    @mcp.tool()
    def get_zen() -> dict | list:
        """Get a random GitHub zen aphorism."""
        return gh_get("/zen")

    # --- Licenses ---

    @mcp.tool()
    def list_licenses() -> dict | list:
        """List commonly used licenses."""
        return gh_get("/licenses")

    @mcp.tool()
    def get_license(license_key: str) -> dict | list:
        """Get a license by key (e.g. 'mit', 'apache-2.0')."""
        return gh_get(f"/licenses/{license_key}")

    @mcp.tool()
    def get_repo_license(owner: str, repo: str) -> dict | list:
        """Get the license for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/license")

    # --- Gitignore ---

    @mcp.tool()
    def list_gitignore_templates() -> dict | list:
        """List all available .gitignore templates."""
        return gh_get("/gitignore/templates")

    @mcp.tool()
    def get_gitignore_template(name: str) -> dict | list:
        """Get a .gitignore template by name (e.g. 'Python', 'Node')."""
        return gh_get(f"/gitignore/templates/{name}")

    # --- Emojis ---

    @mcp.tool()
    def list_emojis() -> dict | list:
        """List all GitHub emojis and their image URLs."""
        return gh_get("/emojis")

    # --- Markdown ---

    @mcp.tool()
    def render_markdown(text: str, mode: str = "markdown", context: str = "") -> dict | list:
        """Render a Markdown document. mode: markdown|gfm. context is repo for gfm mode."""
        payload: dict = {"text": text, "mode": mode}
        if context:
            payload["context"] = context
        return gh_post("/markdown", json=payload)

    # --- API Versions ---

    @mcp.tool()
    def list_api_versions() -> dict | list:
        """List all supported GitHub API versions."""
        return gh_get("/versions")
