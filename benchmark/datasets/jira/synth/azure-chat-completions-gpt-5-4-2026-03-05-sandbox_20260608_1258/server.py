from mcp.server.fastmcp import FastMCP

from generated_tools.issues import *
from generated_tools.projects import *
from generated_tools.search import *
from generated_tools.users import *

mcp = FastMCP("jira-cloud")

for fn in [
    create_issue,
    get_issue,
    update_issue,
    delete_issue,
    assign_issue,
    get_issue_transitions,
    transition_issue,
    get_issue_changelog,
    get_create_issue_meta,
    get_edit_issue_meta,
    list_comments,
    add_comment,
    get_comment,
    update_comment,
    delete_comment,
    list_worklogs,
    add_worklog,
    get_worklog,
    get_issue_watchers,
    add_watcher,
    remove_watcher,
    bulk_is_watching,
    get_attachment_settings,
    get_attachment,
    delete_attachment,
    add_attachment,
    create_issue_link,
    get_issue_link,
    delete_issue_link,
    search_issues,
    issue_picker,
    jql_match,
    list_fields,
    search_fields,
    create_custom_field,
    list_projects,
    search_projects,
    get_project,
    create_project,
    list_components,
    create_component,
    get_component,
    get_user,
    bulk_get_users,
    get_user_groups,
    create_group,
    list_groups,
    get_group_members,
    add_user_to_group,
    remove_user_from_group,
    find_groups,
]:
    mcp.tool()(fn)


if __name__ == "__main__":
    mcp.run()
