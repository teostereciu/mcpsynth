
def list_workflow_runs_for_repository(owner: str, repo: str, actor: str = None, branch: str = None, event: str = None, status: str = None, per_page: int = 30, page: int = 1, created: str = None, exclude_pull_requests: bool = False, check_suite_id: int = None, head_sha: str = None):
    """
    List workflow runs for a repository.
    https://docs.github.com/en/rest/actions/workflow-runs#list-workflow-runs-for-a-repository
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}/actions/runs", params={"actor": actor, "branch": branch, "event": event, "status": status, "per_page": per_page, "page": page, "created": created, "exclude_pull_requests": exclude_pull_requests, "check_suite_id": check_suite_id, "head_sha": head_sha})

def get_workflow_run(owner: str, repo: str, run_id: int, exclude_pull_requests: bool = False):
    """
    Get a workflow run.
    https://docs.github.com/en/rest/actions/workflow-runs#get-a-workflow-run
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}", params={"exclude_pull_requests": exclude_pull_requests})

def delete_workflow_run(owner: str, repo: str, run_id: int):
    """
    Delete a workflow run.
    https://docs.github.com/en/rest/actions/workflow-runs#delete-a-workflow-run
    """
    return _github_api_request("DELETE", f"/repos/{owner}/{repo}/actions/runs/{run_id}")

def cancel_workflow_run(owner: str, repo: str, run_id: int):
    """
    Cancel a workflow run.
    https://docs.github.com/en/rest/actions/workflow-runs#cancel-a-workflow-run
    """
    return _github_api_request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")

def retry_workflow_run(owner: str, repo: str, run_id: int):
    """
    Retry a workflow run.
    https://docs.github.com/en/rest/actions/workflow-runs#retry-a-workflow-run
    """
    return _github_api_request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/retry")

def list_workflow_runs(owner: str, repo: str, workflow_id: int, actor: str = None, branch: str = None, event: str = None, status: str = None, per_page: int = 30, page: int = 1, created: str = None, exclude_pull_requests: bool = False, check_suite_id: int = None, head_sha: str = None):
    """
    List workflow runs for a workflow.
    https://docs.github.com/en/rest/actions/workflow-runs#list-workflow-runs-for-a-workflow
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs", params={"actor": actor, "branch": branch, "event": event, "status": status, "per_page": per_page, "page": page, "created": created, "exclude_pull_requests": exclude_pull_requests, "check_suite_id": check_suite_id, "head_sha": head_sha})
from .utils import _github_api_request

def list_repository_workflows(owner: str, repo: str, per_page: int = 30, page: int = 1):
    """
    List repository workflows.
    https://docs.github.com/en/rest/actions/workflows#list-repository-workflows
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}/actions/workflows", params={"per_page": per_page, "page": page})

def get_workflow(owner: str, repo: str, workflow_id: int):
    """
    Get a workflow.
    https://docs.github.com/en/rest/actions/workflows#get-a-workflow
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")

def disable_workflow(owner: str, repo: str, workflow_id: int):
    """
    Disable a workflow.
    https://docs.github.com/en/rest/actions/workflows#disable-a-workflow
    """
    return _github_api_request("PUT", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable")

def enable_workflow(owner: str, repo: str, workflow_id: int):
    """
    Enable a workflow.
    https://docs.github.com/en/rest/actions/workflows#enable-a-workflow
    """
    return _github_api_request("PUT", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable")

def create_workflow_dispatch_event(owner: str, repo: str, workflow_id: int, ref: str, inputs: dict = None):
    """
    Create a workflow dispatch event.
    https://docs.github.com/en/rest/actions/workflows#create-a-workflow-dispatch-event
    """
    json_data = {"ref": ref, "inputs": inputs}
    return _github_api_request("POST", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches", json_data=json_data)
