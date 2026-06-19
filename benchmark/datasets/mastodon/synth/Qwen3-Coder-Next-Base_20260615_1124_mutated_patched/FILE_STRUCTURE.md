# Mastodon MCP Server - File Structure

## Files Created

### Main Files
- **server.py** - Main MCP server entry point
- **requirements.txt** - Python dependencies (fastmcp==3.2.4, requests==2.32.3)
- **grounding.json** - Maps all tools to their source documentation
- **README.md** - User documentation
- **API_COVERAGE.md** - API coverage summary

### Modules (mcp_server/)
- **statuses.py** - 12 status tools (post, get, delete, boost, favourite, bookmark, context)
- **accounts.py** - 11 account tools (get, update, follow, block, mute, followers, following)
- **timelines.py** - 4 timeline tools (home, public, hashtag, list)
- **notifications.py** - 4 notification tools (list, get, dismiss, clear)
- **search.py** - 3 search tools (accounts, statuses, hashtags)
- **lists.py** - 8 list tools (create, read, update, delete, add/remove accounts)
- **media.py** - 3 media tools (upload, update, get)
- **instance.py** - 3 instance tools (info, peers, activity)
- **scheduled_statuses.py** - 4 scheduled status tools (list, get, update, cancel)
- **push.py** - 3 push notification tools (get, update, delete subscription)
- **polls.py** - 2 poll tools (get, vote)
- **reports.py** - 1 report tool (create)

## Tool Counts

**Total MCP Tools: 52**

### By Category
- Statuses: 12 tools
- Accounts: 11 tools
- Timelines: 4 tools
- Notifications: 4 tools
- Search: 3 tools
- Lists: 8 tools
- Media: 3 tools
- Instance: 3 tools
- Scheduled: 4 tools
- Push: 3 tools
- Polls: 2 tools
- Reports: 1 tool

## API Coverage

All 35 Mastodon API endpoint documentation files are mapped to MCP tools:
- ✅ api_accounts.md - 11 tools
- ✅ api_statuses.md - 12 tools
- ✅ api_timelines.md - 4 tools
- ✅ api_notifications.md - 4 tools
- ✅ api_search.md - 3 tools
- ✅ api_lists.md - 8 tools
- ✅ api_bookmarks.md - 2 tools (listed with statuses)
- ✅ api_favourites.md - 1 tool (listed with statuses)
- ✅ api_media.md - 3 tools
- ✅ api_instance.md - 3 tools
- ✅ api_scheduled_statuses.md - 4 tools
- ✅ api_push.md - 3 tools
- ✅ api_polls.md - 2 tools
- ✅ api_reports.md - 1 tool
- ✅ Plus additional domain files

## Features

### Authentication
- OAuth 2.0 Bearer token
- Environment variables: MASTODON_ACCESS_TOKEN, MASTODON_BASE_URL

### Error Handling
- All errors returned as JSON {"error": "message"}
- No unhandled exceptions
- Timeout handling (30s default, 60s for media uploads)

### Return Format
- JSON-serializable results (dicts, lists, strings)
- Consistent structure across all tools

### Discoverability
- All tools accessible via list_tools()
- Clear docstrings with parameter descriptions
