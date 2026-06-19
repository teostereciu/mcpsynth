from mcp.server.fastmcp import FastMCP

from generated_tools.ingredients import (
    autocomplete_ingredient_search,
    compute_ingredient_amount,
    convert_amounts,
    get_ingredient_information,
    get_ingredient_substitutes,
    get_ingredient_substitutes_by_id,
    ingredient_search,
    parse_ingredients,
)
from generated_tools.meal_planning import (
    generate_meal_plan,
    generate_shopping_list,
    get_meal_plan_day,
    get_meal_plan_week,
    get_shopping_list,
    search_custom_foods,
)
from generated_tools.menu_items import (
    autocomplete_menu_item_search,
    get_menu_item_information,
    search_menu_items,
)
from generated_tools.misc import (
    conversation_suggests,
    detect_food_in_text,
    quick_answer,
    random_food_joke,
    random_food_trivia,
    search_all_food,
    search_food_videos,
    search_site_content,
    talk_to_chatbot,
)
from generated_tools.products import (
    autocomplete_product_search,
    get_product_information,
    search_grocery_products,
    search_grocery_products_by_upc,
)
from generated_tools.recipes import (
    analyze_recipe_search_query,
    autocomplete_recipe_search,
    extract_recipe_from_website,
    get_analyzed_recipe_instructions,
    get_random_recipes,
    get_recipe_equipment,
    get_recipe_information,
    get_recipe_ingredients,
    get_recipe_nutrition,
    get_recipe_price_breakdown,
    get_recipe_taste,
    get_similar_recipes,
    search_recipes,
    search_recipes_by_ingredients,
    search_recipes_by_nutrients,
    summarize_recipe,
)
from generated_tools.wine import (
    get_dish_pairing_for_wine,
    get_wine_description,
    get_wine_pairing,
    get_wine_recommendation,
)

mcp = FastMCP("spoonacular")

for fn in [
    search_recipes,
    search_recipes_by_nutrients,
    search_recipes_by_ingredients,
    get_recipe_information,
    get_similar_recipes,
    get_random_recipes,
    autocomplete_recipe_search,
    get_recipe_taste,
    get_recipe_equipment,
    get_recipe_price_breakdown,
    get_recipe_ingredients,
    get_recipe_nutrition,
    get_analyzed_recipe_instructions,
    extract_recipe_from_website,
    summarize_recipe,
    analyze_recipe_search_query,
    ingredient_search,
    get_ingredient_information,
    compute_ingredient_amount,
    convert_amounts,
    parse_ingredients,
    autocomplete_ingredient_search,
    get_ingredient_substitutes,
    get_ingredient_substitutes_by_id,
    get_meal_plan_week,
    get_meal_plan_day,
    generate_meal_plan,
    get_shopping_list,
    generate_shopping_list,
    search_custom_foods,
    search_menu_items,
    get_menu_item_information,
    autocomplete_menu_item_search,
    search_all_food,
    search_food_videos,
    quick_answer,
    detect_food_in_text,
    search_site_content,
    random_food_joke,
    random_food_trivia,
    talk_to_chatbot,
    conversation_suggests,
    search_grocery_products,
    search_grocery_products_by_upc,
    get_product_information,
    autocomplete_product_search,
    get_dish_pairing_for_wine,
    get_wine_pairing,
    get_wine_description,
    get_wine_recommendation,
]:
    mcp.tool()(fn)


if __name__ == "__main__":
    mcp.run()
