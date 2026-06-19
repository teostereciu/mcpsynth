from mcp.server.fastmcp import FastMCP

from generated_tools.channels import (
    archive_channel,
    get_channel_by_id,
    get_channel_id,
    get_channel_topics,
    get_channels,
    update_channel,
)
from generated_tools.drafts import create_drafts, delete_draft, edit_draft, get_drafts
from generated_tools.messages import (
    add_reaction,
    create_scheduled_message,
    delete_message,
    get_message,
    get_messages,
    get_scheduled_messages,
    remove_reaction,
    send_message,
    update_message,
    update_scheduled_message,
)
from generated_tools.users import (
    create_user,
    deactivate_user,
    get_own_user,
    get_user,
    get_user_by_email,
    get_users,
    reactivate_user,
    update_user,
)

mcp = FastMCP("zulip")

mcp.tool()(send_message)
mcp.tool()(get_messages)
mcp.tool()(get_message)
mcp.tool()(update_message)
mcp.tool()(delete_message)
mcp.tool()(add_reaction)
mcp.tool()(remove_reaction)
mcp.tool()(create_scheduled_message)
mcp.tool()(get_scheduled_messages)
mcp.tool()(update_scheduled_message)
mcp.tool()(get_drafts)
mcp.tool()(create_drafts)
mcp.tool()(edit_draft)
mcp.tool()(delete_draft)
mcp.tool()(get_channels)
mcp.tool()(get_channel_by_id)
mcp.tool()(get_channel_id)
mcp.tool()(update_channel)
mcp.tool()(archive_channel)
mcp.tool()(get_channel_topics)
mcp.tool()(get_users)
mcp.tool()(get_own_user)
mcp.tool()(get_user)
mcp.tool()(get_user_by_email)
mcp.tool()(create_user)
mcp.tool()(update_user)
mcp.tool()(deactivate_user)
mcp.tool()(reactivate_user)

if __name__ == "__main__":
    mcp.run()
