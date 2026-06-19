#!/usr/bin/env python3
"""Forgejo/Codeberg CLI

Auth via env:
  CODEBERG_TOKEN
  CODEBERG_BASE_URL (e.g. https://codeberg.org)
  CODEBERG_USERNAME (optional; used by some commands)

All commands map to specific Forgejo API operations (no generic passthrough).
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass
from typing import Any, Dict, Optional

import click
import requests


DEFAULT_BASE_URL = "https://codeberg.org"
API_PREFIX = "/api/v1"


class ForgejoError(click.ClickException):
    pass


@dataclass
class Client:
    base_url: str
    token: str

    def _url(self, path: str) -> str:
        if not path.startswith("/"):
            path = "/" + path
        return self.base_url.rstrip("/") + API_PREFIX + path

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Any = None,
    ) -> Any:
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/json",
        }
        url = self._url(path)
        resp = requests.request(method, url, headers=headers, params=params, json=json_body, timeout=60)
        if resp.status_code >= 400:
            msg = None
            try:
                msg = resp.json()
            except Exception:
                msg = resp.text
            raise ForgejoError(f"HTTP {resp.status_code} {method} {url}: {msg}")
        if resp.status_code == 204:
            return None
        ctype = resp.headers.get("content-type", "")
        if "application/json" in ctype:
            return resp.json()
        return resp.text


def _client_from_env() -> Client:
    token = os.environ.get("CODEBERG_TOKEN")
    if not token:
        raise ForgejoError("CODEBERG_TOKEN is required")
    base_url = os.environ.get("CODEBERG_BASE_URL", DEFAULT_BASE_URL)
    return Client(base_url=base_url, token=token)


def _echo(data: Any, *, pretty: bool) -> None:
    if data is None:
        return
    if isinstance(data, (dict, list)):
        click.echo(json.dumps(data, indent=2 if pretty else None, sort_keys=False))
    else:
        click.echo(str(data))


@click.group()
@click.option("--pretty/--no-pretty", default=True, help="Pretty-print JSON output")
@click.pass_context
def cli(ctx: click.Context, pretty: bool) -> None:
    ctx.ensure_object(dict)
    ctx.obj["client"] = _client_from_env()
    ctx.obj["pretty"] = pretty


@cli.group()
def user() -> None:
    """User operations."""


@user.command("me")
@click.pass_context
def user_me(ctx: click.Context) -> None:
    """Get the authenticated user's profile."""
    c: Client = ctx.obj["client"]
    data = c.request("GET", "/user")
    _echo(data, pretty=ctx.obj["pretty"])


@user.command("get")
@click.argument("username")
@click.pass_context
def user_get(ctx: click.Context, username: str) -> None:
    """Get a user by username."""
    c: Client = ctx.obj["client"]
    data = c.request("GET", f"/users/{username}")
    _echo(data, pretty=ctx.obj["pretty"])


@user.command("search")
@click.option("-q", "query", required=True)
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.pass_context
def user_search(ctx: click.Context, query: str, page: Optional[int], limit: Optional[int]) -> None:
    """Search users."""
    c: Client = ctx.obj["client"]
    params: Dict[str, Any] = {"q": query}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    data = c.request("GET", "/users/search", params=params)
    _echo(data, pretty=ctx.obj["pretty"])


@cli.group()
def org() -> None:
    """Organization operations."""


@org.command("list")
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.pass_context
def org_list(ctx: click.Context, page: Optional[int], limit: Optional[int]) -> None:
    """List organizations for the authenticated user."""
    c: Client = ctx.obj["client"]
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    data = c.request("GET", "/user/orgs", params=params or None)
    _echo(data, pretty=ctx.obj["pretty"])


@org.command("get")
@click.argument("orgname")
@click.pass_context
def org_get(ctx: click.Context, orgname: str) -> None:
    """Get an organization."""
    c: Client = ctx.obj["client"]
    data = c.request("GET", f"/orgs/{orgname}")
    _echo(data, pretty=ctx.obj["pretty"])


@cli.group()
def repo() -> None:
    """Repository operations."""


