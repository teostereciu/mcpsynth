# Mastodon MCP Server

Mastodon MCP Server - An MCP server with comprehensive coverage of the Mastodon REST API.

## Configuration

### Environment Variables

The server requires the following environment variables:

- `MASTODON_ACCESS_TOKEN` - OAuth access token
- `MASTODON_BASE_URL` - Instance base URL (e.g., `https://mastodon.social`)

### API Base URL

The default API base URL is `{MASTODON_BASE_URL}/api/v1`

## Authentication

Mastodon API uses OAuth 2.0 Bearer token authentication:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Features

This MCP server provides tools for all major Mastodon functionality:

### Statuses
- Post a new status
- Get, delete, boost, favourite, bookmark a status
- View status context/thread
- List favourites and bookmarks

### Accounts
- Get authenticated account
- Get account by ID
- Follow, unfollow, block, mute an account
- Get followers/following

### Timelines
- Home timeline
- Public timeline (local/remote)
- Hashtag timeline
- List timeline

### Notifications
- List, get, dismiss, clear notifications

### Search
- Search for accounts, statuses, hashtags

### Lists
- Create, read, update, delete lists
- Add/remove accounts from lists

### Bookmarks
- List, add, remove bookmarks

### Favourites
- List favourited statuses

### Media
- Upload media attachment (for use in statuses)

### Instance
- Get instance info and statistics

### Scheduled Statuses
- List, get, update, cancel scheduled statuses

### Push Notifications
- Get, update, delete push subscription

### Polls
- Get poll information
- Vote on polls

### Reports
- Create reports with optional status attachments and comments

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set the required environment variables:
```bash
export MASTODON_ACCESS_TOKEN="your_token_here"
export MASTODON_BASE_URL="https://mastodon.social"
```

4. Run the server:
```bash
python server.py
```

## Running as MCP Server

The server runs over stdio and can be used by any MCP-compatible client:

```bash
python server.py --transport stdio
```

## API Coverage

| Module | Tools | Coverage |
|--------|-------|----------|
| Statuses | 10 | Post, Get, Delete, Boost, Favourite, Bookmark, Context |
| Accounts | 11 | Verify, Update, Get, Follow, Block, Mute, Followers, Following |
| Timelines | 4 | Home, Public, Hashtag, List |
| Notifications | 3 | List, Get, Dismiss, Clear |
| Search | 3 | Accounts, Statuses, Hashtags |
| Lists | 7 | Create, Read, Update, Delete, Add/Remove Accounts |
| Media | 3 | Upload, Update, Get |
| Instance | 3 | Info, Peers, Activity |

## Grounding

All tools are documented in `grounding.json` with links to their source API documentation.
