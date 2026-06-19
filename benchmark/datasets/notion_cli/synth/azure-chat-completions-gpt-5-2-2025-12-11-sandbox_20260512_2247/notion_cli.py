#!/usr/bin/env python3
"""Notion CLI

Environment:
  NOTION_API_KEY: Notion integration token
  NOTION_PARENT_PAGE_ID: default parent page id for creating pages/databases

This CLI intentionally exposes only named operations (no generic request passthrough).
"""

from __future__ import annotations

import json
import os
from typing import Any, Optional

import click
import requests

NOTION_BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"


class NotionError(click.ClickException):
    pass


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.environ.get(name)
    return v if v not in (None, "") else default


def _headers() -> dict[str, str]:
    api_key = _env("NOTION_API_KEY")
    if not api_key:
        raise NotionError("NOTION_API_KEY is not set")
    return {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def _request(method: str, path: str, *, params: dict[str, Any] | None = None, json_body: Any | None = None) -> Any:
    url = f"{NOTION_BASE_URL}{path}"
    r = requests.request(method, url, headers=_headers(), params=params, json=json_body, timeout=60)
    if r.status_code >= 400:
        try:
            data = r.json()
        except Exception:
            raise NotionError(f"HTTP {r.status_code}: {r.text}")
        msg = data.get("message") or data.get("error") or r.text
        raise NotionError(f"HTTP {r.status_code}: {msg}")
    if r.status_code == 204:
        return None
    return r.json()


def _parse_json_arg(value: Optional[str]) -> Any:
    if value is None:
        return None
    try:
        return json.loads(value)
    except json.JSONDecodeError as e:
        raise NotionError(f"Invalid JSON: {e}")


def _echo(data: Any, *, pretty: bool) -> None:
    if pretty:
        click.echo(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False))
    else:
        click.echo(json.dumps(data, ensure_ascii=False))


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--pretty/--no-pretty", default=True, help="Pretty-print JSON output")
@click.pass_context
def cli(ctx: click.Context, pretty: bool) -> None:
    ctx.ensure_object(dict)
    ctx.obj["pretty"] = pretty


@cli.group()
def pages() -> None:
    """Page operations."""


@cli.group()
def databases() -> None:
    """Database operations."""


@pages.command("create")
@click.option("--parent-page-id", default=lambda: _env("NOTION_PARENT_PAGE_ID"), help="Parent page id (defaults to NOTION_PARENT_PAGE_ID)")
@click.option("--parent-database-id", default=None, help="Parent database id")
@click.option("--properties", required=True, help="JSON object of page properties")
@click.option("--children", default=None, help="JSON array of block children")
@click.option("--markdown", default=None, help="Notion-flavored Markdown content (mutually exclusive with --children)")
@click.pass_context
def pages_create(ctx: click.Context, parent_page_id: Optional[str], parent_database_id: Optional[str], properties: str, children: Optional[str], markdown: Optional[str]) -> None:
    props = _parse_json_arg(properties)
    kids = _parse_json_arg(children)

    if markdown is not None and kids is not None:
        raise NotionError("--markdown is mutually exclusive with --children")

    parent: dict[str, Any] = {}
    if parent_database_id:
        parent = {"database_id": parent_database_id}
    elif parent_page_id:
        parent = {"page_id": parent_page_id}
    else:
        raise NotionError("Provide --parent-page-id or --parent-database-id (or set NOTION_PARENT_PAGE_ID)")

    body: dict[str, Any] = {"parent": parent, "properties": props}
    if kids is not None:
        body["children"] = kids
    if markdown is not None:
        body["markdown"] = markdown

    data = _request("POST", "/pages", json_body=body)
    _echo(data, pretty=ctx.obj["pretty"])


@pages.command("get")
@click.argument("page_id")
@click.option("--filter-properties", default=None, help="Comma-separated list of property IDs to include")
@click.pass_context
def pages_get(ctx: click.Context, page_id: str, filter_properties: Optional[str]) -> None:
    params = {}
    if filter_properties:
        params["filter_properties"] = filter_properties
    data = _request("GET", f"/pages/{page_id}", params=params or None)
    _echo(data, pretty=ctx.obj["pretty"])


