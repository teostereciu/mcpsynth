"""GitHub Actions Workflows and Workflow Runs tools."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"


def _get(path, params=None):
    try:
        r = requests.get(f"{BASE_URL}{path}", headers=HEADERS, params=params, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def _post(path, json=None):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=HEADERS, json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def _put(path, json=None):
    try:
        r = requests.put(f"{BASE_URL}{path}", headers=HEADERS, json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def _delete(path):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=HEADERS, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def register_actions_tools(mcp: FastMCP):

    # --- Workflows ---

    @mcp.tool()
    def list_repo_workflows(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
        """List all workflows in a repository."""
        return _get(f"/repos/{owner}/{repo}/actions/workflows",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def get_workflow(owner: str, repo: str, workflow_id: str) -> dict:
        """Get a specific workflow by ID or filename (e.g., 'main.yaml')."""
        return _get(f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")

    @mcp.tool()
    def disable_workflow(owner: str, repo: str, workflow_id: str) -> dict:
        """Disable a workflow."""
        return _put(f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable")

    @mcp.tool()
    def enable_workflow(owner: str, repo: str, workflow_id: str) -> dict:
        """Enable a workflow."""
        return _put(f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable")

    @mcp.tool()
    def create_workflow_dispatch(owner: str, repo: str, workflow_id: str,
                                 ref: str, inputs: dict = None) -> dict:
        """Manually trigger a workflow dispatch event."""
        payload = {"ref": ref}
        if inputs:
            payload["inputs"] = inputs
        return _post(f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches", payload)

    @mcp.tool()
    def list_workflow_runs_for_workflow(owner: str, repo: str, workflow_id: str,
                                       actor: str = None, branch: str = None,
                                       event: str = None, status: str = None,
                                       per_page: int = 30, page: int = 1) -> dict:
        """List workflow runs for a specific workflow."""
        params = {"per_page": per_page, "page": page}
        if actor:
            params["actor"] = actor
        if branch:
            params["branch"] = branch
        if event:
            params["event"] = event
        if status:
            params["status"] = status
        return _get(f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs", params)

    # --- Workflow Runs ---

    @mcp.tool()
    def list_workflow_runs(owner: str, repo: str, actor: str = None, branch: str = None,
                           event: str = None, status: str = None,
                           per_page: int = 30, page: int = 1) -> dict:
        """List all workflow runs for a repository."""
        params = {"per_page": per_page, "page": page}
        if actor:
            params["actor"] = actor
        if branch:
            params["branch"] = branch
        if event:
            params["event"] = event
        if status:
            params["status"] = status
        return _get(f"/repos/{owner}/{repo}/actions/runs", params)

    @mcp.tool()
    def get_workflow_run(owner: str, repo: str, run_id: int) -> dict:
        """Get a specific workflow run by ID."""
        return _get(f"/repos/{owner}/{repo}/actions/runs/{run_id}")

    @mcp.tool()
    def cancel_workflow_run(owner: str, repo: str, run_id: int) -> dict:
        """Cancel a workflow run."""
        return _post(f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")

    @mcp.tool()
    def rerun_workflow(owner: str, repo: str, run_id: int,
                       enable_debug_logging: bool = False) -> dict:
        """Re-run a workflow run."""
        return _post(f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun",
                     {"enable_debug_logging": enable_debug_logging})

    @mcp.tool()
    def delete_workflow_run(owner: str, repo: str, run_id: int) -> dict:
        """Delete a workflow run."""
        return _delete(f"/repos/{owner}/{repo}/actions/runs/{run_id}")

    @mcp.tool()
    def list_workflow_run_jobs(owner: str, repo: str, run_id: int,
                               filter: str = "latest", per_page: int = 30, page: int = 1) -> dict:
        """List jobs for a workflow run."""
        return _get(f"/repos/{owner}/{repo}/actions/runs/{run_id}/jobs",
                    {"filter": filter, "per_page": per_page, "page": page})

    @mcp.tool()
    def get_workflow_run_logs_url(owner: str, repo: str, run_id: int) -> dict:
        """Get the URL to download workflow run logs."""
        try:
            r = requests.get(f"{BASE_URL}/repos/{owner}/{repo}/actions/runs/{run_id}/logs",
                             headers=HEADERS, allow_redirects=False, timeout=30)
            if r.status_code in (302, 301):
                return {"logs_url": r.headers.get("Location")}
            return {"status_code": r.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def list_workflow_run_artifacts(owner: str, repo: str, run_id: int,
                                    per_page: int = 30, page: int = 1) -> dict:
        """List artifacts for a workflow run."""
        return _get(f"/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def rerun_failed_jobs(owner: str, repo: str, run_id: int,
                          enable_debug_logging: bool = False) -> dict:
        """Re-run only failed jobs in a workflow run."""
        return _post(f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun-failed-jobs",
                     {"enable_debug_logging": enable_debug_logging})

    # --- Secrets ---

    @mcp.tool()
    def list_repo_secrets(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
        """List secrets for a repository (names only, not values)."""
        return _get(f"/repos/{owner}/{repo}/actions/secrets",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def get_repo_secret(owner: str, repo: str, secret_name: str) -> dict:
        """Get a repository secret by name (metadata only, not value)."""
        return _get(f"/repos/{owner}/{repo}/actions/secrets/{secret_name}")

    @mcp.tool()
    def delete_repo_secret(owner: str, repo: str, secret_name: str) -> dict:
        """Delete a repository secret."""
        return _delete(f"/repos/{owner}/{repo}/actions/secrets/{secret_name}")

    # --- Variables ---

    @mcp.tool()
    def list_repo_variables(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
        """List Actions variables for a repository."""
        return _get(f"/repos/{owner}/{repo}/actions/variables",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def get_repo_variable(owner: str, repo: str, name: str) -> dict:
        """Get a repository Actions variable by name."""
        return _get(f"/repos/{owner}/{repo}/actions/variables/{name}")

    @mcp.tool()
    def create_repo_variable(owner: str, repo: str, name: str, value: str) -> dict:
        """Create a repository Actions variable."""
        return _post(f"/repos/{owner}/{repo}/actions/variables", {"name": name, "value": value})

    @mcp.tool()
    def delete_repo_variable(owner: str, repo: str, name: str) -> dict:
        """Delete a repository Actions variable."""
        return _delete(f"/repos/{owner}/{repo}/actions/variables/{name}")
