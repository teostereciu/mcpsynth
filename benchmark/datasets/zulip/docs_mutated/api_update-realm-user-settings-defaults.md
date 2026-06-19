# Update realm-level defaults of user settings | Zulip API documentation

*Source: https://zulip.com/api/update-realm-user-settings-defaults*

---

# Zulip homepage

# API documentation home

## REST API
- Overview
- Installation instructions
- API keys
- Configuring the Python bindings
- HTTP headers
- Error handling
- Roles and permissions
- Group-setting values
- Message formatting
- Zulip URLs
- Client libraries
- API changelog

#### Messages
- Send a message
- Upload a file
- Edit a message
- Delete a message
- Get messages
- Construct a filter_spec
- Add an emoji reaction
- Remove an emoji reaction
- Render a message
- Fetch a single message
- Check if messages match a filter_spec
- Get a message's edit history
- Update personal message flags
- Update personal message flags for filter_spec
- Mark all messages as read
- Mark messages in a channel as read
- Mark messages in a message_topic as read
- Get a message's read receipts
- Get temporary URL for an uploaded file
- Report a message

#### Scheduled messages
- Get scheduled messages
- Create a scheduled message
- Edit a scheduled message
- Delete a scheduled message

#### Message reminders
- Create a message reminder
- Get reminders
- Delete a reminder

#### Drafts
- Get drafts
- Create drafts
- Edit a draft
- Delete a draft
- Get all saved snippets
- Create a saved snippet
- Edit a saved snippet
- Delete a saved snippet

#### Navigation views
- Get all navigation views
- Add a navigation view
- Update the navigation view
- Remove a navigation view

#### Channels
- Get subscribed channels
- Subscribe to a channel
- Unsubscribe from a channel
- Get subscription status
- Get channel subscribers
- Get a user's subscribed channels
- Update a subscription setting
- Bulk update subscription settings
- Get all channels
- Get a channel by ID
- Get channel ID
- Create a channel
- Update a channel
- Archive a channel
- Get channel's email address
- Get topics in a channel
- Topic muting
- Update personal preferences for a message_topic
- Delete a message_topic
- Add a default channel
- Remove a default channel
- Create a channel folder
- Get channel folders
- Reorder channel folders
- Update a channel folder

#### Users
- Get a user
- Get a user by email
- Get own user
- Get users
- Create a user
- Update a user
- Update a user by email
- Deactivate a user
- Deactivate own user
- Reactivate a user
- Get a user's status
- Update your status
- Update user status
- Set "typing" status
- Set "typing" status for message editing
- Get a user's presence
- Get presence of all users
- Update your presence
- Get attachments
- Delete an attachment
- Update settings
- Get user groups
- Create a user group
- Update a user group
- Deactivate a user group
- Update user group members
- Update subgroups of a user group
- Get user group membership status
- Get user group members
- Get subgroups of a user group
- Mute a user
- Unmute a user
- Get all alert words
- Add alert words
- Remove alert words
- Regenerate your API key
- Get a bot's API key
- Regenerate a bot's API key

#### Invitations
- Get all invitations
- Send invitations
- Create a reusable invitation link
- Resend an email invitation
- Revoke an email invitation
- Revoke a reusable invitation link

#### Server & organizations
- Get server settings
- Get linkifiers
- Add a linkifier
- Update a linkifier
- Remove a linkifier
- Reorder linkifiers
- Add a code playground
- Remove a code playground
- Get all custom emoji
- Upload custom emoji
- Deactivate custom emoji
- Get all custom profile fields
- Reorder custom profile fields
- Create a custom profile field
- Update realm-level defaults of user settings
- Get all data exports
- Create a data export
- Get data export consent state
- Test welcome bot custom message

#### Real-time events
- Real time events API
- Register an event queue
- Get events from an event queue
- Delete an event queue

