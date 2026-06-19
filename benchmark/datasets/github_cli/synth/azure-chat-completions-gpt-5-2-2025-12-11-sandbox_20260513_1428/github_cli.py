#!/usr/bin/env python3
"""GitHub REST API CLI.

Implements a curated set of GitHub REST API operations (no generic passthrough).
Auth via env:
  - GITHUB_TOKEN (required)
  - GITHUB_API_BASE_URL (default: https://api.github.com)
  - GITHUB_TEST_REPO (optional default owner/repo)

Headers:
  - Authorization: Bearer <token>
  - Accept: application/vnd.github+json
  - X-GitHub-Api-Version: 2022-11-28
"""

from __future__ import annotations

import base64
import json
import os
import sys
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import click
import requests

API_VERSION = "2022-11-28"
DEFAULT_BASE_URL = "https://api.github.com"


class GitHubCLIError(click.ClickException):
    pass


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.environ.get(name)
    return v if v not in (None, "") else default


def _require_env(name: str) -> str:
    v = _env(name)
    if not v:
        raise GitHubCLIError(f"Missing required environment variable: {name}")
    return v


def _split_repo(repo: Optional[str]) -> Tuple[str, str]:
    repo = repo or _env("GITHUB_TEST_REPO")
    if not repo or "/" not in repo:
        raise GitHubCLIError(
            "Repository must be provided as --repo OWNER/REPO or via GITHUB_TEST_REPO"
        )
    owner, name = repo.split("/", 1)
    if not owner or not name:
        raise GitHubCLIError("Invalid repo format; expected OWNER/REPO")
    return owner, name


@dataclass
class GitHubClient:
    token: str
    base_url: str = DEFAULT_BASE_URL

    def _headers(self, accept: str = "application/vnd.github+json") -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": accept,
            "X-GitHub-Api-Version": API_VERSION,
        }

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        accept: str = "application/vnd.github+json",
    ) -> Any:
        url = self.base_url.rstrip("/") + path
        resp = requests.request(
            method,
            url,
            headers=self._headers(accept=accept),
            params={k: v for k, v in (params or {}).items() if v is not None},
            json=json_body,
        )
        if resp.status_code >= 400:
            try:
                detail = resp.json()
            except Exception:
                detail = resp.text
            raise GitHubCLIError(f"HTTP {resp.status_code} {method} {path}: {detail}")

        if resp.status_code == 204:
            return None
        ctype = resp.headers.get("content-type", "")
        if "application/json" in ctype or ctype.endswith("+json"):
            return resp.json()
        return resp.text


def _client() -> GitHubClient:
    return GitHubClient(
        token=_require_env("GITHUB_TOKEN"),
        base_url=_env("GITHUB_API_BASE_URL", DEFAULT_BASE_URL) or DEFAULT_BASE_URL,
    )


def _echo(data: Any, *, pretty: bool = True) -> None:
    if isinstance(data, (dict, list)):
        click.echo(json.dumps(data, indent=2 if pretty else None, sort_keys=False))
    elif data is None:
        click.echo("")
    else:
        click.echo(str(data))


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli() -> None:
    """GitHub REST API CLI (curated commands)."""


@cli.group()
def issues() -> None:
    """Issue operations."""


@issues.command("list")
@click.option("--repo", help="OWNER/REPO")
@click.option("--state", type=click.Choice(["open", "closed", "all"]), default=None)
@click.option("--labels", default=None, help="Comma-separated labels")
@click.option("--since", default=None, help="ISO 8601 timestamp")
@click.option("--per-page", type=int, default=None)
@click.option("--page", type=int, default=None)
def issues_list(repo: Optional[str], state: Optional[str], labels: Optional[str], since: Optional[str], per_page: Optional[int], page: Optional[int]) -> None:
    """List repository issues."""
    owner, name = _split_repo(repo)
    data = _client().request(
        "GET",
        f"/repos/{owner}/{name}/issues",
        params={"state": state, "labels": labels, "since": since, "per_page": per_page, "page": page},
    )
    _echo(data)


@issues.command("get")
@click.option("--repo", help="OWNER/REPO")
@click.argument("number", type=int)
def issues_get(repo: Optional[str], number: int) -> None:
    """Get an issue."""
    owner, name = _split_repo(repo)
    data = _client().request("GET", f"/repos/{owner}/{name}/issues/{number}")
    _echo(data)


