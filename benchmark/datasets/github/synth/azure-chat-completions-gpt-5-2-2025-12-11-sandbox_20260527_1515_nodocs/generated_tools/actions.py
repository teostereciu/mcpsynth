from typing import Any, Dict, Optional

from .github_client import GitHubClient


client = GitHubClient()


def list_workflows(owner: str, repo: str, *, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    return client.request("GET", f"/repos/{owner}/{repo}/actions/workflows", params={"per_page": per_page, "page": page})


def get_workflow(owner: str, repo: str, workflow_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")


def list_workflow_runs(owner: str, repo: str, *, workflow_id: Optional[str] = None, branch: Optional[str] = None, status: Optional[str] = None, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if branch is not None:
        params["branch"] = branch
    if status is not None:
        params["status"] = status
    if workflow_id is None:
        return client.request("GET", f"/repos/{owner}/{repo}/actions/runs", params=params)
    return client.request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs", params=params)


def get_workflow_run(owner: str, repo: str, run_id: int) -> Dict[str, Any]:
    return client.request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")


def rerun_workflow_run(owner: str, repo: str, run_id: int) -> Dict[str, Any]:
    return client.request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun")


def cancel_workflow_run(owner: str, repo: str, run_id: int) -> Dict[str, Any]:
    return client.request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")


def dispatch_workflow(owner: str, repo: str, workflow_id: str, ref: str, *, inputs: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"ref": ref}
    if inputs is not None:
        payload["inputs"] = inputs
    return client.request("POST", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches", json=payload)
