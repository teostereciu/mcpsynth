"""
Jira Cloud REST API v3 MCP Server

Exposes comprehensive Jira operations as MCP tools, covering:
- Issues (CRUD, assign, transition, comments, worklogs, attachments, watchers, links)
- JQL Search
- Projects (CRUD, archive, restore, statuses)
- Components (CRUD)
- Versions (CRUD, merge)
- Users (get, search, assignable)
- Groups (CRUD, members)
- Filters (CRUD, favourites)
- Issue Types (CRUD)
- Priorities & Resolutions (CRUD)
- Statuses (CRUD)
- Fields (get, create, update, delete)
- Issue Properties
- Server Info

Authentication via environment variables:
  JIRA_BASE_URL  - e.g. https://your-org.atlassian.net
  JIRA_EMAIL     - account email
  JIRA_API_TOKEN - API token
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("jira-cloud")

# Register all tool modules
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
    priorities_resolutions,
    statuses,
    fields,
    properties,
)

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
priorities_resolutions.register(mcp)
statuses.register(mcp)
fields.register(mcp)
properties.register(mcp)

if __name__ == "__main__":
    mcp.run()
