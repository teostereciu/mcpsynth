import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("github-rest")

API_BASE_URL = os.getenv("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")
API_VERSION = "2026-03-10"
TOKEN = os.getenv("GITHUB_TOKEN")


def _headers(accept: str = "application/vnd.github+json") -> Dict[str, str]:
    headers = {
        "Accept": accept,
        "X-GitHub-Api-Version": API_VERSION,
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    return headers


def _request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None, accept: str = "application/vnd.github+json") -> Any:
    url = f"{API_BASE_URL}{path}"
    try:
        response = requests.request(method, url, headers=_headers(accept), params=params, json=json, timeout=60)
    except requests.RequestException as exc:
        return {"error": str(exc)}

    if response.status_code == 204:
        return {"ok": True, "status": 204}

    content_type = response.headers.get("Content-Type", "")
    if "application/json" in content_type or "+json" in content_type:
        try:
            data = response.json()
        except ValueError:
            data = {"raw": response.text}
    else:
        data = {"raw": response.text, "location": response.headers.get("Location")}

    if response.ok:
        return data
    return {"error": f"HTTP {response.status_code}", "status": response.status_code, "details": data}


def _clean(d: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in d.items() if v is not None}


@mcp.tool()
def list_repository_issues(owner: str, repo: str, state: Optional[str] = None, labels: Optional[str] = None, sort: Optional[str] = None, direction: Optional[str] = None, since: Optional[str] = None, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/issues", params=_clean(locals()))


@mcp.tool()
def create_issue(owner: str, repo: str, title: str, body: Optional[str] = None, assignees: Optional[list[str]] = None, milestone: Optional[int] = None, labels: Optional[list[str]] = None) -> Any:
    payload = _clean({"title": title, "body": body, "assignees": assignees, "milestone": milestone, "labels": labels})
    return _request("POST", f"/repos/{owner}/{repo}/issues", json=payload)


@mcp.tool()
def get_issue(owner: str, repo: str, issue_number: int) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")


@mcp.tool()
def update_issue(owner: str, repo: str, issue_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, state_reason: Optional[str] = None, milestone: Optional[int] = None, labels: Optional[list[str]] = None, assignees: Optional[list[str]] = None) -> Any:
    payload = _clean({"title": title, "body": body, "state": state, "state_reason": state_reason, "milestone": milestone, "labels": labels, "assignees": assignees})
    return _request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=payload)


@mcp.tool()
def list_issue_comments_for_repository(owner: str, repo: str, sort: Optional[str] = None, direction: Optional[str] = None, since: Optional[str] = None, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    params = _clean({"sort": sort, "direction": direction, "since": since, "per_page": per_page, "page": page})
    return _request("GET", f"/repos/{owner}/{repo}/issues/comments", params=params)


@mcp.tool()
def get_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")


@mcp.tool()
def update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> Any:
    return _request("PATCH", f"/repos/{owner}/{repo}/issues/comments/{comment_id}", json={"body": body})


@mcp.tool()
def delete_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    return _request("DELETE", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")


@mcp.tool()
def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> Any:
    return _request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json={"body": body})


@mcp.tool()
def list_pull_requests(owner: str, repo: str, state: Optional[str] = None, head: Optional[str] = None, base: Optional[str] = None, sort: Optional[str] = None, direction: Optional[str] = None, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    params = _clean({"state": state, "head": head, "base": base, "sort": sort, "direction": direction, "per_page": per_page, "page": page})
    return _request("GET", f"/repos/{owner}/{repo}/pulls", params=params)


@mcp.tool()
def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: Optional[str] = None, draft: Optional[bool] = None, maintainer_can_modify: Optional[bool] = None) -> Any:
    payload = _clean({"title": title, "head": head, "base": base, "body": body, "draft": draft, "maintainer_can_modify": maintainer_can_modify})
    return _request("POST", f"/repos/{owner}/{repo}/pulls", json=payload)


@mcp.tool()
def get_pull_request(owner: str, repo: str, pull_number: int) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")


@mcp.tool()
def update_pull_request(owner: str, repo: str, pull_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, base: Optional[str] = None, maintainer_can_modify: Optional[bool] = None) -> Any:
    payload = _clean({"title": title, "body": body, "state": state, "base": base, "maintainer_can_modify": maintainer_can_modify})
    return _request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json=payload)


