# Agent Evaluation Results

Generated: 2026-05-21 15:30
Agent model: `gcp-chat-completions-chat-gemini-2.5-pro-sandbox`

## Summary

| Dataset | Impl | Passed | Total | Pass% |
|---------|------|--------|-------|-------|
| alphavantage | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1210_nodocs | 0 | 19 | 0% |
| confluence | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1211_nodocs | 15 | 21 | 71% |
| ebay_buy | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1212_nodocs | 4 | 17 | 24% |
| ebay_commerce | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1214_nodocs | 0 | 14 | 0% |
| ebay_sell | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1215_nodocs | 0 | 16 | 0% |
| github | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1217_nodocs | 16 | 23 | 70% |
| jira | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1219_nodocs | 4 | 16 | 25% |
| mastodon | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1325_nodocs | 13 | 15 | 87% |
| notion | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1327_nodocs | 0 | 22 | 0% |
| openweathermap | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1328_nodocs | 20 | 23 | 87% |

**Overall: 72/186 (38.7%)**

## Per-Dataset Task Breakdown

### alphavantage (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1210_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_stock_quote | ✗ | 2 | 1 | 1 |
| daily_time_series | ✗ | 2 | 1 | 1 |
| intraday_time_series | ✗ | 3 | 2 | 2 |
| weekly_time_series | ✗ | 2 | 1 | 1 |
| symbol_search | ✗ | 2 | 1 | 1 |
| forex_exchange_rate | ✗ | 2 | 1 | 1 |
| forex_daily_series | ✗ | 2 | 1 | 1 |
| crypto_exchange_rate | ✗ | 2 | 1 | 1 |
| rsi_indicator | ✗ | 2 | 1 | 1 |
| sma_indicator | ✗ | 2 | 1 | 1 |
| company_overview | ✗ | 2 | 1 | 1 |
| earnings_data | ✗ | 2 | 1 | 1 |
| cpi_data | ✗ | 2 | 1 | 1 |
| search_then_overview | ✗ | 2 | 1 | 1 |
| multi_quote_rank | ✗ | 2 | 3 | 3 |
| daily_vs_weekly_compare | ✗ | 2 | 2 | 2 |
| search_quote_rsi_chain | ✗ | 2 | 1 | 1 |
| overview_then_earnings | ✗ | 2 | 2 | 2 |
| invalid_symbol | ✗ | 2 | 1 | 1 |

### confluence (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1211_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_current_user | ✓ | 2 | 1 | 0 |
| list_spaces | ✓ | 2 | 1 | 0 |
| get_space_and_homepage | ✓ | 3 | 2 | 0 |
| list_pages_in_space | ✓ | 2 | 1 | 0 |
| search_content_cql | ✓ | 2 | 1 | 0 |
| create_page | ✓ | 4 | 3 | 1 |
| create_page_with_storage_format | ✗ | 5 | 4 | 3 |
| update_page | ✗ | 7 | 6 | 3 |
| create_and_get_page | ✓ | 6 | 5 | 2 |
| delete_page | ✓ | 7 | 6 | 1 |
| add_label_to_page | ✗ | 5 | 4 | 3 |
| create_footer_comment | ✓ | 8 | 7 | 4 |
| list_page_versions | ✗ | 9 | 8 | 4 |
| create_blog_post | ✓ | 3 | 2 | 1 |
| upload_attachment | ✓ | 7 | 6 | 3 |
| set_content_property | ✓ | 9 | 8 | 4 |
| full_page_lifecycle | ✗ | 15 | 15 | 9 |
| create_page_hierarchy | ✗ | 8 | 7 | 6 |
| get_nonexistent_page | ✓ | 2 | 1 | 1 |
| create_page_missing_space | ✓ | 2 | 1 | 1 |
| cql_create_and_search | ✓ | 7 | 6 | 2 |

### ebay_buy (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1212_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| search_products | ✗ | 2 | 1 | 0 |
| search_with_filter | ✗ | 2 | 1 | 0 |
| search_cheapest | ✓ | 2 | 1 | 0 |
| browse_by_category | ✓ | 2 | 1 | 0 |
| get_item_by_legacy_id | ✗ | 2 | 1 | 0 |
| search_with_price_range | ✗ | 3 | 2 | 0 |
| search_then_get_item | ✗ | 2 | 1 | 0 |
| get_item_shipping | ✗ | 2 | 1 | 0 |
| batch_item_lookup | ✗ | 3 | 2 | 0 |
| get_item_group_variations | ✗ | 5 | 4 | 2 |
| compare_item_prices | ✗ | 2 | 1 | 0 |
| search_across_categories | ✗ | 2 | 2 | 0 |
| error_handling_invalid_item | ✓ | 2 | 1 | 1 |
| search_sort_and_paginate | ✗ | 4 | 3 | 0 |
| search_filter_and_enrich | ✗ | 5 | 4 | 1 |
| search_offset_deduplication | ✗ | 3 | 2 | 0 |
| cheapest_per_category | ✓ | 2 | 2 | 0 |

