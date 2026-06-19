# Zulip REST API MCP Server

A comprehensive Model Context Protocol (MCP) server implementation for the Zulip REST API, enabling autonomous agents to interact with Zulip instances through a standardized interface.

## Overview

This MCP server provides 120+ tools covering the most important Zulip REST API operations, organized into logical domains:

- **Messages**: Send, fetch, edit, delete, react to messages
- **Scheduled Messages**: Create, edit, delete scheduled messages
- **Drafts**: Manage draft messages
- **Streams/Channels**: Create, update, archive, subscribe to channels
- **Topics**: Manage topics within channels
- **Users**: Get user info, create users, manage user status and presence
- **User Groups**: Create and manage user groups
- **Reactions**: Add/remove emoji reactions
- **File Uploads**: Upload and manage file attachments
- **Settings**: Update user and subscription settings
- **Emoji**: Manage custom emoji
- **Alert Words**: Manage alert words
- **Invitations**: Send and manage invitations
- **Reminders**: Create and manage message reminders
- **Saved Snippets**: Manage saved code snippets
- **API Keys**: Manage API keys
- **Server Configuration**: Linkifiers, code playgrounds, custom profile fields

## Installation

### Prerequisites

- Python 3.10+
- Zulip instance with API access
- Valid Zulip credentials (email and API key)

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables:
```bash
export ZULIP_EMAIL="your-email@example.com"
export ZULIP_API_KEY="your-api-key"
export ZULIP_SITE="https://your-org.zulipchat.com"
```

3. Run the server:
```bash
python server.py
```

The server will start listening on stdio and be ready to accept MCP requests.

## Architecture

### Core Components

- **server.py**: Main MCP server implementation with 120+ tools
- **requirements.txt**: Python dependencies (FastMCP, requests)
- **grounding.json**: Mapping of tools to API documentation

### Tool Categories

#### Messages (13 tools)
- `send_message`: Send channel or direct messages
- `get_messages`: Fetch messages with filtering
- `get_message`: Fetch a single message
- `edit_message`: Edit message content or topic
- `delete_message`: Delete a message
- `get_message_history`: Get edit history
- `add_reaction`: Add emoji reaction
- `remove_reaction`: Remove emoji reaction
- `update_message_flags`: Update message flags (read, starred, etc.)
- `mark_all_as_read`: Mark all messages as read
- `mark_stream_as_read`: Mark stream messages as read
- `mark_topic_as_read`: Mark topic messages as read
- `get_read_receipts`: Get read receipt information

#### Scheduled Messages (4 tools)
- `get_scheduled_messages`: List scheduled messages
- `create_scheduled_message`: Create a scheduled message
- `edit_scheduled_message`: Edit a scheduled message
- `delete_scheduled_message`: Delete a scheduled message

#### Drafts (4 tools)
- `get_drafts`: List draft messages
- `create_draft`: Create a draft
- `edit_draft`: Edit a draft
- `delete_draft`: Delete a draft

#### Streams/Channels (15 tools)
- `get_streams`: List all streams
- `get_stream_by_id`: Get stream details
- `get_stream_id`: Get stream ID by name
- `create_stream`: Create a new stream
- `update_stream`: Update stream settings
- `archive_stream`: Archive a stream
- `get_stream_topics`: List topics in a stream
- `delete_topic`: Delete a topic
- `get_subscriptions`: List subscribed streams
- `subscribe`: Subscribe to streams
- `unsubscribe`: Unsubscribe from streams
- `get_stream_subscribers`: List stream subscribers
- `get_subscription_status`: Check subscription status
- `get_stream_email_address`: Get stream email address
- `update_subscription_settings`: Update subscription preferences

#### Topics (3 tools)
- `mute_topic`: Mute a topic
- `unmute_topic`: Unmute a topic
- `update_user_topic`: Update topic visibility policy

#### Users (20 tools)
- `get_users`: List all users
- `get_user`: Get user by ID
- `get_user_by_email`: Get user by email
- `get_own_user`: Get current user profile
- `create_user`: Create a new user (admin)
- `update_user`: Update user (admin)
- `update_user_by_email`: Update user by email (admin)
- `deactivate_user`: Deactivate user (admin)
- `deactivate_own_user`: Deactivate own account
- `reactivate_user`: Reactivate user (admin)
- `get_user_status`: Get user status
- `update_status`: Update own status
- `get_presence`: Get all users' presence
- `get_user_presence`: Get user presence
- `update_presence`: Update own presence
- `mute_user`: Mute a user
- `unmute_user`: Unmute a user
- `get_user_channels`: Get user's subscribed channels
- `set_typing_status`: Set typing status
- `set_typing_status_for_message_edit`: Set typing status for editing

#### User Groups (7 tools)
- `get_user_groups`: List user groups
- `create_user_group`: Create a user group
- `update_user_group`: Update group settings
- `deactivate_user_group`: Deactivate a group
- `get_user_group_members`: List group members
- `update_user_group_members`: Add/remove members
- `get_user_group_subgroups`: List subgroups
- `update_user_group_subgroups`: Add/remove subgroups
- `get_user_group_membership_status`: Check membership

