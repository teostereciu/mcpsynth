"""
Spoonacular Wine API tools.
Source: docs/api_wine.md
"""

import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.spoonacular.com"


def _api_key() -> str:
    key = os.environ.get("SPOONACULAR_API_KEY", "")
    if not key:
        raise ValueError("SPOONACULAR_API_KEY environment variable is not set")
    return key


def _get(path: str, params: dict) -> dict | list:
    params["apiKey"] = _api_key()
    try:
        resp = requests.get(BASE_URL + path, params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}


def register_wine(mcp: FastMCP):

    @mcp.tool()
    def get_dish_pairing_for_wine(wine: str) -> dict:
        """Find dishes that pair well with a given wine type (e.g. 'malbec', 'riesling', 'merlot')."""
        params = {"wine": wine}
        return _get("/food/wine/dishes", params)

    @mcp.tool()
    def get_wine_pairing(food: str, max_price: float = None) -> dict:
        """Find wines that pair well with a food. Food can be a dish name ('steak'),
        an ingredient ('salmon'), or a cuisine ('italian'). Optionally filter by max price in USD."""
        params = {"food": food}
        if max_price is not None:
            params["maxPrice"] = max_price
        return _get("/food/wine/pairing", params)

    @mcp.tool()
    def get_wine_description(wine: str) -> dict:
        """Get a simple description of a wine type (e.g. 'malbec', 'riesling', 'merlot')."""
        params = {"wine": wine}
        return _get("/food/wine/description", params)

    @mcp.tool()
    def get_wine_recommendation(
        wine: str,
        max_price: float = None,
        min_rating: float = None,
        number: int = 3,
    ) -> dict:
        """Get specific wine product recommendations for a given wine type (e.g. 'merlot').
        Optionally filter by max price (USD) and minimum rating (0-1 scale)."""
        params = {"wine": wine, "number": number}
        if max_price is not None:
            params["maxPrice"] = max_price
        if min_rating is not None:
            params["minRating"] = min_rating
        return _get("/food/wine/recommendation", params)
