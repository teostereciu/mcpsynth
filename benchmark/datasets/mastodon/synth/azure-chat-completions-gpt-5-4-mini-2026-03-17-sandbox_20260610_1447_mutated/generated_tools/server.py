from mcp.server.fastmcp import FastMCP

from generated_tools.statuses import *
from generated_tools.timelines import *
from generated_tools.notifications import *

mcp = FastMCP("mastodon")

mcp.tool()(post_status)
mcp.tool()(get_status)
mcp.tool()(delete_status)
mcp.tool()(get_status_context)
mcp.tool()(favourite_status)
mcp.tool()(unfavourite_status)
mcp.tool()(boost_status)
mcp.tool()(unboost_status)
mcp.tool()(bookmark_status)
mcp.tool()(unbookmark_status)
mcp.tool()(get_public_timeline)
mcp.tool()(get_home_timeline)
mcp.tool()(get_hashtag_timeline)
mcp.tool()(get_notifications)

if __name__ == "__main__":
    mcp.run()
