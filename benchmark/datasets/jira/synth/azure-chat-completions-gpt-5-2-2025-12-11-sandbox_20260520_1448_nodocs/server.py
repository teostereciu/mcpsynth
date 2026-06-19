from mcp.server.fastmcp import FastMCP

from generated_tools.issues import (
    add_comment,
    add_watcher,
    add_worklog,
    assign_issue,
    create_issue,
    create_issue_link,
    delete_comment,
    delete_issue,
    delete_issue_link,
    get_comments,
    get_issue,
    get_transitions,
    get_worklogs,
    remove_watcher,
    transition_issue,
    update_comment,
    update_issue,
)
from generated_tools.search import jql_search
from generated_tools.projects import (
    create_project,
    delete_project,
    get_project,
    list_projects,
    update_project,
)
from generated_tools.users import (
    find_assignable_users,
    find_users,
    get_myself,
    get_user,
)
from generated_tools.groups import find_groups, get_group_members
from generated_tools.metadata import list_issue_types, list_priorities, list_statuses
from generated_tools.filters import (
    create_filter,
    delete_filter,
    get_filter,
    list_my_filters,
    update_filter,
)
from generated_tools.components_versions import (
    create_component,
    create_version,
    delete_component,
    delete_version,
    get_component,
    get_version,
    update_component,
    update_version,
)

mcp = FastMCP("jira-cloud")

# Issues
mcp.tool()(get_issue)
mcp.tool()(create_issue)
mcp.tool()(update_issue)
mcp.tool()(delete_issue)
mcp.tool()(assign_issue)
mcp.tool()(get_transitions)
mcp.tool()(transition_issue)

# Comments
mcp.tool()(add_comment)
mcp.tool()(get_comments)
mcp.tool()(update_comment)
mcp.tool()(delete_comment)

# Worklogs
mcp.tool()(add_worklog)
mcp.tool()(get_worklogs)

# Watchers
mcp.tool()(add_watcher)
mcp.tool()(remove_watcher)

# Issue links
mcp.tool()(create_issue_link)
mcp.tool()(delete_issue_link)

# Search
mcp.tool()(jql_search)

# Projects
mcp.tool()(get_project)
mcp.tool()(list_projects)
mcp.tool()(create_project)
mcp.tool()(update_project)
mcp.tool()(delete_project)

# Users
mcp.tool()(get_myself)
mcp.tool()(get_user)
mcp.tool()(find_users)
mcp.tool()(find_assignable_users)

# Groups
mcp.tool()(find_groups)
mcp.tool()(get_group_members)

# Metadata
mcp.tool()(list_issue_types)
mcp.tool()(list_priorities)
mcp.tool()(list_statuses)

# Filters
mcp.tool()(get_filter)
mcp.tool()(list_my_filters)
mcp.tool()(create_filter)
mcp.tool()(update_filter)
mcp.tool()(delete_filter)

# Components & Versions
mcp.tool()(create_component)
mcp.tool()(get_component)
mcp.tool()(update_component)
mcp.tool()(delete_component)

mcp.tool()(create_version)
mcp.tool()(get_version)
mcp.tool()(update_version)
mcp.tool()(delete_version)


if __name__ == "__main__":
    mcp.run()
