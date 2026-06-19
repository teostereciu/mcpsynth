"""GitHub Actions tools."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_post, github_put, github_delete


def list_repository_workflows(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List repository workflows.

    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/actions/workflows", {"per_page": per_page, "page": page})


def get_workflow(owner: str, repo: str, workflow_id: str) -> Any:
    """Get a workflow.

    Args:
        owner: Repository owner
        repo: Repository name
        workflow_id: Workflow ID or file name (e.g. 'main.yml')
    """
    return github_get(f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")


def create_workflow_dispatch(owner: str, repo: str, workflow_id: str, ref: str,
                             inputs: Optional[dict] = None) -> Any:
    """Create a workflow dispatch event (trigger a workflow).

    Args:
        owner: Repository owner
        repo: Repository name
        workflow_id: Workflow ID or file name
        ref: Git reference (branch or tag)
        inputs: Input keys and values for the workflow
    """
    data = {"ref": ref}
    if inputs:
        data["inputs"] = inputs
    return github_post(f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches", data)


def enable_workflow(owner: str, repo: str, workflow_id: str) -> Any:
    """Enable a workflow.

    Args:
        owner: Repository owner
        repo: Repository name
        workflow_id: Workflow ID or file name
    """
    return github_put(f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable")


def disable_workflow(owner: str, repo: str, workflow_id: str) -> Any:
    """Disable a workflow.

    Args:
        owner: Repository owner
        repo: Repository name
        workflow_id: Workflow ID or file name
    """
    return github_put(f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable")


def list_workflow_runs(owner: str, repo: str, workflow_id: Optional[str] = None,
                       actor: Optional[str] = None, branch: Optional[str] = None,
                       event: Optional[str] = None, status: Optional[str] = None,
                       created: Optional[str] = None, head_sha: Optional[str] = None,
                       per_page: int = 30, page: int = 1) -> Any:
    """List workflow runs for a repository or specific workflow.

    Args:
        owner: Repository owner
        repo: Repository name
        workflow_id: Workflow ID or file name (if None, lists all runs)
        actor: Filter by actor username
        branch: Filter by branch name
        event: Filter by event type
        status: Filter by status (completed, action_required, cancelled, failure, neutral, skipped, stale, success, timed_out, in_progress, queued, requested, waiting, pending)
        created: Filter by created date range
        head_sha: Filter by HEAD SHA
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"per_page": per_page, "page": page}
    if actor:
        params["actor"] = actor
    if branch:
        params["branch"] = branch
    if event:
        params["event"] = event
    if status:
        params["status"] = status
    if created:
        params["created"] = created
    if head_sha:
        params["head_sha"] = head_sha

    if workflow_id:
        path = f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs"
    else:
        path = f"/repos/{owner}/{repo}/actions/runs"
    return github_get(path, params)


def get_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    """Get a workflow run.

    Args:
        owner: Repository owner
        repo: Repository name
        run_id: Workflow run ID
    """
    return github_get(f"/repos/{owner}/{repo}/actions/runs/{run_id}")


def cancel_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    """Cancel a workflow run.

    Args:
        owner: Repository owner
        repo: Repository name
        run_id: Workflow run ID
    """
    return github_post(f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")


def rerun_workflow(owner: str, repo: str, run_id: int) -> Any:
    """Re-run a workflow.

    Args:
        owner: Repository owner
        repo: Repository name
        run_id: Workflow run ID
    """
    return github_post(f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun")


def rerun_failed_jobs(owner: str, repo: str, run_id: int) -> Any:
    """Re-run failed jobs from a workflow run.

    Args:
        owner: Repository owner
        repo: Repository name
        run_id: Workflow run ID
    """
    return github_post(f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun-failed-jobs")


def delete_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    """Delete a workflow run.

    Args:
        owner: Repository owner
        repo: Repository name
        run_id: Workflow run ID
    """
    return github_delete(f"/repos/{owner}/{repo}/actions/runs/{run_id}")


def get_workflow_run_usage(owner: str, repo: str, run_id: int) -> Any:
    """Get workflow run usage.

    Args:
        owner: Repository owner
        repo: Repository name
        run_id: Workflow run ID
    """
    return github_get(f"/repos/{owner}/{repo}/actions/runs/{run_id}/timing")


def download_workflow_run_logs(owner: str, repo: str, run_id: int) -> Any:
    """Download workflow run logs (returns redirect URL).

    Args:
        owner: Repository owner
        repo: Repository name
        run_id: Workflow run ID
    """
    return github_get(f"/repos/{owner}/{repo}/actions/runs/{run_id}/logs")


def list_jobs_for_workflow_run(owner: str, repo: str, run_id: int,
                               filter: str = "latest", per_page: int = 30, page: int = 1) -> Any:
    """List jobs for a workflow run.

    Args:
        owner: Repository owner
        repo: Repository name
        run_id: Workflow run ID
        filter: Filter by status (latest, all)
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/actions/runs/{run_id}/jobs",
                      {"filter": filter, "per_page": per_page, "page": page})


def get_job_for_workflow_run(owner: str, repo: str, job_id: int) -> Any:
    """Get a job for a workflow run.

    Args:
        owner: Repository owner
        repo: Repository name
        job_id: Job ID
    """
    return github_get(f"/repos/{owner}/{repo}/actions/jobs/{job_id}")


def list_workflow_run_artifacts(owner: str, repo: str, run_id: int,
                                per_page: int = 30, page: int = 1) -> Any:
    """List workflow run artifacts.

    Args:
        owner: Repository owner
        repo: Repository name
        run_id: Workflow run ID
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts",
                      {"per_page": per_page, "page": page})


def list_repository_artifacts(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List artifacts for a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/actions/artifacts", {"per_page": per_page, "page": page})


def get_artifact(owner: str, repo: str, artifact_id: int) -> Any:
    """Get an artifact.

    Args:
        owner: Repository owner
        repo: Repository name
        artifact_id: Artifact ID
    """
    return github_get(f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}")


def delete_artifact(owner: str, repo: str, artifact_id: int) -> Any:
    """Delete an artifact.

    Args:
        owner: Repository owner
        repo: Repository name
        artifact_id: Artifact ID
    """
    return github_delete(f"/repos/{owner}/{repo}/actions/artifacts/{artifact_id}")
