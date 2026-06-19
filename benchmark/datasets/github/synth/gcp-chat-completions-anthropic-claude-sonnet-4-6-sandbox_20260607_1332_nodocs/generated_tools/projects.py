"""MCP tools for GitHub Projects (classic) and Projects v2."""
from mcp.server.fastmcp import FastMCP
from .client import gh_get, gh_post, gh_patch, gh_delete

def register(mcp: FastMCP):

    # --- Classic Projects ---

    @mcp.tool()
    def list_repo_projects(
        owner: str, repo: str, state: str = "open", per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List projects for a repository (classic)."""
        return gh_get(f"/repos/{owner}/{repo}/projects",
                      params={"state": state, "per_page": per_page, "page": page})

    @mcp.tool()
    def list_org_projects(
        org: str, state: str = "open", per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List projects for an organization (classic)."""
        return gh_get(f"/orgs/{org}/projects",
                      params={"state": state, "per_page": per_page, "page": page})

    @mcp.tool()
    def get_project(project_id: int) -> dict | list:
        """Get a project by ID (classic)."""
        return gh_get(f"/projects/{project_id}")

    @mcp.tool()
    def create_repo_project(owner: str, repo: str, name: str, body: str = "") -> dict | list:
        """Create a project for a repository (classic)."""
        payload: dict = {"name": name}
        if body:
            payload["body"] = body
        return gh_post(f"/repos/{owner}/{repo}/projects", json=payload)

    @mcp.tool()
    def create_org_project(org: str, name: str, body: str = "") -> dict | list:
        """Create a project for an organization (classic)."""
        payload: dict = {"name": name}
        if body:
            payload["body"] = body
        return gh_post(f"/orgs/{org}/projects", json=payload)

    @mcp.tool()
    def update_project(
        project_id: int,
        name: str = "",
        body: str = "",
        state: str = "",
        organization_permission: str = "",
        private: bool | None = None,
    ) -> dict | list:
        """Update a project (classic)."""
        payload: dict = {}
        if name:
            payload["name"] = name
        if body:
            payload["body"] = body
        if state:
            payload["state"] = state
        if organization_permission:
            payload["organization_permission"] = organization_permission
        if private is not None:
            payload["private"] = private
        return gh_patch(f"/projects/{project_id}", json=payload)

    @mcp.tool()
    def delete_project(project_id: int) -> dict | list:
        """Delete a project (classic)."""
        return gh_delete(f"/projects/{project_id}")

    # --- Project Columns ---

    @mcp.tool()
    def list_project_columns(project_id: int, per_page: int = 30, page: int = 1) -> dict | list:
        """List columns for a project (classic)."""
        return gh_get(f"/projects/{project_id}/columns",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_project_column(column_id: int) -> dict | list:
        """Get a project column by ID (classic)."""
        return gh_get(f"/projects/columns/{column_id}")

    @mcp.tool()
    def create_project_column(project_id: int, name: str) -> dict | list:
        """Create a column in a project (classic)."""
        return gh_post(f"/projects/{project_id}/columns", json={"name": name})

    @mcp.tool()
    def update_project_column(column_id: int, name: str) -> dict | list:
        """Update a project column (classic)."""
        return gh_patch(f"/projects/columns/{column_id}", json={"name": name})

    @mcp.tool()
    def delete_project_column(column_id: int) -> dict | list:
        """Delete a project column (classic)."""
        return gh_delete(f"/projects/columns/{column_id}")

    # --- Project Cards ---

    @mcp.tool()
    def list_project_cards(
        column_id: int, archived_state: str = "not_archived", per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List cards in a project column (classic)."""
        return gh_get(f"/projects/columns/{column_id}/cards",
                      params={"archived_state": archived_state, "per_page": per_page, "page": page})

    @mcp.tool()
    def get_project_card(card_id: int) -> dict | list:
        """Get a project card by ID (classic)."""
        return gh_get(f"/projects/columns/cards/{card_id}")

    @mcp.tool()
    def create_project_card(
        column_id: int,
        note: str = "",
        content_id: int | None = None,
        content_type: str = "",
    ) -> dict | list:
        """Create a card in a project column (classic). Use note for text cards or content_id+content_type for issue/PR cards."""
        payload: dict = {}
        if note:
            payload["note"] = note
        if content_id is not None:
            payload["content_id"] = content_id
        if content_type:
            payload["content_type"] = content_type
        return gh_post(f"/projects/columns/{column_id}/cards", json=payload)

    @mcp.tool()
    def update_project_card(
        card_id: int, note: str = "", archived: bool | None = None
    ) -> dict | list:
        """Update a project card (classic)."""
        payload: dict = {}
        if note:
            payload["note"] = note
        if archived is not None:
            payload["archived"] = archived
        return gh_patch(f"/projects/columns/cards/{card_id}", json=payload)

    @mcp.tool()
    def delete_project_card(card_id: int) -> dict | list:
        """Delete a project card (classic)."""
        return gh_delete(f"/projects/columns/cards/{card_id}")

    @mcp.tool()
    def move_project_card(card_id: int, position: str, column_id: int | None = None) -> dict | list:
        """Move a project card. position: top|bottom|after:<card_id>."""
        payload: dict = {"position": position}
        if column_id is not None:
            payload["column_id"] = column_id
        return gh_post(f"/projects/columns/cards/{card_id}/moves", json=payload)

    @mcp.tool()
    def move_project_column(column_id: int, position: str) -> dict | list:
        """Move a project column. position: first|last|after:<column_id>."""
        return gh_post(f"/projects/columns/{column_id}/moves", json={"position": position})
