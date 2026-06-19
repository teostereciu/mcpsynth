#!/usr/bin/env python3
"""GitHub REST API CLI.

Auth:
  - GITHUB_TOKEN (required)
  - GITHUB_API_BASE_URL (optional, default https://api.github.com)

All requests send:
  - Authorization: Bearer $GITHUB_TOKEN
  - Accept: application/vnd.github+json
  - X-GitHub-Api-Version: 2022-11-28

No generic passthrough commands are exposed; each subcommand maps to a named operation.
"""

from __future__ import annotations

import base64
import json
import os
import sys
from dataclasses import dataclass
from typing import Any, Dict, Optional

import click
import requests


DEFAULT_API_VERSION = "2022-11-28"
DEFAULT_BASE_URL = "https://api.github.com"


class GitHubAPIError(click.ClickException):
    pass


@dataclass
class GitHubClient:
    base_url: str
    token: str
    api_version: str = DEFAULT_API_VERSION
    timeout: int = 60

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        h = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": self.api_version,
        }
        if extra:
            h.update(extra)
        return h

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        url = self.base_url.rstrip("/") + path
        resp = requests.request(
            method,
            url,
            headers=self._headers(headers),
            params={k: v for k, v in (params or {}).items() if v is not None},
            json=json_body,
            timeout=self.timeout,
        )
        if resp.status_code >= 400:
            msg = None
            try:
                msg = resp.json().get("message")
            except Exception:
                msg = resp.text
            raise GitHubAPIError(f"{resp.status_code} {method} {path}: {msg}")

        if resp.status_code == 204:
            return None
        ctype = resp.headers.get("content-type", "")
        if "application/json" in ctype:
            return resp.json()
        return resp.text


def _get_client(ctx: click.Context) -> GitHubClient:
    token = ctx.obj["token"]
    base_url = ctx.obj["base_url"]
    api_version = ctx.obj["api_version"]
    return GitHubClient(base_url=base_url, token=token, api_version=api_version)


def _print(data: Any, *, pretty: bool) -> None:
    if data is None:
        return
    if isinstance(data, (dict, list)):
        click.echo(json.dumps(data, indent=2 if pretty else None, sort_keys=False))
    else:
        click.echo(str(data))


def _split_repo(repo: str) -> tuple[str, str]:
    if "/" not in repo:
        raise click.ClickException("--repo must be in owner/repo format")
    owner, name = repo.split("/", 1)
    if not owner or not name:
        raise click.ClickException("--repo must be in owner/repo format")
    return owner, name


@click.group()
@click.option("--base-url", envvar="GITHUB_API_BASE_URL", default=DEFAULT_BASE_URL, show_default=True)
@click.option("--token", envvar="GITHUB_TOKEN", required=True)
@click.option("--api-version", default=DEFAULT_API_VERSION, show_default=True)
@click.option("--pretty/--no-pretty", default=True, show_default=True)
@click.pass_context
def cli(ctx: click.Context, base_url: str, token: str, api_version: str, pretty: bool) -> None:
    ctx.obj = {"base_url": base_url, "token": token, "api_version": api_version, "pretty": pretty}


# -------------------- Users domain --------------------


@cli.group("users")
def users_group() -> None:
    """User-related operations."""


@users_group.command("me")
@click.pass_context
def users_me(ctx: click.Context) -> None:
    """Get the authenticated user (GET /user)."""
    gh = _get_client(ctx)
    data = gh.request("GET", "/user")
    _print(data, pretty=ctx.obj["pretty"])


@users_group.command("get")
@click.argument("username")
@click.pass_context
def users_get(ctx: click.Context, username: str) -> None:
    """Get a user profile (GET /users/{username})."""
    gh = _get_client(ctx)
    data = gh.request("GET", f"/users/{username}")
    _print(data, pretty=ctx.obj["pretty"])


# -------------------- Issues domain --------------------


@cli.group("issues")
def issues_group() -> None:
    """Issue operations."""


