# Task: Build a CLI Tool for the Notion API

## What You're Building

A command-line interface (CLI) tool that covers Notion API functionality,
suitable for use by an autonomous agent completing real-world tasks.

## What You Have

- **API documentation** in `docs/` — 94 markdown files covering the full
  Notion API surface: pages, databases, blocks, comments, users, search,
  and more.
- **Environment variables** for authentication:
  - `NOTION_API_KEY` — integration token (Bearer auth)
  - `NOTION_PARENT_PAGE_ID` — a parent page the integration has access to
- **Base URL:** `https://api.notion.com/v1`
- **Auth:** `Authorization: Bearer $NOTION_API_KEY` header on every request.
  Also set `Notion-Version: 2022-06-28`.

## Coverage Expectations

Aim for broad coverage of the most important operations. Prioritize:

- Pages (create, retrieve, update, archive)
- Databases (create, query with filters/sorts, update schema)
- Blocks (retrieve children, append, update, delete)
- Comments (create, retrieve)
- Users (list, get)
- Search

## Technical Requirements

- **No generic passthrough commands**: do NOT expose a generic `request` or `api` command that accepts arbitrary HTTP methods and paths. Every command must correspond to a specific, named operation.

## Deliverables

- `notion_cli.py` — the CLI tool entry point
- `requirements.txt` — pinned dependencies
