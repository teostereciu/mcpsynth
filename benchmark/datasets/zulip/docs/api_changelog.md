# API changelog | Zulip API documentation

*Source: https://zulip.com/api/changelog*

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
- Construct a narrow
- Add an emoji reaction
- Remove an emoji reaction
- Render a message
- Fetch a single message
- Check if messages match a narrow
- Get a message's edit history
- Update personal message flags
- Update personal message flags for narrow
- Mark all messages as read
- Mark messages in a channel as read
- Mark messages in a topic as read
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
- Update personal preferences for a topic
- Delete a topic
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

# API changelog
This page documents changes to the Zulip Server API over time. See
also theZulip release lifecyclefor background
on why this API changelog is important, and theZulip server
changelog.
The API feature levels system used in this changelog is designed to
make it possible to write API clients, such as the Zulip mobile and
terminal apps, that work with a wide range of Zulip server
versions. Every change to the Zulip API is recorded briefly here and
with full details inChangesentries in the API documentation for
the modified endpoint(s).
When using an API endpoint whose behavior has changed, Zulip API
clients should check thezulip_feature_levelfield, present in theGET /server_settingsandPOST
/registerresponses, to determine the API
format used by the Zulip server that they are interacting with.

```
GET /server_settings
```

```
POST
/register
```

## Changes in Zulip 12.0
Feature level 478
- POST /realm/filters,PATCH /realm/filters/{filter_id}: Addedalternative_url_templatesparameter for specifying additional URL
  templates used only for reverse linkification (converting pasted URLs
  to linkifier pattern text). These templates have no effect on forward
  linkification.
- GET /realm/linkifiers,POST /register,GET /events: Linkifier objects now include thealternative_url_templatesfield.

```
POST /realm/filters
```

```
PATCH /realm/filters/{filter_id}
```

```
GET /realm/linkifiers
```

```
POST /register
```

```
GET /events
```
Feature level 477
- PATCH /realm,POST /register,GET /events: Addedworkplace_users_groupfield which is agroup-setting valuedescribing the set of users who will be considered as workplace
  users for billing.

```
POST /register
```

```
GET /events
```
Feature level 476
- POST /realm/profile_fields,GET /realm/profile_fieldsThedisplay_in_profile_summaryparameter can now be set to true for theParagraphfield type.

```
POST /realm/profile_fields
```

```
GET /realm/profile_fields
```
Feature level 475
- GET /events:realm_userevents withop: "update"are now sent when thedate_joinedfield is updated after an imported
  stub user or a user created via the API logs in for the first time.
- GET /users,GET /users/{user_id},GET /users/{email},GET /users/me: Thedate_joinedfield is initially
  set to the account creation time and is updated to the time of first login
  for imported stub users and users created via the API.

```
GET /events
```

```
GET /users/{user_id}
```

```
GET /users/{email}
```

```
GET /users/me
```
Feature level 474
- GET /events,POST /register:
  Removedapi_keyfield from bot objects.
- GET /events:realm_bot/updateevent is no longer
  sent when a bot's api key is regenerated.
- GET /events,POST /register:
  Removedavatar_url,bot_type,email,full_name,is_activeandowner_idfields from bot objects.
- GET /events:realm_bot/updateevent is no longer
  sent when updating a bot's avatar, email, name, or owner and also when
  deactivating or reactivating a bot.

```
GET /events
```

```
POST /register
```

```
GET /events
```

```
GET /events
```

```
POST /register
```

```
GET /events
```
Feature level 473
- POST /users/{user_id}/status: Bots
  with administrator permissions can now use this endpoint.

```
POST /users/{user_id}/status
```
Feature level 472
- GET /attachments,GET /events:
  Previously, themessagesfield inAttachmentwas array of
  objects containingidanddate_sentproperties. That has been replaced
  by amessage_idsfield, which is a flat array of message IDs.

```
GET /attachments
```

```
GET /events
```
Feature level 471
- GET /events,GET /realm/linkifiers,POST /realm/filters,PATCH /realm/filters/{filter_id}:
  Addedexample_inputandreverse_templateto linkifier objects.example_inputis a sample string matching the url_pattern for the linkifier.reverse_templateis a string that can process input params and turn a url into
  it's abbreviated form.reverse_templaterequiresexample_inputto be provided.
  Pass an empty string during PATCH to set either of these fields back to null, given
  they satisfy the requirements stated above.

```
GET /events
```

```
GET /realm/linkifiers
```

```
POST /realm/filters
```

```
PATCH /realm/filters/{filter_id}
```
Feature level 470
- POST /remove_client_device:
  Added a new endpoint to remove a registered device.

```
POST /remove_client_device
```
Feature level 469
- PATCH /realm,POST /register,GET /events: Added a newmedia_preview_sizerealm setting that controls the size of
  image and video thumbnails in messages.

```
POST /register
```

```
GET /events
```
Feature level 468
- POST /register_client_device:
  Added a new endpoint to register a logged-in device.
- POST /register: Addeddevicesfield to response.
- GET /events:  Adeviceevent is sent
  to clients to live-update thedevicesdictionary.
- POST /mobile_push/register: Redesigned
  the endpoint to support rotation ofpush_keyand FCM/APNs provided token.
- POST /remotes/push/e2ee/register:
  Replacedpush_account_idwithtoken_idto support rotation
  ofpush_keyand FCM/APNs provided token.
- POST /mobile_push/e2ee/test_notification:
  Replacedpush_account_idparameter withdevice_id.
- POST /register: Removedpush_devicesfield from response.
- GET /events: Removedpush_deviceevent.

```
POST /register_client_device
```

```
POST /register
```

```
GET /events
```

```
POST /mobile_push/register
```

```
POST /remotes/push/e2ee/register
```

```
POST /mobile_push/e2ee/test_notification
```

```
POST /register
```

```
GET /events
```
Feature level 467
- Message formatting: The new Markdown
  image syntax now only supports/permits uploaded images, not
  third-party image URLs.
Feature level 466
- POST /register: Addedrealm_uuidfield to response. Used by clients that prefer to compute
  Jdenticon avatars locally.
- POST /register,GET
  /events: Theavatar_sourcefields may now have
  the value"J", for Jdenticons.

```
POST /register
```

```
POST /register
```

```
GET
  /events
```
Feature level 465
- POST /register,GET /events,PATCH /realm: Nextcloud Talk integration added as an option
  for the realm settingvideo_chat_provider.
- POST /calls/nextcloud_talk/create:
  Added a new endpoint to create a Nextcloud Talk video call URL.

```
POST /register
```

```
GET /events
```

```
POST /calls/nextcloud_talk/create
```
Feature level 464
- GET /events: The server now sends arealm/update_dictevent instead ofrealm/updateevent when a
  Realm'sdescriptionproperty is changed.

```
GET /events
```
Feature level 463
- GET /bots/{bot_id}/api_key: Added
  new endpoint to get a bot's API key.

```
GET /bots/{bot_id}/api_key
```
Feature level 462
- GET /events: Addedrendered_descriptionfield
  to the realm update event when thedescriptionproperty is
  changed. Note that this new field was removed and replaced with the
  standardupdate_dictmechanism in feature level 464.

```
GET /events
```
Feature level 461
- GET /events:realm_botupdate events are
  now sent when a bot's Zulip display email address is changed.

```
GET /events
```
Feature level 460
- POST /register,GET /events,PATCH /realm: Constructor Groups integration added as an option
  for the realm settingvideo_chat_provider.
- POST /calls/constructorgroups/create:
  Added a new endpoint to create a Constructor Groups video call URL.

```
POST /register
```

```
GET /events
```

```
POST /calls/constructorgroups/create
```
Feature level 459
- DELETE /users/{user_id}: Added new
  parameteractionsthat asks the server to perform additional
  actions, such as deleting messages the user sent, while deactivating
  the user.

```
DELETE /users/{user_id}
```
Feature level 458
- GET users/{user_id}/channels: Fixed
  missing support for querying subscriptions of bot users.
- GET /users/{user_id}/subscriptions/{stream_id}:
  Fixed missing support for querying subscriptions of bot users.
- GET /user_groups/{user_group_id}/members/{user_id}:
  Fixed missing support for querying group membership of bot users.

```
GET users/{user_id}/channels
```

```
GET /users/{user_id}/subscriptions/{stream_id}
```

```
GET /user_groups/{user_group_id}/members/{user_id}
```
Feature level 457
GET /events:delete_messageevents are now
  sent to the user who deletes the message only if they have content
  access to the messages' recipient, and themessage_idslist only
  includes IDs of the messages that they can access.

```
GET /events
```
Feature level 456
- PATCH /realm,POST /register,GET /events: Added a newdefault_avatar_sourcerealm setting.

```
POST /register
```

```
GET /events
```
Feature level 455
- POST /register,GET
  /events,POST
  /realm/profile_fields,GET
  /realm/profile_fieldsAdded a new
  parameteruse_for_user_matchingto custom profile field objects,
  which indicates whether this custom profile field should be used to
  match users in typeahead.

```
POST /register
```

```
GET
  /events
```

```
POST
  /realm/profile_fields
```

```
GET
  /realm/profile_fields
```
Feature level 454
- PATCH /realm/user_settings_defaultsPOST /register,GET /events,PATCH /settings: Changed theweb_home_viewvalue for the recent view to "recent".

```
PATCH /realm/user_settings_defaults
```

```
POST /register
```

```
GET /events
```

```
PATCH /settings
```
Feature level 453
- POST /register:gif_rating_optionswas renamed togif_rating_policy_options.
- POST /register:realm_giphy_ratingwas
  renamed torealm_gif_rating_policyto reflect that it's shared
  between all GIF picker integrations.
- GET /events,PATCH /realm:giphy_ratingwas renamed togif_rating_policyto reflect that it's shared
  between all GIF picker integrations.

```
POST /register
```

```
POST /register
```

```
GET /events
```
Feature level 452
- GET /events: Messages deleted via a message
  retention policy now correctly generatedelete_messageevents.

```
GET /events
```
Feature level 451
- Message formatting: Changed the
rendering of invalid timestamps from a<span class="timestamp-error">element to plain escaped text.
Feature level 450
- GET /events: Thepush_deviceevents now
  encodepush_account_idas an integer, not a string.

```
GET /events
```
Feature level 449
- POST /export/realm: Theexport_typeparameter now
  takes string values (public,full_with_consent,full_without_consent)
  instead of integers. The newfull_without_consentoption requests a full
  export that includes private data for all users and requires the organization
  to have theowner_full_content_accessflag set to True.
- GET /export/realm,GET /events:export_typefields now contain the new string values, matching thePOST /export/realmparameter format. These endpoints now reportexport_type=full_without_consentfor a full export that includes private data
  for all users.

```
POST /export/realm
```

```
GET /export/realm
```

```
GET /events
```
Feature level 448
- GET /streams/{stream_id}/email_address:
  Users have access to a channel's email address only if they have permission
  to post messages in the channel.

```
GET /streams/{stream_id}/email_address
```
Feature level 447
- PATCH /bots/{bot_id}: Addedshort_nameparameter to support updating bot's email.
Feature level 446
- GET /messages,GET /messages/matches_narrow,POST /messages/flags/narrow,POST /register:
  Added support for a newsearch/narrow filter,mentions. This operator filters messages that contain a direct,
  visible personal mention of the specified user.

```
GET /messages
```

```
GET /messages/matches_narrow
```

```
POST /messages/flags/narrow
```

```
POST /register
```
Feature level 445
- GET /messages: Added a newdatevalue for
   theanchorparameter, and newanchor_dateparameter, to support
   fetching messages around a specific date/time.

```
GET /messages
```
Feature level 444
- PATCH /settings: Added support for bulk updating
  settings for specified users or members of user groups usingtarget_usersandskip_if_already_editedparameters.

```
PATCH /settings
```
Feature level 443
- GET /attachments,GET /events:
  Thecreate_timeanddate_sentfields inattachmentobjects will now
  return UNIX timestamps in seconds. Previously, these values were returned in
  milliseconds.
- PATCH /messages/{message_id}: Thecreate_timeanddate_sentfields indetached_uploadsobject will now return UNIX timestamps
  in seconds. Previously, these values were returned in milliseconds.

```
GET /attachments
```

```
GET /events
```

```
PATCH /messages/{message_id}
```
Feature level 442
- GET /events:giphy_ratingis now used to denote
  the common rating configured for both Tenor and GIPHY integrations.
- POST /register: Added newtenor_api_keyfield, which is required to fetch GIFs using the Tenor API.
- POST /register: Renamedgiphy_rating_optionstogif_rating_optionsto generalize the
  ratings for both GIPHY and Tenor integrations.realm_giphy_ratingis now used for both the Tenor and GIPHY integrations.

```
GET /events
```

```
POST /register
```

```
POST /register
```
Feature level 441
- GET /users/me/subscriptions,GET /streams,GET /events,POST /register: Addedcan_create_topic_groupfield which is agroup-setting valuedescribing
  the set of users with permissions to create new topics in the channel.
- POST /users/me/subscriptions,PATCH /streams/{stream_id}: Addedcan_create_topic_groupparameter to support setting and changing the user group whose members can create
  new topics in the specified channel.

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
GET /events
```

```
POST /register
```

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```
Feature level 440
- GET users/<user_id>/channelsAdded a new endpoint to get the channels another user is subscribed to.

```
GET users/<user_id>/channels
```
Feature level 439
- GET /events: The deprecatedupdate_display_settingsandupdate_global_notificationsevent types are no longer sent to any
  clients. These legacy event types were deprecated in Zulip 5.0 (feature
  level 89) and replaced by theuser_settingsevent
  type.

```
GET /events
```

```
user_settings
```
Feature level 438
- POST /register: Addedrealm_owner_full_content_accessfield indicating whether the
  organization's security model allows owners to access all private
  content in this organization.

```
POST /register
```
Feature level 437
- GET /users,GET
  /users/{user_id},GET
  /users/{email}: Fixed a bug dating to
  feature level 232, where guest users might incorrectly receive fake
  backwards-compatibility users in the format intended for clients
  usingPOST /registerwithout theuser_list_incompleteclient
  capability.
- Message formatting: Added support for
  Markdown image syntax, in addition to the previous link-derived
  image previews; these can be inserted into any block-level element.

```
GET
  /users/{user_id}
```

```
GET
  /users/{email}
```
Feature level 436
- Message formatting: Added new
  specification that emoji-only messages should show enlarged emoji.
Feature level 435
- POST /register: Addedserver_report_message_typesfield which contains a list of supported report types for themessage
  reportfeature.
- POST /message/{message_id}/report: Clients
  that support themessage reportfeature
  should use thekeyvalues in theserver_report_message_typesas the
  valid values for thereport_typeparameter. Prior to this feature
  level, the valid values for thereport_typeparameter were limited to:"harassment","inappropriate","norms","other","spam".

```
POST /register
```

```
POST /message/{message_id}/report
```
Feature level 434
- POST /register,POST /events,PATCH /realm: Added a newsend_channel_events_messagesrealm setting indicating
  whether channel event messages are sent in the organization.

```
POST /register
```

```
POST /events
```
Feature level 433
- GET /users,GET /users/{user_id},GET /users/{email}andGET /users/me: Addedis_imported_stubfield to
  returned user objects.
- POST /register: Addedis_importedfield
  in the user objects returned in therealm_usersfield and in the bot
  objects returned incross_realm_botsfield.
- GET /events: Addedis_imported_stubfield to
  user objects sent inrealm_userevents.

```
GET /users/{user_id}
```

```
GET /users/{email}
```

```
GET /users/me
```

```
POST /register
```

```
GET /events
```
Feature level 432
- POST /mobile_push/register: Replacedpush_public_keyparameter withpush_key.

```
POST /mobile_push/register
```
Feature level 431
- POST /register,PATCH /settings,PATCH /realm/user_settings_defaults:
  Added newweb_inbox_show_channel_foldersdisplay setting,
  controlling whether anychannel foldersconfigured by the organization are used to organize how conversations
  with unread messages are displayed in the web/desktop application's
  Inbox view.

```
POST /register
```

```
PATCH /settings
```

```
PATCH /realm/user_settings_defaults
```
Feature level 430
- GET /export/realm/consents: Added an
  integer fieldemail_address_visibilityto the objects in theexport_consentsarray.

```
GET /export/realm/consents
```
Feature level 429
- Replaced thepm_usersfield withrecipient_user_idsinE2EE mobile push notifications payloadfor group direct message. Previously,pm_userswas included only
for group DMs;recipient_user_idsis present for both 1:1 and
group DM conversations.
Feature level 428
- GET /events: When a user is deactivated,peer_removeevents are now sent for archived streams as well,
  not just unarchived ones.

```
GET /events
```
Feature level 427
- POST /register:stream_creator_or_nobodyvalue fordefault_group_namefield inserver_supported_permission_settingsobject is renamed tochannel_creator.

```
POST /register
```
Feature level 426
- POST /register: Removed therealm_is_zephyr_mirror_realmproperty from the response.

```
POST /register
```
Feature levels 421-424 reserved for future use in 11.x maintenance
releases.

## Changes in Zulip 11.0
Feature level 421
No changes; API feature level used for the Zulip 11.0 release.
Feature level 420
- POST /mobile_push/e2ee/test_notification:
  Added a new endpoint to send an end-to-end encrypted test push notification
  to the user's selected mobile device or all of their mobile devices.

```
POST /mobile_push/e2ee/test_notification
```
Feature level 419
- POST /register: Addedsimplified_presence_eventsclient capability,
  which allows clients to specify whether they support receiving thepresenceevent type with user presence data in the modern API format.
- GET /events: Added thepresencesfield to thepresenceevent type for clients that support thesimplified_presence_eventsclient capability.
  Thepresencesfield will have the user presence data in the modern
  API format. For clients that don't support that client capability the
  event will contain fields with the legacy format for user presence data.

```
POST /register
```

```
GET /events
```
Feature level 418
- GET /events: An event withtype: "channel_folder"andop: "reorder"is sent when channel folders are reordered.

```
GET /events
```
Feature level 417
- POST channels/create: Added a dedicated
  endpoint for creating a new channel. Previously, channel creation
  was done entirely throughPOST /users/me/subscriptions.

```
POST channels/create
```

```
POST /users/me/subscriptions
```
Feature level 416
- POST /invites,POST
  /invites/multiuse: Added a new parameterwelcome_message_custom_textwhich allows the users to add a
  Welcome Bot custom message for new users through invitations.
- POST /register,POST /events,PATCH /realm: Addedwelcome_message_custom_textrealm setting which is the
  default custom message for the Welcome Bot when sending invitations to new users.
- POST /realm/test_welcome_bot_custom_message:
  Added new endpoint test messages with the Welcome Bot custom message. The test
  messages are sent to the acting administrator, allowing them to preview how the
  custom welcome message will appear to new users upon joining the organization.

```
POST /invites
```

```
POST
  /invites/multiuse
```

```
POST /register
```

```
POST /events
```

```
POST /realm/test_welcome_bot_custom_message
```
Feature level 415
- POST /reminders: Added parameternoteto allow users to add notes to their reminders.
- POST /register: Addedmax_reminder_note_lengthfor clients to restrict the reminder note length before sending it to
  the server.

```
POST /reminders
```

```
POST /register
```
Feature level 414
- POST /channel_folders/create,GET /channel_folders,PATCH /channel_folders/{channel_folder_id}:
  Added a new fieldorderto show in which order should channel folders be
  displayed. The list is 0-indexed and works similar to theorderfield of
  custom profile fields.
- PATCH /channel_folders: Added a new
  endpoint for reordering channel folders. It accepts an array of channel
  folder IDs arranged in the order the user desires it to be in.
- GET /channel_folders: Channel folders will
  be ordered by theorderfield instead ofidfield when being returned.

```
POST /channel_folders/create
```

```
GET /channel_folders
```

```
PATCH /channel_folders/{channel_folder_id}
```

```
PATCH /channel_folders
```

```
GET /channel_folders
```
Feature level 413
- Mobile push notification payloads for APNs no longer contain theserverandrealm_idfields, which were unused.
- Mobile push notification payloads for FCM to remove push
  notifications no longer contain the legacy pre-2019zulip_message_idfield; all functional clients support the newerzulip_message_ids.
- Mobile push notification payloads for FCM to for new messages no
  longer contain the (unused)content_truncatedboolean field.
- E2EE mobile push notification payloads now have amodernized and
  documented format.
Feature level 412
- POST /register,GET /users/me/subscriptions:
  Added support for passingpartialas argument toinclude_subscribersparameter to get only partial subscribers data of the channel.
- POST /register,GET /users/me/subscriptions:
  Addedpartial_subscribersfield insubscriptionobjects.

