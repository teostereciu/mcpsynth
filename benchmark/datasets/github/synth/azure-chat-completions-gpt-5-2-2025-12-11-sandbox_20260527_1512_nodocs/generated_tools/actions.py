from typing import Any, Dict, Optional

from ._client import GitHubClient, split_repo


def list_workflows(repo: str, per_page: int = 30, page: int = 1) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/actions/workflows", params={"per_page": per_page, "page": page})


def get_workflow(repo: str, workflow_id: str) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/actions/workflows/{workflow_id}")


def list_workflow_runs(repo: str, workflow_id: Optional[str] = None, branch: Optional[str] = None, event: Optional[str] = None, status: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if branch is not None:
        params["branch"] = branch
    if event is not None:
        params["event"] = event
    if status is not None:
        params["status"] = status
    if workflow_id:
        return client.request("GET", f"/repos/{owner}/{name}/actions/workflows/{workflow_id}/runs", params=params)
    return client.request("GET", f"/repos/{owner}/{name}/actions/runs", params=params)


def get_workflow_run(repo: str, run_id: int) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/actions/runs/{run_id}")


def rerun_workflow_run(repo: str, run_id: int) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("POST", f"/repos/{owner}/{name}/actions/runs/{run_id}/rerun", expected=(201, 202, 204))


def cancel_workflow_run(repo: str, run_id: int) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("POST", f"/repos/{owner}/{name}/actions/runs/{run_id}/cancel", expected=(202, 204))


def dispatch_workflow(repo: str, workflow_id: str, ref: str, inputs: Optional[Dict[str, Any]] = None) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {"ref": ref}
    if inputs is not None:
        payload["inputs"] = inputs
    return client.request("POST", f"/repos/{owner}/{name}/actions/workflows/{workflow_id}/dispatches", json=payload, expected=(204,))
