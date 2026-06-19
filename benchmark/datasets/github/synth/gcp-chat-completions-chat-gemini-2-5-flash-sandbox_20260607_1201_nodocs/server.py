from mcp.server.fastmcp import FastMCP
import os
import requests

# Base URL for GitHub API
GITHUB_API_BASE_URL = os.getenv("GITHUB_API_BASE_URL", "https://api.github.com")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable not set.")

session = requests.Session()
session.headers.update({
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
})

server = FastMCP()

from generated_tools.repositories import get_repository

server.register_tool(get_repository)
server.register_tool(list_user_repositories)
server.register_tool(create_repository_for_authenticated_user)

# Tools will be registered here

if __name__ == "__main__":
    server.run()