@mcp.tool()
def list_pull_request_commits(owner: str, repo: str, pull_number: int, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/commits", params=_clean({"per_page": per_page, "page": page}))


@mcp.tool()
def list_pull_request_files(owner: str, repo: str, pull_number: int, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/files", params=_clean({"per_page": per_page, "page": page}))


@mcp.tool()
def check_pull_request_merged(owner: str, repo: str, pull_number: int) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge")


@mcp.tool()
def merge_pull_request(owner: str, repo: str, pull_number: int, commit_title: Optional[str] = None, commit_message: Optional[str] = None, merge_method: Optional[str] = None, sha: Optional[str] = None) -> Any:
    payload = _clean({"commit_title": commit_title, "commit_message": commit_message, "merge_method": merge_method, "sha": sha})
    return _request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=payload)


@mcp.tool()
def list_pull_review_comments(owner: str, repo: str, pull_number: Optional[int] = None, sort: Optional[str] = None, direction: Optional[str] = None, since: Optional[str] = None, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    params = _clean({"sort": sort, "direction": direction, "since": since, "per_page": per_page, "page": page})
    path = f"/repos/{owner}/{repo}/pulls/comments" if pull_number is None else f"/repos/{owner}/{repo}/pulls/{pull_number}/comments"
    return _request("GET", path, params=params)


@mcp.tool()
def get_pull_review_comment(owner: str, repo: str, comment_id: int) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/pulls/comments/{comment_id}")


@mcp.tool()
def update_pull_review_comment(owner: str, repo: str, comment_id: int, body: str) -> Any:
    return _request("PATCH", f"/repos/{owner}/{repo}/pulls/comments/{comment_id}", json={"body": body})


@mcp.tool()
def delete_pull_review_comment(owner: str, repo: str, comment_id: int) -> Any:
    return _request("DELETE", f"/repos/{owner}/{repo}/pulls/comments/{comment_id}")


@mcp.tool()
def list_org_repositories(org: str, type: Optional[str] = None, sort: Optional[str] = None, direction: Optional[str] = None, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    return _request("GET", f"/orgs/{org}/repos", params=_clean({"type": type, "sort": sort, "direction": direction, "per_page": per_page, "page": page}))


@mcp.tool()
def get_repository(owner: str, repo: str) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}")


@mcp.tool()
def update_repository(owner: str, repo: str, name: Optional[str] = None, description: Optional[str] = None, homepage: Optional[str] = None, private: Optional[bool] = None, visibility: Optional[str] = None, has_issues: Optional[bool] = None, has_projects: Optional[bool] = None, has_wiki: Optional[bool] = None, is_template: Optional[bool] = None, default_branch: Optional[str] = None, allow_squash_merge: Optional[bool] = None, allow_merge_commit: Optional[bool] = None, allow_rebase_merge: Optional[bool] = None, allow_auto_merge: Optional[bool] = None, delete_branch_on_merge: Optional[bool] = None, archived: Optional[bool] = None) -> Any:
    payload = _clean({"name": name, "description": description, "homepage": homepage, "private": private, "visibility": visibility, "has_issues": has_issues, "has_projects": has_projects, "has_wiki": has_wiki, "is_template": is_template, "default_branch": default_branch, "allow_squash_merge": allow_squash_merge, "allow_merge_commit": allow_merge_commit, "allow_rebase_merge": allow_rebase_merge, "allow_auto_merge": allow_auto_merge, "delete_branch_on_merge": delete_branch_on_merge, "archived": archived})
    return _request("PATCH", f"/repos/{owner}/{repo}", json=payload)


@mcp.tool()
def delete_repository(owner: str, repo: str) -> Any:
    return _request("DELETE", f"/repos/{owner}/{repo}")


@mcp.tool()
def list_repository_contributors(owner: str, repo: str, anon: Optional[str] = None, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/contributors", params=_clean({"anon": anon, "per_page": per_page, "page": page}))


@mcp.tool()
def list_repository_languages(owner: str, repo: str) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/languages")


@mcp.tool()
def list_repository_tags(owner: str, repo: str, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/tags", params=_clean({"per_page": per_page, "page": page}))


@mcp.tool()
def create_repository_dispatch(owner: str, repo: str, event_type: str, client_payload: Optional[dict] = None) -> Any:
    return _request("POST", f"/repos/{owner}/{repo}/dispatches", json=_clean({"event_type": event_type, "client_payload": client_payload}))


@mcp.tool()
def get_repository_content(owner: str, repo: str, path: str, ref: Optional[str] = None, accept: str = "application/vnd.github.object+json") -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/contents/{path}", params=_clean({"ref": ref}), accept=accept)


@mcp.tool()
def create_or_update_file_contents(owner: str, repo: str, path: str, message: str, content: str, sha: Optional[str] = None, branch: Optional[str] = None, committer: Optional[dict] = None, author: Optional[dict] = None) -> Any:
    payload = _clean({"message": message, "content": content, "sha": sha, "branch": branch, "committer": committer, "author": author})
    return _request("PUT", f"/repos/{owner}/{repo}/contents/{path}", json=payload)


@mcp.tool()
def delete_file(owner: str, repo: str, path: str, message: str, sha: str, branch: Optional[str] = None, committer: Optional[dict] = None, author: Optional[dict] = None) -> Any:
    payload = _clean({"message": message, "sha": sha, "branch": branch, "committer": committer, "author": author})
    return _request("DELETE", f"/repos/{owner}/{repo}/contents/{path}", json=payload)


@mcp.tool()
def list_releases(owner: str, repo: str, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/releases", params=_clean({"per_page": per_page, "page": page}))


@mcp.tool()
def create_release(owner: str, repo: str, tag_name: str, target_commitish: Optional[str] = None, name: Optional[str] = None, body: Optional[str] = None, draft: Optional[bool] = None, prerelease: Optional[bool] = None, discussion_category_name: Optional[str] = None, generate_release_notes: Optional[bool] = None, make_latest: Optional[str] = None) -> Any:
    payload = _clean({"tag_name": tag_name, "target_commitish": target_commitish, "name": name, "body": body, "draft": draft, "prerelease": prerelease, "discussion_category_name": discussion_category_name, "generate_release_notes": generate_release_notes, "make_latest": make_latest})
    return _request("POST", f"/repos/{owner}/{repo}/releases", json=payload)


@mcp.tool()
def generate_release_notes(owner: str, repo: str, tag_name: str, target_commitish: Optional[str] = None, previous_tag_name: Optional[str] = None, configuration_file_path: Optional[str] = None) -> Any:
    payload = _clean({"tag_name": tag_name, "target_commitish": target_commitish, "previous_tag_name": previous_tag_name, "configuration_file_path": configuration_file_path})
    return _request("POST", f"/repos/{owner}/{repo}/releases/generate-notes", json=payload)


@mcp.tool()
def get_latest_release(owner: str, repo: str) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/releases/latest")


@mcp.tool()
def get_release_by_tag(owner: str, repo: str, tag: str) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/releases/tags/{tag}")


@mcp.tool()
def get_release(owner: str, repo: str, release_id: int) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/releases/{release_id}")


@mcp.tool()
def update_release(owner: str, repo: str, release_id: int, tag_name: Optional[str] = None, target_commitish: Optional[str] = None, name: Optional[str] = None, body: Optional[str] = None, draft: Optional[bool] = None, prerelease: Optional[bool] = None, discussion_category_name: Optional[str] = None, generate_release_notes: Optional[bool] = None, make_latest: Optional[str] = None) -> Any:
    payload = _clean({"tag_name": tag_name, "target_commitish": target_commitish, "name": name, "body": body, "draft": draft, "prerelease": prerelease, "discussion_category_name": discussion_category_name, "generate_release_notes": generate_release_notes, "make_latest": make_latest})
    return _request("PATCH", f"/repos/{owner}/{repo}/releases/{release_id}", json=payload)


@mcp.tool()
def delete_release(owner: str, repo: str, release_id: int) -> Any:
    return _request("DELETE", f"/repos/{owner}/{repo}/releases/{release_id}")


@mcp.tool()
def list_release_assets(owner: str, repo: str, release_id: int, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/releases/{release_id}/assets", params=_clean({"per_page": per_page, "page": page}))


@mcp.tool()
def get_release_asset(owner: str, repo: str, asset_id: int, accept: str = "application/vnd.github+json") -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/releases/assets/{asset_id}", accept=accept)


@mcp.tool()
def update_release_asset(owner: str, repo: str, asset_id: int, name: Optional[str] = None, label: Optional[str] = None, state: Optional[str] = None) -> Any:
    return _request("PATCH", f"/repos/{owner}/{repo}/releases/assets/{asset_id}", json=_clean({"name": name, "label": label, "state": state}))


@mcp.tool()
def delete_release_asset(owner: str, repo: str, asset_id: int) -> Any:
    return _request("DELETE", f"/repos/{owner}/{repo}/releases/assets/{asset_id}")


@mcp.tool()
def list_repository_workflows(owner: str, repo: str, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/actions/workflows", params=_clean({"per_page": per_page, "page": page}))


@mcp.tool()
def get_workflow(owner: str, repo: str, workflow_id: str) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")


@mcp.tool()
def disable_workflow(owner: str, repo: str, workflow_id: str) -> Any:
    return _request("PUT", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable")


@mcp.tool()
def create_workflow_dispatch(owner: str, repo: str, workflow_id: str, ref: str, inputs: Optional[dict] = None) -> Any:
    return _request("POST", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches", json=_clean({"ref": ref, "inputs": inputs}))


@mcp.tool()
def enable_workflow(owner: str, repo: str, workflow_id: str) -> Any:
    return _request("PUT", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable")


@mcp.tool()
def list_workflow_runs(owner: str, repo: str, actor: Optional[str] = None, branch: Optional[str] = None, event: Optional[str] = None, status: Optional[str] = None, per_page: Optional[int] = None, page: Optional[int] = None, created: Optional[str] = None, exclude_pull_requests: Optional[bool] = None, check_suite_id: Optional[int] = None, head_sha: Optional[str] = None) -> Any:
    params = _clean({"actor": actor, "branch": branch, "event": event, "status": status, "per_page": per_page, "page": page, "created": created, "exclude_pull_requests": exclude_pull_requests, "check_suite_id": check_suite_id, "head_sha": head_sha})
    return _request("GET", f"/repos/{owner}/{repo}/actions/runs", params=params)


@mcp.tool()
def get_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")


@mcp.tool()
def cancel_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    return _request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")


@mcp.tool()
def rerun_workflow(owner: str, repo: str, run_id: int, enable_debug_logging: Optional[bool] = None) -> Any:
    return _request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun", json=_clean({"enable_debug_logging": enable_debug_logging}))


@mcp.tool()
def rerun_workflow_job(owner: str, repo: str, job_id: int, enable_debug_logging: Optional[bool] = None) -> Any:
    return _request("POST", f"/repos/{owner}/{repo}/actions/jobs/{job_id}/rerun", json=_clean({"enable_debug_logging": enable_debug_logging}))


@mcp.tool()
def download_workflow_run_logs(owner: str, repo: str, run_id: int) -> Any:
    return _request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}/logs")


@mcp.tool()
def search_code(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    return _request("GET", "/search/code", params=_clean({"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page}))


@mcp.tool()
def search_commits(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    return _request("GET", "/search/commits", params=_clean({"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page}), accept="application/vnd.github+json")


@mcp.tool()
def search_issues_and_pull_requests(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    return _request("GET", "/search/issues", params=_clean({"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page}))


@mcp.tool()
def search_repositories(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    return _request("GET", "/search/repositories", params=_clean({"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page}))


@mcp.tool()
def search_users(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: Optional[int] = None, page: Optional[int] = None) -> Any:
    return _request("GET", "/search/users", params=_clean({"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page}))


if __name__ == "__main__":
    mcp.run()
