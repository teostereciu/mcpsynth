from mcp.server.fastmcp import FastMCP

from generated_tools.catalog import get_product, search_products
from generated_tools.charity import get_charity_org, search_charity_orgs
from generated_tools.identity import get_user
from generated_tools.media import (
    create_document,
    create_document_from_url,
    get_document,
    upload_document,
    create_image_from_file,
    create_image_from_url,
    get_image,
    create_video,
    get_video,
    upload_video,
)
from generated_tools.notification import (
    create_destination,
    get_destinations,
    get_destination,
    update_destination,
    delete_destination,
    get_config,
    update_config,
    get_public_key,
)
from generated_tools.taxonomy import (
    get_default_category_tree_id,
    get_category_tree,
    get_category_subtree,
    get_category_suggestions,
    fetch_item_aspects,
    get_item_aspects_for_category,
    get_compatibility_properties,
    get_compatibility_property_values,
)
from generated_tools.translation import translate


mcp = FastMCP("ebay-commerce")

for fn in [
    get_product,
    search_products,
    get_charity_org,
    search_charity_orgs,
    get_user,
    create_document,
    create_document_from_url,
    get_document,
    upload_document,
    create_image_from_file,
    create_image_from_url,
    get_image,
    create_video,
    get_video,
    upload_video,
    create_destination,
    get_destinations,
    get_destination,
    update_destination,
    delete_destination,
    get_config,
    update_config,
    get_public_key,
    get_default_category_tree_id,
    get_category_tree,
    get_category_subtree,
    get_category_suggestions,
    fetch_item_aspects,
    get_item_aspects_for_category,
    get_compatibility_properties,
    get_compatibility_property_values,
    translate,
]:
    mcp.tool()(fn)


if __name__ == "__main__":
    mcp.run()
