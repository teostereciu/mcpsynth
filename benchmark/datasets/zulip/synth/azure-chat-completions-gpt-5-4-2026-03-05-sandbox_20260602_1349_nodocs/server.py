from mcp.server.fastmcp import FastMCP

from generated_tools.drafts import create_draft, delete_draft, edit_draft, get_drafts
from generated_tools.files import upload_file
from generated_tools.messages import (
    add_reaction,
    delete_message,
    get_message,
    get_message_history,
    get_messages,
    mark_stream_topic_as_read,
    remove_reaction,
    send_message,
    update_message,
    update_message_flags,
)
from generated_tools.scheduled_messages import (
    create_scheduled_message,
    delete_scheduled_message,
    get_scheduled_messages,
    update_scheduled_message,
)
from generated_tools.streams import (
    archive_stream,
    create_streams,
    get_stream_id,
    get_streams,
    get_topics,
    subscribe_streams,
    unsubscribe_streams,
    update_stream,
)
from generated_tools.topics import delete_topic, get_topic_history, rename_topic, resolve_topic, unresolve_topic
from generated_tools.users import get_own_user, get_presence, get_user_by_email, get_user_by_id, get_users, update_status_text

mcp = FastMCP("zulip")

mcp.tool()(send_message)
mcp.tool()(get_messages)
mcp.tool()(get_message)
mcp.tool()(update_message)
mcp.tool()(delete_message)
mcp.tool()(mark_stream_topic_as_read)
mcp.tool()(add_reaction)
mcp.tool()(remove_reaction)
mcp.tool()(update_message_flags)
mcp.tool()(get_message_history)

mcp.tool()(get_streams)
mcp.tool()(create_streams)
mcp.tool()(subscribe_streams)
mcp.tool()(unsubscribe_streams)
mcp.tool()(get_stream_id)
mcp.tool()(archive_stream)
mcp.tool()(update_stream)
mcp.tool()(get_topics)

mcp.tool()(rename_topic)
mcp.tool()(resolve_topic)
mcp.tool()(unresolve_topic)
mcp.tool()(delete_topic)
mcp.tool()(get_topic_history)

mcp.tool()(get_own_user)
mcp.tool()(get_user_by_id)
mcp.tool()(get_user_by_email)
mcp.tool()(get_users)
mcp.tool()(get_presence)
mcp.tool()(update_status_text)

mcp.tool()(get_drafts)
mcp.tool()(create_draft)
mcp.tool()(edit_draft)
mcp.tool()(delete_draft)

mcp.tool()(get_scheduled_messages)
mcp.tool()(create_scheduled_message)
mcp.tool()(update_scheduled_message)
mcp.tool()(delete_scheduled_message)

mcp.tool()(upload_file)


if __name__ == "__main__":
    mcp.run()
