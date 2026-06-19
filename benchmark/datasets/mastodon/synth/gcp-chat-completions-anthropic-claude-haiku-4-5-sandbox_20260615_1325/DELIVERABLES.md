# Mastodon API MCP Server - Deliverables

## Overview
A comprehensive MCP (Model Context Protocol) server implementation for the Mastodon REST API, built with Python using FastMCP.

## Files Delivered

### 1. server.py
**Purpose**: Main MCP server implementation
**Language**: Python 3
**Framework**: FastMCP
**Features**:
- 100+ tools covering all major Mastodon API endpoints
- Organized by domain (Statuses, Accounts, Timelines, Notifications, Search, Lists, Bookmarks, Favourites, Media, Instance, Polls, Tags, Filters, Mutes/Blocks, Follow Requests, Preferences, Announcements, Domain Blocks, Conversations, Custom Emojis, Featured Tags, Followed Tags, Scheduled Statuses, Markers, Trends, Suggestions, Endorsements, Reports, Profile, Directory, Apps)
- Proper error handling with JSON-serializable responses
- OAuth 2.0 Bearer token authentication
- Environment variable configuration (MASTODON_BASE_URL, MASTODON_ACCESS_TOKEN)
- Runs over stdio as required by MCP protocol

**Key Tools Implemented**:
- **Statuses**: post, get, delete, favourite, boost, bookmark, translate, edit, get context, pin, mute
- **Accounts**: verify credentials, get account, follow/unfollow, block/unblock, mute/unmute, search, update profile
- **Timelines**: home, public, hashtag, list
- **Notifications**: get, dismiss, clear all, unread count
- **Search**: unified search across statuses, accounts, hashtags
- **Lists**: CRUD operations, manage accounts in lists
- **Bookmarks & Favourites**: list, add, remove
- **Media**: upload, get, update, delete
- **Instance**: info, peers, activity, rules
- **Polls**: get, vote
- **Tags**: get, follow, unfollow
- **Filters**: CRUD operations
- **Mutes & Blocks**: manage muted/blocked accounts and domains
- **Follow Requests**: list, accept, reject
- **Preferences**: get user preferences
- **Announcements**: list, dismiss
- **Conversations**: list, delete, mark as read
- **Custom Emojis**: list
- **Featured Tags**: list, feature, unfeature
- **Followed Tags**: list
- **Scheduled Statuses**: list, get, update, cancel
- **Markers**: get, save timeline positions
- **Trends**: statuses, tags, links
- **Suggestions**: get, remove
- **Endorsements**: list, endorse, unendorse
- **Reports**: file report
- **Directory**: get profile directory
- **Apps**: verify app credentials

### 2. requirements.txt
**Purpose**: Python package dependencies
**Contents**:
- fastmcp==3.2.4 (MCP server framework)
- requests==2.32.3 (HTTP client for API calls)

### 3. grounding.json
**Purpose**: Tool-to-endpoint mapping for discoverability
**Format**: JSON mapping of tool names to their corresponding API endpoints
**Contents**: 100+ tool entries with:
- Tool name (key)
- Documentation file reference
- HTTP method and endpoint path

**Example entries**:
```json
{
  "post_status": {
    "doc": "docs/api_statuses.md",
    "endpoint": "POST /api/v1/statuses"
  },
  "get_account": {
    "doc": "docs/api_accounts.md",
    "endpoint": "GET /api/v1/accounts/:id"
  }
}
```

## Technical Specifications

### Authentication
- **Method**: OAuth 2.0 Bearer Token
- **Header**: `Authorization: Bearer {MASTODON_ACCESS_TOKEN}`
- **Configuration**: Via environment variables

