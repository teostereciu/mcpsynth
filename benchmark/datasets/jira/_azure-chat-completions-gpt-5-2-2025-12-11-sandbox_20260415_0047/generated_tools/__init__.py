from __future__ import annotations

from fastmcp import FastMCP

mcp = FastMCP("jira-cloud")

# Register tools
from . import myself as _myself  # noqa: F401
from . import projects as _projects  # noqa: F401
from . import issues as _issues  # noqa: F401
from . import issue_comments as _issue_comments  # noqa: F401
from . import issue_search as _issue_search  # noqa: F401
from . import issue_transitions as _issue_transitions  # noqa: F401
from . import issue_watchers as _issue_watchers  # noqa: F401
from . import issue_worklogs as _issue_worklogs  # noqa: F401
from . import server_info as _server_info  # noqa: F401
from . import users as _users  # noqa: F401
from . import groups as _groups  # noqa: F401
from . import filters as _filters  # noqa: F401
from . import dashboards as _dashboards  # noqa: F401
from . import metadata as _metadata  # noqa: F401
from . import jql as _jql  # noqa: F401
from . import issue_attachments as _issue_attachments  # noqa: F401
from . import issue_links as _issue_links  # noqa: F401
from . import issue_votes as _issue_votes  # noqa: F401
