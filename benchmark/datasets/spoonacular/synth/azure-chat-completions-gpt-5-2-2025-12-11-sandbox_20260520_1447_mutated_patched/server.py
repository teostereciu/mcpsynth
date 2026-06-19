import json

from mcp.server.fastmcp import FastMCP

from generated_tools.ingredients import (
    compute_ingredient_amount,
    convert_amounts,
    get_ingredient_information,
    ingredient_search,
    parse_ingredients,
)
from generated_tools.meal_planning import connect_user, generate_meal_plan, get_meal_plan_day, get_meal_plan_week
from generated_tools.menu_items import autocomplete_menu_item_search, get_menu_item_information, search_menu_items
from generated_tools.misc import detect_food_in_text, quick_answer, search_all_food, search_food_videos, search_site_content
from generated_tools.products import get_product_information, search_grocery_products, search_grocery_products_by_upc
from generated_tools.recipes import search_recipes_complex
from generated_tools.wine import wine_description, wine_dish_pairing, wine_pairing, wine_recommendation


mcp = FastMCP("spoonacular")


# Recipes
@mcp.tool()
def search_recipes_complex_tool(**kwargs):
    return search_recipes_complex(**kwargs)


# Ingredients
@mcp.tool()
def ingredient_search_tool(**kwargs):
    return ingredient_search(**kwargs)


@mcp.tool()
def get_ingredient_information_tool(**kwargs):
    return get_ingredient_information(**kwargs)


@mcp.tool()
def compute_ingredient_amount_tool(**kwargs):
    return compute_ingredient_amount(**kwargs)


@mcp.tool()
def convert_amounts_tool(**kwargs):
    return convert_amounts(**kwargs)


@mcp.tool()
def parse_ingredients_tool(**kwargs):
    return parse_ingredients(**kwargs)


# Meal planning
@mcp.tool()
def get_meal_plan_week_tool(**kwargs):
    return get_meal_plan_week(**kwargs)


@mcp.tool()
def get_meal_plan_day_tool(**kwargs):
    return get_meal_plan_day(**kwargs)


@mcp.tool()
def generate_meal_plan_tool(**kwargs):
    return generate_meal_plan(**kwargs)


@mcp.tool()
def connect_user_tool(**kwargs):
    return connect_user(**kwargs)


# Menu items
@mcp.tool()
def search_menu_items_tool(**kwargs):
    return search_menu_items(**kwargs)


@mcp.tool()
def get_menu_item_information_tool(**kwargs):
    return get_menu_item_information(**kwargs)


@mcp.tool()
def autocomplete_menu_item_search_tool(**kwargs):
    return autocomplete_menu_item_search(**kwargs)


# Products
@mcp.tool()
def search_grocery_products_tool(**kwargs):
    return search_grocery_products(**kwargs)


@mcp.tool()
def search_grocery_products_by_upc_tool(**kwargs):
    return search_grocery_products_by_upc(**kwargs)


@mcp.tool()
def get_product_information_tool(**kwargs):
    return get_product_information(**kwargs)


# Misc
@mcp.tool()
def search_all_food_tool(**kwargs):
    return search_all_food(**kwargs)


@mcp.tool()
def search_food_videos_tool(**kwargs):
    return search_food_videos(**kwargs)


@mcp.tool()
def quick_answer_tool(**kwargs):
    return quick_answer(**kwargs)


@mcp.tool()
def detect_food_in_text_tool(**kwargs):
    return detect_food_in_text(**kwargs)


@mcp.tool()
def search_site_content_tool(**kwargs):
    return search_site_content(**kwargs)


# Wine
@mcp.tool()
def wine_dish_pairing_tool(**kwargs):
    return wine_dish_pairing(**kwargs)


@mcp.tool()
def wine_pairing_tool(**kwargs):
    return wine_pairing(**kwargs)


@mcp.tool()
def wine_description_tool(**kwargs):
    return wine_description(**kwargs)


@mcp.tool()
def wine_recommendation_tool(**kwargs):
    return wine_recommendation(**kwargs)


if __name__ == "__main__":
    mcp.run()
