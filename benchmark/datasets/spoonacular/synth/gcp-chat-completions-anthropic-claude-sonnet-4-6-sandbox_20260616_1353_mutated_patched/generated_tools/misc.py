"""
Spoonacular Miscellaneous API tools.
Source: docs/api_misc.md
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


def _post(path: str, params: dict, data: dict) -> dict | list:
    params["apiKey"] = _api_key()
    try:
        resp = requests.post(BASE_URL + path, params=params, data=data, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}


def register_misc(mcp: FastMCP):

    @mcp.tool()
    def search_all_food(
        search_query: str,
        offset: int = 0,
        number: int = 10,
    ) -> dict:
        """Search all food content with one call: recipes, grocery products, menu items,
        simple foods (ingredients), and food videos."""
        params = {"query": search_query, "offset": offset, "number": number}
        return _get("/food/search", params)

    @mcp.tool()
    def search_food_videos(
        search_query: str,
        type: str = "",
        cuisine: str = "",
        diet_type: str = "",
        ingredients: str = "",
        exclude_ingredients: str = "",
        min_length: float = None,
        max_length: float = None,
        offset: int = 0,
        number: int = 10,
    ) -> dict:
        """Search for recipe and food-related YouTube videos. Filter by meal type, cuisine, diet, and ingredients."""
        params = {"query": search_query, "offset": offset, "number": number}
        if type:
            params["type"] = type
        if cuisine:
            params["cuisine"] = cuisine
        if diet_type:
            params["diet"] = diet_type
        if ingredients:
            params["includeIngredients"] = ingredients
        if exclude_ingredients:
            params["excludeIngredients"] = exclude_ingredients
        if min_length is not None:
            params["minLength"] = min_length
        if max_length is not None:
            params["maxLength"] = max_length
        return _get("/food/videos/search", params)

    @mcp.tool()
    def quick_answer(q: str) -> dict:
        """Answer a nutrition-related natural language question.
        E.g. 'How much vitamin C is in 2 apples?'"""
        params = {"q": q}
        return _get("/recipes/quickAnswer", params)

    @mcp.tool()
    def detect_food_in_text(text: str) -> dict:
        """Detect and identify food mentions (dishes and ingredients) in any text using Named Entity Recognition (NER)."""
        data = {"text": text}
        return _post("/food/detect", {}, data)

    @mcp.tool()
    def search_site_content(search_query: str) -> dict:
        """Search spoonacular's site content including recipes, articles, grocery products, and more.
        Supports partial queries (e.g. 'spagh' finds spaghetti content)."""
        params = {"query": search_query}
        return _get("/food/site/search", params)

    @mcp.tool()
    def get_random_food_joke() -> dict:
        """Get a random food-related joke."""
        return _get("/food/jokes/random", {})

    @mcp.tool()
    def get_random_food_trivia() -> dict:
        """Get a random food trivia fact."""
        return _get("/food/trivia/random", {})

    @mcp.tool()
    def talk_to_chatbot(
        text: str,
        context_id: str = "",
    ) -> dict:
        """Talk to the spoonacular chatbot about food and recipes.
        Optionally provide a context_id to continue a conversation."""
        params = {"text": text}
        if context_id:
            params["contextId"] = context_id
        return _get("/food/converse", params)

    @mcp.tool()
    def get_conversation_suggests(
        query: str,
        number: float = None,
    ) -> dict:
        """Get conversation suggestions for the spoonacular chatbot based on a partial query."""
        params = {"query": query}
        if number is not None:
            params["number"] = number
        return _get("/food/converse/suggest", params)
