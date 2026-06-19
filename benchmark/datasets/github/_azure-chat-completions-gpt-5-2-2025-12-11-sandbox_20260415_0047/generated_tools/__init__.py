from __future__ import annotations

from fastmcp import FastMCP

mcp = FastMCP("github-mcp")

# Import tool modules so decorators register tools.
from . import issues as _issues  # noqa: F401
from . import pulls as _pulls  # noqa: F401
from . import repos as _repos  # noqa: F401
from . import actions as _actions  # noqa: F401
from . import releases as _releases  # noqa: F401
from . import gitdata as _gitdata  # noqa: F401
from . import search as _search  # noqa: F401
from . import activity as _activity  # noqa: F401
from . import branches as _branches  # noqa: F401
from . import commits as _commits  # noqa: F401
