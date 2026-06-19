from __future__ import annotations

from fastmcp import FastMCP

mcp = FastMCP("slack-mcp")

# Register tools by importing modules (side-effect registration).
from . import auth as _auth  # noqa: F401
from . import chat as _chat  # noqa: F401
from . import conversations as _conversations  # noqa: F401
from . import users as _users  # noqa: F401
from . import reactions as _reactions  # noqa: F401
from . import files as _files  # noqa: F401
from . import pins as _pins  # noqa: F401
from . import search as _search  # noqa: F401
from . import team as _team  # noqa: F401
from . import dnd as _dnd  # noqa: F401
from . import emoji as _emoji  # noqa: F401
from . import views as _views  # noqa: F401
from . import bookmarks as _bookmarks  # noqa: F401
from . import reminders as _reminders  # noqa: F401
from . import usergroups as _usergroups  # noqa: F401
from . import bots as _bots  # noqa: F401

__all__ = ["mcp"]
