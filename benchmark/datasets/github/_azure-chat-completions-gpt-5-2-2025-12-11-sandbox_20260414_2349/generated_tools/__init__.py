"""GitHub MCP server tools package."""

from __future__ import annotations

from fastmcp import FastMCP

mcp = FastMCP("github-mcp")

# Import modules to register tools
from . import issues as _issues  # noqa: F401
from . import pulls as _pulls  # noqa: F401
from . import repos as _repos  # noqa: F401
from . import releases as _releases  # noqa: F401
from . import actions as _actions  # noqa: F401
from . import webhooks as _webhooks  # noqa: F401
from . import gitdata as _gitdata  # noqa: F401
from . import search as _search  # noqa: F401
from . import activity as _activity  # noqa: F401
from . import labels as _labels  # noqa: F401
from . import statuses as _statuses  # noqa: F401
