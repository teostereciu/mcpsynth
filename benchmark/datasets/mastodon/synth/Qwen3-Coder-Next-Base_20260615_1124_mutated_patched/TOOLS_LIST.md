# Mastodon MCP Tools List

## Status Tools (12 tools)

### Status Operations
1. **post_status** - Post a new status to Mastodon
   - Parameters: text, visibility, in_reply_to_id, media_ids
   
2. **get_status** - Get a single status by ID
   - Parameters: status_id
   
3. **get_statuses** - Get multiple statuses by IDs
   - Parameters: status_ids
   
4. **delete_status** - Delete a status
   - Parameters: status_id, delete_media
   
5. **get_status_context** - Get parent and child statuses in context (thread)
   - Parameters: status_id
   
6. **boost_status** - Boost (reblog) a status
   - Parameters: status_id
   
7. **unboost_status** - Unboost (unreblog) a status
   - Parameters: status_id
   
8. **favourite_status** - Favourite a status
   - Parameters: status_id
   
9. **unfavourite_status** - Unfavourite a status
   - Parameters: status_id
   
10. **bookmark_status** - Bookmark a status
    - Parameters: status_id
    
11. **unbookmark_status** - Unbookmark a status
    - Parameters: status_id
    
12. **list_favourites** - List favourited statuses
    - Parameters: limit, max_id
    
13. **list_bookmarks** - List bookmarked statuses
    - Parameters: limit, max_id

## Account Tools (11 tools)

### Account Management
14. **get_authenticated_account** - Get authenticated account information
    - Returns: CredentialAccount
    
15. **update_account_profile** - Update account profile and preferences
    - Parameters: display_name, note, locked, bot, discoverable, visibility, sensitive, lang, account_fields
    
16. **get_account_by_id** - Get account information by ID
    - Parameters: account_id
    
17. **get_account_statuses** - Get account's statuses
    - Parameters: account_id, pinned, limit, exclude_replies, max_id
    
18. **follow_account** - Follow an account
    - Parameters: account_id
    
19. **unfollow_account** - Unfollow an account
    - Parameters: account_id
    
20. **get_followers** - Get account's followers
    - Parameters: account_id, limit
    
21. **get_following** - Get accounts that this account is following
    - Parameters: account_id, limit
    
22. **block_account** - Block an account
    - Parameters: account_id
    
23. **unblock_account** - Unblock an account
    - Parameters: account_id
    
24. **mute_account** - Mute an account
    - Parameters: account_id, notifications
    
25. **unmute_account** - Unmute an account
    - Parameters: account_id

## Timeline Tools (4 tools)

### Timeline Browsing
26. **get_home_timeline** - Get home timeline statuses
    - Parameters: limit, max_id, since_id
    
27. **get_public_timeline** - Get public timeline statuses
    - Parameters: local, remote, only_media, limit, max_id, since_id
    
28. **get_hashtag_timeline** - Get public timeline for a specific hashtag
    - Parameters: hashtag, local, limit, max_id, since_id
    
29. **get_list_timeline** - Get statuses from a specific list
    - Parameters: list_id, limit, max_id, since_id

## Notification Tools (4 tools)

### Notification Handling
30. **list_notifications** - Get notifications for the current user
    - Parameters: limit, max_id, since_id, min_id, exclude_types
    
31. **get_notification** - Get a single notification by ID
    - Parameters: notification_id
    
32. **dismiss_notification** - Dismiss a single notification
    - Parameters: notification_id
    
33. **clear_all_notifications** - Dismiss all notifications for the current user
    - Returns: success confirmation

## Search Tools (3 tools)

### Content Discovery
34. **search_accounts** - Search for accounts
    - Parameters: query, limit, resolve, following, following_id
    
35. **search_statuses** - Search for statuses
    - Parameters: query, resolve, account_id, offset
    
36. **search_hashtags** - Search for hashtags
    - Parameters: query, resolve

## List Tools (8 tools)

### List Management
37. **create_list** - Create a new list
    - Parameters: title, exclusive
    
38. **get_list** - Get a single list by ID
    - Parameters: list_id
    
39. **update_list** - Update a list
    - Parameters: list_id, title, exclusive
    
40. **delete_list** - Delete a list
    - Parameters: list_id
    
41. **list_lists** - Get all lists for the current user
    - Returns: list of list dictionaries
    
42. **get_accounts_in_list** - Get accounts in a specific list
    - Parameters: list_id
    
43. **add_accounts_to_list** - Add accounts to a list
    - Parameters: list_id, account_ids
    
44. **remove_accounts_from_list** - Remove accounts from a list
    - Parameters: list_id, account_ids

## Media Tools (3 tools)

### Media Handling
45. **upload_media** - Upload a media attachment for use in statuses
    - Parameters: file_path, description, focus
    
46. **update_media** - Update a media attachment's metadata
    - Parameters: media_id, description, focus
    
47. **get_media** - Get information about a media attachment
    - Parameters: media_id

## Instance Tools (3 tools)

### Instance Information
48. **get_instance_info** - Get information about the Mastodon instance
    - Returns: instance details, version, title, description, etc.
    
49. **get_instance_peers** - Get a list of instances this instance knows about
    - Returns: list of domain strings
    
50. **get_instance_activity** - Get weekly activity for the instance
    - Returns: weekly activity statistics

## Advanced Tools (10 tools)

### Scheduled Statuses
51. **list_scheduled_statuses** - Get all scheduled statuses
    - Parameters: limit, max_id, since_id, min_id
    
52. **get_scheduled_status** - Get a single scheduled status
    - Parameters: status_id
    
53. **update_scheduled_status** - Update a scheduled status's publishing date
    - Parameters: status_id, scheduled_at
    
54. **cancel_scheduled_status** - Cancel a scheduled status
    - Parameters: status_id

### Push Notifications
55. **get_push_subscription** - Get the current user's push subscription
    - Returns: push subscription information
    
56. **update_push_subscription** - Update the current user's push subscription alerts
    - Parameters: alerts
    
57. **delete_push_subscription** - Unsubscribe from push notifications
    - Returns: success confirmation

### Polls
58. **get_poll** - Get a poll attached to a status
    - Parameters: poll_id
    
59. **vote_on_poll** - Vote on a poll
    - Parameters: poll_id, choices

### Reports
60. **create_report** - Create a report
    - Parameters: account_id, status_ids, comment, forward

---

**Total: 60 MCP Tools**

All tools are registered with the MCP server and discoverable via `list_tools()`.