```
POST /register
```

```
GET /users/me/subscriptions
```

```
POST /register
```

```
GET /users/me/subscriptions
```
Feature level 411
- POST /register,PATCH /settings,PATCH /realm/user_settings_defaults:
  Added newweb_left_sidebar_show_channel_foldersdisplay setting,
  controlling whether anychannel foldersconfigured by the organization are used to organize how channels
  are displayed in the web/desktop application's left sidebar.

```
POST /register
```

```
PATCH /settings
```

```
PATCH /realm/user_settings_defaults
```
Feature level 410
- POST /register: Addedmax_channel_folder_name_lengthandmax_channel_folder_description_lengthfields to the response.
- Mobile push notification payloads for APNs no longer contain thetimefield, which was unused.

```
POST /register
```
Feature level 409
- PATCH /realm,POST /register,GET /events: Added a newrequire_e2ee_push_notificationsrealm setting.

```
POST /register
```

```
GET /events
```
Feature level 407
- GET /users/me/subscriptions,GET /streams,GET /events,POST /register: Addedcan_delete_any_message_groupfield which is agroup-setting valuedescribing the
  set of users with permissions to delete any message in the channel.
- POST /users/me/subscriptions,PATCH /streams/{stream_id}: Addedcan_delete_any_message_groupparameter to support setting and
  changing the user group whose members can delete any message in the specified
  channel.
- PATCH /realm,POST /register,GET /events: Addedcan_set_delete_message_policy_grouprealm setting, which is agroup-setting valuedescribing the set of users with permission to change per-channelcan_delete_any_message_groupandcan_delete_own_message_groupsettings.
- GET /users/me/subscriptions,GET /streams,GET /events,POST /register: Addedcan_delete_own_message_groupfield which is agroup-setting valuedescribing the
  set of users with permissions to delete the messages they have sent in the channel.
- POST /users/me/subscriptions,PATCH /streams/{stream_id}: Addedcan_delete_own_message_groupparameter to support setting and
  changing the user group whose members can delete the messages they have sent
  in the channel.
- POST /users/{user_id}/status: Added
  new API endpoint for an administrator to update the status for
  another user.

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
GET /events
```

```
POST /register
```

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```

```
POST /register
```

```
GET /events
```

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
GET /events
```

```
POST /register
```

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```

```
POST /users/{user_id}/status
```
Feature level 406
- POST /register: Addedpush_devicesfield to response.
- GET /events: Apush_deviceevent is sent
  to clients when registration to bouncer either succeeds or fails.
- POST /mobile_push/register: Added
  an endpoint to register a device to receive end-to-end encrypted
  mobile push notifications.

```
POST /register
```

```
GET /events
```

```
POST /mobile_push/register
```
Feature level 405
- Message formatting: Added new HTML
  formatting for uploaded audio files generating a player experience.
Feature level 404
- GET /users/me/subscriptions,GET /streams,GET /events,POST /register: Added new"empty_topic_only"option to thetopics_policyfield on Stream and Subscription
  objects.
- POST /users/me/subscriptions,PATCH /streams/{stream_id}: Added new"empty_topic_only"option totopics_policyparameter for"general chat" channels.

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
GET /events
```

```
POST /register
```

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```
Feature level 403
- POST /register: Added aurl_optionsobject
  to therealm_incoming_webhook_botsobject for incoming webhook
  integration URL parameter options. Previously, these optional URL
  parameters were included in theconfig_optionsfield (see feature
  level 318 entry). Theconfig_optionsobject is now reserved for
  configuration data that can be set when creating an bot user for a
  specific incoming webhook integration.

```
POST /register
```
Feature level 402
- GET /users/me/subscriptions,GET /streams,GET /events,POST /register: Addedcan_resolve_topics_groupwhich is agroup-setting valuedescribing the
  set of users with permissions to resolve topics in the channel.
- POST /users/me/subscriptions,PATCH /streams/{stream_id}: Addedcan_resolve_topics_groupwhich is agroup-setting valuedescribing the
  set of users with permissions to resolve topics in the channel.

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
GET /events
```

```
POST /register
```

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```
Feature level 401
- POST /register,PATCH
  /settings,PATCH
  /realm/user_settings_defaults:
  Added new option in user settingweb_channel_default_view, to navigate
  to top unread topic in channel.

```
POST /register
```

```
PATCH
  /settings
```

```
PATCH
  /realm/user_settings_defaults
```
Feature level 400
- Markdown message formatting:
  The server now prefers the latest message in a topic, not the
  oldest, when constructing topic permalinks using the/with/operator.
Feature level 399
- GET /events:
  Addedremindersevents sent to clients when a user creates
  or deletes scheduled messages.
- GET /reminders:
  Clients can now request/remindersendpoint to fetch all
  scheduled reminders.
- DELETE /reminders/{reminder_id}:
  Clients can now delete a scheduled reminder.

```
GET /events
```

```
GET /reminders
```

```
DELETE /reminders/{reminder_id}
```
Feature level 398
- POST /register,PATCH /settings,PATCH /realm/user_settings_defaults:
  Added newweb_left_sidebar_unreads_count_summarydisplay setting,
  controlling whether summary unread counts are displayed in the left sidebar.

```
POST /register
```

```
PATCH /settings
```

```
PATCH /realm/user_settings_defaults
```
Feature level 397
- POST /users/me/subscriptions: Added parametersend_new_subscription_messageswhich determines whether the user
  would like Notification Bot to notify other users who the request
  adds to a channel.
- POST /users/me/subscriptions: Addednew_subscription_messages_sentto the response, which is only
  present ifsend_new_subscription_messageswastruein the request.
- POST /register: Addedmax_bulk_new_subscription_messagesto the response.

```
POST /users/me/subscriptions
```

```
POST /users/me/subscriptions
```

```
POST /register
```
Feature level 396
- GET /users/me/subscriptions,GET /streams,GET /events,POST /register: Addedcan_move_messages_within_channel_groupfield which is agroup-setting valuedescribing the
  set of users with permissions to move messages within the channel.
- POST /users/me/subscriptions,PATCH /streams/{stream_id}: Addedcan_move_messages_within_channel_groupparameter to support setting and
  changing the user group whose members can move messages within the specified
  channel.
- GET /users/me/subscriptions,GET /streams,GET /events,POST /register: Addedcan_move_messages_out_of_channel_groupfield which is agroup-setting valuedescribing the
  set of users with permissions to move messages out of the channel.
- POST /users/me/subscriptions,PATCH /streams/{stream_id}: Addedcan_move_messages_out_of_channel_groupparameter to support setting and
  changing the user group whose members can move messages out of the specified
  channel.

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
GET /events
```

```
POST /register
```

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
GET /events
```

```
POST /register
```

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```
Feature level 395
- Markdown message
  formatting: Previously,
  Zulip's Markdown syntax had special support for previewing Dropbox
  albums. Dropbox albums no longer exist, and links to Dropbox folders
  now consistently use Zulip's standard open graph preview markup.
Feature level 394
- POST /register,GET
  /events,GET /streams,GET /streams/{stream_id}: Added a new
  fieldsubscriber_countto Stream and Subscription objects with the
  total number of non-deactivated users who are subscribed to the
  channel.

```
POST /register
```

```
GET
  /events
```

```
GET /streams
```

```
GET /streams/{stream_id}
```
Feature level 393
- PATCH /messages/{message_id},POST /register,GET /events:
  Indelete_messageevent, all themessage_idswill now be sorted in
  increasing order.
- PATCH /messages/{message_id},POST /register,GET /events:
  Inupdate_messageevent, all themessage_idswill now be sorted in
  increasing order.

```
PATCH /messages/{message_id}
```

```
POST /register
```

```
GET /events
```

```
PATCH /messages/{message_id}
```

```
POST /register
```

```
GET /events
```
Feature level 392
- GET /users/me/subscriptions,GET /streams,GET /events,POST /register: Added thetopics_policyfield to Stream and Subscription objects to support channel-level
  configurations for sending messages to the empty"general chat"
  topic.
- POST /users/me/subscriptions,PATCH /streams/{stream_id}: Addedtopics_policyparameter to support setting and updating the
  channel-level configuration for sending messages to the
  empty"general chat" topic.
- PATCH /realm,GET /events,POST /register: Addedcan_set_topics_policy_grouprealm setting, which is agroup-setting valuedescribing the set
  of users with permission to change the per-channeltopics_policysetting.
- PATCH /realm,GET /events,POST /register:
  Added a new realmtopics_policysetting for the organization's
  default policy for sending channel messages to the empty"general
  chat" topic.
- GET /events,POST /register:
  Deprecated the realmmandatory_topicssetting in favor of the new
  realmtopics_policysetting.
- PATCH /realm: Removed themandatory_topicsparameter as it is now
  replaced by the realmtopics_policysetting.

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
GET /events
```

```
POST /register
```

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```

```
GET /events
```

```
POST /register
```

```
GET /events
```

```
POST /register
```

```
GET /events
```

```
POST /register
```
Feature level 391
- POST /user_groups/{user_group_id}/members,POST /user_groups/{user_group_id}/subgroups:
  Adding/removing members and subgroups to a deactivated group is now allowed.

```
POST /user_groups/{user_group_id}/members
```

```
POST /user_groups/{user_group_id}/subgroups
```
Feature level 390
- GET /events: Events withtype: "navigation_view"are
  sent to the user when a navigation view is created, updated, or removed.
- POST /register: Addednavigation_viewsfield in
  response.
- GET /navigation_views: Added a new endpoint for
  fetching all navigation views of the user.
- POST /navigation_views: Added a new endpoint for
  creating a new navigation view.
- PATCH /navigation_views/{fragment}: Added a new
  endpoint for editing the details of a navigation view.
- DELETE /navigation_views/{fragment}: Added a new
  endpoint for removing a navigation view.

```
GET /events
```

```
POST /register
```

```
GET /navigation_views
```

```
POST /navigation_views
```

```
PATCH /navigation_views/{fragment}
```

```
DELETE /navigation_views/{fragment}
```
Feature level 389
- POST /channel_folders/create: Added
  a new endpoint for creating a new channel folder.
- GET /channel_folders: Added a new endpoint
  to get all channel folders in the realm.
- PATCH /channel_folders/{channel_folder_id}:
  Added a new endpoint to update channel folder.
- POST /register: Addedchannel_foldersfield to
  response.
- GET /events: An event withtype: "channel_folder"is
  sent to all users when a channel folder is created.
- GET /users/me/subscriptions,GET /streams,GET /events,POST /register: Addedfolder_idfield
  to Stream and Subscription objects.
- POST /users/me/subscriptions: Added support to add
  newly created channels to folder usingfolder_idparameter.
- PATCH /streams/{stream_id}: Added support
  for updating folder to which the channel belongs.
- GET /events: An event withtype: "channel_folder"is
  sent to all users when a channel folder is updated.
- GET /events:valuefield instream/updateevents can havenullwhen channel is removed from a folder.

```
POST /channel_folders/create
```

```
GET /channel_folders
```

```
PATCH /channel_folders/{channel_folder_id}
```

```
POST /register
```

```
GET /events
```

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
GET /events
```

```
POST /register
```

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```

```
GET /events
```

```
GET /events
```
Feature level 388
- PATCH /streams/{stream_id}: Addedis_archivedparameter to support unarchiving previously archived
  channels.

```
PATCH /streams/{stream_id}
```
Feature level 387
- GET /users: This endpoint no longer requires
  authentication for organizations using thepublic access
  option.
Feature level 386
- PATCH /user_groups/{user_group_id}:
  Added support to reactivate groups by passingdeactivatedparameter asFalse.

```
PATCH /user_groups/{user_group_id}
```
Feature level 385
- POST /register,PATCH/settings,PATCH/realm/user_settings_defaults:
  Added newresolved_topic_notice_auto_read_policysetting, which controls
  how resolved-topic notices are marked as read for a user.

```
POST /register
```

```
PATCH/settings
```

```
PATCH/realm/user_settings_defaults
```
Feature level 384
- GET /users: Addeduser_idsquery parameter to
  fetch data only for the provideduser_ids.
Feature level 383
- POST /register,PATCH
  /settings,PATCH
  /realm/user_settings_defaults:
  Added new option in user settingweb_channel_default_view, to show
  inbox view style list of topics.

```
POST /register
```

```
PATCH
  /settings
```

```
PATCH
  /realm/user_settings_defaults
```
Feature level 382
- POST /message/{message_id}/report: Added a new
  endpoint forsubmitting a moderation requestfor a message.

```
POST /message/{message_id}/report
```
Feature level 381
- POST /reminders: Added a new endpoint to
  schedule personal reminder for a message.

```
POST /reminders
```
Feature level 380
- POST /register,GET
  /events: Theis_moderatorconvenience field now
  is true for organization administrators, matching howis_adminworks for organization owners.

```
POST /register
```

```
GET
  /events
```
Feature level 379
- PATCH /messages/{message_id}: Added
 optional parameterprev_content_sha256, which clients can use to
 prevent races with the message being edited by another client.

```
PATCH /messages/{message_id}
```
Feature level 378
- GET /events: Archiving and unarchiving
  streams now sendupdateevents to clients that declared
  thearchived_channelsclient capability.deleteandcreateevents are still sent to clients that did not declarearchived_channelsclient capability.
- POST /register: Thestreamsdata
  structure now includes archived channels for clients that
  declared thearchived_channelsclient capability.

```
GET /events
```

```
POST /register
```
Feature level 377
- GET /events: When a user is deactivate, sendpeer_removeevent to all the subscribers of the streams that the
  user was subscribed to.

```
GET /events
```
Feature levels 373-376 reserved for future use in 10.x maintenance
releases.

## Changes in Zulip 10.1
Feature level 372
- POST /typing: The"(no topic)"value
  when used fortopicparameter is now interpreted as an empty string.

```
POST /typing
```

## Changes in Zulip 10.0
Feature level 371
No changes; feature level used for Zulip 10.0 release.
Feature level 370
- POST /messages,POST /scheduled_messages,PATCH /scheduled_messages/<int:scheduled_message_id>:
  The"(no topic)"value when used fortopicparameter is
  now interpreted as an empty string.

```
POST /messages
```

```
POST /scheduled_messages
```

```
PATCH /scheduled_messages/<int:scheduled_message_id>
```
Feature level 369
- POST /register: Addednavigation_tour_video_urlto the response.

```
POST /register
```
Feature level 368
- GET /events: An event withtype: "saved_snippet"andop: "update"is sent to the current user when a saved snippet is edited.
- PATCH /saved_snippets/{saved_snippet_id}:
  Added a new endpoint for editing a saved snippet.

```
GET /events
```

```
PATCH /saved_snippets/{saved_snippet_id}
```
Feature level 367
- POST /register,POST /events:
  Added newcan_resolve_topics_grouprealm setting, which is agroup-setting valuedescribing the set of
  users with permission to resolve topics in a stream.

```
POST /register
```

```
POST /events
```
Feature level 366
- GET /messages,GET /messages/matches_narrow,POST /messages/flags/narrow,POST /register:
  Added a newsearch/narrow filter,is:muted, matching messages in topics and channels that the user
  hasmuted.

```
GET /messages
```

```
GET /messages/matches_narrow
```

```
POST /messages/flags/narrow
```

```
POST /register
```
Feature level 365
- GET /events,GET /messages,GET /messages/{message_id}: Addedlast_moved_timestampfield to message objects for when the message
  was last moved to a different channel or topic. If the message's topic
  has only beenresolved or unresolved, then
  the field is not present. Clients should use this field, rather than
  parsing the message object'sedit_historyarray, to display an
  indicator that the message has been moved.
- GET /events,GET /messages,GET /messages/{message_id}: Thelast_edit_timestampfield on message objects is only present if the
  message's content has been edited. Previously, this field was present
  if the message's content had been edited or moved to a different
  channel or topic. Clients should use this field, rather than parsing
  the message object'sedit_historyarray, to display an indicator
  that the message has been edited.

```
GET /events
```

```
GET /messages
```

```
GET /messages/{message_id}
```

```
GET /events
```

```
GET /messages
```

```
GET /messages/{message_id}
```
Feature level 364
- PATCH /realm/user_settings_defaults,POST /register,PATCH /settingsGET /events: Removeddense_modesetting.

```
PATCH /realm/user_settings_defaults
```

```
POST /register
```

```
PATCH /settings
```

```
GET /events
```
Feature level 363
- PATCH /realm,GET /events,POST /register:
  Addedcan_manage_billing_grouprealm setting which is agroup-setting valuedescribing the set of users
  with permission manage plans and billing for the organization.
- POST /register: Added a newrealm_billingobject
  containing additional information about the organization's billing state,
  such as sponsorship request status.
- GET /users,GET /users/{user_id},GET /users/{email},GET /users/me,GET /events,POST /register:
  Removedis_billing_adminfield from user objects, as the permission to manage
  plans and billing in the organization is now controlled bycan_manage_billing_group.

```
GET /events
```

```
POST /register
```

```
POST /register
```

```
GET /users/{user_id}
```

```
GET /users/{email}
```

```
GET /users/me
```

```
GET /events
```

```
POST /register
```
Feature level 362
- POST /users/me/subscriptions,DELETE /users/me/subscriptions: Subscriptions
  in archived channels can now be edited by users with the appropriate
  permission, just like in non-archived channels.
- PATCH /streams/{stream_id}: Archived
  channels can now be converted between public and private channels,
  just like non-archived channels.
- POST /register: Thenever_subscribeddata
  structure now includes archived channels for clients that declared
  thearchived_channelsclient capability.

```
POST /users/me/subscriptions
```

```
DELETE /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```

```
POST /register
```
Feature level 361
- POST /messages/{message_id}/typing:
  RenamedPOST /messages/{message_id}/typingtoPOST /message_edit_typing, passing the onemessage_idparameter
  in the URL path, for consistency with the rest of the API.

```
POST /messages/{message_id}/typing
```
Feature level 360
- GET /messages/{message_id},GET
  /messages/{message_id}/read_receipts:
  Messages from an archived channels can now be read through these API
  endpoints, if the channel's access control permissions permit doing
  so.

```
GET /messages/{message_id}
```

```
GET
  /messages/{message_id}/read_receipts
```
Feature level 359
- PATCH /bots/{bot_user_id}: Previously, changing the owner of a bot
  unsubscribed the bot from any channels that the new owner was not
  subscribed to. This behavior was removed in favor of documenting the
  security trade-off associated with giving bots read access to
  sensitive channel content.
Feature level 358
- PATCH /realm,GET /events: Changedallow_edit_historyboolean field tomessage_edit_history_visibility_policyinteger field to
  support an intermediate field forMoves onlyedit history of messages.
- POST /register:realm_allow_edit_historyfield is
  deprecated and has been replaced byrealm_message_edit_history_visibility_policy.
  The value ofrealm_allow_edit_historyis set toFalseifrealm_message_edit_history_visibility_policyis configured as "None",
  andTruefor "Moves only" or "All" message edit history.

```
GET /events
```

```
POST /register
```
Feature level 357
- GET /users/me/subscriptions,GET /streams,GET /events,POST /register: Addedcan_subscribe_groupfield to Stream and Subscription objects.
- POST /users/me/subscriptions,PATCH /streams/{stream_id}: Addedcan_subscribe_groupparameter to support setting and changing the
  user group whose members can subscribe to the specified stream.

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
GET /events
```

```
POST /register
```

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```
Feature level 356
- GET /streams: The new parameterinclude_can_access_content, if set to True, returns all the
  channels that the user making the request has content access to.
- GET /streams: Renameinclude_all_activetoinclude_allsince the separateexclude_archivedparameter is
  what controls whether to include archived channels. Theinclude_allparameter is now supported for non-administrators.

```
GET /streams
```

```
GET /streams
```
Feature level 355
- POST /messages/flags/narrow,POST /messages/flags:
  Addedignored_because_not_subscribed_channelsfield in the response, which
  is a list of the channels whose messages were skipped to mark as unread
  because the user is not subscribed to them.

```
POST /messages/flags/narrow
```

```
POST /messages/flags
```
Feature level 354
- GET /messages,GET
  /messages/{message_id}, [POST
  /messages/flags/narrow]: Users can access messages in unsubscribed
  private channels that are accessible only via groups that grant
  content access.
- GET /messages/{message_id}/read_receipts:
  Users can access read receipts in unsubscribed private channels that are
  accessible only via groups that grant content access.
- POST /messages/{message_id}/reactions,DELETE /messages/{message_id}/reactions:
  Users can react to messages in unsubscribed private channels that are
  accessible only via groups that grant content access.
- POST /submessage: Users can interact with polls and similar
  widgets in messages in unsubscribed private channels that are
  accessible only via groups that grant content access.
- PATCH /messages/{message_id}: Users can
  edit messages they have posted in unsubscribed private channels that
  are accessible only via groups that grant content access.
- POST
  /message_edit_typing:
  Users can generate typing notifications when editing messages in
  unsubscribed private channels that are accessible only via groups
  that grant content access.
- POST /messages: Users can send messages to
  private channels with shared history without subscribing if they are
  part of groups that grant content access and also incan_send_message_group.

```
GET /messages
```

```
GET
  /messages/{message_id}
