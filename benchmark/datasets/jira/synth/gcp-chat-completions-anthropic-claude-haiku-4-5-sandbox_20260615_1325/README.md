# Jira Cloud REST API v3 MCP Server

A comprehensive Model Context Protocol (MCP) server implementation for the Jira Cloud REST API v3, enabling autonomous agents to perform real-world Jira operations.

## Features

This MCP server provides extensive coverage of the Jira Cloud REST API v3, including:

### Core Issue Operations
- **Create, Read, Update, Delete** issues
- **Search** issues using JQL (Jira Query Language)
- **Transition** issues between workflow states
- **Assign** issues to users
- **Get issue metadata** for creation and editing

### Issue Comments
- Add, retrieve, update, and delete comments
- Support for comment visibility restrictions

### Issue Worklogs
- Add, retrieve, update, and delete time tracking entries
- Bulk worklog operations

### Projects
- Get all projects or search with pagination
- Create, update, and delete projects
- Get project statuses and configurations
- Manage project components and versions

### Users & Groups
- Get user details and search for users
- Bulk user operations
- Create, update, and delete groups
- Manage group membership
- Find groups by name

### Filters
- Create, read, update, and delete filters
- Get favorite and personal filters
- Search filters with various criteria
- Manage filter favorites

### Issue Types & Priorities
- Get all issue types and priorities
- Create, update, and delete issue types
- Get issue types for specific projects
- Get alternative issue types

### Issue Links
- Create and delete issue links
- Get issue link types
- Manage issue link type definitions

### Additional Features
- **Watchers**: Add/remove issue watchers
- **Votes**: Vote on issues
- **Attachments**: Get and delete attachments
- **Properties**: Get, set, and delete issue properties
- **Changelog**: Get issue change history
- **Project Roles**: Manage user roles in projects
- **Security Levels**: Get issue security levels
- **Labels**: Get all available labels
- **Resolutions**: Get resolution types
- **Server Info**: Get Jira instance information
- **Current User**: Get authenticated user details

## Installation

### Prerequisites
- Python 3.8+
- Jira Cloud instance with API access
- API token (generated from Jira account settings)

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

## Running the Server

```bash
python server.py
```

The server will start and listen for MCP protocol messages over stdio.

## Authentication

The server uses HTTP Basic Authentication with your Jira email and API token. Ensure these environment variables are set:

- `JIRA_BASE_URL`: Your Atlassian instance URL (e.g., `https://your-org.atlassian.net`)
- `JIRA_EMAIL`: Your Jira account email
- `JIRA_API_TOKEN`: Your API token (generate from Account Settings > Security > API tokens)

## Tool Reference

The server exposes 120+ tools covering all major Jira operations. Each tool is documented with:
- Clear parameter descriptions
- Return value documentation
- Error handling

### Example Tools

#### Create an Issue
```python
create_issue(
    project_key="PROJ",
    issue_type="Bug",
    summary="Fix login button",
    description="The login button is not responding",
    assignee_id="user-account-id",
    priority="High",
    labels=["urgent", "frontend"],
    due_date="2024-12-31"
)
```

#### Search Issues
```python
search_issues(
    jql="project = PROJ AND status = 'In Progress'",
    start_at=0,
    max_results=50,
    fields=["summary", "status", "assignee"]
)
```

#### Add Comment
```python
add_comment(
    issue_key="PROJ-123",
    comment_text="This is a comment",
    visibility_type="role",
    visibility_value="Developers"
)
```

#### Manage Users
```python
search_users(query="john", max_results=10)
get_user(account_id="user-id")
create_user(email="newuser@example.com", display_name="New User")
```

#### Manage Groups
```python
create_group(name="developers")
add_user_to_group(account_id="user-id", group_id="group-id")
get_group_members(group_id="group-id")
```

## Grounding Documentation

The `grounding.json` file maps every tool to its source documentation endpoint:

```json
{
  "create_issue": {
    "doc": "docs/api_issues.md",
    "endpoint": "POST /rest/api/3/issue"
  },
  ...
}
```

This enables traceability and verification of all implemented operations.

## Error Handling

The server returns errors as JSON objects:

```json
{
  "error": "Not found"
}
```

Common error responses:
- `404 Not Found`: Resource doesn't exist
- `400 Bad Request`: Invalid parameters
- `401 Unauthorized`: Authentication failed
- `403 Forbidden`: Insufficient permissions

## Supported Operations

### Issues (20+ operations)
- CRUD operations
- Search and filtering
- Transitions and workflows
- Comments and worklogs
- Attachments and links
- Watchers and votes
- Properties and metadata

### Projects (7+ operations)
- List and search
- CRUD operations
- Status management
- Components and versions
- Roles and permissions

### Users (5+ operations)
- Get user details
- Search users
- Bulk operations
- Create and delete users

### Groups (8+ operations)
- CRUD operations
- Member management
- Search and discovery

### Filters (10+ operations)
- Create and manage filters
- Favorite management
- Search and discovery

### Configuration (15+ operations)
- Issue types
- Priorities
- Statuses
- Fields
- Link types
- Resolutions
- Labels

## API Compliance

This server implements the Jira Cloud REST API v3 as documented at:
https://developer.atlassian.com/cloud/jira/platform/rest/v3/

All endpoints follow the official API specifications and authentication requirements.

## Limitations

- No generic passthrough tools (all tools are specific operations)
- Bulk operations limited to API constraints (e.g., 1000 issues for archive)
- Some advanced features may require additional Jira licenses
- Rate limiting applies per Jira instance

## Development

To add new tools:

1. Implement the tool function with `@mcp.tool()` decorator
2. Add corresponding entry to `grounding.json`
3. Ensure proper error handling
4. Return JSON-serializable results

## License

This implementation is provided as-is for use with Jira Cloud instances.

## Support

For issues or questions:
1. Check the Jira Cloud API documentation
2. Verify environment variables are set correctly
3. Ensure your API token has appropriate permissions
4. Check Jira instance logs for detailed error messages
