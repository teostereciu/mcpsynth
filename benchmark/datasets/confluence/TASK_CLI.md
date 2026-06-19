# Task: Build a CLI Tool for the Confluence Cloud REST API

## What You're Building

A command-line interface (CLI) tool that covers Confluence Cloud REST API functionality, suitable for use by an autonomous agent completing real-world tasks.

## What You Have

- **API documentation** in `docs/` — 47 markdown files covering both v1 and v2 Confluence Cloud REST APIs.
- **Environment variables** for authentication:
  - `CONFLUENCE_BASE_URL` — base URL including `/wiki` (e.g. `https://yoursite.atlassian.net/wiki`)
  - `CONFLUENCE_SPACE_KEY` — default space key (e.g. `SYNTH`)
  - `JIRA_EMAIL` — Atlassian account email
  - `JIRA_API_TOKEN` — Atlassian API token
- **Auth:** HTTP Basic Auth with email and API token.

## API Versions

Both v1 (`{CONFLUENCE_BASE_URL}/rest/api/`) and v2 (`{CONFLUENCE_BASE_URL}/api/v2/`) are available. Prefer v2 for pages and spaces where available.

## Coverage Expectations

Aim for broad coverage of the most important operations. Prioritize:
- Pages (create, get, update, delete, list children, move)
- Spaces (list, get, create)
- Search (CQL-based content search)
- Labels (add, list, remove)
- Comments (create and list footer comments)
- Versions (list, get specific version)
- Attachments (list, upload)
- Blog posts (create, get, update, delete)
- Current user (get profile)

## Technical Requirements

- **No generic passthrough commands**: do not expose a generic `request` or `api` command. Every command must correspond to a specific, named operation.

## Deliverables

- `confluence_cli.py` — the CLI tool entry point
- `requirements.txt` — pinned dependencies
