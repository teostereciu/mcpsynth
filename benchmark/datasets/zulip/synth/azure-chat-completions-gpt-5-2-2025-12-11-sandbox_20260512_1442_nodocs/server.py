from mcp.server.fastmcp import FastMCP

from zulip_client import ZulipClient

from generated_tools import messages, streams, topics, users, scheduled, drafts, files


mcp = FastMCP("zulip")
client = ZulipClient()

messages.register(mcp, client)
streams.register(mcp, client)
topics.register(mcp, client)
users.register(mcp, client)
scheduled.register(mcp, client)
drafts.register(mcp, client)
files.register(mcp, client)


if __name__ == "__main__":
    mcp.run()
