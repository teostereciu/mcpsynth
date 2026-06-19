import sys
from mcp.server.fastmcp import FastMCP

from generated_tools import messages
from generated_tools import streams
from generated_tools import users
from generated_tools import reactions
from generated_tools import scheduled_messages
from generated_tools import drafts
from generated_tools import uploads


def list_tools():
    tools = []
    tools.extend(messages.list_tools())
    tools.extend(streams.list_tools())
    tools.extend(users.list_tools())
    tools.extend(reactions.list_tools())
    tools.extend(scheduled_messages.list_tools())
    tools.extend(drafts.list_tools())
    tools.extend(uploads.list_tools())
    return tools


def main():
    mcp = FastMCP(
        tools=[
            messages,
            streams,
            users,
            reactions,
            scheduled_messages,
            drafts,
            uploads,
        ],
        list_tools=list_tools,
    )
    mcp.serve_forever()


if __name__ == "__main__":
    main()
