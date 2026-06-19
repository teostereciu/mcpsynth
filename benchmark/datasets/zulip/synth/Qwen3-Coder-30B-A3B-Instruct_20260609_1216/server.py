#!/usr/bin/env python3
"""
Zulip MCP Server Implementation
"""

import asyncio
import json
import os
from typing import Any, Dict, List, Optional, Union
from mcp.server.fastmcp import FastMCP
from mcp.types import (
    Tool,
    ToolResult,
    TextContent,
    ImageContent,
    Content,
    Message,
    ToolCall,
    ToolResultContent,
)
import zulip

# Initialize the MCP server
app = FastMCP()

# Store Zulip client instances
zulip_clients: Dict[str, zulip.Client] = {}

def get_zulip_client(email: str, api_key: str, server_url: str) -> zulip.Client:
    """Get or create a Zulip client instance"""
    client_key = f"{email}:{server_url}"
    if client_key not in zulip_clients:
        zulip_clients[client_key] = zulip.Client(
            email=email,
            api_key=api_key,
            site=server_url
        )
    return zulip_clients[client_key]

async def send_message_tool(
    email: str,
    api_key: str,
    server_url: str,
    content: str,
    stream: Optional[str] = None,
    topic: Optional[str] = None,
    user_ids: Optional[List[int]] = None
) -> ToolResult:
    """Send a message to a channel or user"""
    
    client = get_zulip_client(email, api_key, server_url)
    
    try:
        # Prepare the request
        request: Dict[str, Any] = {
            "content": content
        }
        
        # Handle channel/stream messaging
        if stream:
            request["type"] = "stream"
            request["to"] = stream
            if topic:
                request["topic"] = topic
        # Handle private messaging
        elif user_ids:
            request["type"] = "private"
            request["to"] = [str(uid) for uid in user_ids]
        else:
            raise ValueError("Either stream or user_ids must be specified")
        
        # Send the message
        result = client.send_message(request)
        
        return ToolResult(
            content=[
                TextContent(
                    text=f"Message sent successfully! Message ID: {result['id']}"
                )
            ]
        )
        
    except Exception as e:
        return ToolResult(
            content=[
                TextContent(
                    text=f"Failed to send message: {str(e)}"
                )
            ],
            isError=True
        )

async def get_messages_tool(
    email: str,
    api_key: str,
    server_url: str,
    stream: Optional[str] = None,
    topic: Optional[str] = None,
    num_before: int = 10,
    num_after: int = 0
) -> ToolResult:
    """Get messages from a channel or topic"""
    
    client = get_zulip_client(email, api_key, server_url)
    
    try:
        # Prepare the request
        request: Dict[str, Any] = {
            "anchor": "newest",
            "num_before": num_before,
            "num_after": num_after,
            "narrow": []
        }
        
        # Add narrowing filters if specified
        if stream:
            request["narrow"].append({
                "operator": "stream",
                "operand": stream
            })
        if topic:
            request["narrow"].append({
                "operator": "topic",
                "operand": topic
            })
        
        # Get messages
        result = client.get_messages(request)
        
        # Format messages for response
        messages = []
        for msg in result.get("messages", [])[:10]:  # Limit to first 10
            msg_text = f"From: {msg.get('sender_full_name', 'Unknown')}\n"
            msg_text += f"Content: {msg.get('content', '')}\n"
            msg_text += f"Time: {msg.get('timestamp', 'Unknown')}\n"
            messages.append(msg_text)
        
        response_text = "\n---\n".join(messages) if messages else "No messages found."
        
        return ToolResult(
            content=[
                TextContent(text=response_text)
            ]
        )
        
    except Exception as e:
        return ToolResult(
            content=[
                TextContent(
                    text=f"Failed to get messages: {str(e)}"
                )
            ],
            isError=True
        )

async def create_channel_tool(
    email: str,
    api_key: str,
    server_url: str,
    name: str,
    description: Optional[str] = None,
    subscribers: Optional[List[int]] = None
) -> ToolResult:
    """Create a new channel"""
    
    client = get_zulip_client(email, api_key, server_url)
    
    try:
        # Prepare the request
        request: Dict[str, Any] = {
            "name": name
        }
        
        if description:
            request["description"] = description
        if subscribers:
            request["subscribers"] = subscribers
            
        # Create channel using the correct endpoint
        result = client.call_endpoint(
            url="channels/create",
            method="POST",
            request=request
        )
        
        return ToolResult(
            content=[
                TextContent(
                    text=f"Channel '{name}' created successfully! Channel ID: {result.get('stream_id', 'Unknown')}"
                )
            ]
        )
        
    except Exception as e:
        return ToolResult(
            content=[
                TextContent(
                    text=f"Failed to create channel: {str(e)}"
                )
            ],
            isError=True
        )

