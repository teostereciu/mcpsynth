# Agent Evaluation Results

Generated: 2026-05-21 12:02
Agent model: `gcp-chat-completions-chat-gemini-2.5-pro-sandbox`

## Summary

| Dataset | Impl | Passed | Total | Pass% |
|---------|------|--------|-------|-------|
| jira | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1447_mutated_patched | 12 | 16 | 75% |
| confluence | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1442_mutated_patched | 20 | 21 | 95% |
| spoonacular | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1447_mutated_patched | 4 | 17 | 24% |
| alphavantage | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1442_mutated_patched | 18 | 19 | 95% |
| shopify | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1442_mutated_patched | 17 | 18 | 94% |
| mastodon | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1443_mutated_patched | 13 | 15 | 87% |
| openweathermap | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1425_mutated_patched | 23 | 23 | 100% |

**Overall: 107/129 (82.9%)**

## Per-Dataset Task Breakdown

### jira (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1447_mutated_patched`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_current_user | ✓ | 2 | 1 | 0 |
| list_projects | ✓ | 2 | 1 | 0 |
| search_issues_jql | ✗ | 2 | 1 | 1 |
| get_issue_types | ✓ | 2 | 1 | 0 |
| get_issue_details | ✓ | 3 | 2 | 2 |
| list_issue_link_types | ✓ | 2 | 1 | 0 |
| get_project_statuses | ✓ | 3 | 2 | 0 |
| create_issue | ✗ | 6 | 5 | 3 |
| create_and_comment | ✓ | 9 | 8 | 2 |
| create_update_transition | ✓ | 7 | 6 | 1 |
| issue_with_watcher | ✓ | 6 | 5 | 0 |
| create_and_link_issues | ✗ | 7 | 7 | 2 |
| update_issue_priority | ✓ | 3 | 2 | 1 |
| create_and_log_work | ✓ | 11 | 10 | 1 |
| create_and_delete_comment | ✗ | 6 | 5 | 2 |
| error_handling_invalid_issue | ✓ | 2 | 1 | 1 |

### confluence (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1442_mutated_patched`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_current_user | ✓ | 2 | 1 | 0 |
| list_spaces | ✓ | 2 | 1 | 0 |
| get_space_and_homepage | ✓ | 3 | 2 | 0 |
| list_pages_in_space | ✓ | 3 | 2 | 0 |
| search_content_cql | ✓ | 2 | 1 | 0 |
| create_page | ✓ | 3 | 2 | 1 |
| create_page_with_storage_format | ✓ | 4 | 3 | 1 |
| update_page | ✓ | 7 | 6 | 5 |
| create_and_get_page | ✓ | 5 | 4 | 1 |
| delete_page | ✓ | 5 | 4 | 0 |
| add_label_to_page | ✓ | 5 | 4 | 1 |
| create_footer_comment | ✓ | 5 | 4 | 1 |
| list_page_versions | ✓ | 6 | 5 | 1 |
| create_blog_post | ✓ | 4 | 3 | 1 |
| upload_attachment | ✗ | 3 | 2 | 1 |
| set_content_property | ✓ | 6 | 5 | 2 |
| full_page_lifecycle | ✓ | 3 | 2 | 1 |
| create_page_hierarchy | ✓ | 3 | 2 | 1 |
| get_nonexistent_page | ✓ | 2 | 1 | 1 |
| create_page_missing_space | ✓ | 2 | 1 | 0 |
| cql_create_and_search | ✓ | 5 | 4 | 0 |

### spoonacular (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1447_mutated_patched`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| search_recipes_by_query | ✓ | 2 | 1 | 0 |
| search_recipes_by_ingredient | ✗ | 2 | 1 | 0 |
| search_vegetarian_recipes | ✓ | 2 | 1 | 0 |
| get_recipe_information | ✗ | 2 | 1 | 0 |
| get_recipe_ingredients | ✗ | 2 | 1 | 0 |
| get_recipe_instructions | ✗ | 3 | 2 | 0 |
| get_similar_recipes | ✗ | 2 | 1 | 0 |
| search_ingredients | ✗ | 4 | 3 | 0 |
| get_ingredient_information | ✗ | 9 | 8 | 0 |
| generate_meal_plan | ✗ | 10 | 9 | 0 |
| get_wine_pairing | ✗ | 4 | 3 | 0 |
| search_then_get_info | ✓ | 5 | 4 | 0 |
| recipe_info_then_instructions | ✗ | 4 | 3 | 0 |
| search_then_similar | ✗ | 3 | 2 | 1 |
| search_recipe_nutrition_chain | ✓ | 2 | 1 | 1 |
| nutrient_search_then_compare | ✗ | 2 | 1 | 1 |
| get_nonexistent_recipe | ✗ | 1 | 0 | 0 |

