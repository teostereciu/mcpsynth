from mcp.server.fastmcp import FastMCP

from generated_tools.confluence_tools import *  # noqa: F401,F403

mcp = FastMCP("confluence-cloud")

mcp.tool()(list_spaces)
mcp.tool()(get_space)
mcp.tool()(create_space)
mcp.tool()(list_pages)
mcp.tool()(get_page)
mcp.tool()(create_page)
mcp.tool()(update_page)
mcp.tool()(delete_page)
mcp.tool()(list_blog_posts)
mcp.tool()(create_blog_post)
mcp.tool()(get_blog_post)
mcp.tool()(update_blog_post)
mcp.tool()(delete_blog_post)

if __name__ == "__main__":
    mcp.run()
