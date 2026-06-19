from typing import Optional, Dict, Any
from .recipes import make_request

def get_recipe_nutrition(id: int) -> Any:
    """Get nutrition for a specific recipe by ID."""
    return make_request("GET", f"/recipes/{id}/nutritionWidget.json")

def visualize_recipe_nutrition(id: int, defaultCss: bool = True) -> Any:
    """Visualize recipe nutrition (returns HTML widget)."""
    params = {"defaultCss": str(defaultCss).lower()}
    return make_request("GET", f"/recipes/{id}/nutritionWidget", params=params)