@repo.command("list")
@click.option("--username", help="List repos for this user (default: CODEBERG_USERNAME)")
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.pass_context
def repo_list(ctx: click.Context, username: Optional[str], page: Optional[int], limit: Optional[int]) -> None:
    """List repositories for a user."""
    c: Client = ctx.obj["client"]
    if not username:
        username = os.environ.get("CODEBERG_USERNAME")
    if not username:
        raise ForgejoError("--username or CODEBERG_USERNAME is required")
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    data = c.request("GET", f"/users/{username}/repos", params=params or None)
    _echo(data, pretty=ctx.obj["pretty"])


@repo.command("get")
@click.argument("owner")
@click.argument("reponame")
@click.pass_context
def repo_get(ctx: click.Context, owner: str, reponame: str) -> None:
    """Get a repository."""
    c: Client = ctx.obj["client"]
    data = c.request("GET", f"/repos/{owner}/{reponame}")
    _echo(data, pretty=ctx.obj["pretty"])


@repo.command("create")
@click.option("--name", required=True)
@click.option("--description")
@click.option("--private/--public", default=False)
@click.option("--auto-init/--no-auto-init", default=True)
@click.option("--default-branch")
@click.pass_context
def repo_create(ctx: click.Context, name: str, description: Optional[str], private: bool, auto_init: bool, default_branch: Optional[str]) -> None:
    """Create a repository for the authenticated user."""
    c: Client = ctx.obj["client"]
    body: Dict[str, Any] = {"name": name, "private": private, "auto_init": auto_init}
    if description is not None:
        body["description"] = description
    if default_branch is not None:
        body["default_branch"] = default_branch
    data = c.request("POST", "/user/repos", json_body=body)
    _echo(data, pretty=ctx.obj["pretty"])


@repo.command("delete")
@click.argument("owner")
@click.argument("reponame")
@click.pass_context
def repo_delete(ctx: click.Context, owner: str, reponame: str) -> None:
    """Delete a repository."""
    c: Client = ctx.obj["client"]
    data = c.request("DELETE", f"/repos/{owner}/{reponame}")
    _echo(data, pretty=ctx.obj["pretty"])


@repo.command("fork")
@click.argument("owner")
@click.argument("reponame")
@click.option("--organization", help="Fork into this organization")
@click.option("--name", help="New repo name")
@click.pass_context
def repo_fork(ctx: click.Context, owner: str, reponame: str, organization: Optional[str], name: Optional[str]) -> None:
    """Fork a repository."""
    c: Client = ctx.obj["client"]
    body: Dict[str, Any] = {}
    if organization:
        body["organization"] = organization
    if name:
        body["name"] = name
    data = c.request("POST", f"/repos/{owner}/{reponame}/forks", json_body=body or None)
    _echo(data, pretty=ctx.obj["pretty"])


@repo.command("search")
@click.option("-q", "query", required=True)
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.option("--topic", multiple=True, help="Filter by topic (repeatable)")
@click.pass_context
def repo_search(ctx: click.Context, query: str, page: Optional[int], limit: Optional[int], topic: tuple[str, ...]) -> None:
    """Search repositories."""
    c: Client = ctx.obj["client"]
    params: Dict[str, Any] = {"q": query}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if topic:
        params["topic"] = list(topic)
    data = c.request("GET", "/repos/search", params=params)
    _echo(data, pretty=ctx.obj["pretty"])


@cli.group()
def issue() -> None:
    """Issue operations."""


@issue.command("list")
@click.argument("owner")
@click.argument("reponame")
@click.option("--state", type=click.Choice(["open", "closed", "all"]))
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.pass_context
def issue_list(ctx: click.Context, owner: str, reponame: str, state: Optional[str], page: Optional[int], limit: Optional[int]) -> None:
    """List issues for a repository."""
    c: Client = ctx.obj["client"]
    params: Dict[str, Any] = {}
    if state:
        params["state"] = state
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    data = c.request("GET", f"/repos/{owner}/{reponame}/issues", params=params or None)
    _echo(data, pretty=ctx.obj["pretty"])


@issue.command("get")
@click.argument("owner")
@click.argument("reponame")
@click.argument("index", type=int)
@click.pass_context
def issue_get(ctx: click.Context, owner: str, reponame: str, index: int) -> None:
    """Get an issue by index."""
    c: Client = ctx.obj["client"]
    data = c.request("GET", f"/repos/{owner}/{reponame}/issues/{index}")
    _echo(data, pretty=ctx.obj["pretty"])