@pages.command("update")
@click.argument("page_id")
@click.option("--properties", default=None, help="JSON object of properties to update")
@click.option("--archived", type=bool, default=None, help="Set archived status")
@click.option("--in-trash", "in_trash", type=bool, default=None, help="Set trash status")
@click.option("--icon", default=None, help="JSON icon object")
@click.option("--cover", default=None, help="JSON cover object")
@click.option("--locked", type=bool, default=None, help="Lock/unlock page")
@click.option("--erase-content", type=bool, default=None, help="Erase all existing content")
@click.option("--children", default=None, help="JSON array of block children to append")
@click.option("--markdown", default=None, help="Notion-flavored Markdown content to append (mutually exclusive with --children)")
@click.pass_context
def pages_update(
    ctx: click.Context,
    page_id: str,
    properties: Optional[str],
    archived: Optional[bool],
    in_trash: Optional[bool],
    icon: Optional[str],
    cover: Optional[str],
    locked: Optional[bool],
    erase_content: Optional[bool],
    children: Optional[str],
    markdown: Optional[str],
) -> None:
    if markdown is not None and children is not None:
        raise NotionError("--markdown is mutually exclusive with --children")

    body: dict[str, Any] = {}
    if properties is not None:
        body["properties"] = _parse_json_arg(properties)
    if archived is not None:
        body["archived"] = archived
    if in_trash is not None:
        body["in_trash"] = in_trash
    if icon is not None:
        body["icon"] = _parse_json_arg(icon)
    if cover is not None:
        body["cover"] = _parse_json_arg(cover)
    if locked is not None:
        body["locked"] = locked
    if erase_content is not None:
        body["erase_content"] = erase_content
    if children is not None:
        body["children"] = _parse_json_arg(children)
    if markdown is not None:
        body["markdown"] = markdown

    if not body:
        raise NotionError("No updates provided")

    data = _request("PATCH", f"/pages/{page_id}", json_body=body)
    _echo(data, pretty=ctx.obj["pretty"])


@pages.command("archive")
@click.argument("page_id")
@click.pass_context
def pages_archive(ctx: click.Context, page_id: str) -> None:
    data = _request("PATCH", f"/pages/{page_id}", json_body={"archived": True})
    _echo(data, pretty=ctx.obj["pretty"])


@pages.command("trash")
@click.argument("page_id")
@click.pass_context
def pages_trash(ctx: click.Context, page_id: str) -> None:
    data = _request("PATCH", f"/pages/{page_id}", json_body={"in_trash": True})
    _echo(data, pretty=ctx.obj["pretty"])


@pages.command("restore")
@click.argument("page_id")
@click.pass_context
def pages_restore(ctx: click.Context, page_id: str) -> None:
    data = _request("PATCH", f"/pages/{page_id}", json_body={"in_trash": False})
    _echo(data, pretty=ctx.obj["pretty"])


@databases.command("create")
@click.option("--parent-page-id", default=lambda: _env("NOTION_PARENT_PAGE_ID"), help="Parent page id (defaults to NOTION_PARENT_PAGE_ID)")
@click.option("--title", required=True, help="Database title (plain text)")
@click.option("--properties", default=None, help="JSON object of database properties schema")
@click.option("--description", default=None, help="JSON rich_text array for description")
@click.option("--is-inline", type=bool, default=None, help="Whether database is inline")
@click.option("--icon", default=None, help="JSON icon object")
@click.option("--cover", default=None, help="JSON cover object")
@click.pass_context
def databases_create(
    ctx: click.Context,
    parent_page_id: Optional[str],
    title: str,
    properties: Optional[str],
    description: Optional[str],
    is_inline: Optional[bool],
    icon: Optional[str],
    cover: Optional[str],
) -> None:
    if not parent_page_id:
        raise NotionError("Provide --parent-page-id or set NOTION_PARENT_PAGE_ID")

    body: dict[str, Any] = {
        "parent": {"type": "page_id", "page_id": parent_page_id},
        "title": [{"type": "text", "text": {"content": title}}],
    }
    if properties is not None:
        body["properties"] = _parse_json_arg(properties)
    if description is not None:
        body["description"] = _parse_json_arg(description)
    if is_inline is not None:
        body["is_inline"] = is_inline
    if icon is not None:
        body["icon"] = _parse_json_arg(icon)
    if cover is not None:
        body["cover"] = _parse_json_arg(cover)

    data = _request("POST", "/databases", json_body=body)
    _echo(data, pretty=ctx.obj["pretty"])


