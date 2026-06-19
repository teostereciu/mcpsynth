from mcp.server.fastmcp import FastMCP
from generated_tools.issues import create_issue, get_issue, edit_issue, delete_issue
from generated_tools.projects import get_projects, get_project, create_project, update_project

mcp = FastMCP("jira-cloud-rest-v3")

mcp.tool()(create_issue)
mcp.tool()(get_issue)
mcp.tool()(edit_issue)
mcp.tool()(delete_issue)
mcp.tool()(get_projects)
mcp.tool()(get_project)
mcp.tool()(create_project)
mcp.tool()(update_project)

if __name__ == "__main__":
    mcp.run()