@issues_group.command("list")
@click.option("--filter", "filter_", type=click.Choice(["assigned", "created", "mentioned", "subscribed", "repos", "all"]))
@click.option("--state", type=click.Choice(["open", "closed", "all"]))
@click.option("--labels")
@click.option("--sort", type=click.Choice(["created", "updated", "comments"]))
@click.option("--direction", type=click.Choice(["asc", "desc"]))
@click.option("--since")
@click.option("--per-page", type=int)
@click.option("--page", type=int)
@click.pass_context
def issues_list(ctx: click.Context, filter_: str | None, state: str | None, labels: str | None, sort: str | None, direction: str | None, since: str | None, per_page: int | None, page: int | None) -> None:
    """List issues assigned to the authenticated user (GET /issues)."""
    gh = _get_client(ctx)
    params = {
        "filter": filter_,
        "state": state,
        "labels": labels,
        "sort": sort,
        "direction": direction,
        "since": since,
        "per_page": per_page,
        "page": page,
    }
    data = gh.request("GET", "/issues", params=params)
    _print(data, pretty=ctx.obj["pretty"])


@issues_group.command("list-repo")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.option("--state", type=click.Choice(["open", "closed", "all"]))
@click.option("--labels")
@click.option("--sort", type=click.Choice(["created", "updated", "comments"]))
@click.option("--direction", type=click.Choice(["asc", "desc"]))
@click.option("--since")
@click.option("--per-page", type=int)
@click.option("--page", type=int)
@click.pass_context
def issues_list_repo(ctx: click.Context, repo: str, state: str | None, labels: str | None, sort: str | None, direction: str | None, since: str | None, per_page: int | None, page: int | None) -> None:
    """List repository issues (GET /repos/{owner}/{repo}/issues)."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    params = {
        "state": state,
        "labels": labels,
        "sort": sort,
        "direction": direction,
        "since": since,
        "per_page": per_page,
        "page": page,
    }
    data = gh.request("GET", f"/repos/{owner}/{name}/issues", params=params)
    _print(data, pretty=ctx.obj["pretty"])


@issues_group.command("get")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.argument("issue_number", type=int)
@click.pass_context
def issues_get(ctx: click.Context, repo: str, issue_number: int) -> None:
    """Get an issue (GET /repos/{owner}/{repo}/issues/{issue_number})."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    data = gh.request("GET", f"/repos/{owner}/{name}/issues/{issue_number}")
    _print(data, pretty=ctx.obj["pretty"])


@issues_group.command("create")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.option("--title", required=True)
@click.option("--body")
@click.option("--assignees", help="Comma-separated list")
@click.option("--labels", help="Comma-separated list")
@click.option("--milestone", type=int)
@click.pass_context
def issues_create(ctx: click.Context, repo: str, title: str, body: str | None, assignees: str | None, labels: str | None, milestone: int | None) -> None:
    """Create an issue (POST /repos/{owner}/{repo}/issues)."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    payload: Dict[str, Any] = {"title": title}
    if body is not None:
        payload["body"] = body
    if assignees:
        payload["assignees"] = [a.strip() for a in assignees.split(",") if a.strip()]
    if labels:
        payload["labels"] = [l.strip() for l in labels.split(",") if l.strip()]
    if milestone is not None:
        payload["milestone"] = milestone
    data = gh.request("POST", f"/repos/{owner}/{name}/issues", json_body=payload)
    _print(data, pretty=ctx.obj["pretty"])


@issues_group.command("update")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.argument("issue_number", type=int)
@click.option("--title")
@click.option("--body")
@click.option("--state", type=click.Choice(["open", "closed"]))
@click.option("--assignees", help="Comma-separated list")
@click.option("--labels", help="Comma-separated list")
@click.option("--milestone", type=int)
@click.pass_context
def issues_update(ctx: click.Context, repo: str, issue_number: int, title: str | None, body: str | None, state: str | None, assignees: str | None, labels: str | None, milestone: int | None) -> None:
    """Update an issue (PATCH /repos/{owner}/{repo}/issues/{issue_number})."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if state is not None:
        payload["state"] = state
    if assignees is not None:
        payload["assignees"] = [a.strip() for a in assignees.split(",") if a.strip()]
    if labels is not None:
        payload["labels"] = [l.strip() for l in labels.split(",") if l.strip()]
    if milestone is not None:
        payload["milestone"] = milestone
    data = gh.request("PATCH", f"/repos/{owner}/{name}/issues/{issue_number}", json_body=payload)
    _print(data, pretty=ctx.obj["pretty"])


