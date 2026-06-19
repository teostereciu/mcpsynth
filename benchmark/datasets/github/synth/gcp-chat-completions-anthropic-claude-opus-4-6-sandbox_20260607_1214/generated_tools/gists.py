"""GitHub Gists tools."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_post, github_patch, github_put, github_delete


def list_gists(since: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """List gists for the authenticated user.

    Args:
        since: Only gists updated after this ISO 8601 timestamp
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"per_page": per_page, "page": page}
    if since:
        params["since"] = since
    return github_get("/gists", params)


def create_gist(files: dict, description: Optional[str] = None, public: bool = False) -> Any:
    """Create a gist.

    Args:
        files: Dict of filename to content dict (e.g. {"file.txt": {"content": "hello"}})
        description: Gist description
        public: Whether the gist is public
    """
    data = {"files": files, "public": public}
    if description:
        data["description"] = description
    return github_post("/gists", data)


def get_gist(gist_id: str) -> Any:
    """Get a gist.

    Args:
        gist_id: Gist ID
    """
    return github_get(f"/gists/{gist_id}")


def update_gist(gist_id: str, files: Optional[dict] = None, description: Optional[str] = None) -> Any:
    """Update a gist.

    Args:
        gist_id: Gist ID
        files: Dict of filename to content dict (set content to empty string to delete)
        description: New description
    """
    data = {}
    if files:
        data["files"] = files
    if description is not None:
        data["description"] = description
    return github_patch(f"/gists/{gist_id}", data)


def delete_gist(gist_id: str) -> Any:
    """Delete a gist.

    Args:
        gist_id: Gist ID
    """
    return github_delete(f"/gists/{gist_id}")


def list_gist_comments(gist_id: str, per_page: int = 30, page: int = 1) -> Any:
    """List comments on a gist.

    Args:
        gist_id: Gist ID
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/gists/{gist_id}/comments", {"per_page": per_page, "page": page})


def create_gist_comment(gist_id: str, body: str) -> Any:
    """Create a comment on a gist.

    Args:
        gist_id: Gist ID
        body: Comment body text
    """
    return github_post(f"/gists/{gist_id}/comments", {"body": body})


def fork_gist(gist_id: str) -> Any:
    """Fork a gist.

    Args:
        gist_id: Gist ID
    """
    return github_post(f"/gists/{gist_id}/forks")


def star_gist(gist_id: str) -> Any:
    """Star a gist.

    Args:
        gist_id: Gist ID
    """
    return github_put(f"/gists/{gist_id}/star")


def unstar_gist(gist_id: str) -> Any:
    """Unstar a gist.

    Args:
        gist_id: Gist ID
    """
    return github_delete(f"/gists/{gist_id}/star")


def check_gist_starred(gist_id: str) -> Any:
    """Check if a gist is starred.

    Args:
        gist_id: Gist ID
    """
    return github_get(f"/gists/{gist_id}/star")
