import os
from mcp.server.fastmcp import FastMCP, tool
from generated_tools import messages, reactions, scheduled, drafts

# Tool registration wrappers
@tool
def send_message(**kwargs):
    """Send a channel or direct message."""
    return messages.send_message(**kwargs)

@tool
def edit_message(**kwargs):
    """Edit a message's content, topic, or channel."""
    return messages.edit_message(**kwargs)

@tool
def delete_message(message_id: int):
    """Permanently delete a message by ID."""
    return messages.delete_message(message_id)

@tool
def get_messages(**kwargs):
    """Fetch messages with optional narrow and anchor."""
    return messages.get_messages(**kwargs)

@tool
def update_message_flags(**kwargs):
    """Add or remove personal message flags (read, starred, etc)."""
    return messages.update_message_flags(**kwargs)

@tool
def get_message_history(message_id: int, allow_empty_topic_name: bool = False):
    """Fetch the edit history of a previously edited message."""
    return messages.get_message_history(message_id, allow_empty_topic_name)

@tool
def add_reaction(**kwargs):
    """Add an emoji reaction to a message."""
    return reactions.add_reaction(**kwargs)

@tool
def remove_reaction(**kwargs):
    """Remove an emoji reaction from a message."""
    return reactions.remove_reaction(**kwargs)

@tool
def create_scheduled_message(**kwargs):
    """Create a scheduled message (channel or direct)."""
    return scheduled.create_scheduled_message(**kwargs)

@tool
def update_scheduled_message(**kwargs):
    """Edit an existing scheduled message."""
    return scheduled.update_scheduled_message(**kwargs)

@tool
def get_scheduled_messages():
    """Fetch all scheduled messages for the current user."""
    return scheduled.get_scheduled_messages()

@tool
def delete_scheduled_message(scheduled_message_id: int):
    """Delete (cancel) a scheduled message by ID."""
    return scheduled.delete_scheduled_message(scheduled_message_id)

@tool
def get_drafts():
    """Fetch all drafts for the current user."""
    return drafts.get_drafts()

@tool
def create_drafts(drafts_list):
    """Create one or more drafts on the server."""
    return drafts.create_drafts(drafts_list)

@tool
def edit_draft(draft_id: int, draft):
    """Edit a draft on the server."""
    return drafts.edit_draft(draft_id, draft)

@tool
def delete_draft(draft_id: int):
    """Delete a single draft from the server."""
    return drafts.delete_draft(draft_id)

if __name__ == "__main__":
    FastMCP().run()
