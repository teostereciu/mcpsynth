from __future__ import annotations

import os
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.github_client import GitHubClient
from generated_tools import (
    issues,
    pulls,
    repos,
    contents,
    releases,
    actions_workflows,
    actions_runs,
    search,
    branch_protection,
)


mcp = FastMCP("github-rest")


def _client() -> GitHubClient:
    return GitHubClient(
        token=os.getenv("GITHUB_TOKEN"),
        base_url=os.getenv("GITHUB_API_BASE_URL"),
        api_version=os.getenv("GITHUB_API_VERSION", "2026-03-10"),
    )


@mcp.tool()
def github_api_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    paginate: bool = False,
    raw: bool = False,
) -> Any:
    """Generic GitHub REST API request.

    Args:
      method: HTTP method (GET/POST/PATCH/PUT/DELETE)
      path: API path, e.g. /repos/{owner}/{repo}
      params: Query parameters
      json: JSON body
      paginate: If true and GET, follow Link rel="next" and return combined list
      raw: If true, return raw text body and headers
    """
    return _client().request(method, path, params=params, json=json, paginate=paginate, raw=raw)


# Issues
@mcp.tool()
def list_my_issues(**kwargs) -> Any:
    return issues.list_my_issues(_client(), **kwargs)


@mcp.tool()
def list_repo_issues(**kwargs) -> Any:
    return issues.list_repo_issues(_client(), **kwargs)


@mcp.tool()
def get_issue(owner: str, repo: str, issue_number: int) -> Any:
    return issues.get_issue(_client(), owner=owner, repo=repo, issue_number=issue_number)


@mcp.tool()
def create_issue(**kwargs) -> Any:
    return issues.create_issue(_client(), **kwargs)


@mcp.tool()
def update_issue(**kwargs) -> Any:
    return issues.update_issue(_client(), **kwargs)


@mcp.tool()
def lock_issue(**kwargs) -> Any:
    return issues.lock_issue(_client(), **kwargs)


@mcp.tool()
def unlock_issue(**kwargs) -> Any:
    return issues.unlock_issue(_client(), **kwargs)


@mcp.tool()
def add_assignees(**kwargs) -> Any:
    return issues.add_assignees(_client(), **kwargs)


@mcp.tool()
def remove_assignees(**kwargs) -> Any:
    return issues.remove_assignees(_client(), **kwargs)


# Pull requests
@mcp.tool()
def list_pulls(**kwargs) -> Any:
    return pulls.list_pulls(_client(), **kwargs)


@mcp.tool()
def get_pull(owner: str, repo: str, pull_number: int) -> Any:
    return pulls.get_pull(_client(), owner=owner, repo=repo, pull_number=pull_number)


@mcp.tool()
def create_pull(**kwargs) -> Any:
    return pulls.create_pull(_client(), **kwargs)


@mcp.tool()
def update_pull(**kwargs) -> Any:
    return pulls.update_pull(_client(), **kwargs)


@mcp.tool()
def merge_pull(**kwargs) -> Any:
    return pulls.merge_pull(_client(), **kwargs)


@mcp.tool()
def request_reviewers(**kwargs) -> Any:
    return pulls.request_reviewers(_client(), **kwargs)


@mcp.tool()
def remove_requested_reviewers(**kwargs) -> Any:
    return pulls.remove_requested_reviewers(_client(), **kwargs)


# Repositories
@mcp.tool()
def get_repo(owner: str, repo: str) -> Any:
    return repos.get_repo(_client(), owner=owner, repo=repo)


@mcp.tool()
def list_org_repos(**kwargs) -> Any:
    return repos.list_org_repos(_client(), **kwargs)


@mcp.tool()
def list_user_repos(**kwargs) -> Any:
    return repos.list_user_repos(_client(), **kwargs)


@mcp.tool()
def create_org_repo(**kwargs) -> Any:
    return repos.create_org_repo(_client(), **kwargs)


@mcp.tool()
def create_user_repo(**kwargs) -> Any:
    return repos.create_user_repo(_client(), **kwargs)


