"""GitHub Git Data tools (refs, trees, commits, tags, blobs)."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_post, github_patch, github_delete


def list_matching_references(owner: str, repo: str, ref: str) -> Any:
    """List matching references (e.g. tags or heads).

    Args:
        owner: Repository owner
        repo: Repository name
        ref: Reference prefix (e.g. 'heads/main', 'tags/v1')
    """
    return github_get(f"/repos/{owner}/{repo}/git/matching-refs/{ref}")


def get_reference(owner: str, repo: str, ref: str) -> Any:
    """Get a reference.

    Args:
        owner: Repository owner
        repo: Repository name
        ref: Reference (e.g. 'heads/main', 'tags/v1.0')
    """
    return github_get(f"/repos/{owner}/{repo}/git/ref/{ref}")


def create_reference(owner: str, repo: str, ref: str, sha: str) -> Any:
    """Create a reference (branch or tag).

    Args:
        owner: Repository owner
        repo: Repository name
        ref: Full reference (e.g. 'refs/heads/new-branch', 'refs/tags/v1.0')
        sha: SHA to point the reference to
    """
    return github_post(f"/repos/{owner}/{repo}/git/refs", {"ref": ref, "sha": sha})


def update_reference(owner: str, repo: str, ref: str, sha: str, force: bool = False) -> Any:
    """Update a reference.

    Args:
        owner: Repository owner
        repo: Repository name
        ref: Reference to update (e.g. 'heads/main')
        sha: New SHA to point to
        force: Whether to force the update
    """
    return github_patch(f"/repos/{owner}/{repo}/git/refs/{ref}", {"sha": sha, "force": force})


def delete_reference(owner: str, repo: str, ref: str) -> Any:
    """Delete a reference.

    Args:
        owner: Repository owner
        repo: Repository name
        ref: Reference to delete (e.g. 'heads/branch-name', 'tags/v1.0')
    """
    return github_delete(f"/repos/{owner}/{repo}/git/refs/{ref}")


def create_tree(owner: str, repo: str, tree: list, base_tree: Optional[str] = None) -> Any:
    """Create a tree.

    Args:
        owner: Repository owner
        repo: Repository name
        tree: List of tree objects (each with path, mode, type, sha or content)
        base_tree: SHA of the base tree
    """
    data = {"tree": tree}
    if base_tree:
        data["base_tree"] = base_tree
    return github_post(f"/repos/{owner}/{repo}/git/trees", data)


def get_tree(owner: str, repo: str, tree_sha: str, recursive: Optional[bool] = None) -> Any:
    """Get a tree.

    Args:
        owner: Repository owner
        repo: Repository name
        tree_sha: Tree SHA
        recursive: Whether to recursively get the tree
    """
    params = {}
    if recursive:
        params["recursive"] = "1"
    return github_get(f"/repos/{owner}/{repo}/git/trees/{tree_sha}", params)


def create_git_commit(owner: str, repo: str, message: str, tree: str, parents: list,
                      author: Optional[dict] = None, committer: Optional[dict] = None) -> Any:
    """Create a commit.

    Args:
        owner: Repository owner
        repo: Repository name
        message: Commit message
        tree: SHA of the tree object
        parents: List of parent commit SHAs
        author: Author info dict (name, email, date)
        committer: Committer info dict (name, email, date)
    """
    data = {"message": message, "tree": tree, "parents": parents}
    if author:
        data["author"] = author
    if committer:
        data["committer"] = committer
    return github_post(f"/repos/{owner}/{repo}/git/commits", data)


def get_git_commit(owner: str, repo: str, commit_sha: str) -> Any:
    """Get a commit object.

    Args:
        owner: Repository owner
        repo: Repository name
        commit_sha: Commit SHA
    """
    return github_get(f"/repos/{owner}/{repo}/git/commits/{commit_sha}")


def create_tag(owner: str, repo: str, tag: str, message: str, object_sha: str,
               type: str = "commit", tagger: Optional[dict] = None) -> Any:
    """Create a tag object.

    Args:
        owner: Repository owner
        repo: Repository name
        tag: Tag name
        message: Tag message
        object_sha: SHA of the object to tag
        type: Type of object (commit, tree, blob)
        tagger: Tagger info dict (name, email, date)
    """
    data = {"tag": tag, "message": message, "object": object_sha, "type": type}
    if tagger:
        data["tagger"] = tagger
    return github_post(f"/repos/{owner}/{repo}/git/tags", data)


def get_tag(owner: str, repo: str, tag_sha: str) -> Any:
    """Get a tag object.

    Args:
        owner: Repository owner
        repo: Repository name
        tag_sha: Tag SHA
    """
    return github_get(f"/repos/{owner}/{repo}/git/tags/{tag_sha}")


def create_blob(owner: str, repo: str, content: str, encoding: str = "utf-8") -> Any:
    """Create a blob.

    Args:
        owner: Repository owner
        repo: Repository name
        content: Blob content
        encoding: Content encoding (utf-8 or base64)
    """
    return github_post(f"/repos/{owner}/{repo}/git/blobs", {"content": content, "encoding": encoding})


def get_blob(owner: str, repo: str, file_sha: str) -> Any:
    """Get a blob.

    Args:
        owner: Repository owner
        repo: Repository name
        file_sha: Blob SHA
    """
    return github_get(f"/repos/{owner}/{repo}/git/blobs/{file_sha}")
