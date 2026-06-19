from fastmcp import FastMCP

mcp = FastMCP("google-workspace")

# Import tool modules so decorators register tools.
from . import gmail  # noqa: E402,F401
from . import calendar  # noqa: E402,F401
from . import drive  # noqa: E402,F401
from . import docs  # noqa: E402,F401
from . import slides  # noqa: E402,F401
from . import sheets  # noqa: E402,F401