@issue.command("create")
@click.argument("owner")
@click.argument("reponame")
@click.option("--title", required=True)
@click.option("--body")
@click.option("--assignee")
@click.option("--milestone", type=int)
@click.option("--labels", help="Comma-separated label IDs")
@click.pass_context
def issue_create(ctx: click.Context, owner: str, reponame: str, title: str, body: Optional[str], assignee: Optional[str], milestone: Optional[int], labels: Optional[str]) -> None:
    """Create an issue."""
    c: Client = ctx.obj["client"]
    payload: Dict[str, Any] = {"title": title}
    if body is not None:
        payload["body"] = body
    if assignee is not None:
        payload["assignee"] = assignee
    if milestone is not None:
        payload["milestone"] = milestone
    if labels:
        payload["labels"] = [int(x) for x in labels.split(",") if x.strip()]
    data = c.request("POST", f"/repos/{owner}/{reponame}/issues", json_body=payload)
    _echo(data, pretty=ctx.obj["pretty"])


@issue.command("update")
@click.argument("owner")
@click.argument("reponame")
@click.argument("index", type=int)
@click.option("--title")
@click.option("--body")
@click.option("--state", type=click.Choice(["open", "closed"]))
@click.option("--assignee")
@click.pass_context
def issue_update(ctx: click.Context, owner: str, reponame: str, index: int, title: Optional[str], body: Optional[str], state: Optional[str], assignee: Optional[str]) -> None:
    """Update an issue."""
    c: Client = ctx.obj["client"]
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if state is not None:
        payload["state"] = state
    if assignee is not None:
        payload["assignee"] = assignee
    data = c.request("PATCH", f"/repos/{owner}/{reponame}/issues/{index}", json_body=payload)
    _echo(data, pretty=ctx.obj["pretty"])


@issue.command("comment")
@click.argument("owner")
@click.argument("reponame")
@click.argument("index", type=int)
@click.option("--body", required=True)
@click.pass_context
def issue_comment(ctx: click.Context, owner: str, reponame: str, index: int, body: str) -> None:
    """Add a comment to an issue."""
    c: Client = ctx.obj["client"]
    data = c.request("POST", f"/repos/{owner}/{reponame}/issues/{index}/comments", json_body={"body": body})
    _echo(data, pretty=ctx.obj["pretty"])


@issue.command("labels")
@click.argument("owner")
@click.argument("reponame")
@click.argument("index", type=int)
@click.option("--labels", required=True, help="Comma-separated label IDs")
@click.pass_context
def issue_add_labels(ctx: click.Context, owner: str, reponame: str, index: int, labels: str) -> None:
    """Add labels to an issue."""
    c: Client = ctx.obj["client"]
    label_ids = [int(x) for x in labels.split(",") if x.strip()]
    data = c.request("POST", f"/repos/{owner}/{reponame}/issues/{index}/labels", json_body=label_ids)
    _echo(data, pretty=ctx.obj["pretty"])


@cli.group()
def pr() -> None:
    """Pull request operations."""


@pr.command("list")
@click.argument("owner")
@click.argument("reponame")
@click.option("--state", type=click.Choice(["open", "closed", "all"]))
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.pass_context
def pr_list(ctx: click.Context, owner: str, reponame: str, state: Optional[str], page: Optional[int], limit: Optional[int]) -> None:
    """List pull requests for a repository."""
    c: Client = ctx.obj["client"]
    params: Dict[str, Any] = {}
    if state:
        params["state"] = state
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    data = c.request("GET", f"/repos/{owner}/{reponame}/pulls", params=params or None)
    _echo(data, pretty=ctx.obj["pretty"])


@pr.command("get")
@click.argument("owner")
@click.argument("reponame")
@click.argument("index", type=int)
@click.pass_context
def pr_get(ctx: click.Context, owner: str, reponame: str, index: int) -> None:
    """Get a pull request by index."""
    c: Client = ctx.obj["client"]
    data = c.request("GET", f"/repos/{owner}/{reponame}/pulls/{index}")
    _echo(data, pretty=ctx.obj["pretty"])


