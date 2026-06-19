"""Twilio MCP server (FastMCP).

Tools are registered from generated_tools.* modules.
"""

from __future__ import annotations

from fastmcp import FastMCP

from . import accounts, conversations, messaging, phone_numbers, verify

mcp = FastMCP("twilio")


# Accounts
mcp.tool()(accounts.account_fetch)

# Messaging
mcp.tool()(messaging.messages_create)
mcp.tool()(messaging.messages_fetch)
mcp.tool()(messaging.messages_list)
mcp.tool()(messaging.messages_update)
mcp.tool()(messaging.messages_delete)

# Phone Numbers
mcp.tool()(phone_numbers.available_phone_numbers_local_list)
mcp.tool()(phone_numbers.incoming_phone_numbers_list)
mcp.tool()(phone_numbers.incoming_phone_numbers_fetch)
mcp.tool()(phone_numbers.incoming_phone_numbers_create)
mcp.tool()(phone_numbers.incoming_phone_numbers_update)
mcp.tool()(phone_numbers.incoming_phone_numbers_delete)

# Verify
mcp.tool()(verify.verify_services_create)
mcp.tool()(verify.verify_services_list)
mcp.tool()(verify.verify_services_fetch)
mcp.tool()(verify.verify_services_update)
mcp.tool()(verify.verify_services_delete)
mcp.tool()(verify.verifications_create)
mcp.tool()(verify.verification_checks_create)

# Conversations
mcp.tool()(conversations.conversations_create)
mcp.tool()(conversations.conversations_fetch)
mcp.tool()(conversations.conversations_list)
mcp.tool()(conversations.conversations_update)
mcp.tool()(conversations.conversations_delete_tool)
mcp.tool()(conversations.conversation_messages_create)
mcp.tool()(conversations.conversation_messages_fetch)
mcp.tool()(conversations.conversation_messages_list)
mcp.tool()(conversations.conversation_participants_create)
mcp.tool()(conversations.conversation_participants_fetch)
mcp.tool()(conversations.conversation_participants_list)
mcp.tool()(conversations.conversation_participants_delete)