async def list_channels_tool(
    email: str,
    api_key: str,
    server_url: str
) -> ToolResult:
    """List all channels"""
    
    client = get_zulip_client(email, api_key, server_url)
    
    try:
        # Get all channels
        result = client.get_streams()
        
        channels = []
        for stream in result.get("streams", [])[:10]:  # Limit to first 10
            channels.append(f"- {stream['name']} (ID: {stream['stream_id']})")
        
        response_text = "\n".join(channels) if channels else "No channels found."
        
        return ToolResult(
            content=[
                TextContent(text=response_text)
            ]
        )
        
    except Exception as e:
        return ToolResult(
            content=[
                TextContent(
                    text=f"Failed to list channels: {str(e)}"
                )
            ],
            isError=True
        )

async def delete_message_tool(
    email: str,
    api_key: str,
    server_url: str,
    message_id: int
) -> ToolResult:
    """Delete a message by ID"""
    
    client = get_zulip_client(email, api_key, server_url)
    
    try:
        # Delete message
        result = client.call_endpoint(
            url=f"messages/{message_id}",
            method="DELETE"
        )
        
        return ToolResult(
            content=[
                TextContent(
                    text=f"Message {message_id} deleted successfully!"
                )
            ]
        )
        
    except Exception as e:
        return ToolResult(
            content=[
                TextContent(
                    text=f"Failed to delete message: {str(e)}"
                )
            ],
            isError=True
        )

async def delete_channel_tool(
    email: str,
    api_key: str,
    server_url: str,
    stream_id: int
) -> ToolResult:
    """Delete a channel by ID"""
    
    client = get_zulip_client(email, api_key, server_url)
    
    try:
        # Archive stream (which effectively deletes it)
        result = client.call_endpoint(
            url=f"streams/{stream_id}",
            method="DELETE"
        )
        
        return ToolResult(
            content=[
                TextContent(
                    text=f"Channel with ID {stream_id} archived successfully!"
                )
            ]
        )
        
    except Exception as e:
        return ToolResult(
            content=[
                TextContent(
                    text=f"Failed to archive channel: {str(e)}"
                )
            ],
            isError=True
        )

async def get_user_info_tool(
    email: str,
    api_key: str,
    server_url: str,
    user_id: Optional[int] = None,
    user_email: Optional[str] = None
) -> ToolResult:
    """Get user information"""
    
    client = get_zulip_client(email, api_key, server_url)
    
    try:
        # Determine which endpoint to use
        if user_id:
            endpoint = f"users/{user_id}"
        elif user_email:
            endpoint = f"users/{user_email}"
        else:
            # Get own user info
            endpoint = "users/me"
            
        # Get user info
        result = client.call_endpoint(
            url=endpoint,
            method="GET"
        )
        
        user_data = result.get("user", result)
        user_info = f"Name: {user_data.get('full_name', 'N/A')}\n"
        user_info += f"Email: {user_data.get('email', 'N/A')}\n"
        user_info += f"User ID: {user_data.get('user_id', 'N/A')}\n"
        user_info += f"Role: {user_data.get('role', 'N/A')}\n"
        
        return ToolResult(
            content=[
                TextContent(
                    text=user_info
                )
            ]
        )
        
    except Exception as e:
        return ToolResult(
            content=[
                TextContent(
                    text=f"Failed to get user info: {str(e)}"
                )
            ],
            isError=True
        )

async def add_reaction_tool(
    email: str,
    api_key: str,
    server_url: str,
    message_id: int,
    emoji_name: str
) -> ToolResult:
    """Add a reaction to a message"""
    
    client = get_zulip_client(email, api_key, server_url)
    
    try:
        # Prepare the request
        request = {
            "message_id": message_id,
            "emoji_name": emoji_name
        }
        
        # Add reaction
        result = client.call_endpoint(
            url=f"messages/{message_id}/reactions",
            method="POST",
            request=request
        )
        
        return ToolResult(
            content=[
                TextContent(
                    text=f"Reaction '{emoji_name}' added to message {message_id} successfully!"
                )
            ]
        )
        
    except Exception as e:
        return ToolResult(
            content=[
                TextContent(
                    text=f"Failed to add reaction: {str(e)}"
                )
            ],
            isError=True
        )

