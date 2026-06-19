import os
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools.issues import list_my_issues
from generated_tools.pulls import list_pull_requests
from generated_tools.repos import create_org_repo, list_org_repos

mcp = FastMCP("github-rest")


def _env_info() -> Dict[str, Any]:
    return {
        "GITHUB_API_BASE_URL": os.getenv("GITHUB_API_BASE_URL", "https://api.github.com"),
        "has_GITHUB_TOKEN": bool(os.getenv("GITHUB_TOKEN")),
        "GITHUB_TEST_REPO": os.getenv("GITHUB_TEST_REPO"),
    }


@mcp.tool()
def github_env_info() -> Dict[str, Any]:
    """Get environment configuration info (non-secret)."""
    return _env_info()


@mcp.tool()
def github_list_my_issues(**kwargs):
    return list_my_issues(**kwargs)


@mcp.tool()
def github_list_pull_requests(**kwargs):
    return list_pull_requests(**kwargs)


@mcp.tool()
def github_list_org_repos(**kwargs):
    return list_org_repos(**kwargs)


@mcp.tool()
def github_create_org_repo(**kwargs):
    return create_org_repo(**kwargs)


if __name__ == "__main__":
    mcp.run()
