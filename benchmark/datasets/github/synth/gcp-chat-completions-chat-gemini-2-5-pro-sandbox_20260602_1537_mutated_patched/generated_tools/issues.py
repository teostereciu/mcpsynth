from .utils import _github_api_request

def list_issues_for_authenticated_user(filter: str = None, state: str = "open", labels: str = None, sort: str = "created", direction: str = "desc", since: str = None, per_page: int = 30, page: int = 1):
    """
    List issues assigned to the authenticated user.
    https://docs.github.com/en/rest/issues/issues#list-issues-assigned-to-the-authenticated-user
    """
    return _github_api_request("GET", "/issues", params={"filter": filter, "state": state, "labels": labels, "sort": sort, "direction": direction, "since": since, "per_page": per_page, "page": page})

def list_organization_issues_for_authenticated_user(org: str, filter: str = None, state: str = "open", labels: str = None, sort: str = "created", direction: str = "desc", since: str = None, per_page: int = 30, page: int = 1):
    """
    List organization issues assigned to the authenticated user.
    https://docs.github.com/en/rest/issues/issues#list-organization-issues-assigned-to-the-authenticated-user
    """
    return _github_api_request("GET", f"/orgs/{org}/issues", params={"filter": filter, "state": state, "labels": labels, "sort": sort, "direction": direction, "since": since, "per_page": per_page, "page": page})

def list_repository_issues(owner: str, repo: str, milestone: str = None, state: str = "open", assignee: str = None, creator: str = None, mentioned: str = None, labels: str = None, sort: str = "created", direction: str = "desc", since: str = None, per_page: int = 30, page: int = 1):
    """
    List repository issues.
    https://docs.github.com/en/rest/issues/issues#list-repository-issues
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}/issues", params={"milestone": milestone, "state": state, "assignee": assignee, "creator": creator, "mentioned": mentioned, "labels": labels, "sort": sort, "direction": direction, "since": since, "per_page": per_page, "page": page})

def create_issue(owner: str, repo: str, title: str, body: str = None, assignee: str = None, milestone: str = None, labels: list = None, assignees: list = None):
    """
    Create an issue.
    https://docs.github.com/en/rest/issues/issues#create-an-issue
    """
    json_data = {"title": title, "body": body, "assignee": assignee, "milestone": milestone, "labels": labels, "assignees": assignees}
    return _github_api_request("POST", f"/repos/{owner}/{repo}/issues", json_data=json_data)

def get_issue(owner: str, repo: str, issue_number: int):
    """
    Get an issue.
    https://docs.github.com/en/rest/issues/issues#get-an-issue
    """
    return _github_api_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")

def update_issue(owner: str, repo: str, issue_number: int, title: str = None, body: str = None, state: str = None, milestone: str = None, labels: list = None, assignees: list = None):
    """
    Update an issue.
    https://docs.github.com/en/rest/issues/issues#update-an-issue
    """
    json_data = {"title": title, "body": body, "state": state, "milestone": milestone, "labels": labels, "assignees": assignees}
    return _github_api_request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json_data=json_data)

def lock_issue(owner: str, repo: str, issue_number: int, lock_reason: str = None):
    """
    Lock an issue.
    https://docs.github.com/en/rest/issues/issues#lock-an-issue
    """
    json_data = {"lock_reason": lock_reason}
    return _github_api_request("PUT", f"/repos/{owner}/{repo}/issues/{issue_number}/lock", json_data=json_data)

def unlock_issue(owner: str, repo: str, issue_number: int):
    """
    Unlock an issue.
    https://docs.github.com/en/rest/issues/issues#unlock-an-issue
    """
    return _github_api_request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/lock")
