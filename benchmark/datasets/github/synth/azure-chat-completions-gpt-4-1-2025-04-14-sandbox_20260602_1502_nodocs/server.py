import sys
from fastmcp import FastMCP

# Import all tool modules to register tools
import generated_tools.issues
import generated_tools.pull_requests
import generated_tools.repos
import generated_tools.contents
import generated_tools.releases
import generated_tools.actions
import generated_tools.search
import generated_tools.webhooks
import generated_tools.branch_protection

if __name__ == "__main__":
    FastMCP().run_stdio()