@databases.command("get")
@click.argument("database_id")
@click.pass_context
def databases_get(ctx: click.Context, database_id: str) -> None:
    data = _request("GET", f"/databases/{database_id}")
    _echo(data, pretty=ctx.obj["pretty"])


@databases.command("update")
@click.argument("database_id")
@click.option("--title", default=None, help="New database title (plain text)")
@click.option("--properties", default=None, help="JSON object of properties schema updates")
@click.option("--description", default=None, help="JSON rich_text array for description")
@click.option("--icon", default=None, help="JSON icon object")
@click.option("--cover", default=None, help="JSON cover object")
@click.pass_context
def databases_update(
    ctx: click.Context,
    database_id: str,
    title: Optional[str],
    properties: Optional[str],
    description: Optional[str],
    icon: Optional[str],
    cover: Optional[str],
) -> None:
    body: dict[str, Any] = {}
    if title is not None:
        body["title"] = [{"type": "text", "text": {"content": title}}]
    if properties is not None:
        body["properties"] = _parse_json_arg(properties)
    if description is not None:
        body["description"] = _parse_json_arg(description)
    if icon is not None:
        body["icon"] = _parse_json_arg(icon)
    if cover is not None:
        body["cover"] = _parse_json_arg(cover)

    if not body:
        raise NotionError("No updates provided")

    data = _request("PATCH", f"/databases/{database_id}", json_body=body)
    _echo(data, pretty=ctx.obj["pretty"])


@databases.command("query")
@click.argument("database_id")
@click.option("--filter", "filter_json", default=None, help="JSON filter object")
@click.option("--sorts", default=None, help="JSON array of sorts")
@click.option("--start-cursor", default=None, help="Pagination cursor")
@click.option("--page-size", type=int, default=None, help="Page size")
@click.option("--filter-properties", default=None, help="Comma-separated list of property IDs to include")
@click.pass_context
def databases_query(
    ctx: click.Context,
    database_id: str,
    filter_json: Optional[str],
    sorts: Optional[str],
    start_cursor: Optional[str],
    page_size: Optional[int],
    filter_properties: Optional[str],
) -> None:
    params: dict[str, Any] = {}
    if filter_properties:
        params["filter_properties"] = filter_properties

    body: dict[str, Any] = {}
    if filter_json is not None:
        body["filter"] = _parse_json_arg(filter_json)
    if sorts is not None:
        body["sorts"] = _parse_json_arg(sorts)
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size

    data = _request("POST", f"/databases/{database_id}/query", params=params or None, json_body=body or {})
    _echo(data, pretty=ctx.obj["pretty"])


@cli.group()
def blocks() -> None:
    """Block operations."""


@blocks.command("get")
@click.argument("block_id")
@click.pass_context
def blocks_get(ctx: click.Context, block_id: str) -> None:
    data = _request("GET", f"/blocks/{block_id}")
    _echo(data, pretty=ctx.obj["pretty"])


@blocks.command("children")
@click.argument("block_id")
@click.option("--start-cursor", default=None)
@click.option("--page-size", type=int, default=None)
@click.pass_context
def blocks_children(ctx: click.Context, block_id: str, start_cursor: Optional[str], page_size: Optional[int]) -> None:
    params: dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    data = _request("GET", f"/blocks/{block_id}/children", params=params or None)
    _echo(data, pretty=ctx.obj["pretty"])


@blocks.command("append")
@click.argument("block_id")
@click.option("--children", required=True, help="JSON array of block children")
@click.pass_context
def blocks_append(ctx: click.Context, block_id: str, children: str) -> None:
    body = {"children": _parse_json_arg(children)}
    data = _request("PATCH", f"/blocks/{block_id}/children", json_body=body)
    _echo(data, pretty=ctx.obj["pretty"])


