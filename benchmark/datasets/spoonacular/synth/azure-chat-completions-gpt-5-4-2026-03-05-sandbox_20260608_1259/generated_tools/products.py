from typing import Any, Optional

from generated_tools.recipes import _request


def search_grocery_products(
    query: str,
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
    return _request("GET", "/food/products/search", locals())


def search_grocery_products_by_upc(upc: str) -> Any:
    return _request("GET", f"/food/products/upc/{upc}")


def get_product_information(id: int) -> Any:
    return _request("GET", f"/food/products/{id}")


def autocomplete_product_search(query: str, number: Optional[int] = None) -> Any:
    return _request("GET", "/food/products/suggest", locals())
