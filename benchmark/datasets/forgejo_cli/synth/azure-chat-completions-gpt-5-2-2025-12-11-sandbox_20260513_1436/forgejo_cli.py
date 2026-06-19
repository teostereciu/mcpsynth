#!/usr/bin/env python3
"""Forgejo/Codeberg CLI

Implements a curated set of Forgejo REST API operations (no generic passthrough).
Auth via env:
  CODEBERG_BASE_URL (e.g. https://codeberg.org)
  CODEBERG_TOKEN
  CODEBERG_USERNAME (optional; used by some defaults)
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


@dataclass
class Client:
    base_url: str
    token: str

    @property
    def api_base(self) -> str:
        return self.base_url.rstrip("/") + API_PREFIX

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"token {self.token}",
            "Accept": "application/json",
        }

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
    ) -> Any:
        url = self.api_base + path
        resp = requests.request(
            method,
            url,
            headers=self._headers(),
            params=params,
            json=json_body,
            timeout=60,
        )
        if resp.status_code >= 400:
            raise click.ClickException(
                f"HTTP {resp.status_code} for {method} {path}: {resp.text}"
            )
        if resp.status_code == 204 or not resp.content:
            return None
        ctype = resp.headers.get("Content-Type", "")
        if "application/json" in ctype:
            return resp.json()
        return resp.text


def get_client() -> Client:
    base_url = os.environ.get("CODEBERG_BASE_URL", DEFAULT_BASE_URL)
    token = os.environ.get("CODEBERG_TOKEN")
    if not token:
        raise click.ClickException("CODEBERG_TOKEN is required")
    return Client(base_url=base_url, token=token)


def echo_json(data: Any) -> None:
    click.echo(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False))


@click.group()
def cli() -> None:
    """Forgejo/Codeberg CLI."""


@cli.group("user")
def user_group() -> None:
    pass


@user_group.command("me")
def user_me() -> None:
    """Get the authenticated user."""
    c = get_client()
    echo_json(c.request("GET", "/user"))


@user_group.command("get")
@click.argument("username")
def user_get(username: str) -> None:
    """Get a user by username."""
    c = get_client()
    echo_json(c.request("GET", f"/users/{username}"))


@user_group.command("search")
@click.option("--q", required=True, help="Search query")
@click.option("--limit", type=int)
@click.option("--page", type=int)
def user_search(q: str, limit: Optional[int], page: Optional[int]) -> None:
    """Search users."""
    c = get_client()
    params: Dict[str, Any] = {"q": q}
    if limit is not None:
        params["limit"] = limit
    if page is not None:
        params["page"] = page
    echo_json(c.request("GET", "/users/search", params=params))


@cli.group("org")
def org_group() -> None:
    pass


@org_group.command("list")
def org_list_my() -> None:
    """List organizations of the authenticated user."""
    c = get_client()
    echo_json(c.request("GET", "/user/orgs"))


@org_group.command("get")
@click.argument("org")
def org_get(org: str) -> None:
    """Get an organization."""
    c = get_client()
    echo_json(c.request("GET", f"/orgs/{org}"))


@cli.group("repo")
def repo_group() -> None:
    pass


@repo_group.command("list")
@click.option("--username", help="Owner username (defaults to CODEBERG_USERNAME)")
@click.option("--limit", type=int)
@click.option("--page", type=int)
def repo_list_user(username: Optional[str], limit: Optional[int], page: Optional[int]) -> None:
    """List repositories for a user."""
    c = get_client()
    if not username:
        username = os.environ.get("CODEBERG_USERNAME")
    if not username:
        raise click.ClickException("--username or CODEBERG_USERNAME is required")
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if page is not None:
        params["page"] = page
    echo_json(c.request("GET", f"/users/{username}/repos", params=params or None))


@repo_group.command("get")
@click.argument("owner")
@click.argument("repo")
def repo_get(owner: str, repo: str) -> None:
    """Get a repository."""
    c = get_client()
    echo_json(c.request("GET", f"/repos/{owner}/{repo}"))


@repo_group.command("create")
@click.argument("name")
@click.option("--description", default="")
@click.option("--private/--public", default=False)
def repo_create(name: str, description: str, private: bool) -> None:
    """Create a repository for the authenticated user."""
    c = get_client()
    body = {"name": name, "description": description, "private": private}
    echo_json(c.request("POST", "/user/repos", json_body=body))


@repo_group.command("delete")
@click.argument("owner")
@click.argument("repo")
def repo_delete(owner: str, repo: str) -> None:
    """Delete a repository."""
    c = get_client()
    c.request("DELETE", f"/repos/{owner}/{repo}")
    click.echo("OK")


@repo_group.command("fork")
@click.argument("owner")
@click.argument("repo")
@click.option("--new-owner", help="Fork into this owner (user/org)")
@click.option("--new-name", help="New repo name")
def repo_fork(owner: str, repo: str, new_owner: Optional[str], new_name: Optional[str]) -> None:
    """Fork a repository."""
    c = get_client()
    body: Dict[str, Any] = {}
    if new_owner:
        body["organization"] = new_owner
    if new_name:
        body["name"] = new_name
    echo_json(c.request("POST", f"/repos/{owner}/{repo}/forks", json_body=body or None))


@repo_group.command("search")
@click.option("--q", required=True)
@click.option("--limit", type=int)
@click.option("--page", type=int)
def repo_search(q: str, limit: Optional[int], page: Optional[int]) -> None:
    """Search repositories."""
    c = get_client()
    params: Dict[str, Any] = {"q": q}
    if limit is not None:
        params["limit"] = limit
    if page is not None:
        params["page"] = page
    echo_json(c.request("GET", "/repos/search", params=params))


@cli.group("issue")
def issue_group() -> None:
    pass


@issue_group.command("list")
@click.argument("owner")
@click.argument("repo")
@click.option("--state", type=click.Choice(["open", "closed", "all"]), default="open")
@click.option("--limit", type=int)
@click.option("--page", type=int)
def issue_list(owner: str, repo: str, state: str, limit: Optional[int], page: Optional[int]) -> None:
    """List issues for a repository."""
    c = get_client()
    params: Dict[str, Any] = {"state": state}
    if limit is not None:
        params["limit"] = limit
    if page is not None:
        params["page"] = page
    echo_json(c.request("GET", f"/repos/{owner}/{repo}/issues", params=params))


@issue_group.command("get")
@click.argument("owner")
@click.argument("repo")
@click.argument("index", type=int)
def issue_get(owner: str, repo: str, index: int) -> None:
    """Get an issue by index."""
    c = get_client()
    echo_json(c.request("GET", f"/repos/{owner}/{repo}/issues/{index}"))


@issue_group.command("create")
@click.argument("owner")
@click.argument("repo")
@click.option("--title", required=True)
@click.option("--body", default="")
def issue_create(owner: str, repo: str, title: str, body: str) -> None:
    """Create an issue."""
    c = get_client()
    echo_json(
        c.request(
            "POST",
            f"/repos/{owner}/{repo}/issues",
            json_body={"title": title, "body": body},
        )
    )


@issue_group.command("update")
@click.argument("owner")
@click.argument("repo")
@click.argument("index", type=int)
@click.option("--title")
@click.option("--body")
@click.option("--state", type=click.Choice(["open", "closed"]))
def issue_update(owner: str, repo: str, index: int, title: Optional[str], body: Optional[str], state: Optional[str]) -> None:
    """Update an issue."""
    c = get_client()
    patch: Dict[str, Any] = {}
    if title is not None:
        patch["title"] = title
    if body is not None:
        patch["body"] = body
    if state is not None:
        patch["state"] = state
    if not patch:
        raise click.ClickException("No fields to update")
    echo_json(c.request("PATCH", f"/repos/{owner}/{repo}/issues/{index}", json_body=patch))


@issue_group.command("comment")
@click.argument("owner")
@click.argument("repo")
@click.argument("index", type=int)
@click.option("--body", required=True)
def issue_comment(owner: str, repo: str, index: int, body: str) -> None:
    """Add a comment to an issue."""
    c = get_client()
    echo_json(
        c.request(
            "POST",
            f"/repos/{owner}/{repo}/issues/{index}/comments",
            json_body={"body": body},
        )
    )


@issue_group.command("labels-add")
@click.argument("owner")
@click.argument("repo")
@click.argument("index", type=int)
@click.option("--labels", required=True, help="Comma-separated label IDs")
def issue_labels_add(owner: str, repo: str, index: int, labels: str) -> None:
    """Add labels to an issue (by label IDs)."""
    c = get_client()
    label_ids = [int(x.strip()) for x in labels.split(",") if x.strip()]
    echo_json(
        c.request(
            "POST",
            f"/repos/{owner}/{repo}/issues/{index}/labels",
            json_body=label_ids,
        )
    )


@cli.group("pr")
def pr_group() -> None:
    pass


@pr_group.command("list")
@click.argument("owner")
@click.argument("repo")
@click.option("--state", type=click.Choice(["open", "closed", "all"]), default="open")
@click.option("--limit", type=int)
@click.option("--page", type=int)
def pr_list(owner: str, repo: str, state: str, limit: Optional[int], page: Optional[int]) -> None:
    """List pull requests."""
    c = get_client()
    params: Dict[str, Any] = {"state": state}
    if limit is not None:
        params["limit"] = limit
    if page is not None:
        params["page"] = page
    echo_json(c.request("GET", f"/repos/{owner}/{repo}/pulls", params=params))


@pr_group.command("get")
@click.argument("owner")
@click.argument("repo")
@click.argument("index", type=int)
def pr_get(owner: str, repo: str, index: int) -> None:
    """Get a pull request."""
    c = get_client()
    echo_json(c.request("GET", f"/repos/{owner}/{repo}/pulls/{index}"))


@pr_group.command("create")
@click.argument("owner")
@click.argument("repo")
@click.option("--title", required=True)
@click.option("--body", default="")
@click.option("--head", required=True, help="Head branch (e.g. user:branch or branch)")
@click.option("--base", required=True, help="Base branch")
def pr_create(owner: str, repo: str, title: str, body: str, head: str, base: str) -> None:
    """Create a pull request."""
    c = get_client()
    echo_json(
        c.request(
            "POST",
            f"/repos/{owner}/{repo}/pulls",
            json_body={"title": title, "body": body, "head": head, "base": base},
        )
    )


@cli.group("branch")
def branch_group() -> None:
    pass


@branch_group.command("list")
@click.argument("owner")
@click.argument("repo")
def branch_list(owner: str, repo: str) -> None:
    """List branches."""
    c = get_client()
    echo_json(c.request("GET", f"/repos/{owner}/{repo}/branches"))


@branch_group.command("get")
@click.argument("owner")
@click.argument("repo")
@click.argument("branch")
def branch_get(owner: str, repo: str, branch: str) -> None:
    """Get a branch."""
    c = get_client()
    echo_json(c.request("GET", f"/repos/{owner}/{repo}/branches/{branch}"))


@branch_group.command("create")
@click.argument("owner")
@click.argument("repo")
@click.option("--new", "new_branch", required=True)
@click.option("--from", "from_branch", required=True, help="Existing branch name")
def branch_create(owner: str, repo: str, new_branch: str, from_branch: str) -> None:
    """Create a branch from another branch."""
    c = get_client()
    echo_json(
        c.request(
            "POST",
            f"/repos/{owner}/{repo}/branches",
            json_body={"new_branch_name": new_branch, "old_branch_name": from_branch},
        )
    )


@cli.group("release")
def release_group() -> None:
    pass


@release_group.command("list")
@click.argument("owner")
@click.argument("repo")
def release_list(owner: str, repo: str) -> None:
    """List releases."""
    c = get_client()
    echo_json(c.request("GET", f"/repos/{owner}/{repo}/releases"))


@release_group.command("get")
@click.argument("owner")
@click.argument("repo")
@click.argument("id", type=int)
def release_get(owner: str, repo: str, id: int) -> None:
    """Get a release by ID."""
    c = get_client()
    echo_json(c.request("GET", f"/repos/{owner}/{repo}/releases/{id}"))


@release_group.command("create")
@click.argument("owner")
@click.argument("repo")
@click.option("--tag", required=True)
@click.option("--name", required=True)
@click.option("--body", default="")
@click.option("--draft/--no-draft", default=False)
@click.option("--prerelease/--no-prerelease", default=False)
def release_create(owner: str, repo: str, tag: str, name: str, body: str, draft: bool, prerelease: bool) -> None:
    """Create a release."""
    c = get_client()
    payload = {
        "tag_name": tag,
        "name": name,
        "body": body,
        "draft": draft,
        "prerelease": prerelease,
    }
    echo_json(c.request("POST", f"/repos/{owner}/{repo}/releases", json_body=payload))


def main(argv: Optional[list[str]] = None) -> int:
    try:
        cli.main(args=argv, prog_name="forgejo")
        return 0
    except click.ClickException as e:
        click.echo(str(e), err=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
