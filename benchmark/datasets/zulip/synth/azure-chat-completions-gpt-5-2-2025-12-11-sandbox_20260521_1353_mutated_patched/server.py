from mcp.server.fastmcp import FastMCP

from generated_tools.messages import get_messages, send_message, upload_file
from generated_tools.streams import (
    archive_stream,
    create_stream,
    get_stream_by_id,
    get_stream_id,
    get_stream_topics,
    get_streams,
    get_subscriptions,
    subscribe,
    unsubscribe,
    update_stream,
)
from generated_tools.topics import delete_topic, update_user_topic
from generated_tools.reactions import add_reaction, remove_reaction
from generated_tools.users import (
    add_alert_words,
    get_alert_words,
    get_own_user,
    get_presence,
    get_user,
    get_user_by_email,
    get_user_presence,
    get_user_status,
    get_users,
    mute_user,
    remove_alert_words,
    unmute_user,
    update_presence,
    update_status,
)
from generated_tools.scheduled_messages import (
    create_scheduled_message,
    delete_scheduled_message,
    get_scheduled_messages,
    update_scheduled_message,
)
from generated_tools.drafts import create_drafts, delete_draft, edit_draft, get_drafts
from generated_tools.server_org import get_server_settings


mcp = FastMCP("zulip")

# Messages
mcp.tool()(send_message)
mcp.tool()(get_messages)
mcp.tool()(upload_file)

# Streams / subscriptions
mcp.tool()(get_streams)
mcp.tool()(get_stream_id)
mcp.tool()(get_stream_by_id)
mcp.tool()(create_stream)
mcp.tool()(update_stream)
mcp.tool()(archive_stream)
mcp.tool()(get_subscriptions)
mcp.tool()(subscribe)
mcp.tool()(unsubscribe)
mcp.tool()(get_stream_topics)

# Topics
mcp.tool()(update_user_topic)
mcp.tool()(delete_topic)

# Reactions
mcp.tool()(add_reaction)
mcp.tool()(remove_reaction)

# Users
mcp.tool()(get_own_user)
mcp.tool()(get_user)
mcp.tool()(get_user_by_email)
mcp.tool()(get_users)
mcp.tool()(get_user_presence)
mcp.tool()(get_presence)
mcp.tool()(update_presence)
mcp.tool()(get_user_status)
mcp.tool()(update_status)
mcp.tool()(mute_user)
mcp.tool()(unmute_user)
mcp.tool()(get_alert_words)
mcp.tool()(add_alert_words)
mcp.tool()(remove_alert_words)

# Scheduled messages
mcp.tool()(get_scheduled_messages)
mcp.tool()(create_scheduled_message)
mcp.tool()(update_scheduled_message)
mcp.tool()(delete_scheduled_message)

# Drafts
mcp.tool()(get_drafts)
mcp.tool()(create_drafts)
mcp.tool()(edit_draft)
mcp.tool()(delete_draft)

# Server/org
mcp.tool()(get_server_settings)


if __name__ == "__main__":
    mcp.run()
