from __future__ import annotations

from fastmcp import FastMCP

from . import alert_words, messages, reactions, scheduled_messages, streams, topics, users

mcp = FastMCP("zulip")

# Messages
mcp.tool()(messages.send_message)
mcp.tool()(messages.update_message)
mcp.tool()(messages.delete_message)
mcp.tool()(messages.get_message)
mcp.tool()(messages.get_messages)
mcp.tool()(messages.get_message_history)
mcp.tool()(messages.render_message)
mcp.tool()(messages.check_messages_match_narrow)
mcp.tool()(messages.update_message_flags)
mcp.tool()(messages.update_message_flags_for_narrow)
mcp.tool()(messages.mark_all_as_read)
mcp.tool()(messages.mark_stream_as_read)
mcp.tool()(messages.mark_topic_as_read)
mcp.tool()(messages.get_read_receipts)
mcp.tool()(messages.report_message)

# Reactions
mcp.tool()(reactions.add_reaction)
mcp.tool()(reactions.remove_reaction)

# Scheduled messages
mcp.tool()(scheduled_messages.create_scheduled_message)
mcp.tool()(scheduled_messages.get_scheduled_messages)
mcp.tool()(scheduled_messages.update_scheduled_message)
mcp.tool()(scheduled_messages.delete_scheduled_message)

# Streams/channels
mcp.tool()(streams.get_stream_id)
mcp.tool()(streams.get_stream_topics)
mcp.tool()(streams.subscribe)
mcp.tool()(streams.unsubscribe)
mcp.tool()(streams.get_subscribers)

# Topics
mcp.tool()(topics.delete_topic)

# Users
mcp.tool()(users.get_user)
mcp.tool()(users.get_user_by_email)
mcp.tool()(users.get_users)
mcp.tool()(users.get_own_user)

# Alert words
mcp.tool()(alert_words.get_alert_words)
mcp.tool()(alert_words.add_alert_words)
mcp.tool()(alert_words.remove_alert_words)