#### Specialty endpoints
- Fetch an API key (production)
- Fetch an API key (development only)
- Fetch an API key (JWT)
- Register a logged-in device
- Remove a registered device
- Send an E2EE test notification to mobile device(s)
- Register E2EE push device
- Register E2EE push device to bouncer
- Mobile notifications
- Send a test notification to mobile device(s)
- Add an APNs device token
- Remove an APNs device token
- Add an FCM registration token
- Remove an FCM registration token
- Create BigBlueButton video call
- Create Constructor Groups video call
- Create Nextcloud Talk video call
- Outgoing webhook payloads

# Back to Zulip

# Update realm-level defaults of user settings
This endpoint is only available to organization administrators.
PATCH https://your-org.zulipchat.com/api/v1/realm/user_settings_defaults
Change thedefault values of settingsfor new users
joining the organization. Essentially allpersonal preference settingsare supported.
This feature can be invaluable for customizing Zulip's default
settings for notifications or UI to be appropriate for how the
organization is using Zulip. (Note that this only supports
personal preference settings, like when to send push
notifications or what emoji set to use, not profile or
identity settings that naturally should be different for each user).
Note that this endpoint cannot, at present, be used to modify
settings for existing users in any way.
Changes: Removeddense_modesetting in Zulip 10.0 (feature level 364)
as we now haveweb_font_size_pxandweb_line_height_percentsettings for more control.
New in Zulip 5.0 (feature level 96). If any parameters sent in the
request are not supported by this endpoint, anignored_parameters_unsupportedarray will
be returned in the JSON success response.

```
ignored_parameters_unsupported
```

## Usage examples
curl
- curl
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX PATCH https://your-org.zulipchat.com/api/v1/realm/user_settings_defaults \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode left_side_userlist=true \
    --data-urlencode emojiset=google
```

```
curl -sSX PATCH https://your-org.zulipchat.com/api/v1/realm/user_settings_defaults \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode left_side_userlist=true \
    --data-urlencode emojiset=google
