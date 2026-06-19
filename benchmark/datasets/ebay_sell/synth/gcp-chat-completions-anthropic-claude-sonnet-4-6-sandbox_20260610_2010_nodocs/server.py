"""
eBay Sell API — MCP Server
Runs over stdio using FastMCP.

Environment variables required:
  EBAY_APP_ID       — OAuth client ID
  EBAY_CERT_ID      — OAuth client secret
  EBAY_REFRESH_TOKEN — User refresh token
  EBAY_ENVIRONMENT  — SANDBOX (default) or PRODUCTION
"""

from mcp.server.fastmcp import FastMCP

# ── Create the top-level MCP server ─────────────────────────────────────────
mcp = FastMCP("ebay-sell")

# ── Import all domain modules and register their tools ───────────────────────
# Each module defines its own local FastMCP instance and decorates functions
# with @mcp.tool(). We re-register those tools on the top-level server by
# importing the functions and adding them directly.

# Inventory
from generated_tools.inventory import (
    get_inventory_item,
    get_inventory_items,
    create_or_replace_inventory_item,
    delete_inventory_item,
    bulk_create_or_replace_inventory_item,
    bulk_get_inventory_item,
    bulk_update_price_quantity,
    get_inventory_item_group,
    create_or_replace_inventory_item_group,
    delete_inventory_item_group,
    get_offers,
    get_offer,
    create_offer,
    update_offer,
    delete_offer,
    publish_offer,
    publish_offer_by_inventory_item_group,
    withdraw_offer,
    bulk_create_offer,
    bulk_publish_offer,
    get_listing_fees,
    get_inventory_location,
    get_inventory_locations,
    create_inventory_location,
    update_inventory_location,
    delete_inventory_location,
    enable_inventory_location,
    disable_inventory_location,
)

# Fulfillment
from generated_tools.fulfillment import (
    get_orders,
    get_order,
    issue_order_refund,
    get_shipping_fulfillments,
    get_shipping_fulfillment,
    create_shipping_fulfillment,
    get_payment_disputes,
    get_payment_dispute,
    accept_payment_dispute,
    contest_payment_dispute,
    add_evidence_to_payment_dispute,
    get_payment_dispute_activities,
    get_payment_dispute_evidence,
)

# Account
from generated_tools.account import (
    get_fulfillment_policies,
    get_fulfillment_policy,
    get_fulfillment_policy_by_name,
    create_fulfillment_policy,
    update_fulfillment_policy,
    delete_fulfillment_policy,
    get_payment_policies,
    get_payment_policy,
    get_payment_policy_by_name,
    create_payment_policy,
    update_payment_policy,
    delete_payment_policy,
    get_return_policies,
    get_return_policy,
    get_return_policy_by_name,
    create_return_policy,
    update_return_policy,
    delete_return_policy,
    get_sales_taxes,
    get_sales_tax,
    create_or_replace_sales_tax,
    delete_sales_tax,
    get_opted_in_programs,
    opt_in_to_program,
    opt_out_of_program,
    get_seller_privileges,
    get_subscriptions,
    get_rate_tables,
    get_kyc,
)

# Marketing
from generated_tools.marketing import (
    get_campaigns,
    get_campaign,
    get_campaign_by_name,
    create_campaign,
    update_campaign_identification,
    update_campaign_budget,
    pause_campaign,
    resume_campaign,
    end_campaign,
    delete_campaign,
    clone_campaign,
    get_ads,
    get_ad,
    create_ads_by_listing_id,
    create_ads_by_inventory_reference,
    delete_ads,
    update_bids,
    get_promotions,
    get_promotion,
    get_promotion_reports,
    get_promotion_summary_report,
    create_item_price_markdown_promotion,
    update_item_price_markdown_promotion,
    delete_promotion,
    pause_promotion,
    resume_promotion,
    create_item_promotion,
    update_item_promotion,
    get_report_tasks,
    create_report_task,
    get_report,
)

# Finances
from generated_tools.finances import (
    get_transactions,
    get_transaction_summary,
    get_payouts,
    get_payout,
    get_payout_summary,
    get_transactions_for_payout,
    get_seller_funds_summary,
    get_fees,
    get_transfer,
    get_buyer_payment_instruments,
)

# Feed
from generated_tools.feed import (
    get_feed_types,
    get_feed_type,
    get_tasks,
    get_task,
    create_task,
    delete_task,
    get_task_input_file,
    get_task_result_file,
    upload_task_input_file,
    get_schedules,
    get_schedule,
    create_schedule,
    update_schedule,
    delete_schedule,
    get_schedule_template,
    get_schedule_templates,
)

# Catalog / Taxonomy
from generated_tools.catalog import (
    get_default_category_tree_id,
    get_category_tree,
    get_category_subtree,
    get_category_suggestions,
    get_item_aspects_for_category,
    get_categories_by_aspects,
    get_compatibility_properties,
    get_compatibility_property_values,
    search_catalog_products,
    get_catalog_product,
)

