from typing import Any, Dict

from .http import request_json


def recipes_get_nutrition_widget_json(id: int) -> Dict[str, Any]:
    return request_json("GET", f"/recipes/{id}/nutritionWidget.json", params={})


def recipes_get_nutrition_widget(id: int) -> Dict[str, Any]:
    # Returns HTML; wrapped in {"result": ...}
    return request_json("GET", f"/recipes/{id}/nutritionWidget", params={})
