from mcp.server.fastmcp import FastMCP

from generated_tools import (
    # messages
    send_message,
    get_messages,
    update_message,
    delete_message,
    # streams/topics
    subscribe,
    unsubscribe,
    get_streams,
    get_stream_id,
    get_stream_by_id,
    update_stream,
    archive_stream,
    get_subscriptions,
    get_stream_topics,
    update_user_topic,
    # users
    get_own_user,
    get_users,
    get_user,
    get_user_by_email,
    get_user_presence,
    get_presence,
    update_presence,
    update_status,
    # reactions
    add_reaction,
    remove_reaction,
    # scheduled messages
    get_scheduled_messages,
    create_scheduled_message,
    update_scheduled_message,
    delete_scheduled_message,
    # drafts
    get_drafts,
    create_drafts,
    edit_draft,
    delete_draft,
    # files
    upload_file,
    get_file_temporary_url,
)

mcp = FastMCP("zulip")


# Messages
mcp.tool()(send_message)
mcp.tool()(get_messages)
mcp.tool()(update_message)
mcp.tool()(delete_message)

# Streams / subscriptions / topics
mcp.tool()(subscribe)
mcp.tool()(unsubscribe)
mcp.tool()(get_subscriptions)
mcp.tool()(get_streams)
mcp.tool()(get_stream_id)
mcp.tool()(get_stream_by_id)
mcp.tool()(update_stream)
mcp.tool()(archive_stream)
mcp.tool()(get_stream_topics)
mcp.tool()(update_user_topic)

# Users / presence / status
mcp.tool()(get_own_user)
mcp.tool()(get_users)
mcp.tool()(get_user)
mcp.tool()(get_user_by_email)
mcp.tool()(get_user_presence)
mcp.tool()(get_presence)
mcp.tool()(update_presence)
mcp.tool()(update_status)

# Reactions
mcp.tool()(add_reaction)
mcp.tool()(remove_reaction)

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

# Files
mcp.tool()(upload_file)
mcp.tool()(get_file_temporary_url)


if __name__ == "__main__":
    mcp.run()
