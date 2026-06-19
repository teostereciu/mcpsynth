"""
MCP Server for the Spoonacular Food API.

Runs over stdio using FastMCP. All tools are registered from the
generated_tools sub-modules.

Usage:
    SPOONACULAR_API_KEY=<your_key> python server.py
"""

from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Import all domain functions
# ---------------------------------------------------------------------------
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
    analyze_recipe_instructions,
    guess_nutrition_by_dish_name,
    get_recipe_price_breakdown,
)
from generated_tools.ingredients import (
    search_ingredients,
    get_ingredient_information,
    get_ingredient_substitutes,
    get_ingredient_substitutes_by_id,
    autocomplete_ingredient_search,
    parse_ingredients,
    compute_ingredient_amount,
    convert_amounts,
)
from generated_tools.nutrition import (
    get_recipe_nutrition_by_id,
    analyze_recipe_nutrition,
    get_nutrition_for_recipe_from_url,
    search_food_products,
    get_food_product_information,
    search_menu_items,
    get_menu_item_information,
    get_comparable_products,
    map_ingredients_to_grocery_products,
)
from generated_tools.meal_planning import (
    generate_meal_plan,
    get_meal_plan_week,
    get_meal_plan_day,
    add_meal_plan_item,
    delete_meal_plan_item,
    get_meal_plan_templates,
    get_meal_plan_template,
    delete_meal_plan_template,
    get_shopping_list,
    add_to_shopping_list,
    delete_shopping_list_item,
)
from generated_tools.wine import (
    get_wine_pairing,
    get_wine_description,
    get_wine_recommendation,
    get_dish_pairing_for_wine,
)
from generated_tools.food_trivia import (
    get_random_food_trivia,
    get_random_food_joke,
    detect_food_in_text,
    classify_cuisine,
    classify_grocery_product,
    search_all_food,
    get_conversation_suggests,
    talk_to_chatbot,
)

# ---------------------------------------------------------------------------
# Create MCP server
# ---------------------------------------------------------------------------
mcp = FastMCP(
    name="spoonacular",
    description=(
        "Comprehensive MCP server for the Spoonacular Food API. "
        "Covers recipe search, recipe details, ingredient lookup, "
        "nutrition analysis, meal planning, wine pairing, and more."
    ),
)

# ---------------------------------------------------------------------------
# Register — Recipes
# ---------------------------------------------------------------------------
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
mcp.tool()(analyze_recipe_instructions)
mcp.tool()(guess_nutrition_by_dish_name)
mcp.tool()(get_recipe_price_breakdown)

# ---------------------------------------------------------------------------
# Register — Ingredients
# ---------------------------------------------------------------------------
mcp.tool()(search_ingredients)
mcp.tool()(get_ingredient_information)
mcp.tool()(get_ingredient_substitutes)
mcp.tool()(get_ingredient_substitutes_by_id)
mcp.tool()(autocomplete_ingredient_search)
mcp.tool()(parse_ingredients)
mcp.tool()(compute_ingredient_amount)
mcp.tool()(convert_amounts)

# ---------------------------------------------------------------------------
# Register — Nutrition
# ---------------------------------------------------------------------------
mcp.tool()(get_recipe_nutrition_by_id)
mcp.tool()(analyze_recipe_nutrition)
mcp.tool()(get_nutrition_for_recipe_from_url)
mcp.tool()(search_food_products)
mcp.tool()(get_food_product_information)
mcp.tool()(search_menu_items)
mcp.tool()(get_menu_item_information)
mcp.tool()(get_comparable_products)
mcp.tool()(map_ingredients_to_grocery_products)

# ---------------------------------------------------------------------------
# Register — Meal Planning
# ---------------------------------------------------------------------------
mcp.tool()(generate_meal_plan)
mcp.tool()(get_meal_plan_week)
mcp.tool()(get_meal_plan_day)
mcp.tool()(add_meal_plan_item)
mcp.tool()(delete_meal_plan_item)
mcp.tool()(get_meal_plan_templates)
mcp.tool()(get_meal_plan_template)
mcp.tool()(delete_meal_plan_template)
mcp.tool()(get_shopping_list)
mcp.tool()(add_to_shopping_list)
mcp.tool()(delete_shopping_list_item)

# ---------------------------------------------------------------------------
# Register — Wine
# ---------------------------------------------------------------------------
mcp.tool()(get_wine_pairing)
mcp.tool()(get_wine_description)
mcp.tool()(get_wine_recommendation)
mcp.tool()(get_dish_pairing_for_wine)

# ---------------------------------------------------------------------------
# Register — Food Trivia / Misc
# ---------------------------------------------------------------------------
mcp.tool()(get_random_food_trivia)
mcp.tool()(get_random_food_joke)
mcp.tool()(detect_food_in_text)
mcp.tool()(classify_cuisine)
mcp.tool()(classify_grocery_product)
mcp.tool()(search_all_food)
mcp.tool()(get_conversation_suggests)
mcp.tool()(talk_to_chatbot)

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    mcp.run(transport="stdio")
