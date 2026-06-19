from typing import Optional, Dict, Any
from generated_tools.client import request

def get_wine_pairing(
    food: str,
    maxPrice: Optional[float] = None
) -> Dict[str, Any]:
    """
    Get wine pairings for a given food/dish.
    
    Args:
        food: The food/dish to pair wine with (e.g., "steak", "salmon").
        maxPrice: The maximum price of the wine in USD.
    """
    params = {"food": food}
    if maxPrice is not None:
        params["maxPrice"] = maxPrice
        
    return request("GET", "/food/wine/pairing", params=params)

def get_wine_description(wine: str) -> Dict[str, Any]:
    """
    Get a description and information about a specific wine type.
    
    Args:
        wine: The wine type (e.g., "merlot", "chardonnay").
    """
    params = {"wine": wine}
    return request("GET", "/food/wine/description", params=params)
