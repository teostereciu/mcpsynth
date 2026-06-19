from typing import Optional, Dict, Any
from .recipes import make_request

def autocomplete_recipe_search(query: str, number: int = 10) -> Any:
    """Autocomplete recipe search."""
    params = {"query": query, "number": number}
    return make_request("GET", "/recipes/autocomplete", params=params)

def autocomplete_ingredient_search(query: str, number: int = 10) -> Any:
    """Autocomplete ingredient search."""
    params = {"query": query, "number": number}
    return make_request("GET", "/food/ingredients/autocomplete", params=params)
