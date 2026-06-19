from mcp.server.fastmcp import FastMCP

from generated_tools import messages, streams, topics, users, drafts, scheduled, files

mcp = FastMCP("zulip")

# Messages
mcp.tool()(messages.send_message)
mcp.tool()(messages.get_messages)
mcp.tool()(messages.get_message)
mcp.tool()(messages.update_message)
mcp.tool()(messages.delete_message)
mcp.tool()(messages.add_reaction)
mcp.tool()(messages.remove_reaction)
mcp.tool()(messages.update_message_flags)
mcp.tool()(messages.render_message)

# Streams
mcp.tool()(streams.get_streams)
mcp.tool()(streams.get_stream_id)
mcp.tool()(streams.get_subscriptions)
mcp.tool()(streams.create_streams)
mcp.tool()(streams.subscribe)
mcp.tool()(streams.unsubscribe)
mcp.tool()(streams.update_stream)
mcp.tool()(streams.archive_stream)

# Topics
mcp.tool()(topics.get_topics)
mcp.tool()(topics.update_topic)

# Users
mcp.tool()(users.get_users)
mcp.tool()(users.get_user)
mcp.tool()(users.get_own_profile)
mcp.tool()(users.update_own_profile)
mcp.tool()(users.get_presence)

# Drafts
mcp.tool()(drafts.get_drafts)
mcp.tool()(drafts.create_drafts)
mcp.tool()(drafts.edit_draft)
mcp.tool()(drafts.delete_draft)

# Scheduled messages
mcp.tool()(scheduled.get_scheduled_messages)
mcp.tool()(scheduled.schedule_message)
mcp.tool()(scheduled.update_scheduled_message)
mcp.tool()(scheduled.delete_scheduled_message)

# Files
mcp.tool()(files.upload_file)


if __name__ == "__main__":
    mcp.run()