```

```
GET /messages/{message_id}/read_receipts
```

```
POST /messages/{message_id}/reactions
```

```
DELETE /messages/{message_id}/reactions
```

```
PATCH /messages/{message_id}
```

```
POST
  /message_edit_typing
```

```
POST /messages
```
Feature level 353
- POST /register,GET /events,PATCH /realm: Zoom Server to Server OAuth integration added as an option
  for the realm settingvideo_chat_provider.

```
POST /register
```

```
GET /events
```
Feature level 352
- PATCH /realm,POST /register,GET /events: Addedcan_mention_many_users_grouprealm setting, which is agroup-setting valuedescribing the set of users with permission to use wildcard mentions in large
  channels.
- PATCH /realm,GET /events: Removedwildcard_mention_policyproperty, as the permission to use wildcard mentions
  in large channels is now controlled bycan_mention_many_users_groupsetting.
- POST /register:realm_wildcard_mention_policyfield is deprecated, having been replaced bycan_mention_many_users_group.
  Notably, this backwards-compatiblerealm_wildcard_mention_policyvalue
  now contains the superset of the true value that best approximates the actual
  permission setting.

```
POST /register
```

```
GET /events
```

```
GET /events
```

```
POST /register
```
Feature level 351
- POST /message_edit_typing:
  Added a new endpoint for sending typing notification when a message is
  being edited both in streams and direct messages.
- GET /events: The newtyping_edit_messageevent
  is sent when a user starts editing a message.

```
POST /message_edit_typing
```

```
GET /events
```
Feature level 350
- POST /register: Addedserver_can_summarize_topicsto the response.
- POST /register,POST /events,PATCH /realm: Addedcan_summarize_topics_grouprealm setting which is
  agroup-setting valuedescribing the set of
  users with permission to use AI summarization.
- PATCH /realm/user_settings_defaults,POST /register,PATCH /settings:
  Added newhide_ai_featuresoption for hiding all AI features in the UI.

```
POST /register
```

```
POST /register
```

```
POST /events
```

```
PATCH /realm/user_settings_defaults
```

```
POST /register
```

```
PATCH /settings
```
Feature level 349
- POST /users/me/subscriptions: Users belonging tocan_add_subscribers_groupshould be able to add subscribers to a
  private channel without being subscribed to it.
- DELETE /users/me/subscriptions: Channel
  administrators can now unsubscribe other users even if they are not
  an organization administrator or part ofcan_remove_subscribers_group.
- PATCH /streams/{stream_id},DELETE /streams/{stream_id}: Channel and
  organization administrators can modify all the settings requiring
  only metadata access without having content access to it. They
  cannot add subscribers to the channel or change it's privacy setting
  without having content access to it.
- GET /events: All users with metadata access to
  a channel are now notified when a relevant stream event occurs.
  Previously, non-admin users who were channel admins or users
  belonging tocan_add_subscribers_groupwere not notified of events
  for a private channel they were not subscribed to.
- GET /events: If a user is a channel
  administrator for a private channel they are not subscribed to. That
  channel will now appear either in theunsubscribedornever_subscribedlist in subscription info.

```
POST /users/me/subscriptions
```

```
DELETE /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```

```
DELETE /streams/{stream_id}
```

```
GET /events
```

```
GET /events
```
Feature level 348
- POST /register,POST /events,PATCH /realm: Addedenable_guest_user_dm_warningsetting to decide
  whether clients should show a warning when a user is composing to a
  guest user in the organization.

```
POST /register
```

```
POST /events
```
Feature level 347
- Markdown message formatting:
  Links to topic without a specified message now use thewithoperator to follow moves of topics.
Feature level 346
- Markdown message formatting:
  Added support for empty string as a valid topic name in syntaxes
  for linking to topics and messages.
Feature level 345
- POST /remotes/server/register/transfer,POST /remotes/server/register/verify_challenge,POST /zulip-services/verify/{access_token}/: Added new API
  endpoints for transferring Zulip services registrations.
- POST /remotes/server/register: Added new response format for
  hostnames that are already registered.
Feature level 344
- PATCH /realm,GET /events,POST /register:
  Added two new realm settings,can_create_bots_groupwhich is agroup-setting valuedescribing the set of users
  with permission to create bot users in the organization, andcan_create_write_only_bots_groupwhich is agroup-setting valuedescribing the set of users
  with permission to create bot users who can only send messages in the organization
  in addition to the users who are incan_create_bots_group.
- PATCH /realm,GET /events: Removedbot_creation_policyproperty, as the permission to create bot users
  in the organization is now controlled by two new realm settings,can_create_bots_groupandcan_create_write_only_bots_group.

```
GET /events
```

```
POST /register
```

```
GET /events
```
Feature level 343
- GET /events: Added a new fieldstream_idsto replacestreamsin stream delete event and labelstreamsas deprecated.

```
GET /events
```
Feature level 342
- GET /users/me/subscriptions,GET /streams,GET /events,POST /register: Addedcan_add_subscribers_groupfield to Stream and Subscription
  objects.
- POST /users/me/subscriptions,PATCH /streams/{stream_id}: Addedcan_add_subscribers_groupparameter to support setting and
  changing the user group whose members can add other subscribers
  to the specified stream.
- POST /invites,POST
  /invites/multiuse: Users can now always
  include default channels in an invite's initial subscriptions.

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
GET /events
```

```
POST /register
```

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```

```
POST /invites
```

```
POST
  /invites/multiuse
```
Feature level 341
- PATCH /realm,GET /events,POST /register:
  Addedcan_add_subscribers_grouprealm setting which is agroup-setting valuedescribing the set of users
  with permission to add subscribers to channels in the organization.
- POST /register: Removedcan_subscribe_other_usersboolean field from the response.
- PATCH /realm,GET /events: Removedinvite_to_stream_policyproperty, as the permission to subscribe
  other users to channels in the organization is now controlled by thecan_add_subscribers_groupsetting.

```
GET /events
```

```
POST /register
```

```
POST /register
```

```
GET /events
```
Feature level 340
PATCH /user_groups/{user_group_id}: All
the permission settings and description can now be updated for
deactivated groups.

```
PATCH /user_groups/{user_group_id}
```
Feature level 339
- GET /events: Addeduserfield back inreactionevents, reverting part of the feature level 328
  changes. Note that this field was only restored in the events API,
  and remains deprecated, pending core clients fully migrating away
  from accessing it.

```
GET /events
```
Feature level 338
- POST /register: Addedpassword_max_lengthfield, which is the maximum allowed password length.

```
POST /register
```
Feature level 337
- POST /calls/bigbluebutton/create: Added avoice_onlyparameter
  controlling whether the call should be voice-only, in which case we
  keep cameras disabled for this call. Now the call creator is a
  moderator and all other joiners are viewers.
Feature level 336
- Markdown message formatting: Addeddata-original-content-typeattribute to convey the type of the original
  image, and optionaldata-transcoded-imageattribute for images with formats
  which are not widely supported by browsers.
Feature level 335
- GET /streams/{stream_id}/email_address:
  Added an optionalsender_idparameter to specify the ID of a user or bot
  which should appear as the sender when messages are sent to the channel using
  the returned channel email address.

```
GET /streams/{stream_id}/email_address
```
Feature level 334
- POST /register: Addedrealm_empty_topic_display_namefield for clients to use
  while adding support for empty string as topic name.
- POST /register: Addedempty_topic_nameclient capabilityto allow client to specify whether it supports empty string as a topic name
  inregisterresponse or events involving topic names.
  Clients that don't support this client capability receiverealm_empty_topic_display_namefield value as the topic name replacing
  the empty string.
- GET /events: For clients that don't support
  theempty_topic_nameclient capability,
  the following fields will have the value ofrealm_empty_topic_display_namefield replacing the empty string for channel messages:subjectfield in themessageevent typetopicfield in thedelete_messageevent typeorig_subjectandsubjectfields in theupdate_messageevent typetopic_namefield in theuser_topicevent typetopicfield in thetypingevent typetopicfield in theupdate_message_flagsevent type when removingreadflag
- GET /messages,GET /messages/{message_id}: Addedallow_empty_topic_nameboolean parameter to decide whether the topic names in the fetched messages
  can be empty strings.
- GET /messages/{message_id}/history:
  Addedallow_empty_topic_nameboolean parameter to decide whether the
  topic names in the fetched message history objects can be empty strings.
- GET /users/me/{stream_id}/topics:
  Addedallow_empty_topic_nameboolean parameter to decide whether the
  topic names in the fetchedtopicsarray can be empty strings.
- POST /register: For clients that don't support
  theempty_topic_nameclient capability,
  thetopicfield in theunread_msgsobject andtopic_namefield
  in theuser_topicsobjects will have the value ofrealm_empty_topic_display_namefield replacing the empty string
  for channel messages.

```
POST /register
```

```
POST /register
```

```
GET /events
```
- subjectfield in themessageevent type
- topicfield in thedelete_messageevent type
- orig_subjectandsubjectfields in theupdate_messageevent type
- topic_namefield in theuser_topicevent type
- topicfield in thetypingevent type
- topicfield in theupdate_message_flagsevent type when removingreadflag

```
GET /messages
```

```
GET /messages/{message_id}
```

```
GET /messages/{message_id}/history
```

```
GET /users/me/{stream_id}/topics
```

```
POST /register
```
Feature level 333
- Message formatting: System groups can now
  be silently mentioned.
- GET /users/me/subscriptions,GET /streams,GET /events,POST /register: Addedcan_send_message_groupwhich is agroup-setting valuedescribing the
  set of users with permissions to post in the channel.
- POST /users/me/subscriptions,PATCH /streams/{stream_id}: Addedcan_send_message_groupwhich is agroup-setting valuedescribing the
  set of users with permissions to post in the channel.
- GET /users/me/subscriptions,GET /streams,GET /events,POST /register:stream_post_policyfield is
  deprecated, having been replaced bycan_send_message_group. Notably,
  this backwards-compatiblestream_post_policyvalue now contains the
  superset of the true value that best approximates the actual permission
  setting.
- POST /users/me/subscriptions,PATCH /streams/{stream_id}: Removedstream_post_policyandis_announcement_onlyproperties, as the permission
  to post in the channel is now controlled bycan_send_message_groupsetting.

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
GET /events
```

```
POST /register
```

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
GET /events
```

```
POST /register
```

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```
Feature level 332
- POST /register: Addedserver_min_deactivated_realm_deletion_daysandserver_max_deactivated_realm_deletion_daysfields for the permitted
  number of days before full data deletion of a deactivated organization
  on the server.
- POST /realm/deactivate: Addeddeletion_delay_daysparameter to
  support setting when a full data deletion of the deactivated
  organization may be done.

```
POST /register
```
Feature level 331
- POST /register,POST /events,PATCH /realm: Addedmoderation_request_channel_idrealm setting, which is
  the ID of the private channel to which moderation requests will be sent.

```
POST /register
```

```
POST /events
```
Feature level 330
- POST /register,GET /events:
  Default channels data only includes channel IDs now instead of full
  channel data.
- POST /register,GET /events:
  Default channel groups data only includes channel IDs now instead of
  full channel data.

```
POST /register
```

```
GET /events
```

```
POST /register
```

```
GET /events
```
Feature level 329
- PATCH /realm/user_settings_defaults,POST /register,PATCH /settings:
  Added newweb_suggest_update_timezoneuser setting to indicate whether
  the user should be shown an alert, offering to update theirprofile
  time zone, when the time displayed for the
  profile time zone differs from the current time displayed by the time
  zone configured on their device.

```
PATCH /realm/user_settings_defaults
```

```
POST /register
```

```
PATCH /settings
```
Feature level 328
- GET /messages,GET /events:
  Removed deprecateduserdictionary from thereactionsobjects returned
  by the API, as the clients now useuser_idfield instead.

```
GET /messages
```

```
GET /events
```
Feature level 327
- GET /messages,GET
  /messages/{message_id},GET /events:
  Adjusted therecipient_idfield of an incoming 1:1 direct message to use the
  same value that would be used for an outgoing message in that conversation.

```
GET /messages
```

```
GET
  /messages/{message_id}
```

```
GET /events
```
Feature level 326
- POST /register: Removedallow_owners_groupfield from configuration data object of permission settings passed inserver_supported_permission_settings.
- POST /register: Removedid_field_namefield from configuration data object of permission settings passed
  inserver_supported_permission_settings.

```
POST /register
```

```
POST /register
```
Feature level 325
- GET /users/me/subscriptions,GET /streams,GET /events,POST /register: Addedcan_administer_channel_groupwhich is agroup-setting valuedescribing the
  set of users with permissions to administer the channel in addition to realm
  admins.
- POST /users/me/subscriptions,PATCH /streams/{stream_id}: Addedcan_administer_channel_groupwhich is agroup-setting valuedescribing the
  set of users with permissions to administer the channel in addition to realm
  admins.

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
GET /events
```

```
POST /register
```

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```
Feature level 324
- POST /register,GET /events,GET /user_groups: Addcan_remove_members_groupto user group objects.
- POST /user_groups/create: Addedcan_remove_members_groupparameter to support setting the user group which
  can remove members from the user group.
- PATCH /user_groups/{user_group_id}: Addedcan_remove_members_groupparameter to support changing the user group which
  can remove members from the specified user group.

```
POST /register
```

```
GET /events
```

```
GET /user_groups
```

```
POST /user_groups/create
```

```
PATCH /user_groups/{user_group_id}
```
Feature level 323
- POST /register,GET
  /events,GET /streams,GET /streams/{stream_id}: Added a new
  fieldis_recently_activeto stream objects as a new deterministic
  source of truth fordemote_inactive_streamsactivity decisions.

```
POST /register
```

```
GET
  /events
```

```
GET /streams
```

```
GET /streams/{stream_id}
```
Feature level 322
- POST /invites,POST
  /invites/multiuse: Added a new parametergroup_idswhich allows users to be added to user groups through
  invitations.

```
POST /invites
```

```
POST
  /invites/multiuse
```
Feature level 321
- PATCH /realm,GET /events,POST /register:
  Addedcan_invite_users_grouprealm setting which is agroup-setting valuedescribing the set of users
  with permission to send email invitations for inviting other users to the
  organization.
- PATCH /realm,GET /events: Removedinvite_to_realm_policyproperty, as the permission to send email invitations
  for inviting other users to the organization is now controlled bycan_invite_users_groupsetting.

```
GET /events
```

```
POST /register
```

```
GET /events
```
Feature level 320
- GET /users/me/subscriptions,GET /streams,GET /events,POST /register:can_remove_subscribers_groupfield can now either be an ID of a named user group with the permission,
  or an object describing the set of users and groups with the permission.
- POST /users/me/subscriptions,PATCH /streams/{stream_id}: Thecan_remove_subscribers_groupparameter can now either be an ID of a
  named user group or an object describing a set of users and groups.

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
GET /events
```

```
POST /register
```

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```
Feature level 319
- Markdown message
  formatting: Added
  newmessage-linkformat for special direct links to messages.
Feature level 318
- POST /register: Renamed theconfigobject in therealm_incoming_webhook_botsobject toconfig_options. This object now
  includes details about optional URL parameters that can be configured whengenerating a URLfor an incoming webhook
  integration. Previously, this object was reserved for key-value pairs that
  indicated that a bot user could be created with additional configuration
  data (such as an API key) for that incoming webhook integration, but this
  functionality has not been implemented for any existing integrations.

```
POST /register
```
Feature level 317
- POST /user_groups/create:
  Addedgroup_idto the success response of the user group creation
  endpoint, enabling clients to easily access the unique identifier
  of the newly created user group.

```
POST /user_groups/create
```
Feature level 316
- PATCH /realm,GET /events,POST /register:
  Addedcan_move_messages_between_topics_grouprealm setting which is agroup-setting valuedescribing the set of users
  with permission to move messages from one topic to another within a channel
  in the organization.
- PATCH /realm,GET /events: Removededit_topic_policyproperty, as the permission to move messages between
  topics in the organization is now controlled bycan_move_messages_between_topics_groupsetting.

```
GET /events
```

```
POST /register
```

```
GET /events
```
Feature level 315
- POST /register,GET
  /streams/{stream_id},GET
  /events,GET
  /users/me/subscriptions: Theis_archivedproperty has been added to channel and subscription objects.
- GET /streams: The new parameterexclude_archivedcontrols whether archived channels should be
  returned.
- POST /register: The newarchived_channelsclient
  capabilityallows the client to specify whether it supports archived channels
  being present in the response.

```
GET
  /streams/{stream_id}
```

```
GET
  /events
```

```
GET /streams
```

```
POST /register
```
Feature level 314
- PATCH /realm,POST /register,GET /events: Anonymous groups are now accepted
  bycreate_multiuse_invite_grouprealm setting, which is a now agroup-setting valueinstead of an
  integer ID of the group.
- PATCH /realm,POST /register,GET /events: Anonymous groups are now accepted
  bycan_access_all_users_grouprealm setting, which is a now agroup-setting valueinstead of an
  integer ID of the group.

```
POST /register
```

```
GET /events
```

```
POST /register
```

```
GET /events
```
Feature level 313
- PATCH /users/{user_id}: Addednew_emailfield to
  allow updating the email address of the target user. The requester must be
  an organization administrator and have thecan_change_user_emailsspecial
  permission.
- PATCH /users/{email}: Added new endpoint,
  which is a copy ofPATCH /users/{user_id}, but the user
  is specified by their email address, following the same rules asGET
  /users/{email}.

```
PATCH /users/{user_id}
```

```
PATCH /users/{email}
```

```
PATCH /users/{user_id}
```

```
GET
  /users/{email}
```
Feature level 312
- GET /events: Addedrealm_export_consentevent
  type to allow realm administrators to view which users have
  consented to export their private data as part of a realm export.

```
GET /events
```
Feature level 311
- POST /user_groups/{user_group_id}/members:
  Addedadd_subgroupsanddelete_subgroupsparameters to support updating
  subgroups of a user group using this endpoint.
- POST /user_groups/create: Addedsubgroupsparameter to support setting subgroups of a user group during its creation.

```
POST /user_groups/{user_group_id}/members
```

```
POST /user_groups/create
```
Feature level 310
- PATCH /realm,GET /events,POST /register:
  Addedcan_move_messages_between_channels_grouprealm setting which is agroup-setting valuedescribing the set of users
  with permission to move messages from one channel to another in the organization.
- PATCH /realm,GET /events: Removedmove_messages_between_streams_policyproperty, as the permission to move
  messages between channels in the organization is now controlled bycan_move_messages_between_channels_groupsetting.

```
GET /events
```

```
POST /register
```

```
GET /events
```
Feature level 309
- Group-setting values: Starting with
  this feature level, it's now possible to use group-setting values in
  production for those settings whose value is not required to be a
  system group
Feature level 308
- POST /register,GET /events,GET /user_groups: Addcan_leave_groupto
  user group objects.
- POST /user_groups/create: Addedcan_leave_groupparameter to support setting the user group whose members can leave the user
  group.
- PATCH /user_groups/{user_group_id}: Addedcan_leave_groupparameter to support changing the user group whose
  members can leave the specified user group.

```
POST /register
```

```
GET /events
```

```
GET /user_groups
```

```
POST /user_groups/create
```

```
PATCH /user_groups/{user_group_id}
```
Feature level 307
- PATCH /realm,GET /events,POST /register:
  Addedcan_add_custom_emoji_grouprealm setting which is agroup-setting valuedescribing the set of users
  with permission to add custom emoji in the organization.
- PATCH /realm,GET /events: Removedadd_custom_emoji_policyproperty, as the permission to add custom emoji
  in the organization is now controlled bycan_add_custom_emoji_groupsetting.

```
GET /events
```

```
POST /register
```

```
GET /events
```
Feature level 306
- GET /events: Removed theextra_dataoptional
  field from therealm/updateevent format, which was only used forplan_typeevents, with a singleupload_quotafield. Now, we use
  a standardrealm/update_dictevent to notify clients about changes
  inplan_typeand other fields that atomically change with a given
  change in plan.
