"""GitHub Checks tools."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_post, github_patch


def create_check_run(owner: str, repo: str, name: str, head_sha: str,
                     status: Optional[str] = None, conclusion: Optional[str] = None,
                     details_url: Optional[str] = None, external_id: Optional[str] = None,
                     output: Optional[dict] = None, started_at: Optional[str] = None,
                     completed_at: Optional[str] = None) -> Any:
    """Create a check run.

    Args:
        owner: Repository owner
        repo: Repository name
        name: Check run name
        head_sha: SHA of the commit
        status: Status (queued, in_progress, completed)
        conclusion: Conclusion (action_required, cancelled, failure, neutral, success, skipped, stale, timed_out)
        details_url: URL with more details
        external_id: External identifier
        output: Output dict with title, summary, text, annotations, images
        started_at: ISO 8601 timestamp
        completed_at: ISO 8601 timestamp
    """
    data = {"name": name, "head_sha": head_sha}
    if status:
        data["status"] = status
    if conclusion:
        data["conclusion"] = conclusion
    if details_url:
        data["details_url"] = details_url
    if external_id:
        data["external_id"] = external_id
    if output:
        data["output"] = output
    if started_at:
        data["started_at"] = started_at
    if completed_at:
        data["completed_at"] = completed_at
    return github_post(f"/repos/{owner}/{repo}/check-runs", data)


def get_check_run(owner: str, repo: str, check_run_id: int) -> Any:
    """Get a check run.

    Args:
        owner: Repository owner
        repo: Repository name
        check_run_id: Check run ID
    """
    return github_get(f"/repos/{owner}/{repo}/check-runs/{check_run_id}")


def update_check_run(owner: str, repo: str, check_run_id: int, name: Optional[str] = None,
                     status: Optional[str] = None, conclusion: Optional[str] = None,
                     details_url: Optional[str] = None, output: Optional[dict] = None,
                     completed_at: Optional[str] = None) -> Any:
    """Update a check run.

    Args:
        owner: Repository owner
        repo: Repository name
        check_run_id: Check run ID
        name: New name
        status: New status
        conclusion: Conclusion
        details_url: URL with more details
        output: Output dict
        completed_at: ISO 8601 timestamp
    """
    data = {}
    if name:
        data["name"] = name
    if status:
        data["status"] = status
    if conclusion:
        data["conclusion"] = conclusion
    if details_url:
        data["details_url"] = details_url
    if output:
        data["output"] = output
    if completed_at:
        data["completed_at"] = completed_at
    return github_patch(f"/repos/{owner}/{repo}/check-runs/{check_run_id}", data)


def list_check_runs_for_ref(owner: str, repo: str, ref: str, check_name: Optional[str] = None,
                            status: Optional[str] = None, filter: str = "latest",
                            per_page: int = 30, page: int = 1) -> Any:
    """List check runs for a Git reference.

    Args:
        owner: Repository owner
        repo: Repository name
        ref: Git reference (SHA, branch, or tag)
        check_name: Filter by check name
        status: Filter by status (queued, in_progress, completed)
        filter: Filter by latest or all (latest, all)
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"filter": filter, "per_page": per_page, "page": page}
    if check_name:
        params["check_name"] = check_name
    if status:
        params["status"] = status
    return github_get(f"/repos/{owner}/{repo}/commits/{ref}/check-runs", params)


def list_check_suites_for_ref(owner: str, repo: str, ref: str, app_id: Optional[int] = None,
                              check_name: Optional[str] = None,
                              per_page: int = 30, page: int = 1) -> Any:
    """List check suites for a Git reference.

    Args:
        owner: Repository owner
        repo: Repository name
        ref: Git reference (SHA, branch, or tag)
        app_id: Filter by GitHub App ID
        check_name: Filter by check name
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"per_page": per_page, "page": page}
    if app_id:
        params["app_id"] = app_id
    if check_name:
        params["check_name"] = check_name
    return github_get(f"/repos/{owner}/{repo}/commits/{ref}/check-suites", params)


def get_check_suite(owner: str, repo: str, check_suite_id: int) -> Any:
    """Get a check suite.

    Args:
        owner: Repository owner
        repo: Repository name
        check_suite_id: Check suite ID
    """
    return github_get(f"/repos/{owner}/{repo}/check-suites/{check_suite_id}")


def rerequest_check_suite(owner: str, repo: str, check_suite_id: int) -> Any:
    """Rerequest a check suite.

    Args:
        owner: Repository owner
        repo: Repository name
        check_suite_id: Check suite ID
    """
    return github_post(f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest")
