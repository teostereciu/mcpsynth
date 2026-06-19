# Agent Evaluation Results

Generated: 2026-05-21 12:17
Agent model: `gcp-chat-completions-chat-gemini-2.5-pro-sandbox`

## Summary

| Dataset | Impl | Passed | Total | Pass% |
|---------|------|--------|-------|-------|
| jira | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1447 | 12 | 16 | 75% |
| confluence | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1442 | 19 | 21 | 90% |
| spoonacular | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1447 | 10 | 17 | 59% |
| alphavantage | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1447 | 0 | 19 | 0% |
| shopify | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1442 | 0 | 18 | 0% |
| mastodon | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1451_docs | 14 | 15 | 93% |
| openweathermap | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1447 | 0 | 23 | 0% |

**Overall: 55/129 (42.6%)**

## Per-Dataset Task Breakdown

### jira (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1447`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_current_user | ✗ | 2 | 1 | 1 |
| list_projects | ✓ | 2 | 1 | 0 |
| search_issues_jql | ✓ | 3 | 2 | 2 |
| get_issue_types | ✗ | 2 | 1 | 0 |
| get_issue_details | ✓ | 5 | 4 | 4 |
| list_issue_link_types | ✗ | 1 | 0 | 0 |
| get_project_statuses | ✓ | 3 | 2 | 0 |
| create_issue | ✗ | 9 | 8 | 2 |
| create_and_comment | ✓ | 7 | 6 | 2 |
| create_update_transition | ✓ | 10 | 9 | 1 |
| issue_with_watcher | ✓ | 6 | 5 | 0 |
| create_and_link_issues | ✓ | 6 | 5 | 1 |
| update_issue_priority | ✓ | 4 | 3 | 3 |
| create_and_log_work | ✓ | 6 | 5 | 0 |
| create_and_delete_comment | ✓ | 6 | 5 | 1 |
| error_handling_invalid_issue | ✓ | 2 | 1 | 1 |

### confluence (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1442`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_current_user | ✓ | 2 | 1 | 0 |
| list_spaces | ✓ | 2 | 1 | 0 |
| get_space_and_homepage | ✓ | 3 | 2 | 0 |
| list_pages_in_space | ✓ | 3 | 2 | 0 |
| search_content_cql | ✓ | 2 | 1 | 0 |
| create_page | ✓ | 3 | 2 | 0 |
| create_page_with_storage_format | ✓ | 3 | 2 | 0 |
| update_page | ✓ | 4 | 3 | 0 |
| create_and_get_page | ✓ | 6 | 5 | 1 |
| delete_page | ✓ | 5 | 4 | 0 |
| add_label_to_page | ✓ | 5 | 4 | 0 |
| create_footer_comment | ✓ | 4 | 3 | 0 |
| list_page_versions | ✓ | 5 | 4 | 0 |
| create_blog_post | ✓ | 3 | 2 | 0 |
| upload_attachment | ✗ | 3 | 2 | 0 |
| set_content_property | ✓ | 9 | 8 | 3 |
| full_page_lifecycle | ✓ | 7 | 6 | 0 |
| create_page_hierarchy | ✗ | 5 | 4 | 1 |
| get_nonexistent_page | ✓ | 2 | 1 | 1 |
| create_page_missing_space | ✓ | 2 | 1 | 1 |
| cql_create_and_search | ✓ | 5 | 4 | 0 |

### spoonacular (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1447`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| search_recipes_by_query | ✓ | 4 | 3 | 0 |
| search_recipes_by_ingredient | ✓ | 13 | 12 | 0 |
| search_vegetarian_recipes | ✓ | 2 | 1 | 0 |
| get_recipe_information | ✗ | 6 | 5 | 0 |
| get_recipe_ingredients | ✗ | 1 | 0 | 0 |
| get_recipe_instructions | ✗ | 4 | 3 | 0 |
| get_similar_recipes | ✗ | 1 | 0 | 0 |
| search_ingredients | ✓ | 2 | 1 | 0 |
| get_ingredient_information | ✓ | 2 | 1 | 0 |
| generate_meal_plan | ✓ | 2 | 1 | 0 |
| get_wine_pairing | ✓ | 2 | 1 | 0 |
| search_then_get_info | ✓ | 10 | 9 | 0 |
| recipe_info_then_instructions | ✗ | 5 | 4 | 0 |
| search_then_similar | ✓ | 4 | 3 | 1 |
| search_recipe_nutrition_chain | ✓ | 7 | 6 | 5 |
| nutrient_search_then_compare | ✗ | 2 | 1 | 1 |
| get_nonexistent_recipe | ✗ | 1 | 0 | 0 |