@issues_group.command("comment")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.argument("issue_number", type=int)
@click.option("--body", required=True, help="Comment body")
@click.pass_context
def issues_comment(ctx: click.Context, repo: str, issue_number: int, body: str) -> None:
    """Create an issue comment (POST /repos/{owner}/{repo}/issues/{issue_number}/comments)."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    data = gh.request(
        "POST",
        f"/repos/{owner}/{name}/issues/{issue_number}/comments",
        json_body={"body": body},
    )
    _print(data, pretty=ctx.obj["pretty"])


@issues_group.command("labels-add")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.argument("issue_number", type=int)
@click.option("--labels", required=True, help="Comma-separated label names")
@click.pass_context
def issues_labels_add(ctx: click.Context, repo: str, issue_number: int, labels: str) -> None:
    """Add labels to an issue (POST /repos/{owner}/{repo}/issues/{issue_number}/labels)."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    label_list = [l.strip() for l in labels.split(",") if l.strip()]
    data = gh.request(
        "POST",
        f"/repos/{owner}/{name}/issues/{issue_number}/labels",
        json_body={"labels": label_list},
    )
    _print(data, pretty=ctx.obj["pretty"])


@issues_group.command("labels-set")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.argument("issue_number", type=int)
@click.option("--labels", required=True, help="Comma-separated label names (empty string to clear)")
@click.pass_context
def issues_labels_set(ctx: click.Context, repo: str, issue_number: int, labels: str) -> None:
    """Set labels for an issue (PUT /repos/{owner}/{repo}/issues/{issue_number}/labels)."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    label_list = [l.strip() for l in labels.split(",") if l.strip()]
    data = gh.request(
        "PUT",
        f"/repos/{owner}/{name}/issues/{issue_number}/labels",
        json_body={"labels": label_list},
    )
    _print(data, pretty=ctx.obj["pretty"])


# -------------------- Repos domain --------------------


@cli.group("repos")
def repos_group() -> None:
    """Repository operations."""


@repos_group.command("get")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.pass_context
def repos_get(ctx: click.Context, repo: str) -> None:
    """Get a repository (GET /repos/{owner}/{repo})."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    data = gh.request("GET", f"/repos/{owner}/{name}")
    _print(data, pretty=ctx.obj["pretty"])


@repos_group.command("branches")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.option("--per-page", type=int)
@click.option("--page", type=int)
@click.pass_context
def repos_branches(ctx: click.Context, repo: str, per_page: int | None, page: int | None) -> None:
    """List branches (GET /repos/{owner}/{repo}/branches)."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    data = gh.request("GET", f"/repos/{owner}/{name}/branches", params={"per_page": per_page, "page": page})
    _print(data, pretty=ctx.obj["pretty"])


@repos_group.command("commits")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.option("--sha", help="Branch name or commit SHA")
@click.option("--path")
@click.option("--author")
@click.option("--since")
@click.option("--until")
@click.option("--per-page", type=int)
@click.option("--page", type=int)
@click.pass_context
def repos_commits(ctx: click.Context, repo: str, sha: str | None, path: str | None, author: str | None, since: str | None, until: str | None, per_page: int | None, page: int | None) -> None:
    """List commits (GET /repos/{owner}/{repo}/commits)."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    params = {"sha": sha, "path": path, "author": author, "since": since, "until": until, "per_page": per_page, "page": page}
    data = gh.request("GET", f"/repos/{owner}/{name}/commits", params=params)
    _print(data, pretty=ctx.obj["pretty"])


@repos_group.command("content-get")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.option("--path", required=True, help="Path in repo")
@click.option("--ref", help="Branch, tag, or commit")
@click.pass_context
def repos_content_get(ctx: click.Context, repo: str, path: str, ref: str | None) -> None:
    """Get repository content (GET /repos/{owner}/{repo}/contents/{path})."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    data = gh.request("GET", f"/repos/{owner}/{name}/contents/{path}", params={"ref": ref})
    _print(data, pretty=ctx.obj["pretty"])


@repos_group.command("content-put")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.option("--path", required=True, help="Path in repo")
@click.option("--message", required=True, help="Commit message")
@click.option("--content", required=True, help="Raw content string (will be base64-encoded)")
@click.option("--branch")
@click.option("--sha", help="Required when updating an existing file")
@click.option("--committer-name")
@click.option("--committer-email")
@click.pass_context
def repos_content_put(
    ctx: click.Context,
    repo: str,
    path: str,
    message: str,
    content: str,
    branch: str | None,
    sha: str | None,
    committer_name: str | None,
    committer_email: str | None,
) -> None:
    """Create or update file contents (PUT /repos/{owner}/{repo}/contents/{path})."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    payload: Dict[str, Any] = {
        "message": message,
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
    }
    if branch is not None:
        payload["branch"] = branch
    if sha is not None:
        payload["sha"] = sha
    if committer_name or committer_email:
        payload["committer"] = {"name": committer_name, "email": committer_email}
    data = gh.request("PUT", f"/repos/{owner}/{name}/contents/{path}", json_body=payload)
    _print(data, pretty=ctx.obj["pretty"])


