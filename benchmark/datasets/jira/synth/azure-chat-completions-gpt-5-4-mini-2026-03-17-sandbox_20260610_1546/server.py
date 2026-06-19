from mcp.server.fastmcp import FastMCP

from generated_tools.comments import add_comment, get_comments
from generated_tools.components import create_component, get_components
from generated_tools.issues import create_issue, edit_issue, get_issue
from generated_tools.projects import create_project, get_project, get_projects
from generated_tools.versions import create_version, get_versions
from generated_tools.worklogs import add_worklog, get_worklogs

mcp = FastMCP("jira-cloud-rest-v3")

mcp.tool()(create_issue)
mcp.tool()(get_issue)
mcp.tool()(edit_issue)
mcp.tool()(get_comments)
mcp.tool()(add_comment)
mcp.tool()(get_worklogs)
mcp.tool()(add_worklog)
mcp.tool()(get_projects)
mcp.tool()(get_project)
mcp.tool()(create_project)
mcp.tool()(get_components)
mcp.tool()(create_component)
mcp.tool()(get_versions)
mcp.tool()(create_version)

if __name__ == "__main__":
    mcp.run()
