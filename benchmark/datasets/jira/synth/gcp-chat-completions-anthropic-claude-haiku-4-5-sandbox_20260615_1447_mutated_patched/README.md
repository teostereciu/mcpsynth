# Jira Cloud REST API v3 MCP Server

A comprehensive Model Context Protocol (MCP) server implementation for the Jira Cloud REST API v3, enabling autonomous agents to manage Jira issues, projects, users, and more.

## Features

This MCP server provides 80+ tools covering the most important Jira operations:

### Issues Management
- Create, read, update, and delete issues
- Assign issues to users
- Transition issues between statuses
- Get issue changelogs
- Manage issue comments (add, read, update, delete)
- Manage issue worklogs (add, read, update, delete)
- Manage issue watchers (add, remove, list)
- Create and manage issue links
- Manage attachments

### Search & Discovery
- Search issues using JQL (Jira Query Language)
- Count issues matching JQL queries
- Get issue picker suggestions
- Check issues against JQL queries

### Projects
- Get all projects or specific project details
- Create, update, and delete projects
- Get project statuses
- Manage project components (create, read, update, delete)
- Manage project versions (create, read, update, delete)

### Users & Groups
- Get user details
- Create and delete users
- Get all users with pagination
- Get user groups
- Create and delete groups
- Manage group membership (add/remove users)
- Find groups by name

### Filters
- Create, read, update, and delete filters
- Get user's own filters
- Get favorite filters
- Add/remove filters from favorites

### Configuration
- Get all issue types
- Get all priorities
- Get all statuses
- Get server information
- Get current user information

## Installation

### Prerequisites
- Python 3.8+
- Jira Cloud instance with API access
- API token for authentication

### Setup

1. Clone or download this repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set environment variables:
```bash
export JIRA_BASE_URL="https://your-org.atlassian.net"
export JIRA_EMAIL="your-email@example.com"
export JIRA_API_TOKEN="your-api-token"
```

To generate an API token:
1. Go to https://id.atlassian.com/manage-profile/security/api-tokens
2. Click "Create API token"
3. Copy the token and use it as `JIRA_API_TOKEN`

## Usage

### Running the Server

```bash
python server.py
```

The server will start and listen on stdio, ready to accept MCP protocol messages.

### Example Tool Calls

#### Create an Issue
```json
{
  "tool": "create_issue",
  "arguments": {
    "project_id": "10000",
    "issue_type": "10001",
    "summary": "Fix login bug",
    "description": "Users cannot log in with SSO",
    "priority_id": "2"
  }
}
```

#### Search Issues
```json
{
  "tool": "search_issues",
  "arguments": {
    "jql": "project = PROJ AND status = Open",
    "page_size": 20
  }
}
```

#### Assign Issue
```json
{
  "tool": "assign_issue",
  "arguments": {
    "issue_key": "PROJ-123",
    "assignee_id": "5b10a2844c20165700ede21g"
  }
}
```

#### Transition Issue
```json
{
  "tool": "transition_issue",
  "arguments": {
    "issue_key": "PROJ-123",
    "transition_id": "11",
    "comment": "Moving to In Progress"
  }
}
```

#### Add Comment
```json
{
  "tool": "add_comment",
  "arguments": {
    "issue_key": "PROJ-123",
    "comment_text": "This is a comment on the issue"
  }
}
```

## Tool Categories

### Issues (8 tools)
- `create_issue` - Create a new issue
- `get_issue` - Get issue details
- `update_issue` - Update issue fields
- `delete_issue` - Delete an issue
- `assign_issue` - Assign issue to user
- `get_issue_transitions` - Get available transitions
- `transition_issue` - Move issue to new status
- `get_issue_changelog` - Get issue change history

### Issue Search (3 tools)
- `search_issues` - Search using JQL
- `count_issues` - Count issues matching JQL
- `get_issue_picker_suggestions` - Get autocomplete suggestions

