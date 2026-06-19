from typing import Any, Dict, Optional

from .github_client import GitHubClient


def list_workflows(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """GET /repos/{owner}/{repo}/actions/workflows"""
    params = {"per_page": per_page, "page": page}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/actions/workflows", params=params)


def get_workflow(owner: str, repo: str, workflow_id: str) -> Any:
    """GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}"""
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")


def list_workflow_runs(owner: str, repo: str, workflow_id: str, branch: Optional[str] = None, event: Optional[str] = None, status: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs"""
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if branch:
        params["branch"] = branch
    if event:
        params["event"] = event
    if status:
        params["status"] = status
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs", params=params)


def get_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    """GET /repos/{owner}/{repo}/actions/runs/{run_id}"""
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")


def rerun_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    """POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun"""
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun")


def cancel_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    """POST /repos/{owner}/{repo}/actions/runs/{run_id}/cancel"""
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")


def list_repo_secrets(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """GET /repos/{owner}/{repo}/actions/secrets"""
    params = {"per_page": per_page, "page": page}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/actions/secrets", params=params)
