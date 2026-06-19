# Agent Evaluation Results

Generated: 2026-05-21 20:01
Agent model: `gcp-chat-completions-chat-gemini-2.5-pro-sandbox`

## Summary

| Dataset | Impl | Passed | Total | Pass% |
|---------|------|--------|-------|-------|
| alphavantage | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1210_mutated_patched | 0 | 19 | 0% |
| confluence | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1212_mutated_patched | 9 | 21 | 43% |
| ebay_buy | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1216_mutated_patched | 0 | 17 | 0% |
| ebay_commerce | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1326_mutated_patched | 6 | 14 | 43% |
| ebay_sell | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1328_mutated_patched | 5 | 16 | 31% |
| github | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1330_mutated_patched | 0 | 23 | 0% |
| jira | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1332_mutated_patched | 7 | 16 | 44% |
| mastodon | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1335_mutated_patched | 13 | 15 | 87% |
| notion | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1338_mutated_patched | 10 | 22 | 45% |
| openweathermap | azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1342_mutated_patched | 21 | 23 | 91% |

**Overall: 71/186 (38.2%)**

## Per-Dataset Task Breakdown

### alphavantage (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1210_mutated_patched`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_stock_quote | ✗ | 2 | 1 | 1 |
| daily_time_series | ✗ | 2 | 1 | 1 |
| intraday_time_series | ✗ | 3 | 2 | 2 |
| weekly_time_series | ✗ | 2 | 1 | 1 |
| symbol_search | ✗ | 2 | 1 | 1 |
| forex_exchange_rate | ✗ | 2 | 1 | 1 |
| forex_daily_series | ✗ | 2 | 1 | 1 |
| crypto_exchange_rate | ✗ | 3 | 2 | 2 |
| rsi_indicator | ✗ | 2 | 1 | 1 |
| sma_indicator | ✗ | 2 | 1 | 1 |
| company_overview | ✗ | 2 | 1 | 1 |
| earnings_data | ✗ | 2 | 1 | 1 |
| cpi_data | ✗ | 2 | 1 | 1 |
| search_then_overview | ✗ | 2 | 1 | 1 |
| multi_quote_rank | ✗ | 3 | 4 | 4 |
| daily_vs_weekly_compare | ✗ | 2 | 2 | 2 |
| search_quote_rsi_chain | ✗ | 2 | 1 | 1 |
| overview_then_earnings | ✗ | 2 | 2 | 2 |
| invalid_symbol | ✗ | 2 | 1 | 1 |

### confluence (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1212_mutated_patched`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_current_user | ✓ | 2 | 1 | 0 |
| list_spaces | ✓ | 2 | 1 | 0 |
| get_space_and_homepage | ✓ | 3 | 2 | 0 |
| list_pages_in_space | ✓ | 3 | 2 | 0 |
| search_content_cql | ✗ | 2 | 1 | 0 |
| create_page | ✗ | 3 | 2 | 1 |
| create_page_with_storage_format | ✗ | 3 | 2 | 1 |
| update_page | ✗ | 6 | 5 | 2 |
| create_and_get_page | ✓ | 5 | 4 | 1 |
| delete_page | ✗ | 5 | 4 | 2 |
| add_label_to_page | ✗ | 6 | 5 | 4 |
| create_footer_comment | ✓ | 6 | 5 | 2 |
| list_page_versions | ✗ | 5 | 4 | 3 |
| create_blog_post | ✗ | 4 | 3 | 1 |
| upload_attachment | ✗ | 5 | 4 | 3 |
| set_content_property | ✗ | 2 | 1 | 1 |
| full_page_lifecycle | ✓ | 6 | 7 | 2 |
| create_page_hierarchy | ✓ | 7 | 6 | 2 |
| get_nonexistent_page | ✓ | 2 | 1 | 1 |
| create_page_missing_space | ✗ | 2 | 1 | 0 |
| cql_create_and_search | ✗ | 7 | 6 | 4 |

