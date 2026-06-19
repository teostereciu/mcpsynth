"""MCP tools for GitHub Webhooks (repo and org hooks)."""
from mcp.server.fastmcp import FastMCP
from .client import gh_get, gh_post, gh_patch, gh_delete

def register(mcp: FastMCP):

    # --- Repository Webhooks ---

    @mcp.tool()
    def list_repo_webhooks(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List webhooks for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/hooks", params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_repo_webhook(owner: str, repo: str, hook_id: int) -> dict | list:
        """Get a repository webhook by ID."""
        return gh_get(f"/repos/{owner}/{repo}/hooks/{hook_id}")

    @mcp.tool()
    def create_repo_webhook(
        owner: str,
        repo: str,
        url: str,
        content_type: str = "json",
        secret: str = "",
        insecure_ssl: str = "0",
        events: list[str] | None = None,
        active: bool = True,
    ) -> dict | list:
        """Create a webhook for a repository."""
        config: dict = {"url": url, "content_type": content_type, "insecure_ssl": insecure_ssl}
        if secret:
            config["secret"] = secret
        payload: dict = {
            "name": "web",
            "active": active,
            "events": events or ["push"],
            "config": config,
        }
        return gh_post(f"/repos/{owner}/{repo}/hooks", json=payload)

    @mcp.tool()
    def update_repo_webhook(
        owner: str,
        repo: str,
        hook_id: int,
        url: str = "",
        content_type: str = "",
        secret: str = "",
        events: list[str] | None = None,
        active: bool | None = None,
        add_events: list[str] | None = None,
        remove_events: list[str] | None = None,
    ) -> dict | list:
        """Update a repository webhook."""
        payload: dict = {}
        config: dict = {}
        if url:
            config["url"] = url
        if content_type:
            config["content_type"] = content_type
        if secret:
            config["secret"] = secret
        if config:
            payload["config"] = config
        if events is not None:
            payload["events"] = events
        if active is not None:
            payload["active"] = active
        if add_events:
            payload["add_events"] = add_events
        if remove_events:
            payload["remove_events"] = remove_events
        return gh_patch(f"/repos/{owner}/{repo}/hooks/{hook_id}", json=payload)

    @mcp.tool()
    def delete_repo_webhook(owner: str, repo: str, hook_id: int) -> dict | list:
        """Delete a repository webhook."""
        return gh_delete(f"/repos/{owner}/{repo}/hooks/{hook_id}")

    @mcp.tool()
    def ping_repo_webhook(owner: str, repo: str, hook_id: int) -> dict | list:
        """Ping a repository webhook."""
        return gh_post(f"/repos/{owner}/{repo}/hooks/{hook_id}/pings")

    @mcp.tool()
    def test_push_repo_webhook(owner: str, repo: str, hook_id: int) -> dict | list:
        """Test a push webhook for a repository."""
        return gh_post(f"/repos/{owner}/{repo}/hooks/{hook_id}/tests")

    @mcp.tool()
    def redeliver_repo_webhook_delivery(owner: str, repo: str, hook_id: int, delivery_id: int) -> dict | list:
        """Redeliver a webhook delivery for a repository webhook."""
        return gh_post(f"/repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}/attempts")

    @mcp.tool()
    def list_repo_webhook_deliveries(owner: str, repo: str, hook_id: int, per_page: int = 30) -> dict | list:
        """List deliveries for a repository webhook."""
        return gh_get(f"/repos/{owner}/{repo}/hooks/{hook_id}/deliveries",
                      params={"per_page": per_page})

    # --- Organization Webhooks ---

    @mcp.tool()
    def list_org_webhooks(org: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List webhooks for an organization."""
        return gh_get(f"/orgs/{org}/hooks", params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_org_webhook(org: str, hook_id: int) -> dict | list:
        """Get an organization webhook by ID."""
        return gh_get(f"/orgs/{org}/hooks/{hook_id}")

    @mcp.tool()
    def create_org_webhook(
        org: str,
        url: str,
        content_type: str = "json",
        secret: str = "",
        insecure_ssl: str = "0",
        events: list[str] | None = None,
        active: bool = True,
    ) -> dict | list:
        """Create a webhook for an organization."""
        config: dict = {"url": url, "content_type": content_type, "insecure_ssl": insecure_ssl}
        if secret:
            config["secret"] = secret
        payload: dict = {
            "name": "web",
            "active": active,
            "events": events or ["push"],
            "config": config,
        }
        return gh_post(f"/orgs/{org}/hooks", json=payload)

    @mcp.tool()
    def update_org_webhook(
        org: str,
        hook_id: int,
        url: str = "",
        content_type: str = "",
        secret: str = "",
        events: list[str] | None = None,
        active: bool | None = None,
    ) -> dict | list:
        """Update an organization webhook."""
        payload: dict = {}
        config: dict = {}
        if url:
            config["url"] = url
        if content_type:
            config["content_type"] = content_type
        if secret:
            config["secret"] = secret
        if config:
            payload["config"] = config
        if events is not None:
            payload["events"] = events
        if active is not None:
            payload["active"] = active
        return gh_patch(f"/orgs/{org}/hooks/{hook_id}", json=payload)

    @mcp.tool()
    def delete_org_webhook(org: str, hook_id: int) -> dict | list:
        """Delete an organization webhook."""
        return gh_delete(f"/orgs/{org}/hooks/{hook_id}")

    @mcp.tool()
    def ping_org_webhook(org: str, hook_id: int) -> dict | list:
        """Ping an organization webhook."""
        return gh_post(f"/orgs/{org}/hooks/{hook_id}/pings")