- GET /events: Addedmax_file_upload_size_mibfield to thedataobject inrealm/update_dictevent format;
  previously, this was a constant. Note that the field does not have arealm_prefix in thePOST /registerresponse.

```
GET /events
```

```
GET /events
```

```
POST /register
```
Feature level 305
- POST /register,GET /events,GET /user_groups: Addcan_add_members_groupto
  user group objects.
- POST /user_groups/create: Addedcan_add_members_groupparameter to support setting the user group which can add members to the user
  group.
- PATCH /user_groups/{user_group_id}: Addedcan_add_members_groupparameter to support changing the user group which
  can add members to the specified user group.
- Thecan_manage_all_groupspermission now has the natural semantics
  of applying to all groups, regardless of the role of the user given
  this permission. Since its introduction in feature level 299,can_manage_all_groupshad temporarily had unusual semantics
  matching those of the originaluser_group_edit_policysetting.

```
POST /register
```

```
GET /events
```

```
GET /user_groups
```

```
POST /user_groups/create
```

```
PATCH /user_groups/{user_group_id}
```
Feature level 304
- GET /export/realm,GET /events: Addedexport_typefield
  to the dictionaries inexportsarray. It indicates whether
  the export is of public data or full data with user consent
  (standard export).
- POST /export/realm: Addedexport_typeparameter to add support for admins to decide whether to create a
  public or a standard data export.

```
GET /export/realm
```

```
GET /events
```

```
POST /export/realm
```
Feature level 303
- POST /register,GET /user_groups,GET /user_groups/{user_group_id}/members/{user_id},GET /user_groups/{user_group_id}/members:
  Deactivated users are no longer returned as members of the user groups
  that they were members of prior to deactivation.
- POST /register: Settings, represented asgroup-setting value, will never include
  deactivated users in thedirect_memberslist for settings whose
  value is an anonymous group.
- POST /user_groups/{user_group_id}/members:
  Deactivated users cannot be added or removed from a user group; they
  are now implicitly not members of any groups while deactivated.
- GET /events: User reactivation event is not sent
  to users who cannot access the reactivated user anymore due to acan_access_all_users_grouppolicy.
- GET /events: The server will now senduser_groupevents with theadd_members/remove_membersoperations as appropriate when deactivating or reactivating a user,
  to ensure client state correctly reflects groups never containing
  deactivated users.
- GET /events: To ensure thatgroup-setting
  valuesare correct,realm/update_dictanduser_group/updateevents may now be by sent by the server when
  processing a deactivation/reactivation of a user, to ensure client
  state correctly reflects the state, given that deactivated users
  cannot have permissions in an organization.

```
POST /register
```

```
GET /user_groups
```

```
GET /user_groups/{user_group_id}/members/{user_id}
```

```
GET /user_groups/{user_group_id}/members
```

```
POST /register
```

```
POST /user_groups/{user_group_id}/members
```

```
GET /events
```

```
GET /events
```

```
GET /events
```
Feature level 302
- GET /users/{email}: Changed theemailvalues by which users can successfully be looked up to match the
  user email visibility setting's semantics better.

```
GET /users/{email}
```
Feature level 301
- POST /register,GET /events,GET /user_groups: Addcan_join_groupto
  user group objects.
- POST /user_groups/create: Addedcan_join_groupparameter to support setting the user group whose members can join the user
  group.
- PATCH /user_groups/{user_group_id}: Addedcan_join_groupparameter to support changing the user group whose
  members can join the specified user group.

```
POST /register
```

```
GET /events
```

```
GET /user_groups
```

```
POST /user_groups/create
```

```
PATCH /user_groups/{user_group_id}
```
Feature level 300
- GET /messages: Added a new message_ids parameter,
  as an alternative method of specifying which messages to fetch.

```
GET /messages
```
Feature level 299
- PATCH /realm,POST /register,GET /events: Addedcan_create_groupsrealm setting, which is agroup-setting valuedescribing the set of users with permission to create user groups.
- PATCH /realm,POST /register,GET /events: Addedcan_manage_all_groupsrealm setting, which is agroup-setting valuedescribing the set of users with permission to manage all user groups.
- PATCH /realm,GET /events: Removeduser_group_edit_policyproperty, as the permission to create user
  groups is now controlled bycan_create_groupssetting and permission to
  manage groups in now controlled bycan_manage_all_groupssetting.
- POST /register:user_group_edit_policyfield is deprecated, having been replaced bycan_create_groupsfor user
  group creation andcan_manage_all_groupsfor user group management.

```
POST /register
```

```
GET /events
```

```
POST /register
```

```
GET /events
```

```
GET /events
```

```
POST /register
```
Feature level 298
- POST /user_groups/{user_group_id}/deactivate:
  Server now returns a specific error response ("code": CANNOT_DEACTIVATE_GROUP_IN_USE)
  when a user group cannot be deactivated because it is in use. The
  error response contains details about where the user group is being used.

```
POST /user_groups/{user_group_id}/deactivate
```
Feature level 297
- GET /events,POST /register:
  An event withtype: "saved_snippet"is sent to the current user when a
  saved snippet is created or deleted.
- GET /saved_snippets: Added a new endpoint for
  fetching saved snippets of the user.
- POST /saved_snippets: Added a new endpoint for
  creating a new saved snippet.
- DELETE /saved_snippets/{saved_snippet_id}: Added
  a new endpoint for deleting saved snippets.

```
GET /events
```

```
POST /register
```

```
GET /saved_snippets
```

```
POST /saved_snippets
```

```
DELETE /saved_snippets/{saved_snippet_id}
```
Feature level 296
- POST /register,GET /events,POST /realm/profile_fields,GET /realm/profile_fields: Added a new
  parametereditable_by_userto custom profile field objects, which indicates whether
  regular users can edit the value of the profile field on their own account.

```
POST /register
```

```
GET /events
```

```
POST /realm/profile_fields
```

```
GET /realm/profile_fields
```
Feature level 295
- GET /export/realm/consents: Added
  a new endpoint to fetch theconsents of usersfor their private data exports.
- /api/v1/tusis an endpoint implementing thetusprotocolfor resumable uploads.
  Clients which send authenticated credentials (either via browser-based
  cookies, or API key viaAuthorizationheader) may use this endpoint to
  create uploads, similar toPOST /user_uploads.

```
GET /export/realm/consents
```

```
POST /user_uploads
```
Feature level 294
- POST /register: Clients that do not
  support theinclude_deactivated_groupsclient capabilitydo not receive deactivated user groups in the response.
- GET /events: Clients that do not support theinclude_deactivated_groupsclient capabilityreceiveremoveevent on user group deactivation instead ofupdateevent.
- GET /events: Clients that do not support theinclude_deactivated_groupsclient capabilitydo not receiveupdateevent when name of a deactivated user group
  is updated.
- GET /user_groups: Renamedallow_deactivatedparameter toinclude_deactivated_groups.
- DELETE /user_groups/{user_group_id}: Removed support for user group
  deletion as we now support deactivating user groups.

```
POST /register
```

```
GET /events
```

```
GET /events
```

```
GET /user_groups
```
Feature level 293
- POST /register,PATCH /settings:
  Added a newallow_private_data_exportsetting to allow users to decide
  whether to let administrators export their private data.

```
POST /register
```

```
PATCH /settings
```
Feature level 292
- POST /register,GET
  /events,GET
  /user_groups: Addedcreator_idanddate_createdfields to user groups objects.

```
POST /register
```

```
GET
  /events
```

```
GET
  /user_groups
```
Feature level 291
- PATCH /realm,GET /events,POST /register:
  Addedcan_delete_own_message_grouprealm setting which is agroup-setting valuedescribing the set of users
  with permission to delete the messages that they have sent in the organization.
- PATCH /realm,GET /events: Removeddelete_own_message_policyproperty, as the permission to delete own messages
  is now controlled bycan_delete_own_message_groupsetting.

```
GET /events
```

```
POST /register
```

```
GET /events
```
Feature level 290
- POST /user_groups/{user_group_id}/deactivate:
  Added new API endpoint to deactivate a user group.
- POST /register,GET
  /user_groups: Addeddeactivatedfield in
  the user group objects to identify deactivated user groups.
- GET /events: When a user group is deactivated,
  auser_groupevent withop=updateis sent to clients.
- GET /user_groups: Added support for
  excluding deactivated user groups from the response.

```
POST /user_groups/{user_group_id}/deactivate
```

```
POST /register
```

```
GET
  /user_groups
```

```
GET /events
```

```
GET /user_groups
```
Feature level 289
- POST /users/{user_id}/subscription: In the response,
  users are identified by their numeric user ID rather than by their
  Zulip API email address.

```
POST /users/{user_id}/subscription
```
Feature level 288
- POST /register:
  A newpresence_history_limit_daysparameter can be given, instructing
  the server to only fetch presence data more recent than the given
  number of days ago.
- POST /users/me/presence:
  A newhistory_limit_daysparameter can be given, with the
  same meaning as in thepresence_history_limit_daysparameter ofPOST /registerabove.

```
POST /register
```

```
POST /users/me/presence
```

```
POST /register
```
Feature level 287
- Markdown message
  formatting: Addeddata-original-dimensionsattributes to placeholder images
  (image-loading-placeholder), containing the dimensions of the
  original image. This change was also backported to the Zulip 9.x
  series, at feature level 278.
Feature level 286
- POST /user_uploads: Addedfilenamefield to
  the response, which is closer to the original filename than the
  basename of theurlfield in the response.

```
POST /user_uploads
```
Feature level 285
- PATCH /messages/{message_id}: Addeddetached_uploadsto the response, indicating which uploaded files
  are now only accessible via message edit history.

```
PATCH /messages/{message_id}
```
Feature level 284
- GET /events,GET /messages,GET /messages/{message_id},outgoing webhook payloads:
  Removed theprev_rendered_content_versionfield from theedit_historyobject within message objects and theupdate_messageevent type as it
  is an internal server implementation detail not used by any client.

```
GET /events
```

```
GET /messages
```

```
GET /messages/{message_id}
```
Feature level 283
- GET /events,POST /register,GET /user_groups: Addcan_manage_groupto
  user group objects.
- POST /user_groups/create: Addedcan_manage_groupparameter to support setting the user group whose members can manage the user
  group.
- PATCH /user_groups/{user_group_id}: Addedcan_manage_groupparameter to support changing the user group whose
  members can manage the specified user group.

```
GET /events
```

```
POST /register
```

```
GET /user_groups
```

```
POST /user_groups/create
```

```
PATCH /user_groups/{user_group_id}
```
Feature level 282
- POST users/me/tutorial_status: Removed this undocumented endpoint,
  as the state that it maintained has been replaced by a cleaneronboarding_stepsimplementation.
Feature level 281
- GET /events,POST /register:
  Added a new realm settingrealm_can_delete_any_message_groupwhich is agroup-setting valuedescribing the set of
  users with permission to delete any message in the organization.

```
GET /events
```

```
POST /register
```
Feature level 280
- PATCH /realm,POST /register,GET /events: Addedcan_create_web_public_channel_grouprealm setting, which is agroup-setting valuedescribing the set of users with permission to create web-public channels.
- PATCH /realm,GET /events: Removedcreate_web_public_stream_policyproperty, as the permission to create
  web-public channels is now controlled bycan_create_web_public_channel_groupsetting.
- POST /register:realm_create_web_public_stream_policyfield is deprecated, having been replaced bycan_create_web_public_channel_group.
  Notably, this backwards-compatiblerealm_create_web_public_stream_policyvalue
  now contains the superset of the true value that best approximates the actual
  permission setting.

```
POST /register
```

```
GET /events
```

```
GET /events
```

```
POST /register
```
Feature level 279 is reserved for future use in 9.x maintenance
releases.

## Changes in Zulip 9.2
Feature level 278
- Markdown message
  formatting: Addeddata-original-dimensionsattributes to placeholder images
  (image-loading-placeholder), containing the dimensions of the
  original image. Backported change from feature level 287.

## Changes in Zulip 9.0
Feature level 277
No changes; feature level used for Zulip 9.0 release.
Feature level 276
- Markdown message formatting:
  Image preview elements not contain adata-original-dimensionsattribute containing the dimensions of the original image.
Feature level 275
- POST /register,PATCH
  /settings,PATCH
  /realm/user_settings_defaults:
  Added newweb_animate_image_previewssetting, which controls how
  animated images should be played in the web/desktop app message feed.

```
POST /register
```

```
PATCH
  /settings
```

```
PATCH
  /realm/user_settings_defaults
```
Feature level 274
- GET /events:delete_messageevents are now
  always sent to the user who deletes the message, even if the message
  was in a channel that the user was not subscribed to.

```
GET /events
```
Feature level 273
- POST /register: Addedserver_thumbnail_formatsdescribing what formats the server will thumbnail images into.

```
POST /register
```
Feature level 272
- POST /user_uploads:uriwas renamed
  tourl, but remains available as a deprecated alias for
  backwards-compatibility.

```
POST /user_uploads
```
Feature level 271
- GET /messages,GET /messages/matches_narrow,POST /messages/flags/narrow,POST /register:
  Added support for a newsearch/narrow filteroperator,with, which uses a message ID for its operand. It returns
  messages in the same conversation as the message with the specified
  ID, and is designed to be used for creating permanent links to topics
  that continue to work when a topic is moved or resolved.

```
GET /messages
```

```
GET /messages/matches_narrow
```

```
POST /messages/flags/narrow
```

```
POST /register
```
Feature level 270
- PATCH /realm,POST /register,GET /events: Added two new realm settings,direct_message_initiator_group, which is agroup-setting valuedescribing the
  set of users with permission to initiate direct message thread, anddirect_message_permission_group, which is agroup-setting valuedescribing the
  set of users of which at least one member must be included as sender
  or recipient in all personal and group direct messages.
  Removedprivate_message_policyproperty, as the permission to send
  direct messages is now controlled bydirect_message_initiator_groupanddirect_message_permission_groupsettings.

```
POST /register
```

```
GET /events
```
Feature level 269
- POST /register,PATCH
  /settings,PATCH
  /realm/user_settings_defaults:
  Added new user settingweb_channel_default_view, controlling the
  behavior of clicking a channel link in the web/desktop apps.

```
POST /register
```

```
PATCH
  /settings
```

```
PATCH
  /realm/user_settings_defaults
```
Feature level 268
- PATCH /realm/user_settings_defaults,POST /register,PATCH /settings:
  Added a newweb_navigate_to_sent_messagesetting to allow users to decide
  whether to automatically go to conversation where they sent a message.

```
PATCH /realm/user_settings_defaults
```

```
POST /register
```

```
PATCH /settings
```
Feature level 267
- GET /invites,POST /invites: Addednotify_referrer_on_joinparameter, indicating whether the referrer has opted
  to receive a direct message from the notification bot whenever a user joins
  via this invitation.

```
GET /invites
```

```
POST /invites
```
Feature level 266
- PATCH /realm,POST /register,GET /events: Addedcan_create_private_channel_grouprealm setting, which is agroup-setting valuedescribing the set of users with permission to create private channels.
- PATCH /realm,GET /events: Removedcreate_private_stream_policyproperty, as the permission to create private
  channels is now controlled bycan_create_private_channel_groupsetting.
- POST /register:realm_create_private_stream_policyfield is deprecated, having been replaced bycan_create_private_channel_group.
  Notably, this backwards-compatiblerealm_create_private_stream_policyvalue
  now contains the superset of the true value that best approximates the actual
  permission setting.

```
POST /register
```

```
GET /events
```

```
GET /events
```

```
POST /register
```
Feature level 265
- GET /messages,GET /messages/matches_narrow,POST /messages/flags/narrow,POST /register:
  Added a newsearch/narrow filter,is:followed, matching messages in topics that the current user isfollowing.

```
GET /messages
```

```
GET /messages/matches_narrow
```

```
POST /messages/flags/narrow
```

```
POST /register
```
Feature level 264
- PATCH /realm,POST /register,GET /events: Addedcan_create_public_channel_grouprealm setting, which is agroup-setting valuedescribing the set of users with permission to create channels.
- PATCH /realm,GET /events: Removedcreate_public_stream_policyproperty, as the permission to create public
  channels is now controlled bycan_create_public_channel_groupsetting.
- POST /register:realm_create_public_stream_policyfield is deprecated, having been replaced bycan_create_public_channel_group.
  Notably, this backwards-compatiblerealm_create_public_stream_policyvalue
  now contains the superset of the true value that best approximates the actual
  permission setting.

```
POST /register
```

```
GET /events
```

```
GET /events
```

```
POST /register
```
Feature level 263
- POST /users/me/presence:
  A newlast_update_idparameter can be given, instructing
  the server to only fetch presence data withlast_update_idgreater than the value provided. The server also provides
  apresence_last_update_idfield in the response, which
  tells the client the greatestlast_update_idof the fetched
  presence data. This can then be used as the value in the
  aforementioned parameter to avoid re-fetching of already known
  data when polling the endpoint next time.
  Additionally, the client specifying thelast_update_idimplies it uses the modern API format, soslim_presence=truewill be assumed by the server.
- POST /register: The response now also
  includes apresence_last_update_idfield, with the same
  meaning as described above for/users/me/presence.
  In the same way, the retrieved value can be passed when
  querying/users/me/presenceto avoid
  re-fetching of already known data.

```
POST /users/me/presence
```

```
POST /register
```

```
/users/me/presence
```

```
/users/me/presence
```
Feature level 262
- GET /users/{user_id}/status: Added a new
  endpoint to fetch an individual user's currently setstatus.

```
GET /users/{user_id}/status
```
Feature level 261
- POST /invites,POST /invites/multiuse: Addedinclude_realm_default_subscriptionsparameter to indicate whether
  the newly created user will be automatically subscribed todefault
  channelsin the
  organization. Previously, the default channel IDs needed to be included
  in thestream_idsparameter. This also allows a newly created user
  to be automatically subscribed to the default channels in an
  organization when the user creating the invitation does not generally
  have permission tosubscribe other users to
  channels.

```
POST /invites
```

```
POST /invites/multiuse
```
Feature level 260
- PATCH /user_groups/{user_group_id}:
  Updatingcan_mention_groupnow uses a race-resistant format where
  the client sends the expectedoldvalue and desirednewvalue.

```
PATCH /user_groups/{user_group_id}
```
Feature level 259
- POST /register,GET /events:
  For theonboarding_stepsevent type, an array of onboarding steps
  to be displayed to clients is sent. Onboarding step now has one-time
  notices as the only valid type. Prior to this, both hotspots and
  one-time notices were valid types of onboarding steps. There is no compatibility
  support, as we expect that only official Zulip clients will interact with
  this data. Currently, no client other than the Zulip web app uses this.

```
POST /register
```

```
GET /events
```
Feature level 258
- GET /user_groups,POST
  /register:can_mention_groupfield can now
  either be an ID of a named user group with the permission, or an
  object describing the set of users and groups with the permission.
- POST /user_groups/create,PATCH
  /user_groups/{user_group_id}: Thecan_mention_groupparameter can now either be an ID of a named
  user group or an object describing a set of users and groups.

```
GET /user_groups
```

```
POST
  /register
```

```
POST /user_groups/create
```

```
PATCH
  /user_groups/{user_group_id}
```
Feature level 257
- POST /register,POST /server_settings,PATCH /realm:realm_uriwas renamed torealm_url, but remains available as a
  deprecated alias for backwards-compatibility.
- Mobile push notification payloads, similarly, have a newrealm_url,
  replacingrealm_uri, which remains available as a deprecated alias
  for backwards-compatibility.

```
POST /register
```

```
POST /server_settings
```
Feature level 256
- POST /streams/{stream_id}/delete_topic,GET /events: When messages are deleted, astreamop:updateevent with
  an updated value forfirst_message_idmay now be sent to clients.

```
POST /streams/{stream_id}/delete_topic
```

```
GET /events
```
Feature level 255
- "Stream" was renamed to "Channel" across strings in the Zulip API
  and UI. Clients supporting a range of server versions are encouraged
  to use different strings based on the server's API feature level for
  consistency. Note that feature level marks the strings transition
  only: Actual API changes related to this transition have their own
  API changelog entries.
Feature level 254
- POST /register,GET /events,GET /streams,GET /streams/{stream_id},GET /users/me/subscriptions: Added a new
  fieldcreator_idto stream and subscription objects, which contains the
  user ID of the stream's creator.

```
POST /register
```

```
GET /events
```

```
GET /streams
```

```
GET /streams/{stream_id}
```

```
GET /users/me/subscriptions
```
Feature level 253
- PATCH /realm/user_settings_defaults,POST /register,PATCH /settings:
  Added newreceives_typing_notificationsoption to allow users to decide whether
  to receive typing notification events from other users.

