"""
MCP Server for the Spoonacular Food API.

Exposes tools across six domains:
  - Recipes       (search, details, nutrition, instructions, similar, random, …)
  - Ingredients   (search, info, substitutes, parse, autocomplete, …)
  - Meal Planning (daily/weekly plans, shopping lists, …)
  - Nutrition     (analyze, glycemic load, food detection, videos, chatbot)
  - Wine          (pairing, description, recommendation)
  - Products      (grocery search, UPC lookup, classify, …)
  - Menu Items    (restaurant menu search, info, autocomplete)

Run with:
    python server.py
"""

from mcp.server.fastmcp import FastMCP

# ── domain modules ──────────────────────────────────────────────────────────
from generated_tools.recipes import (
    complex_recipe_search,
    search_recipes_by_ingredients,
    search_recipes_by_nutrients,
    autocomplete_recipe_search,
    get_recipe_information,
    get_recipe_information_bulk,
    get_recipe_ingredients,
    get_recipe_nutrition,
    get_recipe_instructions,
    get_similar_recipes,
    get_random_recipes,
    summarize_recipe,
    get_recipe_taste,
    analyze_recipe_instructions,
    guess_nutrition_by_dish_name,
    classify_cuisine,
)
from generated_tools.ingredients import (
    search_ingredients,
    get_ingredient_information,
    get_ingredient_substitutes,
    get_ingredient_substitutes_by_id,
    autocomplete_ingredient_search,
    parse_ingredients,
    compute_ingredient_amount,
    get_ingredient_nutrition_by_id,
)
from generated_tools.meal_planning import (
    generate_meal_plan_daily,
    generate_meal_plan_weekly,
    get_meal_plan_week,
    get_meal_plan_day,
    add_meal_plan_item,
    delete_meal_plan_item,
    get_meal_plan_templates,
    get_shopping_list,
    add_to_shopping_list,
    delete_from_shopping_list,
)
from generated_tools.nutrition import (
    get_recipe_nutrition_by_id,
    get_recipe_nutrition_label,
    analyze_recipe_nutrition,
    compute_glycemic_load,
    detect_food_in_text,
    search_food_videos,
    get_random_food_videos,
    get_conversation_suggests,
    talk_to_chatbot,
)
from generated_tools.wine import (
    get_dish_pairing_for_wine,
    get_wine_pairing_for_dish,
    get_wine_description,
    get_wine_recommendation,
)
from generated_tools.products import (
    search_grocery_products,
    get_product_information,
    get_comparable_products,
    search_grocery_products_by_upc,
    autocomplete_product_search,
    classify_grocery_product,
    classify_grocery_product_bulk,
    get_product_nutrition_by_id,
)
from generated_tools.menu_items import (
    search_menu_items,
    get_menu_item_information,
    autocomplete_menu_item_search,
    get_menu_item_nutrition_by_id,
)

# ── server ───────────────────────────────────────────────────────────────────
mcp = FastMCP(
    name="spoonacular",
    description="Comprehensive Spoonacular Food API — recipes, ingredients, "
                "meal planning, nutrition, wine pairing, grocery products, "
                "and restaurant menu items.",
)

# ── Recipe tools ─────────────────────────────────────────────────────────────
mcp.tool()(complex_recipe_search)
mcp.tool()(search_recipes_by_ingredients)
mcp.tool()(search_recipes_by_nutrients)
mcp.tool()(autocomplete_recipe_search)
mcp.tool()(get_recipe_information)
mcp.tool()(get_recipe_information_bulk)
mcp.tool()(get_recipe_ingredients)
mcp.tool()(get_recipe_nutrition)
mcp.tool()(get_recipe_instructions)
mcp.tool()(get_similar_recipes)
mcp.tool()(get_random_recipes)
mcp.tool()(summarize_recipe)
mcp.tool()(get_recipe_taste)
mcp.tool()(analyze_recipe_instructions)
mcp.tool()(guess_nutrition_by_dish_name)
mcp.tool()(classify_cuisine)

# ── Ingredient tools ──────────────────────────────────────────────────────────
mcp.tool()(search_ingredients)
mcp.tool()(get_ingredient_information)
mcp.tool()(get_ingredient_substitutes)
mcp.tool()(get_ingredient_substitutes_by_id)
mcp.tool()(autocomplete_ingredient_search)
mcp.tool()(parse_ingredients)
mcp.tool()(compute_ingredient_amount)
mcp.tool()(get_ingredient_nutrition_by_id)

# ── Meal Planning tools ───────────────────────────────────────────────────────
mcp.tool()(generate_meal_plan_daily)
mcp.tool()(generate_meal_plan_weekly)
mcp.tool()(get_meal_plan_week)
mcp.tool()(get_meal_plan_day)
mcp.tool()(add_meal_plan_item)
mcp.tool()(delete_meal_plan_item)
mcp.tool()(get_meal_plan_templates)
mcp.tool()(get_shopping_list)
mcp.tool()(add_to_shopping_list)
mcp.tool()(delete_from_shopping_list)

# ── Nutrition tools ───────────────────────────────────────────────────────────
mcp.tool()(get_recipe_nutrition_by_id)
mcp.tool()(get_recipe_nutrition_label)
mcp.tool()(analyze_recipe_nutrition)
mcp.tool()(compute_glycemic_load)
mcp.tool()(detect_food_in_text)
mcp.tool()(search_food_videos)
mcp.tool()(get_random_food_videos)
mcp.tool()(get_conversation_suggests)
mcp.tool()(talk_to_chatbot)

# ── Wine tools ────────────────────────────────────────────────────────────────
mcp.tool()(get_dish_pairing_for_wine)
mcp.tool()(get_wine_pairing_for_dish)
mcp.tool()(get_wine_description)
mcp.tool()(get_wine_recommendation)

# ── Grocery Product tools ─────────────────────────────────────────────────────
mcp.tool()(search_grocery_products)
mcp.tool()(get_product_information)
mcp.tool()(get_comparable_products)
mcp.tool()(search_grocery_products_by_upc)
mcp.tool()(autocomplete_product_search)
mcp.tool()(classify_grocery_product)
mcp.tool()(classify_grocery_product_bulk)
mcp.tool()(get_product_nutrition_by_id)

# ── Menu Item tools ───────────────────────────────────────────────────────────
mcp.tool()(search_menu_items)
mcp.tool()(get_menu_item_information)
mcp.tool()(autocomplete_menu_item_search)
mcp.tool()(get_menu_item_nutrition_by_id)


if __name__ == "__main__":
    mcp.run(transport="stdio")
