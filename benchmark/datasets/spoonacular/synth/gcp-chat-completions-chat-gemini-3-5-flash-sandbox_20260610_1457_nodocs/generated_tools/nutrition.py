from typing import Dict, Any
from generated_tools.client import request

def get_recipe_nutrition(id: int) -> Dict[str, Any]:
    """
    Get nutritional information for a recipe by its ID.
    
    Args:
        id: The recipe ID.
    """
    return request("GET", f"/recipes/{id}/nutritionWidget.json")