### Comments (5 tools)
- `add_comment` - Add comment to issue
- `get_issue_comments` - Get all comments
- `get_comment` - Get specific comment
- `update_comment` - Update comment
- `delete_comment` - Delete comment

### Worklogs (5 tools)
- `add_worklog` - Log time on issue
- `get_issue_worklogs` - Get all worklogs
- `get_worklog` - Get specific worklog
- `update_worklog` - Update worklog
- `delete_worklog` - Delete worklog

### Watchers (3 tools)
- `get_issue_watchers` - Get issue watchers
- `add_watcher` - Add watcher to issue
- `remove_watcher` - Remove watcher from issue

### Issue Links (3 tools)
- `create_issue_link` - Link two issues
- `get_issue_link` - Get link details
- `delete_issue_link` - Delete link

### Attachments (2 tools)
- `get_attachment_metadata` - Get attachment info
- `delete_attachment` - Delete attachment

### Projects (6 tools)
- `get_projects` - Get all projects
- `get_project` - Get project details
- `create_project` - Create new project
- `update_project` - Update project
- `delete_project` - Delete project
- `get_project_statuses` - Get project statuses

### Components (5 tools)
- `get_project_components` - Get all components
- `create_component` - Create component
- `get_component` - Get component details
- `update_component` - Update component
- `delete_component` - Delete component

### Versions (5 tools)
- `get_project_versions` - Get all versions
- `create_version` - Create version
- `get_version` - Get version details
- `update_version` - Update version
- `delete_version` - Delete version

### Users (5 tools)
- `get_user` - Get user details
- `create_user` - Create new user
- `delete_user` - Delete user
- `get_all_users` - Get all users
- `get_user_groups` - Get user's groups

### Groups (6 tools)
- `create_group` - Create group
- `delete_group` - Delete group
- `get_group_members` - Get group members
- `add_user_to_group` - Add user to group
- `remove_user_from_group` - Remove user from group
- `find_groups` - Find groups by name

### Filters (8 tools)
- `create_filter` - Create filter
- `get_filter` - Get filter details
- `update_filter` - Update filter
- `delete_filter` - Delete filter
- `get_my_filters` - Get user's filters
- `get_favorite_filters` - Get favorite filters
- `add_filter_as_favorite` - Add to favorites
- `remove_filter_as_favorite` - Remove from favorites

### Issue Types (5 tools)
- `get_all_issue_types` - Get all issue types
- `get_issue_type` - Get issue type details
- `create_issue_type` - Create issue type
- `update_issue_type` - Update issue type
- `delete_issue_type` - Delete issue type

### Priorities (2 tools)
- `get_priorities` - Get all priorities
- `get_priority` - Get priority details

### Statuses (2 tools)
- `get_all_statuses` - Get all statuses
- `get_status` - Get status details

### Server (2 tools)
- `get_server_info` - Get Jira server info
- `get_current_user` - Get current user info

## Error Handling

All tools return JSON-serializable responses. Errors are returned as dictionaries with an "error" key:

```json
{
  "error": "HTTP 404",
  "message": "Issue not found"
}
```

Expected errors (404s, invalid IDs, etc.) are handled gracefully and returned as error dictionaries rather than raising exceptions.

## Authentication

The server uses HTTP Basic Authentication with your Jira email and API token. Credentials are read from environment variables and included in all API requests.

## API Documentation

For detailed API documentation, see the Jira Cloud REST API v3 documentation:
https://developer.atlassian.com/cloud/jira/platform/rest/v3/

## Grounding

The `grounding.json` file maps each tool to its corresponding API endpoint and documentation file for reference and validation.

## Limitations

- Some advanced features (e.g., custom fields, workflows) may require additional configuration
- Bulk operations are supported through individual tool calls
- File uploads for attachments are not directly supported (use the API directly for binary uploads)
- Some endpoints require specific Jira licenses or permissions

## Support

For issues or questions:
1. Check the Jira Cloud REST API documentation
2. Verify your API token and permissions
3. Ensure environment variables are set correctly

## License

This MCP server implementation is provided as-is for use with the Jira Cloud REST API.