### ebay_buy (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1216_mutated_patched`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| search_products | ✗ | 0 | 0 | 0 |
| search_with_filter | ✗ | 0 | 0 | 0 |
| search_cheapest | ✗ | 0 | 0 | 0 |
| browse_by_category | ✗ | 0 | 0 | 0 |
| get_item_by_legacy_id | ✗ | 0 | 0 | 0 |
| search_with_price_range | ✗ | 0 | 0 | 0 |
| search_then_get_item | ✗ | 0 | 0 | 0 |
| get_item_shipping | ✗ | 0 | 0 | 0 |
| batch_item_lookup | ✗ | 0 | 0 | 0 |
| get_item_group_variations | ✗ | 0 | 0 | 0 |
| compare_item_prices | ✗ | 0 | 0 | 0 |
| search_across_categories | ✗ | 0 | 0 | 0 |
| error_handling_invalid_item | ✗ | 0 | 0 | 0 |
| search_sort_and_paginate | ✗ | 0 | 0 | 0 |
| search_filter_and_enrich | ✗ | 0 | 0 | 0 |
| search_offset_deduplication | ✗ | 0 | 0 | 0 |
| cheapest_per_category | ✗ | 0 | 0 | 0 |

### ebay_commerce (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1326_mutated_patched`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_default_category_tree | ✓ | 2 | 1 | 0 |
| get_category_tree | ✗ | 3 | 2 | 0 |
| get_category_subtree | ✗ | 5 | 4 | 2 |
| get_category_suggestions | ✓ | 3 | 2 | 0 |
| get_item_aspects_electronics | ✗ | 4 | 3 | 1 |
| search_charities | ✓ | 2 | 1 | 0 |
| translate_text | ✗ | 3 | 2 | 2 |
| get_category_suggestions_phones | ✓ | 3 | 2 | 0 |
| get_item_aspects_cameras | ✗ | 6 | 5 | 3 |
| translate_multiple | ✗ | 5 | 8 | 8 |
| get_expired_categories | ✓ | 3 | 2 | 0 |
| category_tree_then_aspects | ✗ | 4 | 3 | 1 |
| search_charity_then_get_details | ✓ | 3 | 2 | 0 |
| error_handling_invalid_category | ✗ | 3 | 2 | 1 |

### ebay_sell (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1328_mutated_patched`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_category_metadata | ✗ | 1 | 0 | 0 |
| get_listing_recommendations | ✗ | 2 | 1 | 0 |
| get_item_aspects_shoes | ✗ | 1 | 0 | 0 |
| get_sales_analytics | ✗ | 2 | 1 | 1 |
| list_inventory_locations | ✗ | 1 | 0 | 0 |
| list_fulfillment_policies | ✓ | 2 | 1 | 0 |
| create_inventory_item | ✓ | 2 | 1 | 0 |
| create_fulfillment_policy | ✗ | 2 | 1 | 0 |
| create_return_policy | ✗ | 1 | 0 | 0 |
| create_payment_policy | ✓ | 2 | 1 | 1 |
| get_inventory_item | ✓ | 3 | 2 | 0 |
| delete_inventory_item | ✗ | 4 | 3 | 0 |
| inventory_item_group | ✗ | 3 | 2 | 0 |
| create_listing_workflow | ✓ | 4 | 3 | 0 |
| inventory_location_workflow | ✗ | 1 | 0 | 0 |
| error_handling_invalid_category | ✗ | 1 | 0 | 0 |

### github (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1330_mutated_patched`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_authenticated_user | ✗ | 1 | 0 | 0 |
| get_repo_info | ✗ | 2 | 1 | 1 |
| list_repo_issues | ✗ | 3 | 2 | 2 |
| list_repo_branches | ✗ | 3 | 2 | 1 |
| list_pull_requests | ✗ | 2 | 1 | 1 |
| search_repositories | ✗ | 2 | 1 | 0 |
| list_releases | ✗ | 1 | 0 | 0 |
| list_workflow_runs | ✗ | 1 | 0 | 0 |
| commit_status_check | ✗ | 2 | 1 | 1 |
| create_issue | ✗ | 1 | 0 | 0 |
| create_and_label_issue | ✗ | 1 | 0 | 0 |
| create_gist | ✗ | 1 | 0 | 0 |
| label_management | ✗ | 1 | 0 | 0 |
| issue_comment_workflow | ✗ | 1 | 0 | 0 |
| repo_contents_read | ✗ | 3 | 2 | 0 |
| error_handling_invalid_repo | ✗ | 3 | 2 | 2 |
| paginate_issues | ✗ | 3 | 2 | 2 |
| paginate_commits | ✗ | 5 | 4 | 3 |
| create_issue_missing_title | ✗ | 1 | 0 | 0 |
| update_file_wrong_sha | ✗ | 1 | 0 | 0 |
| read_then_update_file | ✗ | 3 | 2 | 1 |
| issue_to_pr_search | ✗ | 2 | 1 | 1 |
| commit_sha_to_file_read | ✗ | 2 | 1 | 1 |

