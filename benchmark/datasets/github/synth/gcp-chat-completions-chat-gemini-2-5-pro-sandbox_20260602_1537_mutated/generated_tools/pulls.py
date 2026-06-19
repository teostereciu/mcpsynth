from .utils import _github_api_request

def list_pull_requests(owner: str, repo: str, state: str = "open", head: str = None, base: str = None, sort: str = "created", direction: str = "desc", per_page: int = 30, page: int = 1):
    """
    List pull requests.
    https://docs.github.com/en/rest/pulls/pulls#list-pull-requests
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}/pulls", params={"state": state, "head": head, "base": base, "sort": sort, "direction": direction, "per_page": per_page, "page": page})

def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: str = None, maintainer_can_modify: bool = None, draft: bool = None, issue: int = None):
    """
    Create a pull request.
    https://docs.github.com/en/rest/pulls/pulls#create-a-pull-request
    """
    json_data = {"title": title, "head": head, "base": base, "body": body, "maintainer_can_modify": maintainer_can_modify, "draft": draft, "issue": issue}
    return _github_api_request("POST", f"/repos/{owner}/{repo}/pulls", json_data=json_data)

def get_pull_request(owner: str, repo: str, pull_number: int):
    """
    Get a pull request.
    https://docs.github.com/en/rest/pulls/pulls#get-a-pull-request
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")

def update_pull_request(owner: str, repo: str, pull_number: int, title: str = None, body: str = None, state: str = None, base: str = None, maintainer_can_modify: bool = None):
    """
    Update a pull request.
    https://docs.github.com/en/rest/pulls/pulls#update-a-pull-request
    """
    json_data = {"title": title, "body": body, "state": state, "base": base, "maintainer_can_modify": maintainer_can_modify}
    return _github_api_request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json_data=json_data)

def merge_pull_request(owner: str, repo: str, pull_number: int, commit_title: str = None, commit_message: str = None, sha: str = None, merge_method: str = "merge"):
    """
    Merge a pull request.
    https://docs.github.com/en/rest/pulls/pulls#merge-a-pull-request
    """
    json_data = {"commit_title": commit_title, "commit_message": commit_message, "sha": sha, "merge_method": merge_method}
    return _github_api_request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json_data=json_data)

def list_pull_request_commits(owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1):
    """
    List commits on a pull request.
    https://docs.github.com/en/rest/pulls/pulls#list-commits-on-a-pull-request
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/commits", params={"per_page": per_page, "page": page})

def list_pull_request_files(owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1):
    """
    List files for a pull request.
    https://docs.github.com/en/rest/pulls/pulls#list-pull-requests-files
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/files", params={"per_page": per_page, "page": page})

def check_if_pull_request_has_been_merged(owner: str, repo: str, pull_number: int):
    """
    Check if a pull request has been merged.
    https://docs.github.com/en/rest/pulls/pulls#check-if-a-pull-request-has-been-merged
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge")
