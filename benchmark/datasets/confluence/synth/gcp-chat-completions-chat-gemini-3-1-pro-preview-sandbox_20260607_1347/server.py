from mcp.server.fastmcp import FastMCP

mcp = FastMCP("confluence")

# Import all tool modules so they register their tools
import tools.pages
import tools.spaces
import tools.search
import tools.labels
import tools.attachments
import tools.comments
import tools.versions
import tools.properties
import tools.blog_posts
import tools.users

if __name__ == "__main__":
    mcp.run()
