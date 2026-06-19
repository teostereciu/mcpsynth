"""MCP tools for GitHub Deployments and Environments."""
from mcp.server.fastmcp import FastMCP
from .client import gh_get, gh_post, gh_delete

def register(mcp: FastMCP):

    # --- Deployments ---

    @mcp.tool()
    def list_deployments(
        owner: str,
        repo: str,
        sha: str = "",
        ref: str = "",
        task: str = "",
        environment: str = "",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """List deployments for a repository."""
        params: dict = {"per_page": per_page, "page": page}
        if sha:
            params["sha"] = sha
        if ref:
            params["ref"] = ref
        if task:
            params["task"] = task
        if environment:
            params["environment"] = environment
        return gh_get(f"/repos/{owner}/{repo}/deployments", params=params)

    @mcp.tool()
    def get_deployment(owner: str, repo: str, deployment_id: int) -> dict | list:
        """Get a deployment by ID."""
        return gh_get(f"/repos/{owner}/{repo}/deployments/{deployment_id}")

    @mcp.tool()
    def create_deployment(
        owner: str,
        repo: str,
        ref: str,
        task: str = "deploy",
        auto_merge: bool = True,
        required_contexts: list[str] | None = None,
        payload: dict | None = None,
        environment: str = "production",
        description: str = "",
        transient_environment: bool = False,
        production_environment: bool = True,
    ) -> dict | list:
        """Create a deployment."""
        body: dict = {
            "ref": ref,
            "task": task,
            "auto_merge": auto_merge,
            "environment": environment,
            "transient_environment": transient_environment,
            "production_environment": production_environment,
        }
        if required_contexts is not None:
            body["required_contexts"] = required_contexts
        if payload is not None:
            body["payload"] = payload
        if description:
            body["description"] = description
        return gh_post(f"/repos/{owner}/{repo}/deployments", json=body)

    @mcp.tool()
    def delete_deployment(owner: str, repo: str, deployment_id: int) -> dict | list:
        """Delete a deployment."""
        return gh_delete(f"/repos/{owner}/{repo}/deployments/{deployment_id}")

    # --- Deployment Statuses ---

    @mcp.tool()
    def list_deployment_statuses(
        owner: str, repo: str, deployment_id: int, per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List statuses for a deployment."""
        return gh_get(f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_deployment_status(owner: str, repo: str, deployment_id: int, status_id: int) -> dict | list:
        """Get a deployment status by ID."""
        return gh_get(f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}")

    @mcp.tool()
    def create_deployment_status(
        owner: str,
        repo: str,
        deployment_id: int,
        state: str,
        target_url: str = "",
        log_url: str = "",
        description: str = "",
        environment: str = "",
        environment_url: str = "",
        auto_inactive: bool = True,
    ) -> dict | list:
        """Create a deployment status. state: error|failure|inactive|in_progress|queued|pending|success."""
        body: dict = {"state": state, "auto_inactive": auto_inactive}
        if target_url:
            body["target_url"] = target_url
        if log_url:
            body["log_url"] = log_url
        if description:
            body["description"] = description
        if environment:
            body["environment"] = environment
        if environment_url:
            body["environment_url"] = environment_url
        return gh_post(f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses", json=body)

    # --- Environments ---

    @mcp.tool()
    def list_environments(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List environments for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/environments",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_environment(owner: str, repo: str, environment_name: str) -> dict | list:
        """Get an environment by name."""
        return gh_get(f"/repos/{owner}/{repo}/environments/{environment_name}")

    @mcp.tool()
    def create_or_update_environment(
        owner: str,
        repo: str,
        environment_name: str,
        wait_timer: int | None = None,
        reviewers: list[dict] | None = None,
        deployment_branch_policy: dict | None = None,
    ) -> dict | list:
        """Create or update an environment."""
        body: dict = {}
        if wait_timer is not None:
            body["wait_timer"] = wait_timer
        if reviewers is not None:
            body["reviewers"] = reviewers
        if deployment_branch_policy is not None:
            body["deployment_branch_policy"] = deployment_branch_policy
        from .client import gh_put
        return gh_put(f"/repos/{owner}/{repo}/environments/{environment_name}", json=body)

    @mcp.tool()
    def delete_environment(owner: str, repo: str, environment_name: str) -> dict | list:
        """Delete an environment."""
        return gh_delete(f"/repos/{owner}/{repo}/environments/{environment_name}")
