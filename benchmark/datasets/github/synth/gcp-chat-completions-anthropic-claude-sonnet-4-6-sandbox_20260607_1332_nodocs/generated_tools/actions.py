"""MCP tools for GitHub Actions (workflows, runs, jobs, artifacts, secrets)."""
from mcp.server.fastmcp import FastMCP
from .client import gh_get, gh_post, gh_patch, gh_delete, gh_put

def register(mcp: FastMCP):

    # --- Workflows ---

    @mcp.tool()
    def list_repo_workflows(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List workflows in a repository."""
        return gh_get(f"/repos/{owner}/{repo}/actions/workflows",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_workflow(owner: str, repo: str, workflow_id: str) -> dict | list:
        """Get a workflow by ID or filename (e.g. 'ci.yml')."""
        return gh_get(f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")

    @mcp.tool()
    def enable_workflow(owner: str, repo: str, workflow_id: str) -> dict | list:
        """Enable a workflow."""
        return gh_put(f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable")

    @mcp.tool()
    def disable_workflow(owner: str, repo: str, workflow_id: str) -> dict | list:
        """Disable a workflow."""
        return gh_put(f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable")

    @mcp.tool()
    def trigger_workflow(
        owner: str,
        repo: str,
        workflow_id: str,
        ref: str,
        inputs: dict | None = None,
    ) -> dict | list:
        """Trigger a workflow dispatch event."""
        payload: dict = {"ref": ref}
        if inputs:
            payload["inputs"] = inputs
        return gh_post(f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches", json=payload)

    @mcp.tool()
    def list_workflow_runs(
        owner: str,
        repo: str,
        workflow_id: str = "",
        actor: str = "",
        branch: str = "",
        event: str = "",
        status: str = "",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """List workflow runs. Optionally filter by workflow_id (ID or filename)."""
        params: dict = {"per_page": per_page, "page": page}
        if actor:
            params["actor"] = actor
        if branch:
            params["branch"] = branch
        if event:
            params["event"] = event
        if status:
            params["status"] = status
        if workflow_id:
            return gh_get(f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs", params=params)
        return gh_get(f"/repos/{owner}/{repo}/actions/runs", params=params)

    @mcp.tool()
    def get_workflow_run(owner: str, repo: str, run_id: int) -> dict | list:
        """Get a workflow run by ID."""
        return gh_get(f"/repos/{owner}/{repo}/actions/runs/{run_id}")

    @mcp.tool()
    def rerun_workflow(owner: str, repo: str, run_id: int) -> dict | list:
        """Re-run a workflow run."""
        return gh_post(f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun")

    @mcp.tool()
    def rerun_failed_jobs(owner: str, repo: str, run_id: int) -> dict | list:
        """Re-run only failed jobs in a workflow run."""
        return gh_post(f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun-failed-jobs")

    @mcp.tool()
    def cancel_workflow_run(owner: str, repo: str, run_id: int) -> dict | list:
        """Cancel a workflow run."""
        return gh_post(f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")

    @mcp.tool()
    def delete_workflow_run(owner: str, repo: str, run_id: int) -> dict | list:
        """Delete a workflow run."""
        return gh_delete(f"/repos/{owner}/{repo}/actions/runs/{run_id}")

    @mcp.tool()
    def get_workflow_run_logs_url(owner: str, repo: str, run_id: int) -> dict | list:
        """Get the URL to download workflow run logs."""
        return gh_get(f"/repos/{owner}/{repo}/actions/runs/{run_id}/logs")

    # --- Jobs ---

    @mcp.tool()
    def list_jobs_for_workflow_run(
        owner: str, repo: str, run_id: int, filter: str = "latest", per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List jobs for a workflow run. filter: latest|all."""
        return gh_get(f"/repos/{owner}/{repo}/actions/runs/{run_id}/jobs",
                      params={"filter": filter, "per_page": per_page, "page": page})

    @mcp.tool()
    def get_job(owner: str, repo: str, job_id: int) -> dict | list:
        """Get a job for a workflow run."""
        return gh_get(f"/repos/{owner}/{repo}/actions/jobs/{job_id}")

    @mcp.tool()
    def get_job_logs_url(owner: str, repo: str, job_id: int) -> dict | list:
        """Get the URL to download job logs."""
        return gh_get(f"/repos/{owner}/{repo}/actions/jobs/{job_id}/logs")

    # --- Artifacts ---

    @mcp.tool()
    def list_workflow_run_artifacts(
        owner: str, repo: str, run_id: int, per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List artifacts for a workflow run."""
        return gh_get(f"/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def list_repo_artifacts(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List all artifacts for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/actions/artifacts",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_artifact(owner: str, repo: str, artifact_id: int) -> dict | list:
        """Get an artifact by ID."""
        return gh_get(f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}")

    @mcp.tool()
    def delete_artifact(owner: str, repo: str, artifact_id: int) -> dict | list:
        """Delete an artifact."""
        return gh_delete(f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}")

    # --- Secrets ---

    @mcp.tool()
    def list_repo_secrets(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List secrets for a repository (names only, not values)."""
        return gh_get(f"/repos/{owner}/{repo}/actions/secrets",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_repo_secret(owner: str, repo: str, secret_name: str) -> dict | list:
        """Get a repository secret (metadata only)."""
        return gh_get(f"/repos/{owner}/{repo}/actions/secrets/{secret_name}")

    @mcp.tool()
    def delete_repo_secret(owner: str, repo: str, secret_name: str) -> dict | list:
        """Delete a repository secret."""
        return gh_delete(f"/repos/{owner}/{repo}/actions/secrets/{secret_name}")

    @mcp.tool()
    def get_repo_public_key(owner: str, repo: str) -> dict | list:
        """Get the public key for encrypting repository secrets."""
        return gh_get(f"/repos/{owner}/{repo}/actions/secrets/public-key")

    # --- Variables ---

    @mcp.tool()
    def list_repo_variables(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List Actions variables for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/actions/variables",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_repo_variable(owner: str, repo: str, variable_name: str) -> dict | list:
        """Get an Actions variable for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/actions/variables/{variable_name}")

    @mcp.tool()
    def create_repo_variable(owner: str, repo: str, name: str, value: str) -> dict | list:
        """Create an Actions variable for a repository."""
        return gh_post(f"/repos/{owner}/{repo}/actions/variables", json={"name": name, "value": value})

    @mcp.tool()
    def update_repo_variable(owner: str, repo: str, variable_name: str, name: str, value: str) -> dict | list:
        """Update an Actions variable for a repository."""
        return gh_patch(f"/repos/{owner}/{repo}/actions/variables/{variable_name}",
                        json={"name": name, "value": value})

    @mcp.tool()
    def delete_repo_variable(owner: str, repo: str, variable_name: str) -> dict | list:
        """Delete an Actions variable for a repository."""
        return gh_delete(f"/repos/{owner}/{repo}/actions/variables/{variable_name}")

    # --- Runners ---

    @mcp.tool()
    def list_repo_runners(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List self-hosted runners for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/actions/runners",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_runner(owner: str, repo: str, runner_id: int) -> dict | list:
        """Get a self-hosted runner for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/actions/runners/{runner_id}")

    @mcp.tool()
    def delete_runner(owner: str, repo: str, runner_id: int) -> dict | list:
        """Delete a self-hosted runner from a repository."""
        return gh_delete(f"/repos/{owner}/{repo}/actions/runners/{runner_id}")

    @mcp.tool()
    def list_runner_applications(owner: str, repo: str) -> dict | list:
        """List runner applications for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/actions/runners/downloads")

    # --- Workflow usage ---

    @mcp.tool()
    def get_workflow_usage(owner: str, repo: str, workflow_id: str) -> dict | list:
        """Get billable minutes used by a workflow."""
        return gh_get(f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing")

    @mcp.tool()
    def get_workflow_run_usage(owner: str, repo: str, run_id: int) -> dict | list:
        """Get billable minutes and timing for a workflow run."""
        return gh_get(f"/repos/{owner}/{repo}/actions/runs/{run_id}/timing")