# Analytics / Compliance
from generated_tools.analytics import (
    get_seller_standards_profiles,
    get_seller_standards_profile,
    get_traffic_report,
    get_customer_service_metric,
    find_listing_violations,
    get_listing_violation_summary,
    suppress_listing_violation,
)

# Recommendation
from generated_tools.recommendation import (
    find_listing_recommendations,
)

# Negotiation
from generated_tools.negotiation import (
    find_eligible_items,
    send_offers_to_interested_buyers,
    get_offers_to_buyers,
)

# Logistics
from generated_tools.logistics import (
    create_shipping_quote,
    get_shipping_quote,
    create_shipment,
    get_shipment,
    cancel_shipment,
    download_label_file,
)

# Stores
from generated_tools.stores import (
    get_store,
    update_store,
    get_store_categories,
    create_store_category,
    update_store_category,
)

# ── Register all tools on the top-level server ───────────────────────────────
_ALL_TOOLS = [
    # Inventory
    get_inventory_item, get_inventory_items, create_or_replace_inventory_item,
    delete_inventory_item, bulk_create_or_replace_inventory_item, bulk_get_inventory_item,
    bulk_update_price_quantity, get_inventory_item_group,
    create_or_replace_inventory_item_group, delete_inventory_item_group,
    get_offers, get_offer, create_offer, update_offer, delete_offer,
    publish_offer, publish_offer_by_inventory_item_group, withdraw_offer,
    bulk_create_offer, bulk_publish_offer, get_listing_fees,
    get_inventory_location, get_inventory_locations, create_inventory_location,
    update_inventory_location, delete_inventory_location,
    enable_inventory_location, disable_inventory_location,
    # Fulfillment
    get_orders, get_order, issue_order_refund,
    get_shipping_fulfillments, get_shipping_fulfillment, create_shipping_fulfillment,
    get_payment_disputes, get_payment_dispute, accept_payment_dispute,
    contest_payment_dispute, add_evidence_to_payment_dispute,
    get_payment_dispute_activities, get_payment_dispute_evidence,
    # Account
    get_fulfillment_policies, get_fulfillment_policy, get_fulfillment_policy_by_name,
    create_fulfillment_policy, update_fulfillment_policy, delete_fulfillment_policy,
    get_payment_policies, get_payment_policy, get_payment_policy_by_name,
    create_payment_policy, update_payment_policy, delete_payment_policy,
    get_return_policies, get_return_policy, get_return_policy_by_name,
    create_return_policy, update_return_policy, delete_return_policy,
    get_sales_taxes, get_sales_tax, create_or_replace_sales_tax, delete_sales_tax,
    get_opted_in_programs, opt_in_to_program, opt_out_of_program,
    get_seller_privileges, get_subscriptions, get_rate_tables, get_kyc,
    # Marketing
    get_campaigns, get_campaign, get_campaign_by_name, create_campaign,
    update_campaign_identification, update_campaign_budget,
    pause_campaign, resume_campaign, end_campaign, delete_campaign, clone_campaign,
    get_ads, get_ad, create_ads_by_listing_id, create_ads_by_inventory_reference,
    delete_ads, update_bids,
    get_promotions, get_promotion, get_promotion_reports, get_promotion_summary_report,
    create_item_price_markdown_promotion, update_item_price_markdown_promotion,
    delete_promotion, pause_promotion, resume_promotion,
    create_item_promotion, update_item_promotion,
    get_report_tasks, create_report_task, get_report,
    # Finances
    get_transactions, get_transaction_summary, get_payouts, get_payout,
    get_payout_summary, get_transactions_for_payout, get_seller_funds_summary,
    get_fees, get_transfer, get_buyer_payment_instruments,
    # Feed
    get_feed_types, get_feed_type, get_tasks, get_task, create_task, delete_task,
    get_task_input_file, get_task_result_file, upload_task_input_file,
    get_schedules, get_schedule, create_schedule, update_schedule, delete_schedule,
    get_schedule_template, get_schedule_templates,
    # Catalog / Taxonomy
    get_default_category_tree_id, get_category_tree, get_category_subtree,
    get_category_suggestions, get_item_aspects_for_category, get_categories_by_aspects,
    get_compatibility_properties, get_compatibility_property_values,
    search_catalog_products, get_catalog_product,
    # Analytics / Compliance
    get_seller_standards_profiles, get_seller_standards_profile,
    get_traffic_report, get_customer_service_metric,
    find_listing_violations, get_listing_violation_summary, suppress_listing_violation,
    # Recommendation
    find_listing_recommendations,
    # Negotiation
    find_eligible_items, send_offers_to_interested_buyers, get_offers_to_buyers,
    # Logistics
    create_shipping_quote, get_shipping_quote, create_shipment, get_shipment,
    cancel_shipment, download_label_file,
    # Stores
    get_store, update_store, get_store_categories,
    create_store_category, update_store_category,
]

for _tool_fn in _ALL_TOOLS:
    mcp.tool()(_tool_fn)


if __name__ == "__main__":
    mcp.run()