```
PATCH /realm/user_settings_defaults
```

```
POST /register
```

```
PATCH /settings
```
Feature level 252
- PATCH /realm/profile_fields/{field_id}:name,hint,display_in_profile_summary,requiredandfield_datafields are now optional during an update. Previously we
  required the clients to populate the fields in the PATCH request even if there was
  no change to those fields' values.
Feature level 251
- POST /register: Fixedrealm_upload_quota_mibvalue to actually be in MiB. Until now the value was in bytes.

```
POST /register
```
Feature level 250
- GET /messages,GET /messages/matches_narrow,POST /messages/flags/narrow,POST /register:
  Added support for twosearch/narrow filtersrelated to stream messages:channelandchannels. Thechanneloperator is an alias for thestreamoperator. Thechannelsoperator is an alias for thestreamsoperator.

```
GET /messages
```

```
GET /messages/matches_narrow
```

```
POST /messages/flags/narrow
```

```
POST /register
```
Feature level 249
- GET /messages,GET /messages/matches_narrow,POST /messages/flags/narrow,POST /register:
  Added support for a newsearch/narrow filter,has:reaction, which returns messages with at least oneemoji
  reaction.

```
GET /messages
```

```
GET /messages/matches_narrow
```

```
POST /messages/flags/narrow
```

```
POST /register
```
Feature level 248
- POST /typing,POST /messages,POST /scheduled_messages,PATCH /scheduled_messages/<int:scheduled_message_id>:
  Added"channel"as an additional value for thetypeparameter to
  indicate a stream message.

```
POST /typing
```

```
POST /messages
```

```
POST /scheduled_messages
```

```
PATCH /scheduled_messages/<int:scheduled_message_id>
```
Feature level 247
- Markdown message formatting:
  Addedchannelto the supported options forwildcard
  mentions.
Feature level 246
- POST /register,POST
  /events: Added newrequire_unique_namessetting
  controlling whether users names can duplicate others.

```
POST /register
```

```
POST
  /events
```
Feature level 245
- PATCH
  /realm/user_settings_defaultsPOST /register,GET
  /events,PATCH
  /settings: Added newweb_font_size_pxandweb_line_height_percentsettings to allow users to control the
  styling of the web application.

```
PATCH
  /realm/user_settings_defaults
```

```
POST /register
```

```
GET
  /events
```

```
PATCH
  /settings
```
Feature level 244
- POST /register,GET /events,POST /realm/profile_fields,GET /realm/profile_fields: Added a new
  parameterrequired, on custom profile field objects, indicating whether an
  organization administrator has configured the field as something users should
  be required to provide.

```
POST /register
```

```
GET /events
```

```
POST /realm/profile_fields
```

```
GET /realm/profile_fields
```
Feature level 243
- POST /register,GET
  /events: Changed the format ofrealm_authentication_methodsandauthentication_methods,
  respectively, to use a dictionary rather than a boolean as the value
  for each authentication method. The new dictionaries are more
  extensively and contain fields indicating whether the backend is
  unavailable to the current realm due to Zulip Cloud plan
  restrictions or any other reason.

```
POST /register
```

```
GET
  /events
```
Feature level 242
- POST /register,POST /events,PATCH /realm: Addedzulip_update_announcements_stream_idrealm setting,
  which is the ID of the of the stream to which automated messages announcing
  new features or other end-user updates about the Zulip software are sent.

```
POST /register
```

```
POST /events
```
Feature level 241
- POST /register,POST /events,PATCH /realm: Renamed the realm settingsnotifications_streamandsignup_notifications_streamtonew_stream_announcements_streamandsignup_announcements_stream, respectively.

```
POST /register
```

```
POST /events
```
Feature level 240
- GET /events: Therestartevent no longer contains an
  optionalimmediateflag.
- GET /events: A newweb_reload_clientevent has been
  added; it is used to signal to website-based clients that they should reload
  their code.  This was previously implied by therestartevent.

```
GET /events
```

```
GET /events
```
Feature levels 238-239 are reserved for future use in 8.x maintenance
releases.

## Changes in Zulip 8.0
Feature level 237
No changes; feature level used for Zulip 8.0 release.
Feature level 236
- POST /messages,POST
  /scheduled_messages: The newread_by_senderparameter lets the client override the heuristic
  that determines whether the new message will be initially marked
  read by its sender.

```
POST /messages
```

```
POST
  /scheduled_messages
```
Feature level 235
- PATCH /realm/user_settings_defaults,POST /register,PATCH /settings:
  Added a new user setting,automatically_follow_topics_where_mentioned,
  that allows the user to automatically follow topics where the user is mentioned.

```
PATCH /realm/user_settings_defaults
```

```
POST /register
```

```
PATCH /settings
```
Feature level 234
- Mobile push notifications now include arealm_namefield.
- POST /mobile_push/test_notificationnow sends
  a test notification withtestrather thantest-by-device-tokenin theeventfield.

```
POST /mobile_push/test_notification
```
Feature level 233
- POST /register,GET /events:
  Renamed thehotspotsevent type and the relatedhotspotsobject array
  toonboarding_steps. These are sent to clients if there are onboarding
  steps to display to the user. Onboarding steps now include
  both hotspots and one-time notices. Prior to this, hotspots were the only
  type of onboarding step. Also, added atypefield to the objects
  returned in the renamedonboarding_stepsarray to distinguish between
  the two types of onboarding steps.
- POST /users/me/onboarding_steps: Added a new endpoint, which
  deprecates the/users/me/hotspotsendpoint, in order to support
  displaying both one-time notices (which highlight new features for
  existing users) and hotspots (which are used in new user tutorials).
  This endpoint marks both types of onboarding steps, i.e.hotspotandone_time_notice, as read by the user. There is no compatibility
  support for/users/me/hotspotsas no client other than the Zulip
  web app used the endpoint prior to these changes.

```
POST /register
```

```
GET /events
```
Feature level 232
- POST /register: Added a newuser_list_incompleteclient
  capabilitycontrolling whetherrealm_userscontains "Unknown user"
  placeholder objects for users that the current user cannot access
  due to acan_access_all_users_grouppolicy.
- GET /events: The newuser_list_incompleteclient
  capabilitycontrols whether to sendrealm_userevents withop: "add"containing "Unknown user" placeholder objects to clients when a new
  user is created that the client does not have access to due to acan_access_all_users_grouppolicy.

```
POST /register
```

```
GET /events
```
Feature level 231
- POST /register:realm_push_notifications_enablednow represents more accurately
  whether push notifications are actually enabled via the mobile push
  notifications service. Addedrealm_push_notifications_enabled_end_timestampfield to realm
  data.
- GET /events: Arealmupdate event is now sent
  wheneverpush_notifications_enabledorpush_notifications_enabled_end_timestampchanges.

```
POST /register
```

```
GET /events
```
Feature level 230
- POST /register,GET /events:
  Addedhas_triggerfield to objects returned in thehotspotsarray to
  identify if the hotspot will activate only when some specific event
  occurs.

```
POST /register
```

```
GET /events
```
Feature level 229
- PATCH /messages/{message_id},POST
  /messages: Topic wildcard mentions involving
  large numbers of participants are now restricted bywildcard_mention_policy. The server now uses theSTREAM_WILDCARD_MENTION_NOT_ALLOWEDandTOPIC_WILDCARD_MENTION_NOT_ALLOWEDerror codes when a message is
  rejected because ofwildcard_mention_policy.

```
PATCH /messages/{message_id}
```

```
POST
  /messages
```
Feature level 228
- GET /events:realm_userevents withop: "update"are now only sent to users who can access the modified user.
- GET /events:presenceevents are now only sent to
  users who can access the user who comes back online if theCAN_ACCESS_ALL_USERS_GROUP_LIMITS_PRESENCEserver setting is set
  totrue.
- GET /events:user_statusevents are now only
  sent to users who can access the modified user.
- GET /realm/presence: The endpoint now returns
  presence information of accessible users only if theCAN_ACCESS_ALL_USERS_GROUP_LIMITS_PRESENCEserver setting is set
  totrue.
- GET /events:realm_userevents withop: "add"are now also sent when a guest user gains access to a user.
- GET /events:realm_userevents withop: "remove"are now also sent when a guest user loses access to a user.

```
GET /events
```

```
GET /events
```

```
GET /events
```

```
GET /realm/presence
```

```
GET /events
```

```
GET /events
```
Feature level 227
- PATCH /realm/user_settings_defaults,POST /register,PATCH /settings:
  AddedDMs, mentions, and followed topicsoption fordesktop_icon_count_displaysetting, and renumbered the options.
  The total unread count of DMs, mentions, and followed topics appears in
  desktop sidebar and browser tab when this option is configured.

```
PATCH /realm/user_settings_defaults
```

```
POST /register
```

```
PATCH /settings
```
Feature level 226
- POST /register,GET /events,GET /users/me/subscriptions: Removedemail_addressfield from subscription objects.
- GET /streams/{stream_id}/email_address:
  Added new endpoint to get email address of a stream.

```
POST /register
```

```
GET /events
```

```
GET /users/me/subscriptions
```

```
GET /streams/{stream_id}/email_address
```
Feature level 225
- PATCH /realm,POST /register,GET /events: Addedcan_access_all_users_group_idrealm setting, which is the ID of the user group whose members can
  access all the users in the organization.
- POST /register: Addedallowed_system_groupsfield to configuration data object of permission settings passed inserver_supported_permission_settings.

```
POST /register
```

```
GET /events
```

```
POST /register
```
Feature level 224
- GET /events,GET /messages,GET /messages/{message_id}: Of theavailable
  message flagsthat a user
  may have for a message, thewildcard_mentionedflag was
  deprecated in favor of thestream_wildcard_mentionedandtopic_wildcard_mentionedflags, but it is still available for
  backwards compatibility.

```
GET /events
```

```
GET /messages
```

```
GET /messages/{message_id}
```
Feature level 223
- POST /users/me/apns_device_token:
  Theappidparameter is now required.
  Previously it defaulted to the server settingZULIP_IOS_APP_ID,
  defaulting to "org.zulip.Zulip".
- POST /remotes/server/register: Theios_app_idparameter is now
  required whenkindis 1, i.e. when registering an APNs token.
  Previously it was ignored, and the push bouncer effectively
  assumed its value was the server settingAPNS_TOPIC,
  defaulting to "org.zulip.Zulip".

```
POST /users/me/apns_device_token
```
Feature level 222
- GET /events: When a user is deactivated or
  reactivated, the server usesrealm_userevents withop: "update"updating theis_activefield, instead ofrealm_userevents withop: "remove"andop: "add", respectively.
- GET /events: When a bot is deactivated or
  reactivated, the server sendsrealm_botevents withop: "update"updating theis_activefield, instead ofrealm_botevents withop: "remove"andop: "add", respectively.

```
GET /events
```

```
GET /events
```
Feature level 221
- POST /register: Addedserver_supported_permission_settingsfield in the response which contains configuration data for various permission
  settings.

```
POST /register
```
Feature level 220
- GET /events: Stream creation events for web-public
  streams are now sent to all guest users in the organization as well.
- GET /events: Thesubscriptionevents forop:
  "peer_add"andop: "peer_remove"are now sent to subscribed guest
  users for public streams and to all the guest users for web-public
  streams; previously, they incorrectly only received these for
  private streams.

```
GET /events
```

```
GET /events
```
Feature level 219
- PATCH /realm/user_settings_defaultsPOST /register,GET /events,PATCH /settings: Renameddefault_viewandescape_navigates_to_default_viewsettings toweb_home_viewandweb_escape_navigates_to_home_viewrespectively.
- POST /user_topics,POST
  register,GET /events:
  Added followed as a supported value for visibility policies inuser_topicobjects.

```
PATCH /realm/user_settings_defaults
```

```
POST /register
```

```
GET /events
```

```
PATCH /settings
```

```
POST /user_topics
```

```
POST
  register
```

```
GET /events
```
Feature level 218
- POST /messages: Added an optionalautomatic_new_visibility_policyenum field in the success response
  to indicate the new visibility policy value due to thevisibility policy settingsduring the send message action.

```
POST /messages
```
Feature level 217
- POST /mobile_push/test_notification: Added new endpoint
  to send a test push notification to a mobile device or devices.

```
POST /mobile_push/test_notification
```
Feature level 216
- PATCH /realm,POST register,GET /events: Addedenable_guest_user_indicatorsetting to control whether "(guest)" is added to user names in UI.

```
POST register
```

```
GET /events
```
Feature level 215
- GET /events: Replaced the valueprivatewithdirectin themessage_typefield for thetypingevents
  sent when a user starts or stops typing a message.
- POST /typing: Stopped supportingprivateas a valid value for thetypeparameter.
- POST /typing: Stopped using thetoparameter
  for the"stream"type. Previously, in the case of the"stream"type, it
  accepted a single-element list containing the ID of the stream. Added an
  optional parameter,stream_id. Now,tois used only for"direct"type.
  In the case of"stream"type,stream_idandtopicare used.
- Note that stream typing notifications were not enabled in any Zulip client
  prior to feature level 215.

```
GET /events
```

```
POST /typing
```

```
POST /typing
```
Feature level 214
- PATCH /realm/user_settings_defaults,POST /register,PATCH /settings:
  Added two new user settings,automatically_follow_topics_policyandautomatically_unmute_topics_in_muted_streams_policy. The settings control the
  user's preference on which topics the user will automatically 'follow' and
  'unmute in muted streams' respectively.

```
PATCH /realm/user_settings_defaults
```

```
POST /register
```

```
PATCH /settings
```
Feature level 213
- POST /register: Fixed incorrect handling of
  unmuted and followed topics in calculating thementionsandcountfields of theunread_msgsobject.

```
POST /register
```
Feature level 212
- GET /events,POST /register,PATCH /realm: Added thejitsi_server_urlfield to therealmobject,
  allowing organizations to set a custom Jitsi Meet server. Previously, this
  was only available as a server-level configuration.
- POST /register: Addedserver_jitsi_server_urlfields to therealmobject. The existingjitsi_server_urlwill now be
  calculated asrealm_jitsi_server_url || server_jitsi_server_url.

```
GET /events
```

```
POST /register
```

```
POST /register
```
Feature level 211
- POST /streams/{stream_id}/delete_topic,POST /mark_all_as_read:
  Added acompleteboolean field in the success response to indicate
  whether all or only some of the targeted messages were processed.
  This replaces the use of"result": "partially_completed"(introduced
  in feature levels 154 and 153), so that these endpoints now send aresultstring of either"success"or"error", like the rest of
  the Zulip API.

```
POST /streams/{stream_id}/delete_topic
```

```
POST /mark_all_as_read
```
Feature level 210
- POST /register,PATCH /settings,PATCH /realm/user_settings_defaults:
  Added newweb_stream_unreads_count_display_policydisplay setting, which controls in
  which streams (all/unmuted/none) unread messages count shows up
  in left sidebar.

```
POST /register
```

```
PATCH /settings
```

```
PATCH /realm/user_settings_defaults
```
Feature level 209
- PATCH /realm,POST /register,GET /events: Addedcreate_multiuse_invite_grouprealm setting, which is the ID of the user group whose members can
  createreusable invitation linksto an organization. Previously, only admin users could create these
  links.
- POST /invites/multiuse: Non-admin users can
  now use this endpoint to create reusable invitation links. Previously,
  this endpoint was restricted to admin users only.
- GET /invites: Endpoint response for non-admin users now
  includes both email invitations and reusable invitation links that they have
  created. Previously, non-admin users could only create email invitations, and
  therefore the response did not include reusable invitation links for these
  users.
- DELETE /invites/multiuse/{invite_id}: Non-admin
  users can now revoke reusable invitation links they have created. Previously,
  only admin users could create and revoke reusable invitation links.
- GET /events: When the set of invitations in an
  organization changes, aninvites_changedevent is now sent to the
  creator of the changed invitation, as well as all admin users.
  Previously, this event was only sent to admin users.

```
POST /register
```

```
GET /events
```

```
POST /invites/multiuse
```

```
GET /invites
```

```
DELETE /invites/multiuse/{invite_id}
```

```
GET /events
```
Feature level 208
- POST /users/me/subscriptions,DELETE /users/me/subscriptions: These endpoints
  now return an HTTP status code of 400 withcode: "BAD_REQUEST"in
  the error response when a user specified in theprincipalsparameter
  is deactivated or does not exist. Previously, these endpoints returned
  an HTTP status code of 403 withcode: "UNAUTHORIZED_PRINCIPAL"in the
  error response for these cases.

```
POST /users/me/subscriptions
```

```
DELETE /users/me/subscriptions
```
Feature level 207
- POST /register: Addeddisplay_nameandall_event_typesfields to therealm_incoming_webhook_botsobject.

```
POST /register
```
Feature level 206
- POST /calls/zoom/create: Addedis_video_callparameter
  controlling whether to request a Zoom meeting that defaults to
  having video enabled.
Feature level 205
- POST /register:streamsfield in the response
  now includesweb-public streamsas well.
- GET /events: Events for stream creation and deletion
  are now sent to clients when a user gains or loses access to any streams
  due to a change in theirrole.
- GET /events: Thesubscriptionevents forop:
  "peer_add"are now sent to clients when a user gains access to a stream
  due to a change in their role.

```
POST /register
```

```
GET /events
```

```
GET /events
```
Feature level 204
- POST /register: Addedserver_typing_started_wait_period_milliseconds,server_typing_stopped_wait_period_milliseconds, andserver_typing_started_expiry_period_millisecondsfields
  for clients to use when implementingtyping
  notificationsprotocol.

```
POST /register
```
Feature level 203
- POST /register: Addrealm_date_createdfield to realm data.

```
POST /register
```
Feature level 202
- PATCH /realm/linkifiers: Added new endpoint
  to support changing the order in which linkifiers will be processed.

```
PATCH /realm/linkifiers
```
Feature level 201
- POST /zulip-outgoing-webhook: Renamed the notification triggerprivate_messagetodirect_message.
Feature level 200
- PATCH /streams/{stream_id}: Addedis_default_streamparameter to change whether the stream is a
  default stream for new users in the organization.
- POST /users/me/subscriptions: Addedis_default_streamparameter which determines whether any streams
  created by this request will be default streams for new users.

```
PATCH /streams/{stream_id}
```

```
POST /users/me/subscriptions
```
Feature level 199
- POST /register,GET /events,GET /streams,GET /streams/{stream_id}: Stream objects now
  include astream_weekly_trafficfield indicating the stream's level of
  traffic.

```
POST /register
```

```
GET /events
```

```
GET /streams
```

```
GET /streams/{stream_id}
```
Feature level 198
- GET /events,POST /register,GET /user_groups,POST /user_groups/create,PATCH /user_groups/{user_group_id}:Renamed
  group settingcan_mention_group_idtocan_mention_group.

```
GET /events
```

```
POST /register
```

```
GET /user_groups
```

```
POST /user_groups/create
```