@mcp.tool()
def fork_repo(**kwargs) -> Any:
    return repos.fork_repo(_client(), **kwargs)


@mcp.tool()
def update_repo(**kwargs) -> Any:
    return repos.update_repo(_client(), **kwargs)


# Contents
@mcp.tool()
def get_content(**kwargs) -> Any:
    return contents.get_content(_client(), **kwargs)


@mcp.tool()
def create_or_update_file(**kwargs) -> Any:
    return contents.create_or_update_file(_client(), **kwargs)


@mcp.tool()
def delete_file(**kwargs) -> Any:
    return contents.delete_file(_client(), **kwargs)


# Releases
@mcp.tool()
def list_releases(**kwargs) -> Any:
    return releases.list_releases(_client(), **kwargs)


@mcp.tool()
def get_latest_release(**kwargs) -> Any:
    return releases.get_latest_release(_client(), **kwargs)


@mcp.tool()
def get_release(**kwargs) -> Any:
    return releases.get_release(_client(), **kwargs)


@mcp.tool()
def create_release(**kwargs) -> Any:
    return releases.create_release(_client(), **kwargs)


@mcp.tool()
def update_release(**kwargs) -> Any:
    return releases.update_release(_client(), **kwargs)


@mcp.tool()
def delete_release(**kwargs) -> Any:
    return releases.delete_release(_client(), **kwargs)


@mcp.tool()
def generate_release_notes(**kwargs) -> Any:
    return releases.generate_release_notes(_client(), **kwargs)


# Actions: workflows
@mcp.tool()
def list_workflows(**kwargs) -> Any:
    return actions_workflows.list_workflows(_client(), **kwargs)


@mcp.tool()
def get_workflow(**kwargs) -> Any:
    return actions_workflows.get_workflow(_client(), **kwargs)


@mcp.tool()
def enable_workflow(**kwargs) -> Any:
    return actions_workflows.enable_workflow(_client(), **kwargs)


@mcp.tool()
def disable_workflow(**kwargs) -> Any:
    return actions_workflows.disable_workflow(_client(), **kwargs)


@mcp.tool()
def create_workflow_dispatch(**kwargs) -> Any:
    return actions_workflows.create_workflow_dispatch(_client(), **kwargs)


@mcp.tool()
def get_workflow_timing(**kwargs) -> Any:
    return actions_workflows.get_workflow_timing(_client(), **kwargs)


# Actions: runs
@mcp.tool()
def list_workflow_runs(**kwargs) -> Any:
    return actions_runs.list_workflow_runs(_client(), **kwargs)


@mcp.tool()
def get_workflow_run(**kwargs) -> Any:
    return actions_runs.get_workflow_run(_client(), **kwargs)


@mcp.tool()
def cancel_workflow_run(**kwargs) -> Any:
    return actions_runs.cancel_workflow_run(_client(), **kwargs)


@mcp.tool()
def rerun_workflow_run(**kwargs) -> Any:
    return actions_runs.rerun_workflow_run(_client(), **kwargs)


@mcp.tool()
def rerun_job(**kwargs) -> Any:
    return actions_runs.rerun_job(_client(), **kwargs)


# Search
@mcp.tool()
def search_code(**kwargs) -> Any:
    return search.search_code(_client(), **kwargs)


@mcp.tool()
def search_issues_and_prs(**kwargs) -> Any:
    return search.search_issues_and_prs(_client(), **kwargs)


@mcp.tool()
def search_repositories(**kwargs) -> Any:
    return search.search_repositories(_client(), **kwargs)


@mcp.tool()
def search_users(**kwargs) -> Any:
    return search.search_users(_client(), **kwargs)


# Branch protection
@mcp.tool()
def get_branch_protection(**kwargs) -> Any:
    return branch_protection.get_branch_protection(_client(), **kwargs)


@mcp.tool()
def update_branch_protection(**kwargs) -> Any:
    return branch_protection.update_branch_protection(_client(), **kwargs)


@mcp.tool()
def delete_branch_protection(**kwargs) -> Any:
    return branch_protection.delete_branch_protection(_client(), **kwargs)


if __name__ == "__main__":
    mcp.run()