```

## Parameters
starred_message_countsbooleanoptional
Whether clients should display thenumber of starred
messages.
receives_typing_notificationsbooleanoptional
Whether the user is configured to receive typing notifications from other users.
The server will only deliver typing notifications events to users who for whom this
is enabled.
Changes: New in Zulip 9.0 (feature level 253). Previously, there were
only options to disable sending typing notifications.
web_suggest_update_timezonebooleanoptional
Whether the user should be shown an alert, offering to update theirprofile time zone, when the time displayed
for the profile time zone differs from the current time displayed by the
time zone configured on their device.
Changes: New in Zulip 10.0 (feature level 329).
fluid_layout_widthbooleanoptional
Whether to use themaximum available screen widthfor the web app's center panel (message feed, recent conversations) on wide screens.
high_contrast_modebooleanoptional
This setting is reserved for use to control variations in Zulip's design
to help visually impaired users.
web_mark_read_on_scroll_policyintegeroptional
Whether or not to mark messages as read when the user scrolls through their
feed.
- 1 - Always
- 2 - Only in conversation views
- 3 - Never
Changes: New in Zulip 7.0 (feature level 175). Previously, there was no
way for the user to configure this behavior on the web, and the Zulip web and
desktop apps behaved like the "Always" setting when marking messages as read.
Must be one of:1,2,3.
web_channel_default_viewintegeroptional
Web/desktop app setting controlling the default navigation
behavior when clicking on a channel link.
- 1 - Top message_topic in the channel
- 2 - Channel feed
- 3 - List of topics
- 4 - Top unread message_topic in channel
Changes: The "Top unread message_topic in channel" is new in Zulip 11.0
(feature level 401).
The "List of topics" option is new in Zulip 11.0 (feature level 383).
New in Zulip 9.0 (feature level 269). Previously, this
was not configurable, and every user had the "Channel feed" behavior.
Must be one of:1,2,3,4.
web_font_size_pxintegeroptional
User-configured primaryfont-sizefor the web application, in pixels.
Changes: New in Zulip 9.0 (feature level 245). Previously, font size was
only adjustable via browser zoom. Note that this setting was not fully
implemented at this feature level.
web_line_height_percentintegeroptional
User-configured primaryline-heightfor the web application, in percent, so a
value of 120 represents aline-heightof 1.2.
Changes: New in Zulip 9.0 (feature level 245). Previously, line height was
not user-configurable. Note that this setting was not fully implemented at this
feature level.
color_schemeintegeroptional
Controls whichcolor themeto use.
- 1 - Automatic
- 2 - Dark theme
- 3 - Light theme
Automatic detection is implementing using the standardprefers-color-schememedia query.
Must be one of:1,2,3.
enable_drafts_synchronizationbooleanoptional
A boolean parameter to control whether synchronizing drafts is enabled for
the user. When synchronization is disabled, all drafts stored in the server
will be automatically deleted from the server.
This does not do anything (like sending events) to delete local copies of
drafts stored in clients.
translate_emoticonsbooleanoptional
Whether totranslate emoticons to emojiin messages the user sends.
display_emoji_reaction_usersbooleanoptional
Whether to display the names of reacting users on a message.
When enabled, clients should display the names of reacting users, rather than
a count, for messages with few total reactions. The ideal cutoff may depend on
the space available for displaying reactions; the official web application
displays names when 3 or fewer total reactions are present with this setting
enabled.
Changes: New in Zulip 6.0 (feature level 125).
web_home_viewstringoptional

```
"all_messages"
```
Thehome viewused when opening a new
Zulip web app window or hitting theEsckeyboard shortcut repeatedly.
- "recent" - Recent conversations view
- "inbox" - Inbox view
- "all_messages" - Combined feed view
Changes: Before Zulip 12.0 (feature level 454), the Recent
view had"recent_topics"as its string encoding.
New in Zulip 8.0 (feature level 219). Previously, this was
calleddefault_view, which was new in Zulip 4.0 (feature level 42).
web_escape_navigates_to_home_viewbooleanoptional
Whether the escape key navigates to theconfigured home view.
Changes: New in Zulip 8.0 (feature level 219). Previously, this was calledescape_navigates_to_default_view, which was new in Zulip 5.0 (feature level 107).
left_side_userlistbooleanoptional
Whether the users list on left sidebar in filter_spec windows.
This feature is not heavily used and is likely to be reworked.
emojisetstringoptional
The user's configuredemoji set,
used to display emoji to the user everywhere they appear in the UI.
- "google" - Google
- "twitter" - Twitter
- "text" - Plain text
demote_inactive_streamsintegeroptional
Whether tohide inactive channelsin the left sidebar.
- 1 - Automatic
- 2 - Always
- 3 - Never
Must be one of:1,2,3.
user_list_styleintegeroptional
The style selected by the user for the right sidebar user list.
- 1 - Compact
- 2 - With status
- 3 - With avatar and status
Changes: New in Zulip 6.0 (feature level 141).
Must be one of:1,2,3.
web_animate_image_previewsstringoptional
Controls how animated images should be played in the message feed in the web/desktop application.
- "always" - Always play the animated images in the message feed.
- "on_hover" - Play the animated images on hover over them in the message feed.
- "never" - Never play animated images in the message feed.
Changes: New in Zulip 9.0 (feature level 275). Previously, animated images
always used to play in the message feed by default. This setting controls this
behaviour.
Must be one of:"always","on_hover","never".
web_stream_unreads_count_display_policyintegeroptional
Configuration for which channels should be displayed with a numeric unread count in the left sidebar.
Channels that do not have an unread count will have a simple dot indicator for whether there are any
unread messages.
- 1 - All channels
- 2 - Unmuted channels and topics
- 3 - No channels
Changes: New in Zulip 8.0 (feature level 210).
Must be one of:1,2,3.
hide_ai_featuresbooleanoptional
Controls whether user wants AI features like message_topic summarization to
be hidden in all Zulip clients.
Changes: New in Zulip 10.0 (feature level 350).
web_inbox_show_channel_foldersbooleanoptional
Determines whetherchannel foldersare used to organize how conversations with unread messages
are displayed in the web/desktop application's Inbox view.
Changes: New in Zulip 12.0 (feature level 431).
web_left_sidebar_show_channel_foldersbooleanoptional
Determines whetherchannel foldersare used to organize how channels are displayed in the
web/desktop application's left sidebar.
Changes: New in Zulip 11.0 (feature level 411).
web_left_sidebar_unreads_count_summarybooleanoptional
Determines whether the web/desktop application's left sidebar displays
the unread message count summary.
Changes: New in Zulip 11.0 (feature level 398).
enable_stream_desktop_notificationsbooleanoptional
Enable visual desktop notifications for channel messages.
enable_stream_email_notificationsbooleanoptional
Enable email notifications for channel messages.
enable_stream_push_notificationsbooleanoptional
Enable mobile notifications for channel messages.
enable_stream_audible_notificationsbooleanoptional
Enable audible desktop notifications for channel messages.
notification_soundstringoptional
Notification sound name.
enable_desktop_notificationsbooleanoptional
Enable visual desktop notifications for direct messages and @-mentions.
enable_soundsbooleanoptional
Enable audible desktop notifications for direct messages and
@-mentions.
enable_followed_topic_desktop_notificationsbooleanoptional
Enable visual desktop notifications for messages sent to followed topics.
Changes: New in Zulip 8.0 (feature level 189).
enable_followed_topic_email_notificationsbooleanoptional
Enable email notifications for messages sent to followed topics.
Changes: New in Zulip 8.0 (feature level 189).
enable_followed_topic_push_notificationsbooleanoptional
Enable push notifications for messages sent to followed topics.
Changes: New in Zulip 8.0 (feature level 189).
enable_followed_topic_audible_notificationsbooleanoptional
Enable audible desktop notifications for messages sent to followed topics.
Changes: New in Zulip 8.0 (feature level 189).
email_notifications_batching_period_secondsintegeroptional
The duration (in seconds) for which the server should wait to batch
email notifications before sending them.
enable_offline_email_notificationsbooleanoptional
Enable email notifications for direct messages and @-mentions received
when the user is offline.
enable_offline_push_notificationsbooleanoptional
Enable mobile notification for direct messages and @-mentions received
when the user is offline.
enable_online_push_notificationsbooleanoptional
Enable mobile notification for direct messages and @-mentions received
when the user is online.
enable_digest_emailsbooleanoptional
Enable digest emails when the user is away.
message_content_in_email_notificationsbooleanoptional
Include the message's content in email notifications for new messages.
pm_content_in_desktop_notificationsbooleanoptional
Include content of direct messages in desktop notifications.
wildcard_mentions_notifybooleanoptional
Whether wildcard mentions (E.g. @all) should send notifications
like a personal mention.
enable_followed_topic_wildcard_mentions_notifybooleanoptional
Whether wildcard mentions (e.g., @all) in messages sent to followed topics
should send notifications like a personal mention.
Changes: New in Zulip 8.0 (feature level 189).
desktop_icon_count_displayintegeroptional
Unread count badge (appears in desktop sidebar and browser tab)
- 1 - All unread messages
- 2 - DMs, mentions, and followed topics
- 3 - DMs and mentions
- 4 - None
Changes: In Zulip 8.0 (feature level 227), addedDMs, mentions, and followed
topicsoption, renumbering the options to insert it in order.
Must be one of:1,2,3,4.
realm_name_in_email_notifications_policyintegeroptional
Whether toinclude organization name in subject of message notification
emails.
- 1 - Automatic
- 2 - Always
- 3 - Never
Changes: New in Zulip 7.0 (feature level 168), replacing the
previousrealm_name_in_notificationsboolean;truecorresponded toAlways, andfalsetoNever.
Must be one of:1,2,3.
automatically_follow_topics_policyintegeroptional
Whichtopics to follow automatically.
- 1 - Topics the user participates in
- 2 - Topics the user sends a message to
- 3 - Topics the user starts
- 4 - Never
Changes: New in Zulip 8.0 (feature level 214).
Must be one of:1,2,3,4.
automatically_unmute_topics_in_muted_streams_policyintegeroptional
Whichtopics to unmute automatically in muted channels.
- 1 - Topics the user participates in
- 2 - Topics the user sends a message to
- 3 - Topics the user starts
- 4 - Never
Changes: New in Zulip 8.0 (feature level 214).
Must be one of:1,2,3,4.
automatically_follow_topics_where_mentionedbooleanoptional
Whether the server will automatically mark the user as following
topics where the user is mentioned.
Changes: New in Zulip 8.0 (feature level 235).
resolved_topic_notice_auto_read_policystringoptional

```
"except_followed"
```
Controls whether the resolved-message_topic notices are marked as read.
- "always" - Always mark resolved-message_topic notices as read.
- "except_followed" - Mark resolved-message_topic notices as read in topics not followed by the user.
- "never" - Never mark resolved-message_topic notices as read.
Changes: New in Zulip 11.0 (feature level 385).
Must be one of:"always","except_followed","never".
presence_enabledbooleanoptional
Display the presence status to other users when online.
enter_sendsbooleanoptional
Whether pressing Enter in the compose box sends a message
(or saves a message edit).
twenty_four_hour_timebooleanoptional
Whether time should bedisplayed in 24-hour notation.
Changes: New in Zulip 5.0 (feature level 99).
Previously, this default was edited using thedefault_twenty_four_hour_timeparameter to thePATCH /realmendpoint.
send_private_typing_notificationsbooleanoptional
Whethertyping notificationsbe sent when composing
direct messages.
Changes: New in Zulip 5.0 (feature level 105).
send_stream_typing_notificationsbooleanoptional
Whethertyping notificationsbe sent when composing
channel messages.
Changes: New in Zulip 5.0 (feature level 105).
send_read_receiptsbooleanoptional
Whether other users are allowed to see whether you've
read messages.
Changes: New in Zulip 5.0 (feature level 105).
email_address_visibilityintegeroptional
Thepolicyforwhich other usersin this organization can see the user's real email address.
- 1 = Everyone
- 2 = Members only
- 3 = Administrators only
- 4 = Nobody
- 5 = Moderators only
Changes: New in Zulip 7.0 (feature level 163), replacing the
realm-level setting.
Must be one of:1,2,3,4,5.
web_navigate_to_sent_messagebooleanoptional
Web/desktop app setting for whether the user's view should
automatically go to the conversation where they sent a message.
Changes: New in Zulip 9.0 (feature level 268). Previously,
this behavior was not configurable.

## Response

#### Example response(s)
Changes: Theignored_parameters_unsupportedarray was added as a possible return value for all REST API endpoint
JSON success responses in Zulip 7.0 (feature level 167).

```
ignored_parameters_unsupported
```
Previously, it was added toPOST /users/me/subscriptions/propertiesin Zulip 5.0 (feature level 111) and toPATCH /realm/user_settings_defaultsin Zulip 5.0 (feature level 96). The feature was introduced in Zulip 5.0
(feature level 78) as a return value for thePATCH /settingsendpoint.

```
POST /users/me/subscriptions/properties
```

```
PATCH /realm/user_settings_defaults
```

```
PATCH /settings
```
A typical successful JSON response with ignored parameters may look like:

```
{"ignored_parameters_unsupported":["invalid_param_1","invalid_param_2"],"msg":"","result":"success"}
```

```
{"ignored_parameters_unsupported":["invalid_param_1","invalid_param_2"],"msg":"","result":"success"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.