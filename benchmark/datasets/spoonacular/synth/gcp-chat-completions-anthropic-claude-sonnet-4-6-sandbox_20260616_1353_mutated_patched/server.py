"""
Spoonacular Food API — MCP Server
Runs over stdio using FastMCP.

Required environment variable:
    SPOONACULAR_API_KEY  — your Spoonacular API key
"""

from mcp.server.fastmcp import FastMCP

from generated_tools.recipes import register_recipes
from generated_tools.ingredients import register_ingredients
from generated_tools.wine import register_wine
from generated_tools.meal_planning import register_meal_planning
from generated_tools.menu_items import register_menu_items
from generated_tools.products import register_products
from generated_tools.misc import register_misc

mcp = FastMCP(
    name="spoonacular",
    instructions=(
        "This server exposes the Spoonacular Food API. "
        "You can search recipes, get recipe details and nutrition, work with ingredients, "
        "pair wines with food, plan meals, manage shopping lists, search grocery products "
        "and restaurant menu items, and more. "
        "All tools require the SPOONACULAR_API_KEY environment variable to be set."
    ),
)

# Register all domain tool groups
register_recipes(mcp)
register_ingredients(mcp)
register_wine(mcp)
register_meal_planning(mcp)
register_menu_items(mcp)
register_products(mcp)
register_misc(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
