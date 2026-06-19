from typing import Any, Optional

from .common import spoonacular_request


def search_grocery_products(
    search_query: str,
    minCalories: Optional[float] = None,
    maxCalories: Optional[float] = None,
    minCarbs: Optional[float] = None,
    maxCarbs: Optional[float] = None,
    minProtein: Optional[float] = None,
    maxProtein: Optional[float] = None,
    minFat: Optional[float] = None,
    maxFat: Optional[float] = None,
    addProductInformation: Optional[bool] = None,
    offset: Optional[int] = None,
    number: Optional[int] = None,
) -> Any:
    return spoonacular_request("GET", "/food/products/search", params=locals())


def search_grocery_products_by_upc(upc: str) -> Any:
    return spoonacular_request("GET", f"/food/products/upc/{upc}")


def get_product_information(id: int) -> Any:
    return spoonacular_request("GET", f"/food/products/{id}")