@blocks.command("update")
@click.argument("block_id")
@click.option("--block", "block_json", required=True, help="JSON object of block fields to update")
@click.pass_context
def blocks_update(ctx: click.Context, block_id: str, block_json: str) -> None:
    data = _request("PATCH", f"/blocks/{block_id}", json_body=_parse_json_arg(block_json))
    _echo(data, pretty=ctx.obj["pretty"])


@blocks.command("delete")
@click.argument("block_id")
@click.pass_context
def blocks_delete(ctx: click.Context, block_id: str) -> None:
    data = _request("DELETE", f"/blocks/{block_id}")
    _echo(data, pretty=ctx.obj["pretty"])


@cli.group()
def comments() -> None:
    """Comment operations."""


@comments.command("create")
@click.option("--page-id", default=None, help="Page id to comment on")
@click.option("--discussion-id", default=None, help="Discussion id")
@click.option("--rich-text", required=True, help="JSON rich_text array")
@click.pass_context
def comments_create(ctx: click.Context, page_id: Optional[str], discussion_id: Optional[str], rich_text: str) -> None:
    if bool(page_id) == bool(discussion_id):
        raise NotionError("Provide exactly one of --page-id or --discussion-id")
    body: dict[str, Any] = {"rich_text": _parse_json_arg(rich_text)}
    if page_id:
        body["parent"] = {"page_id": page_id}
    else:
        body["discussion_id"] = discussion_id
    data = _request("POST", "/comments", json_body=body)
    _echo(data, pretty=ctx.obj["pretty"])


@comments.command("list")
@click.option("--block-id", default=None, help="Block id")
@click.option("--page-id", default=None, help="Page id")
@click.option("--discussion-id", default=None, help="Discussion id")
@click.option("--start-cursor", default=None)
@click.option("--page-size", type=int, default=None)
@click.pass_context
def comments_list(
    ctx: click.Context,
    block_id: Optional[str],
    page_id: Optional[str],
    discussion_id: Optional[str],
    start_cursor: Optional[str],
    page_size: Optional[int],
) -> None:
    provided = [x for x in (block_id, page_id, discussion_id) if x]
    if len(provided) != 1:
        raise NotionError("Provide exactly one of --block-id, --page-id, or --discussion-id")
    params: dict[str, Any] = {}
    if block_id:
        params["block_id"] = block_id
    if page_id:
        params["page_id"] = page_id
    if discussion_id:
        params["discussion_id"] = discussion_id
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    data = _request("GET", "/comments", params=params)
    _echo(data, pretty=ctx.obj["pretty"])


@cli.group()
def users() -> None:
    """User operations."""


@users.command("list")
@click.option("--start-cursor", default=None)
@click.option("--page-size", type=int, default=None)
@click.pass_context
def users_list(ctx: click.Context, start_cursor: Optional[str], page_size: Optional[int]) -> None:
    params: dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    data = _request("GET", "/users", params=params or None)
    _echo(data, pretty=ctx.obj["pretty"])


@users.command("get")
@click.argument("user_id")
@click.pass_context
def users_get(ctx: click.Context, user_id: str) -> None:
    data = _request("GET", f"/users/{user_id}")
    _echo(data, pretty=ctx.obj["pretty"])


@users.command("me")
@click.pass_context
def users_me(ctx: click.Context) -> None:
    data = _request("GET", "/users/me")
    _echo(data, pretty=ctx.obj["pretty"])


@cli.command("search")
@click.option("--query", default=None, help="Search query")
@click.option("--filter", "filter_json", default=None, help="JSON filter object")
@click.option("--sort", default=None, help="JSON sort object")
@click.option("--start-cursor", default=None)
@click.option("--page-size", type=int, default=None)
@click.pass_context
def search_cmd(
    ctx: click.Context,
    query: Optional[str],
    filter_json: Optional[str],
    sort: Optional[str],
    start_cursor: Optional[str],
    page_size: Optional[int],
) -> None:
    body: dict[str, Any] = {}
    if query is not None:
        body["query"] = query
    if filter_json is not None:
        body["filter"] = _parse_json_arg(filter_json)
    if sort is not None:
        body["sort"] = _parse_json_arg(sort)
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size

    data = _request("POST", "/search", json_body=body)
    _echo(data, pretty=ctx.obj["pretty"])


if __name__ == "__main__":
    cli()