@pr.command("create")
@click.argument("owner")
@click.argument("reponame")
@click.option("--title", required=True)
@click.option("--head", required=True, help="Branch name in the form 'user:branch' or 'branch'")
@click.option("--base", required=True, help="Base branch")
@click.option("--body")
@click.option("--draft/--no-draft", default=False)
@click.pass_context
def pr_create(ctx: click.Context, owner: str, reponame: str, title: str, head: str, base: str, body: Optional[str], draft: bool) -> None:
    """Create a pull request."""
    c: Client = ctx.obj["client"]
    payload: Dict[str, Any] = {"title": title, "head": head, "base": base, "draft": draft}
    if body is not None:
        payload["body"] = body
    data = c.request("POST", f"/repos/{owner}/{reponame}/pulls", json_body=payload)
    _echo(data, pretty=ctx.obj["pretty"])


@cli.group()
def branch() -> None:
    """Branch operations."""


@branch.command("list")
@click.argument("owner")
@click.argument("reponame")
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.pass_context
def branch_list(ctx: click.Context, owner: str, reponame: str, page: Optional[int], limit: Optional[int]) -> None:
    """List branches."""
    c: Client = ctx.obj["client"]
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    data = c.request("GET", f"/repos/{owner}/{reponame}/branches", params=params or None)
    _echo(data, pretty=ctx.obj["pretty"])


@branch.command("get")
@click.argument("owner")
@click.argument("reponame")
@click.argument("branch")
@click.pass_context
def branch_get(ctx: click.Context, owner: str, reponame: str, branch: str) -> None:
    """Get a branch."""
    c: Client = ctx.obj["client"]
    data = c.request("GET", f"/repos/{owner}/{reponame}/branches/{branch}")
    _echo(data, pretty=ctx.obj["pretty"])


@branch.command("create")
@click.argument("owner")
@click.argument("reponame")
@click.option("--new", "new_branch", required=True, help="New branch name")
@click.option("--old", "old_branch", required=True, help="Existing branch name")
@click.pass_context
def branch_create(ctx: click.Context, owner: str, reponame: str, new_branch: str, old_branch: str) -> None:
    """Create a branch from an existing branch."""
    c: Client = ctx.obj["client"]
    payload = {"new_branch_name": new_branch, "old_branch_name": old_branch}
    data = c.request("POST", f"/repos/{owner}/{reponame}/branches", json_body=payload)
    _echo(data, pretty=ctx.obj["pretty"])


@cli.group()
def release() -> None:
    """Release operations."""


@release.command("list")
@click.argument("owner")
@click.argument("reponame")
@click.option("--page", type=int)
@click.option("--limit", type=int)
@click.pass_context
def release_list(ctx: click.Context, owner: str, reponame: str, page: Optional[int], limit: Optional[int]) -> None:
    """List releases."""
    c: Client = ctx.obj["client"]
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    data = c.request("GET", f"/repos/{owner}/{reponame}/releases", params=params or None)
    _echo(data, pretty=ctx.obj["pretty"])


@release.command("get")
@click.argument("owner")
@click.argument("reponame")
@click.argument("id", type=int)
@click.pass_context
def release_get(ctx: click.Context, owner: str, reponame: str, id: int) -> None:
    """Get a release by ID."""
    c: Client = ctx.obj["client"]
    data = c.request("GET", f"/repos/{owner}/{reponame}/releases/{id}")
    _echo(data, pretty=ctx.obj["pretty"])


@release.command("create")
@click.argument("owner")
@click.argument("reponame")
@click.option("--tag", required=True)
@click.option("--name")
@click.option("--body")
@click.option("--draft/--no-draft", default=False)
@click.option("--prerelease/--no-prerelease", default=False)
@click.option("--target-commitish")
@click.pass_context
def release_create(
    ctx: click.Context,
    owner: str,
    reponame: str,
    tag: str,
    name: Optional[str],
    body: Optional[str],
    draft: bool,
    prerelease: bool,
    target_commitish: Optional[str],
) -> None:
    """Create a release."""
    c: Client = ctx.obj["client"]
    payload: Dict[str, Any] = {"tag_name": tag, "draft": draft, "prerelease": prerelease}
    if name is not None:
        payload["name"] = name
    if body is not None:
        payload["body"] = body
    if target_commitish is not None:
        payload["target_commitish"] = target_commitish
    data = c.request("POST", f"/repos/{owner}/{reponame}/releases", json_body=payload)
    _echo(data, pretty=ctx.obj["pretty"])


def main(argv: Optional[list[str]] = None) -> int:
    try:
        cli.main(args=argv, prog_name="forgejo-cli", standalone_mode=False)
        return 0
    except click.ClickException as e:
        e.show()
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
