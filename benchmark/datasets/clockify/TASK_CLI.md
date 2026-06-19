# Task: Build a CLI Tool for the Clockify API

## What You're Building

A command-line interface (CLI) tool that covers Clockify time tracking API functionality, suitable for use by an autonomous agent completing real-world tasks.

## What You Have

- **API documentation** in `docs/` — 16 markdown files covering the Clockify API endpoints.
- **Environment variables** for authentication:
  - `CLOCKIFY_API_KEY` — API key
- **Base URL:** `https://api.clockify.me/api/v1`
- **Auth:** `X-Api-Key: YOUR_API_KEY` header on every request.

## Coverage Expectations

Aim for broad coverage of the most important operations. Prioritize:
- Current user (get profile)
- Workspaces (list, get)
- Projects (list, get, create, update, delete)
- Time entries (list, get, create, update, delete, stop running timer)
- Clients (list, create)
- Tags (list, create)
- Tasks within projects (list, create)
- Users in workspace (list)

## Technical Requirements

- **No generic passthrough commands**: do not expose a generic `request` command that accepts arbitrary HTTP methods and paths. Every command must correspond to a specific, named operation.

## Deliverables

- `clockify_cli.py` — the CLI tool entry point
- `requirements.txt` — pinned dependencies