# -------------------- Pull requests domain --------------------


@cli.group("pulls")
def pulls_group() -> None:
    """Pull request operations."""


@pulls_group.command("list")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.option("--state", type=click.Choice(["open", "closed", "all"]))
@click.option("--head")
@click.option("--base")
@click.option("--sort", type=click.Choice(["created", "updated", "popularity", "long-running"]))
@click.option("--direction", type=click.Choice(["asc", "desc"]))
@click.option("--per-page", type=int)
@click.option("--page", type=int)
@click.pass_context
def pulls_list(ctx: click.Context, repo: str, state: str | None, head: str | None, base: str | None, sort: str | None, direction: str | None, per_page: int | None, page: int | None) -> None:
    """List pull requests (GET /repos/{owner}/{repo}/pulls)."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    params = {"state": state, "head": head, "base": base, "sort": sort, "direction": direction, "per_page": per_page, "page": page}
    data = gh.request("GET", f"/repos/{owner}/{name}/pulls", params=params)
    _print(data, pretty=ctx.obj["pretty"])


@pulls_group.command("get")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.argument("pull_number", type=int)
@click.pass_context
def pulls_get(ctx: click.Context, repo: str, pull_number: int) -> None:
    """Get a pull request (GET /repos/{owner}/{repo}/pulls/{pull_number})."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    data = gh.request("GET", f"/repos/{owner}/{name}/pulls/{pull_number}")
    _print(data, pretty=ctx.obj["pretty"])


@pulls_group.command("create")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.option("--title", required=True)
@click.option("--head", required=True, help="The name of the branch where your changes are implemented")
@click.option("--base", required=True, help="The name of the branch you want the changes pulled into")
@click.option("--body")
@click.option("--draft/--no-draft", default=False, show_default=True)
@click.pass_context
def pulls_create(ctx: click.Context, repo: str, title: str, head: str, base: str, body: str | None, draft: bool) -> None:
    """Create a pull request (POST /repos/{owner}/{repo}/pulls)."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    payload: Dict[str, Any] = {"title": title, "head": head, "base": base, "draft": draft}
    if body is not None:
        payload["body"] = body
    data = gh.request("POST", f"/repos/{owner}/{name}/pulls", json_body=payload)
    _print(data, pretty=ctx.obj["pretty"])


@pulls_group.command("merge")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.argument("pull_number", type=int)
@click.option("--commit-title")
@click.option("--commit-message")
@click.option("--merge-method", type=click.Choice(["merge", "squash", "rebase"]))
@click.option("--sha", help="Expected head SHA")
@click.pass_context
def pulls_merge(ctx: click.Context, repo: str, pull_number: int, commit_title: str | None, commit_message: str | None, merge_method: str | None, sha: str | None) -> None:
    """Merge a pull request (PUT /repos/{owner}/{repo}/pulls/{pull_number}/merge)."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    payload: Dict[str, Any] = {}
    if commit_title is not None:
        payload["commit_title"] = commit_title
    if commit_message is not None:
        payload["commit_message"] = commit_message
    if merge_method is not None:
        payload["merge_method"] = merge_method
    if sha is not None:
        payload["sha"] = sha
    data = gh.request("PUT", f"/repos/{owner}/{name}/pulls/{pull_number}/merge", json_body=payload)
    _print(data, pretty=ctx.obj["pretty"])


# -------------------- Releases domain --------------------


@cli.group("releases")
def releases_group() -> None:
    """Release operations."""


@releases_group.command("list")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.option("--per-page", type=int)
@click.option("--page", type=int)
@click.pass_context
def releases_list(ctx: click.Context, repo: str, per_page: int | None, page: int | None) -> None:
    """List releases (GET /repos/{owner}/{repo}/releases)."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    data = gh.request("GET", f"/repos/{owner}/{name}/releases", params={"per_page": per_page, "page": page})
    _print(data, pretty=ctx.obj["pretty"])


@releases_group.command("get")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.argument("release_id", type=int)
@click.pass_context
def releases_get(ctx: click.Context, repo: str, release_id: int) -> None:
    """Get a release (GET /repos/{owner}/{repo}/releases/{release_id})."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    data = gh.request("GET", f"/repos/{owner}/{name}/releases/{release_id}")
    _print(data, pretty=ctx.obj["pretty"])


