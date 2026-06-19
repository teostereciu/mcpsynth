from typing import Any, Dict

from server import _request


def wine_dish_pairing(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/wine/dishes", params=params)


def wine_pairing(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/wine/pairing", params=params)


def wine_description(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/wine/description", params=params)


def wine_recommendation(**params: Any) -> Dict[str, Any]:
    return _request("GET", "/food/wine/recommendation", params=params)