```
PATCH /user_groups/{user_group_id}
```
Feature level 197
- POST /users/me/subscriptions,PATCH /streams/{stream_id},GET /users/me/subscriptions,GET /streams,POST /register,GET /events: Renamed
  stream settingcan_remove_subscribers_group_idtocan_remove_subscribers_group.

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
POST /register
```

```
GET /events
```
Feature level 196
- POST /realm/playgrounds:url_prefixis
  replaced byurl_template, which only acceptsRFC 6570compliant
  URL templates. The old prefix format is no longer supported.
- GET /events,POST /register:url_prefixis replaced byurl_templateinrealm_playgroundsevents.

```
POST /realm/playgrounds
```

```
GET /events
```

```
POST /register
```
Feature level 195
- GET /events,POST /register:
  Thedefault_code_block_languagerealm setting is now consistently an
  empty string when no default pygments language code is set. Previously,
  the server had a bug that meant it might represent no default for this
  realm setting as eithernullor an empty string. Clients supporting
  older server versions should treat either value (nullor"") as no
  default being set.

```
GET /events
```

```
POST /register
```
Feature level 194
- GET /messages,GET /messages/matches_narrow,POST /messages/flags/narrow,POST /register:
  Forsearch/narrow filterswith theidoperator, added support for encoding the message ID operand as either
  a string or an integer. Previously, only string encoding was supported.

```
GET /messages
```

```
GET /messages/matches_narrow
```

```
POST /messages/flags/narrow
```

```
POST /register
```
Feature level 193
- POST /messages/{message_id}/reactions,DELETE /messages/{message_id}/reactions:
  Endpoints return specific error responses if an emoji reaction
  already exists when adding a reaction ("code": "REACTION_ALREADY_EXISTS")
  or if an emoji reaction does not exist when deleting a reaction
  ("code": "REACTION_DOES_NOT_EXIST"). Previously, these errors
  returned the"BAD_REQUEST"code.

```
POST /messages/{message_id}/reactions
```

```
DELETE /messages/{message_id}/reactions
```
Feature level 192
- GET /events: Stream creation events are now
  sent when guest users gain access to a public stream by being
  subscribed. Guest users previously only received these events when
  subscribed to private streams.

```
GET /events
```
Feature level 191
- GET /events,POST /register,GET /user_groups: Addcan_mention_group_idto
  user group objects.
- POST /user_groups/create: Addedcan_mention_group_idparameter to support setting the user group whose members can mention the new user
  group.
- PATCH /user_groups/{user_group_id}: Addedcan_mention_group_idparameter to support changing the user group whose
  members can mention the specified user group.

```
GET /events
```

```
POST /register
```

```
GET /user_groups
```

```
POST /user_groups/create
```

```
PATCH /user_groups/{user_group_id}
```
Feature level 190
- DELETE /realm/emoji/{emoji_name}: This endpoint
  now returns an HTTP status code of 404 when an emoji does not exist, instead of 400.

```
DELETE /realm/emoji/{emoji_name}
```
Feature level 189
- PATCH /realm/user_settings_defaults,POST /register,PATCH /settings:
  Added new boolean user settingsenable_followed_topic_email_notifications,enable_followed_topic_push_notifications,enable_followed_topic_wildcard_mentions_notify,enable_followed_topic_desktop_notificationsandenable_followed_topic_audible_notificationsto control whether a user
  receives email, push, wildcard mention, visual desktop and audible desktop
  notifications, respectively, for messages sent to followed topics.

```
PATCH /realm/user_settings_defaults
```

```
POST /register
```

```
PATCH /settings
```
Feature level 188
- POST /users/me/muted_users/{muted_user_id},DELETE /users/me/muted_users/{muted_user_id}:
  Added support to mute/unmute bot users.

```
POST /users/me/muted_users/{muted_user_id}
```

```
DELETE /users/me/muted_users/{muted_user_id}
```
Feature levels 186-187 are reserved for future use in 7.x maintenance
releases.

## Changes in Zulip 7.0
Feature level 185
No changes; feature level used for Zulip 7.0 release.
Feature level 184
- PATCH /scheduled_messages/<int:scheduled_message_id>:
  Added new endpoint for editing an existing scheduled message.
- POST /scheduled_messages:
  Removed optionalscheduled_message_idparameter, which had
  been a previous way for clients to support editing an existing
  scheduled message.

```
PATCH /scheduled_messages/<int:scheduled_message_id>
```

```
POST /scheduled_messages
```
Feature level 183
- POST /register: Removed therealm_community_topic_editing_limit_secondsproperty, which was no
  longer in use. The time limit for editing topics is controlled by the
  realm settingmove_messages_within_stream_limit_seconds, see feature
  level 162.
- GET /events: Removed thecommunity_topic_editing_limit_secondsproperty from realmupdate_dictevent documentation, because it was
  never returned as a changed property in this event and was only ever
  returned in thePOST /registerresponse.

```
POST /register
```

```
GET /events
```

```
POST /register
```
Feature level 182
- POST /export/realm: This endpoint now returns the ID
  of the data export object created by the request.

```
POST /export/realm
```
Feature level 181
- GET /scheduled_messages,GET
  /events,POST /register:
  Addedfailedboolean field to scheduled message objects to
  indicate if the server tried to send the scheduled message and was
  unsuccessful. Clients that support unscheduling and editing
  scheduled messages should use this field to indicate to the user
  when a scheduled message failed to send at the appointed time.

```
GET /scheduled_messages
```

```
GET
  /events
```

```
POST /register
```
Feature level 180
- POST /invites: Added support for invitations specifying
  the empty list as the user's initial stream subscriptions. Previously, this
  returned an error. This change was also backported to Zulip 6.2, and
  is available at feature levels 157-158 as well.

```
POST /invites
```
Feature level 179
- POST /scheduled_messages:
  Added new endpoint to create and edit scheduled messages.
- GET /events:
  Addedscheduled_messagesevents sent to clients when a user creates,
  edits or deletes scheduled messages.
- POST /register:
  Added an optionalscheduled_messagesfield to that includes all
  of the undelivered scheduled messages for the current user.

```
POST /scheduled_messages
```

```
GET /events
```

```
POST /register
```
Feature level 178
- POST /users/me/presence,GET /users/<user_id_or_email>/presence,GET /realm/presence,POST /register,GET /events:
  The server no longer stores which client submitted presence data,
  and presence responses from the server will always contain the"aggregated"and"website"keys.

```
POST /users/me/presence
```

```
GET /users/<user_id_or_email>/presence
```

```
GET /realm/presence
```

```
POST /register
```

```
GET /events
```
Feature level 177
- GET /messages,GET /messages/matches_narrow,POST /messages/flags/narrow,POST /register:
  Added support for threesearch/narrow filtersrelated to direct messages:is:dm,dmanddm-including.
  Thedmoperator replaces and deprecates thepm-withoperator.
  Theis:dmfilter replaces and deprecates theis:privatefilter.
  Thedm-includingoperator replaces and deprecates thegroup-pm-withoperator. Because existing Zulip messages may have links with these
  legacy filters, they are still supported for backwards-compatibility.

```
GET /messages
```

```
GET /messages/matches_narrow
```

```
POST /messages/flags/narrow
```

```
POST /register
```
Feature level 176
- POST /realm/filters,PATCH /realm/filters/<int:filter_id>:
  Theurl_format_stringparameter is replaced byurl_template.Linkifiersnow only acceptRFC 6570compliant URL templates. The old URL format
  strings are no longer supported.
- GET /events,POST /register:
  Theurl_format_stringkey inrealm_linkifiersobjects is replaced
  byurl_template. For backwards-compatibility, clients that do not
  support thelinkifier_url_templateclient capabilitywill receive an emptyrealm_linkifiersarray in the/registerresponse and not receiverealm_linkifiersevents. Unconditionally,
  the deprecatedrealm_filtersevent type returns an empty array in
  the/registerresponse and these events are no longer sent to
  clients.

```
POST /realm/filters
```

```
PATCH /realm/filters/<int:filter_id>
```

```
GET /events
```

```
POST /register
```
Feature level 175
- POST /register,PATCH /settings,PATCH /realm/user_settings_defaults:
  Added new user settingweb_mark_read_on_scroll_policy. Clients may use this to
  determine the user's preference on whether to mark messages as read or not when
  scrolling through their message feed.

```
POST /register
```

```
PATCH /settings
```

```
PATCH /realm/user_settings_defaults
```
Feature level 174
- POST /typing,POST /messages:
  Added"direct"as the preferred way to indicate a direct message for thetypeparameter, deprecating the original"private". While"private"is still supported for direct messages, clients are encouraged to use
  the modern convention with servers that support it, because support for"private"may eventually be removed.

```
POST /typing
```

```
POST /messages
```
Feature level 173
- GET /scheduled_messages,DELETE
  /scheduled_messages/<int:scheduled_message_id>:
  Added new endpoints to fetch and delete scheduled messages.

```
GET /scheduled_messages
```

```
DELETE
  /scheduled_messages/<int:scheduled_message_id>
```
Feature level 172
- PATCH /messages/{message_id}:Topic editing restrictionsnow apply
  to stream messages without a topic.
- PATCH /messages/{message_id}: When users, other
  than organization administrators and moderators, use"propagate_mode": "change_all"to move messages that have passed the
  organization's time limit for updating a message's topic and/or stream,
  this endpoint now returns an error response
  ("code": "MOVE_MESSAGES_TIME_LIMIT_EXCEEDED").

```
PATCH /messages/{message_id}
```

```
PATCH /messages/{message_id}
```
Feature level 171
- POST /fetch_api_key,POST /dev_fetch_api_key: The return values
  for these endpoints now include the unique ID of the user who owns the
  API key.

```
POST /fetch_api_key
```

```
POST /dev_fetch_api_key
```
Feature level 170
- POST /user_topics: Added a new endpoint to
  update a user's personal preferences for a topic, which deprecates thePATCH /users/me/subscriptions/muted_topicsendpoint.
  The deprecated endpoint is maintained for backwards-compatibility but may be
  removed in a future release.
- POST /register,GET /events:
  Unmuted added as a visibility policy option to the objects sent in response
  to theuser_topicevent.

```
POST /user_topics
```

```
PATCH /users/me/subscriptions/muted_topics
```

```
POST /register
```

```
GET /events
```
Feature level 169
- PATCH /users/me/subscriptions/muted_topics:
  Trying to mute a topic that is already muted or unmute a topic
  that was not previously muted now results in a success response
  rather than an error.

```
PATCH /users/me/subscriptions/muted_topics
```
Feature level 168
- POST /register,PATCH /settings,PATCH /realm/user_settings_defaults:
  Replaced the boolean user settingrealm_name_in_notificationswith an integerrealm_name_in_email_notifications_policy.

```
POST /register
```

```
PATCH /settings
```

```
PATCH /realm/user_settings_defaults
```
Feature level 167
- All REST API endpoints:
  Implementedignored_parameters_unsupportedas a possible return value
  in the JSON success response for all endpoints. This value is a array
  of any parameters that were sent in the request by the client that are
  not supported by the endpoint. Previously, unsupported parameters were
  silently ignored, except in the subset of endpoints which already
  supported this return value; see feature levels 111, 96 and 78.
Feature level 166
- POST /messages: Eliminated the undocumentedrealm_strparameter. This parameter was already redundant due to
  it needing to match the realm of the user making the request, otherwise
  returning an authorization error. With this, the parameter is removed,
  meaning that if provided in the API request, it will be ignored.

```
POST /messages
```
Feature level 165
- PATCH /user_groups/{user_group_id}: Thenameanddescriptionparameters are now optional.

```
PATCH /user_groups/{user_group_id}
```
Feature level 164
- POST /register: Added theserver_presence_ping_interval_secondsandserver_presence_offline_threshold_secondsfields for clients
  to use when implementing thepresencesystem.

```
POST /register
```
Feature level 163
- GET /users,GET /users/{user_id},GET /users/{email},GET /users/me,GET /events:
  Thedelivery_emailfield is always present in user objects, including
  the case when a user'semail_address_visibilityis set to everyone.
  The value will benullif the requester does not have access to the
  user's real email. For bot users, thedelivery_emailfield is always
  set to the bot user's real email.
- GET /events: Event for updating a user'sdelivery_emailis now sent to all users who have access to it, and
  is also sent when a user'semail_address_visibilitysetting changes.
- GET /events,POST /registerGET /users,GET /users/{user_id},GET /users/{email},GET /users/me,GET /messages,GET /messages/{message_id}: Whether theavatar_urlfield in message and user objects returned by these endpoints can benullnow depends on if the current user has access to the other user's real
  email address based on the other user'semail_address_visibilitypolicy.
- POST /register,PATCH /settings,PATCH /realm/user_settings_defaults:
  Added user settingemail_address_visibility, to replace the
  realm settingemail_address_visibility.
- POST /register,PATCH /realm: Removed realm
  settingemail_address_visibility.

```
GET /users/{user_id}
```

```
GET /users/{email}
```

```
GET /users/me
```

```
GET /events
```

```
GET /events
```

```
GET /events
```

```
POST /register
```

```
GET /users/{user_id}
```

```
GET /users/{email}
```

```
GET /users/me
```

```
GET /messages
```

```
GET /messages/{message_id}
```

```
POST /register
```

```
PATCH /settings
```

```
PATCH /realm/user_settings_defaults
```

```
POST /register
```
Feature level 162
- PATCH /realm,POST /register,GET /events: Added two new realm settingsmove_messages_within_stream_limit_secondsandmove_messages_between_streams_limit_secondsfor organizations to
  configure time limits for editing topics and moving messages between streams.
- PATCH /messages/{message_id}: For users other than
  administrators and moderators, the time limit for editing topics is now
  controlled via the realm settingmove_messages_within_stream_limit_secondsand the time limit for moving messages between streams is now controlled by
  the realm settingmove_messages_between_streams_limit_seconds.

```
POST /register
```

```
GET /events
```

```
PATCH /messages/{message_id}
```
Feature level 161
- POST /users/me/subscriptions,PATCH /streams/{stream_id}: Addedcan_remove_subscribers_group_idparameter to support setting and
  changing the user group whose members can remove other subscribers
  from the specified stream.
- DELETE /users/me/subscriptions: Expanded the
  situations where users can use this endpoint to unsubscribe other
  users from a stream to include the case where the current user has
  access to the stream and is a member of the user group specified by
  thecan_remove_subscribers_group_idfor the stream.

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```

```
DELETE /users/me/subscriptions
```
Feature level 160
- POST /api/v1/jwt/fetch_api_key: Added
  new endpoint to fetch API keys using JSON Web Token (JWT)
  authentication.
- accounts/login/jwt/: Adjusted format of requests to undocumented,
  optional endpoint for JWT authentication log in support.

```
POST /api/v1/jwt/fetch_api_key
```
Feature level 159
- PATCH /realm,POST /register,GET /events:
  Nobody added as an option for the realm settingsedit_topic_policyandmove_messages_between_streams_policy.
- PATCH /messages/{message_id}: Permission
  to edit the stream and/or topic of messages no longer depends on the
  realm settingallow_message_editing.
- PATCH /messages/{message_id}: The user who
  sent the message can no longer edit the message's topic indefinitely.

```
POST /register
```

```
GET /events
```

```
PATCH /messages/{message_id}
```

```
PATCH /messages/{message_id}
```
Feature level 158 is reserved for future use in 6.x maintenance
releases.

## Changes in Zulip 6.2
Feature level 157
- POST /invites: Added support for invitations specifying
  the empty list as the user's initial stream subscriptions. Previously, this
  returned an error. This change was backported from the Zulip 7.0
  branch, and thus is available at feature levels 157-158 and 180+.

```
POST /invites
```

## Changes in Zulip 6.0
Feature level 156
No changes; feature level used for Zulip 6.0 release.
Feature level 155
- GET /messages: The newinclude_anchorparameter controls whether a message with ID matching the specifiedanchorshould be included.
- Theupdate_message_flagsevent sent byPOST
  /messages/flagsno longer redundantly
  lists messages where the flag was set to the same state it was
  already in.
- POST /messages/flags/narrow:
  This new endpoint allows updating message flags on a range of
  messages within a narrow.

```
GET /messages
```

```
POST
  /messages/flags
```

```
POST /messages/flags/narrow
```
Feature level 154
- POST /streams/{stream_id}/delete_topic:
  When the process of deleting messages times out, but successfully
  deletes some messages in the topic (see feature level 147 for when
  this endpoint started deleting messages in batches), a success
  response with"result": "partially_completed"will now be returned
  by the server, analogically to thePOST /mark_all_as_readendpoint
  (see feature level 153 entry below).

```
POST /streams/{stream_id}/delete_topic
```
Feature level 153
- POST /mark_all_as_read: Messages are now
  marked as read in batches, so that progress will be made even if the
  request times out because of an extremely large number of unread
  messages to process. Upon timeout, a success response with"result": "partially_completed"will be returned by the server.

```
POST /mark_all_as_read
```
Feature level 152
- PATCH /messages/{message_id}:
  The default value forsend_notification_to_old_threadwas changed fromtruetofalse.
  When moving a topic within a stream, thesend_notification_to_old_threadandsend_notification_to_new_threadparameters are now respected, and by
  default a notification is sent to the new thread.

```
PATCH /messages/{message_id}
```
Feature level 151
- POST /register,GET /events,POST /realm/profile_fields,GET /realm/profile_fields: Added
  pronouns custom profile field type.

```
POST /register
```

```
GET /events
```

```
POST /realm/profile_fields
```

```
GET /realm/profile_fields
```
Feature level 150
- GET /events: Separate events are now sent on changingallow_message_editing,message_content_edit_limit_secondsandedit_topic_policysettings, whereas previously one event was sent including
  all of these setting values irrespective of which of them were actually changed.
- PATCH /realm: Only changed settings are included in the response data now
  when changingallow_message_editing,edit_topic_policyandmessage_content_edit_limit_secondssettings, instead of including all the
  fields even if one of these settings was changed.

```
GET /events
```
Feature level 149
- POST /register: Theclient_gravatarandinclude_subscribersparameters now return an error forunauthenticated requestsif an
  unsupported value is requested by the client.

```
POST /register
```
Feature level 148
- POST /users/me/status,POST /register,GET /events:
  The user statusawayfield/parameter is deprecated, and as of this
  feature level are a legacy way to access the user'spresence_enabledsetting, withaway = !presence_enabled. To be removed in a future
  release.

```
POST /users/me/status
```

```
POST /register
```

```
GET /events
```
Feature level 147
- POST /streams/{stream_id}/delete_topic:
  Messages now are deleted in batches, starting from the newest, so
  that progress will be made even if the request times out because of
  an extremely large topic.

```
POST /streams/{stream_id}/delete_topic
```
Feature level 146
- POST /realm/profile_fields,GET /realm/profile_fields: Added a
new parameterdisplay_in_profile_summary, which clients use to
decide whether to display the field in a small/summary section of the
user's profile.

```
POST /realm/profile_fields
```

```
GET /realm/profile_fields
```
Feature level 145
- DELETE /users/me/subscriptions: Normal users can
  now remove bots that they own from streams.

```
DELETE /users/me/subscriptions
```
Feature level 144
- GET /messages/{message_id}/read_receipts:
  Theuser_idsarray returned by the server no longer includes IDs
  of users who have been muted by or have muted the current user.

```
GET /messages/{message_id}/read_receipts
```
Feature level 143
- PATCH /realm: Thedisallow_disposable_email_addresses,emails_restricted_to_domains,invite_required, andwaiting_period_thresholdsettings can no longer be changed by
  organization administrators who are not owners.
- PATCH /realm/domains,POST /realm/domains,DELETE
  /realm/domains: Organization administrators who are not owners can
  no longer access these endpoints.
Feature level 142
- GET /users/me/subscriptions,GET
  /streams,POST /register,GET /events: Addedcan_remove_subscribers_group_idfield to Stream and Subscription objects.

```
GET /users/me/subscriptions
```

```
GET
  /streams
```

```
POST /register
```

```
GET /events
```
Feature level 141
- POST /register,PATCH
  /settings,PATCH
  /realm/user_settings_defaults:
  Added newuser_list_styledisplay setting, which controls the
  layout of the right sidebar.

```
POST /register
```

```
PATCH
  /settings
```

```
PATCH
  /realm/user_settings_defaults
```
Feature level 140
- POST /register: Added string fieldserver_emoji_data_urlto the response.

```
POST /register
```
Feature level 139
- GET /get-events: When a user mutes or unmutes
  their subscription to a stream, asubscriptionupdate event
  is now sent for theis_mutedproperty and for the deprecatedin_home_viewproperty to support clients fully migrating to use theis_mutedproperty. Prior to this feature level, only one event was
  sent to clients with the deprecatedin_home_viewproperty.

```
GET /get-events
```
Feature level 138
- POST /register,GET
  /events:message_content_edit_limit_secondsnow represents no limit usingnull, instead of the integer 0.
- PATCH /realm: One now setsmessage_content_edit_limit_secondsto no limit by passing the stringunlimited, rather than the
  integer 0.

```
POST /register
```

```
GET
  /events
```
Feature level 137
- GET /messages/{message_id}/read_receipts:
  Added new endpoint to fetch read receipts for a message.
- POST /register,GET
  /events,PATCH /realm: Added newenable_read_receiptsrealm setting.

```
GET /messages/{message_id}/read_receipts
```

```
POST /register
```

```
GET
  /events
```
Feature level 136
- PATCH /streams/{stream_id}: The endpoint
  now returns an error for a request to make a public stream with
  protected history which was previously ignored silently.
- PATCH /streams/{stream_id}: Added support
  to change access to history of the stream by only passinghistory_public_to_subscribersparameter withoutis_privateandis_web_publicparameters.

```
PATCH /streams/{stream_id}
```

```
PATCH /streams/{stream_id}
```
Feature level 135
- DELETE /user/{user_id}: Addeddeactivation_notification_commentfield controlling whether the
  user receives a notification email about their deactivation.

```
DELETE /user/{user_id}
```
Feature level 134
- GET /events: Addeduser_topicevent type
  which is sent when a topic is muted or unmuted. This generalizes and
  replaces the previousmuted_topicsarray, which will no longer be
  sent ifuser_topicwas included inevent_typeswhen registering
  the queue.