@issues.command("create")
@click.option("--repo", help="OWNER/REPO")
@click.option("--title", required=True)
@click.option("--body", default=None)
@click.option("--assignees", default=None, help="Comma-separated logins")
@click.option("--labels", default=None, help="Comma-separated labels")
def issues_create(repo: Optional[str], title: str, body: Optional[str], assignees: Optional[str], labels: Optional[str]) -> None:
    """Create an issue."""
    owner, name = _split_repo(repo)
    payload: Dict[str, Any] = {"title": title}
    if body is not None:
        payload["body"] = body
    if assignees:
        payload["assignees"] = [a for a in assignees.split(",") if a]
    if labels:
        payload["labels"] = [l for l in labels.split(",") if l]
    data = _client().request("POST", f"/repos/{owner}/{name}/issues", json_body=payload)
    _echo(data)


@issues.command("update")
@click.option("--repo", help="OWNER/REPO")
@click.argument("number", type=int)
@click.option("--title", default=None)
@click.option("--body", default=None)
@click.option("--state", type=click.Choice(["open", "closed"]), default=None)
@click.option("--labels", default=None, help="Comma-separated labels (replaces)")
def issues_update(repo: Optional[str], number: int, title: Optional[str], body: Optional[str], state: Optional[str], labels: Optional[str]) -> None:
    """Update an issue."""
    owner, name = _split_repo(repo)
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if state is not None:
        payload["state"] = state
    if labels is not None:
        payload["labels"] = [l for l in labels.split(",") if l]
    data = _client().request("PATCH", f"/repos/{owner}/{name}/issues/{number}", json_body=payload)
    _echo(data)


@issues.command("comment")
@click.option("--repo", help="OWNER/REPO")
@click.argument("number", type=int)
@click.option("--body", required=True)
def issues_comment(repo: Optional[str], number: int, body: str) -> None:
    """Add a comment to an issue."""
    owner, name = _split_repo(repo)
    data = _client().request(
        "POST",
        f"/repos/{owner}/{name}/issues/{number}/comments",
        json_body={"body": body},
    )
    _echo(data)


@issues.command("add-labels")
@click.option("--repo", help="OWNER/REPO")
@click.argument("number", type=int)
@click.option("--labels", required=True, help="Comma-separated labels")
def issues_add_labels(repo: Optional[str], number: int, labels: str) -> None:
    """Add labels to an issue."""
    owner, name = _split_repo(repo)
    data = _client().request(
        "POST",
        f"/repos/{owner}/{name}/issues/{number}/labels",
        json_body={"labels": [l for l in labels.split(",") if l]},
    )
    _echo(data)


@cli.group()
def pulls() -> None:
    """Pull request operations."""


@pulls.command("list")
@click.option("--repo", help="OWNER/REPO")
@click.option("--state", type=click.Choice(["open", "closed", "all"]), default=None)
@click.option("--base", default=None)
@click.option("--head", default=None)
@click.option("--per-page", type=int, default=None)
@click.option("--page", type=int, default=None)
def pulls_list(repo: Optional[str], state: Optional[str], base: Optional[str], head: Optional[str], per_page: Optional[int], page: Optional[int]) -> None:
    """List pull requests."""
    owner, name = _split_repo(repo)
    data = _client().request(
        "GET",
        f"/repos/{owner}/{name}/pulls",
        params={"state": state, "base": base, "head": head, "per_page": per_page, "page": page},
    )
    _echo(data)


@pulls.command("get")
@click.option("--repo", help="OWNER/REPO")
@click.argument("number", type=int)
def pulls_get(repo: Optional[str], number: int) -> None:
    """Get a pull request."""
    owner, name = _split_repo(repo)
    data = _client().request("GET", f"/repos/{owner}/{name}/pulls/{number}")
    _echo(data)


@pulls.command("create")
@click.option("--repo", help="OWNER/REPO")
@click.option("--title", required=True)
@click.option("--head", required=True, help="The name of the branch where changes are implemented")
@click.option("--base", required=True, help="The name of the branch you want the changes pulled into")
@click.option("--body", default=None)
@click.option("--draft", is_flag=True, default=False)
def pulls_create(repo: Optional[str], title: str, head: str, base: str, body: Optional[str], draft: bool) -> None:
    """Create a pull request."""
    owner, name = _split_repo(repo)
    payload: Dict[str, Any] = {"title": title, "head": head, "base": base, "draft": draft}
    if body is not None:
        payload["body"] = body
    data = _client().request("POST", f"/repos/{owner}/{name}/pulls", json_body=payload)
    _echo(data)