# -------------------- Actions domain --------------------


@cli.group("actions")
def actions_group() -> None:
    """GitHub Actions operations."""


@actions_group.command("runs")
@click.option("--repo", envvar="GITHUB_TEST_REPO", required=True, help="owner/repo")
@click.option("--branch")
@click.option("--status")
@click.option("--event")
@click.option("--per-page", type=int)
@click.option("--page", type=int)
@click.pass_context
def actions_runs(ctx: click.Context, repo: str, branch: str | None, status: str | None, event: str | None, per_page: int | None, page: int | None) -> None:
    """List workflow runs for a repository (GET /repos/{owner}/{repo}/actions/runs)."""
    owner, name = _split_repo(repo)
    gh = _get_client(ctx)
    params = {"branch": branch, "status": status, "event": event, "per_page": per_page, "page": page}
    data = gh.request("GET", f"/repos/{owner}/{name}/actions/runs", params=params)
    _print(data, pretty=ctx.obj["pretty"])


# -------------------- Search domain --------------------


@cli.group("search")
def search_group() -> None:
    """Search operations."""


@search_group.command("repos")
@click.option("--q", required=True, help="Search query")
@click.option("--sort", type=click.Choice(["stars", "forks", "help-wanted-issues", "updated"]))
@click.option("--order", type=click.Choice(["desc", "asc"]))
@click.option("--per-page", type=int)
@click.option("--page", type=int)
@click.pass_context
def search_repos(ctx: click.Context, q: str, sort: str | None, order: str | None, per_page: int | None, page: int | None) -> None:
    """Search repositories (GET /search/repositories)."""
    gh = _get_client(ctx)
    params = {"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page}
    data = gh.request("GET", "/search/repositories", params=params)
    _print(data, pretty=ctx.obj["pretty"])


@search_group.command("code")
@click.option("--q", required=True, help="Search query")
@click.option("--sort", type=click.Choice(["indexed"]))
@click.option("--order", type=click.Choice(["desc", "asc"]))
@click.option("--per-page", type=int)
@click.option("--page", type=int)
@click.pass_context
def search_code(ctx: click.Context, q: str, sort: str | None, order: str | None, per_page: int | None, page: int | None) -> None:
    """Search code (GET /search/code)."""
    gh = _get_client(ctx)
    params = {"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page}
    data = gh.request("GET", "/search/code", params=params)
    _print(data, pretty=ctx.obj["pretty"])


# -------------------- Gists domain --------------------


@cli.group("gists")
def gists_group() -> None:
    """Gist operations."""


@gists_group.command("list")
@click.option("--since")
@click.option("--per-page", type=int)
@click.option("--page", type=int)
@click.pass_context
def gists_list(ctx: click.Context, since: str | None, per_page: int | None, page: int | None) -> None:
    """List gists for the authenticated user (GET /gists)."""
    gh = _get_client(ctx)
    params = {"since": since, "per_page": per_page, "page": page}
    data = gh.request("GET", "/gists", params=params)
    _print(data, pretty=ctx.obj["pretty"])


@gists_group.command("create")
@click.option("--description")
@click.option("--public/--secret", default=False, show_default=True)
@click.option("--file", "files", multiple=True, required=True, help="Repeatable: name=content")
@click.pass_context
def gists_create(ctx: click.Context, description: str | None, public: bool, files: tuple[str, ...]) -> None:
    """Create a gist (POST /gists)."""
    gh = _get_client(ctx)
    files_obj: Dict[str, Dict[str, str]] = {}
    for item in files:
        if "=" not in item:
            raise click.ClickException("--file must be in name=content format")
        name, content = item.split("=", 1)
        name = name.strip()
        if not name:
            raise click.ClickException("--file name cannot be empty")
        files_obj[name] = {"content": content}

    payload: Dict[str, Any] = {"public": public, "files": files_obj}
    if description is not None:
        payload["description"] = description

    data = gh.request("POST", "/gists", json_body=payload)
    _print(data, pretty=ctx.obj["pretty"])


def main(argv: Optional[list[str]] = None) -> int:
    try:
        cli.main(args=argv, prog_name="github-cli", standalone_mode=False)
        return 0
    except click.ClickException as e:
        e.show()
        return 2
    except GitHubAPIError as e:
        e.show()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