### jira (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1332_mutated_patched`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_current_user | ✗ | 3 | 2 | 1 |
| list_projects | ✓ | 2 | 1 | 0 |
| search_issues_jql | ✗ | 2 | 1 | 1 |
| get_issue_types | ✗ | 1 | 0 | 0 |
| get_issue_details | ✗ | 3 | 2 | 2 |
| list_issue_link_types | ✗ | 2 | 1 | 0 |
| get_project_statuses | ✗ | 4 | 3 | 1 |
| create_issue | ✗ | 5 | 4 | 1 |
| create_and_comment | ✓ | 4 | 3 | 0 |
| create_update_transition | ✓ | 6 | 5 | 0 |
| issue_with_watcher | ✓ | 5 | 4 | 0 |
| create_and_link_issues | ✓ | 6 | 5 | 0 |
| update_issue_priority | ✗ | 4 | 3 | 2 |
| create_and_log_work | ✓ | 5 | 4 | 0 |
| create_and_delete_comment | ✓ | 6 | 5 | 0 |
| error_handling_invalid_issue | ✗ | 1 | 0 | 0 |

### mastodon (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1335_mutated_patched`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| get_authenticated_account | ✓ | 2 | 1 | 0 |
| get_instance_info | ✗ | 2 | 1 | 0 |
| get_home_timeline | ✓ | 2 | 1 | 0 |
| search_statuses | ✓ | 2 | 1 | 0 |
| search_content | ✓ | 2 | 2 | 0 |
| get_notifications | ✓ | 3 | 2 | 0 |
| get_bookmarks | ✓ | 6 | 5 | 0 |
| post_status | ✓ | 2 | 1 | 0 |
| post_and_delete_status | ✓ | 3 | 2 | 0 |
| post_and_favourite | ✓ | 3 | 2 | 0 |
| post_with_spoiler | ✗ | 3 | 2 | 0 |
| create_and_delete_list | ✓ | 3 | 2 | 0 |
| bookmark_status | ✓ | 4 | 3 | 0 |
| get_nonexistent_status | ✓ | 2 | 1 | 0 |
| post_status_empty_content | ✓ | 2 | 1 | 0 |

### notion (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1338_mutated_patched`)

| Task | Pass | Turns | Tool Calls | Errors |
|------|------|-------|------------|--------|
| list_workspace_users | ✓ | 2 | 1 | 0 |
| get_integration_identity | ✓ | 2 | 1 | 0 |
| search_all_content | ✗ | 3 | 3 | 1 |
| count_pages_vs_databases | ✗ | 5 | 6 | 3 |
| find_database_by_title | ✗ | 5 | 4 | 1 |
| create_titled_page | ✗ | 1 | 0 | 0 |
| create_database_with_select | ✗ | 4 | 3 | 1 |
| create_and_rename_page | ✓ | 4 | 3 | 0 |
| archive_and_confirm | ✓ | 4 | 3 | 0 |
| create_page_with_blocks | ✓ | 4 | 3 | 0 |
| add_comment_to_page | ✓ | 4 | 3 | 0 |
| populate_and_filter_database | ✗ | 7 | 6 | 2 |
| sorted_database_query | ✗ | 4 | 3 | 1 |
| database_number_filter | ✗ | 9 | 15 | 10 |
| mixed_block_types | ✓ | 4 | 3 | 0 |
| rich_text_formatting | ✓ | 4 | 3 | 0 |
| nested_page_creation | ✗ | 2 | 1 | 0 |
| paginate_block_children | ✗ | 6 | 5 | 1 |
| retrieve_nonexistent_page | ✓ | 2 | 1 | 1 |
| invalid_property_filter | ✗ | 3 | 2 | 0 |
| update_existing_block | ✓ | 6 | 5 | 0 |
| compound_filter_and_or | ✗ | 5 | 4 | 1 |

### openweathermap (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260521_1342_mutated_patched`)

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
| full_city_conditions | ✗ | 1 | 0 | 0 |
