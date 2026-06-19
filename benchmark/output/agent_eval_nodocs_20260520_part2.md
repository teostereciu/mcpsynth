# Agent Evaluation Results

Generated: 2026-05-21 11:53
Agent model: `gcp-chat-completions-chat-gemini-2.5-pro-sandbox`

## Summary

| Dataset | Impl | Passed | Total | Pass% |
|---------|------|--------|-------|-------|
| ebay_commerce | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1448_nodocs | 11 | 14 | 79% |
| jira | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1448_nodocs | 14 | 16 | 88% |
| confluence | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1448_nodocs | 20 | 21 | 95% |
| spoonacular | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1448_nodocs | 0 | 17 | 0% |
| alphavantage | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1448_nodocs | 16 | 19 | 84% |
| shopify | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1448_nodocs | 0 | 18 | 0% |
| mastodon | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1448_nodocs | 13 | 15 | 87% |
| openweathermap | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1449_nodocs | 21 | 23 | 91% |

**Overall: 95/143 (66.4%)**

## Per-Dataset Task Breakdown

### ebay_commerce (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1448_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_default_category_tree | ✓ | 3 | 2 | 2 |
| get_category_tree | ✓ | 4 | 3 | 3 |
| get_category_subtree | ✓ | 3 | 2 | 2 |
| get_category_suggestions | ✓ | 3 | 2 | 2 |
| get_item_aspects_electronics | ✓ | 3 | 2 | 1 |
| search_charities | ✗ | 3 | 2 | 1 |
| translate_text | ✓ | 2 | 1 | 1 |
| get_category_suggestions_phones | ✓ | 5 | 4 | 4 |
| get_item_aspects_cameras | ✓ | 4 | 3 | 2 |
| translate_multiple | ✓ | 2 | 2 | 2 |
| get_expired_categories | ✗ | 3 | 2 | 2 |
| category_tree_then_aspects | ✗ | 7 | 6 | 6 |
| search_charity_then_get_details | ✓ | 4 | 3 | 2 |
| error_handling_invalid_category | ✓ | 2 | 1 | 1 |

### jira (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1448_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_current_user | ✓ | 2 | 1 | 0 |
| list_projects | ✓ | 2 | 1 | 0 |
| search_issues_jql | ✓ | 2 | 1 | 1 |
| get_issue_types | ✓ | 2 | 1 | 0 |
| get_issue_details | ✓ | 3 | 2 | 2 |
| list_issue_link_types | ✗ | 1 | 0 | 0 |
| get_project_statuses | ✓ | 3 | 2 | 0 |
| create_issue | ✓ | 9 | 8 | 5 |
| create_and_comment | ✓ | 4 | 3 | 0 |
| create_update_transition | ✓ | 8 | 7 | 1 |
| issue_with_watcher | ✓ | 15 | 15 | 1 |
| create_and_link_issues | ✗ | 8 | 7 | 1 |
| update_issue_priority | ✓ | 2 | 1 | 1 |
| create_and_log_work | ✓ | 7 | 6 | 2 |
| create_and_delete_comment | ✓ | 10 | 9 | 2 |
| error_handling_invalid_issue | ✓ | 2 | 1 | 1 |

### confluence (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1448_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_current_user | ✓ | 2 | 1 | 0 |
| list_spaces | ✓ | 2 | 1 | 0 |
| get_space_and_homepage | ✓ | 3 | 2 | 0 |
| list_pages_in_space | ✓ | 2 | 1 | 0 |
| search_content_cql | ✓ | 2 | 1 | 0 |
| create_page | ✓ | 4 | 3 | 1 |
| create_page_with_storage_format | ✓ | 4 | 3 | 1 |
| update_page | ✓ | 8 | 7 | 3 |
| create_and_get_page | ✓ | 5 | 4 | 1 |
| delete_page | ✓ | 5 | 4 | 0 |
| add_label_to_page | ✓ | 6 | 5 | 1 |
| create_footer_comment | ✓ | 5 | 4 | 1 |
| list_page_versions | ✓ | 14 | 13 | 6 |
| create_blog_post | ✓ | 3 | 2 | 1 |
| upload_attachment | ✓ | 5 | 4 | 1 |
| set_content_property | ✗ | 8 | 7 | 2 |
| full_page_lifecycle | ✓ | 8 | 7 | 1 |
| create_page_hierarchy | ✓ | 7 | 6 | 2 |
| get_nonexistent_page | ✓ | 2 | 1 | 1 |
| create_page_missing_space | ✓ | 3 | 2 | 1 |
| cql_create_and_search | ✓ | 5 | 4 | 0 |

### spoonacular (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1448_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| search_recipes_by_query | ✗ | 0 | 0 | 0 |
| search_recipes_by_ingredient | ✗ | 0 | 0 | 0 |
| search_vegetarian_recipes | ✗ | 0 | 0 | 0 |
| get_recipe_information | ✗ | 0 | 0 | 0 |
| get_recipe_ingredients | ✗ | 0 | 0 | 0 |
| get_recipe_instructions | ✗ | 0 | 0 | 0 |
| get_similar_recipes | ✗ | 0 | 0 | 0 |
| search_ingredients | ✗ | 0 | 0 | 0 |
| get_ingredient_information | ✗ | 0 | 0 | 0 |
| generate_meal_plan | ✗ | 0 | 0 | 0 |
| get_wine_pairing | ✗ | 0 | 0 | 0 |
| search_then_get_info | ✗ | 0 | 0 | 0 |
| recipe_info_then_instructions | ✗ | 0 | 0 | 0 |
| search_then_similar | ✗ | 0 | 0 | 0 |
| search_recipe_nutrition_chain | ✗ | 0 | 0 | 0 |
| nutrient_search_then_compare | ✗ | 0 | 0 | 0 |
| get_nonexistent_recipe | ✗ | 0 | 0 | 0 |

