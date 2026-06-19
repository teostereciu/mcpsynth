from mcp_server import mcp

import tools.issues
import tools.pulls
import tools.repos
import tools.releases
import tools.actions
import tools.search
import tools.webhooks
import tools.branches

if __name__ == "__main__":
    mcp.run()
