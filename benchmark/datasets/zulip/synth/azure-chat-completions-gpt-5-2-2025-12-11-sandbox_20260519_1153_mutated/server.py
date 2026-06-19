from mcp.server.fastmcp import FastMCP

from generated_tools.messages import (
    add_reaction,
    delete_message,
    get_message,
    get_messages,
    remove_reaction,
    send_message,
    update_message,
)
from generated_tools.streams import (
    archive_stream,
    delete_topic,
    get_stream_topics,
    get_streams,
    subscribe,
    unsubscribe,
)
from generated_tools.users import (
    get_own_user,
    get_realm_presence,
    get_user_presence,
    get_users,
)
from generated_tools.scheduled_messages import (
    create_scheduled_message,
    delete_scheduled_message,
    get_scheduled_messages,
    update_scheduled_message,
)
from generated_tools.files import get_file_temporary_url, upload_file

mcp = FastMCP("zulip")

# Messages
mcp.tool()(send_message)
mcp.tool()(get_messages)
mcp.tool()(get_message)
mcp.tool()(update_message)
mcp.tool()(delete_message)
mcp.tool()(add_reaction)
mcp.tool()(remove_reaction)

# Streams / Topics
mcp.tool()(get_streams)
mcp.tool()(subscribe)
mcp.tool()(unsubscribe)
mcp.tool()(archive_stream)
mcp.tool()(get_stream_topics)
mcp.tool()(delete_topic)

# Users / Presence
mcp.tool()(get_own_user)
mcp.tool()(get_users)
mcp.tool()(get_user_presence)
mcp.tool()(get_realm_presence)

# Scheduled messages
mcp.tool()(get_scheduled_messages)
mcp.tool()(create_scheduled_message)
mcp.tool()(update_scheduled_message)
mcp.tool()(delete_scheduled_message)

# Files
mcp.tool()(upload_file)
mcp.tool()(get_file_temporary_url)


if __name__ == "__main__":
    mcp.run()