### ebay_commerce (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1214_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_default_category_tree | ✗ | 0 | 0 | 0 |
| get_category_tree | ✗ | 0 | 0 | 0 |
| get_category_subtree | ✗ | 0 | 0 | 0 |
| get_category_suggestions | ✗ | 0 | 0 | 0 |
| get_item_aspects_electronics | ✗ | 0 | 0 | 0 |
| search_charities | ✗ | 0 | 0 | 0 |
| translate_text | ✗ | 0 | 0 | 0 |
| get_category_suggestions_phones | ✗ | 0 | 0 | 0 |
| get_item_aspects_cameras | ✗ | 0 | 0 | 0 |
| translate_multiple | ✗ | 0 | 0 | 0 |
| get_expired_categories | ✗ | 0 | 0 | 0 |
| category_tree_then_aspects | ✗ | 0 | 0 | 0 |
| search_charity_then_get_details | ✗ | 0 | 0 | 0 |
| error_handling_invalid_category | ✗ | 0 | 0 | 0 |

### ebay_sell (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1215_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_category_metadata | ✗ | 1 | 0 | 0 |
| get_listing_recommendations | ✗ | 1 | 0 | 0 |
| get_item_aspects_shoes | ✗ | 1 | 0 | 0 |
| get_sales_analytics | ✗ | 1 | 0 | 0 |
| list_inventory_locations | ✗ | 2 | 1 | 0 |
| list_fulfillment_policies | ✗ | 2 | 1 | 0 |
| create_inventory_item | ✗ | 2 | 1 | 0 |
| create_fulfillment_policy | ✗ | 2 | 1 | 0 |
| create_return_policy | ✗ | 2 | 1 | 0 |
| create_payment_policy | ✗ | 2 | 1 | 0 |
| get_inventory_item | ✗ | 2 | 1 | 0 |
| delete_inventory_item | ✗ | 3 | 2 | 0 |
| inventory_item_group | ✗ | 4 | 5 | 0 |
| create_listing_workflow | ✗ | 3 | 2 | 0 |
| inventory_location_workflow | ✗ | 2 | 2 | 0 |
| error_handling_invalid_category | ✗ | 1 | 0 | 0 |

### github (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1217_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_authenticated_user | ✗ | 2 | 1 | 0 |
| get_repo_info | ✗ | 1 | 0 | 0 |
| list_repo_issues | ✓ | 3 | 2 | 0 |
| list_repo_branches | ✓ | 3 | 2 | 0 |
| list_pull_requests | ✓ | 3 | 2 | 0 |
| search_repositories | ✗ | 2 | 1 | 0 |
| list_releases | ✓ | 3 | 2 | 0 |
| list_workflow_runs | ✓ | 3 | 2 | 0 |
| commit_status_check | ✗ | 2 | 1 | 0 |
| create_issue | ✓ | 4 | 3 | 0 |
| create_and_label_issue | ✓ | 6 | 5 | 1 |
| create_gist | ✗ | 1 | 0 | 0 |
| label_management | ✓ | 4 | 3 | 1 |
| issue_comment_workflow | ✓ | 4 | 3 | 0 |
| repo_contents_read | ✓ | 3 | 2 | 0 |
| error_handling_invalid_repo | ✓ | 2 | 1 | 1 |
| paginate_issues | ✗ | 4 | 3 | 0 |
| paginate_commits | ✓ | 3 | 2 | 0 |
| create_issue_missing_title | ✓ | 3 | 2 | 1 |
| update_file_wrong_sha | ✓ | 4 | 3 | 1 |
| read_then_update_file | ✗ | 4 | 3 | 0 |
| issue_to_pr_search | ✓ | 3 | 3 | 0 |
| commit_sha_to_file_read | ✓ | 4 | 3 | 0 |

### jira (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1219_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_current_user | ✗ | 4 | 3 | 1 |
| list_projects | ✓ | 3 | 2 | 0 |
| search_issues_jql | ✗ | 2 | 1 | 1 |
| get_issue_types | ✗ | 2 | 1 | 0 |
| get_issue_details | ✗ | 4 | 3 | 3 |
| list_issue_link_types | ✗ | 1 | 0 | 0 |
| get_project_statuses | ✗ | 3 | 2 | 0 |
| create_issue | ✗ | 12 | 11 | 4 |
| create_and_comment | ✗ | 5 | 4 | 1 |
| create_update_transition | ✓ | 9 | 8 | 1 |
| issue_with_watcher | ✗ | 4 | 3 | 0 |
| create_and_link_issues | ✓ | 9 | 9 | 0 |
| update_issue_priority | ✗ | 4 | 3 | 2 |
| create_and_log_work | ✗ | 7 | 6 | 2 |
| create_and_delete_comment | ✗ | 5 | 4 | 1 |
| error_handling_invalid_issue | ✓ | 2 | 1 | 1 |

