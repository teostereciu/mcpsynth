"""
Spoonacular Food API — MCP Server
Runs over stdio using FastMCP.
"""
from mcp.server.fastmcp import FastMCP

# ── domain modules ──────────────────────────────────────────────────────────
from generated_tools.recipes import (
    search_recipes,
    search_recipes_by_nutrients,
    search_recipes_by_ingredients,
    get_recipe_information,
    get_recipe_information_bulk,
    get_similar_recipes,
    get_random_recipes,
    autocomplete_recipe_search,
    get_recipe_taste_by_id,
    get_recipe_equipment_by_id,
    get_recipe_price_breakdown_by_id,
    get_recipe_ingredients_by_id,
    get_recipe_nutrition_by_id,
    get_analyzed_recipe_instructions,
    extract_recipe_from_website,
    analyze_recipe,
    summarize_recipe,
    analyze_recipe_instructions,
    classify_cuisine,
    analyze_recipe_search_query,
)
from generated_tools.ingredients import (
    search_ingredients,
    get_ingredient_information,
    compute_ingredient_amount,
    convert_amounts,
    parse_ingredients,
    compute_glycemic_load,
    autocomplete_ingredient_search,
    get_ingredient_substitutes,
    get_ingredient_substitutes_by_id,
)
from generated_tools.wine import (
    get_dish_pairing_for_wine,
    get_wine_pairing,
    get_wine_description,
    get_wine_recommendation,
)
from generated_tools.meal_planning import (
    get_meal_plan_week,
    get_meal_plan_day,
    generate_meal_plan,
    add_to_meal_plan,
    clear_meal_plan_day,
    delete_from_meal_plan,
    get_meal_plan_templates,
    get_meal_plan_template,
    add_meal_plan_template,
    delete_meal_plan_template,
    get_shopping_list,
    add_to_shopping_list,
    delete_from_shopping_list,
    generate_shopping_list,
    compute_shopping_list,
    connect_user,
)
from generated_tools.menu_items import (
    search_menu_items,
    get_menu_item_information,
    autocomplete_menu_item_search,
)
from generated_tools.products import (
    search_grocery_products,
    search_grocery_products_by_upc,
    get_product_information,
    get_comparable_products,
    autocomplete_product_search,
    classify_grocery_product,
    classify_grocery_product_bulk,
    map_ingredients_to_grocery_products,
)
from generated_tools.misc import (
    search_all_food,
    search_food_videos,
    quick_answer,
    detect_food_in_text,
    search_site_content,
    get_random_food_joke,
    get_random_food_trivia,
    talk_to_chatbot,
    conversation_suggests,
)

# ── MCP server ───────────────────────────────────────────────────────────────
mcp = FastMCP("spoonacular")

# ── Recipes ──────────────────────────────────────────────────────────────────
mcp.tool()(search_recipes)
mcp.tool()(search_recipes_by_nutrients)
mcp.tool()(search_recipes_by_ingredients)
mcp.tool()(get_recipe_information)
mcp.tool()(get_recipe_information_bulk)
mcp.tool()(get_similar_recipes)
mcp.tool()(get_random_recipes)
mcp.tool()(autocomplete_recipe_search)
mcp.tool()(get_recipe_taste_by_id)
mcp.tool()(get_recipe_equipment_by_id)
mcp.tool()(get_recipe_price_breakdown_by_id)
mcp.tool()(get_recipe_ingredients_by_id)
mcp.tool()(get_recipe_nutrition_by_id)
mcp.tool()(get_analyzed_recipe_instructions)
mcp.tool()(extract_recipe_from_website)
mcp.tool()(analyze_recipe)
mcp.tool()(summarize_recipe)
mcp.tool()(analyze_recipe_instructions)
mcp.tool()(classify_cuisine)
mcp.tool()(analyze_recipe_search_query)

# ── Ingredients ───────────────────────────────────────────────────────────────
mcp.tool()(search_ingredients)
mcp.tool()(get_ingredient_information)
mcp.tool()(compute_ingredient_amount)
mcp.tool()(convert_amounts)
mcp.tool()(parse_ingredients)
mcp.tool()(compute_glycemic_load)
mcp.tool()(autocomplete_ingredient_search)
mcp.tool()(get_ingredient_substitutes)
mcp.tool()(get_ingredient_substitutes_by_id)

# ── Wine ──────────────────────────────────────────────────────────────────────
mcp.tool()(get_dish_pairing_for_wine)
mcp.tool()(get_wine_pairing)
mcp.tool()(get_wine_description)
mcp.tool()(get_wine_recommendation)

# ── Meal Planning ─────────────────────────────────────────────────────────────
mcp.tool()(get_meal_plan_week)
mcp.tool()(get_meal_plan_day)
mcp.tool()(generate_meal_plan)
mcp.tool()(add_to_meal_plan)
mcp.tool()(clear_meal_plan_day)
mcp.tool()(delete_from_meal_plan)
mcp.tool()(get_meal_plan_templates)
mcp.tool()(get_meal_plan_template)
mcp.tool()(add_meal_plan_template)
mcp.tool()(delete_meal_plan_template)
mcp.tool()(get_shopping_list)
mcp.tool()(add_to_shopping_list)
mcp.tool()(delete_from_shopping_list)
mcp.tool()(generate_shopping_list)
mcp.tool()(compute_shopping_list)
mcp.tool()(connect_user)

# ── Menu Items ────────────────────────────────────────────────────────────────
mcp.tool()(search_menu_items)
mcp.tool()(get_menu_item_information)
mcp.tool()(autocomplete_menu_item_search)

# ── Grocery Products ──────────────────────────────────────────────────────────
mcp.tool()(search_grocery_products)
mcp.tool()(search_grocery_products_by_upc)
mcp.tool()(get_product_information)
mcp.tool()(get_comparable_products)
mcp.tool()(autocomplete_product_search)
mcp.tool()(classify_grocery_product)
mcp.tool()(classify_grocery_product_bulk)
mcp.tool()(map_ingredients_to_grocery_products)

# ── Misc ──────────────────────────────────────────────────────────────────────
mcp.tool()(search_all_food)
mcp.tool()(search_food_videos)
mcp.tool()(quick_answer)
mcp.tool()(detect_food_in_text)
mcp.tool()(search_site_content)
mcp.tool()(get_random_food_joke)
mcp.tool()(get_random_food_trivia)
mcp.tool()(talk_to_chatbot)
mcp.tool()(conversation_suggests)

# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    mcp.run(transport="stdio")
