from typing import Optional

from generated_tools.github_common import compact, github_request


def list_workflow_runs(owner: str, repo: str, actor: Optional[str] = None, branch: Optional[str] = None, event: Optional[str] = None, status: Optional[str] = None, per_page: int = 30, page: int = 1, created: Optional[str] = None, exclude_pull_requests: bool = False, check_suite_id: Optional[int] = None, head_sha: Optional[str] = None) -> str:
    return compact(github_request("GET", f"/repos/{owner}/{repo}/actions/runs", params={"actor": actor, "branch": branch, "event": event, "status": status, "per_page": per_page, "page": page, "created": created, "exclude_pull_requests": exclude_pull_requests, "check_suite_id": check_suite_id, "head_sha": head_sha}))


def get_workflow_run(owner: str, repo: str, run_id: int) -> str:
    return compact(github_request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}"))


def rerun_workflow(owner: str, repo: str, run_id: int, enable_debug_logging: bool = False) -> str:
    return compact(github_request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun", json_body={"enable_debug_logging": enable_debug_logging}))


def cancel_workflow_run(owner: str, repo: str, run_id: int) -> str:
    return compact(github_request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel"))
