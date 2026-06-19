# Mastodon API MCP Server

A comprehensive Model Context Protocol (MCP) server implementation for the Mastodon REST API, enabling autonomous agents to interact with Mastodon instances.

## Features

- **100+ Tools**: Complete coverage of Mastodon API endpoints including:
  - Accounts: authentication, profile management, relationships
  - Statuses: posting, editing, deleting, interactions (boost, favourite, bookmark)
  - Timelines: home, public, hashtag, list timelines
  - Notifications: retrieval, dismissal, filtering
  - Search: accounts, statuses, hashtags
  - Lists: creation, management, member operations
  - Media: upload, retrieval, updates
  - Conversations: direct messages and threads
  - Follow requests: accept/reject
  - Blocks & Mutes: account and domain management
  - Filters: content filtering
  - Polls: voting
  - Tags: following, featuring, trending
  - Trends: trending tags, statuses, links
  - Suggestions: follow recommendations
  - Instance: server information
  - And more...

- **OAuth 2.0 Authentication**: Secure Bearer token authentication
- **Error Handling**: Graceful error responses without exceptions
- **Pagination Support**: Built-in support for paginated results
- **JSON Responses**: All results returned as JSON-serializable dicts

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone or download this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set environment variables:
```bash
export MASTODON_BASE_URL="https://mastodon.social"
export MASTODON_ACCESS_TOKEN="your_oauth_token_here"
```

## Usage

### Running the Server

```bash
python server.py
```

The server will start and listen on stdio for MCP protocol messages.

### Environment Variables

- `MASTODON_BASE_URL`: The base URL of your Mastodon instance (default: `https://mastodon.social`)
- `MASTODON_ACCESS_TOKEN`: Your OAuth 2.0 access token for authentication

### Example Tool Calls

#### Get authenticated user's account
```python
get_account_credentials()
```

#### Post a status
```python
post_status(
    status="Hello Mastodon!",
    visibility="public",
    sensitive=False
)
```

#### Get home timeline
```python
get_home_timeline(limit=20)
```

#### Search for accounts
```python
search_accounts(q="mastodon", limit=10)
```

#### Create a list
```python
create_list(title="Friends", replies_policy="list")
```

#### Upload media
```python
upload_media(
    file_path="/path/to/image.jpg",
    description="My image"
)
```

## Tool Categories

### Accounts (14 tools)
- `get_account_credentials` - Get authenticated user info
- `update_account_credentials` - Update profile
- `get_account` - Get account by ID
- `get_account_statuses` - Get account's posts
- `get_account_followers` - Get followers
- `get_account_following` - Get following
- `follow_account` - Follow an account
- `unfollow_account` - Unfollow
- `block_account` - Block account
- `unblock_account` - Unblock
- `mute_account` - Mute account
- `unmute_account` - Unmute
- `get_account_relationships` - Check relationships
- `search_accounts` - Search accounts

### Statuses (13 tools)
- `post_status` - Create new status
- `get_status` - Get status by ID
- `delete_status` - Delete status
- `get_status_context` - Get thread context
- `favourite_status` - Favourite
- `unfavourite_status` - Unfavourite
- `boost_status` - Reblog/boost
- `unboost_status` - Undo reblog
- `bookmark_status` - Bookmark
- `unbookmark_status` - Unbookmark
- `pin_status` - Pin to profile
- `unpin_status` - Unpin
- `edit_status` - Edit status

### Timelines (4 tools)
- `get_home_timeline` - Home feed
- `get_public_timeline` - Public timeline
- `get_hashtag_timeline` - Hashtag timeline
- `get_list_timeline` - List timeline

### Notifications (5 tools)
- `get_notifications` - Get all notifications
- `get_notification` - Get single notification
- `dismiss_notification` - Dismiss notification
- `clear_notifications` - Clear all
- `get_unread_notification_count` - Unread count

### Search (1 tool)
- `search` - Search accounts, statuses, hashtags

### Lists (7 tools)
- `get_lists` - Get all lists
- `get_list` - Get list by ID
- `create_list` - Create new list
- `update_list` - Update list
- `delete_list` - Delete list
- `get_list_accounts` - Get list members
- `add_accounts_to_list` - Add members
- `remove_accounts_from_list` - Remove members

