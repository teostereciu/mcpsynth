# Quick Start Guide

## 5-Minute Setup

### 1. Get Your API Token

1. Go to https://id.atlassian.com/manage-profile/security/api-tokens
2. Click "Create API token"
3. Copy the generated token

### 2. Set Environment Variables

```bash
export JIRA_BASE_URL="https://your-org.atlassian.net"
export JIRA_EMAIL="your-email@example.com"
export JIRA_API_TOKEN="your-api-token"
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Server

```bash
python server.py
```

The server is now ready to accept MCP protocol messages over stdio.

## Common Tasks

### Get Current User

```json
{
  "tool": "get_current_user",
  "arguments": {}
}
```

### List All Projects

```json
{
  "tool": "get_projects",
  "arguments": {}
}
```

### Search Issues

```json
{
  "tool": "search_issues",
  "arguments": {
    "jql": "project = MYPROJ AND status = Open",
    "page_size": 10
  }
}
```

### Create an Issue

```json
{
  "tool": "create_issue",
  "arguments": {
    "project_id": "10000",
    "issue_type": "10001",
    "summary": "Fix login bug",
    "description": "Users cannot log in with SSO"
  }
}
```

### Get Issue Details

```json
{
  "tool": "get_issue",
  "arguments": {
    "issue_key": "MYPROJ-123"
  }
}
```

### Update Issue

```json
{
  "tool": "update_issue",
  "arguments": {
    "issue_key": "MYPROJ-123",
    "summary": "Updated summary",
    "priority_id": "2"
  }
}
```

### Assign Issue

```json
{
  "tool": "assign_issue",
  "arguments": {
    "issue_key": "MYPROJ-123",
    "assignee_id": "5b10a2844c20165700ede21g"
  }
}
```

### Get Issue Transitions

```json
{
  "tool": "get_issue_transitions",
  "arguments": {
    "issue_key": "MYPROJ-123"
  }
}
```

Response includes available transitions with their IDs.

### Transition Issue

```json
{
  "tool": "transition_issue",
  "arguments": {
    "issue_key": "MYPROJ-123",
    "transition_id": "11",
    "comment": "Moving to In Progress"
  }
}
```

### Add Comment

```json
{
  "tool": "add_comment",
  "arguments": {
    "issue_key": "MYPROJ-123",
    "comment_text": "This is a comment"
  }
}
```

### Get Comments

```json
{
  "tool": "get_issue_comments",
  "arguments": {
    "issue_key": "MYPROJ-123"
  }
}
```

### Add Worklog

```json
{
  "tool": "add_worklog",
  "arguments": {
    "issue_key": "MYPROJ-123",
    "time_spent": "2h 30m",
    "comment": "Completed implementation"
  }
}
```

### Get Worklogs

```json
{
  "tool": "get_issue_worklogs",
  "arguments": {
    "issue_key": "MYPROJ-123"
  }
}
```

### Add Watcher

```json
{
  "tool": "add_watcher",
  "arguments": {
    "issue_key": "MYPROJ-123",
    "account_id": "5b10a2844c20165700ede21g"
  }
}
```

### Get Watchers

```json
{
  "tool": "get_issue_watchers",
  "arguments": {
    "issue_key": "MYPROJ-123"
  }
}
```

### Create Issue Link

```json
{
  "tool": "create_issue_link",
  "arguments": {
    "link_type": "relates to",
    "inward_issue": "MYPROJ-123",
    "outward_issue": "MYPROJ-124"
  }
}
```

### Create Project

```json
{
  "tool": "create_project",
  "arguments": {
    "key": "NEWPROJ",
    "name": "New Project",
    "project_type": "software"
  }
}
```

### Get Project Details

```json
{
  "tool": "get_project",
  "arguments": {
    "project_key": "MYPROJ"
  }
}
```

### Get Project Components

```json
{
  "tool": "get_project_components",
  "arguments": {
    "project_key": "MYPROJ"
  }
}
```

### Create Component

```json
{
  "tool": "create_component",
  "arguments": {
    "project_key": "MYPROJ",
    "name": "Backend",
    "description": "Backend services"
  }
}
```

### Get Project Versions

```json
{
  "tool": "get_project_versions",
  "arguments": {
    "project_key": "MYPROJ"
  }
}
```

### Create Version

```json
{
  "tool": "create_version",
  "arguments": {
    "project_key": "MYPROJ",
    "name": "1.0.0",
    "description": "First release",
    "released": false
  }
}
```

### Get All Users

```json
{
  "tool": "get_all_users",
  "arguments": {
    "start_at": 0,
    "max_results": 50
  }
}
```

### Get User Details

```json
{
  "tool": "get_user",
  "arguments": {
    "account_id": "5b10a2844c20165700ede21g"
  }
}
```

### Create Group

```json
{
  "tool": "create_group",
  "arguments": {
    "group_name": "developers"
  }
}
```

### Add User to Group

```json
{
  "tool": "add_user_to_group",
  "arguments": {
    "group_name": "developers",
    "account_id": "5b10a2844c20165700ede21g"
  }
}
```

### Create Filter

```json
{
  "tool": "create_filter",
  "arguments": {
    "name": "My Open Issues",
    "jql": "assignee = currentUser() AND status = Open",
    "favorite": true
  }
}
```

### Get My Filters

```json
{
  "tool": "get_my_filters",
  "arguments": {}
}
```

### Get All Issue Types

```json
{
  "tool": "get_all_issue_types",
  "arguments": {}
}
```

### Get All Priorities

```json
{
  "tool": "get_priorities",
  "arguments": {}
}
```

### Get All Statuses

```json
{
  "tool": "get_all_statuses",
  "arguments": {}
}
```

## Troubleshooting

### "HTTP 401 Unauthorized"
- Check JIRA_EMAIL and JIRA_API_TOKEN are correct
- Verify API token hasn't expired
- Ensure JIRA_BASE_URL is correct

### "HTTP 404 Not Found"
- Verify issue key or project key exists
- Check spelling and case sensitivity
- Ensure you have permission to view the resource

### "HTTP 403 Forbidden"
- You don't have permission for this operation
- Check your Jira user permissions
- Some operations require admin access

### "HTTP 400 Bad Request"
- Check required parameters are provided
- Verify parameter values are valid
- Check field IDs and type IDs are correct

### Connection Timeout
- Check JIRA_BASE_URL is accessible
- Verify network connectivity
- Check firewall rules

## Finding IDs

### Project ID
```json
{
  "tool": "get_project",
  "arguments": {"project_key": "MYPROJ"}
}
```
Look for `"id"` in response.

### Issue Type ID
```json
{
  "tool": "get_all_issue_types",
  "arguments": {}
}
```
Look for `"id"` for each issue type.

### Priority ID
```json
{
  "tool": "get_priorities",
  "arguments": {}
}
```
Look for `"id"` for each priority.

### User Account ID
```json
{
  "tool": "get_all_users",
  "arguments": {}
}
```
Look for `"user_id"` or `"accountId"` in response.

### Component ID
```json
{
  "tool": "get_project_components",
  "arguments": {"project_key": "MYPROJ"}
}
```
Look for `"id"` for each component.

### Version ID
```json
{
  "tool": "get_project_versions",
  "arguments": {"project_key": "MYPROJ"}
}
```
Look for `"id"` for each version.

## Next Steps

1. Read the full [README.md](README.md) for complete tool documentation
2. Check [IMPLEMENTATION.md](IMPLEMENTATION.md) for technical details
3. Review [grounding.json](grounding.json) for endpoint mappings
4. Explore the [Jira API documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)
