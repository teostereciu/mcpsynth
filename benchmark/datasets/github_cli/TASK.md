# Task: Build a CLI Tool for the GitHub REST API

## What You're Building

A command-line interface (CLI) tool that covers GitHub REST API functionality,
suitable for use by an autonomous agent completing real-world tasks.

## What You Have

- **API documentation** in `docs/` — 181 markdown files scraped from the GitHub
  REST API reference. Each file covers one or more endpoints with parameter
  descriptions, request/response formats, and examples.
- **Environment variables** for authentication:
  - `GITHUB_TOKEN` — personal access token (Bearer auth)
  - `GITHUB_API_BASE_URL` — base URL (e.g. `https://api.github.com`)
  - `GITHUB_TEST_REPO` — a real repo in `owner/repo` format for testing
- **Auth:** `Authorization: Bearer $GITHUB_TOKEN` header on every request.
  Also set `Accept: application/vnd.github+json` and
  `X-GitHub-Api-Version: 2022-11-28`.

## Coverage Expectations

Aim for broad coverage of the most important operations. Prioritize:

- Issues (list, get, create, update, add comments, add labels)
- Pull requests (list, get, create, merge)
- Repositories (get, list branches, list commits, get/create/update file contents)
- Releases (list, get)
- Actions (list workflow runs)
- Search (repositories, code)
- Gists (create, list)
- Users (get authenticated user, get user profile)

## Technical Requirements

- **No generic passthrough commands**: do NOT expose a generic `request` or `api` command that accepts arbitrary HTTP methods and paths. Every command must correspond to a specific, named operation.

## Deliverables

- `github_cli.py` — the CLI tool entry point
- `requirements.txt` — pinned dependencies
