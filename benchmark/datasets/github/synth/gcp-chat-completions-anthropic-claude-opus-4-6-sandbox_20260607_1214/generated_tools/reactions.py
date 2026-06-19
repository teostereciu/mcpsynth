"""GitHub Reactions tools."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_post, github_delete


def list_reactions_for_issue(owner: str, repo: str, issue_number: int,
                             content: Optional[str] = None,
                             per_page: int = 30, page: int = 1) -> Any:
    """List reactions for an issue.

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        content: Filter by reaction type (+1, -1, laugh, confused, heart, hooray, rocket, eyes)
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"per_page": per_page, "page": page}
    if content:
        params["content"] = content
    return github_get(f"/repos/{owner}/{repo}/issues/{issue_number}/reactions", params)


def create_reaction_for_issue(owner: str, repo: str, issue_number: int, content: str) -> Any:
    """Create a reaction for an issue.

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        content: Reaction type (+1, -1, laugh, confused, heart, hooray, rocket, eyes)
    """
    return github_post(f"/repos/{owner}/{repo}/issues/{issue_number}/reactions", {"content": content})


def delete_issue_reaction(owner: str, repo: str, issue_number: int, reaction_id: int) -> Any:
    """Delete an issue reaction.

    Args:
        owner: Repository owner
        repo: Repository name
        issue_number: Issue number
        reaction_id: Reaction ID
    """
    return github_delete(f"/repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id}")


def list_reactions_for_issue_comment(owner: str, repo: str, comment_id: int,
                                     content: Optional[str] = None,
                                     per_page: int = 30, page: int = 1) -> Any:
    """List reactions for an issue comment.

    Args:
        owner: Repository owner
        repo: Repository name
        comment_id: Comment ID
        content: Filter by reaction type
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"per_page": per_page, "page": page}
    if content:
        params["content"] = content
    return github_get(f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions", params)


def create_reaction_for_issue_comment(owner: str, repo: str, comment_id: int, content: str) -> Any:
    """Create a reaction for an issue comment.

    Args:
        owner: Repository owner
        repo: Repository name
        comment_id: Comment ID
        content: Reaction type (+1, -1, laugh, confused, heart, hooray, rocket, eyes)
    """
    return github_post(f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions", {"content": content})


def delete_issue_comment_reaction(owner: str, repo: str, comment_id: int, reaction_id: int) -> Any:
    """Delete an issue comment reaction.

    Args:
        owner: Repository owner
        repo: Repository name
        comment_id: Comment ID
        reaction_id: Reaction ID
    """
    return github_delete(f"/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id}")


def create_reaction_for_pr_review_comment(owner: str, repo: str, comment_id: int, content: str) -> Any:
    """Create a reaction for a pull request review comment.

    Args:
        owner: Repository owner
        repo: Repository name
        comment_id: Comment ID
        content: Reaction type (+1, -1, laugh, confused, heart, hooray, rocket, eyes)
    """
    return github_post(f"/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions", {"content": content})


def create_reaction_for_release(owner: str, repo: str, release_id: int, content: str) -> Any:
    """Create a reaction for a release.

    Args:
        owner: Repository owner
        repo: Repository name
        release_id: Release ID
        content: Reaction type (+1, laugh, heart, hooray, rocket, eyes)
    """
    return github_post(f"/repos/{owner}/{repo}/releases/{release_id}/reactions", {"content": content})
