# Task: Build a CLI Tool for the Mastodon API

## What You're Building

A command-line interface (CLI) tool that covers Mastodon functionality, suitable for use by an autonomous agent completing real-world tasks.

You have access to the full Mastodon server source code in `source/`. Read it to understand what operations are available, what parameters they accept, and how the API is structured.

## What You Have

- **Full Mastodon server source code** in `source/` — a Rails application.
  Start with `config/routes.rb` to discover available endpoints, then follow
  references into `app/controllers/api/` for parameter details.
- **Environment variables** for authentication:
  - `MASTODON_ACCESS_TOKEN` — OAuth access token
  - `MASTODON_BASE_URL` — instance base URL (e.g. `https://mastodon.social`)
- **API Base URL:** `{MASTODON_BASE_URL}/api/v1`
- **Auth:** OAuth 2.0 Bearer token:
  ```
  Authorization: Bearer YOUR_ACCESS_TOKEN
  ```

## Coverage Expectations

Aim for broad coverage of the most important operations. Prioritize:
- Statuses (post, get, delete, boost/reblog, favourite, get context/thread)
- Accounts (get authenticated account, get account by ID, follow, unfollow, get followers/following)
- Timelines (home, public, hashtag, list)
- Notifications (list, get, dismiss, clear all)
- Search (accounts, statuses, hashtags)
- Lists (create, read, update, delete; add/remove accounts)
- Bookmarks (list, add, remove)
- Favourites (list favourited statuses)
- Media (upload attachment)
- Instance (get info and statistics)

## Technical Requirements

- **No generic passthrough commands**: do not expose a generic `request` or `api` command. Every command must correspond to a specific, named operation.

## Deliverables

- `mastodon_cli.py` — the CLI tool entry point
- `requirements.txt` — pinned dependencies
