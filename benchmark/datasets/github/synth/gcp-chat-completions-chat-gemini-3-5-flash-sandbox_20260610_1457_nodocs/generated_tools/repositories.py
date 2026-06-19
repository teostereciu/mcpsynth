from typing import Any, Dict, List, Optional, Union
import base64
from github_client import client

def get_repository(owner: str, repo: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Get a repository.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    """
    return client.request("GET", f"/repos/{owner}/{repo}")

def create_repository(
    name: str,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: Optional[bool] = False,
    has_issues: Optional[bool] = True,
    has_projects: Optional[bool] = True,
    has_wiki: Optional[bool] = True,
    is_template: Optional[bool] = False
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Create a new repository for the authenticated user.
    
    Parameters:
    - name: The name of the repository.
    - description: A short description of the repository.
    - homepage: A URL with more information about the repository.
    - private: Whether the repository is private.
    - has_issues: Whether issues are enabled.
    - has_projects: Whether projects are enabled.
    - has_wiki: Whether the wiki is enabled.
    - is_template: Whether this repository is a template.
    """
    data = {
        "name": name,
        "private": private,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "is_template": is_template
    }
    if description is not None: data["description"] = description
    if homepage is not None: data["homepage"] = homepage

    return client.request("POST", "/user/repos", json_data=data)

def create_fork(
    owner: str,
    repo: str,
    organization: Optional[str] = None,
    name: Optional[str] = None,
    default_branch_only: Optional[bool] = False
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Fork a repository.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - organization: Optional name of organization to fork into.
    - name: Optional name of the fork.
    - default_branch_only: Whether to fork only the default branch.
    """
    data = {"default_branch_only": default_branch_only}
    if organization is not None: data["organization"] = organization
    if name is not None: data["name"] = name

    return client.request("POST", f"/repos/{owner}/{repo}/forks", json_data=data)

def list_branches(
    owner: str,
    repo: str,
    protected: Optional[bool] = None,
    per_page: Optional[int] = 30,
    page: Optional[int] = 1
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """
    List branches in a repository.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - protected: Setting to true returns only protected branches.
    - per_page: The number of results per page (max 100).
    - page: Page number of the results to fetch.
    """
    params = {"per_page": per_page, "page": page}
    if protected is not None: params["protected"] = str(protected).lower()

    return client.request("GET", f"/repos/{owner}/{repo}/branches", params=params)

def get_branch(owner: str, repo: str, branch: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Get a branch.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - branch: The name of the branch.
    """
    return client.request("GET", f"/repos/{owner}/{repo}/branches/{branch}")

def list_commits(
    owner: str,
    repo: str,
    sha: Optional[str] = None,
    path: Optional[str] = None,
    author: Optional[str] = None,
    since: Optional[str] = None,
    until: Optional[str] = None,
    per_page: Optional[int] = 30,
    page: Optional[int] = 1
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """
    List commits in a repository.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - sha: SHA or branch to start listing commits from.
    - path: Only commits containing this file path will be returned.
    - author: GitHub username or email address to filter by.
    - since: Only commits after this date (ISO 8601).
    - until: Only commits before this date (ISO 8601).
    - per_page: The number of results per page (max 100).
    - page: Page number of the results to fetch.
    """
    params = {"per_page": per_page, "page": page}
    if sha: params["sha"] = sha
    if path: params["path"] = path
    if author: params["author"] = author
    if since: params["since"] = since
    if until: params["until"] = until

    return client.request("GET", f"/repos/{owner}/{repo}/commits", params=params)

def get_commit(owner: str, repo: str, ref: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Get a commit.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - ref: Commit SHA, branch name, or tag name.
    """
    return client.request("GET", f"/repos/{owner}/{repo}/commits/{ref}")

def get_repository_content(owner: str, repo: str, path: str, ref: Optional[str] = None) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Get repository content (file or directory).
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - path: The path to the file or directory.
    - ref: The name of the commit/branch/tag.
    """
    params = {}
    if ref: params["ref"] = ref
    return client.request("GET", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}", params=params)

def create_or_update_file_contents(
    owner: str,
    repo: str,
    path: str,
    message: str,
    content: str,
    sha: Optional[str] = None,
    branch: Optional[str] = None
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Create or update file contents.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - path: The content path.
    - message: The commit message.
    - content: The new file content (plain text, will be base64 encoded automatically).
    - sha: The blob SHA of the file being replaced (required when updating).
    - branch: The branch name.
    """
    encoded_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    data = {
        "message": message,
        "content": encoded_content
    }
    if sha: data["sha"] = sha
    if branch: data["branch"] = branch

    return client.request("PUT", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}", json_data=data)

def delete_file(
    owner: str,
    repo: str,
    path: str,
    message: str,
    sha: str,
    branch: Optional[str] = None
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Delete a file.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - path: The content path.
    - message: The commit message.
    - sha: The blob SHA of the file being deleted.
    - branch: The branch name.
    """
    data = {
        "message": message,
        "sha": sha
    }
    if branch: data["branch"] = branch

    return client.request("DELETE", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}", json_data=data)
