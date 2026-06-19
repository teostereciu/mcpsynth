
import os
import json
import requests
from mcp.server.fastmcp import FastMCP

class GitHub:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN')}",
        })
        self.base_url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")

    def _request(self, method, path, **kwargs):
        url = f"{self.base_url}{path}"
        response = self.session.request(method, url, **kwargs)
        if response.status_code >= 400:
            return {"error": response.text}
        if response.status_code == 204:
            return {}
        return response.json()

    def list_workflow_runs(self, owner: str, repo: str, workflow_id: str):
        """List workflow runs for a workflow."""
        return self._request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs")

    def search_code(self, query: str):
        """Search for code."""
        return self._request("GET", "/search/code", params={"q": query})

    def create_repository(self, name: str, description: str = None, private: bool = False):
        """Create a new repository for the authenticated user."""
        data = {"name": name, "private": private}
        if description:
            data["description"] = description
        return self._request("POST", "/user/repos", json=data)

    def create_comment(self, owner: str, repo: str, issue_number: int, body: str):
        """Create a comment on an issue."""
        return self._request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json={"body": body})

    def get_repository_contents(self, owner: str, repo: str, path: str, ref: str = None):
        """Gets the contents of a file or directory in a repository."""
        url = f"/repos/{owner}/{repo}/contents/{path}"
        params = {}
        if ref:
            params["ref"] = ref
        return self._request("GET", url, params=params)

    def merge_pull_request(self, owner: str, repo: str, pull_number: int, commit_title: str = None, commit_message: str = None, merge_method: str = None):
        """Merge a pull request."""
        data = {}
        if commit_title:
            data["commit_title"] = commit_title
        if commit_message:
            data["commit_message"] = commit_message
        if merge_method:
            data["merge_method"] = merge_method
        return self._request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=data)

    def get_pull_request(self, owner: str, repo: str, pull_number: int):
        """Get a pull request."""
        return self._request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")

    def create_pull_request(self, owner: str, repo: str, title: str, head: str, base: str, body: str = None):
        """Create a pull request."""
        data = {
            "title": title,
            "head": head,
            "base": base,
        }
        if body:
            data["body"] = body
        return self._request("POST", f"/repos/{owner}/{repo}/pulls", json=data)

    def update_issue(self, owner: str, repo: str, issue_number: int, title: str = None, body: str = None, state: str = None, labels: list = None, assignees: list = None):
        """Update an issue."""
        data = {}
        if title:
            data["title"] = title
        if body:
            data["body"] = body
        if state:
            data["state"] = state
        if labels:
            data["labels"] = labels
        if assignees:
            data["assignees"] = assignees
        return self._request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=data)

    def get_issue(self, owner: str, repo: str, issue_number: int):
        """Get an issue."""
        return self._request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")

    def create_issue(self, owner: str, repo: str, title: str, body: str = None, labels: list = None, assignees: list = None):
        """Create an issue."""
        data = {"title": title}
        if body:
            data["body"] = body
        if labels:
            data["labels"] = labels
        if assignees:
            data["assignees"] = assignees
        return self._request("POST", f"/repos/{owner}/{repo}/issues", json=data)

    def list_user_repositories(self, username: str):
        """List public repositories for the specified user."""
        return self._request("GET", f"/users/{username}/repos")

    def get_repository(self, owner: str, repo: str):
        """Get a repository."""
        return self._request("GET", f"/repos/{owner}/{repo}")

if __name__ == "__main__":
    server = FastMCP()
    server.register_tools(GitHub(), "github")
    server.run()
