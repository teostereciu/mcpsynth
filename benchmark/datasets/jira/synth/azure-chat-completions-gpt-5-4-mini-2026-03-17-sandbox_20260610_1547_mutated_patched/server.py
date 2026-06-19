from mcp.server.fastmcp import FastMCP
from generated_tools.issues import create_issue, get_issue, update_issue, delete_issue, assign_issue, get_issue_transitions, transition_issue
from generated_tools.comments import list_comments_by_ids, get_issue_comments, add_comment, get_comment, update_comment, delete_comment
from generated_tools.projects import get_projects, create_project, search_projects, get_project, update_project, delete_project
from generated_tools.search import issue_picker, jql_match, search_issues_get, search_issues_post
from generated_tools.worklogs import get_issue_worklogs, add_worklog

mcp = FastMCP("jira-cloud")

mcp.tool()(create_issue)
mcp.tool()(get_issue)
mcp.tool()(update_issue)
mcp.tool()(delete_issue)
mcp.tool()(assign_issue)
mcp.tool()(get_issue_transitions)
mcp.tool()(transition_issue)
mcp.tool()(list_comments_by_ids)
mcp.tool()(get_issue_comments)
mcp.tool()(add_comment)
mcp.tool()(get_comment)
mcp.tool()(update_comment)
mcp.tool()(delete_comment)
mcp.tool()(get_projects)
mcp.tool()(create_project)
mcp.tool()(search_projects)
mcp.tool()(get_project)
mcp.tool()(update_project)
mcp.tool()(delete_project)
mcp.tool()(issue_picker)
mcp.tool()(jql_match)
mcp.tool()(search_issues_get)
mcp.tool()(search_issues_post)
mcp.tool()(get_issue_worklogs)
mcp.tool()(add_worklog)

if __name__ == '__main__':
    mcp.run(transport='stdio')
