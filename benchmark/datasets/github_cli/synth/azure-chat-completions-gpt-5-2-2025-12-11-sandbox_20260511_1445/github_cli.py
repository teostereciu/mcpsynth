#!/usr/bin/env python3
"""GitHub REST API CLI.

Auth via env:
  - GITHUB_TOKEN (required)
  - GITHUB_API_BASE_URL (optional, default https://api.github.com)
  - GITHUB_TEST_REPO (optional, owner/repo)

This CLI is intentionally pragmatic for agent use: it supports JSON in/out,
pagination helpers, and common GitHub workflows.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Tuple

import requests

DEFAULT_API_BASE_URL = "https://api.github.com"
DEFAULT_API_VERSION = "2022-11-28"
DEFAULT_ACCEPT = "application/vnd.github+json"


class GitHubCLIError(RuntimeError):
    pass


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.environ.get(name)
    return v if v not in (None, "") else default


@dataclass
class GitHubClient:
    token: str
    base_url: str = DEFAULT_API_BASE_URL
    api_version: str = DEFAULT_API_VERSION

    def _headers(self, accept: str = DEFAULT_ACCEPT) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": accept,
            "X-GitHub-Api-Version": self.api_version,
        }

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        accept: str = DEFAULT_ACCEPT,
    ) -> Any:
        url = self.base_url.rstrip("/") + path
        resp = requests.request(
            method,
            url,
            headers=self._headers(accept=accept),
            params={k: v for k, v in (params or {}).items() if v is not None},
            json=json_body,
            timeout=60,
        )
        if resp.status_code >= 400:
            msg = resp.text
            try:
                msg = json.dumps(resp.json(), indent=2)
            except Exception:
                pass
            raise GitHubCLIError(f"HTTP {resp.status_code} {method} {path}: {msg}")
        if resp.status_code == 204:
            return None
        ctype = resp.headers.get("content-type", "")
        if "application/json" in ctype:
            return resp.json()
        return resp.text

    def paginate(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        accept: str = DEFAULT_ACCEPT,
        per_page: int = 100,
        max_pages: Optional[int] = None,
    ) -> List[Any]:
        out: List[Any] = []
        page = 1
        while True:
            p = dict(params or {})
            p.setdefault("per_page", per_page)
            p["page"] = page
            data = self.request(method, path, params=p, accept=accept)
            if not isinstance(data, list):
                return data  # type: ignore[return-value]
            out.extend(data)
            if len(data) < per_page:
                break
            page += 1
            if max_pages is not None and page > max_pages:
                break
        return out


def _parse_owner_repo(value: Optional[str]) -> Tuple[str, str]:
    if not value:
        raise GitHubCLIError("owner/repo is required (or set GITHUB_TEST_REPO)")
    if "/" not in value:
        raise GitHubCLIError("Expected owner/repo")
    owner, repo = value.split("/", 1)
    return owner, repo


def _print(data: Any, *, raw: bool = False) -> None:
    if raw and isinstance(data, str):
        sys.stdout.write(data)
        if not data.endswith("\n"):
            sys.stdout.write("\n")
        return
    sys.stdout.write(json.dumps(data, indent=2, sort_keys=False))
    sys.stdout.write("\n")


def _add_common_repo_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--repo", default=_env("GITHUB_TEST_REPO"), help="owner/repo (default: GITHUB_TEST_REPO)")


def cmd_users_me(client: GitHubClient, args: argparse.Namespace) -> None:
    _print(client.request("GET", "/user"))


def cmd_users_get(client: GitHubClient, args: argparse.Namespace) -> None:
    _print(client.request("GET", f"/users/{args.username}"))


def cmd_gists_list(client: GitHubClient, args: argparse.Namespace) -> None:
    path = "/gists" if args.mine else f"/users/{args.username}/gists"
    _print(client.paginate("GET", path, params={"since": args.since}))


def cmd_gists_create(client: GitHubClient, args: argparse.Namespace) -> None:
    files: Dict[str, Dict[str, str]] = {}
    for spec in args.file:
        if "=" not in spec:
            raise GitHubCLIError("--file expects name=path")
        name, fpath = spec.split("=", 1)
        with open(fpath, "r", encoding="utf-8") as f:
            files[name] = {"content": f.read()}
    body = {"description": args.description, "public": args.public, "files": files}
    _print(client.request("POST", "/gists", json_body=body))


def cmd_search_repos(client: GitHubClient, args: argparse.Namespace) -> None:
    _print(client.request("GET", "/search/repositories", params={"q": args.q, "sort": args.sort, "order": args.order, "per_page": args.per_page, "page": args.page}))


def cmd_search_code(client: GitHubClient, args: argparse.Namespace) -> None:
    accept = "application/vnd.github.text-match+json" if args.text_match else DEFAULT_ACCEPT
    _print(client.request("GET", "/search/code", params={"q": args.q, "sort": args.sort, "order": args.order, "per_page": args.per_page, "page": args.page}, accept=accept))


def cmd_search_issues(client: GitHubClient, args: argparse.Namespace) -> None:
    accept = "application/vnd.github.text-match+json" if args.text_match else DEFAULT_ACCEPT
    _print(client.request("GET", "/search/issues", params={"q": args.q, "sort": args.sort, "order": args.order, "per_page": args.per_page, "page": args.page}, accept=accept))


def cmd_repos_get(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    _print(client.request("GET", f"/repos/{owner}/{repo}"))


def cmd_repos_branches(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    _print(client.paginate("GET", f"/repos/{owner}/{repo}/branches", params={"protected": args.protected}))


def cmd_repos_commits(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    params = {"sha": args.sha, "path": args.path, "since": args.since, "until": args.until, "author": args.author}
    _print(client.paginate("GET", f"/repos/{owner}/{repo}/commits", params=params))


def cmd_repos_contents_get(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    params = {"ref": args.ref}
    data = client.request("GET", f"/repos/{owner}/{repo}/contents/{args.path.lstrip('/')}" , params=params)
    if args.decode and isinstance(data, dict) and data.get("content") and data.get("encoding") == "base64":
        content = base64.b64decode(data["content"].encode("utf-8")).decode("utf-8", errors="replace")
        _print({"path": data.get("path"), "sha": data.get("sha"), "content": content}, raw=False)
    else:
        _print(data)


def cmd_repos_contents_put(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    with open(args.file, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    body: Dict[str, Any] = {"message": args.message, "content": b64, "branch": args.branch}
    if args.sha:
        body["sha"] = args.sha
    if args.committer_name or args.committer_email:
        body["committer"] = {"name": args.committer_name, "email": args.committer_email}
    if args.author_name or args.author_email:
        body["author"] = {"name": args.author_name, "email": args.author_email}
    _print(client.request("PUT", f"/repos/{owner}/{repo}/contents/{args.path.lstrip('/')}" , json_body={k: v for k, v in body.items() if v is not None}))


def cmd_repos_contents_delete(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    body: Dict[str, Any] = {"message": args.message, "sha": args.sha, "branch": args.branch}
    if args.committer_name or args.committer_email:
        body["committer"] = {"name": args.committer_name, "email": args.committer_email}
    if args.author_name or args.author_email:
        body["author"] = {"name": args.author_name, "email": args.author_email}
    _print(client.request("DELETE", f"/repos/{owner}/{repo}/contents/{args.path.lstrip('/')}" , json_body={k: v for k, v in body.items() if v is not None}))


def cmd_issues_list(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    params = {"state": args.state, "labels": args.labels, "since": args.since, "per_page": args.per_page}
    _print(client.paginate("GET", f"/repos/{owner}/{repo}/issues", params=params, per_page=args.per_page))


def cmd_issues_get(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    _print(client.request("GET", f"/repos/{owner}/{repo}/issues/{args.number}"))


def cmd_issues_create(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    body: Dict[str, Any] = {"title": args.title, "body": args.body}
    if args.assignees:
        body["assignees"] = args.assignees
    if args.labels:
        body["labels"] = args.labels
    _print(client.request("POST", f"/repos/{owner}/{repo}/issues", json_body=body))


def cmd_issues_update(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    body: Dict[str, Any] = {}
    for k in ("title", "body", "state"):
        v = getattr(args, k)
        if v is not None:
            body[k] = v
    if args.assignees is not None:
        body["assignees"] = args.assignees
    if args.labels is not None:
        body["labels"] = args.labels
    _print(client.request("PATCH", f"/repos/{owner}/{repo}/issues/{args.number}", json_body=body))


def cmd_issues_comment(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    _print(client.request("POST", f"/repos/{owner}/{repo}/issues/{args.number}/comments", json_body={"body": args.body}))


def cmd_issues_labels_add(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    _print(client.request("POST", f"/repos/{owner}/{repo}/issues/{args.number}/labels", json_body={"labels": args.labels}))


def cmd_pulls_list(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    params = {"state": args.state, "base": args.base, "head": args.head, "sort": args.sort, "direction": args.direction, "per_page": args.per_page}
    _print(client.paginate("GET", f"/repos/{owner}/{repo}/pulls", params=params, per_page=args.per_page))


def cmd_pulls_get(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    _print(client.request("GET", f"/repos/{owner}/{repo}/pulls/{args.number}"))


def cmd_pulls_create(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    body: Dict[str, Any] = {"title": args.title, "head": args.head, "base": args.base, "body": args.body, "draft": args.draft}
    _print(client.request("POST", f"/repos/{owner}/{repo}/pulls", json_body=body))


def cmd_pulls_merge(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    body: Dict[str, Any] = {"commit_title": args.commit_title, "commit_message": args.commit_message, "merge_method": args.merge_method}
    _print(client.request("PUT", f"/repos/{owner}/{repo}/pulls/{args.number}/merge", json_body={k: v for k, v in body.items() if v is not None}))


def cmd_releases_list(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    _print(client.paginate("GET", f"/repos/{owner}/{repo}/releases", per_page=args.per_page, params={"per_page": args.per_page}))


def cmd_releases_get(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    _print(client.request("GET", f"/repos/{owner}/{repo}/releases/{args.release_id}"))


def cmd_releases_latest(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    _print(client.request("GET", f"/repos/{owner}/{repo}/releases/latest"))


def cmd_releases_create(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    body: Dict[str, Any] = {
        "tag_name": args.tag_name,
        "target_commitish": args.target_commitish,
        "name": args.name,
        "body": args.body,
        "draft": args.draft,
        "prerelease": args.prerelease,
        "generate_release_notes": args.generate_release_notes,
        "make_latest": args.make_latest,
        "discussion_category_name": args.discussion_category_name,
    }
    _print(client.request("POST", f"/repos/{owner}/{repo}/releases", json_body={k: v for k, v in body.items() if v is not None}))


def cmd_actions_workflow_runs(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    params = {
        "actor": args.actor,
        "branch": args.branch,
        "event": args.event,
        "status": args.status,
        "created": args.created,
        "exclude_pull_requests": args.exclude_pull_requests,
        "check_suite_id": args.check_suite_id,
        "head_sha": args.head_sha,
        "per_page": args.per_page,
        "page": args.page,
    }
    _print(client.request("GET", f"/repos/{owner}/{repo}/actions/runs", params=params))


def cmd_actions_run_cancel(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    _print(client.request("POST", f"/repos/{owner}/{repo}/actions/runs/{args.run_id}/cancel"))


def cmd_actions_run_rerun(client: GitHubClient, args: argparse.Namespace) -> None:
    owner, repo = _parse_owner_repo(args.repo)
    _print(client.request("POST", f"/repos/{owner}/{repo}/actions/runs/{args.run_id}/rerun"))


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="github_cli", description="GitHub REST API CLI")
    p.add_argument("--api-base-url", default=_env("GITHUB_API_BASE_URL", DEFAULT_API_BASE_URL))
    p.add_argument("--api-version", default=_env("GITHUB_API_VERSION", DEFAULT_API_VERSION))
    p.add_argument("--token", default=_env("GITHUB_TOKEN"), help="GitHub token (default: GITHUB_TOKEN)")

    sub = p.add_subparsers(dest="cmd", required=True)

    # users
    sp = sub.add_parser("users.me", help="Get the authenticated user")
    sp.set_defaults(func=cmd_users_me)

    sp = sub.add_parser("users.get", help="Get a user")
    sp.add_argument("username")
    sp.set_defaults(func=cmd_users_get)

    # gists
    sp = sub.add_parser("gists.list", help="List gists")
    g = sp.add_mutually_exclusive_group(required=True)
    g.add_argument("--mine", action="store_true", help="List authenticated user's gists")
    g.add_argument("--username", help="List a user's gists")
    sp.add_argument("--since")
    sp.set_defaults(func=cmd_gists_list)

    sp = sub.add_parser("gists.create", help="Create a gist")
    sp.add_argument("--description", default="")
    sp.add_argument("--public", action="store_true")
    sp.add_argument("--file", action="append", required=True, help="name=path (repeatable)")
    sp.set_defaults(func=cmd_gists_create)

    # search
    sp = sub.add_parser("search.repos", help="Search repositories")
    sp.add_argument("q")
    sp.add_argument("--sort")
    sp.add_argument("--order")
    sp.add_argument("--per-page", type=int, default=30)
    sp.add_argument("--page", type=int, default=1)
    sp.set_defaults(func=cmd_search_repos)

    sp = sub.add_parser("search.code", help="Search code")
    sp.add_argument("q")
    sp.add_argument("--sort")
    sp.add_argument("--order")
    sp.add_argument("--text-match", action="store_true", help="Include text match metadata")
    sp.add_argument("--per-page", type=int, default=30)
    sp.add_argument("--page", type=int, default=1)
    sp.set_defaults(func=cmd_search_code)

    sp = sub.add_parser("search.issues", help="Search issues and pull requests")
    sp.add_argument("q")
    sp.add_argument("--sort")
    sp.add_argument("--order")
    sp.add_argument("--text-match", action="store_true", help="Include text match metadata")
    sp.add_argument("--per-page", type=int, default=30)
    sp.add_argument("--page", type=int, default=1)
    sp.set_defaults(func=cmd_search_issues)

    # repos
    sp = sub.add_parser("repos.get", help="Get a repository")
    _add_common_repo_args(sp)
    sp.set_defaults(func=cmd_repos_get)

    sp = sub.add_parser("repos.branches", help="List branches")
    _add_common_repo_args(sp)
    sp.add_argument("--protected", type=lambda x: x.lower() == "true", default=None)
    sp.set_defaults(func=cmd_repos_branches)

    sp = sub.add_parser("repos.commits", help="List commits")
    _add_common_repo_args(sp)
    sp.add_argument("--sha")
    sp.add_argument("--path")
    sp.add_argument("--since")
    sp.add_argument("--until")
    sp.add_argument("--author")
    sp.set_defaults(func=cmd_repos_commits)

    sp = sub.add_parser("repos.contents.get", help="Get repository content")
    _add_common_repo_args(sp)
    sp.add_argument("path")
    sp.add_argument("--ref")
    sp.add_argument("--decode", action="store_true", help="Decode base64 file content")
    sp.set_defaults(func=cmd_repos_contents_get)

    sp = sub.add_parser("repos.contents.put", help="Create or update file contents")
    _add_common_repo_args(sp)
    sp.add_argument("path")
    sp.add_argument("--file", required=True, help="Local file path")
    sp.add_argument("--message", required=True, help="Commit message")
    sp.add_argument("--branch")
    sp.add_argument("--sha", help="Required when updating an existing file")
    sp.add_argument("--committer-name")
    sp.add_argument("--committer-email")
    sp.add_argument("--author-name")
    sp.add_argument("--author-email")
    sp.set_defaults(func=cmd_repos_contents_put)

    sp = sub.add_parser("repos.contents.delete", help="Delete a file")
    _add_common_repo_args(sp)
    sp.add_argument("path")
    sp.add_argument("--message", required=True, help="Commit message")
    sp.add_argument("--sha", required=True, help="Blob SHA of the file being deleted")
    sp.add_argument("--branch")
    sp.add_argument("--committer-name")
    sp.add_argument("--committer-email")
    sp.add_argument("--author-name")
    sp.add_argument("--author-email")
    sp.set_defaults(func=cmd_repos_contents_delete)

    # issues
    sp = sub.add_parser("issues.list", help="List issues for a repository")
    _add_common_repo_args(sp)
    sp.add_argument("--state", choices=["open", "closed", "all"], default="open")
    sp.add_argument("--labels", help="Comma-separated labels")
    sp.add_argument("--since")
    sp.add_argument("--per-page", type=int, default=30)
    sp.set_defaults(func=cmd_issues_list)

    sp = sub.add_parser("issues.get", help="Get an issue")
    _add_common_repo_args(sp)
    sp.add_argument("number", type=int)
    sp.set_defaults(func=cmd_issues_get)

    sp = sub.add_parser("issues.create", help="Create an issue")
    _add_common_repo_args(sp)
    sp.add_argument("--title", required=True)
    sp.add_argument("--body", default="")
    sp.add_argument("--assignees", nargs="*")
    sp.add_argument("--labels", nargs="*")
    sp.set_defaults(func=cmd_issues_create)

    sp = sub.add_parser("issues.update", help="Update an issue")
    _add_common_repo_args(sp)
    sp.add_argument("number", type=int)
    sp.add_argument("--title")
    sp.add_argument("--body")
    sp.add_argument("--state", choices=["open", "closed"], default=None)
    sp.add_argument("--assignees", nargs="*", default=None)
    sp.add_argument("--labels", nargs="*", default=None)
    sp.set_defaults(func=cmd_issues_update)

    sp = sub.add_parser("issues.comment", help="Create an issue comment")
    _add_common_repo_args(sp)
    sp.add_argument("number", type=int)
    sp.add_argument("--body", required=True)
    sp.set_defaults(func=cmd_issues_comment)

    sp = sub.add_parser("issues.labels.add", help="Add labels to an issue")
    _add_common_repo_args(sp)
    sp.add_argument("number", type=int)
    sp.add_argument("labels", nargs="+", help="Label names")
    sp.set_defaults(func=cmd_issues_labels_add)

    # pulls
    sp = sub.add_parser("pulls.list", help="List pull requests")
    _add_common_repo_args(sp)
    sp.add_argument("--state", choices=["open", "closed", "all"], default="open")
    sp.add_argument("--head")
    sp.add_argument("--base")
    sp.add_argument("--sort", choices=["created", "updated", "popularity", "long-running"], default=None)
    sp.add_argument("--direction", choices=["asc", "desc"], default=None)
    sp.add_argument("--per-page", type=int, default=30)
    sp.set_defaults(func=cmd_pulls_list)

    sp = sub.add_parser("pulls.get", help="Get a pull request")
    _add_common_repo_args(sp)
    sp.add_argument("number", type=int)
    sp.set_defaults(func=cmd_pulls_get)

    sp = sub.add_parser("pulls.create", help="Create a pull request")
    _add_common_repo_args(sp)
    sp.add_argument("--title", required=True)
    sp.add_argument("--head", required=True, help="The name of the branch where your changes are implemented")
    sp.add_argument("--base", required=True, help="The name of the branch you want the changes pulled into")
    sp.add_argument("--body", default="")
    sp.add_argument("--draft", action="store_true")
    sp.set_defaults(func=cmd_pulls_create)

    sp = sub.add_parser("pulls.merge", help="Merge a pull request")
    _add_common_repo_args(sp)
    sp.add_argument("number", type=int)
    sp.add_argument("--commit-title")
    sp.add_argument("--commit-message")
    sp.add_argument("--merge-method", choices=["merge", "squash", "rebase"], default=None)
    sp.set_defaults(func=cmd_pulls_merge)

    # releases
    sp = sub.add_parser("releases.list", help="List releases")
    _add_common_repo_args(sp)
    sp.add_argument("--per-page", type=int, default=30)
    sp.set_defaults(func=cmd_releases_list)

    sp = sub.add_parser("releases.get", help="Get a release by id")
    _add_common_repo_args(sp)
    sp.add_argument("release_id", type=int)
    sp.set_defaults(func=cmd_releases_get)

    sp = sub.add_parser("releases.latest", help="Get the latest release")
    _add_common_repo_args(sp)
    sp.set_defaults(func=cmd_releases_latest)

    sp = sub.add_parser("releases.create", help="Create a release")
    _add_common_repo_args(sp)
    sp.add_argument("--tag-name", required=True)
    sp.add_argument("--target-commitish")
    sp.add_argument("--name")
    sp.add_argument("--body")
    sp.add_argument("--draft", action="store_true")
    sp.add_argument("--prerelease", action="store_true")
    sp.add_argument("--generate-release-notes", action="store_true")
    sp.add_argument("--discussion-category-name")
    sp.add_argument("--make-latest", choices=["true", "false", "legacy"], default=None)
    sp.set_defaults(func=cmd_releases_create)

    # actions
    sp = sub.add_parser("actions.runs", help="List workflow runs for a repository")
    _add_common_repo_args(sp)
    sp.add_argument("--actor")
    sp.add_argument("--branch")
    sp.add_argument("--event")
    sp.add_argument("--status")
    sp.add_argument("--created", help="Date-time range query")
    sp.add_argument("--exclude-pull-requests", action="store_true")
    sp.add_argument("--check-suite-id", type=int)
    sp.add_argument("--head-sha")
    sp.add_argument("--per-page", type=int, default=30)
    sp.add_argument("--page", type=int, default=1)
    sp.set_defaults(func=cmd_actions_workflow_runs)

    sp = sub.add_parser("actions.runs.cancel", help="Cancel a workflow run")
    _add_common_repo_args(sp)
    sp.add_argument("run_id", type=int)
    sp.set_defaults(func=cmd_actions_run_cancel)

    sp = sub.add_parser("actions.runs.rerun", help="Re-run a workflow run")
    _add_common_repo_args(sp)
    sp.add_argument("run_id", type=int)
    sp.set_defaults(func=cmd_actions_run_rerun)

    return p


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if not args.token:
        raise GitHubCLIError("Missing token. Set GITHUB_TOKEN or pass --token")
    client = GitHubClient(token=args.token, base_url=args.api_base_url, api_version=args.api_version)
    args.func(client, args)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except GitHubCLIError as e:
        sys.stderr.write(f"error: {e}\n")
        raise SystemExit(2)
