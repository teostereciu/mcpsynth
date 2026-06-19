#!/usr/bin/env python3
"""Notion CLI

Implements a task-focused CLI over the Notion API.
Auth via env var NOTION_API_KEY.
Default parent page via env var NOTION_PARENT_PAGE_ID.
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass
from typing import Any, Dict, Optional

import click
import requests

NOTION_BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"


class NotionError(click.ClickException):
    pass


@dataclass
class NotionClient:
    api_key: str
    base_url: str = NOTION_BASE_URL
    notion_version: str = NOTION_VERSION
    timeout_s: int = 60

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Notion-Version": self.notion_version,
            "Content-Type": "application/json",
        }

    def request(self, method: str, path: str, *, params: Optional[dict] = None, json_body: Optional[dict] = None) -> Any:
        url = self.base_url + path
        resp = requests.request(
            method,
            url,
            headers=self._headers(),
            params=params,
            json=json_body,
            timeout=self.timeout_s,
        )
        if resp.status_code >= 400:
            try:
                payload = resp.json()
            except Exception:
                payload = {"message": resp.text}
            raise NotionError(f"HTTP {resp.status_code}: {json.dumps(payload, ensure_ascii=False)}")
        if resp.status_code == 204:
            return None
        return resp.json()


def _client() -> NotionClient:
    api_key = os.environ.get("NOTION_API_KEY")
    if not api_key:
        raise NotionError("NOTION_API_KEY is not set")
    return NotionClient(api_key=api_key)


def _echo(data: Any, *, pretty: bool) -> None:
    if pretty:
        click.echo(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False))
    else:
        click.echo(json.dumps(data, ensure_ascii=False))


def _load_json_arg(value: Optional[str]) -> Optional[dict]:
    if value is None:
        return None
    value = value.strip()
    if not value:
        return None
    # Allow @file.json
    if value.startswith("@"):
        with open(value[1:], "r", encoding="utf-8") as f:
            return json.load(f)
    return json.loads(value)


@click.group()
@click.option("--pretty/--no-pretty", default=True, help="Pretty-print JSON output")
def cli(pretty: bool) -> None:
    """Notion API CLI."""
    ctx = click.get_current_context()
    ctx.obj = {"pretty": pretty}


@cli.group()
def pages() -> None:
    """Page operations."""


@pages.command("create")
@click.option("--parent-page-id", default=lambda: os.environ.get("NOTION_PARENT_PAGE_ID"), show_default="env NOTION_PARENT_PAGE_ID")
@click.option("--parent-database-id", default=None)
@click.option("--properties", required=True, help='JSON object for page properties. Example: {"Name": {"title": [{"text": {"content": "Hello"}}]}}')
@click.option("--children", default=None, help="JSON array of block children")
@click.option("--markdown", default=None, help="Notion-flavored Markdown content (mutually exclusive with --children)")
def pages_create(parent_page_id: Optional[str], parent_database_id: Optional[str], properties: str, children: Optional[str], markdown: Optional[str]) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]

    if bool(children) and bool(markdown):
        raise NotionError("--children and --markdown are mutually exclusive")

    parent: Dict[str, str]
    if parent_database_id:
        parent = {"database_id": parent_database_id}
    else:
        if not parent_page_id:
            raise NotionError("Provide --parent-page-id or set NOTION_PARENT_PAGE_ID, or use --parent-database-id")
        parent = {"page_id": parent_page_id}

    body: Dict[str, Any] = {
        "parent": parent,
        "properties": _load_json_arg(properties) or {},
    }
    if children:
        body["children"] = _load_json_arg(children) or []
    if markdown:
        body["markdown"] = markdown

    data = c.request("POST", "/pages", json_body=body)
    _echo(data, pretty=pretty)


@pages.command("get")
@click.argument("page_id")
def pages_get(page_id: str) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    data = c.request("GET", f"/pages/{page_id}")
    _echo(data, pretty=pretty)


@pages.command("update")
@click.argument("page_id")
@click.option("--properties", default=None, help="JSON object of properties to update")
@click.option("--archived", type=bool, default=None)
@click.option("--in-trash", type=bool, default=None)
def pages_update(page_id: str, properties: Optional[str], archived: Optional[bool], in_trash: Optional[bool]) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    body: Dict[str, Any] = {}
    if properties is not None:
        body["properties"] = _load_json_arg(properties) or {}
    if archived is not None:
        body["archived"] = archived
    if in_trash is not None:
        body["in_trash"] = in_trash
    if not body:
        raise NotionError("No updates provided")
    data = c.request("PATCH", f"/pages/{page_id}", json_body=body)
    _echo(data, pretty=pretty)


@pages.command("archive")
@click.argument("page_id")
def pages_archive(page_id: str) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    data = c.request("PATCH", f"/pages/{page_id}", json_body={"archived": True})
    _echo(data, pretty=pretty)


@pages.command("trash")
@click.argument("page_id")
def pages_trash(page_id: str) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    data = c.request("PATCH", f"/pages/{page_id}", json_body={"in_trash": True})
    _echo(data, pretty=pretty)


@pages.command("property")
@click.argument("page_id")
@click.argument("property_id")
def pages_property(page_id: str, property_id: str) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    data = c.request("GET", f"/pages/{page_id}/properties/{property_id}")
    _echo(data, pretty=pretty)


@cli.group()
def databases() -> None:
    """Database operations."""


@databases.command("create")
@click.option("--parent-page-id", default=lambda: os.environ.get("NOTION_PARENT_PAGE_ID"), show_default="env NOTION_PARENT_PAGE_ID")
@click.option("--title", required=True, help="Database title (plain text)")
@click.option("--properties", required=True, help="JSON object of database properties schema")
def databases_create(parent_page_id: Optional[str], title: str, properties: str) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    if not parent_page_id:
        raise NotionError("Provide --parent-page-id or set NOTION_PARENT_PAGE_ID")
    body = {
        "parent": {"type": "page_id", "page_id": parent_page_id},
        "title": [{"type": "text", "text": {"content": title}}],
        "properties": _load_json_arg(properties) or {},
    }
    data = c.request("POST", "/databases", json_body=body)
    _echo(data, pretty=pretty)


@databases.command("get")
@click.argument("database_id")
def databases_get(database_id: str) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    data = c.request("GET", f"/databases/{database_id}")
    _echo(data, pretty=pretty)


@databases.command("update")
@click.argument("database_id")
@click.option("--title", default=None, help="New title (plain text)")
@click.option("--properties", default=None, help="JSON object of properties schema updates")
def databases_update(database_id: str, title: Optional[str], properties: Optional[str]) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    body: Dict[str, Any] = {}
    if title is not None:
        body["title"] = [{"type": "text", "text": {"content": title}}]
    if properties is not None:
        body["properties"] = _load_json_arg(properties) or {}
    if not body:
        raise NotionError("No updates provided")
    data = c.request("PATCH", f"/databases/{database_id}", json_body=body)
    _echo(data, pretty=pretty)


@databases.command("query")
@click.argument("database_id")
@click.option("--filter", "filter_json", default=None, help="JSON filter object")
@click.option("--sorts", default=None, help="JSON array of sorts")
@click.option("--start-cursor", default=None)
@click.option("--page-size", default=None, type=int)
def databases_query(database_id: str, filter_json: Optional[str], sorts: Optional[str], start_cursor: Optional[str], page_size: Optional[int]) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    body: Dict[str, Any] = {}
    if filter_json is not None:
        body["filter"] = _load_json_arg(filter_json)
    if sorts is not None:
        body["sorts"] = _load_json_arg(sorts)
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size
    data = c.request("POST", f"/databases/{database_id}/query", json_body=body)
    _echo(data, pretty=pretty)


@cli.group()
def blocks() -> None:
    """Block operations."""


@blocks.command("get")
@click.argument("block_id")
def blocks_get(block_id: str) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    data = c.request("GET", f"/blocks/{block_id}")
    _echo(data, pretty=pretty)


@blocks.command("children")
@click.argument("block_id")
@click.option("--start-cursor", default=None)
@click.option("--page-size", default=None, type=int)
def blocks_children(block_id: str, start_cursor: Optional[str], page_size: Optional[int]) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    data = c.request("GET", f"/blocks/{block_id}/children", params=params or None)
    _echo(data, pretty=pretty)


@blocks.command("append")
@click.argument("block_id")
@click.option("--children", required=True, help="JSON array of block children to append")
def blocks_append(block_id: str, children: str) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    body = {"children": _load_json_arg(children) or []}
    data = c.request("PATCH", f"/blocks/{block_id}/children", json_body=body)
    _echo(data, pretty=pretty)


@blocks.command("update")
@click.argument("block_id")
@click.option("--block", "block_json", required=True, help="JSON object for block update payload")
def blocks_update(block_id: str, block_json: str) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    body = _load_json_arg(block_json) or {}
    data = c.request("PATCH", f"/blocks/{block_id}", json_body=body)
    _echo(data, pretty=pretty)


@blocks.command("delete")
@click.argument("block_id")
def blocks_delete(block_id: str) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    data = c.request("DELETE", f"/blocks/{block_id}")
    _echo(data, pretty=pretty)


@cli.group()
def comments() -> None:
    """Comment operations."""


@comments.command("create")
@click.option("--page-id", default=None)
@click.option("--discussion-id", default=None)
@click.option("--rich-text", required=True, help="JSON array of rich_text objects")
def comments_create(page_id: Optional[str], discussion_id: Optional[str], rich_text: str) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    if bool(page_id) == bool(discussion_id):
        raise NotionError("Provide exactly one of --page-id or --discussion-id")
    body: Dict[str, Any] = {"rich_text": _load_json_arg(rich_text) or []}
    if page_id:
        body["parent"] = {"page_id": page_id}
    else:
        body["discussion_id"] = discussion_id
    data = c.request("POST", "/comments", json_body=body)
    _echo(data, pretty=pretty)


@comments.command("list")
@click.option("--block-id", default=None)
@click.option("--page-size", default=None, type=int)
@click.option("--start-cursor", default=None)
def comments_list(block_id: Optional[str], page_size: Optional[int], start_cursor: Optional[str]) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    params: Dict[str, Any] = {}
    if block_id is not None:
        params["block_id"] = block_id
    if page_size is not None:
        params["page_size"] = page_size
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    data = c.request("GET", "/comments", params=params or None)
    _echo(data, pretty=pretty)


@comments.command("get")
@click.argument("comment_id")
def comments_get(comment_id: str) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    data = c.request("GET", f"/comments/{comment_id}")
    _echo(data, pretty=pretty)


@cli.group()
def users() -> None:
    """User operations."""


@users.command("list")
@click.option("--page-size", default=None, type=int)
@click.option("--start-cursor", default=None)
def users_list(page_size: Optional[int], start_cursor: Optional[str]) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    params: Dict[str, Any] = {}
    if page_size is not None:
        params["page_size"] = page_size
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    data = c.request("GET", "/users", params=params or None)
    _echo(data, pretty=pretty)


@users.command("get")
@click.argument("user_id")
def users_get(user_id: str) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    data = c.request("GET", f"/users/{user_id}")
    _echo(data, pretty=pretty)


@users.command("me")
def users_me() -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    data = c.request("GET", "/users/me")
    _echo(data, pretty=pretty)


@cli.command("search")
@click.option("--query", default=None)
@click.option("--filter", "filter_json", default=None, help="JSON filter object")
@click.option("--sort", default=None, help="JSON sort object")
@click.option("--start-cursor", default=None)
@click.option("--page-size", default=None, type=int)
def search_cmd(query: Optional[str], filter_json: Optional[str], sort: Optional[str], start_cursor: Optional[str], page_size: Optional[int]) -> None:
    c = _client()
    pretty = click.get_current_context().obj["pretty"]
    body: Dict[str, Any] = {}
    if query is not None:
        body["query"] = query
    if filter_json is not None:
        body["filter"] = _load_json_arg(filter_json)
    if sort is not None:
        body["sort"] = _load_json_arg(sort)
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size
    data = c.request("POST", "/search", json_body=body)
    _echo(data, pretty=pretty)


def main(argv: Optional[list[str]] = None) -> int:
    try:
        cli.main(args=argv, prog_name="notion")
        return 0
    except NotionError as e:
        raise click.ClickException(str(e))


if __name__ == "__main__":
    sys.exit(main())
