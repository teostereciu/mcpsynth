from mcp.server.fastmcp import FastMCP

from generated_tools.attachments import (
    add_attachment,
    delete_attachment,
    get_attachment_metadata,
    get_attachment_settings,
)
from generated_tools.comments import (
    add_comment,
    delete_comment,
    get_comment,
    get_comments_by_ids,
    list_comments,
    update_comment,
)
from generated_tools.issue_links import create_issue_link, delete_issue_link, get_issue_link
from generated_tools.issues import (
    assign_issue,
    create_issue,
    delete_issue,
    get_issue,
    get_transitions,
    transition_issue,
    update_issue,
)
from generated_tools.projects import (
    create_project,
    delete_project,
    get_project,
    list_projects,
    search_projects,
    update_project,
)
from generated_tools.search import issue_picker, match_issues_against_jql, search_issues
from generated_tools.users import bulk_get_users, get_user, get_user_groups, search_users
from generated_tools.watchers import add_watcher, bulk_is_watching, get_issue_watchers, remove_watcher
from generated_tools.worklogs import add_worklog, delete_worklog, get_worklog, list_worklogs, update_worklog

mcp = FastMCP("jira-cloud")


# Issues
mcp.tool()(create_issue)
mcp.tool()(get_issue)
mcp.tool()(update_issue)
mcp.tool()(delete_issue)
mcp.tool()(assign_issue)
mcp.tool()(get_transitions)
mcp.tool()(transition_issue)

# Search
mcp.tool()(search_issues)
mcp.tool()(issue_picker)
mcp.tool()(match_issues_against_jql)

# Projects
mcp.tool()(list_projects)
mcp.tool()(search_projects)
mcp.tool()(get_project)
mcp.tool()(create_project)
mcp.tool()(update_project)
mcp.tool()(delete_project)

# Comments
mcp.tool()(list_comments)
mcp.tool()(add_comment)
mcp.tool()(get_comment)
mcp.tool()(update_comment)
mcp.tool()(delete_comment)
mcp.tool()(get_comments_by_ids)

# Worklogs
mcp.tool()(list_worklogs)
mcp.tool()(add_worklog)
mcp.tool()(get_worklog)
mcp.tool()(update_worklog)
mcp.tool()(delete_worklog)

# Attachments
mcp.tool()(get_attachment_settings)
mcp.tool()(get_attachment_metadata)
mcp.tool()(delete_attachment)
mcp.tool()(add_attachment)

# Watchers
mcp.tool()(get_issue_watchers)
mcp.tool()(add_watcher)
mcp.tool()(remove_watcher)
mcp.tool()(bulk_is_watching)

# Issue links
mcp.tool()(create_issue_link)
mcp.tool()(get_issue_link)
mcp.tool()(delete_issue_link)

# Users
mcp.tool()(get_user)
mcp.tool()(bulk_get_users)
mcp.tool()(get_user_groups)
mcp.tool()(search_users)


if __name__ == "__main__":
    mcp.run()
