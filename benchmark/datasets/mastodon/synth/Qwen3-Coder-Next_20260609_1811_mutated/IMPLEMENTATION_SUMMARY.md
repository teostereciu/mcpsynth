# Mastodon MCP Server - Implementation Summary

## Overview
A comprehensive Model Context Protocol (MCP) server implementing the Mastodon REST API, suitable for use by autonomous agents.

## Files Created

### 1. server.py
- Main MCP server implementation using FastMCP
- 65+ tools covering all Mastodon API domains:
  - **Status Operations**: post, get, delete, reblog, favourite, bookmark, context, translate, pin, mute
  - **Account Operations**: verify credentials, update, get, follow, block, mute, pin, endorse, relationships
  - **Timeline Operations**: home, public, hashtag, list timelines
  - **Notification Operations**: list, get, clear, dismiss, unread count
  - **Search**: comprehensive search functionality
  - **List Operations**: CRUD operations for user-defined lists
  - **Bookmark/Favourite Operations**: list your bookmarks and favourites
  - **Media Operations**: upload media attachments
  - **Instance Operations**: get server information
  - **Follow Request Operations**: accept/reject follow requests
  - **Conversation Operations**: list, remove, mark read
  - **Suggestion Operations**: view and remove follow suggestions
  - **Block Operations**: list blocked accounts
  - **Domain Block Operations**: block/unblock domains

### 2. grounding.json
- Maps every tool to its source documentation
- Contains 65+ entries in the format:
  ```json
  {
    "tool_name": {
      "doc": "docs/api_*.md",
      "endpoint": "HTTP_METHOD /api/v1/endpoint"
    }
  }
  ```

### 3. requirements.txt
- Python dependencies with pinned versions:
  - fastmcp==3.2.4
  - requests==2.32.3
  - python-dotenv==1.0.1

### 4. package.json
- Node.js configuration for the project
- Includes start and validate scripts

### 5. .env.example
- Example environment variables for configuration:
  - MASTODON_ACCESS_TOKEN
  - MASTODON_BASE_URL

### 6. validate.py
- Validation script for grounding.json

## API Coverage

### Statuses
- ✅ POST /api/v1/statuses - Post a new status
- ✅ GET /api/v1/statuses/:id - View a status
- ✅ DELETE /api/v1/statuses/:id - Delete a status
- ✅ POST /api/v1/statuses/:id/reblog - Boost a status
- ✅ POST /api/v1/statuses/:id/unreblog - Undo boost
- ✅ POST /api/v1/statuses/:id/favourite - Favourite a status
- ✅ POST /api/v1/statuses/:id/unfavourite - Undo favourite
- ✅ POST /api/v1/statuses/:id/bookmark - Bookmark a status
- ✅ POST /api/v1/statuses/:id/unbookmark - Undo bookmark
- ✅ GET /api/v1/statuses/:id/context - Get thread context
- ✅ POST /api/v1/statuses/:id/translate - Translate status
- ✅ POST /api/v1/statuses/:id/pin - Pin a status
- ✅ POST /api/v1/statuses/:id/unpin - Unpin a status
- ✅ POST /api/v1/statuses/:id/mute - Mute a status
- ✅ POST /api/v1/statuses/:id/unmute - Unmute a status

### Accounts
- ✅ GET /api/v1/accounts/verify_credentials - Verify credentials
- ✅ PATCH /api/v1/accounts/update_credentials - Update profile
- ✅ GET /api/v1/accounts/:id - Get account info
- ✅ GET /api/v1/accounts/:id/statuses - Get account posts
- ✅ POST /api/v1/accounts/:id/follow - Follow an account
- ✅ POST /api/v1/accounts/:id/unfollow - Unfollow an account
- ✅ POST /api/v1/accounts/:id/block - Block an account
- ✅ POST /api/v1/accounts/:id/unblock - Unblock an account
- ✅ POST /api/v1/accounts/:id/mute - Mute an account
- ✅ POST /api/v1/accounts/:id/unmute - Unmute an account
- ✅ POST /api/v1/accounts/:id/pin - Pin an account
- ✅ POST /api/v1/accounts/:id/unpin - Unpin an account
- ✅ POST /api/v1/accounts/:id/endorse - Endorse an account
- ✅ POST /api/v1/accounts/:id/unendorse - Unendorse an account
- ✅ POST /api/v1/accounts/:id/note - Add a note
- ✅ GET /api/v1/accounts/relationships - Get relationships
- ✅ GET /api/v1/accounts/:id/followers - Get followers
- ✅ GET /api/v1/accounts/:id/following - Get following
- ✅ GET /api/v1/accounts/search - Search accounts