### Bookmarks & Favourites (2 tools)
- `get_bookmarks` - Get bookmarked statuses
- `get_favourites` - Get favourited statuses

### Media (4 tools)
- `upload_media` - Upload attachment
- `get_media` - Get media info
- `update_media` - Update media
- `delete_media` - Delete media

### Instance (3 tools)
- `get_instance_info` - Server information
- `get_instance_peers` - Connected domains
- `get_instance_activity` - Activity stats

### Tags (3 tools)
- `get_tag` - Get tag info
- `follow_tag` - Follow hashtag
- `unfollow_tag` - Unfollow hashtag

### Polls (2 tools)
- `get_poll` - Get poll
- `vote_on_poll` - Vote on poll

### Conversations (3 tools)
- `get_conversations` - Get conversations
- `delete_conversation` - Delete conversation
- `mark_conversation_as_read` - Mark as read

### Follow Requests (3 tools)
- `get_follow_requests` - Get pending requests
- `accept_follow_request` - Accept request
- `reject_follow_request` - Reject request

### Blocks & Mutes (5 tools)
- `get_blocks` - Get blocked accounts
- `get_mutes` - Get muted accounts
- `get_domain_blocks` - Get domain blocks
- `block_domain` - Block domain
- `unblock_domain` - Unblock domain

### Filters (5 tools)
- `get_filters` - Get all filters
- `get_filter` - Get filter by ID
- `create_filter` - Create filter
- `update_filter` - Update filter
- `delete_filter` - Delete filter

### Preferences (1 tool)
- `get_preferences` - Get user preferences

### Endorsements (3 tools)
- `get_endorsements` - Get featured profiles
- `feature_account` - Feature account
- `unfeature_account` - Unfeature account

### Announcements (2 tools)
- `get_announcements` - Get announcements
- `dismiss_announcement` - Dismiss announcement

### Reports (1 tool)
- `file_report` - File a report

### Scheduled Statuses (4 tools)
- `get_scheduled_statuses` - Get scheduled posts
- `get_scheduled_status` - Get scheduled post
- `update_scheduled_status` - Update schedule
- `cancel_scheduled_status` - Cancel scheduled post

### Custom Emojis (1 tool)
- `get_custom_emojis` - Get custom emojis

### Directory (1 tool)
- `get_directory` - Get profile directory

### Followed Tags (1 tool)
- `get_followed_tags` - Get followed tags

### Featured Tags (3 tools)
- `get_featured_tags` - Get featured tags
- `feature_tag` - Feature tag
- `unfeature_tag` - Unfeature tag

### Trends (3 tools)
- `get_trending_tags` - Get trending tags
- `get_trending_statuses` - Get trending statuses
- `get_trending_links` - Get trending links

### Suggestions (2 tools)
- `get_suggestions` - Get follow suggestions
- `remove_suggestion` - Remove suggestion

## API Documentation

All tools are documented in `grounding.json`, which maps each tool to:
- Description
- Endpoint (HTTP method and path)
- Source documentation file

## Error Handling

All tools return JSON-serializable responses. Errors are returned as dictionaries:

```python
{
  "error": "Error message describing what went wrong"
}
```

No exceptions are raised to the caller - all errors are caught and returned as error dicts.

## Authentication

The server uses OAuth 2.0 Bearer token authentication. Provide your access token via the `MASTODON_ACCESS_TOKEN` environment variable.

To obtain an access token:
1. Go to your Mastodon instance's settings
2. Navigate to Development > Your applications
3. Create a new application with appropriate scopes
4. Copy the access token

## Pagination

Many endpoints support pagination with these parameters:
- `limit`: Number of results to return
- `max_id`: Get results before this ID
- `min_id`: Get results after this ID
- `since_id`: Get results newer than this ID

## Rate Limiting

The Mastodon API has rate limits. The server does not implement rate limiting itself - respect your instance's limits.

## Supported Mastodon Versions

This server is compatible with Mastodon 3.0+ and should work with most recent versions.

## License

This MCP server implementation is provided as-is for use with the Model Context Protocol.

## Support

For issues with the MCP server implementation, check the error responses. For API-specific questions, refer to the [Mastodon API documentation](https://docs.joinmastodon.org/).