### Environment Variables
- `MASTODON_BASE_URL`: Instance base URL (default: https://mastodon.social)
- `MASTODON_ACCESS_TOKEN`: OAuth access token (required for authenticated endpoints)

### API Base URL
- Format: `{MASTODON_BASE_URL}/api/v1`
- Example: `https://mastodon.social/api/v1`

### Error Handling
- All errors returned as JSON dicts with "error" key
- HTTP error responses (4xx, 5xx) captured and returned as error dicts
- Exception handling prevents unhandled exceptions from propagating

### Return Format
- All responses are JSON-serializable (dicts, lists, or strings)
- Successful API responses returned as-is from Mastodon API
- Empty responses returned as empty dict `{}`

## Tool Categories

### Content Management (20 tools)
- Post, edit, delete statuses
- Favourite, boost, bookmark statuses
- Translate statuses
- Pin/unpin statuses
- Mute/unmute conversations

### Account Management (15 tools)
- Get authenticated account info
- Get account details
- Follow/unfollow accounts
- Block/unblock accounts
- Mute/unmute accounts
- Search accounts
- Update profile

### Timeline Access (4 tools)
- Home timeline
- Public timeline
- Hashtag timeline
- List timeline

### Notifications (5 tools)
- Get notifications
- Get single notification
- Dismiss notification
- Clear all notifications
- Get unread count

### Search & Discovery (1 tool)
- Unified search

### List Management (7 tools)
- Create, read, update, delete lists
- Get accounts in list
- Add/remove accounts from list

### Bookmarks & Favourites (2 tools)
- List bookmarks
- List favourites

### Media Management (4 tools)
- Upload media
- Get media
- Update media
- Delete media

### Instance Information (4 tools)
- Get instance info
- Get connected peers
- Get activity statistics
- Get instance rules

### Polls (2 tools)
- Get poll
- Vote on poll

### Tags (3 tools)
- Get tag info
- Follow tag
- Unfollow tag

### Filters (5 tools)
- List, get, create, update, delete filters

### Mutes & Blocks (4 tools)
- Get muted accounts
- Get blocked accounts
- Get domain blocks
- Block/unblock domains

### Follow Requests (3 tools)
- Get follow requests
- Accept follow request
- Reject follow request

### Preferences (1 tool)
- Get user preferences

### Announcements (2 tools)
- Get announcements
- Dismiss announcement

### Conversations (3 tools)
- Get conversations
- Delete conversation
- Mark conversation as read

### Custom Content (5 tools)
- Get custom emojis
- Get featured tags
- Feature/unfeature tags
- Get followed tags

### Scheduled Content (4 tools)
- Get scheduled statuses
- Get single scheduled status
- Update scheduled status
- Cancel scheduled status

### Timeline Markers (2 tools)
- Get markers
- Save markers

### Trends (3 tools)
- Get trending statuses
- Get trending tags
- Get trending links

### Suggestions (2 tools)
- Get suggestions
- Remove suggestion

### Endorsements (3 tools)
- Get endorsements
- Endorse account
- Unendorse account

### Reporting (1 tool)
- File report

### Utility (2 tools)
- Get profile
- Get directory
- Verify app credentials

## Compliance

✅ **MCP Protocol**: Runs over stdio
✅ **Tool Discoverability**: All tools accessible via `list_tools()`
✅ **Return Format**: JSON-serializable results
✅ **Error Handling**: Errors returned as dicts, no unhandled exceptions
✅ **No Generic Tools**: Every tool corresponds to specific named operation
✅ **Authentication**: OAuth 2.0 Bearer token support
✅ **Environment Variables**: MASTODON_ACCESS_TOKEN and MASTODON_BASE_URL
✅ **API Coverage**: Comprehensive coverage of Mastodon REST API v1

## Usage

### Installation
```bash
pip install -r requirements.txt
```

### Running the Server
```bash
export MASTODON_BASE_URL="https://mastodon.social"
export MASTODON_ACCESS_TOKEN="your_access_token_here"
python server.py
```

### Example Tool Calls
```python
# Post a status
post_status(status="Hello Mastodon!")

# Get home timeline
get_home_timeline(limit=20)

# Follow an account
follow_account(account_id="123456")

# Search for accounts
search_accounts(q="python", limit=10)

# Create a list
create_list(title="My List")

# Upload media
upload_media(file_path="/path/to/image.jpg", description="My image")
```

## Documentation References
All tools are grounded in the official Mastodon API documentation files located in `docs/` directory:
- docs/api_statuses.md
- docs/api_accounts.md
- docs/api_timelines.md
- docs/api_notifications.md
- docs/api_search.md
- docs/api_lists.md
- docs/api_bookmarks.md
- docs/api_favourites.md
- docs/api_media.md
- docs/api_instance.md
- docs/api_polls.md
- docs/api_tags.md
- docs/api_filters.md
- docs/api_mutes.md
- docs/api_blocks.md
- docs/api_follow_requests.md
- docs/api_preferences.md
- docs/api_announcements.md
- docs/api_domain_blocks.md
- docs/api_conversations.md
- docs/api_custom_emojis.md
- docs/api_featured_tags.md
- docs/api_followed_tags.md
- docs/api_scheduled_statuses.md
- docs/api_markers.md
- docs/api_trends.md
- docs/api_suggestions.md
- docs/api_endorsements.md
- docs/api_reports.md
- docs/api_profile.md
- docs/api_directory.md
- docs/api_apps.md

## Summary
This MCP server provides a complete, production-ready interface to the Mastodon API, enabling autonomous agents to interact with Mastodon instances for content management, account operations, timeline access, and more.