### Timelines
- ✅ GET /api/v1/timelines/home - Home timeline
- ✅ GET /api/v1/timelines/public - Public timeline
- ✅ GET /api/v1/timelines/tag/:hashtag - Hashtag timeline
- ✅ GET /api/v1/timelines/list/:list_id - List timeline

### Notifications
- ✅ GET /api/v1/notifications - List notifications
- ✅ GET /api/v1/notifications/:id - Get notification
- ✅ POST /api/v1/notifications/clear - Clear all
- ✅ POST /api/v1/notifications/:id/dismiss - Dismiss one
- ✅ GET /api/v1/notifications/unread_count - Get unread count

### Search
- ✅ GET /api/v2/search - Comprehensive search

### Lists
- ✅ GET /api/v1/lists - Get lists
- ✅ GET /api/v1/lists/:id - Get list
- ✅ POST /api/v1/lists - Create list
- ✅ PUT /api/v1/lists/:id - Update list
- ✅ DELETE /api/v1/lists/:id - Delete list
- ✅ GET /api/v1/lists/:id/accounts - Get list accounts
- ✅ POST /api/v1/lists/:id/accounts - Add accounts
- ✅ DELETE /api/v1/lists/:id/accounts - Remove accounts

### Bookmarks & Favourites
- ✅ GET /api/v1/bookmarks - Get bookmarks
- ✅ GET /api/v1/favourites - Get favourites

### Media
- ✅ POST /api/v2/media - Upload media

### Instance
- ✅ GET /api/v2/instance - Get server info

### Follow Requests
- ✅ GET /api/v1/follow_requests - Get pending requests
- ✅ POST /api/v1/follow_requests/:account_id/authorize - Accept
- ✅ POST /api/v1/follow_requests/:account_id/reject - Reject

### Conversations
- ✅ GET /api/v1/conversations - Get conversations
- ✅ DELETE /api/v1/conversations/:id - Remove conversation
- ✅ POST /api/v1/conversations/:id/read - Mark as read

### Suggestions
- ✅ GET /api/v2/suggestions - Get suggestions
- ✅ DELETE /api/v1/suggestions/:account_id - Remove suggestion

### Blocks
- ✅ GET /api/v1/blocks - Get blocked accounts

### Domain Blocks
- ✅ GET /api/v1/domain_blocks - Get domain blocks
- ✅ POST /api/v1/domain_blocks - Block domain
- ✅ DELETE /api/v1/domain_blocks - Unblock domain

## Technical Features

### Error Handling
- All API errors are returned as JSON objects with "error" key
- Handles 401 (Unauthorized), 404 (Not Found), 422 (Validation) errors
- No unhandled exceptions raised to MCP protocol

### Authentication
- OAuth 2.0 Bearer token authentication
- Environment variables for credentials:
  - MASTODON_ACCESS_TOKEN
  - MASTODON_BASE_URL

### Pagination
- Supports max_id, since_id, min_id for cursor-based pagination
- Limit parameter for result count control

### Return Format
- All tools return JSON-serializable results (dicts, lists, or strings)
- Error responses are consistently formatted

## Running the Server

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

3. Run the server:
   ```bash
   python3 server.py
   ```

## Integration with MCP

The server exposes all tools via the `list_tools()` endpoint and can be consumed by any MCP-compatible client. Tools are discoverable and include comprehensive docstrings.
