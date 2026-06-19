# Agent Evaluation Results

Generated: 2026-05-21 15:03
Agent model: `gcp-chat-completions-chat-gemini-2.5-pro-sandbox`

## Summary

| Dataset | Impl | Passed | Total | Pass% |
|---------|------|--------|-------|-------|
| shopify | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1346 | 0 | 18 | 0% |
| spoonacular | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1348 | 0 | 17 | 0% |
| stripe | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1351 | 12 | 22 | 55% |
| zulip | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1356 | 17 | 25 | 68% |

**Overall: 29/82 (35.4%)**

## Per-Dataset Task Breakdown

### shopify (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1346`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_shop_info | ✗ | 0 | 0 | 0 |
| list_products | ✗ | 0 | 0 | 0 |
| create_and_list_draft_order | ✗ | 0 | 0 | 0 |
| create_and_verify_customer_list | ✗ | 0 | 0 | 0 |
| list_webhooks | ✗ | 0 | 0 | 0 |
| filter_products_by_status | ✗ | 0 | 0 | 0 |
| list_inventory_locations | ✗ | 0 | 0 | 0 |
| create_product | ✗ | 0 | 0 | 0 |
| create_webhook | ✗ | 0 | 0 | 0 |
| create_price_rule | ✗ | 0 | 0 | 0 |
| create_customer | ✗ | 0 | 0 | 0 |
| create_product_then_update | ✗ | 0 | 0 | 0 |
| price_rule_and_discount_code | ✗ | 0 | 0 | 0 |
| create_product_then_get_details | ✗ | 0 | 0 | 0 |
| draft_order_with_line_items | ✗ | 0 | 0 | 0 |
| create_product_with_variant | ✗ | 0 | 0 | 0 |
| inventory_level_workflow | ✗ | 0 | 0 | 0 |
| error_handling_invalid_resource | ✗ | 0 | 0 | 0 |

### spoonacular (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1348`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| search_recipes_by_query | ✗ | 2 | 1 | 1 |
| search_recipes_by_ingredient | ✗ | 2 | 1 | 1 |
| search_vegetarian_recipes | ✗ | 2 | 1 | 1 |
| get_recipe_information | ✗ | 2 | 1 | 1 |
| get_recipe_ingredients | ✗ | 1 | 0 | 0 |
| get_recipe_instructions | ✗ | 1 | 0 | 0 |
| get_similar_recipes | ✗ | 1 | 0 | 0 |
| search_ingredients | ✗ | 2 | 1 | 1 |
| get_ingredient_information | ✗ | 2 | 1 | 1 |
| generate_meal_plan | ✗ | 2 | 1 | 1 |
| get_wine_pairing | ✗ | 2 | 1 | 1 |
| search_then_get_info | ✗ | 2 | 1 | 1 |
| recipe_info_then_instructions | ✗ | 2 | 1 | 1 |
| search_then_similar | ✗ | 2 | 1 | 1 |
| search_recipe_nutrition_chain | ✗ | 2 | 1 | 1 |
| nutrient_search_then_compare | ✗ | 2 | 1 | 1 |
| get_nonexistent_recipe | ✗ | 1 | 0 | 0 |

### stripe (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1351`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| query_account_balance | ✓ | 2 | 1 | 0 |
| list_customers | ✓ | 2 | 1 | 0 |
| list_active_products | ✓ | 2 | 1 | 0 |
| retrieve_payment_intents | ✓ | 2 | 1 | 0 |
| create_customer | ✓ | 2 | 1 | 0 |
| create_product_and_price | ✓ | 3 | 2 | 0 |
| create_payment_intent | ✗ | 2 | 1 | 0 |
| create_checkout_session | ✗ | 2 | 1 | 0 |
| create_coupon | ✓ | 2 | 1 | 0 |
| create_payment_link | ✓ | 3 | 2 | 0 |
| customer_update_and_verify | ✓ | 4 | 3 | 0 |
| charge_and_refund | ✓ | 3 | 2 | 0 |
| subscription_workflow | ✗ | 4 | 3 | 1 |
| invoice_workflow | ✗ | 4 | 3 | 1 |
| save_payment_method | ✓ | 3 | 2 | 0 |
| coupon_and_promotion_code | ✗ | 4 | 3 | 0 |
| find_and_update_customer | ✓ | 3 | 2 | 0 |
| full_payment_flow | ✗ | 6 | 5 | 1 |
| subscription_then_cancel | ✗ | 9 | 8 | 2 |
| invoice_void_workflow | ✗ | 6 | 5 | 1 |
| balance_transactions_after_charge | ✗ | 3 | 2 | 0 |
| tax_rate_on_invoice | ✗ | 1 | 0 | 0 |

### zulip (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1356`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| list_streams | ✓ | 2 | 1 | 0 |
| get_profile | ✓ | 2 | 1 | 0 |
| list_users | ✓ | 2 | 1 | 0 |
| get_server_settings | ✗ | 1 | 0 | 0 |
| get_stream_subscribers | ✗ | 3 | 2 | 0 |
| get_topics_in_stream | ✓ | 3 | 2 | 0 |
| get_messages_and_count_topics | ✓ | 2 | 1 | 0 |
| send_stream_message | ✓ | 3 | 2 | 0 |
| send_direct_message | ✓ | 3 | 2 | 0 |
| edit_message | ✓ | 4 | 3 | 0 |
| add_scheduled_message | ✓ | 3 | 2 | 0 |
| add_alert_word | ✗ | 1 | 0 | 0 |
| update_stream_description | ✓ | 4 | 3 | 0 |
| send_and_react | ✓ | 3 | 2 | 0 |
| create_stream_and_post | ✓ | 3 | 2 | 0 |
| search_messages | ✗ | 6 | 5 | 1 |
| paginate_stream_messages | ✗ | 4 | 3 | 0 |
| send_to_nonexistent_stream | ✓ | 2 | 1 | 1 |
| delete_nonexistent_message | ✓ | 2 | 1 | 1 |
| invalid_emoji_reaction | ✓ | 3 | 2 | 1 |
| message_edit_history | ✓ | 6 | 5 | 0 |
| star_and_retrieve | ✗ | 3 | 2 | 1 |
| move_message_topic | ✓ | 6 | 5 | 1 |
| exhaust_pagination | ✗ | 3 | 2 | 0 |
| narrow_by_sender | ✗ | 5 | 4 | 1 |
