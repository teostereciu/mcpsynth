import importlib
from fastmcp import FastMCP, list_tools

# Import all tool modules to register tools
import generated_tools.messages
import generated_tools.streams
import generated_tools.topics
import generated_tools.users
import generated_tools.reactions
import generated_tools.scheduled
import generated_tools.drafts
import generated_tools.files


def main():
    server = FastMCP()
    server.serve_stdio()

if __name__ == "__main__":
    main()