@pulls.command("merge")
@click.option("--repo", help="OWNER/REPO")
@click.argument("number", type=int)
@click.option("--commit-title", default=None)
@click.option("--commit-message", default=None)
@click.option("--merge-method", type=click.Choice(["merge", "squash", "rebase"]), default=None)
def pulls_merge(repo: Optional[str], number: int, commit_title: Optional[str], commit_message: Optional[str], merge_method: Optional[str]) -> None:
    """Merge a pull request."""
    owner, name = _split_repo(repo)
    payload: Dict[str, Any] = {}
    if commit_title is not None:
        payload["commit_title"] = commit_title
    if commit_message is not None:
        payload["commit_message"] = commit_message
    if merge_method is not None:
        payload["merge_method"] = merge_method
    data = _client().request("PUT", f"/repos/{owner}/{name}/pulls/{number}/merge", json_body=payload or None)
    _echo(data)


@cli.group()
def repos() -> None:
    """Repository operations."""


@repos.command("get")
@click.option("--repo", help="OWNER/REPO")
def repos_get(repo: Optional[str]) -> None:
    """Get repository details."""
    owner, name = _split_repo(repo)
    data = _client().request("GET", f"/repos/{owner}/{name}")
    _echo(data)


@repos.command("branches")
@click.option("--repo", help="OWNER/REPO")
@click.option("--per-page", type=int, default=None)
@click.option("--page", type=int, default=None)
def repos_branches(repo: Optional[str], per_page: Optional[int], page: Optional[int]) -> None:
    """List branches."""
    owner, name = _split_repo(repo)
    data = _client().request("GET", f"/repos/{owner}/{name}/branches", params={"per_page": per_page, "page": page})
    _echo(data)


@repos.command("commits")
@click.option("--repo", help="OWNER/REPO")
@click.option("--sha", default=None)
@click.option("--path", "path_", default=None)
@click.option("--author", default=None)
@click.option("--since", default=None)
@click.option("--until", default=None)
@click.option("--per-page", type=int, default=None)
@click.option("--page", type=int, default=None)
def repos_commits(repo: Optional[str], sha: Optional[str], path_: Optional[str], author: Optional[str], since: Optional[str], until: Optional[str], per_page: Optional[int], page: Optional[int]) -> None:
    """List commits."""
    owner, name = _split_repo(repo)
    data = _client().request(
        "GET",
        f"/repos/{owner}/{name}/commits",
        params={"sha": sha, "path": path_, "author": author, "since": since, "until": until, "per_page": per_page, "page": page},
    )
    _echo(data)


@repos.command("content-get")
@click.option("--repo", help="OWNER/REPO")
@click.option("--path", "path_", required=True, help="Path in repo")
@click.option("--ref", default=None)
@click.option("--raw", is_flag=True, default=False, help="Return raw content (Accept: application/vnd.github.raw)")
def repos_content_get(repo: Optional[str], path_: str, ref: Optional[str], raw: bool) -> None:
    """Get repository content (file or directory listing)."""
    owner, name = _split_repo(repo)
    accept = "application/vnd.github.raw" if raw else "application/vnd.github+json"
    data = _client().request(
        "GET",
        f"/repos/{owner}/{name}/contents/{path_.lstrip('/')}" ,
        params={"ref": ref},
        accept=accept,
    )
    _echo(data, pretty=not raw)


@repos.command("content-put")
@click.option("--repo", help="OWNER/REPO")
@click.option("--path", "path_", required=True)
@click.option("--message", required=True)
@click.option("--content", required=True, help="Raw file content (will be base64-encoded)")
@click.option("--branch", default=None)
@click.option("--sha", default=None, help="Required when updating an existing file")
def repos_content_put(repo: Optional[str], path_: str, message: str, content: str, branch: Optional[str], sha: Optional[str]) -> None:
    """Create or update file contents."""
    owner, name = _split_repo(repo)
    b64 = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    payload: Dict[str, Any] = {"message": message, "content": b64}
    if branch is not None:
        payload["branch"] = branch
    if sha is not None:
        payload["sha"] = sha
    data = _client().request(
        "PUT",
        f"/repos/{owner}/{name}/contents/{path_.lstrip('/')}" ,
        json_body=payload,
    )
    _echo(data)