### mastodon (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1325_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_authenticated_account | ✓ | 2 | 1 | 0 |
| get_instance_info | ✗ | 2 | 1 | 0 |
| get_home_timeline | ✓ | 2 | 1 | 0 |
| search_statuses | ✓ | 2 | 1 | 0 |
| search_content | ✓ | 2 | 1 | 0 |
| get_notifications | ✓ | 2 | 1 | 0 |
| get_bookmarks | ✓ | 6 | 5 | 0 |
| post_status | ✓ | 2 | 1 | 0 |
| post_and_delete_status | ✗ | 3 | 2 | 1 |
| post_and_favourite | ✓ | 3 | 2 | 0 |
| post_with_spoiler | ✓ | 2 | 1 | 0 |
| create_and_delete_list | ✓ | 3 | 2 | 0 |
| bookmark_status | ✓ | 4 | 3 | 0 |
| get_nonexistent_status | ✓ | 2 | 1 | 1 |
| post_status_empty_content | ✓ | 2 | 1 | 1 |

### notion (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1327_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| list_workspace_users | ✗ | 0 | 0 | 0 |
| get_integration_identity | ✗ | 0 | 0 | 0 |
| search_all_content | ✗ | 0 | 0 | 0 |
| count_pages_vs_databases | ✗ | 0 | 0 | 0 |
| find_database_by_title | ✗ | 0 | 0 | 0 |
| create_titled_page | ✗ | 0 | 0 | 0 |
| create_database_with_select | ✗ | 0 | 0 | 0 |
| create_and_rename_page | ✗ | 0 | 0 | 0 |
| archive_and_confirm | ✗ | 0 | 0 | 0 |
| create_page_with_blocks | ✗ | 0 | 0 | 0 |
| add_comment_to_page | ✗ | 0 | 0 | 0 |
| populate_and_filter_database | ✗ | 0 | 0 | 0 |
| sorted_database_query | ✗ | 0 | 0 | 0 |
| database_number_filter | ✗ | 0 | 0 | 0 |
| mixed_block_types | ✗ | 0 | 0 | 0 |
| rich_text_formatting | ✗ | 0 | 0 | 0 |
| nested_page_creation | ✗ | 0 | 0 | 0 |
| paginate_block_children | ✗ | 0 | 0 | 0 |
| retrieve_nonexistent_page | ✗ | 0 | 0 | 0 |
| invalid_property_filter | ✗ | 0 | 0 | 0 |
| update_existing_block | ✗ | 0 | 0 | 0 |
| compound_filter_and_or | ✗ | 0 | 0 | 0 |

### openweathermap (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1328_nodocs`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| current_weather_london | ✓ | 2 | 1 | 0 |
| weather_feels_like | ✓ | 2 | 1 | 0 |
| wind_conditions | ✓ | 2 | 1 | 0 |
| cloud_and_visibility | ✓ | 2 | 1 | 0 |
| pressure_and_humidity | ✓ | 2 | 1 | 0 |
| sunrise_sunset | ✓ | 2 | 1 | 0 |
| forecast_timestamps | ✓ | 2 | 1 | 0 |
| forecast_precipitation | ✗ | 2 | 1 | 0 |
| forecast_temperature_range | ✓ | 2 | 1 | 0 |
| air_quality_paris | ✓ | 5 | 4 | 0 |
| air_quality_level | ✓ | 4 | 3 | 0 |
| geocode_city | ✓ | 3 | 2 | 0 |
| reverse_geocode | ✓ | 2 | 1 | 0 |
| geocode_then_weather | ✗ | 3 | 2 | 0 |
| humidity_comparison | ✓ | 2 | 2 | 0 |
| temperature_ranking | ✓ | 2 | 3 | 0 |
| weather_and_air_quality | ✓ | 3 | 3 | 0 |
| geocode_then_air_pollution_forecast | ✓ | 6 | 5 | 0 |
| zip_weather_vs_city_weather | ✓ | 2 | 2 | 0 |
| five_city_temperature_ranking | ✓ | 2 | 5 | 0 |
| forecast_hottest_slot | ✓ | 2 | 1 | 0 |
| air_quality_history_vs_forecast | ✓ | 5 | 5 | 0 |
| full_city_conditions | ✗ | 6 | 6 | 0 |
