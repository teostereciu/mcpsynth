from mcp.server.fastmcp import FastMCP

from generated_tools import (
    analyze_recipe,
    analyze_recipe_instructions,
    analyze_recipe_search_query,
    autocomplete_menu_item_search,
    autocomplete_recipe_search,
    classify_cuisine,
    compute_ingredient_amount,
    connect_user,
    convert_amounts,
    detect_food_in_text,
    dish_pairing_for_wine,
    extract_recipe_from_website,
    generate_meal_plan,
    get_analyzed_recipe_instructions,
    get_ingredient_information,
    get_meal_plan_day,
    get_meal_plan_week,
    get_menu_item_information,
    get_product_information,
    get_random_recipes,
    get_recipe_information,
    get_recipe_information_bulk,
    get_similar_recipes,
    ingredient_search,
    ingredients_by_id,
    nutrition_by_id,
    parse_ingredients,
    price_breakdown_by_id,
    quick_answer,
    search_all_food,
    search_food_videos,
    search_grocery_products,
    search_grocery_products_by_upc,
    search_menu_items,
    search_recipes_by_ingredients,
    search_recipes_by_nutrients,
    search_recipes_complex,
    search_site_content,
    summarize_recipe,
    taste_by_id,
    wine_description,
    wine_pairing,
    wine_recommendation,
    equipment_by_id,
)

mcp = FastMCP("spoonacular-food-api")


@mcp.tool()
def recipes_search_complex(**kwargs):
    return search_recipes_complex(**kwargs)


@mcp.tool()
def recipes_search_by_nutrients(**kwargs):
    return search_recipes_by_nutrients(**kwargs)


@mcp.tool()
def recipes_search_by_ingredients(**kwargs):
    return search_recipes_by_ingredients(**kwargs)


@mcp.tool()
def recipes_get_information(id: int, includeNutrition: bool | None = None):
    return get_recipe_information(id=id, includeNutrition=includeNutrition)


@mcp.tool()
def recipes_get_information_bulk(ids: str, includeNutrition: bool | None = None):
    return get_recipe_information_bulk(ids=ids, includeNutrition=includeNutrition)


@mcp.tool()
def recipes_get_similar(id: int, number: int | None = None):
    return get_similar_recipes(id=id, number=number)


@mcp.tool()
def recipes_get_random(number: int | None = None, tags: str | None = None):
    return get_random_recipes(number=number, tags=tags)


@mcp.tool()
def recipes_autocomplete(search_query: str, number: int | None = None):
    return autocomplete_recipe_search(search_query=search_query, number=number)


@mcp.tool()
def recipes_taste_by_id(id: int, normalize: bool | None = None):
    return taste_by_id(id=id, normalize=normalize)


@mcp.tool()
def recipes_equipment_by_id(id: int):
    return equipment_by_id(id=id)


@mcp.tool()
def recipes_price_breakdown_by_id(id: int):
    return price_breakdown_by_id(id=id)


@mcp.tool()
def recipes_ingredients_widget_by_id(id: int):
    return ingredients_by_id(id=id)


@mcp.tool()
def recipes_nutrition_widget_by_id(id: int):
    return nutrition_by_id(id=id)


@mcp.tool()
def recipes_get_analyzed_instructions(id: int, stepBreakdown: bool | None = None):
    return get_analyzed_recipe_instructions(id=id, stepBreakdown=stepBreakdown)


@mcp.tool()
def recipes_extract_from_website(url: str, forceExtraction: bool | None = None, analyze: bool | None = None):
    return extract_recipe_from_website(url=url, forceExtraction=forceExtraction, analyze=analyze)


@mcp.tool()
def recipes_analyze(title: str, ingredientList: str, servings: int, instructions: str | None = None, language: str | None = None, includeNutrition: bool | None = None, includeTaste: bool | None = None):
    return analyze_recipe(title=title, ingredientList=ingredientList, servings=servings, instructions=instructions, language=language, includeNutrition=includeNutrition, includeTaste=includeTaste)


@mcp.tool()
def recipes_summarize(id: int):
    return summarize_recipe(id=id)


@mcp.tool()
def recipes_analyze_instructions(instructions: str):
    return analyze_recipe_instructions(instructions=instructions)


