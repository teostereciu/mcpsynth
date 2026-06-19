"""
Jira Cloud REST API v3 MCP Server

Runs over stdio using FastMCP. Exposes comprehensive tools for interacting
with Jira Cloud: issues, comments, worklogs, attachments, watchers, votes,
links, projects, components, versions, users, groups, filters, issue types,
priorities, statuses, fields, properties, permissions, dashboards, JQL, and more.

Required environment variables:
  JIRA_BASE_URL   - e.g. https://your-org.atlassian.net
  JIRA_EMAIL      - your Atlassian account email
  JIRA_API_TOKEN  - your Atlassian API token
"""

from mcp.server.fastmcp import FastMCP

# Import all domain modules
from generated_tools import (
    issues,
    comments,
    worklogs,
    attachments,
    watchers_votes,
    issue_links,
    projects,
    components,
    versions,
    users,
    groups,
    filters,
    issue_types,
    priorities,
    statuses,
    fields,
    issue_properties,
    permissions,
    remote_links,
    resolutions,
    jql,
    dashboards,
    project_roles,
)

mcp = FastMCP(
    name="jira-cloud",
    instructions=(
        "MCP server for Jira Cloud REST API v3. "
        "Provides tools for managing issues, projects, users, and all core Jira resources. "
        "Authentication uses JIRA_BASE_URL, JIRA_EMAIL, and JIRA_API_TOKEN environment variables."
    ),
)

# Register all tool domains
issues.register(mcp)
comments.register(mcp)
worklogs.register(mcp)
attachments.register(mcp)
watchers_votes.register(mcp)
issue_links.register(mcp)
projects.register(mcp)
components.register(mcp)
versions.register(mcp)
users.register(mcp)
groups.register(mcp)
filters.register(mcp)
issue_types.register(mcp)
priorities.register(mcp)
statuses.register(mcp)
fields.register(mcp)
issue_properties.register(mcp)
permissions.register(mcp)
remote_links.register(mcp)
resolutions.register(mcp)
jql.register(mcp)
dashboards.register(mcp)
project_roles.register(mcp)

if __name__ == "__main__":
    mcp.run()
