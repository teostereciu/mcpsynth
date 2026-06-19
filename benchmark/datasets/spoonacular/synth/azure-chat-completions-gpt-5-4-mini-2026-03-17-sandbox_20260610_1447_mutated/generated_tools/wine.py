from typing import Any, Dict
from generated_tools.spoonacular_client import request


def dish_pairing_for_wine(**kwargs) -> Dict[str, Any]:
    return request("GET", "/food/wine/dishes", params=kwargs)


def wine_pairing(**kwargs) -> Dict[str, Any]:
    return request("GET", "/food/wine/pairing", params=kwargs)


def wine_description(**kwargs) -> Dict[str, Any]:
    return request("GET", "/food/wine/description", params=kwargs)
