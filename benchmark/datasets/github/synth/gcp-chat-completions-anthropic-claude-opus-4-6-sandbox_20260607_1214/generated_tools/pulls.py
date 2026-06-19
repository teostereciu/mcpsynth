"""GitHub Pull Requests tools."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_post, github_patch, github_put, github_delete


def list_pull_requests(owner: str, repo: str, state: str = "open", head: Optional[str] = None,
                       base: Optional[str] = None, sort: str = "created", direction: str = "desc",
                       per_page: int = 30, page: int = 1) -> Any:
    """List pull requests in a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        state: State filter (open, closed, all)
        head: Filter by head user/org and branch (format: user:ref-name or org:ref-name)
        base: Filter by base branch name
        sort: Sort by (created, updated, popularity, long-running)
        direction: Sort direction (asc, desc)
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"state": state, "sort": sort, "direction": direction, "per_page": per_page, "page": page}
    if head:
        params["head"] = head
    if base:
        params["base"] = base
    return github_get(f"/repos/{owner}/{repo}/pulls", params)


def create_pull_request(owner: str, repo: str, title: str, head: str, base: str,
                        body: Optional[str] = None, draft: bool = False,
                        maintainer_can_modify: bool = True) -> Any:
    """Create a pull request.

    Args:
        owner: Repository owner
        repo: Repository name
        title: PR title
        head: The name of the branch where your changes are implemented (or user:branch for cross-repo)
        base: The name of the branch you want the changes pulled into
        body: PR body text
        draft: Whether to create as draft PR
        maintainer_can_modify: Whether maintainers can modify the PR
    """
    data = {"title": title, "head": head, "base": base, "draft": draft,
            "maintainer_can_modify": maintainer_can_modify}
    if body is not None:
        data["body"] = body
    return github_post(f"/repos/{owner}/{repo}/pulls", data)


def get_pull_request(owner: str, repo: str, pull_number: int) -> Any:
    """Get a pull request.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
    """
    return github_get(f"/repos/{owner}/{repo}/pulls/{pull_number}")


def update_pull_request(owner: str, repo: str, pull_number: int, title: Optional[str] = None,
                        body: Optional[str] = None, state: Optional[str] = None,
                        base: Optional[str] = None, maintainer_can_modify: Optional[bool] = None) -> Any:
    """Update a pull request.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        title: New title
        body: New body text
        state: New state (open, closed)
        base: New base branch
        maintainer_can_modify: Whether maintainers can modify
    """
    data = {}
    if title is not None:
        data["title"] = title
    if body is not None:
        data["body"] = body
    if state is not None:
        data["state"] = state
    if base is not None:
        data["base"] = base
    if maintainer_can_modify is not None:
        data["maintainer_can_modify"] = maintainer_can_modify
    return github_patch(f"/repos/{owner}/{repo}/pulls/{pull_number}", data)


def list_pull_request_commits(owner: str, repo: str, pull_number: int,
                              per_page: int = 30, page: int = 1) -> Any:
    """List commits on a pull request.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/pulls/{pull_number}/commits",
                      {"per_page": per_page, "page": page})


def list_pull_request_files(owner: str, repo: str, pull_number: int,
                            per_page: int = 30, page: int = 1) -> Any:
    """List files changed in a pull request.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/pulls/{pull_number}/files",
                      {"per_page": per_page, "page": page})


def check_pull_request_merged(owner: str, repo: str, pull_number: int) -> Any:
    """Check if a pull request has been merged.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
    """
    return github_get(f"/repos/{owner}/{repo}/pulls/{pull_number}/merge")


