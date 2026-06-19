import json
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools import issues


mcp = FastMCP("github-rest")


def _ok(result: Any) -> Any:
    # Ensure JSON-serializable (FastMCP will serialize); keep as-is.
    return result


@mcp.tool()
def list_my_issues(**kwargs) -> Any:
    return _ok(issues.list_my_issues(**kwargs))


@mcp.tool()
def list_repo_issue_comments(owner: str, repo: str, **kwargs) -> Any:
    return _ok(issues.list_repo_issue_comments(owner, repo, **kwargs))


@mcp.tool()
def get_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    return _ok(issues.get_issue_comment(owner, repo, comment_id))


@mcp.tool()
def update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> Any:
    return _ok(issues.update_issue_comment(owner, repo, comment_id, body))


@mcp.tool()
def delete_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    return _ok(issues.delete_issue_comment(owner, repo, comment_id))


@mcp.tool()
def pin_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    return _ok(issues.pin_issue_comment(owner, repo, comment_id))


if __name__ == "__main__":
    mcp.run()