### alphavantage (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1447`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_stock_quote | ✗ | 7 | 6 | 0 |
| daily_time_series | ✗ | 11 | 10 | 0 |
| intraday_time_series | ✗ | 6 | 5 | 0 |
| weekly_time_series | ✗ | 6 | 5 | 0 |
| symbol_search | ✗ | 8 | 7 | 0 |
| forex_exchange_rate | ✗ | 10 | 9 | 0 |
| forex_daily_series | ✗ | 6 | 5 | 0 |
| crypto_exchange_rate | ✗ | 7 | 6 | 0 |
| rsi_indicator | ✗ | 5 | 4 | 0 |
| sma_indicator | ✗ | 7 | 6 | 0 |
| company_overview | ✗ | 2 | 1 | 0 |
| earnings_data | ✗ | 3 | 2 | 0 |
| cpi_data | ✗ | 6 | 5 | 0 |
| search_then_overview | ✗ | 13 | 12 | 0 |
| multi_quote_rank | ✗ | 4 | 5 | 0 |
| daily_vs_weekly_compare | ✗ | 6 | 10 | 0 |
| search_quote_rsi_chain | ✗ | 9 | 8 | 0 |
| overview_then_earnings | ✗ | 10 | 17 | 0 |
| invalid_symbol | ✗ | 2 | 1 | 0 |

### shopify (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1442`)

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

### mastodon (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1451_docs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_authenticated_account | ✓ | 2 | 1 | 0 |
| get_instance_info | ✓ | 2 | 1 | 0 |
| get_home_timeline | ✓ | 2 | 1 | 0 |
| search_statuses | ✓ | 2 | 1 | 0 |
| search_content | ✓ | 2 | 1 | 0 |
| get_notifications | ✓ | 3 | 2 | 0 |
| get_bookmarks | ✗ | 3 | 2 | 1 |
| post_status | ✓ | 2 | 1 | 0 |
| post_and_delete_status | ✓ | 2 | 1 | 1 |
| post_and_favourite | ✓ | 3 | 2 | 0 |
| post_with_spoiler | ✓ | 2 | 1 | 0 |
| create_and_delete_list | ✓ | 2 | 1 | 1 |
| bookmark_status | ✓ | 2 | 1 | 1 |
| get_nonexistent_status | ✓ | 2 | 1 | 1 |
| post_status_empty_content | ✓ | 2 | 1 | 1 |

### openweathermap (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1447`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| current_weather_london | ✗ | 0 | 0 | 0 |
| weather_feels_like | ✗ | 0 | 0 | 0 |
| wind_conditions | ✗ | 0 | 0 | 0 |
| cloud_and_visibility | ✗ | 0 | 0 | 0 |
| pressure_and_humidity | ✗ | 0 | 0 | 0 |
| sunrise_sunset | ✗ | 0 | 0 | 0 |
| forecast_timestamps | ✗ | 0 | 0 | 0 |
| forecast_precipitation | ✗ | 0 | 0 | 0 |
| forecast_temperature_range | ✗ | 0 | 0 | 0 |
| air_quality_paris | ✗ | 0 | 0 | 0 |
| air_quality_level | ✗ | 0 | 0 | 0 |
| geocode_city | ✗ | 0 | 0 | 0 |
| reverse_geocode | ✗ | 0 | 0 | 0 |
| geocode_then_weather | ✗ | 0 | 0 | 0 |
| humidity_comparison | ✗ | 0 | 0 | 0 |
| temperature_ranking | ✗ | 0 | 0 | 0 |
| weather_and_air_quality | ✗ | 0 | 0 | 0 |
| geocode_then_air_pollution_forecast | ✗ | 0 | 0 | 0 |
| zip_weather_vs_city_weather | ✗ | 0 | 0 | 0 |
| five_city_temperature_ranking | ✗ | 0 | 0 | 0 |
| forecast_hottest_slot | ✗ | 0 | 0 | 0 |
| air_quality_history_vs_forecast | ✗ | 0 | 0 | 0 |
| full_city_conditions | ✗ | 0 | 0 | 0 |
