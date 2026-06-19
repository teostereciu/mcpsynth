"""MCP tools for GitHub Notifications."""
from mcp.server.fastmcp import FastMCP
from .client import gh_get, gh_post, gh_patch, gh_delete, gh_put

def register(mcp: FastMCP):

    @mcp.tool()
    def list_notifications(
        all: bool = False,
        participating: bool = False,
        since: str = "",
        before: str = "",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """List notifications for the authenticated user."""
        params: dict = {"all": str(all).lower(), "participating": str(participating).lower(),
                        "per_page": per_page, "page": page}
        if since:
            params["since"] = since
        if before:
            params["before"] = before
        return gh_get("/notifications", params=params)

    @mcp.tool()
    def mark_notifications_as_read(last_read_at: str = "") -> dict | list:
        """Mark all notifications as read."""
        payload: dict = {}
        if last_read_at:
            payload["last_read_at"] = last_read_at
        return gh_put("/notifications", json=payload)

    @mcp.tool()
    def get_thread(thread_id: int) -> dict | list:
        """Get a notification thread."""
        return gh_get(f"/notifications/threads/{thread_id}")

    @mcp.tool()
    def mark_thread_as_read(thread_id: int) -> dict | list:
        """Mark a notification thread as read."""
        return gh_patch(f"/notifications/threads/{thread_id}")

    @mcp.tool()
    def get_thread_subscription(thread_id: int) -> dict | list:
        """Get the subscription for a notification thread."""
        return gh_get(f"/notifications/threads/{thread_id}/subscription")

    @mcp.tool()
    def set_thread_subscription(thread_id: int, ignored: bool = False) -> dict | list:
        """Subscribe or ignore a notification thread."""
        return gh_put(f"/notifications/threads/{thread_id}/subscription", json={"ignored": ignored})

    @mcp.tool()
    def delete_thread_subscription(thread_id: int) -> dict | list:
        """Delete a notification thread subscription."""
        return gh_delete(f"/notifications/threads/{thread_id}/subscription")

    @mcp.tool()
    def list_repo_notifications(
        owner: str,
        repo: str,
        all: bool = False,
        participating: bool = False,
        since: str = "",
        before: str = "",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """List notifications for a repository."""
        params: dict = {"all": str(all).lower(), "participating": str(participating).lower(),
                        "per_page": per_page, "page": page}
        if since:
            params["since"] = since
        if before:
            params["before"] = before
        return gh_get(f"/repos/{owner}/{repo}/notifications", params=params)

    @mcp.tool()
    def mark_repo_notifications_as_read(owner: str, repo: str, last_read_at: str = "") -> dict | list:
        """Mark all notifications in a repository as read."""
        payload: dict = {}
        if last_read_at:
            payload["last_read_at"] = last_read_at
        return gh_put(f"/repos/{owner}/{repo}/notifications", json=payload)
