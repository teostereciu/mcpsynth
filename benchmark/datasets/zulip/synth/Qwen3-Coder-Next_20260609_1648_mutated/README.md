# Zulip MCP Server

An MCP server providing comprehensive coverage of the Zulip REST API, suitable for use by autonomous agents.

## Prerequisites

- Python 3.8+
- Zulip account with API credentials
- Zulip site URL

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Set these environment variables:

```bash
export ZULIP_EMAIL="your-bot-email@example.com"
export ZULIP_API_KEY="your-api-key"
export ZULIP_SITE="https://your-org.zulipchat.com"
```

## Usage

```bash
python server.py
```

The server will run over stdio as an MCP server.

## Available Tools

The server exposes over 80 tools covering:

### Messages
- Send, fetch, edit, delete messages
- Get message history and edit history
- Add/remove emoji reactions
- Update message flags (read, starred, etc.)
- Mark messages as read
- Scheduled messages and reminders
- File uploads

### Channels (Streams)
- Get channels and subscriptions
- Subscribe/unsubscribe users
- Create, update, archive channels
- Get topics and subscribers

### Topics
- Update topic preferences (mute, pin, follow)
- Delete topics
- Rename topics

### Users
- Get user details and presence
- Create, update, deactivate users
- Manage user groups
- Set typing status

### Drafts
- Get, create, update, delete drafts

### Invitations
- Send email invitations
- Create reusable invite links
- Manage invites

### Navigation Views
- Manage custom navigation views

### Settings
- Update user settings
- Configure realm-level defaults

### And More
- Alert words
- Linkifiers
- Custom emoji
- Custom profile fields
- Saved snippets
- Server settings

## Authentication

Uses HTTP Basic Auth with email and API key.

## Error Handling

All errors are returned as JSON objects:
```json
{"error": "Error message", "code": "ERROR_CODE"}
```

## Documentation

For more information on Zulip's API, see:
- [Zulip API Documentation](https://zulip.com/api/)
