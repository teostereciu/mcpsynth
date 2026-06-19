"""GitHub Deployments tools."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_post, github_put, github_delete


def list_deployments(owner: str, repo: str, sha: Optional[str] = None,
                     ref: Optional[str] = None, task: Optional[str] = None,
                     environment: Optional[str] = None,
                     per_page: int = 30, page: int = 1) -> Any:
    """List deployments.

    Args:
        owner: Repository owner
        repo: Repository name
        sha: Filter by SHA
        ref: Filter by ref
        task: Filter by task
        environment: Filter by environment
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"per_page": per_page, "page": page}
    if sha:
        params["sha"] = sha
    if ref:
        params["ref"] = ref
    if task:
        params["task"] = task
    if environment:
        params["environment"] = environment
    return github_get(f"/repos/{owner}/{repo}/deployments", params)


def create_deployment(owner: str, repo: str, ref: str, task: str = "deploy",
                      auto_merge: bool = True, environment: str = "production",
                      description: Optional[str] = None,
                      required_contexts: Optional[list] = None,
                      payload: Optional[dict] = None,
                      transient_environment: bool = False,
                      production_environment: bool = True) -> Any:
    """Create a deployment.

    Args:
        owner: Repository owner
        repo: Repository name
        ref: Git ref to deploy (branch, SHA, or tag)
        task: Task to execute
        auto_merge: Whether to auto-merge the default branch
        environment: Environment name
        description: Description
        required_contexts: Required status contexts
        payload: JSON payload with extra information
        transient_environment: Whether the environment is transient
        production_environment: Whether the environment is production
    """
    data = {"ref": ref, "task": task, "auto_merge": auto_merge, "environment": environment,
            "transient_environment": transient_environment, "production_environment": production_environment}
    if description:
        data["description"] = description
    if required_contexts is not None:
        data["required_contexts"] = required_contexts
    if payload:
        data["payload"] = payload
    return github_post(f"/repos/{owner}/{repo}/deployments", data)


def get_deployment(owner: str, repo: str, deployment_id: int) -> Any:
    """Get a deployment.

    Args:
        owner: Repository owner
        repo: Repository name
        deployment_id: Deployment ID
    """
    return github_get(f"/repos/{owner}/{repo}/deployments/{deployment_id}")


def delete_deployment(owner: str, repo: str, deployment_id: int) -> Any:
    """Delete a deployment.

    Args:
        owner: Repository owner
        repo: Repository name
        deployment_id: Deployment ID
    """
    return github_delete(f"/repos/{owner}/{repo}/deployments/{deployment_id}")


def list_deployment_statuses(owner: str, repo: str, deployment_id: int,
                             per_page: int = 30, page: int = 1) -> Any:
    """List deployment statuses.

    Args:
        owner: Repository owner
        repo: Repository name
        deployment_id: Deployment ID
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses",
                      {"per_page": per_page, "page": page})


def create_deployment_status(owner: str, repo: str, deployment_id: int, state: str,
                             target_url: Optional[str] = None, log_url: Optional[str] = None,
                             description: Optional[str] = None,
                             environment: Optional[str] = None,
                             environment_url: Optional[str] = None,
                             auto_inactive: bool = True) -> Any:
    """Create a deployment status.

    Args:
        owner: Repository owner
        repo: Repository name
        deployment_id: Deployment ID
        state: Status state (error, failure, inactive, in_progress, queued, pending, success)
        target_url: Target URL
        log_url: Log URL
        description: Description
        environment: Environment name
        environment_url: Environment URL
        auto_inactive: Whether to mark previous deployments as inactive
    """
    data = {"state": state, "auto_inactive": auto_inactive}
    if target_url:
        data["target_url"] = target_url
    if log_url:
        data["log_url"] = log_url
    if description:
        data["description"] = description
    if environment:
        data["environment"] = environment
    if environment_url:
        data["environment_url"] = environment_url
    return github_post(f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses", data)


def get_deployment_status(owner: str, repo: str, deployment_id: int, status_id: int) -> Any:
    """Get a deployment status.

    Args:
        owner: Repository owner
        repo: Repository name
        deployment_id: Deployment ID
        status_id: Status ID
    """
    return github_get(f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}")


def list_environments(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List environments for a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/environments", {"per_page": per_page, "page": page})


def get_environment(owner: str, repo: str, environment_name: str) -> Any:
    """Get an environment.

    Args:
        owner: Repository owner
        repo: Repository name
        environment_name: Environment name
    """
    return github_get(f"/repos/{owner}/{repo}/environments/{environment_name}")


def create_or_update_environment(owner: str, repo: str, environment_name: str,
                                  wait_timer: Optional[int] = None,
                                  reviewers: Optional[list] = None,
                                  deployment_branch_policy: Optional[dict] = None) -> Any:
    """Create or update an environment.

    Args:
        owner: Repository owner
        repo: Repository name
        environment_name: Environment name
        wait_timer: Wait timer in minutes (0-43200)
        reviewers: List of reviewer dicts (type, id)
        deployment_branch_policy: Branch policy dict (protected_branches, custom_branch_policies)
    """
    data = {}
    if wait_timer is not None:
        data["wait_timer"] = wait_timer
    if reviewers is not None:
        data["reviewers"] = reviewers
    if deployment_branch_policy is not None:
        data["deployment_branch_policy"] = deployment_branch_policy
    return github_put(f"/repos/{owner}/{repo}/environments/{environment_name}", data)


def delete_environment(owner: str, repo: str, environment_name: str) -> Any:
    """Delete an environment.

    Args:
        owner: Repository owner
        repo: Repository name
        environment_name: Environment name
    """
    return github_delete(f"/repos/{owner}/{repo}/environments/{environment_name}")
