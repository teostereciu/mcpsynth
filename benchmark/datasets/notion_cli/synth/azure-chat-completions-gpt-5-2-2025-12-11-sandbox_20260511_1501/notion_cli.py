#!/usr/bin/env python3
"""Notion CLI

Environment:
  NOTION_API_KEY (required)
  NOTION_PARENT_PAGE_ID (optional; used as default parent for page/db create)

Base URL: https://api.notion.com/v1
Headers:
  Authorization: Bearer <token>
  Notion-Version: 2022-06-28

This CLI focuses on the most common Notion operations: pages, databases, blocks,
comments, users, and search.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any, Dict, Optional

import requests

BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"


class NotionError(RuntimeError):
    pass


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.environ.get(name)
    return v if v not in (None, "") else default


def _headers() -> Dict[str, str]:
    token = _env("NOTION_API_KEY")
    if not token:
        raise NotionError("NOTION_API_KEY is required")
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def _request(method: str, path: str, *, params: Dict[str, Any] | None = None, json_body: Any | None = None) -> Any:
    url = BASE_URL + path
    resp = requests.request(method, url, headers=_headers(), params=params, json=json_body, timeout=60)
    if resp.status_code >= 400:
        try:
            detail = resp.json()
        except Exception:
            detail = resp.text
        raise NotionError(f"HTTP {resp.status_code} {method} {path}: {detail}")
    if resp.status_code == 204:
        return None
    return resp.json()


def _print(obj: Any, *, pretty: bool = True) -> None:
    if pretty:
        json.dump(obj, sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
    else:
        json.dump(obj, sys.stdout, ensure_ascii=False)
        sys.stdout.write("\n")


def _load_json_arg(s: str) -> Any:
    """Load JSON from a string or @file.json."""
    if s.startswith("@"):
        with open(s[1:], "r", encoding="utf-8") as f:
            return json.load(f)
    return json.loads(s)


# -------------------- Pages --------------------

def pages_create(args: argparse.Namespace) -> None:
    parent: Dict[str, Any]
    if args.parent_page_id:
        parent = {"type": "page_id", "page_id": args.parent_page_id}
    elif args.parent_data_source_id:
        parent = {"type": "data_source_id", "data_source_id": args.parent_data_source_id}
    else:
        default_parent = _env("NOTION_PARENT_PAGE_ID")
        if not default_parent:
            raise NotionError("Provide --parent-page-id or --parent-data-source-id, or set NOTION_PARENT_PAGE_ID")
        parent = {"type": "page_id", "page_id": default_parent}

    properties = _load_json_arg(args.properties_json)
    body: Dict[str, Any] = {"parent": parent, "properties": properties}

    if args.children_json and args.markdown:
        raise NotionError("--children-json and --markdown are mutually exclusive")
    if args.children_json:
        body["children"] = _load_json_arg(args.children_json)
    if args.markdown:
        body["markdown"] = args.markdown

    res = _request("POST", "/pages", json_body=body)
    _print(res, pretty=not args.compact)


def pages_get(args: argparse.Namespace) -> None:
    params: Dict[str, Any] = {}
    if args.filter_properties:
        params["filter_properties"] = args.filter_properties
    res = _request("GET", f"/pages/{args.page_id}", params=params or None)
    _print(res, pretty=not args.compact)


def pages_update(args: argparse.Namespace) -> None:
    body: Dict[str, Any] = {}
    if args.properties_json:
        body["properties"] = _load_json_arg(args.properties_json)
    if args.icon_json:
        body["icon"] = _load_json_arg(args.icon_json)
    if args.cover_json:
        body["cover"] = _load_json_arg(args.cover_json)
    if args.in_trash is not None:
        body["in_trash"] = args.in_trash
    if args.archived is not None:
        body["archived"] = args.archived

    if not body:
        raise NotionError("No updates provided")

    res = _request("PATCH", f"/pages/{args.page_id}", json_body=body)
    _print(res, pretty=not args.compact)


def pages_property_get(args: argparse.Namespace) -> None:
    params: Dict[str, Any] = {}
    if args.start_cursor:
        params["start_cursor"] = args.start_cursor
    if args.page_size:
        params["page_size"] = args.page_size
    res = _request("GET", f"/pages/{args.page_id}/properties/{args.property_id}", params=params or None)
    _print(res, pretty=not args.compact)


def pages_move(args: argparse.Namespace) -> None:
    parent: Dict[str, Any]
    if args.parent_page_id:
        parent = {"type": "page_id", "page_id": args.parent_page_id}
    elif args.parent_data_source_id:
        parent = {"type": "data_source_id", "data_source_id": args.parent_data_source_id}
    else:
        raise NotionError("Provide --parent-page-id or --parent-data-source-id")

    res = _request("POST", f"/pages/{args.page_id}/move", json_body={"parent": parent})
    _print(res, pretty=not args.compact)


# -------------------- Databases --------------------

def databases_create(args: argparse.Namespace) -> None:
    parent_page_id = args.parent_page_id or _env("NOTION_PARENT_PAGE_ID")
    if not parent_page_id:
        raise NotionError("Provide --parent-page-id or set NOTION_PARENT_PAGE_ID")

    title = _load_json_arg(args.title_json)
    properties = _load_json_arg(args.properties_json)

    body = {
        "parent": {"type": "page_id", "page_id": parent_page_id},
        "title": title,
        "properties": properties,
    }
    if args.icon_json:
        body["icon"] = _load_json_arg(args.icon_json)
    if args.cover_json:
        body["cover"] = _load_json_arg(args.cover_json)

    res = _request("POST", "/databases", json_body=body)
    _print(res, pretty=not args.compact)


def databases_get(args: argparse.Namespace) -> None:
    res = _request("GET", f"/databases/{args.database_id}")
    _print(res, pretty=not args.compact)


def databases_list(args: argparse.Namespace) -> None:
    params: Dict[str, Any] = {}
    if args.start_cursor:
        params["start_cursor"] = args.start_cursor
    if args.page_size:
        params["page_size"] = args.page_size
    res = _request("GET", "/databases", params=params or None)
    _print(res, pretty=not args.compact)


def databases_update(args: argparse.Namespace) -> None:
    body: Dict[str, Any] = {}
    if args.title_json:
        body["title"] = _load_json_arg(args.title_json)
    if args.properties_json:
        body["properties"] = _load_json_arg(args.properties_json)
    if args.icon_json:
        body["icon"] = _load_json_arg(args.icon_json)
    if args.cover_json:
        body["cover"] = _load_json_arg(args.cover_json)
    if args.is_inline is not None:
        body["is_inline"] = args.is_inline

    if not body:
        raise NotionError("No updates provided")

    res = _request("PATCH", f"/databases/{args.database_id}", json_body=body)
    _print(res, pretty=not args.compact)


def databases_query(args: argparse.Namespace) -> None:
    body: Dict[str, Any] = {}
    if args.filter_json:
        body["filter"] = _load_json_arg(args.filter_json)
    if args.sorts_json:
        body["sorts"] = _load_json_arg(args.sorts_json)
    if args.start_cursor:
        body["start_cursor"] = args.start_cursor
    if args.page_size:
        body["page_size"] = args.page_size

    params: Dict[str, Any] = {}
    if args.filter_properties:
        params["filter_properties"] = args.filter_properties

    res = _request("POST", f"/databases/{args.database_id}/query", params=params or None, json_body=body or {})
    _print(res, pretty=not args.compact)


# -------------------- Blocks --------------------

def blocks_get(args: argparse.Namespace) -> None:
    res = _request("GET", f"/blocks/{args.block_id}")
    _print(res, pretty=not args.compact)


def blocks_delete(args: argparse.Namespace) -> None:
    res = _request("DELETE", f"/blocks/{args.block_id}")
    _print(res, pretty=not args.compact)


def blocks_update(args: argparse.Namespace) -> None:
    body = _load_json_arg(args.block_json)
    res = _request("PATCH", f"/blocks/{args.block_id}", json_body=body)
    _print(res, pretty=not args.compact)


def blocks_children_list(args: argparse.Namespace) -> None:
    params: Dict[str, Any] = {}
    if args.start_cursor:
        params["start_cursor"] = args.start_cursor
    if args.page_size:
        params["page_size"] = args.page_size
    res = _request("GET", f"/blocks/{args.block_id}/children", params=params or None)
    _print(res, pretty=not args.compact)


def blocks_children_append(args: argparse.Namespace) -> None:
    body: Dict[str, Any] = {"children": _load_json_arg(args.children_json)}
    if args.after:
        body["after"] = args.after
    res = _request("PATCH", f"/blocks/{args.block_id}/children", json_body=body)
    _print(res, pretty=not args.compact)


# -------------------- Comments --------------------

def comments_create(args: argparse.Namespace) -> None:
    parent: Dict[str, Any]
    if args.page_id:
        parent = {"page_id": args.page_id}
    elif args.block_id:
        parent = {"block_id": args.block_id}
    else:
        raise NotionError("Provide --page-id or --block-id")

    rich_text = _load_json_arg(args.rich_text_json)
    body = {"parent": parent, "rich_text": rich_text}
    res = _request("POST", "/comments", json_body=body)
    _print(res, pretty=not args.compact)


def comments_get(args: argparse.Namespace) -> None:
    res = _request("GET", f"/comments/{args.comment_id}")
    _print(res, pretty=not args.compact)


def comments_list(args: argparse.Namespace) -> None:
    params: Dict[str, Any] = {}
    if args.block_id:
        params["block_id"] = args.block_id
    if args.page_id:
        params["page_id"] = args.page_id
    if args.start_cursor:
        params["start_cursor"] = args.start_cursor
    if args.page_size:
        params["page_size"] = args.page_size
    res = _request("GET", "/comments", params=params or None)
    _print(res, pretty=not args.compact)


# -------------------- Users --------------------

def users_list(args: argparse.Namespace) -> None:
    params: Dict[str, Any] = {}
    if args.start_cursor:
        params["start_cursor"] = args.start_cursor
    if args.page_size:
        params["page_size"] = args.page_size
    res = _request("GET", "/users", params=params or None)
    _print(res, pretty=not args.compact)


def users_get(args: argparse.Namespace) -> None:
    res = _request("GET", f"/users/{args.user_id}")
    _print(res, pretty=not args.compact)


def users_me(args: argparse.Namespace) -> None:
    res = _request("GET", "/users/me")
    _print(res, pretty=not args.compact)


# -------------------- Search --------------------

def search(args: argparse.Namespace) -> None:
    body: Dict[str, Any] = {}
    if args.query is not None:
        body["query"] = args.query
    if args.sort_json:
        body["sort"] = _load_json_arg(args.sort_json)
    if args.filter_json:
        body["filter"] = _load_json_arg(args.filter_json)
    if args.start_cursor:
        body["start_cursor"] = args.start_cursor
    if args.page_size:
        body["page_size"] = args.page_size

    res = _request("POST", "/search", json_body=body)
    _print(res, pretty=not args.compact)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="notion", description="Notion API CLI")
    p.add_argument("--compact", action="store_true", help="Print compact JSON")

    sub = p.add_subparsers(dest="cmd", required=True)

    # pages
    pages = sub.add_parser("pages", help="Pages operations")
    pages_sub = pages.add_subparsers(dest="subcmd", required=True)

    pc = pages_sub.add_parser("create", help="Create a page")
    pc.add_argument("--parent-page-id")
    pc.add_argument("--parent-data-source-id")
    pc.add_argument("--properties-json", required=True, help='JSON string or @file.json for page properties')
    pc.add_argument("--children-json", help='JSON string or @file.json for children blocks')
    pc.add_argument("--markdown", help="Notion-flavored Markdown content (mutually exclusive with --children-json)")
    pc.set_defaults(func=pages_create)

    pg = pages_sub.add_parser("get", help="Retrieve a page")
    pg.add_argument("page_id")
    pg.add_argument("--filter-properties", nargs="*", help="Property IDs to include")
    pg.set_defaults(func=pages_get)

    pu = pages_sub.add_parser("update", help="Update a page")
    pu.add_argument("page_id")
    pu.add_argument("--properties-json", help='JSON string or @file.json')
    pu.add_argument("--icon-json", help='JSON string or @file.json')
    pu.add_argument("--cover-json", help='JSON string or @file.json')
    pu.add_argument("--in-trash", type=lambda s: s.lower() == "true", choices=[True, False])
    pu.add_argument("--archived", type=lambda s: s.lower() == "true", choices=[True, False])
    pu.set_defaults(func=pages_update)

    pp = pages_sub.add_parser("property", help="Retrieve a page property item")
    pp.add_argument("page_id")
    pp.add_argument("property_id")
    pp.add_argument("--start-cursor")
    pp.add_argument("--page-size", type=int)
    pp.set_defaults(func=pages_property_get)

    pm = pages_sub.add_parser("move", help="Move a page")
    pm.add_argument("page_id")
    pm.add_argument("--parent-page-id")
    pm.add_argument("--parent-data-source-id")
    pm.set_defaults(func=pages_move)

    # databases
    db = sub.add_parser("databases", help="Databases operations")
    db_sub = db.add_subparsers(dest="subcmd", required=True)

    dbc = db_sub.add_parser("create", help="Create a database")
    dbc.add_argument("--parent-page-id")
    dbc.add_argument("--title-json", required=True, help='JSON string or @file.json (array of rich_text objects)')
    dbc.add_argument("--properties-json", required=True, help='JSON string or @file.json')
    dbc.add_argument("--icon-json")
    dbc.add_argument("--cover-json")
    dbc.set_defaults(func=databases_create)

    dbg = db_sub.add_parser("get", help="Retrieve a database")
    dbg.add_argument("database_id")
    dbg.set_defaults(func=databases_get)

    dbl = db_sub.add_parser("list", help="List databases")
    dbl.add_argument("--start-cursor")
    dbl.add_argument("--page-size", type=int)
    dbl.set_defaults(func=databases_list)

    dbu = db_sub.add_parser("update", help="Update a database")
    dbu.add_argument("database_id")
    dbu.add_argument("--title-json")
    dbu.add_argument("--properties-json")
    dbu.add_argument("--icon-json")
    dbu.add_argument("--cover-json")
    dbu.add_argument("--is-inline", type=lambda s: s.lower() == "true", choices=[True, False])
    dbu.set_defaults(func=databases_update)

    dbq = db_sub.add_parser("query", help="Query a database")
    dbq.add_argument("database_id")
    dbq.add_argument("--filter-json")
    dbq.add_argument("--sorts-json")
    dbq.add_argument("--start-cursor")
    dbq.add_argument("--page-size", type=int)
    dbq.add_argument("--filter-properties", nargs="*")
    dbq.set_defaults(func=databases_query)

    # blocks
    bl = sub.add_parser("blocks", help="Blocks operations")
    bl_sub = bl.add_subparsers(dest="subcmd", required=True)

    bg = bl_sub.add_parser("get", help="Retrieve a block")
    bg.add_argument("block_id")
    bg.set_defaults(func=blocks_get)

    bd = bl_sub.add_parser("delete", help="Delete a block")
    bd.add_argument("block_id")
    bd.set_defaults(func=blocks_delete)

    bu = bl_sub.add_parser("update", help="Update a block")
    bu.add_argument("block_id")
    bu.add_argument("--block-json", required=True, help='JSON string or @file.json for PATCH body')
    bu.set_defaults(func=blocks_update)

    bcl = bl_sub.add_parser("children", help="List block children")
    bcl.add_argument("block_id")
    bcl.add_argument("--start-cursor")
    bcl.add_argument("--page-size", type=int)
    bcl.set_defaults(func=blocks_children_list)

    bca = bl_sub.add_parser("append", help="Append block children")
    bca.add_argument("block_id")
    bca.add_argument("--children-json", required=True, help='JSON string or @file.json (array of blocks)')
    bca.add_argument("--after", help="Append after a specific block_id")
    bca.set_defaults(func=blocks_children_append)

    # comments
    cm = sub.add_parser("comments", help="Comments operations")
    cm_sub = cm.add_subparsers(dest="subcmd", required=True)

    ccc = cm_sub.add_parser("create", help="Create a comment")
    ccc.add_argument("--page-id")
    ccc.add_argument("--block-id")
    ccc.add_argument("--rich-text-json", required=True, help='JSON string or @file.json (array of rich_text objects)')
    ccc.set_defaults(func=comments_create)

    ccg = cm_sub.add_parser("get", help="Retrieve a comment")
    ccg.add_argument("comment_id")
    ccg.set_defaults(func=comments_get)

    ccl = cm_sub.add_parser("list", help="List comments")
    ccl.add_argument("--block-id")
    ccl.add_argument("--page-id")
    ccl.add_argument("--start-cursor")
    ccl.add_argument("--page-size", type=int)
    ccl.set_defaults(func=comments_list)

    # users
    us = sub.add_parser("users", help="Users operations")
    us_sub = us.add_subparsers(dest="subcmd", required=True)

    ul = us_sub.add_parser("list", help="List users")
    ul.add_argument("--start-cursor")
    ul.add_argument("--page-size", type=int)
    ul.set_defaults(func=users_list)

    ug = us_sub.add_parser("get", help="Retrieve a user")
    ug.add_argument("user_id")
    ug.set_defaults(func=users_get)

    ume = us_sub.add_parser("me", help="Retrieve bot user")
    ume.set_defaults(func=users_me)

    # search
    se = sub.add_parser("search", help="Search")
    se.add_argument("--query")
    se.add_argument("--sort-json")
    se.add_argument("--filter-json")
    se.add_argument("--start-cursor")
    se.add_argument("--page-size", type=int)
    se.set_defaults(func=search)

    return p


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        args.func(args)
        return 0
    except NotionError as e:
        sys.stderr.write(str(e) + "\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
