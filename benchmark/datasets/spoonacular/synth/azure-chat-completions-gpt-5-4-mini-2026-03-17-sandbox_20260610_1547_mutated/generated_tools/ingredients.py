from generated_tools.common import api_get, api_post


def search_ingredients(**kwargs):
    return api_get("/food/ingredients/search", kwargs)


def get_ingredient_information(ingredient_id, **kwargs):
    return api_get(f"/food/ingredients/{ingredient_id}/information", kwargs)


def compute_ingredient_amount(ingredient_id, **kwargs):
    return api_get(f"/food/ingredients/{ingredient_id}/amount", kwargs)


def autocomplete_ingredient_search(query, **kwargs):
    params = {"query": query, **kwargs}
    return api_get("/food/ingredients/autocomplete", params)