# Define tools
tools: List[Tool] = [
    Tool(
        name="zulip_send_message",
        description="Send a message to a Zulip channel or user",
        inputSchema={
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "Zulip email address"},
                "api_key": {"type": "string", "description": "Zulip API key"},
                "server_url": {"type": "string", "description": "Zulip server URL"},
                "content": {"type": "string", "description": "Message content"},
                "stream": {"type": "string", "description": "Channel name (optional)"},
                "topic": {"type": "string", "description": "Topic name (optional)"},
                "user_ids": {
                    "type": "array", 
                    "items": {"type": "integer"},
                    "description": "User IDs for private messages (optional)"
                }
            },
            "required": ["email", "api_key", "server_url", "content"]
        }
    ),
    Tool(
        name="zulip_get_messages",
        description="Get messages from a Zulip channel or topic",
        inputSchema={
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "Zulip email address"},
                "api_key": {"type": "string", "description": "Zulip API key"},
                "server_url": {"type": "string", "description": "Zulip server URL"},
                "stream": {"type": "string", "description": "Channel name (optional)"},
                "topic": {"type": "string", "description": "Topic name (optional)"},
                "num_before": {"type": "integer", "description": "Number of messages before anchor", "default": 10},
                "num_after": {"type": "integer", "description": "Number of messages after anchor", "default": 0}
            },
            "required": ["email", "api_key", "server_url"]
        }
    ),
    Tool(
        name="zulip_create_channel",
        description="Create a new Zulip channel",
        inputSchema={
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "Zulip email address"},
                "api_key": {"type": "string", "description": "Zulip API key"},
                "server_url": {"type": "string", "description": "Zulip server URL"},
                "name": {"type": "string", "description": "Channel name"},
                "description": {"type": "string", "description": "Channel description (optional)"},
                "subscribers": {
                    "type": "array", 
                    "items": {"type": "integer"},
                    "description": "User IDs to subscribe to the channel (optional)"
                }
            },
            "required": ["email", "api_key", "server_url", "name"]
        }
    ),
    Tool(
        name="zulip_list_channels",
        description="List all Zulip channels",
        inputSchema={
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "Zulip email address"},
                "api_key": {"type": "string", "description": "Zulip API key"},
                "server_url": {"type": "string", "description": "Zulip server URL"}
            },
            "required": ["email", "api_key", "server_url"]
        }
    ),
    Tool(
        name="zulip_delete_message",
        description="Delete a message by ID",
        inputSchema={
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "Zulip email address"},
                "api_key": {"type": "string", "description": "Zulip API key"},
                "server_url": {"type": "string", "description": "Zulip server URL"},
                "message_id": {"type": "integer", "description": "ID of the message to delete"}
            },
            "required": ["email", "api_key", "server_url", "message_id"]
        }
    ),
    Tool(
        name="zulip_delete_channel",
        description="Archive a channel by ID",
        inputSchema={
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "Zulip email address"},
                "api_key": {"type": "string", "description": "Zulip API key"},
                "server_url": {"type": "string", "description": "Zulip server URL"},
                "stream_id": {"type": "integer", "description": "ID of the channel to archive"}
            },
            "required": ["email", "api_key", "server_url", "stream_id"]
        }
    ),
    Tool(
        name="zulip_get_user_info",
        description="Get information about a user",
        inputSchema={
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "Zulip email address"},
                "api_key": {"type": "string", "description": "Zulip API key"},
                "server_url": {"type": "string", "description": "Zulip server URL"},
                "user_id": {"type": "integer", "description": "User ID (optional)"},
                "user_email": {"type": "string", "description": "User email (optional)"}
            },
            "required": ["email", "api_key", "server_url"]
        }
    ),
    Tool(
        name="zulip_add_reaction",
        description="Add a reaction to a message",
        inputSchema={
            "type": "object",
            "properties": {
                "email": {"type": "string", "description": "Zulip email address"},
                "api_key": {"type": "string", "description": "Zulip API key"},
                "server_url": {"type": "string", "description": "Zulip server URL"},
                "message_id": {"type": "integer", "description": "ID of the message to react to"},
                "emoji_name": {"type": "string", "description": "Name of the emoji to react with"}
            },
            "required": ["email", "api_key", "server_url", "message_id", "emoji_name"]
        }
    )
]

@app.on_tool_call
async def handle_tool_call(tool_call: ToolCall) -> ToolResult:
    """Handle tool calls from the MCP protocol"""
    tool_name = tool_call.name
    args = tool_call.arguments
    
    if tool_name == "zulip_send_message":
        return await send_message_tool(**args)
    elif tool_name == "zulip_get_messages":
        return await get_messages_tool(**args)
    elif tool_name == "zulip_create_channel":
        return await create_channel_tool(**args)
    elif tool_name == "zulip_list_channels":
        return await list_channels_tool(**args)
    elif tool_name == "zulip_delete_message":
        return await delete_message_tool(**args)
    elif tool_name == "zulip_delete_channel":
        return await delete_channel_tool(**args)
    elif tool_name == "zulip_get_user_info":
        return await get_user_info_tool(**args)
    elif tool_name == "zulip_add_reaction":
        return await add_reaction_tool(**args)
    else:
        return ToolResult(
            content=[
                TextContent(
                    text=f"Unknown tool: {tool_name}"
                )
            ],
            isError=True
        )

@app.on_list_tools
async def handle_list_tools() -> List[Tool]:
    """Return the list of available tools"""
    return tools

if __name__ == "__main__":
    # Run the MCP server
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--stdio":
        # Run with stdio interface
        app.run_stdio()
    else:
        # Run with default configuration
        app.run()