- POST /register: Addeduser_topicsarray
  to the response. This generalizes and replaces the previousmuted_topicsarray, which will no longer be sent ifuser_topicis included infetch_event_types.
- GET /events: When private streams are made
  public,streamevents forop: "create"andsubscriptionevents
  forop: "peer_add"are now sent to clients.

```
GET /events
```

```
POST /register
```

```
GET /events
```
Feature level 133
- POST /register,PATCH /realm: Removed
  stream administrators option fromwildcard_mention_policysetting.
- POST /register,GET /events,GET /users/me/subscriptions: Removedrolefield from subscription objects.

```
POST /register
```

```
POST /register
```

```
GET /events
```

```
GET /users/me/subscriptions
```
Feature level 132
- GET /streams/{stream_id}:
  Added new endpoint to get a stream by ID.

```
GET /streams/{stream_id}
```
Feature level 131
- GET /user_groups,POST
  /register: Renamedsubgroupsfield in
  the user group objects todirect_subgroup_ids.
- GET /events: Renamedsubgroup_idsfield
  in the group object todirect_subgroup_ids.

```
GET /user_groups
```

```
POST
  /register
```

```
GET /events
```
Feature level 130
- PATCH /bots/{bot_user_id}: Added support for changing a bot's role
  via this endpoint. Previously, this could only be done viaPATCH
  /users/{user_id}.

```
PATCH
  /users/{user_id}
```
Feature level 129
- POST /register,GET /events,PATCH /realm: Added realm settingwant_advertise_in_communities_directoryfor organizations to give
  permission to be advertised in the Zulip communities directory.

```
POST /register
```

```
GET /events
```
Feature level 128
- POST /register,GET
  /events,PATCH /realm: Addedorg_typerealm setting.

```
POST /register
```

```
GET
  /events
```
Feature level 127
- GET /user_groups,POST
  /register: Addedsubgroupsfield,
  which is a list of IDs of all the subgroups of the user group, to
  user group objects.
- GET /events: Added newuser_groupevents
  operations for live updates to subgroups (add_subgroupsandremove_subgroups).
- PATCH /user_groups/{user_group_id}/subgroups:
  Added new endpoint for updating subgroups of a user group.
- GET /user_groups/{user_group_id}/members/{user_id}:
  Added new endpoint for checking whether a given user is member of a
  given user group.
- GET /user_groups/{user_group_id}/members:
  Added new endpoint to get members of a user group.
- GET /user_groups/{user_group_id}/members:
  Added new endpoint to get subgroups of a user group.

```
GET /user_groups
```

```
POST
  /register
```

```
GET /events
```

```
PATCH /user_groups/{user_group_id}/subgroups
```

```
GET /user_groups/{user_group_id}/members/{user_id}
```

```
GET /user_groups/{user_group_id}/members
```

```
GET /user_groups/{user_group_id}/members
```
Feature level 126
- POST /invites,POST /invites/multiuse: Replacedinvite_expires_in_daysparameter withinvite_expires_in_minutes.

```
POST /invites
```

```
POST /invites/multiuse
```
Feature level 125
- POST /register,PATCH
  /settings,PATCH
  /realm/user_settings_defaults:
  Added newdisplay_emoji_reaction_usersdisplay setting,
  controlling whether to display the names of users with emoji reactions.

```
POST /register
```

```
PATCH
  /settings
```

```
PATCH
  /realm/user_settings_defaults
```
Feature levels 123-124 are reserved for future use in 5.x maintenance
releases.

## Changes in Zulip 5.0
Feature level 122
No changes; feature level used for Zulip 5.0 release.
Feature level 121
- GET /events: Addedmessage_detailsfield
  appearing in message flag update events when marking previously read
  messages as unread.

```
GET /events
```
Feature level 120
- GET /messages/{message_id}: This endpoint
  now sends the full message details. Previously, it only returned
  the message's raw Markdown content.

```
GET /messages/{message_id}
```
Feature level 119
- POST /register: Addedother_user_idfield
  to thepmsobjects in theunread_msgsdata set, deprecating the
  less clearly namedsender_idfield. This change was motivated by
  the possibility that a one-on-one direct message sent by the current
  user to another user could be marked as unread. Thesender_idfield
  is still present for backwards compatibility with older server versions.

```
POST /register
```
Feature level 118
- GET /messages,GET
  /events: Improved the format of theedit_historyobject within message objects. Entries for stream
  edits now include a both aprev_streamandstreamfield to
  indicate the previous and current stream IDs. Prior to this feature
  level, only theprev_streamfield was present. Entries for topic
  edits now include both aprev_topicandtopicfield to indicate
  the previous and current topic, replacing theprev_subjectfield. These changes substantially simplify client complexity for
  processing historical message edits.
- GET /messages/{message_id}/history:
  Addedstreamfield to message historysnapshotindicating
  the updated stream ID of messages moved to a new stream.

```
GET /messages
```

```
GET
  /events
```

```
GET /messages/{message_id}/history
```
Feature level 117
- POST /invites,POST /invites/multiuse: Added support
  for passingnullas theinvite_expires_in_daysparameter to
  request an invitation that never expires.

```
POST /invites
```

```
POST /invites/multiuse
```
Feature level 116
- GET /server_settings: Addedrealm_web_public_access_enabledas a realm-specific server setting,
  which can be used by clients to detect whether the realm allows and
  has at least oneweb-public stream.

```
GET /server_settings
```
Feature level 115
- Mobile push notifications about stream messages now include thestream_idfield.
Feature level 114
- GET /events: Addedrendering_onlyfield toupdate_messageevent type to indicate if the message change only
  updated the rendering of the message or if it was the result of a
  user interaction.
- GET /events: Updatedupdate_messageevent type
  to always includeedit_timestampanduser_idfields. If the event
  only updates the rendering of the message, then theuser_idfield
  will be present, but with a value ofnull, as the update was not the
  result of a user interaction.

```
GET /events
```

```
GET /events
```
Feature level 113
- GET /realm/emoji,POST /realm/emoji/{emoji_name},GET
  /events,POST /register:
  Thestill_urlfield for custom emoji objects is now always
  present, with a value ofnullfor non-animated emoji. Previously, it
  only was present for animated emoji.

```
GET
  /events
```

```
POST /register
```
Feature level 112
- GET /events: Updatedupdate_messageevent type
  to includestream_idfield for all edits to stream messages.

```
GET /events
```
Feature level 111
- POST /users/me/subscriptions/properties:
  Removedsubscription_datafrom response object, replacing it withignored_parameters_unsupported.

```
POST /users/me/subscriptions/properties
```
Feature level 110
- POST /register: Addedserver_web_public_streams_enabledto the response.

```
POST /register
```
Feature level 109
- POST /register,GET
  /events,PATCH /realm: Added newenable_spectator_accessrealm setting.

```
POST /register
```

```
GET
  /events
```
Feature level 108
- In the mobile application authentication flow, the authenticated
  user'suser_idis now included in the parameters encoded in the
  finalzulip://redirect URL.
Feature level 107
- POST /register,PATCH /settings,PATCH /realm/user_settings_defaults:
  Added user settingescape_navigates_to_default_viewto allow users todisable the keyboard shortcutfor theEsckey that
  navigates the app to the default view.

```
POST /register
```

```
PATCH /settings
```

```
PATCH /realm/user_settings_defaults
```
Feature level 106
- PATCH /user/{user_id}: Removed unnecessary JSON-encoding of string
  parameterfull_name.

```
PATCH /user/{user_id}
```
Feature level 105
- POST /register,PATCH
  /settings,PATCH
  /realm/user_settings_defaults:
  Added three new privacy settings:send_private_typing_notifications,send_stream_typing_notifications, andsend_read_receipts.

```
POST /register
```

```
PATCH
  /settings
```

```
PATCH
  /realm/user_settings_defaults
```
Feature level 104
- PATCH /realm: Addedstring_idparameter for changing an
  organization's subdomain. Currently, this is only allowed for
  changing a demo organization to a normal one.
Feature level 103
- POST /register: Addedcreate_web_public_stream_policypolicy for which users can create web-public streams.
- GET /events,PATCH /realm: Added support for updatingcreate_web_public_stream_policy.
- POST /register: Addedcan_create_web_public_streamsboolean
  field to the response.

```
POST /register
```

```
GET /events
```

```
POST /register
```
Feature level 102
- POST /register,PATCH /realm: Thecreate_stream_policysetting was split into two settings for
  different types of streams:create_private_stream_policyandcreate_public_stream_policy.
- POST /register: Thecreate_stream_policyproperty was deprecated in favor of thecreate_private_stream_policyandcreate_public_stream_policyproperties, but it still available for backwards-compatibility.

```
POST /register
```

```
POST /register
```
Feature level 101
- POST /register,PATCH /realm: Replaced
  theallow_message_deletingboolean field with an integer fielddelete_own_message_policydefining which roles can delete messages
  they had sent.

```
POST /register
```
Feature level 100
- POST /register,GET
  /events:message_content_delete_limit_secondsnow represents no limit usingnull, instead of the integer 0, and 0 is
  no longer a possible value with any meaning.
- PATCH /realm: One now setsmessage_content_delete_limit_secondsto no limit by passing the stringunlimited, rather than the
  integer 0.

```
POST /register
```

```
GET
  /events
```
Feature level 99
- PATCH /realm/user_settings_defaults,PATCH /realm: Thedefault_twenty_four_hour_timeparameter toPATCH /realmhas been replaced by thetwenty_four_hour_timeparameter
  toPATCH /realm/user_settings_defaults, to match the new model for
  user preference defaults settings.
- POST /register: Removedrealm_default_twenty_four_hour_timefrom the response object. This value is now available in thetwenty_four_hour_timefield of therealm_user_settings_defaultobject.

```
PATCH /realm/user_settings_defaults
```

```
POST /register
```
Feature level 98
- POST /users/me/subscriptions: Addedis_web_publicparameter
  for requesting the creation of a web-public stream.
- PATCH /streams/{stream_id}: Addedis_web_publicparameter for converting a stream into a web-public stream.

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```
Feature level 97
- GET /realm/emoji,POST /realm/emoji/{emoji_name},GET
  /events,POST /register:
  Custom emoji objects may now contain astill_urlfield, with the
  URL of a PNG still image version of the emoji. This field will only be
  present for animated emoji.

```
GET
  /events
```

```
POST /register
```
Feature level 96
- PATCH /realm/user_settings_defaults:
  Added new endpoint to update default values of user settings in a realm.
- POST /invites,POST /invites/multiuse: Addedinvite_expires_in_daysparameter encoding the number days before
  the invitation should expire.

```
PATCH /realm/user_settings_defaults
```

```
POST /invites
```

```
POST /invites/multiuse
```
Feature level 95
- POST /register: Addedrealm_user_settings_defaultsobject, containing default values of
  personal user settings for new users in the realm.
- GET /events: Addedrealm_user_settings_defaultsevent type, which is sent when the
  organization's configured default settings for new users change.

```
POST /register
```

```
GET /events
```
Feature level 94
- POST /register: Addeddemo_organization_scheduled_deletion_datefield to realm data.

```
POST /register
```
Feature level 93
- POST /register,GET /user_groups,GET /events: Addedis_system_groupfield to user group
  objects.

```
POST /register
```

```
GET /user_groups
```

```
GET /events
```
Feature level 92
- GET /messages,POST
  /register,GET /users,GET /users/{user_id},GET
  /users/{email}: Theclient_gravatarparameter now defaults totrue.

```
GET /messages
```

```
POST
  /register
```

```
GET /users/{user_id}
```

```
GET
  /users/{email}
```
Feature level 91
- PATCH /realm,PATCH /streams/{stream_id}:
  These endpoints now accept"unlimited"formessage_retention_days,
  replacing"forever"as the way to encode a retention policy where
  messages are not automatically deleted.

```
PATCH /streams/{stream_id}
```
Feature level 90
- POST /register: Theunread_msgssection
  of the response no longer includessender_idsin thestreamsdictionaries. These were removed because no clients were interested
  in using the data, which required substantial complexity to
  construct correctly.

```
POST /register
```
Feature level 89
- GET /events: Introduced theuser_settingsevent type, unifying and replacing the previousupdate_display_settingsandupdate_global_notificationsevent
  types. The legacy event types are still supported for backwards
  compatibility, but will be removed in a future release.
- POST /register: Addeduser_settingsfield
  in the response, which is a dictionary containing all the user's
  personal settings. For backwards-compatibility, individual settings
  will still appear in the top-level response for clients don't
  support theuser_settings_objectclient capability.
- POST /register: Added theuser_settings_objectproperty to supportedclient_capabilities.
  When enabled, the server will not include a duplicate copy of
  personal settings in the top-level response.
- GET /events:update_display_settingsandupdate_global_notificationsevents now only sent to clients that
  did not includeuser_settings_objectin theirclient_capabilitieswhen the event queue was created.

```
GET /events
```

```
POST /register
```

```
POST /register
```

```
GET /events
```
Feature level 88
- POST /register: Addedzulip_merge_basefield to the response.
- GET /events: Added newzulip_merge_basefield to therestartevent.
- GET /server_settings: Addedzulip_merge_baseto the responses which can be used to
  make "About Zulip" widgets in clients.

```
POST /register
```

```
GET /events
```

```
GET /server_settings
```
Feature level 87
- PATCH /settings: Added a newenable_drafts_synchronizationsetting, which controls whether the
  syncing drafts between different clients is enabled.
- GET /events,POST /register:
  Added newenable_drafts_synchronizationsetting underupdate_display_settings.
- GET /drafts: Added new endpoint to fetch user's
  synced drafts from the server.
- POST /drafts: Added new endpoint to create
  drafts when syncing has been enabled.
- PATCH /drafts/{draft_id}: Added new endpoint
  to edit a draft already owned by the user.
- DELETE /drafts/{draft_id}: Added new endpoint
  to delete a draft already owned by the user.

```
PATCH /settings
```

```
GET /events
```

```
POST /register
```

```
GET /drafts
```

```
POST /drafts
```

```
PATCH /drafts/{draft_id}
```

```
DELETE /drafts/{draft_id}
```
Feature level 86
- GET /events: Addedemoji_name,emoji_code, andreaction_typefields touser_statusobjects.
- POST /register: Addedemoji_name,emoji_code, andreaction_typefields touser_statusobjects.
- POST /users/me/status: Added support for newemoji_name,emoji_code, andreaction_typeparameters.

```
GET /events
```

```
POST /register
```

```
POST /users/me/status
```
Feature level 85
- POST /register,PATCH /realm: Replacedadd_emoji_by_admins_onlyfield with an integer fieldadd_custom_emoji_policy.

```
POST /register
```
Feature level 84
- POST /register: Theenter_sendssetting
  is now sent whenupdate_display_settingis present infetch_event_typesinstead ofrealm_user.

```
POST /register
```
Feature level 83
- POST /register: Thecross_realm_botssection of the response now uses theis_system_botflag to
  indicate whether the bot is a system bot.

```
POST /register
```
Feature level 82
- PATCH /settingsnow accepts a newemail_notifications_batching_period_secondsfield for setting the
  time duration for which the server will collect email notifications
  before sending them.

```
PATCH /settings
```
Feature level 81
- POST /users/me/enter-sendshas been removed. Theenter_sendssetting is now edited using the normalPATCH
  /settingsendpoint.

```
PATCH
  /settings
```
Feature level 80
- PATCH /settings: The/settings/notificationsand/settings/displayendpoints were
  merged into the main/settingsendpoint; now all personal settings
  should be edited using that single endpoint. The old URLs are
  preserved as deprecated aliases for backwards compatibility.

```
PATCH /settings
```
Feature level 79
- GET /users/me/subscriptions: Thesubscribersfield now returns user IDs ifinclude_subscribersis
  passed. Previously, this endpoint returned user display email
  addresses in this field.
- GET /streams/{stream_id}/members: This endpoint now returns user
  IDs. Previously, it returned display email addresses.

```
GET /users/me/subscriptions
```
Feature level 78
- PATCH /settings: Addedignored_parameters_unsupportedfield, which is a list of
  parameters that were ignored by the endpoint, to the response
  object.
- PATCH /settings: Removedfull_nameandaccount_emailfields from the response object.

```
PATCH /settings
```

```
PATCH /settings
```
Feature level 77
- GET /events: Removedrecipient_idandsender_idfield in responses ofdelete_messageevent whenmessage_typeisprivate.

```
GET /events
```
Feature level 76
- POST /fetch_api_key,POST /dev_fetch_api_key: The HTTP status
  for authentication errors is now 401. These previously used the HTTP
  403 error status.
- Error handling: API
  requests that involve a deactivated user or organization now use the
  HTTP 401 error status. These previously used the HTTP 403 error status.
- Error handling: All error responses
  now include acodekey with a machine-readable string value. The
  default value for this key is"BAD_REQUEST"for general error
  responses.
- Mobile push notifications now include thementioned_user_group_idandmentioned_user_group_namefields when a user group containing
  the user is mentioned.  Previously, these were indistinguishable
  from personal mentions (as both types havetrigger="mention").

```
POST /fetch_api_key
```

```
POST /dev_fetch_api_key
```
Feature level 75
- POST /register,PATCH /realm: Replacedallow_community_topic_editingfield with an integer fieldedit_topic_policy.

```
POST /register
```
Feature level 74
- POST /register: Addedserver_needs_upgradeandevent_queue_longpoll_timeout_secondsfield when fetching
  realm data.

```
POST /register
```
Feature level 73
- GET /users,GET /users/{user_id},GET /users/{email}andGET /users/me: Added isuser_billing_adminfield to
  returned user objects.
- GET /events: Addedis_billing_adminfield to
  user objects sent inrealm_userevents.
- POST /register: Addedis_billing_adminfield
  in the user objects returned in therealm_usersfield.

```
GET /users/{user_id}
```

```
GET /users/{email}
```

```
GET /users/me
```

```
GET /events
```

```
POST /register
```
Feature level 72
- POST /register: Renamedmax_icon_file_sizetomax_icon_file_size_mib,realm_upload_quotatorealm_upload_quota_mibandmax_logo_file_sizetomax_logo_file_size_mib.

```
POST /register
```
Feature level 71
- GET /events: Addedis_web_publicfield tostreamevents changinginvite_only.

```
GET /events
```
Feature level 70
- POST /register: Added new top-levelserver_timestampfield when fetching presence data, to match the
  existing presence API.

```
POST /register
```
Feature levels 66-69 are reserved for future use in 4.x maintenance
releases.

## Changes in Zulip 4.0
Feature level 65
No changes; feature level used for Zulip 4.0 release.
Feature level 64
- PATCH /streams/{stream_id}: Removed unnecessary JSON-encoding of string
  parametersnew_nameanddescription.
- PATCH /settings/display: Removed unnecessary JSON-encoding of string
  parametersdefault_view,emojisetandtimezone.
Feature level 63
- PATCH /settings/notifications: Removed unnecessary JSON-encoding of string
  parameternotification_sound.
- PATCH /settings/display: Removed unnecessary JSON-encoding of string
  parameterdefault_language.
- POST /users/me/tutorial_status: Removed unnecessary JSON-encoding of string
  parameterstatus.
- POST /realm/domains: Removed unnecessary JSON-encoding of string
  parameterdomain.
- PATCH /default_stream_groups/{user_id}: Removed unnecessary JSON-encoding of string
  parametersnew_group_nameandnew_description.
- POST /users/me/hotspots: Removed unnecessary JSON-encoding of string
  parameterhotspot.
Feature level 62
- Addedmoderators onlyoption forwildcard_mention_policy.
Feature level 61
- POST /invites,POST /invites/multiuse: Added support
  for inviting users as moderators.

```
POST /invites
```

```
POST /invites/multiuse
```
Feature level 60
- POST /register: Added a new boolean fieldis_moderator, similar to the existingis_admin,is_ownerandis_guestfields, to the response.
- PATCH /users/{user_id}: Added support for
  changing a user's organization-level role to moderator.
- API endpoints that returnrolevalues can now return300, the
  encoding of the moderator role.

```
POST /register
```

```
PATCH /users/{user_id}
```
Feature level 59
- GET /users,GET /users/{user_id},GET /users/{email}andGET /users/me: Addedrolefield to returned
  user objects.
- GET /events: Addedrolefield to
  user objects sent inrealm_userevents.
- POST /register: Addedrolefield
  in the user objects returned in therealm_usersfield.
- GET /events: Added newzulip_versionandzulip_feature_levelfields to therestartevent.

```
GET /users/{user_id}
```

```
GET /users/{email}
```

```
GET /users/me
```

```
GET /events
```

```
POST /register
```

```
GET /events
```
Feature level 58
- POST /register: Added the newstream_typing_notificationsproperty to supportedclient_capabilities.
- GET /events: Extended format fortypingevents to support typing notifications in stream messages. These new
  events are only sent to clients withclient_capabilitiesshowing support forstream_typing_notifications.
- POST /typing: Added support
  for sending typing notifications for stream messages.

```
POST /register
```

```
GET /events
```

```
POST /typing
```
Feature level 57
- PATCH /realm/filters/{filter_id}: New
  endpoint added to update a realm linkifier.

```
PATCH /realm/filters/{filter_id}
```
Feature level 56
- POST /register: Added a new settingmove_messages_between_streams_policyfor controlling who can
  move messages between streams.

```
POST /register
```
Feature level 55
- POST /register: Addedrealm_giphy_ratingandgiphy_rating_optionsfields.
- PATCH /realm: Addedgiphy_ratingparameter.

```
POST /register
```
Feature level 54
- GET /realm/filtershas been removed and replace withGET
  /realm/linkifierswhich returns the data in a
  cleaner dictionary format.
- GET /events: Introduced new event typerealm_linkifiers.  The previousrealm_filtersevent type is
  still supported for backwards compatibility, but will be removed in
  a future release.
- POST /register: The response now supports arealm_linkifiersevent type, containing the same data as the
  legacyrealm_filterskey, with a more extensible object
  format. The previousrealm_filtersevent type is still supported
  for backwards compatibility, but will be removed in a future
  release. The legacyrealm_filterskey is deprecated but remains
  available for backwards compatibility.

```
GET
  /realm/linkifiers
