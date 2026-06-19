import os
from mcp.server.fastmcp import FastMCP
from generated_tools import messages

TOOLS = [
    messages.send_message,
    messages.get_messages,
    messages.edit_message,
    messages.delete_message,
    messages.get_message_history,
    messages.add_reaction,
    messages.remove_reaction,
    messages.create_scheduled_message,
    messages.get_scheduled_messages,
    messages.edit_scheduled_message,
    messages.delete_scheduled_message,
    messages.create_drafts,
    messages.get_drafts,
    messages.edit_draft,
    messages.delete_draft,
]

if __name__ == "__main__":
    FastMCP(
        tools=TOOLS,
        list_tools=True,
    ).run_stdio()
