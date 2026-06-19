from mcp.server.fastmcp import FastMCP

from generated_tools.messaging import (
    send_message,
    fetch_message,
    list_messages,
    delete_message,
    update_message,
)
from generated_tools.voice import (
    create_call,
    fetch_call,
    list_calls,
    update_call,
    delete_call,
)
from generated_tools.phone_numbers import (
    list_incoming_phone_numbers,
    fetch_incoming_phone_number,
    purchase_incoming_phone_number,
    update_incoming_phone_number,
    delete_incoming_phone_number,
    search_available_local_numbers,
)
from generated_tools.verify import start_verification, check_verification
from generated_tools.conversations import (
    create_conversation,
    fetch_conversation,
    list_conversations,
    update_conversation,
    delete_conversation,
    add_participant,
    list_participants,
    delete_participant,
    send_conversation_message,
    list_conversation_messages,
)


mcp = FastMCP("twilio-rest")

# Messaging
mcp.tool()(send_message)
mcp.tool()(fetch_message)
mcp.tool()(list_messages)
mcp.tool()(update_message)
mcp.tool()(delete_message)

# Voice
mcp.tool()(create_call)
mcp.tool()(fetch_call)
mcp.tool()(list_calls)
mcp.tool()(update_call)
mcp.tool()(delete_call)

# Phone Numbers
mcp.tool()(search_available_local_numbers)
mcp.tool()(list_incoming_phone_numbers)
mcp.tool()(fetch_incoming_phone_number)
mcp.tool()(purchase_incoming_phone_number)
mcp.tool()(update_incoming_phone_number)
mcp.tool()(delete_incoming_phone_number)

# Verify
mcp.tool()(start_verification)
mcp.tool()(check_verification)

# Conversations
mcp.tool()(create_conversation)
mcp.tool()(fetch_conversation)
mcp.tool()(list_conversations)
mcp.tool()(update_conversation)
mcp.tool()(delete_conversation)
mcp.tool()(add_participant)
mcp.tool()(list_participants)
mcp.tool()(delete_participant)
mcp.tool()(send_conversation_message)
mcp.tool()(list_conversation_messages)


if __name__ == "__main__":
    mcp.run()