```

```
GET /events
```

```
POST /register
```
Feature level 53
- POST /register: Addedmax_topic_lengthandmax_message_length, and renamedmax_stream_name_lengthandmax_stream_description_lengthto allow clients to transparently
  support these values changing in a future server version.

```
POST /register
```
Feature level 52
- PATCH /realm: Removed unnecessary JSON-encoding of string
  parametersname,description,default_language, anddefault_code_block_language.
Feature level 51
- POST /register: Added a new boolean fieldcan_invite_others_to_realm.

```
POST /register
```
Feature level 50
- POST /register: Replacedinvite_by_admins_onlyfield with an integer fieldinvite_to_realm_policy.

```
POST /register
```
Feature level 49
- Added newPOST /realm/playgroundandDELETE /realm/playground/{playground_id}endpoints for code playgrounds.
- GET /events: A newrealm_playgroundsevents
  is sent when changes are made to a set of configured code playgrounds for
  an organization.
- POST /register: Added a newrealm_playgroundsfield, which is required to fetch the set of configured code playgrounds for
  an organization.

```
POST /realm/playground
```

```
DELETE /realm/playground/{playground_id}
```

```
GET /events
```

```
POST /register
```
Feature level 48
- POST /users/me/muted_users/{muted_user_id},DELETE /users/me/muted_users/{muted_user_id}:
  New endpoints added to mute/unmute users.
- GET /events: Added new event typemuted_userswhich will be sent to a user when the set of users muted by them has
  changed.
- POST /register: Added a newmuted_usersfield,
  which identifies the set of other users the current user has muted.

```
POST /users/me/muted_users/{muted_user_id}
```

```
DELETE /users/me/muted_users/{muted_user_id}
```

```
GET /events
```

```
POST /register
```
Feature level 47
- POST /register: Added a newgiphy_api_keyfield, which is required to fetch GIFs using the GIPHY API.

```
POST /register
```
Feature level 46
- GET /messagesandGET
  /events: Thetopic_linksfield now contains a
  list of dictionaries, rather than a list of strings.

```
GET /messages
```

```
GET
  /events
```
Feature level 45
- GET /events: Removed uselessopfield fromcustom_profile_fieldsevents.  These events contain the full set
  of configuredcustom_profile_fieldsfor the organization
  regardless of what triggered the change.

```
GET /events
```
Feature level 44
- POST /register: extended theunread_msgsobject to includeold_unreads_missing, which indicates whether the
  server truncated theunread_msgsdue to excessive total unread
  messages.

```
POST /register
```
Feature level 43
- GET /users/{user_id_or_email}/presence:
  Added support for passing theuser_idto identify the target user.

```
GET /users/{user_id_or_email}/presence
```
Feature level 42
- PATCH /settings/display: Added a newdefault_viewsetting allowing
  the user toset the default view.
Feature level 41
- GET /events: Removednamefield from update
  subscription events.

```
GET /events
```
Feature level 40
- GET /events: Removedemailfield from update
  subscription events.

```
GET /events
```
Feature level 39
- Added newGET /users/{email}endpoint.

```
GET /users/{email}
```
Feature level 38
- POST /register: Increasedrealm_community_topic_editing_limit_secondstime limit value
  to 259200s (3 days).

```
POST /register
```
Feature level 37
- Consistently providesubscribersin stream data when
  clients register for subscriptions withinclude_subscribers,
  even if the user can't access subscribers.
Feature level 36
- POST /users: Restricted access to organization
  administrators with thecan_create_userspermission.
- Error handling: Thecodekey will now be present in errors that are due to rate
  limits, with a value of"RATE_LIMIT_HIT".

```
POST /users
```
Feature level 35
- GET /events: Thesubscriptionevents forpeer_addandpeer_removenow includeuser_idsandstream_idsarrays. Previously, these events included singularuser_idandstream_idintegers.

```
GET /events
```
Feature level 34
- POST /register: Added a newwildcard_mention_policysetting for controlling who can use wildcard mentions in large streams.

```
POST /register
```
Feature level 33
- Markdown message formatting:Code blocksnow have adata-code-languageattribute attached to the outer HTMLdivelement, recording the
  programming language that was selected for syntax highlighting.
Feature level 32
- GET /events: Addedopfield toupdate_message_flagsevents, deprecating theoperationfield
  (which has the same value).  This removes an unintentional anomaly
  in the format of this event type.

```
GET /events
```
Feature level 31
- GET /users/me/subscriptions: Added arolefield to Subscription objects representing whether the user
  is a stream administrator.
- GET /events: Addedrolefield to
  Subscription objects sent insubscriptionsevents.

```
GET /users/me/subscriptions
```

```
GET /events
```
Note that as of this feature level, stream administrators are a
partially completed feature.  In particular, it is impossible for a
user to be a stream administrator at this feature level.
Feature level 30
- GET /users/me/subscriptions,GET
  /streams: Addeddate_createdto Stream
  objects.
- POST /users,POST /bots: The ID of the newly
  created user is now returned in the response.

```
GET /users/me/subscriptions
```

```
GET
  /streams
```

```
POST /users
```
Feature levels 28 and 29 are reserved for future use in 3.x bug fix
releases.

## Changes in Zulip 3.1
Feature level 27
- POST /users: Removedshort_namefield fromdisplay_recipientarray objects.

```
POST /users
```
Feature level 26
- GET /messages,GET /events:
  Thesender_short_namefield is no longer included in message objects
  returned by these endpoints.
- GET /messages: Removedshort_namefield fromdisplay_recipientarray objects.

```
GET /messages
```

```
GET /events
```

```
GET /messages
```

## Changes in Zulip 3.0
Feature level 25
No changes; feature level used for Zulip 3.0 release.
Feature level 24
- Markdown message formatting:
  The rarely used!avatar()and!gravatar()markup syntax, which
  was never documented and had inconsistent syntax, was removed.
Feature level 23
- GET/PUT/POST /users/me/pointer: Removed.  Zulip 3.0 removes thepointerconcept from Zulip; this legacy data structure was
  replaced by tracking unread messages and loading views centered on
  the first unread message.
Feature level 22
- GET /attachments: The date when a message
  using the attachment was sent is now correctly encoded asdate_sent, replacing the confusingly namednamefield.  Thedate_sentandcreate_timefields of attachment objects are now
  encoded as integers; (previously the implementation could send
  floats incorrectly suggesting that microsecond precision is
  relevant).
- GET /invites: Now encodes the user ID of the person
   who created the invitation asinvited_by_user_id, replacing the previousreffield (which had that user's Zulip display email address).
- POST /register: The encoding of an
  unlimitedrealm_message_retention_daysin the response was changed
  fromnullto-1.

```
GET /attachments
```

```
GET /invites
```

```
POST /register
```
Feature level 21
- PATCH /settings/display: Replaced thenight_modeboolean withcolor_schemeas part of supporting automatic night theme detection.
Feature level 20
- Added support for inviting users as organization owners to the
  invitation endpoints.
Feature level 19
- GET /events: Thesubscriptionevents forpeer_addandpeer_removenow identify the modified
  stream by thestream_idfield, replacing the oldnamefield.

```
GET /events
```
Feature level 18
- POST /register: Addeduser_avatar_url_field_optionalto supportedclient_capabilities.

```
POST /register
```
Feature level 17
- GET /users/me/subscriptions,GET /streams: Addedmessage_retention_daysto Stream objects.
- POST /users/me/subscriptions,PATCH
  /streams/{stream_id}: Addedmessage_retention_daysparameter.

```
GET /users/me/subscriptions
```

```
GET /streams
```

```
POST /users/me/subscriptions
```

```
PATCH
  /streams/{stream_id}
```
Feature level 16
- GET /users/me: Removedpointerfrom the response,
  as the "pointer" concept is being removed in Zulip.
- Changed the rendered HTML markup for mentioning a time to use the<time>HTML tag.  It is OK for clients to ignore the previous time
  mention markup, as the feature was not advertised before this change.

```
GET /users/me
```
Feature level 15
- Markdown message formatting: Addedspoilersto supported message formatting features.
Feature level 14
- GET /users/me/subscriptions: Removed
  theis_old_streamfield from Stream objects.  This field was
  always equivalent tostream_weekly_traffic != nullon the same object.

```
GET /users/me/subscriptions
```
Feature level 13
- POST /register: Addedbulk_message_deletionto supportedclient_capabilities.
- GET /events:delete_messageevents have new behavior.  Thesenderandsender_idfields were
  removed, and themessage_idfield was replaced by amessage_idslist for clients with thebulk_message_deletionclient capability.
  All clients should upgrade; we expectbulk_message_deletionto be
  required in the future.

```
POST /register
```

```
GET /events
```
Feature level 12
- GET /users/{user_id}/subscriptions/{stream_id}:
  New endpoint added for checking if another user is subscribed to a stream.

```
GET /users/{user_id}/subscriptions/{stream_id}
```
Feature level 11
- POST /register: Addedrealm_community_topic_editing_limit_secondsto the response, the
  time limit before community topic editing is forbidden.  Anullvalue means no limit. This was previously hard-coded in the server
  as 86400 seconds (1 day).
- POST /register: The response now contains
  anis_ownerboolean field, which is similar to the existingis_adminandis_guestfields.
- POST /typing: Removed legacy
  support for sending email addresses in thetoparameter, rather
  than user IDs, to encode direct message recipients.

```
POST /register
```

```
POST /register
```

```
POST /typing
```
Feature level 10
- GET /users/me: Addedavatar_version,is_guest,is_active,timezone, anddate_joinedfields to the User objects.
- GET /users/me: Removedclient_idandshort_namefrom the response to this endpoint.  These fields had no purpose and
  were inconsistent with other API responses describing users.

```
GET /users/me
```

```
GET /users/me
```
Feature level 9
- POST /users/me/subscriptions,DELETE
  /users/me/subscriptions: Other users to
  subscribe/unsubscribe, declared in theprincipalsparameter, can
  now be referenced by user_id, rather than Zulip display email
  address.
- PATCH /messages/{message_id}: Addedsend_notification_to_old_threadandsend_notification_to_new_threadoptional parameters.

```
POST /users/me/subscriptions
```

```
DELETE
  /users/me/subscriptions
```

```
PATCH /messages/{message_id}
```
Feature level 8
- GET /users,GET /users/{user_id}andGET /users/me: User objects now contain theis_ownerfield as well.
- Markdown message formatting:
  Addedglobal timesto supported message
  formatting features.

```
GET /users/{user_id}
```

```
GET /users/me
```
Feature level 7
- GET /events:realm_userandrealm_botevents no longer contain anemailfield to identify
  the user; use theuser_idfield instead.  Previously, some (but
  not all) events of these types contained anemailkey in addition to
  touser_id) for identifying the modified user.
- PATCH /users/{user_id}: Theis_adminandis_guestparameters were removed in favor of the more generalroleparameter for specifying a change in user role.
- GET /events:realm_userevents
  sent when a user's role changes now includeroleproperty, instead
  of the previousis_guestoris_adminbooleans.
- GET /realm/emoji: The user who uploaded a
  given custom emoji is now indicated by anauthor_idfield, replacing
  a previousauthorobject that had unnecessary additional data.

```
GET /events
```

```
PATCH /users/{user_id}
```

```
GET /events
```

```
GET /realm/emoji
```
Feature level 6
- GET /events:realm_userevents to
  update a user's avatar now include theavatar_versionfield, which
  is important for correctly refetching medium-size avatar images when
  the user's avatar changes.
- GET /usersandGET
  /users/{user_id}: User objects now contain theavatar_versionfield as well.

```
GET /events
```

```
GET
  /users/{user_id}
```
Feature level 5
- GET /events:realm_botevents,
  sent when changes are made to bot users, now contain an
  integer-formatowner_idfield, replacing theownerfield (which
  was an email address).

```
GET /events
```
Feature level 4
- jitsi_server_url,development_environment,server_generation,password_min_length,password_min_guesses,max_file_upload_size_mib,max_avatar_file_size_mib,server_inline_image_preview,server_inline_url_embed_preview,server_avatar_changes_disabledandserver_name_changes_disabledfields are now available viaPOST /registerto make them accessible to all the clients;
  they were only internally available to Zulip's web app prior to this.
Feature level 3
- POST /register:zulip_versionandzulip_feature_levelare always returned in the endpoint response.
  Previously, they were only present ifevent_typesincludedzulip_version.
- Added newpresence_enableduser notification setting; previouslypresencewas always enabled.

```
POST /register
```
Feature level 2
- POST /messages/{message_id}/reactions:
  Thereaction_typeparameter is optional; the server will guess thereaction_typeif it is not specified (checking custom emoji, then
  Unicode emoji for any with the provided name).
- reactionsobjects returned by the API (both inGET /messagesand
  inGET /events) now include the user who reacted in a top-leveluser_idfield.  The legacyuserdictionary (which had
  inconsistent format between those two endpoints) is deprecated.

```
POST /messages/{message_id}/reactions
```
Feature level 1
- PATCH /messages/{message_id}: Added thestream_idparameter to support moving messages between streams.
- GET /messages,GET /events:
  Addedprev_streamas a potential property of theedit_historyobject
  within message objects to indicate when a message was moved to another
  stream.
- GET /messages/{message_id}/history:prev_streamis present insnapshotobjects withinmessage_historyobject when a message was moved to another stream.
- GET /server_settings: Addedzulip_feature_level, which can be used by clients to detect which
  of the features described in this changelog are supported.
- POST /register: Addedzulip_feature_levelto the response ifzulip_versionis among the requestedevent_types.
- GET /users: User objects for bots now
  contain abot_owner_id, replacing the previousbot_ownerfield
  (which had the email address of the bot owner).
- GET /users/{user_id}: New endpoint added to get
  a single user's details by the user's ID.
- GET /messages: Add support for string-format
  values for theanchorparameter, deprecating and replacing theuse_first_unread_anchorparameter.
- GET /messages,GET /events:
  Message objects now usetopic_linksrather thansubject_linksto
  indicate links either present in the topic or generated by linkifiers
  applied to the topic.
- GET /streams,POST /users/me/subscriptions,PATCH /streams/{stream_id}: Stream objects now
  havestream_post_policyenum for specifying who can post to the stream,
  deprecating and replacing theis_announcement_onlyboolean.
- GET /user_uploads/{realm_id_str}/{filename}:
  New endpoint added for requesting a temporary URL for an uploaded
  file that does not require authentication to access (e.g., for passing
  from a Zulip desktop, mobile, or terminal app to the user's default
  browser).
- POST /register,GET /events,PATCH /realm: Nobody added as an option for the realm settingemail_address_visibility.
- POST /register,GET /events,PATCH /realm: Added realm settingprivate_message_policy.
- POST /register,GET /events:muted_topicsarray objects now are 3-item tuples that include the
  stream name, the topic name, and the time when the topic was muted.
  Previously, they were 2-item tuples and did not include the time when
  the topic was muted.
- GET /server_settings: Addedgitlabboolean
  to deprecatedauthentication_methodsobject.
- POST /register,GET /events,PATCH /realm: None added as an option for the realm settingvideo_chat_providerto disable video call UI.

```
PATCH /messages/{message_id}
```

```
GET /messages
```

```
GET /events
```

```
GET /messages/{message_id}/history
```

```
GET /server_settings
```

```
POST /register
```

```
GET /users/{user_id}
```

```
GET /messages
```

```
GET /messages
```

```
GET /events
```

```
GET /streams
```

```
POST /users/me/subscriptions
```

```
PATCH /streams/{stream_id}
```

```
GET /user_uploads/{realm_id_str}/{filename}
```

```
POST /register
```

```
GET /events
```

```
POST /register
```

```
GET /events
```

```
POST /register
```

```
GET /events
```

```
GET /server_settings
```

```
POST /register
```

```
GET /events
```

## Changes in Zulip 2.1
- POST /register: Addedrealm_default_external_accountsto endpoint response.
- GET /messages: Added support forsearch/narrow optionsthat use stream/user
  IDs to specify a message's sender, its stream, and/or its recipient(s).
- GET /users: Addedinclude_custom_profile_fieldsto request custom profile field data.
- GET /users/me: Addedavatar_urlfield,
  containing the user's avatar URL, to the response.
- GET /users/me/subscriptions: Addedinclude_subscribersparameter controlling whether data on the
  other subscribers is included.  Previous behavior was to always send
  subscriber data.
- GET /users/me/subscriptions:
  Stream-level notification settings likepush_notificationswere
  changed to be nullable boolean fields (true/false/null), withnullmeaning that the stream inherits the organization-level default.
  Previously, the only values weretrueorfalse. A client communicates
  support for this feature usingclient_capabilities.
- GET /users/me/subscriptions: Addedwildcard_mentions_notifynotification setting, with the same
  global-plus-stream-level-override model as other notification settings.
- GET /server_settings: Addedexternal_authentication_methodsstructure, used to display login
  buttons nicely in the mobile apps.
- Addedfirst_message_idfield to Stream objects.  This is helpful
  for determining whether the stream has any messages older than a
  window cached in a client.
- Addedis_web_publicfield to Stream objects.  This field is
  intended to support web-public streams.
- GET /export/realm: Added endpoint for
  fetching public data exports.POST /export/realm: Added endpoint for
  triggering a public data export.
- PATCH /realm: Addedinvite_to_stream_policy,create_stream_policy,digest_emails_enabled,digest_weekday,user_group_edit_policy, andavatar_changes_disabledorganization settings.
- Addedfluid_layout_width,desktop_icon_count_display, anddemote_inactive_streamsdisplay settings.
- enable_stream_soundswas renamed toenable_stream_audible_notifications.
- POST /users/me/subscriptions/properties:
  Deprecatedin_home_view, replacing it with the more readableis_muted(with the opposite meaning).
- Custom profile fields: AddedEXTERNAL_ACCOUNTfield type.

```
POST /register
```

```
GET /messages
```

```
GET /users/me
```

```
GET /users/me/subscriptions
```

```
GET /users/me/subscriptions
```

```
GET /users/me/subscriptions
```

```
GET /server_settings
```

```
GET /export/realm
```

```
POST /export/realm
```

```
POST /users/me/subscriptions/properties
```

## Changes in Zulip 2.0
- PATCH /users/me/subscriptions/muted_topics:
  Added support for using stream IDs to specify the stream in which to
  mute/unmute a topic.
- POST /messages: Added support for using user
  IDs and stream IDs for specifying the recipients of a message.
- POST /messages,POST
  /messages/{message_id}: Added support for
  encoding topics using thetopicparameter name.  The previoussubjectparameter name was deprecated but is still supported for
  backwards-compatibility.
- POST /typing: Added support for specifying the
  recipients with user IDs, deprecating the original API of specifying
  them using email addresses.

```
PATCH /users/me/subscriptions/muted_topics
```

```
POST /messages
```

```
POST /messages
```

```
POST
  /messages/{message_id}
```

```
POST /typing
```

## Changes not yet stabilized
- POST /register: Addedslim_presenceparameter.  Changes the format of presence events, but is still
  being changed and should not be used by clients.

```
POST /register
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.