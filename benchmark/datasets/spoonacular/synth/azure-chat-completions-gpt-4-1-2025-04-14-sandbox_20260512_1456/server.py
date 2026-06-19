import os
from mcp.server.fastmcp import FastMCP
import generated_tools.recipes as recipes
import generated_tools.ingredients as ingredients
import generated_tools.meal_planning as meal_planning
import generated_tools.menu_items as menu_items
import generated_tools.misc as misc
import generated_tools.products as products
import generated_tools.wine as wine

TOOLS = {
    # Recipes
    'search_recipes': recipes.search_recipes,
    'search_recipes_by_nutrients': recipes.search_recipes_by_nutrients,
    'search_recipes_by_ingredients': recipes.search_recipes_by_ingredients,
    'get_recipe_information': recipes.get_recipe_information,
    'get_recipe_ingredients': recipes.get_recipe_ingredients,
    'get_recipe_nutrition': recipes.get_recipe_nutrition,
    'get_recipe_instructions': recipes.get_recipe_instructions,
    'get_similar_recipes': recipes.get_similar_recipes,
    'autocomplete_recipe_search': recipes.autocomplete_recipe_search,
    # Ingredients
    'search_ingredients': ingredients.search_ingredients,
    'get_ingredient_information': ingredients.get_ingredient_information,
    'compute_ingredient_amount': ingredients.compute_ingredient_amount,
    'convert_amounts': ingredients.convert_amounts,
    'parse_ingredients': ingredients.parse_ingredients,
    # Meal Planning
    'get_meal_plan_week': meal_planning.get_meal_plan_week,
    'get_meal_plan_day': meal_planning.get_meal_plan_day,
    'generate_meal_plan': meal_planning.generate_meal_plan,
    # Menu Items
    'search_menu_items': menu_items.search_menu_items,
    'get_menu_item_information': menu_items.get_menu_item_information,
    'autocomplete_menu_item_search': menu_items.autocomplete_menu_item_search,
    # Misc
    'search_all_food': misc.search_all_food,
    'search_food_videos': misc.search_food_videos,
    'quick_answer': misc.quick_answer,
    'detect_food_in_text': misc.detect_food_in_text,
    # Products
    'search_grocery_products': products.search_grocery_products,
    'search_grocery_products_by_upc': products.search_grocery_products_by_upc,
    'get_product_information': products.get_product_information,
    # Wine
    'dish_pairing_for_wine': wine.dish_pairing_for_wine,
    'wine_pairing': wine.wine_pairing,
    'wine_description': wine.wine_description,
    'wine_recommendation': wine.wine_recommendation,
}

def list_tools():
    """
    List all available tools.
    """
    return list(TOOLS.keys())

TOOLS['list_tools'] = list_tools

if __name__ == '__main__':
    FastMCP(TOOLS).run_stdio()