@mcp.tool()
def recipes_classify_cuisine(title: str, ingredientList: str, language: str | None = None):
    return classify_cuisine(title=title, ingredientList=ingredientList, language=language)


@mcp.tool()
def recipes_analyze_search_query(q: str):
    return analyze_recipe_search_query(q=q)


@mcp.tool()
def ingredients_search(**kwargs):
    return ingredient_search(**kwargs)


@mcp.tool()
def ingredients_get_information(id: int, amount: float | None = None, unit: str | None = None, locale: str | None = None):
    return get_ingredient_information(id=id, amount=amount, unit=unit, locale=locale)


@mcp.tool()
def ingredients_compute_amount(id: int, nutrient: str, target: float, unit: str | None = None):
    return compute_ingredient_amount(id=id, nutrient=nutrient, target=target, unit=unit)


@mcp.tool()
def ingredients_convert_amounts(ingredientName: str, sourceAmount: float, sourceUnit: str, targetUnit: str):
    return convert_amounts(ingredientName=ingredientName, sourceAmount=sourceAmount, sourceUnit=sourceUnit, targetUnit=targetUnit)


@mcp.tool()
def ingredients_parse(ingredientList: str, servings: int, includeNutrition: bool | None = None, language: str | None = None):
    return parse_ingredients(ingredientList=ingredientList, servings=servings, includeNutrition=includeNutrition, language=language)


@mcp.tool()
def meal_planning_connect_user(username: str, firstName: str | None = None, lastName: str | None = None, email: str | None = None):
    return connect_user(username=username, firstName=firstName, lastName=lastName, email=email)


@mcp.tool()
def meal_planning_get_week(username: str, start_date: str, hash: str):
    return get_meal_plan_week(username=username, start_date=start_date, hash=hash)


@mcp.tool()
def meal_planning_get_day(username: str, date: str, hash: str):
    return get_meal_plan_day(username=username, date=date, hash=hash)


@mcp.tool()
def meal_planning_generate(timeFrame: str, targetCalories: int | None = None, diet: str | None = None, exclude: str | None = None):
    return generate_meal_plan(timeFrame=timeFrame, targetCalories=targetCalories, diet=diet, exclude=exclude)


@mcp.tool()
def menu_items_search(**kwargs):
    return search_menu_items(**kwargs)


@mcp.tool()
def menu_items_get_information(id: int):
    return get_menu_item_information(id=id)


@mcp.tool()
def menu_items_autocomplete(search_query: str, number: int | None = None):
    return autocomplete_menu_item_search(search_query=search_query, number=number)


@mcp.tool()
def products_search(**kwargs):
    return search_grocery_products(**kwargs)


@mcp.tool()
def products_get_by_upc(upc: str):
    return search_grocery_products_by_upc(upc=upc)


@mcp.tool()
def products_get_information(id: int):
    return get_product_information(id=id)


@mcp.tool()
def misc_search_all_food(search_query: str, offset: int | None = None, number: int | None = None):
    return search_all_food(search_query=search_query, offset=offset, number=number)


@mcp.tool()
def misc_search_food_videos(**kwargs):
    return search_food_videos(**kwargs)


@mcp.tool()
def misc_quick_answer(q: str):
    return quick_answer(q=q)


@mcp.tool()
def misc_detect_food_in_text(text: str):
    return detect_food_in_text(text=text)


@mcp.tool()
def misc_search_site_content(search_query: str):
    return search_site_content(search_query=search_query)


@mcp.tool()
def wine_dish_pairing(wine: str):
    return dish_pairing_for_wine(wine=wine)


@mcp.tool()
def wine_pair_food(food: str, maxPrice: float | None = None):
    return wine_pairing(food=food, maxPrice=maxPrice)


@mcp.tool()
def wine_get_description(wine: str):
    return wine_description(wine=wine)


@mcp.tool()
def wine_get_recommendation(wine: str, maxPrice: float | None = None, minRating: float | None = None, number: int | None = None):
    return wine_recommendation(wine=wine, maxPrice=maxPrice, minRating=minRating, number=number)


if __name__ == "__main__":
    mcp.run()