### alphavantage (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1448_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_stock_quote | ✓ | 2 | 1 | 0 |
| daily_time_series | ✗ | 2 | 1 | 0 |
| intraday_time_series | ✓ | 2 | 1 | 0 |
| weekly_time_series | ✓ | 2 | 1 | 0 |
| symbol_search | ✓ | 2 | 1 | 0 |
| forex_exchange_rate | ✓ | 2 | 1 | 0 |
| forex_daily_series | ✓ | 2 | 1 | 0 |
| crypto_exchange_rate | ✓ | 2 | 1 | 0 |
| rsi_indicator | ✓ | 2 | 1 | 0 |
| sma_indicator | ✓ | 2 | 1 | 0 |
| company_overview | ✓ | 2 | 1 | 0 |
| earnings_data | ✗ | 2 | 1 | 0 |
| cpi_data | ✓ | 2 | 1 | 0 |
| search_then_overview | ✓ | 4 | 3 | 0 |
| multi_quote_rank | ✓ | 3 | 5 | 0 |
| daily_vs_weekly_compare | ✓ | 2 | 2 | 0 |
| search_quote_rsi_chain | ✓ | 4 | 3 | 0 |
| overview_then_earnings | ✗ | 3 | 2 | 0 |
| invalid_symbol | ✓ | 2 | 1 | 0 |

### shopify (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1448_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_shop_info | ✗ | 2 | 1 | 0 |
| list_products | ✗ | 1 | 0 | 0 |
| create_and_list_draft_order | ✗ | 1 | 0 | 0 |
| create_and_verify_customer_list | ✗ | 2 | 1 | 0 |
| list_webhooks | ✗ | 2 | 1 | 0 |
| filter_products_by_status | ✗ | 1 | 0 | 0 |
| list_inventory_locations | ✗ | 1 | 0 | 0 |
| create_product | ✗ | 2 | 1 | 0 |
| create_webhook | ✗ | 1 | 0 | 0 |
| create_price_rule | ✗ | 2 | 1 | 0 |
| create_customer | ✗ | 1 | 0 | 0 |
| create_product_then_update | ✗ | 2 | 1 | 0 |
| price_rule_and_discount_code | ✗ | 1 | 0 | 0 |
| create_product_then_get_details | ✗ | 1 | 0 | 0 |
| draft_order_with_line_items | ✗ | 2 | 1 | 0 |
| create_product_with_variant | ✗ | 2 | 1 | 0 |
| inventory_level_workflow | ✗ | 3 | 2 | 0 |
| error_handling_invalid_resource | ✗ | 1 | 0 | 0 |

### mastodon (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1448_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_authenticated_account | ✓ | 2 | 1 | 0 |
| get_instance_info | ✓ | 2 | 1 | 0 |
| get_home_timeline | ✓ | 2 | 1 | 0 |
| search_statuses | ✓ | 2 | 1 | 0 |
| search_content | ✓ | 3 | 2 | 0 |
| get_notifications | ✓ | 2 | 1 | 0 |
| get_bookmarks | ✓ | 6 | 5 | 0 |
| post_status | ✓ | 2 | 1 | 0 |
| post_and_delete_status | ✓ | 3 | 2 | 0 |
| post_and_favourite | ✓ | 2 | 1 | 1 |
| post_with_spoiler | ✗ | 3 | 2 | 1 |
| create_and_delete_list | ✓ | 3 | 2 | 0 |
| bookmark_status | ✗ | 1 | 0 | 0 |
| get_nonexistent_status | ✓ | 2 | 1 | 1 |
| post_status_empty_content | ✓ | 2 | 1 | 1 |

### openweathermap (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1449_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| current_weather_london | ✓ | 2 | 1 | 0 |
| weather_feels_like | ✓ | 2 | 1 | 0 |
| wind_conditions | ✓ | 2 | 1 | 0 |
| cloud_and_visibility | ✓ | 2 | 1 | 0 |
| pressure_and_humidity | ✓ | 2 | 1 | 0 |
| sunrise_sunset | ✗ | 2 | 1 | 0 |
| forecast_timestamps | ✓ | 2 | 1 | 0 |
| forecast_precipitation | ✓ | 2 | 1 | 0 |
| forecast_temperature_range | ✗ | 2 | 1 | 0 |
| air_quality_paris | ✓ | 3 | 2 | 0 |
| air_quality_level | ✓ | 3 | 2 | 0 |
| geocode_city | ✓ | 2 | 1 | 0 |
| reverse_geocode | ✓ | 2 | 1 | 0 |
| geocode_then_weather | ✓ | 3 | 2 | 0 |
| humidity_comparison | ✓ | 2 | 2 | 0 |
| temperature_ranking | ✓ | 2 | 3 | 0 |
| weather_and_air_quality | ✓ | 4 | 3 | 0 |
| geocode_then_air_pollution_forecast | ✓ | 3 | 2 | 0 |
| zip_weather_vs_city_weather | ✓ | 2 | 2 | 0 |
| five_city_temperature_ranking | ✓ | 2 | 5 | 0 |
| forecast_hottest_slot | ✓ | 2 | 1 | 0 |
| air_quality_history_vs_forecast | ✓ | 3 | 3 | 0 |
| full_city_conditions | ✓ | 3 | 4 | 0 |