@repos.command("content-delete")
@click.option("--repo", help="OWNER/REPO")
@click.option("--path", "path_", required=True)
@click.option("--message", required=True)
@click.option("--sha", required=True)
@click.option("--branch", default=None)
def repos_content_delete(repo: Optional[str], path_: str, message: str, sha: str, branch: Optional[str]) -> None:
    """Delete a file."""
    owner, name = _split_repo(repo)
    payload: Dict[str, Any] = {"message": message, "sha": sha}
    if branch is not None:
        payload["branch"] = branch
    data = _client().request(
        "DELETE",
        f"/repos/{owner}/{name}/contents/{path_.lstrip('/')}" ,
        json_body=payload,
    )
    _echo(data)


@cli.group()
def releases() -> None:
    """Release operations."""


@releases.command("list")
@click.option("--repo", help="OWNER/REPO")
@click.option("--per-page", type=int, default=None)
@click.option("--page", type=int, default=None)
def releases_list(repo: Optional[str], per_page: Optional[int], page: Optional[int]) -> None:
    """List releases."""
    owner, name = _split_repo(repo)
    data = _client().request("GET", f"/repos/{owner}/{name}/releases", params={"per_page": per_page, "page": page})
    _echo(data)


@releases.command("get")
@click.option("--repo", help="OWNER/REPO")
@click.argument("release_id", type=int)
def releases_get(repo: Optional[str], release_id: int) -> None:
    """Get a release by id."""
    owner, name = _split_repo(repo)
    data = _client().request("GET", f"/repos/{owner}/{name}/releases/{release_id}")
    _echo(data)


@releases.command("latest")
@click.option("--repo", help="OWNER/REPO")
def releases_latest(repo: Optional[str]) -> None:
    """Get the latest release."""
    owner, name = _split_repo(repo)
    data = _client().request("GET", f"/repos/{owner}/{name}/releases/latest")
    _echo(data)


@releases.command("create")
@click.option("--repo", help="OWNER/REPO")
@click.option("--tag", "tag_name", required=True)
@click.option("--target", "target_commitish", default=None)
@click.option("--name", "name_", default=None)
@click.option("--body", default=None)
@click.option("--draft", is_flag=True, default=False)
@click.option("--prerelease", is_flag=True, default=False)
@click.option("--generate-notes", is_flag=True, default=False)
@click.option("--make-latest", type=click.Choice(["true", "false", "legacy"]), default=None)
def releases_create(
    repo: Optional[str],
    tag_name: str,
    target_commitish: Optional[str],
    name_: Optional[str],
    body: Optional[str],
    draft: bool,
    prerelease: bool,
    generate_notes: bool,
    make_latest: Optional[str],
) -> None:
    """Create a release."""
    owner, name = _split_repo(repo)
    payload: Dict[str, Any] = {
        "tag_name": tag_name,
        "draft": draft,
        "prerelease": prerelease,
        "generate_release_notes": generate_notes,
    }
    if target_commitish is not None:
        payload["target_commitish"] = target_commitish
    if name_ is not None:
        payload["name"] = name_
    if body is not None:
        payload["body"] = body
    if make_latest is not None:
        payload["make_latest"] = make_latest
    data = _client().request("POST", f"/repos/{owner}/{name}/releases", json_body=payload)
    _echo(data)


@releases.command("generate-notes")
@click.option("--repo", help="OWNER/REPO")
@click.option("--tag", "tag_name", required=True)
@click.option("--target", "target_commitish", default=None)
@click.option("--previous-tag", default=None)
@click.option("--config-path", default=None)
def releases_generate_notes(
    repo: Optional[str],
    tag_name: str,
    target_commitish: Optional[str],
    previous_tag: Optional[str],
    config_path: Optional[str],
) -> None:
    """Generate release notes content (not saved)."""
    owner, name = _split_repo(repo)
    payload: Dict[str, Any] = {"tag_name": tag_name}
    if target_commitish is not None:
        payload["target_commitish"] = target_commitish
    if previous_tag is not None:
        payload["previous_tag_name"] = previous_tag
    if config_path is not None:
        payload["configuration_file_path"] = config_path
    data = _client().request(
        "POST",
        f"/repos/{owner}/{name}/releases/generate-notes",
        json_body=payload,
    )
    _echo(data)


