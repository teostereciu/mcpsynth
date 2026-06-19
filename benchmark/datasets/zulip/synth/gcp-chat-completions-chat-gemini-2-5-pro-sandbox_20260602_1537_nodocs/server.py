
from mcp.server.fastmcp import FastMCP
import generated_tools.messages
import generated_tools.streams
import generated_tools.users
import generated_tools.drafts
import generated_tools.scheduled_messages
import generated_tools.topics
import generated_tools.files

if __name__ == "__main__":
    mcp = FastMCP()
    mcp.register_tools(generated_tools.messages)
    mcp.register_tools(generated_tools.streams)
    mcp.register_tools(generated_tools.users)
    mcp.register_tools(generated_tools.drafts)
    mcp.register_tools(generated_tools.scheduled_messages)
    mcp.register_tools(generated_tools.topics)
    mcp.register_tools(generated_tools.files)
    mcp.serve()
