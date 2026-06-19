import json
import os
from typing import Any, Dict

import requests
from mcp.server.fastmcp import FastMCP

from generated_tools.ingredients import *  # noqa: F401,F403
from generated_tools.meal_planning import *  # noqa: F401,F403
from generated_tools.menu_items import *  # noqa: F401,F403
from generated_tools.misc import *  # noqa: F401,F403
from generated_tools.products import *  # noqa: F401,F403
from generated_tools.recipes import *  # noqa: F401,F403
from generated_tools.wine import *  # noqa: F401,F403

BASE_URL = "https://api.spoonacular.com"
API_KEY_ENV = "SPOONACULAR_API_KEY"

mcp = FastMCP("spoonacular-food-api")


def _request(method: str, path: str, params: Dict[str, Any] | None = None, data: Dict[str, Any] | None = None):
    api_key = os.getenv(API_KEY_ENV)
    if not api_key:
        return {"error": f"Missing environment variable {API_KEY_ENV}"}
    try:
        query = dict(params or {})
        query["apiKey"] = api_key
        resp = requests.request(method, f"{BASE_URL}{path}", params=query, data=data, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        try:
            return {"error": resp.json()}
        except Exception:
            return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def list_tools() -> Dict[str, Any]:
    return {"tools": [name for name in globals() if callable(globals()[name]) and not name.startswith("_") and name not in {"FastMCP", "Dict", "Any", "json", "os", "requests", "list_tools"}]}


if __name__ == "__main__":
    mcp.run()
