from typing import Optional, Dict, Any
from .recipes import make_request

def get_wine_pairing(food: str, maxPrice: Optional[float] = None) -> Any:
    """Get wine pairing for a specific food/dish."""
    params = {"food": food}
    if maxPrice is not None: params["maxPrice"] = maxPrice
    return make_request("GET", "/food/wine/pairing", params=params)

def get_wine_description(wine: str) -> Any:
    """Get description for a specific wine."""
    params = {"wine": wine}
    return make_request("GET", "/food/wine/description", params=params)