def merge_pull_request(owner: str, repo: str, pull_number: int, commit_title: Optional[str] = None,
                       commit_message: Optional[str] = None, sha: Optional[str] = None,
                       merge_method: str = "merge") -> Any:
    """Merge a pull request.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        commit_title: Title for the merge commit
        commit_message: Message for the merge commit
        sha: SHA that PR head must match to allow merge
        merge_method: Merge method (merge, squash, rebase)
    """
    data = {"merge_method": merge_method}
    if commit_title:
        data["commit_title"] = commit_title
    if commit_message:
        data["commit_message"] = commit_message
    if sha:
        data["sha"] = sha
    return github_put(f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", data)


def update_pull_request_branch(owner: str, repo: str, pull_number: int,
                               expected_head_sha: Optional[str] = None) -> Any:
    """Update a pull request branch with the base branch.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        expected_head_sha: Expected SHA of the PR's HEAD ref
    """
    data = {}
    if expected_head_sha:
        data["expected_head_sha"] = expected_head_sha
    return github_put(f"/repos/{owner}/{repo}/pulls/{pull_number}/update-branch", data)


def list_pull_request_reviews(owner: str, repo: str, pull_number: int,
                              per_page: int = 30, page: int = 1) -> Any:
    """List reviews for a pull request.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
                      {"per_page": per_page, "page": page})


def create_pull_request_review(owner: str, repo: str, pull_number: int, event: str,
                               body: Optional[str] = None, comments: Optional[list] = None,
                               commit_id: Optional[str] = None) -> Any:
    """Create a review for a pull request.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        event: Review action (APPROVE, REQUEST_CHANGES, COMMENT)
        body: Review body text
        comments: List of review comments (each with path, position/line, body)
        commit_id: SHA of commit to review
    """
    data = {"event": event}
    if body:
        data["body"] = body
    if comments:
        data["comments"] = comments
    if commit_id:
        data["commit_id"] = commit_id
    return github_post(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", data)


def get_pull_request_review(owner: str, repo: str, pull_number: int, review_id: int) -> Any:
    """Get a review for a pull request.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        review_id: Review ID
    """
    return github_get(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}")


def dismiss_pull_request_review(owner: str, repo: str, pull_number: int, review_id: int,
                                message: str, event: str = "DISMISS") -> Any:
    """Dismiss a review for a pull request.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        review_id: Review ID
        message: Dismissal message
        event: Must be DISMISS
    """
    return github_put(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals",
                      {"message": message, "event": event})


def submit_pull_request_review(owner: str, repo: str, pull_number: int, review_id: int,
                               event: str, body: Optional[str] = None) -> Any:
    """Submit a pending review for a pull request.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        review_id: Review ID
        event: Review action (APPROVE, REQUEST_CHANGES, COMMENT)
        body: Review body text
    """
    data = {"event": event}
    if body:
        data["body"] = body
    return github_post(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events", data)


def request_reviewers(owner: str, repo: str, pull_number: int,
                      reviewers: Optional[list] = None, team_reviewers: Optional[list] = None) -> Any:
    """Request reviewers for a pull request.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        reviewers: List of usernames to request review from
        team_reviewers: List of team slugs to request review from
    """
    data = {}
    if reviewers:
        data["reviewers"] = reviewers
    if team_reviewers:
        data["team_reviewers"] = team_reviewers
    return github_post(f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", data)


def remove_requested_reviewers(owner: str, repo: str, pull_number: int,
                               reviewers: Optional[list] = None, team_reviewers: Optional[list] = None) -> Any:
    """Remove requested reviewers from a pull request.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        reviewers: List of usernames to remove
        team_reviewers: List of team slugs to remove
    """
    data = {}
    if reviewers:
        data["reviewers"] = reviewers
    if team_reviewers:
        data["team_reviewers"] = team_reviewers
    return github_delete(f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", data)


def get_requested_reviewers(owner: str, repo: str, pull_number: int) -> Any:
    """Get all requested reviewers for a pull request.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
    """
    return github_get(f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers")


def list_review_comments_on_pr(owner: str, repo: str, pull_number: int,
                               sort: str = "created", direction: str = "desc",
                               since: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """List review comments on a pull request.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        sort: Sort by (created, updated)
        direction: Sort direction (asc, desc)
        since: Only comments updated after this ISO 8601 timestamp
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"sort": sort, "direction": direction, "per_page": per_page, "page": page}
    if since:
        params["since"] = since
    return github_get(f"/repos/{owner}/{repo}/pulls/{pull_number}/comments", params)


def create_review_comment(owner: str, repo: str, pull_number: int, body: str,
                          path: str, line: Optional[int] = None, side: Optional[str] = None,
                          commit_id: Optional[str] = None, subject_type: Optional[str] = None,
                          start_line: Optional[int] = None, start_side: Optional[str] = None) -> Any:
    """Create a review comment on a pull request.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        body: Comment body text
        path: Relative file path
        line: Line number in the diff
        side: Side of the diff (LEFT, RIGHT)
        commit_id: SHA of the commit to comment on
        subject_type: Subject type (line, file)
        start_line: Start line for multi-line comment
        start_side: Start side for multi-line comment
    """
    data = {"body": body, "path": path}
    if line is not None:
        data["line"] = line
    if side:
        data["side"] = side
    if commit_id:
        data["commit_id"] = commit_id
    if subject_type:
        data["subject_type"] = subject_type
    if start_line is not None:
        data["start_line"] = start_line
    if start_side:
        data["start_side"] = start_side
    return github_post(f"/repos/{owner}/{repo}/pulls/{pull_number}/comments", data)


def create_reply_for_review_comment(owner: str, repo: str, pull_number: int,
                                    comment_id: int, body: str) -> Any:
    """Create a reply to a review comment.

    Args:
        owner: Repository owner
        repo: Repository name
        pull_number: Pull request number
        comment_id: Comment ID to reply to
        body: Reply body text
    """
    return github_post(f"/repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies",
                       {"body": body})
