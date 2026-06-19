# Task: Build a CLI Tool for the Zulip API

## What You're Building

A command-line interface (CLI) tool that covers Zulip functionality, suitable
for use by an autonomous agent completing real-world tasks.

You have access to the full Zulip server source code in `source/`. Read it to
understand what operations are available, what parameters they accept, and how
the API is structured.

## What You Have

- **Full Zulip server source code** in `source/` — a Django application.
  Start with `zerver/urls.py` to discover available endpoints, then follow
  references into `zerver/views/` for parameter details.
- **Environment variables** for authentication:
  - `ZULIP_EMAIL` — bot or user email address
  - `ZULIP_API_KEY` — API key
  - `ZULIP_SITE` — your Zulip instance URL (e.g. `https://your-org.zulipchat.com`)
- **Base URL:** `{ZULIP_SITE}/api/v1`
- **Auth:** HTTP Basic Auth with email and API key

## Coverage Expectations

Aim for broad coverage of the most important operations. Prioritize:
- Messages (send, edit, delete, fetch, flags, history, reactions)
- Streams/channels (create, list, subscribe, update, topics)
- Users (profiles, presence, list)
- Scheduled messages, drafts, alert words

## Technical Requirements

- **No generic passthrough commands**: do NOT expose a generic `request` or `api` command that accepts arbitrary HTTP methods and paths. Every command must correspond to a specific, named operation.

## Deliverables

- `zulip_cli.py` — the CLI tool entry point
- `requirements.txt` — pinned dependencies
