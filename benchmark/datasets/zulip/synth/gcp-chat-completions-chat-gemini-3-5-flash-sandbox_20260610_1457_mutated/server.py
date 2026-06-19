from mcp.server.fastmcp import FastMCP
import generated_tools.messages as messages
import generated_tools.streams as streams
import generated_tools.topics as topics
import generated_tools.users as users
import generated_tools.reactions as reactions
import generated_tools.scheduled_messages as scheduled_messages
import generated_tools.drafts as drafts
import generated_tools.uploads as uploads

mcp = FastMCP("Zulip REST API MCP Server")

# Register messages tools
mcp.tool()(messages.send_message)
mcp.tool()(messages.update_message)
mcp.tool()(messages.delete_message)
mcp.tool()(messages.get_messages)
mcp.tool()(messages.get_message)
mcp.tool()(messages.get_message_history)
mcp.tool()(messages.update_message_flags)

# Register streams tools
mcp.tool()(streams.subscribe_to_streams)
mcp.tool()(streams.unsubscribe_from_streams)
mcp.tool()(streams.get_subscriptions)
mcp.tool()(streams.get_streams)
mcp.tool()(streams.get_stream_by_id)
mcp.tool()(streams.get_stream_id)
mcp.tool()(streams.update_stream)
mcp.tool()(streams.archive_stream)
mcp.tool()(streams.get_stream_subscribers)

# Register topics tools
mcp.tool()(topics.get_stream_topics)
mcp.tool()(topics.update_user_topic)
mcp.tool()(topics.delete_topic)

# Register users tools
mcp.tool()(users.get_users)
mcp.tool()(users.get_user)
mcp.tool()(users.get_user_by_email)
mcp.tool()(users.get_own_user)
mcp.tool()(users.create_user)
mcp.tool()(users.update_user)
mcp.tool()(users.deactivate_user)
mcp.tool()(users.reactivate_user)
mcp.tool()(users.get_user_presence)
mcp.tool()(users.get_realm_presence)

# Register reactions tools
mcp.tool()(reactions.add_reaction)
mcp.tool()(reactions.remove_reaction)

# Register scheduled messages tools
mcp.tool()(scheduled_messages.create_scheduled_message)
mcp.tool()(scheduled_messages.get_scheduled_messages)
mcp.tool()(scheduled_messages.update_scheduled_message)
mcp.tool()(scheduled_messages.delete_scheduled_message)

# Register drafts tools
mcp.tool()(drafts.create_drafts)
mcp.tool()(drafts.get_drafts)
mcp.tool()(drafts.edit_draft)
mcp.tool()(drafts.delete_draft)

# Register uploads tools
mcp.tool()(uploads.upload_file_from_path)
mcp.tool()(uploads.upload_file_from_content)

if __name__ == "__main__":
    mcp.run()
