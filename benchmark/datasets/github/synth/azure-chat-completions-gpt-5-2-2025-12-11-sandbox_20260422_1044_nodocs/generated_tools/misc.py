import os
from typing import Any, Dict, Optional

from .github_client import GitHubClient, parse_owner_repo


def get_authenticated_user() -> Dict[str, Any]:
    return GitHubClient().request("GET", "/user")


def get_rate_limit() -> Dict[str, Any]:
    return GitHubClient().request("GET", "/rate_limit")


def get_test_repo() -> Dict[str, Any]:
    owner_repo = os.getenv("GITHUB_TEST_REPO")
    if not owner_repo:
        return {"error": "GITHUB_TEST_REPO is not set"}
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return {"ok": True, "data": {"owner": owner, "repo": repo, "owner_repo": owner_repo}}