### alphavantage (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1442_mutated_patched`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_stock_quote | ✓ | 2 | 1 | 0 |
| daily_time_series | ✓ | 2 | 1 | 1 |
| intraday_time_series | ✓ | 2 | 1 | 1 |
| weekly_time_series | ✓ | 2 | 1 | 1 |
| symbol_search | ✓ | 2 | 1 | 1 |
| forex_exchange_rate | ✓ | 2 | 1 | 1 |
| forex_daily_series | ✓ | 2 | 1 | 1 |
| crypto_exchange_rate | ✓ | 3 | 2 | 2 |
| rsi_indicator | ✓ | 2 | 1 | 1 |
| sma_indicator | ✓ | 2 | 1 | 1 |
| company_overview | ✓ | 2 | 1 | 1 |
| earnings_data | ✓ | 2 | 1 | 1 |
| cpi_data | ✓ | 2 | 1 | 1 |
| search_then_overview | ✓ | 2 | 1 | 1 |
| multi_quote_rank | ✓ | 2 | 3 | 3 |
| daily_vs_weekly_compare | ✓ | 2 | 2 | 2 |
| search_quote_rsi_chain | ✓ | 2 | 1 | 1 |
| overview_then_earnings | ✗ | 3 | 3 | 3 |
| invalid_symbol | ✓ | 2 | 1 | 1 |

### shopify (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1442_mutated_patched`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_shop_info | ✓ | 2 | 1 | 0 |
| list_products | ✓ | 2 | 1 | 0 |
| create_and_list_draft_order | ✓ | 3 | 2 | 0 |
| create_and_verify_customer_list | ✓ | 2 | 2 | 0 |
| list_webhooks | ✓ | 3 | 2 | 0 |
| filter_products_by_status | ✓ | 3 | 4 | 0 |
| list_inventory_locations | ✓ | 2 | 1 | 0 |
| create_product | ✓ | 2 | 1 | 0 |
| create_webhook | ✓ | 2 | 1 | 0 |
| create_price_rule | ✗ | 1 | 0 | 0 |
| create_customer | ✓ | 2 | 1 | 0 |
| create_product_then_update | ✓ | 4 | 3 | 0 |
| price_rule_and_discount_code | ✓ | 3 | 2 | 0 |
| create_product_then_get_details | ✓ | 3 | 2 | 0 |
| draft_order_with_line_items | ✓ | 3 | 2 | 0 |
| create_product_with_variant | ✓ | 4 | 3 | 0 |
| inventory_level_workflow | ✓ | 8 | 7 | 1 |
| error_handling_invalid_resource | ✓ | 2 | 1 | 1 |

### mastodon (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1443_mutated_patched`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_authenticated_account | ✓ | 2 | 1 | 0 |
| get_instance_info | ✓ | 2 | 1 | 0 |
| get_home_timeline | ✓ | 2 | 1 | 0 |
| search_statuses | ✓ | 2 | 1 | 0 |
| search_content | ✓ | 2 | 1 | 0 |
| get_notifications | ✓ | 3 | 2 | 0 |
| get_bookmarks | ✓ | 5 | 4 | 1 |
| post_status | ✗ | 3 | 2 | 1 |
| post_and_delete_status | ✓ | 3 | 2 | 0 |
| post_and_favourite | ✓ | 3 | 2 | 0 |
| post_with_spoiler | ✓ | 2 | 1 | 0 |
| create_and_delete_list | ✓ | 3 | 2 | 0 |
| bookmark_status | ✗ | 4 | 3 | 1 |
| get_nonexistent_status | ✓ | 2 | 1 | 1 |
| post_status_empty_content | ✓ | 2 | 1 | 1 |

### openweathermap (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260520_1425_mutated_patched`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| current_weather_london | ✓ | 2 | 1 | 0 |
| weather_feels_like | ✓ | 2 | 1 | 0 |
| wind_conditions | ✓ | 3 | 2 | 0 |
| cloud_and_visibility | ✓ | 2 | 1 | 0 |
| pressure_and_humidity | ✓ | 2 | 1 | 0 |
| sunrise_sunset | ✓ | 2 | 1 | 0 |
| forecast_timestamps | ✓ | 3 | 2 | 0 |
| forecast_precipitation | ✓ | 3 | 2 | 0 |
| forecast_temperature_range | ✓ | 3 | 2 | 0 |
| air_quality_paris | ✓ | 3 | 2 | 0 |
| air_quality_level | ✓ | 3 | 2 | 0 |
| geocode_city | ✓ | 2 | 1 | 0 |
| reverse_geocode | ✓ | 2 | 1 | 0 |
| geocode_then_weather | ✓ | 3 | 2 | 0 |
| humidity_comparison | ✓ | 2 | 2 | 0 |
| temperature_ranking | ✓ | 2 | 3 | 0 |
| weather_and_air_quality | ✓ | 3 | 2 | 0 |
| geocode_then_air_pollution_forecast | ✓ | 3 | 2 | 0 |
| zip_weather_vs_city_weather | ✓ | 3 | 3 | 0 |
| five_city_temperature_ranking | ✓ | 2 | 5 | 0 |
| forecast_hottest_slot | ✓ | 3 | 2 | 0 |
| air_quality_history_vs_forecast | ✓ | 3 | 3 | 0 |
| full_city_conditions | ✓ | 3 | 4 | 0 |
