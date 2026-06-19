# Task: Build a CLI Tool for the Forgejo/Codeberg API

## What You're Building

A command-line interface (CLI) tool that covers Forgejo REST API functionality, suitable for use by an autonomous agent completing real-world tasks. The tool will be tested against a Codeberg.org account.

## What You Have

- **API documentation** in `docs/` — 7 markdown files covering the Forgejo API endpoints.
- **Environment variables** for authentication:
  - `CODEBERG_TOKEN` — Forgejo API token
  - `CODEBERG_BASE_URL` — base URL (e.g. `https://codeberg.org`)
- **API Base URL:** `{CODEBERG_BASE_URL}/api/v1`
- **Auth:** `Authorization: token YOUR_TOKEN` header on every request.

## Coverage Expectations

Aim for broad coverage of the most important operations. Prioritize:
- Authenticated user (get profile)
- Repositories (list user repos, get, create, delete, fork, search)
- Issues (list, get, create, update, add comments, add labels)
- Pull requests (list, get, create)
- Branches (list, get, create)
- Releases (list, create, get)
- Organizations (list, get)
- Users (get by username, search)

## Technical Requirements

- **No generic passthrough commands**: do not expose a generic `request` or `api` command that accepts arbitrary HTTP methods and paths. Every command must correspond to a specific, named operation.

## Deliverables

- `forgejo_cli.py` — the CLI tool entry point
- `requirements.txt` — pinned dependencies
