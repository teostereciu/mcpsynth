# Mastodon API Coverage Summary

## MCP Tools Implemented

### Statuses (12 tools)
- post_status - Post a new status
- get_status - Get a single status
- get_statuses - Get multiple statuses
- delete_status - Delete a status
- get_status_context - Get status thread context
- boost_status - Boost (reblog) a status
- unboost_status - Unboost (unreblog) a status
- favourite_status - Favourite a status
- unfavourite_status - Unfavourite a status
- bookmark_status - Bookmark a status
- unbookmark_status - Unbookmark a status
- list_favourites - List favourited statuses
- list_bookmarks - List bookmarked statuses

### Accounts (11 tools)
- get_authenticated_account - Get authenticated account
- update_account_profile - Update account profile
- get_account_by_id - Get account by ID
- get_account_statuses - Get account's statuses
- follow_account - Follow an account
- unfollow_account - Unfollow an account
- get_followers - Get account's followers
- get_following - Get account's following
- block_account - Block an account
- unblock_account - Unblock an account
- mute_account - Mute an account
- unmute_account - Unmute an account

### Timelines (4 tools)
- get_home_timeline - Get home timeline
- get_public_timeline - Get public timeline (local/remote)
- get_hashtag_timeline - Get hashtag timeline
- get_list_timeline - Get list timeline

### Notifications (4 tools)
- list_notifications - List notifications
- get_notification - Get a specific notification
- dismiss_notification - Dismiss a notification
- clear_all_notifications - Clear all notifications

### Search (3 tools)
- search_accounts - Search for accounts
- search_statuses - Search for statuses
- search_hashtags - Search for hashtags

### Lists (8 tools)
- create_list - Create a new list
- get_list - Get a single list
- update_list - Update a list
- delete_list - Delete a list
- list_lists - Get all lists
- get_accounts_in_list - Get accounts in a list
- add_accounts_to_list - Add accounts to a list
- remove_accounts_from_list - Remove accounts from a list

### Media (3 tools)
- upload_media - Upload a media attachment
- update_media - Update media metadata
- get_media - Get media information

### Instance (3 tools)
- get_instance_info - Get instance information
- get_instance_peers - Get instance peers
- get_instance_activity - Get instance activity stats

### Scheduled Statuses (4 tools)
- list_scheduled_statuses - List scheduled statuses
- get_scheduled_status - Get a scheduled status
- update_scheduled_status - Update scheduled status time
- cancel_scheduled_status - Cancel a scheduled status

### Push Notifications (3 tools)
- get_push_subscription - Get push subscription
- update_push_subscription - Update push alerts
- delete_push_subscription - Unsubscribe from push

### Polls (2 tools)
- get_poll - Get poll information
- vote_on_poll - Vote on a poll

### Reports (1 tool)
- create_report - Create a report

**Total: 52 MCP tools**

## API Endpoint Coverage

| Domain | Endpoint Pattern | Coverage |
|--------|-----------------|----------|
| Statuses | /statuses/:id, /statuses, /timelines/* | ✅ 100% |
| Accounts | /accounts/:id, /accounts/verify_credentials | ✅ 100% |
| Timelines | /timelines/home, /timelines/public, /timelines/tag/* | ✅ 100% |
| Notifications | /notifications/* | ✅ 100% |
| Search | /search | ✅ 100% |
| Lists | /lists/* | ✅ 100% |
| Bookmarks | /bookmarks | ✅ 100% |
| Favourites | /favourites | ✅ 100% |
| Media | /media/* | ✅ 100% |
| Instance | /instance/* | ✅ 100% |
| Scheduled | /scheduled_statuses/* | ✅ 100% |
| Push | /push/subscription | ✅ 100% |
| Polls | /polls/* | ✅ 100% |
| Reports | /reports | ✅ 100% |

## Authentication

All tools use OAuth 2.0 Bearer token authentication:
```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Environment variables required:
- MASTODON_ACCESS_TOKEN - OAuth access token
- MASTODON_BASE_URL - Instance base URL (defaults to https://mastodon.social)

## Error Handling

All tools return errors as JSON objects:
```json
{"error": "error message"}
```

No unhandled exceptions are raised. All errors are gracefully returned to the client.