@cli.group()
def actions() -> None:
    """GitHub Actions operations."""


@actions.command("runs")
@click.option("--repo", help="OWNER/REPO")
@click.option("--workflow-id", default=None, help="If provided, list runs for a workflow")
@click.option("--actor", default=None)
@click.option("--branch", default=None)
@click.option("--event", default=None)
@click.option("--status", default=None)
@click.option("--per-page", type=int, default=None)
@click.option("--page", type=int, default=None)
def actions_runs(repo: Optional[str], workflow_id: Optional[str], actor: Optional[str], branch: Optional[str], event: Optional[str], status: Optional[str], per_page: Optional[int], page: Optional[int]) -> None:
    """List workflow runs for a repository or workflow."""
    owner, name = _split_repo(repo)
    if workflow_id:
        path = f"/repos/{owner}/{name}/actions/workflows/{workflow_id}/runs"
    else:
        path = f"/repos/{owner}/{name}/actions/runs"
    data = _client().request(
        "GET",
        path,
        params={
            "actor": actor,
            "branch": branch,
            "event": event,
            "status": status,
            "per_page": per_page,
            "page": page,
        },
    )
    _echo(data)


@cli.group()
def search() -> None:
    """Search operations."""


@search.command("repos")
@click.option("--q", required=True, help="Search query")
@click.option("--sort", default=None)
@click.option("--order", type=click.Choice(["desc", "asc"]), default=None)
@click.option("--per-page", type=int, default=None)
@click.option("--page", type=int, default=None)
def search_repos(q: str, sort: Optional[str], order: Optional[str], per_page: Optional[int], page: Optional[int]) -> None:
    """Search repositories."""
    data = _client().request(
        "GET",
        "/search/repositories",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
    )
    _echo(data)


@search.command("code")
@click.option("--q", required=True, help="Search query")
@click.option("--sort", default=None)
@click.option("--order", type=click.Choice(["desc", "asc"]), default=None)
@click.option("--per-page", type=int, default=None)
@click.option("--page", type=int, default=None)
def search_code(q: str, sort: Optional[str], order: Optional[str], per_page: Optional[int], page: Optional[int]) -> None:
    """Search code."""
    data = _client().request(
        "GET",
        "/search/code",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
    )
    _echo(data)


@cli.group()
def gists() -> None:
    """Gist operations."""


@gists.command("list")
@click.option("--per-page", type=int, default=None)
@click.option("--page", type=int, default=None)
def gists_list(per_page: Optional[int], page: Optional[int]) -> None:
    """List gists for the authenticated user."""
    data = _client().request("GET", "/gists", params={"per_page": per_page, "page": page})
    _echo(data)


@gists.command("create")
@click.option("--description", default=None)
@click.option("--public", "public_", is_flag=True, default=False)
@click.option("--file", "files", multiple=True, required=True, help="FILEPATH=CONTENT (repeatable)")
def gists_create(description: Optional[str], public_: bool, files: Tuple[str, ...]) -> None:
    """Create a gist."""
    files_obj: Dict[str, Any] = {}
    for item in files:
        if "=" not in item:
            raise GitHubCLIError("--file must be in NAME=CONTENT format")
        name, content = item.split("=", 1)
        files_obj[name] = {"content": content}
    payload: Dict[str, Any] = {"public": public_, "files": files_obj}
    if description is not None:
        payload["description"] = description
    data = _client().request("POST", "/gists", json_body=payload)
    _echo(data)


@cli.group()
def users() -> None:
    """User operations."""


@users.command("me")
def users_me() -> None:
    """Get the authenticated user."""
    data = _client().request("GET", "/user")
    _echo(data)


@users.command("get")
@click.argument("username")
def users_get(username: str) -> None:
    """Get a user profile."""
    data = _client().request("GET", f"/users/{username}")
    _echo(data)


def main(argv: Optional[list[str]] = None) -> int:
    try:
        cli.main(args=argv, prog_name="github_cli", standalone_mode=False)
        return 0
    except click.ClickException as e:
        e.show()
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