#### File Management (3 tools)
- `upload_file`: Upload a file
- `get_attachments`: List uploaded files
- `delete_attachment`: Delete an attachment
- `get_file_temporary_url`: Get temporary file URL

#### Settings (2 tools)
- `get_settings`: Get user settings
- `update_settings`: Update user settings

#### Emoji (3 tools)
- `get_custom_emoji`: List custom emoji
- `upload_custom_emoji`: Upload custom emoji
- `deactivate_custom_emoji`: Deactivate emoji

#### Alert Words (3 tools)
- `get_alert_words`: List alert words
- `add_alert_words`: Add alert words
- `remove_alert_words`: Remove alert words

#### Server & Organization (10 tools)
- `get_server_settings`: Get server settings
- `get_linkifiers`: List linkifiers
- `add_linkifier`: Add a linkifier
- `update_linkifier`: Update a linkifier
- `remove_linkifier`: Remove a linkifier
- `reorder_linkifiers`: Reorder linkifiers
- `get_custom_profile_fields`: List custom profile fields
- `create_custom_profile_field`: Create custom profile field
- `reorder_custom_profile_fields`: Reorder profile fields
- `add_code_playground`: Add code playground
- `remove_code_playground`: Remove code playground

#### Invitations (5 tools)
- `get_invites`: List pending invitations
- `send_invites`: Send invitations
- `create_invite_link`: Create reusable invite link
- `revoke_invite_link`: Revoke invite link
- `resend_email_invite`: Resend email invitation
- `revoke_email_invite`: Revoke email invitation

#### Reminders (3 tools)
- `get_reminders`: List reminders
- `create_reminder`: Create a reminder
- `delete_reminder`: Delete a reminder

#### Saved Snippets (4 tools)
- `get_saved_snippets`: List saved snippets
- `create_saved_snippet`: Create a snippet
- `edit_saved_snippet`: Edit a snippet
- `delete_saved_snippet`: Delete a snippet

#### API Keys (3 tools)
- `regenerate_api_key`: Regenerate own API key
- `get_bot_api_key`: Get bot API key
- `regenerate_bot_api_key`: Regenerate bot API key

#### Additional Tools (3 tools)
- `render_message`: Render markdown to HTML
- `check_messages_match_narrow`: Check if messages match filter
- `report_message`: Report a message
- `add_default_stream`: Add default stream
- `remove_default_stream`: Remove default stream
- `get_channel_folders`: List channel folders
- `create_channel_folder`: Create channel folder
- `update_channel_folder`: Update channel folder

## Authentication

The server uses HTTP Basic Authentication with credentials from environment variables:

- `ZULIP_EMAIL`: Your Zulip email address
- `ZULIP_API_KEY`: Your Zulip API key
- `ZULIP_SITE`: Your Zulip instance URL (e.g., https://your-org.zulipchat.com)

To obtain API credentials:
1. Log in to your Zulip instance
2. Go to Settings → Account & Privacy
3. Scroll to "API key" section
4. Copy your email and API key

## Error Handling

All tools return JSON-serializable responses. Errors are returned as dictionaries with an "error" key:

```json
{
  "error": "Stream 'nonexistent' does not exist"
}
```

Expected errors (404s, invalid IDs, etc.) are handled gracefully and returned as error dicts rather than raising exceptions.

## Tool Documentation

Each tool includes comprehensive docstrings with:
- Description of functionality
- Parameter documentation with types
- Return value documentation
- Links to corresponding API documentation

The `grounding.json` file maps each tool to its API documentation file for reference.

## Usage Examples

### Send a Message
```python
result = send_message(
    type="channel",
    to="general",
    topic="Hello",
    content="This is a test message"
)
```

### Get Messages
```python
result = get_messages(
    start_message_id="newest",
    num_before=10,
    num_after=0,
    filter_spec=[{"operator": "channel", "operand": "general"}]
)
```

### Create a Stream
```python
result = create_stream(
    name="my-stream",
    description="A test stream",
    subscribers=[1, 2, 3]
)
```

### Update User Status
```python
result = update_status(
    status_text="In a meeting",
    status_emoji="calendar"
)
```

## Limitations

- No generic passthrough tools - all operations are specific, named tools
- File uploads are limited by server configuration
- Some operations require admin privileges
- Rate limiting is enforced by the Zulip server

## Development

### Adding New Tools

1. Implement the tool function in `server.py` with the `@server.tool()` decorator
2. Add comprehensive docstring with parameter and return documentation
3. Update `grounding.json` with the tool mapping
4. Test the tool with your Zulip instance

### Testing

To test the server:

```bash
# Set environment variables
export ZULIP_EMAIL="test@example.com"
export ZULIP_API_KEY="your-api-key"
export ZULIP_SITE="https://your-org.zulipchat.com"

# Run the server
python server.py
```

## API Documentation

Complete API documentation is available in the `docs/` directory. Each tool is mapped to its corresponding documentation file in `grounding.json`.

## License

This implementation is provided as-is for use with the Zulip REST API.

## Support

For issues with:
- **Zulip API**: See https://zulip.com/api/
- **MCP Protocol**: See https://modelcontextprotocol.io/
- **This Implementation**: Check the tool docstrings and grounding.json
