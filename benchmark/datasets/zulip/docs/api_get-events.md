# Get events from an event queue | Zulip API documentation

*Source: https://zulip.com/api/get-events*

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

# Get events from an event queue
GET https://your-org.zulipchat.com/api/v1/events
This endpoint allows you to receive new events froma registered event queue.
Long-lived clients should use theevent_queue_longpoll_timeout_secondsproperty returned byPOST /registeras the client-side HTTP request timeout for
calls to this endpoint. It is guaranteed to be higher than
heartbeat frequency and should be respected by clients to
avoid breaking when heartbeat frequency increases.

## Usage examples
PythonJavaScriptcurl
- Python
- JavaScript
- curl

```
#!/usr/bin/env python3importsysimportzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# If you already have a queue registered, and thus have a `queue_id`# on hand, you may use `client.get_events()` and pass in the below# parameters, like so:result=client.get_events(queue_id=queue_id,last_event_id=-1)print(result)
```

```
#!/usr/bin/env python3importsysimportzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# If you already have a queue registered, and thus have a `queue_id`# on hand, you may use `client.get_events()` and pass in the below# parameters, like so:result=client.get_events(queue_id=queue_id,last_event_id=-1)print(result)
```
More examples and documentation can be foundhere.

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Retrieve events from a queue with given "queue_id"consteventParams={queue_id,last_event_id:-1,};console.log(awaitclient.events.retrieve(eventParams));})();
```

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Retrieve events from a queue with given "queue_id"consteventParams={queue_id,last_event_id:-1,};console.log(awaitclient.events.retrieve(eventParams));})();
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/events \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode queue_id=fb67bf8a-c031-47cc-84cf-ed80accacda8 \
    --data-urlencode last_event_id=-1
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/events \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode queue_id=fb67bf8a-c031-47cc-84cf-ed80accacda8 \
    --data-urlencode last_event_id=-1
```

## Parameters
queue_idstringrequired

```
"fb67bf8a-c031-47cc-84cf-ed80accacda8"
```
The ID of an event queue that was previously registered viaPOST /api/v1/register(seeRegister a queue).
last_event_idintegeroptional
The highest event ID in this queue that you've received and
wish to acknowledge. See thecode forcall_on_each_eventin thezulip Python
modulefor an
example implementation of correctly processing each event
exactly once.

```
call_on_each_event
```
dont_blockbooleanoptional
Set totrueif the client is requesting a nonblocking reply. If not
specified, the request will block until either a new event is available
or a few minutes have passed, in which case the server will send the
client a heartbeat event.
Defaults tofalse.
Note: The parameters documented above are optional in the sense that
even if you haven't registered a queue by explicitly requesting thePOST /registerendpoint, you could pass the parameters forthePOST /registerendpointto this
endpoint and a queue would be registered in the absence of aqueue_id.

```
POST /register
```

## Response

#### Return values
- events:arrayAn array ofeventobjects (possibly zero-length ifdont_blockis
set) with IDs newer thanlast_event_id. Event IDs are
guaranteed to be increasing, but they are not guaranteed to be
consecutive.
- queue_id:stringThe ID of the registered queue.

## Events bytype

### alert_words
Event sent to a user's clients when that user's set of configuredalert wordshave changed.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- alert_words:(string)[]An array of strings, where each string is an alert word (or phrase)
configured by the user.
Example

```
{"alert_words":["alert_word"],"id":0,"type":"alert_words"}
```

```
{"alert_words":["alert_word"],"id":0,"type":"alert_words"}
```

### user_settingsop: update
Event sent to a user's clients when that user's settings have changed.
Changes: In Zulip 12.0 (feature level 439), the deprecated, legacyupdate_display_settingsandupdate_global_notificationsevent types
were removed entirely. All clients should be using this event type for
updates to a user's settings.
New in Zulip 5.0 (feature level 89), replaced and deprecated theupdate_display_settingsandupdate_global_notificationsevent types.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- property:stringName of the changed setting.
- value:boolean | integer | stringNew value of the changed setting.
- language_name:stringPresent only if the setting to be changed isdefault_language. Contains the name of the
new default language in English.
Example

```
{"id":0,"op":"update","property":"high_contrast_mode","type":"user_settings","value":false}
```

```
{"id":0,"op":"update","property":"high_contrast_mode","type":"user_settings","value":false}
```

### realm_userop: update
Event sent generally to all users who can access the modified
user for changes in the set of users or those users metadata.
Changes: Prior to Zulip 8.0 (feature level 228), this event
was sent to all users in the organization.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- person:object | object | object | object | object | object | object | object | object | object | objectObject containing the changed details of the user.
It has multiple forms depending on the value changed.Changes: Removedis_billing_adminfield in Zulip 10.0
(feature level 363), as it was replaced by thecan_manage_billing_grouprealm setting.When a user changes their full name.user_id:integerThe ID of modified user.full_name:stringThe new full name for the user.When a user changes their avatar.user_id:integerThe ID of the user who is affected by this change.avatar_url:stringThe URL of the new avatar for the user.avatar_source:stringThe new avatar data source type for the user. Valid values are:"G" = Hosted by Gravatar"J" = Generated using Jdenticon"U" = Uploaded by userChanges: The "J" value is new in Zulip 12.0 (feature level 466).avatar_url_medium:stringThe new medium-size avatar URL for user.avatar_version:integerThe version number for the user's avatar. This is useful
for cache-busting.When a user changes theirprofile time zone.user_id:integerThe ID of modified user.email:stringThe Zulip API email of the user.Deprecated: This field will be removed in a future
release as it is redundant with theuser_id.timezone:stringThe IANA identifier of the new profile time zone for the user.When the owner of a bot changes.user_id:integerThe ID of the user/bot whose owner has changed.bot_owner_id:integerThe user ID of the new bot owner.When theroleof a user changes.user_id:integerThe ID of the user affected by this change.role:integerThe newroleof the user.When the value of a user's delivery email as visible to you changes,
    either due to the email address changing or your access to the user's
    email changing via an update to theiremail_address_visibilitysetting.Changes: Prior to Zulip 7.0 (feature level 163), this event was
sent only to the affected user, and this event would only be triggered
by changing the affected user's delivery email.user_id:integerThe ID of the user affected by this change.delivery_email:string | nullThe new delivery email of the user.This value can benullif the affected user
changed theiremail_address_visibilitysetting
such that you cannot access their real email.Changes: Before Zulip 7.0 (feature level 163),nullwas not a possible value for this event as
it was only sent to the affected user when their
email address was changed.When the user updates one of their custom profile
    fields.user_id:integerThe ID of the user affected by this change.custom_profile_field:objectObject containing details about the custom
profile data change.id:integerThe ID of the custom profile field which user updated.value:string | nullUser's personal value for this custom profile field,
ornullif unset.rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.When the Zulip API email address of a user changes,
    either due to the user's email address changing, or
    due to changes in the user'semail address visibility.user_id:integerThe ID of the user affected by this change.new_email:stringThe new value ofemailfor the user. The client
should update any data structures associated
with this user to use this new value as the
user's Zulip API email address.When a user is deactivated or reactivated. Only
    users who can access the modified user under the
    organization'scan_access_all_users_grouppolicy
    will receive this event.Clients receiving a deactivation event should
remove the user from all user groups in their data
structures, because deactivated users cannot be
members of groups.Changes: Prior to Zulip 10.0 (feature level
303), reactivation events were sent to users who
could not access the reactivated user due to acan_access_all_users_grouppolicy. Also,
previously, Clients were not required to update
group membership records during user deactivation.New in Zulip 8.0 (feature level 222). Previously the server
sent arealm_userevent withopfield set toremovewhen deactivating a user and arealm_userevent withopfield set toaddwhen reactivating a user.user_id:integerThe ID of the user affected by this change.is_active:booleanA boolean describing whether the user account has been deactivated.When an imported user logs into the organization for
    the first time.Changes: New in Zulip 12.0 (feature level 433).user_id:integerThe ID of the user affected by this change.is_imported_stub:booleanThis value is alwaysfalse.
    * Sent when thedate_joinedvalue is updated after an
        imported stub user or a user created via the API logs
        in for the first time.Changes: New in Zulip 12.0 (feature level 475).user_id:integerThe ID of the user affected by this change.date_joined:stringThe time when the user logged in to their account
for the first time.
- When a user changes their full name.user_id:integerThe ID of modified user.full_name:stringThe new full name for the user.
- When a user changes their avatar.user_id:integerThe ID of the user who is affected by this change.avatar_url:stringThe URL of the new avatar for the user.avatar_source:stringThe new avatar data source type for the user. Valid values are:"G" = Hosted by Gravatar"J" = Generated using Jdenticon"U" = Uploaded by userChanges: The "J" value is new in Zulip 12.0 (feature level 466).avatar_url_medium:stringThe new medium-size avatar URL for user.avatar_version:integerThe version number for the user's avatar. This is useful
for cache-busting.
- When a user changes theirprofile time zone.user_id:integerThe ID of modified user.email:stringThe Zulip API email of the user.Deprecated: This field will be removed in a future
release as it is redundant with theuser_id.timezone:stringThe IANA identifier of the new profile time zone for the user.
- When the owner of a bot changes.user_id:integerThe ID of the user/bot whose owner has changed.bot_owner_id:integerThe user ID of the new bot owner.
- When theroleof a user changes.user_id:integerThe ID of the user affected by this change.role:integerThe newroleof the user.
- When the value of a user's delivery email as visible to you changes,
    either due to the email address changing or your access to the user's
    email changing via an update to theiremail_address_visibilitysetting.Changes: Prior to Zulip 7.0 (feature level 163), this event was
sent only to the affected user, and this event would only be triggered
by changing the affected user's delivery email.user_id:integerThe ID of the user affected by this change.delivery_email:string | nullThe new delivery email of the user.This value can benullif the affected user
changed theiremail_address_visibilitysetting
such that you cannot access their real email.Changes: Before Zulip 7.0 (feature level 163),nullwas not a possible value for this event as
it was only sent to the affected user when their
email address was changed.
- When the user updates one of their custom profile
    fields.user_id:integerThe ID of the user affected by this change.custom_profile_field:objectObject containing details about the custom
profile data change.id:integerThe ID of the custom profile field which user updated.value:string | nullUser's personal value for this custom profile field,
ornullif unset.rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- When the Zulip API email address of a user changes,
    either due to the user's email address changing, or
    due to changes in the user'semail address visibility.user_id:integerThe ID of the user affected by this change.new_email:stringThe new value ofemailfor the user. The client
should update any data structures associated
with this user to use this new value as the
user's Zulip API email address.
- When a user is deactivated or reactivated. Only
    users who can access the modified user under the
    organization'scan_access_all_users_grouppolicy
    will receive this event.Clients receiving a deactivation event should
remove the user from all user groups in their data
structures, because deactivated users cannot be
members of groups.Changes: Prior to Zulip 10.0 (feature level
303), reactivation events were sent to users who
could not access the reactivated user due to acan_access_all_users_grouppolicy. Also,
previously, Clients were not required to update
group membership records during user deactivation.New in Zulip 8.0 (feature level 222). Previously the server
sent arealm_userevent withopfield set toremovewhen deactivating a user and arealm_userevent withopfield set toaddwhen reactivating a user.user_id:integerThe ID of the user affected by this change.is_active:booleanA boolean describing whether the user account has been deactivated.
- When an imported user logs into the organization for
    the first time.Changes: New in Zulip 12.0 (feature level 433).user_id:integerThe ID of the user affected by this change.is_imported_stub:booleanThis value is alwaysfalse.
    * Sent when thedate_joinedvalue is updated after an
        imported stub user or a user created via the API logs
        in for the first time.Changes: New in Zulip 12.0 (feature level 475).user_id:integerThe ID of the user affected by this change.date_joined:stringThe time when the user logged in to their account
for the first time.
- user_id:integerThe ID of modified user.
- full_name:stringThe new full name for the user.
- user_id:integerThe ID of the user who is affected by this change.
- avatar_url:stringThe URL of the new avatar for the user.
- avatar_source:stringThe new avatar data source type for the user. Valid values are:"G" = Hosted by Gravatar"J" = Generated using Jdenticon"U" = Uploaded by userChanges: The "J" value is new in Zulip 12.0 (feature level 466).
- avatar_url_medium:stringThe new medium-size avatar URL for user.
- avatar_version:integerThe version number for the user's avatar. This is useful
for cache-busting.
- "G" = Hosted by Gravatar
- "J" = Generated using Jdenticon
- "U" = Uploaded by user
- user_id:integerThe ID of modified user.
- email:stringThe Zulip API email of the user.Deprecated: This field will be removed in a future
release as it is redundant with theuser_id.
- timezone:stringThe IANA identifier of the new profile time zone for the user.
- user_id:integerThe ID of the user/bot whose owner has changed.
- bot_owner_id:integerThe user ID of the new bot owner.
- user_id:integerThe ID of the user affected by this change.
- role:integerThe newroleof the user.
- user_id:integerThe ID of the user affected by this change.
- delivery_email:string | nullThe new delivery email of the user.This value can benullif the affected user
changed theiremail_address_visibilitysetting
such that you cannot access their real email.Changes: Before Zulip 7.0 (feature level 163),nullwas not a possible value for this event as
it was only sent to the affected user when their
email address was changed.
- user_id:integerThe ID of the user affected by this change.
- custom_profile_field:objectObject containing details about the custom
profile data change.id:integerThe ID of the custom profile field which user updated.value:string | nullUser's personal value for this custom profile field,
ornullif unset.rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- id:integerThe ID of the custom profile field which user updated.
- value:string | nullUser's personal value for this custom profile field,
ornullif unset.
- rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- user_id:integerThe ID of the user affected by this change.
- new_email:stringThe new value ofemailfor the user. The client
should update any data structures associated
with this user to use this new value as the
user's Zulip API email address.
- user_id:integerThe ID of the user affected by this change.
- is_active:booleanA boolean describing whether the user account has been deactivated.
- user_id:integerThe ID of the user affected by this change.
- is_imported_stub:booleanThis value is alwaysfalse.
    * Sent when thedate_joinedvalue is updated after an
        imported stub user or a user created via the API logs
        in for the first time.
- user_id:integerThe ID of the user affected by this change.
- date_joined:stringThe time when the user logged in to their account
for the first time.
Example

```
{"id":0,"op":"update","person":{"avatar_source":"G","avatar_url":"https://secure.gravatar.com/avatar/6d8cad0fd00256e7b40691d27ddfd466?d=identicon&version=3","avatar_url_medium":"https://secure.gravatar.com/avatar/6d8cad0fd00256e7b40691d27ddfd466?d=identicon&s=500&version=3","avatar_version":3,"user_id":10},"type":"realm_user"}
```

```
{"id":0,"op":"update","person":{"avatar_source":"G","avatar_url":"https://secure.gravatar.com/avatar/6d8cad0fd00256e7b40691d27ddfd466?d=identicon&version=3","avatar_url_medium":"https://secure.gravatar.com/avatar/6d8cad0fd00256e7b40691d27ddfd466?d=identicon&s=500&version=3","avatar_version":3,"user_id":10},"type":"realm_user"}
```

### subscriptionop: add
Event sent to a user's clients when that user's channel subscriptions
have changed (either the set of subscriptions or their properties).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- subscriptions:(object)[]A list of dictionaries where each dictionary contains
information about one of the subscribed channels.Changes: Removedemail_addressfield from the dictionary
in Zulip 8.0 (feature level 226).Removedrolefield from the dictionary
in Zulip 6.0 (feature level 133).stream_id:integerThe unique ID of a channel.name:stringThe name of a channel.description:stringThedescriptionof the channel inZulip-flavored Markdownformat,
intended to be used to prepopulate UI for editing a channel's
description.SeeMarkdown message formattingfor details on Zulip's HTML format.See alsorendered_description.rendered_description:stringThedescriptionof the channel rendered as HTML, intended to
be used when displaying the channel description in a UI.One should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax
work correctly. And any client-side security logic for
user-generated message content should be applied when displaying
this HTML as though it were the body of a Zulip message.See alsodescription.date_created:integerThe UNIX timestamp for when the channel was created, in UTC seconds.Changes: New in Zulip 4.0 (feature level 30).creator_id:integer | nullThe ID of the user who created this channel.Anullvalue means the channel has no recorded creator, which is often
because the channel is very old, was created during realm creation or
because it was created via a data import tool ormanagement command.Changes: New in Zulip 9.0 (feature level 254).invite_only:booleanSpecifies whether the channel is private or not.
Only people who have been invited can access a private channel.subscribers:(integer)[]A list of user IDs of users who are also subscribed
to a given channel. Included only ifinclude_subscribersistrue.partial_subscribers:(integer)[]Ifinclude_subscribers="partial"was requested, the server may, at its discretion, send apartial_subscriberslist rather than asubscriberslist
for channels with a large number of subscribers.Thepartial_subscriberslist contains an arbitrary
subset of the channel's subscribers that is guaranteed
to include all bot user subscribers as well as all
users who have been active in the last 14 days, but
otherwise can be chosen arbitrarily by the server.Changes: New in Zulip 11.0 (feature level 412).desktop_notifications:boolean | nullA boolean specifying whether desktop notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_desktop_notifications, for
this channel.email_notifications:boolean | nullA boolean specifying whether email notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_email_notifications, for
this channel.wildcard_mentions_notify:boolean | nullA boolean specifying whether wildcard mentions
trigger notifications as though they were personal
mentions in this channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting, wildcard_mentions_notify, for
this channel.push_notifications:boolean | nullA boolean specifying whether push notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_push_notifications, for
this channel.audible_notifications:boolean | nullA boolean specifying whether audible notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_audible_notifications, for
this channel.pin_to_top:booleanA boolean specifying whether the given channel has been pinned
to the top.is_muted:booleanWhether the user has muted the channel. Muted channels do
not count towards your total unread count and do not show
up in theCombined feedview (previously known asAll messages).Changes: Prior to Zulip 2.1.0, this feature was
represented by the more confusingly namedin_home_view(with the
opposite value,in_home_view=!is_muted).in_home_view:booleanLegacy property for if the given channel is muted, with inverted meaning.Changes: Deprecated in Zulip 2.1.0. Clients should useis_mutedwhere available.is_announcement_only:booleanWhether only organization administrators can post to the channel.Changes: Deprecated in Zulip 3.0 (feature level 1). Clients
should usestream_post_policyinstead.is_web_public:booleanWhether the channel has been configured to allow unauthenticated
access to its message history from the web.color:stringThe user's personal color for the channel.stream_post_policy:integerA deprecated representation of a superset of the users who
have permission to post messages to the channel available
for backwards-compatibility. Clients should usecan_send_message_groupinstead.It is an enum with the following possible values, corresponding
to roles/system groups:1 = Any user can post.2 = Only administrators can post.3 = Onlyfull memberscan post.4 = Only moderators can post.Changes: Deprecated in Zulip 10.0 (feature level 333) and
replaced bycan_send_message_group, which supports finer
resolution of configurations, resulting in this property being
inaccurate following that transition.New in Zulip 3.0 (feature level 1), replacing the previousis_announcement_onlyboolean.message_retention_days:integer | nullNumber of days that messages sent to this channel will be stored
before being automatically deleted by themessage retention
policy. There are two special values:null, the default, means the channel will inherit the organization
  level setting.-1encodes retaining messages in this channel forever.Changes: New in Zulip 3.0 (feature level 17).history_public_to_subscribers:booleanWhether the history of the channel is public to its subscribers.Currently always true for public channels (i.e."invite_only": falseimplies"history_public_to_subscribers": true), but clients should not make that
assumption, as we may change that behavior in the future.first_message_id:integer | nullThe ID of the first message in the channel.Intended to help clients determine whether they need to display
UI like the "show all topics" widget that would suggest the channel
has older history that can be accessed.Isnullfor channels with no message history.folder_id:integer | nullThe ID of the folder to which the channel belongs.Isnullif channel does not belong to any folder.Changes: New in Zulip 11.0 (feature level 389).topics_policy:stringWhethernamed topicsand the empty
topic (i.e.,"general chat" topic)
are enabled in this channel."inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty topic in this
  channel."allow_empty_topic": Messages can be sent to both named topics and
  the empty topic in this channel."disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty topic is disabled."empty_topic_only": Messages can be sent to the empty topic in this
  channel, but named topics are disabled. See"general chat"
  channels.The"empty_topic_only"policy can only be set if all existing messages
in the channel are already in the empty topic.When creating a new channel, if thetopics_policyis not specified, the"inherit"option will be set.Changes: In Zulip 11.0 (feature level 404), the"empty_topic_only"option was added.New in Zulip 11.0 (feature level 392).is_recently_active:booleanWhether the channel has recent message activity. Clients should use this to implementhiding inactive channels.Changes: New in Zulip 10.0 (feature level 323). Previously, clients implemented the
demote_inactive_streams from local message history, resulting in a choppy loading
experience.stream_weekly_traffic:integer | nullThe average number of messages sent to the channel per week, as
estimated based on recent weeks, rounded to the nearest integer.Ifnull, the channel was recently created and there is
insufficient data to estimate the average traffic.can_add_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to add subscribers to this channel.Users who can administer the channel or have similar realm-level
permissions can add subscribers to a public channel regardless
of the value of this setting.Users in this group need not be subscribed to a private channel to
add subscribers to it.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 342). Previously, there was no
channel-level setting for this permission.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_remove_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to remove subscribers from this channel.Organization administrators can unsubscribe others from a channel as though
they were in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349), channel administrators
could not unsubscribe other users if they were not an organization
administrator or part ofcan_remove_subscribers_group. Realm administrators
were not allowed to unsubscribe other users from a private channel if they
were not subscribed to that channel.Prior to Zulip 10.0 (feature level 320), this value was always the integer
ID of a system group.Before Zulip 8.0 (feature level 197), thecan_remove_subscribers_groupsetting was namedcan_remove_subscribers_group_id.New in Zulip 6.0 (feature level 142).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_administer_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to administer this channel.Organization administrators can administer every channel as though they were
in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349) a user needed tohave content accessto a channel in
order to modify it. The exception to this rule was that organization
administrators can edit channel names and descriptions without
having full access to the channel.New in Zulip 10.0 (feature level 325). Prior to this
change, the permission to administer channels was limited to realm
administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_delete_any_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete any message in the channel.Note that a user musthave content accessto a
channel in order to delete any message in the channel.Users present in the organization-levelcan_delete_any_message_groupsetting can always delete any message in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users incan_delete_any_message_groupwere able
delete any message in the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_delete_own_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete the messages that they have sent in the channel.Note that a user musthave content accessto a
channel in order to delete their own message in the channel.Users with permission to delete any message in the channel
and users present in the organization-levelcan_delete_own_message_groupsetting
can always delete their own messages in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users in the organization-levelcan_delete_any_message_groupandcan_delete_own_message_groupsettings were able delete their own messages in
the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_move_messages_out_of_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages out of this channel.Note that a user musthave content accessto a
channel in order to move messages out of the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_channels_groupsetting can always move messages
out of the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_channels_groupwere able
move messages between channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_move_messages_within_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages within this channel.Note that a user musthave content accessto a
channel in order to move messages within the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_topics_groupsetting can always move messages
within the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_topics_groupwere able
move messages between topics of a channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_send_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to post in this channel.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Note that using this permission to send a message to a new topic requires
also having permission to create new topics in the channel.Changes: New in Zulip 10.0 (feature level 333). Previouslystream_post_policyfield used to control the permission to
post in the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_subscribe_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to subscribe themselves to this channel.Everyone, excluding guests, can subscribe to any public channel
irrespective of this setting.Users in this group can subscribe to a private channel as well.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 357).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_resolve_topics_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to resolve topics in the channel.Users who have similar realm-level permissions can resolve topics
in a channel regardless of the value of this setting.Changes: New in Zulip 11.0 (feature level 402).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_create_topic_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to create a new topic in this channel.Note that using this permission requires also having permission to
send messages in the channel.Note that this must be therole:everyonesystem groupforprivate channels with protected history.Changes: New in Zulip 12.0 (feature level 441). Previously,
if you could send messages in a channel, you could create topics in
the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.is_archived:booleanA boolean indicating whether the channel isarchived.Changes: New in Zulip 10.0 (feature level 315).
Previously, subscriptions only included active
channels. Note that some endpoints will never return archived
channels unless the client declares explicit support for
them via thearchived_channelsclient capability.subscriber_count:numberThe total number of non-deactivated users (including bots) who
are subscribed to the channel. Clients are responsible for updating
this value usingpeer_addandpeer_removeevents.The server's internals cannot guarantee this value is correctly
synced withpeer_addandpeer_removeevents for the channel. As
a result, if a (rare) race occurs between a change in the channel's
subscribers and fetching this value, it is possible for a client
that is correctly following the events protocol to end up with a
permanently off-by-one error in the channel's subscriber count.Clients are recommended to fetch full subscriber data for a channel
in contexts where it is important to avoid this risk. The official
web application, for example, uses this field primarily while
waiting to fetch a given channel's full subscriber list from the
server.Changes: New in Zulip 11.0 (feature level 394).
- stream_id:integerThe unique ID of a channel.
- name:stringThe name of a channel.
- description:stringThedescriptionof the channel inZulip-flavored Markdownformat,
intended to be used to prepopulate UI for editing a channel's
description.SeeMarkdown message formattingfor details on Zulip's HTML format.See alsorendered_description.
- rendered_description:stringThedescriptionof the channel rendered as HTML, intended to
be used when displaying the channel description in a UI.One should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax
work correctly. And any client-side security logic for
user-generated message content should be applied when displaying
this HTML as though it were the body of a Zulip message.See alsodescription.
- date_created:integerThe UNIX timestamp for when the channel was created, in UTC seconds.Changes: New in Zulip 4.0 (feature level 30).
- creator_id:integer | nullThe ID of the user who created this channel.Anullvalue means the channel has no recorded creator, which is often
because the channel is very old, was created during realm creation or
because it was created via a data import tool ormanagement command.Changes: New in Zulip 9.0 (feature level 254).
- invite_only:booleanSpecifies whether the channel is private or not.
Only people who have been invited can access a private channel.
- subscribers:(integer)[]A list of user IDs of users who are also subscribed
to a given channel. Included only ifinclude_subscribersistrue.
- partial_subscribers:(integer)[]Ifinclude_subscribers="partial"was requested, the server may, at its discretion, send apartial_subscriberslist rather than asubscriberslist
for channels with a large number of subscribers.Thepartial_subscriberslist contains an arbitrary
subset of the channel's subscribers that is guaranteed
to include all bot user subscribers as well as all
users who have been active in the last 14 days, but
otherwise can be chosen arbitrarily by the server.Changes: New in Zulip 11.0 (feature level 412).
- desktop_notifications:boolean | nullA boolean specifying whether desktop notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_desktop_notifications, for
this channel.
- email_notifications:boolean | nullA boolean specifying whether email notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_email_notifications, for
this channel.
- wildcard_mentions_notify:boolean | nullA boolean specifying whether wildcard mentions
trigger notifications as though they were personal
mentions in this channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting, wildcard_mentions_notify, for
this channel.
- push_notifications:boolean | nullA boolean specifying whether push notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_push_notifications, for
this channel.
- audible_notifications:boolean | nullA boolean specifying whether audible notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_audible_notifications, for
this channel.
- pin_to_top:booleanA boolean specifying whether the given channel has been pinned
to the top.
- is_muted:booleanWhether the user has muted the channel. Muted channels do
not count towards your total unread count and do not show
up in theCombined feedview (previously known asAll messages).Changes: Prior to Zulip 2.1.0, this feature was
represented by the more confusingly namedin_home_view(with the
opposite value,in_home_view=!is_muted).
- in_home_view:booleanLegacy property for if the given channel is muted, with inverted meaning.Changes: Deprecated in Zulip 2.1.0. Clients should useis_mutedwhere available.
- is_announcement_only:booleanWhether only organization administrators can post to the channel.Changes: Deprecated in Zulip 3.0 (feature level 1). Clients
should usestream_post_policyinstead.
- is_web_public:booleanWhether the channel has been configured to allow unauthenticated
access to its message history from the web.
- color:stringThe user's personal color for the channel.
- stream_post_policy:integerA deprecated representation of a superset of the users who
have permission to post messages to the channel available
for backwards-compatibility. Clients should usecan_send_message_groupinstead.It is an enum with the following possible values, corresponding
to roles/system groups:1 = Any user can post.2 = Only administrators can post.3 = Onlyfull memberscan post.4 = Only moderators can post.Changes: Deprecated in Zulip 10.0 (feature level 333) and
replaced bycan_send_message_group, which supports finer
resolution of configurations, resulting in this property being
inaccurate following that transition.New in Zulip 3.0 (feature level 1), replacing the previousis_announcement_onlyboolean.
- message_retention_days:integer | nullNumber of days that messages sent to this channel will be stored
before being automatically deleted by themessage retention
policy. There are two special values:null, the default, means the channel will inherit the organization
  level setting.-1encodes retaining messages in this channel forever.Changes: New in Zulip 3.0 (feature level 17).
- history_public_to_subscribers:booleanWhether the history of the channel is public to its subscribers.Currently always true for public channels (i.e."invite_only": falseimplies"history_public_to_subscribers": true), but clients should not make that
assumption, as we may change that behavior in the future.
- first_message_id:integer | nullThe ID of the first message in the channel.Intended to help clients determine whether they need to display
UI like the "show all topics" widget that would suggest the channel
has older history that can be accessed.Isnullfor channels with no message history.
- folder_id:integer | nullThe ID of the folder to which the channel belongs.Isnullif channel does not belong to any folder.Changes: New in Zulip 11.0 (feature level 389).
- topics_policy:stringWhethernamed topicsand the empty
topic (i.e.,"general chat" topic)
are enabled in this channel."inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty topic in this
  channel."allow_empty_topic": Messages can be sent to both named topics and
  the empty topic in this channel."disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty topic is disabled."empty_topic_only": Messages can be sent to the empty topic in this
  channel, but named topics are disabled. See"general chat"
  channels.The"empty_topic_only"policy can only be set if all existing messages
in the channel are already in the empty topic.When creating a new channel, if thetopics_policyis not specified, the"inherit"option will be set.Changes: In Zulip 11.0 (feature level 404), the"empty_topic_only"option was added.New in Zulip 11.0 (feature level 392).
- is_recently_active:booleanWhether the channel has recent message activity. Clients should use this to implementhiding inactive channels.Changes: New in Zulip 10.0 (feature level 323). Previously, clients implemented the
demote_inactive_streams from local message history, resulting in a choppy loading
experience.
- stream_weekly_traffic:integer | nullThe average number of messages sent to the channel per week, as
estimated based on recent weeks, rounded to the nearest integer.Ifnull, the channel was recently created and there is
insufficient data to estimate the average traffic.
- can_add_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to add subscribers to this channel.Users who can administer the channel or have similar realm-level
permissions can add subscribers to a public channel regardless
of the value of this setting.Users in this group need not be subscribed to a private channel to
add subscribers to it.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 342). Previously, there was no
channel-level setting for this permission.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_remove_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to remove subscribers from this channel.Organization administrators can unsubscribe others from a channel as though
they were in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349), channel administrators
could not unsubscribe other users if they were not an organization
administrator or part ofcan_remove_subscribers_group. Realm administrators
were not allowed to unsubscribe other users from a private channel if they
were not subscribed to that channel.Prior to Zulip 10.0 (feature level 320), this value was always the integer
ID of a system group.Before Zulip 8.0 (feature level 197), thecan_remove_subscribers_groupsetting was namedcan_remove_subscribers_group_id.New in Zulip 6.0 (feature level 142).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_administer_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to administer this channel.Organization administrators can administer every channel as though they were
in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349) a user needed tohave content accessto a channel in
order to modify it. The exception to this rule was that organization
administrators can edit channel names and descriptions without
having full access to the channel.New in Zulip 10.0 (feature level 325). Prior to this
change, the permission to administer channels was limited to realm
administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_delete_any_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete any message in the channel.Note that a user musthave content accessto a
channel in order to delete any message in the channel.Users present in the organization-levelcan_delete_any_message_groupsetting can always delete any message in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users incan_delete_any_message_groupwere able
delete any message in the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_delete_own_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete the messages that they have sent in the channel.Note that a user musthave content accessto a
channel in order to delete their own message in the channel.Users with permission to delete any message in the channel
and users present in the organization-levelcan_delete_own_message_groupsetting
can always delete their own messages in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users in the organization-levelcan_delete_any_message_groupandcan_delete_own_message_groupsettings were able delete their own messages in
the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_move_messages_out_of_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages out of this channel.Note that a user musthave content accessto a
channel in order to move messages out of the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_channels_groupsetting can always move messages
out of the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_channels_groupwere able
move messages between channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_move_messages_within_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages within this channel.Note that a user musthave content accessto a
channel in order to move messages within the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_topics_groupsetting can always move messages
within the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_topics_groupwere able
move messages between topics of a channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_send_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to post in this channel.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Note that using this permission to send a message to a new topic requires
also having permission to create new topics in the channel.Changes: New in Zulip 10.0 (feature level 333). Previouslystream_post_policyfield used to control the permission to
post in the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_subscribe_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to subscribe themselves to this channel.Everyone, excluding guests, can subscribe to any public channel
irrespective of this setting.Users in this group can subscribe to a private channel as well.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 357).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_resolve_topics_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to resolve topics in the channel.Users who have similar realm-level permissions can resolve topics
in a channel regardless of the value of this setting.Changes: New in Zulip 11.0 (feature level 402).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_create_topic_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to create a new topic in this channel.Note that using this permission requires also having permission to
send messages in the channel.Note that this must be therole:everyonesystem groupforprivate channels with protected history.Changes: New in Zulip 12.0 (feature level 441). Previously,
if you could send messages in a channel, you could create topics in
the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- is_archived:booleanA boolean indicating whether the channel isarchived.Changes: New in Zulip 10.0 (feature level 315).
Previously, subscriptions only included active
channels. Note that some endpoints will never return archived
channels unless the client declares explicit support for
them via thearchived_channelsclient capability.
- subscriber_count:numberThe total number of non-deactivated users (including bots) who
are subscribed to the channel. Clients are responsible for updating
this value usingpeer_addandpeer_removeevents.The server's internals cannot guarantee this value is correctly
synced withpeer_addandpeer_removeevents for the channel. As
a result, if a (rare) race occurs between a change in the channel's
subscribers and fetching this value, it is possible for a client
that is correctly following the events protocol to end up with a
permanently off-by-one error in the channel's subscriber count.Clients are recommended to fetch full subscriber data for a channel
in contexts where it is important to avoid this risk. The official
web application, for example, uses this field primarily while
waiting to fetch a given channel's full subscriber list from the
server.Changes: New in Zulip 11.0 (feature level 394).

```
include_subscribers="partial"
```
- 1 = Any user can post.
- 2 = Only administrators can post.
- 3 = Onlyfull memberscan post.
- 4 = Only moderators can post.
- null, the default, means the channel will inherit the organization
  level setting.
- -1encodes retaining messages in this channel forever.
- "inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty topic in this
  channel.
- "allow_empty_topic": Messages can be sent to both named topics and
  the empty topic in this channel.
- "disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty topic is disabled.
- "empty_topic_only": Messages can be sent to the empty topic in this
  channel, but named topics are disabled. See"general chat"
  channels.

```
realm_topics_policy
```
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
Example

```
{"id":0,"op":"add","subscriptions":[{"audible_notifications":null,"can_add_subscribers_group":2,"can_remove_subscribers_group":2,"can_subscribe_group":2,"color":"#76ce90","creator_id":null,"description":"","desktop_notifications":null,"email_notifications":null,"first_message_id":null,"folder_id":1,"history_public_to_subscribers":true,"in_home_view":true,"invite_only":false,"is_announcement_only":false,"is_archived":false,"is_muted":false,"is_recently_active":true,"is_web_public":false,"message_retention_days":null,"name":"test","pin_to_top":false,"push_notifications":null,"rendered_description":"","stream_id":9,"stream_post_policy":1,"stream_weekly_traffic":null,"subscribers":[10],"wildcard_mentions_notify":null}],"type":"subscription"}
```

```
{"id":0,"op":"add","subscriptions":[{"audible_notifications":null,"can_add_subscribers_group":2,"can_remove_subscribers_group":2,"can_subscribe_group":2,"color":"#76ce90","creator_id":null,"description":"","desktop_notifications":null,"email_notifications":null,"first_message_id":null,"folder_id":1,"history_public_to_subscribers":true,"in_home_view":true,"invite_only":false,"is_announcement_only":false,"is_archived":false,"is_muted":false,"is_recently_active":true,"is_web_public":false,"message_retention_days":null,"name":"test","pin_to_top":false,"push_notifications":null,"rendered_description":"","stream_id":9,"stream_post_policy":1,"stream_weekly_traffic":null,"subscribers":[10],"wildcard_mentions_notify":null}],"type":"subscription"}
```

### subscriptionop: remove
Event sent to a user's clients when that user has been unsubscribed
from one or more channels.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- subscriptions:(object)[]A list of dictionaries, where each dictionary contains
information about one of the newly unsubscribed channels.stream_id:integerThe ID of the channel.name:stringThe name of the channel.
- stream_id:integerThe ID of the channel.
- name:stringThe name of the channel.
Example

```
{"id":0,"op":"remove","subscriptions":[{"name":"test","stream_id":9}],"type":"subscription"}
```

```
{"id":0,"op":"remove","subscriptions":[{"name":"test","stream_id":9}],"type":"subscription"}
```

### subscriptionop: update
Event sent to a user's clients when a property of the user's
subscription to a channel has been updated. This event is used
only for personal properties likeis_mutedorpin_to_top.
See thestream op: updateeventfor updates to global properties of a channel.

```
stream op: update
```
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- stream_id:integerThe ID of the channel whose subscription details have changed.
- property:stringThe property of the subscription which has changed. For details on the
various subscription properties that a user can change, seePOST /users/me/subscriptions/properties.Clients should generally handle an unknown property received here without
crashing, since that will naturally happen when connecting to a Zulip
server running a new version that adds a new subscription property.Changes: As of Zulip 6.0 (feature level 139), updates to theis_mutedproperty or the deprecatedin_home_viewproperty will send twosubscriptionupdate events, one for each property, to support clients fully migrating to
use theis_mutedproperty. Prior to this feature level, updates to either
property only sent one event with the deprecatedin_home_viewproperty.
- value:integer | boolean | stringThe new value of the changed property.
Example

```
{"id":0,"op":"update","property":"pin_to_top","stream_id":11,"type":"subscription","value":true}
```

```
{"id":0,"op":"update","property":"pin_to_top","stream_id":11,"type":"subscription","value":true}
```

### subscriptionop: peer_add
Event sent when another user subscribes to a channel, or their
subscription is newly visible to the current user.
When a user subscribes to a channel, the current user will receive this
event only if theyhave permission to see the channel's subscriber
list. When the current user gains permission
to see a given channel's subscriber list, they will receive this event
for the existing subscriptions to the channel.
Changes: Prior to Zulip 8.0 (feature level 220), this event was
incorrectly not sent to guest users when subscribers to web-public
channels and subscribed public channels changed.
Prior to Zulip 8.0 (feature level 205), this event was not sent when
a user gained access to a channel due to theirrole
changing.
Prior to Zulip 6.0 (feature level 134), this event was not sent when a
private channel was made public.
In Zulip 4.0 (feature level 35), the singularuser_idandstream_idintegers included in this event were replaced with pluraluser_idsandstream_idsinteger arrays.
In Zulip 3.0 (feature level 19), thestream_idfield was added to
identify the channel the user subscribed to, replacing thenamefield.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- stream_ids:(integer)[]The IDs of channels that have new or updated subscriber data.Changes: New in Zulip 4.0 (feature level 35), replacing
thestream_idinteger.
- user_ids:(integer)[]The IDs of the users who are newly visible as subscribed to
the specified channels.Changes: New in Zulip 4.0 (feature level 35), replacing
theuser_idinteger.
Example

```
{"id":0,"op":"peer_add","stream_ids":[9],"type":"subscription","user_ids":[12]}
```

```
{"id":0,"op":"peer_add","stream_ids":[9],"type":"subscription","user_ids":[12]}
```

### subscriptionop: peer_remove
Event sent to other users when users have been unsubscribed
from channels. Sent to all users if the channel is public or to only
the existing subscribers if the channel is private.
Changes: Prior to Zulip 8.0 (feature level 220), this event was
incorrectly not sent to guest users when subscribers to web-public
channels and subscribed public channels changed.
In Zulip 4.0 (feature level 35), the singularuser_idandstream_idintegers included in this event were replaced
with pluraluser_idsandstream_idsinteger arrays.
In Zulip 3.0 (feature level 19), thestream_idfield was
added to identify the channel the user unsubscribed from,
replacing thenamefield.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- stream_ids:(integer)[]The IDs of the channels from which the users have been
unsubscribed from.When a user is deactivated, the server will send this event
removing the user's subscriptions before therealm_userevent
for the user's deactivation.Changes: Before Zulip 12.0 (feature level 428), this event
was incorrectly not sent when deactivating a user subscribed to
archived channels. Clients supporting older server versions and
maintaining peer subscriber data need to remove all channel
subscriptions for a user when processing therealm_userevent
withop="remove".Changes: Before Zulip 10.0 (feature level 377), this event
was not sent on user deactivation.Changes: New in Zulip 4.0 (feature level 35), replacing
thestream_idinteger.
- user_ids:(integer)[]The IDs of the users who have been unsubscribed.Changes: New in Zulip 4.0 (feature level 35), replacing
theuser_idinteger.
Example

```
{"id":0,"op":"peer_remove","stream_ids":[9],"type":"subscription","user_ids":[12]}
```

```
{"id":0,"op":"peer_remove","stream_ids":[9],"type":"subscription","user_ids":[12]}
```

### message
Event type for messages.
Changes: In Zulip 3.1 (feature level 26), thesender_short_namefield was removed from message
objects.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- message:objectObject containing details of the message.avatar_url:string | nullThe URL of the message sender's avatar. Can benullonly if
the current user has access to the sender's real email address
andclient_gravatarwastrue.Ifnull, then the sender has not uploaded an avatar in Zulip,
and the client can compute the gravatar URL by hashing the
sender's email address, which corresponds in this case to their
real email address.Changes: Before Zulip 7.0 (feature level 163), access to a
user's real email address was a realm-level setting. As of this
feature level,email_address_visibilityis a user setting.client:stringA Zulip "client" string, describing what Zulip client
sent the message.content:stringThe content/body of the message.
Whenapply_markdownis set, it will be in HTML format.SeeMarkdown message formattingfor details on Zulip's HTML format.content_type:stringThe HTTPcontent_typefor the message content. This
will betext/htmlortext/x-markdown, depending on
whetherapply_markdownwas set.See the help center article onmessage formattingfor details on Zulip-flavored Markdown.display_recipient:string | (object)[]Data on the recipient of the message;
either the name of a channel or a dictionary containing basic data on
the users who received the message.id:integerID of the user.email:stringZulip API email of the user.full_name:stringFull name of the user.is_mirror_dummy:booleanWhether the user is a mirror dummy.edit_history:(object)[]An array of objects, with each object documenting the
changes in a previous edit made to the message,
ordered chronologically from most recent to least recent
edit.Not present if the message has never been edited or moved,
or ifviewing message edit historyis not allowed in the organization.Every object will containuser_idandtimestamp.The other fields are optional, and will be present or not
depending on whether the channel, topic, and/or message
content were modified in the edit event. For example, if
only the topic was edited, onlyprev_topicandtopicwill be present in addition touser_idandtimestamp.Changes: In Zulip 10.0 (feature level 284), removed theprev_rendered_content_versionfield as it is an internal
server implementation detail not used by any client.prev_content:stringOnly present if message's content was edited.The content of the message immediately prior to this
edit event.prev_rendered_content:stringOnly present if message's content was edited.The rendered HTML representation ofprev_content.SeeMarkdown message formattingfor details on Zulip's HTML format.prev_stream:integerOnly present if message's channel was edited.The channel ID of the message immediately prior to this
edit event.Changes: New in Zulip 3.0 (feature level 1).prev_topic:stringOnly present if message's topic was edited.The topic of the message immediately prior to this
edit event.Changes: New in Zulip 5.0 (feature level 118).
Previously, this field was calledprev_subject;
clients are recommended to renameprev_subjecttoprev_topicif present for compatibility with
older Zulip servers.stream:integerOnly present if message's channel was edited.The ID of the channel containing the message
immediately after this edit event.Changes: New in Zulip 5.0 (feature level 118).timestamp:integerThe UNIX timestamp for the edit.topic:stringOnly present if message's topic was edited.The topic of the message immediately after this edit event.Changes: New in Zulip 5.0 (feature level 118).user_id:integer | nullThe ID of the user that made the edit.Will benullonly for edit history
events predating March 2017.Clients can display edit history events where this
isnullas modified by either the sender (for content
edits) or an unknown user (for topic edits).id:integerThe unique message ID. Messages should always be
displayed sorted by ID.is_me_message:booleanWhether the message is a/me status messagelast_edit_timestamp:integerThe UNIX timestamp for when the message's content was last edited, in
UTC seconds.Not present if the message's content has never been edited.Clients should use this field, rather than parsing theedit_historyarray, to display an indicator that the message has been edited.Changes: Prior to Zulip 10.0 (feature level 365), this was the
time when the message was last edited or moved.last_moved_timestamp:integerThe UNIX timestamp for when the message was last moved to a different
channel or topic, in UTC seconds.Not present if the message has never been moved, or if the only topic
moves for the message areresolving or unresolvingthe message's topic.Clients should use this field, rather than parsing theedit_historyarray, to display an indicator that the message has been moved.Changes: New in Zulip 10.0 (feature level 365). Previously,
parsing theedit_historyarray was required in order to correctly
display moved message indicators.reactions:(object)[]Data on anyreactionsto the message,
ordered chronologically from oldest to newest reaction.Changes: In Zulip 10.0 (feature level 328), the deprecateduserobject was removed from the data for each reaction. It contained the
following information about the user who added the reaction:id,email,full_nameandis_mirror_dummy.emoji_name:stringName of the emoji.emoji_code:stringA unique identifier, defining the specific emoji codepoint requested,
within the namespace of thereaction_type.reaction_type:stringA string indicating the type of emoji. Each emojireaction_typehas an independent namespace for values ofemoji_code.Must be one of the following values:unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").user_id:integerThe ID of the user who added the reaction.Changes: New in Zulip 3.0 (feature level 2), which
deprecated theuserobject.recipient_id:integerA unique ID for the set of users receiving the
message (either a channel or group of users). Useful primarily
for hashing.Changes: Before Zulip 10.0 (feature level 327),recipient_idwas the same across all incoming 1:1 direct messages. Now, each
incoming message uniquely shares arecipient_idwith outgoing
messages in the same conversation.sender_email:stringThe Zulip API email address of the message's sender.sender_full_name:stringThe full name of the message's sender.sender_id:integerThe user ID of the message's sender.sender_realm_str:stringA string identifier for the realm the sender is in. Unique only within
the context of a given Zulip server.E.g. onexample.zulip.com, this will beexample.stream_id:integerOnly present for channel messages; the ID of the channel.subject:stringThetopicof the message. Currently always""for direct messages,
though this could change if Zulip adds support for topics in direct
message conversations.The field name is a legacy holdover from when topics were
called "subjects" and will eventually change.For clients that don't support theempty_topic_nameclient capability,
the empty string value is replaced with the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse, for channel messages.Changes: Before Zulip 10.0 (feature level 334),empty_topic_nameclient capability didn't exist and empty string as the topic name for
channel messages wasn't allowed.submessages:(object)[]Data used for certain experimental Zulip integrations.msg_type:stringThe type of the message.content:stringThe new content of the submessage.message_id:integerThe ID of the message to which the submessage has been added.sender_id:integerThe ID of the user who sent the message.id:integerThe ID of the submessage.timestamp:integerThe UNIX timestamp for when the message was sent,
in UTC seconds.topic_links:(object)[]Data on any links to be included in thetopicline (these are generated bycustom linkification
filtersthat match content in the
message's topic.)Changes: This field contained a list of urls before
Zulip 4.0 (feature level 46).New in Zulip 3.0 (feature level 1). Previously, this field was calledsubject_links; clients are recommended to renamesubject_linkstotopic_linksif present for compatibility with older Zulip servers.text:stringThe original link text present in the topic.url:stringThe expanded target url which the link points to.type:stringThe type of the message:"stream"or"private".
- flags:(string)[]The user'smessage flagsfor the message.Clients should inspect the flags field rather than assuming that
new messages are unread;muted users, messages
sent by the current user, and more subtle scenarios can result
in a new message that the server has already marked as read for
the user.Changes: In Zulip 8.0 (feature level 224), thewildcard_mentionedflag was deprecated in favor of thestream_wildcard_mentionedandtopic_wildcard_mentionedflags. Thewildcard_mentionedflag exists
for backwards compatibility with older clients and equalsstream_wildcard_mentioned || topic_wildcard_mentioned. Clients
supporting older server versions should treat this field as a previous
name for thestream_wildcard_mentionedflag as topic wildcard mentions
were not available prior to this feature level.
- local_message_id:stringFor clients supportinglocal echo.
Only present iflocal_idandqueue_idwere passed by the
client when the message was sent to the server.The same unique string-format identifier chosen by the client to identify
the locally echoed message (which was the value passed as thelocal_idparameter). This lets the client know unambiguously that it should
replace the locally echoed message, rather than adding this new message
(which would be correct if the user had sent the new message from another
device).
- avatar_url:string | nullThe URL of the message sender's avatar. Can benullonly if
the current user has access to the sender's real email address
andclient_gravatarwastrue.Ifnull, then the sender has not uploaded an avatar in Zulip,
and the client can compute the gravatar URL by hashing the
sender's email address, which corresponds in this case to their
real email address.Changes: Before Zulip 7.0 (feature level 163), access to a
user's real email address was a realm-level setting. As of this
feature level,email_address_visibilityis a user setting.
- client:stringA Zulip "client" string, describing what Zulip client
sent the message.
- content:stringThe content/body of the message.
Whenapply_markdownis set, it will be in HTML format.SeeMarkdown message formattingfor details on Zulip's HTML format.
- content_type:stringThe HTTPcontent_typefor the message content. This
will betext/htmlortext/x-markdown, depending on
whetherapply_markdownwas set.See the help center article onmessage formattingfor details on Zulip-flavored Markdown.
- display_recipient:string | (object)[]Data on the recipient of the message;
either the name of a channel or a dictionary containing basic data on
the users who received the message.id:integerID of the user.email:stringZulip API email of the user.full_name:stringFull name of the user.is_mirror_dummy:booleanWhether the user is a mirror dummy.
- edit_history:(object)[]An array of objects, with each object documenting the
changes in a previous edit made to the message,
ordered chronologically from most recent to least recent
edit.Not present if the message has never been edited or moved,
or ifviewing message edit historyis not allowed in the organization.Every object will containuser_idandtimestamp.The other fields are optional, and will be present or not
depending on whether the channel, topic, and/or message
content were modified in the edit event. For example, if
only the topic was edited, onlyprev_topicandtopicwill be present in addition touser_idandtimestamp.Changes: In Zulip 10.0 (feature level 284), removed theprev_rendered_content_versionfield as it is an internal
server implementation detail not used by any client.prev_content:stringOnly present if message's content was edited.The content of the message immediately prior to this
edit event.prev_rendered_content:stringOnly present if message's content was edited.The rendered HTML representation ofprev_content.SeeMarkdown message formattingfor details on Zulip's HTML format.prev_stream:integerOnly present if message's channel was edited.The channel ID of the message immediately prior to this
edit event.Changes: New in Zulip 3.0 (feature level 1).prev_topic:stringOnly present if message's topic was edited.The topic of the message immediately prior to this
edit event.Changes: New in Zulip 5.0 (feature level 118).
Previously, this field was calledprev_subject;
clients are recommended to renameprev_subjecttoprev_topicif present for compatibility with
older Zulip servers.stream:integerOnly present if message's channel was edited.The ID of the channel containing the message
immediately after this edit event.Changes: New in Zulip 5.0 (feature level 118).timestamp:integerThe UNIX timestamp for the edit.topic:stringOnly present if message's topic was edited.The topic of the message immediately after this edit event.Changes: New in Zulip 5.0 (feature level 118).user_id:integer | nullThe ID of the user that made the edit.Will benullonly for edit history
events predating March 2017.Clients can display edit history events where this
isnullas modified by either the sender (for content
edits) or an unknown user (for topic edits).
- id:integerThe unique message ID. Messages should always be
displayed sorted by ID.
- is_me_message:booleanWhether the message is a/me status message
- last_edit_timestamp:integerThe UNIX timestamp for when the message's content was last edited, in
UTC seconds.Not present if the message's content has never been edited.Clients should use this field, rather than parsing theedit_historyarray, to display an indicator that the message has been edited.Changes: Prior to Zulip 10.0 (feature level 365), this was the
time when the message was last edited or moved.
- last_moved_timestamp:integerThe UNIX timestamp for when the message was last moved to a different
channel or topic, in UTC seconds.Not present if the message has never been moved, or if the only topic
moves for the message areresolving or unresolvingthe message's topic.Clients should use this field, rather than parsing theedit_historyarray, to display an indicator that the message has been moved.Changes: New in Zulip 10.0 (feature level 365). Previously,
parsing theedit_historyarray was required in order to correctly
display moved message indicators.
- reactions:(object)[]Data on anyreactionsto the message,
ordered chronologically from oldest to newest reaction.Changes: In Zulip 10.0 (feature level 328), the deprecateduserobject was removed from the data for each reaction. It contained the
following information about the user who added the reaction:id,email,full_nameandis_mirror_dummy.emoji_name:stringName of the emoji.emoji_code:stringA unique identifier, defining the specific emoji codepoint requested,
within the namespace of thereaction_type.reaction_type:stringA string indicating the type of emoji. Each emojireaction_typehas an independent namespace for values ofemoji_code.Must be one of the following values:unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").user_id:integerThe ID of the user who added the reaction.Changes: New in Zulip 3.0 (feature level 2), which
deprecated theuserobject.
- recipient_id:integerA unique ID for the set of users receiving the
message (either a channel or group of users). Useful primarily
for hashing.Changes: Before Zulip 10.0 (feature level 327),recipient_idwas the same across all incoming 1:1 direct messages. Now, each
incoming message uniquely shares arecipient_idwith outgoing
messages in the same conversation.
- sender_email:stringThe Zulip API email address of the message's sender.
- sender_full_name:stringThe full name of the message's sender.
- sender_id:integerThe user ID of the message's sender.
- sender_realm_str:stringA string identifier for the realm the sender is in. Unique only within
the context of a given Zulip server.E.g. onexample.zulip.com, this will beexample.
- stream_id:integerOnly present for channel messages; the ID of the channel.
- subject:stringThetopicof the message. Currently always""for direct messages,
though this could change if Zulip adds support for topics in direct
message conversations.The field name is a legacy holdover from when topics were
called "subjects" and will eventually change.For clients that don't support theempty_topic_nameclient capability,
the empty string value is replaced with the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse, for channel messages.Changes: Before Zulip 10.0 (feature level 334),empty_topic_nameclient capability didn't exist and empty string as the topic name for
channel messages wasn't allowed.
- submessages:(object)[]Data used for certain experimental Zulip integrations.msg_type:stringThe type of the message.content:stringThe new content of the submessage.message_id:integerThe ID of the message to which the submessage has been added.sender_id:integerThe ID of the user who sent the message.id:integerThe ID of the submessage.
- timestamp:integerThe UNIX timestamp for when the message was sent,
in UTC seconds.
- topic_links:(object)[]Data on any links to be included in thetopicline (these are generated bycustom linkification
filtersthat match content in the
message's topic.)Changes: This field contained a list of urls before
Zulip 4.0 (feature level 46).New in Zulip 3.0 (feature level 1). Previously, this field was calledsubject_links; clients are recommended to renamesubject_linkstotopic_linksif present for compatibility with older Zulip servers.text:stringThe original link text present in the topic.url:stringThe expanded target url which the link points to.
- type:stringThe type of the message:"stream"or"private".
- id:integerID of the user.
- email:stringZulip API email of the user.
- full_name:stringFull name of the user.
- is_mirror_dummy:booleanWhether the user is a mirror dummy.
- prev_content:stringOnly present if message's content was edited.The content of the message immediately prior to this
edit event.
- prev_rendered_content:stringOnly present if message's content was edited.The rendered HTML representation ofprev_content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- prev_stream:integerOnly present if message's channel was edited.The channel ID of the message immediately prior to this
edit event.Changes: New in Zulip 3.0 (feature level 1).
- prev_topic:stringOnly present if message's topic was edited.The topic of the message immediately prior to this
edit event.Changes: New in Zulip 5.0 (feature level 118).
Previously, this field was calledprev_subject;
clients are recommended to renameprev_subjecttoprev_topicif present for compatibility with
older Zulip servers.
- stream:integerOnly present if message's channel was edited.The ID of the channel containing the message
immediately after this edit event.Changes: New in Zulip 5.0 (feature level 118).
- timestamp:integerThe UNIX timestamp for the edit.
- topic:stringOnly present if message's topic was edited.The topic of the message immediately after this edit event.Changes: New in Zulip 5.0 (feature level 118).
- user_id:integer | nullThe ID of the user that made the edit.Will benullonly for edit history
events predating March 2017.Clients can display edit history events where this
isnullas modified by either the sender (for content
edits) or an unknown user (for topic edits).
- emoji_name:stringName of the emoji.
- emoji_code:stringA unique identifier, defining the specific emoji codepoint requested,
within the namespace of thereaction_type.
- reaction_type:stringA string indicating the type of emoji. Each emojireaction_typehas an independent namespace for values ofemoji_code.Must be one of the following values:unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").
- user_id:integerThe ID of the user who added the reaction.Changes: New in Zulip 3.0 (feature level 2), which
deprecated theuserobject.
- unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.
- realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.
- zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").
- msg_type:stringThe type of the message.
- content:stringThe new content of the submessage.
- message_id:integerThe ID of the message to which the submessage has been added.
- sender_id:integerThe ID of the user who sent the message.
- id:integerThe ID of the submessage.
- text:stringThe original link text present in the topic.
- url:stringThe expanded target url which the link points to.
Example

```
{"flags":[],"id":1,"message":{"avatar_url":null,"client":"test suite","content":"<p>First message ...<a href=\"user_uploads/2/ce/2Xpnnwgh8JWKxBXtTfD6BHKV/zulip.txt\">zulip.txt</a></p>","content_type":"text/html","display_recipient":"Denmark","id":31,"is_me_message":false,"reactions":[],"recipient_id":23,"sender_email":"user10@zulip.testserver","sender_full_name":"King Hamlet","sender_id":10,"sender_realm_str":"zulip","stream_id":1,"subject":"test","submessages":[],"timestamp":1594825416,"topic_links":[],"type":"stream"},"type":"message"}
```

```
{"flags":[],"id":1,"message":{"avatar_url":null,"client":"test suite","content":"<p>First message ...<a href=\"user_uploads/2/ce/2Xpnnwgh8JWKxBXtTfD6BHKV/zulip.txt\">zulip.txt</a></p>","content_type":"text/html","display_recipient":"Denmark","id":31,"is_me_message":false,"reactions":[],"recipient_id":23,"sender_email":"user10@zulip.testserver","sender_full_name":"King Hamlet","sender_id":10,"sender_realm_str":"zulip","stream_id":1,"subject":"test","submessages":[],"timestamp":1594825416,"topic_links":[],"type":"stream"},"type":"message"}
```

### has_zoom_token
Event sent to a user's clients when the user completes the OAuth flow
for theZoom integration. Clients need
to know whether initiating Zoom OAuth is required before creating a Zoom
call.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- value:booleanA boolean specifying whether the user has zoom
token or not.
Example

```
{"id":0,"type":"has_zoom_token","value":true}
```

```
{"id":0,"type":"has_zoom_token","value":true}
```

### invites_changed
A simple event sent when the set of invitations changes.
This event is sent to organization administrators and the creator of
the changed invitation; this tells clients they need to refetch
data fromGET /invitesif they are displaying UI containing active
invitations.
Changes: Before Zulip 8.0 (feature level 209), this event was
only sent to organization administrators.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
Example

```
{"id":0,"type":"invites_changed"}
```

```
{"id":0,"type":"invites_changed"}
```

### realm_userop: add
Event sent to all users in a Zulip organization when a new
user joins or when a guest user gains access to a user.
Processing this event is important to being able to display
basic details on other users given only their ID.
If the current user is a guest whose access to a newly created user
is limited by acan_access_all_users_grouppolicy, and the event
queue was registered with theuser_list_incompleteclient
capability, then the event queue will not receive an event for such
a new user. If a newly created user is inaccessible to the current
user via such a policy, but the client lacksuser_list_incompleteclient capability, then this event will be delivered to the queue,
with an "Unknown user" object with the usual format but placeholder
data whose only variable content is the user ID.
Changes: Before Zulip 8.0 (feature level 232), theuser_list_incompleteclient capability did not exist, and so all
clients whose access to a new user was prevented bycan_access_all_users_grouppolicy would receive a fake "Unknown
user" event for such a user.
Starting with Zulip 8.0 (feature level 228),
this event is also sent when a guest user gains access to
a user.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- person:objectA dictionary containing basic data on a given Zulip user.Changes: Removedis_billing_adminfield in Zulip 10.0 (feature level 363), as it was
replaced by thecan_manage_billing_grouprealm setting.user_id:integerThe unique ID of the user.delivery_email:string | nullThe user's real email address. This value will benullif you cannot
access user's real email address. For bot users, this field is always
set to the real email of the bot, because bot users always haveemail_address_visibilityset to everyone.Changes: Prior to Zulip 7.0 (feature level 163), this field was
present only whenemail_address_visibilitywas restricted and you had
access to the user's real email. As of this feature level, this field
is always present, including the case whenemail_address_visibilityis set to everyone (and therefore not restricted).email:stringThe Zulip API email address of the user or bot.If you do not have permission to view the email address of the target user,
this will be a fake email address that is usable for the Zulip API but nothing else.full_name:stringFull name of the user or bot, used for all display purposes.date_joined:stringThe time when the user joined. For users imported from other
applications and users created via the API, this is set to the
account creation time until the user logs in for the first time,
after which it is updated to that login time.For imported users, clients can use theis_imported_stubflag
to determine how to display this field: whenis_imported_stubistrue, the user has not yet logged in and this value is the
account creation time during import; whenis_imported_stubisfalse, this value reflects when the user first logged in.Changes: Starting with Zulip 12.0 (feature level 475),
this field is updated when an imported stub user or a user created
via the API logs in for the first time.is_active:booleanA boolean specifying whether the user account has been deactivated.is_owner:booleanA boolean specifying whether the user is an organization owner.
If true,is_adminwill also be true.Changes: New in Zulip 3.0 (feature level 8).is_admin:booleanA boolean specifying whether the user is an organization administrator.is_guest:booleanA boolean specifying whether the user is a guest user.is_bot:booleanA boolean specifying whether the user is a bot or full account.bot_type:integer | nullAn integer describing the type of bot:nullif the user isn't a bot.1for aGenericbot.2for anIncoming webhookbot.3for anOutgoing webhookbot.4for anEmbeddedbot.bot_owner_id:integer | nullIf the user is a bot (i.e.is_botis true), thenbot_owner_idis the user ID of the bot's owner (usually, whoever created the bot).Will benullfor legacy bots that do not have an owner.Changes: New in Zulip 3.0 (feature level 1). In previous
versions, there was abot_ownerfield containing the email
address of the bot's owner.role:integerOrganization-level roleof the user.
Possible values are:100 = Organization owner200 = Organization administrator300 = Organization moderator400 = Member600 = GuestChanges: New in Zulip 4.0 (feature level 59).timezone:stringThe IANA identifier of the user'sprofile time zone,
which is used primarily to display the user's local time to other users.avatar_url:string | nullURL for the user's avatar.Will benullif theclient_gravatarquery parameter was set totrue, the current user has access to
this user's real email address, and this user's avatar is hosted by
the Gravatar provider (i.e. this user has never uploaded an avatar).Changes: Before Zulip 7.0 (feature level 163), access to a
user's real email address was a realm-level setting. As of this
feature level,email_address_visibilityis a user setting.In Zulip 3.0 (feature level 18), if the client has theuser_avatar_url_field_optionalcapability, this will be missing at
the server's sole discretion.avatar_version:integerVersion for the user's avatar. Used for cache-busting requests
for the user's avatar. Clients generally shouldn't need to use this;
most avatar URLs sent by Zulip will already end with?v={avatar_version}.is_imported_stub:booleanIndicates whether this user object is a stub account imported from
another chat system. Stub accounts are used to represent the senders
for imported messages. Stub accounts can be converted to regular Zulip
accounts when the user starts using Zulip, preserving that imported
user's message history.Changes: New in Zulip 12.0 (feature level 433).profile_data:objectOnly present ifis_botis false; bots can't have custom profile fields.A dictionary containing custom profile field data for the user. Each entry
maps the integer ID of a custom profile field in the organization to a
dictionary containing the user's data for that field. Generally the data
includes just a singlevaluekey; for those custom profile fields
supporting Markdown, arendered_valuekey will also be present.{id}:objectObject with data about what value the user filled in the custom
profile field with that ID.value:stringUser's personal value for this custom profile field.rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- user_id:integerThe unique ID of the user.
- delivery_email:string | nullThe user's real email address. This value will benullif you cannot
access user's real email address. For bot users, this field is always
set to the real email of the bot, because bot users always haveemail_address_visibilityset to everyone.Changes: Prior to Zulip 7.0 (feature level 163), this field was
present only whenemail_address_visibilitywas restricted and you had
access to the user's real email. As of this feature level, this field
is always present, including the case whenemail_address_visibilityis set to everyone (and therefore not restricted).
- email:stringThe Zulip API email address of the user or bot.If you do not have permission to view the email address of the target user,
this will be a fake email address that is usable for the Zulip API but nothing else.
- full_name:stringFull name of the user or bot, used for all display purposes.
- date_joined:stringThe time when the user joined. For users imported from other
applications and users created via the API, this is set to the
account creation time until the user logs in for the first time,
after which it is updated to that login time.For imported users, clients can use theis_imported_stubflag
to determine how to display this field: whenis_imported_stubistrue, the user has not yet logged in and this value is the
account creation time during import; whenis_imported_stubisfalse, this value reflects when the user first logged in.Changes: Starting with Zulip 12.0 (feature level 475),
this field is updated when an imported stub user or a user created
via the API logs in for the first time.
- is_active:booleanA boolean specifying whether the user account has been deactivated.
- is_owner:booleanA boolean specifying whether the user is an organization owner.
If true,is_adminwill also be true.Changes: New in Zulip 3.0 (feature level 8).
- is_admin:booleanA boolean specifying whether the user is an organization administrator.
- is_guest:booleanA boolean specifying whether the user is a guest user.
- is_bot:booleanA boolean specifying whether the user is a bot or full account.
- bot_type:integer | nullAn integer describing the type of bot:nullif the user isn't a bot.1for aGenericbot.2for anIncoming webhookbot.3for anOutgoing webhookbot.4for anEmbeddedbot.
- bot_owner_id:integer | nullIf the user is a bot (i.e.is_botis true), thenbot_owner_idis the user ID of the bot's owner (usually, whoever created the bot).Will benullfor legacy bots that do not have an owner.Changes: New in Zulip 3.0 (feature level 1). In previous
versions, there was abot_ownerfield containing the email
address of the bot's owner.
- role:integerOrganization-level roleof the user.
Possible values are:100 = Organization owner200 = Organization administrator300 = Organization moderator400 = Member600 = GuestChanges: New in Zulip 4.0 (feature level 59).
- timezone:stringThe IANA identifier of the user'sprofile time zone,
which is used primarily to display the user's local time to other users.
- avatar_url:string | nullURL for the user's avatar.Will benullif theclient_gravatarquery parameter was set totrue, the current user has access to
this user's real email address, and this user's avatar is hosted by
the Gravatar provider (i.e. this user has never uploaded an avatar).Changes: Before Zulip 7.0 (feature level 163), access to a
user's real email address was a realm-level setting. As of this
feature level,email_address_visibilityis a user setting.In Zulip 3.0 (feature level 18), if the client has theuser_avatar_url_field_optionalcapability, this will be missing at
the server's sole discretion.
- avatar_version:integerVersion for the user's avatar. Used for cache-busting requests
for the user's avatar. Clients generally shouldn't need to use this;
most avatar URLs sent by Zulip will already end with?v={avatar_version}.
- is_imported_stub:booleanIndicates whether this user object is a stub account imported from
another chat system. Stub accounts are used to represent the senders
for imported messages. Stub accounts can be converted to regular Zulip
accounts when the user starts using Zulip, preserving that imported
user's message history.Changes: New in Zulip 12.0 (feature level 433).
- profile_data:objectOnly present ifis_botis false; bots can't have custom profile fields.A dictionary containing custom profile field data for the user. Each entry
maps the integer ID of a custom profile field in the organization to a
dictionary containing the user's data for that field. Generally the data
includes just a singlevaluekey; for those custom profile fields
supporting Markdown, arendered_valuekey will also be present.{id}:objectObject with data about what value the user filled in the custom
profile field with that ID.value:stringUser's personal value for this custom profile field.rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- nullif the user isn't a bot.
- 1for aGenericbot.
- 2for anIncoming webhookbot.
- 3for anOutgoing webhookbot.
- 4for anEmbeddedbot.
- 100 = Organization owner
- 200 = Organization administrator
- 300 = Organization moderator
- 400 = Member
- 600 = Guest
- {id}:objectObject with data about what value the user filled in the custom
profile field with that ID.value:stringUser's personal value for this custom profile field.rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- value:stringUser's personal value for this custom profile field.
- rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
Example

```
{"id":0,"op":"add","person":{"avatar_url":"https://secure.gravatar.com/avatar/c6b5578d4964bd9c5fae593c6868912a?d=identicon&version=1","avatar_version":1,"date_joined":"2020-07-15T15:04:02.030833+00:00","delivery_email":null,"email":"foo@zulip.com","full_name":"full name","is_active":true,"is_admin":false,"is_bot":false,"is_guest":false,"is_imported_stub":false,"is_owner":false,"profile_data":{},"role":400,"timezone":"","user_id":38},"type":"realm_user"}
```

```
{"id":0,"op":"add","person":{"avatar_url":"https://secure.gravatar.com/avatar/c6b5578d4964bd9c5fae593c6868912a?d=identicon&version=1","avatar_version":1,"date_joined":"2020-07-15T15:04:02.030833+00:00","delivery_email":null,"email":"foo@zulip.com","full_name":"full name","is_active":true,"is_admin":false,"is_bot":false,"is_guest":false,"is_imported_stub":false,"is_owner":false,"profile_data":{},"role":400,"timezone":"","user_id":38},"type":"realm_user"}
```

### realm_userop: remove
Event sent to guest users when they lose access to a user.
Changes: As of Zulip 8.0 (feature level 228), this event is no
longer deprecated.
In Zulip 8.0 (feature level 222), this event was deprecated and no
longer sent to clients. Prior to this feature level, it was sent to all
users in a Zulip organization when a user was deactivated.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- person:objectObject containing details of the deactivated user.user_id:integerThe ID of the deactivated user.full_name:stringThe full name of the user.Deprecated: We expect to remove this field in the future.
- user_id:integerThe ID of the deactivated user.
- full_name:stringThe full name of the user.Deprecated: We expect to remove this field in the future.
Example

```
{"id":0,"op":"remove","person":{"full_name":"Foo Bot","user_id":35},"type":"realm_user"}
```

```
{"id":0,"op":"remove","person":{"full_name":"Foo Bot","user_id":35},"type":"realm_user"}
```

### presence
Event sent to all users in an organization when a user comes back
online after being offline for a while.
In addition to handling these events, a client that wants to
maintain presence data must poll themain presence
endpoint. Most updates to
presence data, refreshing the timestamps of users who are already
online, do not appear in the event queue. This design is an
optimization by allowing those updates to be batched up, because
there is no urgency in the information that an already-online user
is still online.
These events are provided because when a user transitions from
offline to online, that is information the client may want to show
promptly in the UI to avoid showing a confusing state (for example,
if the newly-online user sends a message or otherwise demonstrates
they're online).
If the client supports thesimplified_presence_eventsclient
capability,
these events will include thepresencesfield, which provides the
modified user's presence data in the modern format. Clients are
strongly encouraged to implement this client capability, as legacy
format support will be removed in a future release.
If theCAN_ACCESS_ALL_USERS_GROUP_LIMITS_PRESENCEserver-level
setting is set totrue, then the event is only sent to users
who can access the user who came back online.
Changes: Prior to Zulip 11.0 (feature level 419), thesimplified_presence_eventsclient capability did not exist.
Therefore, all events were in the legacy format, and did not
include thepresencesfield.
Prior to Zulip 8.0 (feature level 228), this event was sent to all
users in the organization.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- presences:objectOnly present for clients that support thesimplified_presence_eventsclient capability.A dictionary mapping user IDs to the presence data (modern
format) for the modified user(s). Clients should support
updating multiple users in a single event.Changes: New in Zulip 11.0 (feature level 419).{user_id}:objectPresence data (modern format) for the user with
the specified ID.active_timestamp:integerThe UNIX timestamp of the last time a client connected
to Zulip reported that the user was actually present
(e.g. via focusing a browser window or interacting
with a computer running the desktop app).Clients should display users with a currentactive_timestampas fully present.idle_timestamp:integerThe UNIX timestamp of the last time the user had a
client connected to Zulip, including idle clients
where the user hasn't interacted with the system
recently.The Zulip server has no way of distinguishing whether
an idle web app user is at their computer, but hasn't
interacted with the Zulip tab recently, or simply left
their desktop computer on when they left.Thus, clients should display users with a currentidle_timestampbut no currentactive_timestampas
potentially present.
- user_id:integerNot present for clients that support thesimplified_presence_eventsclient capability.The ID of the modified user.
- email:stringNot present for clients that support thesimplified_presence_eventsclient capability.The Zulip API email of the user.Deprecated: This field will be removed in a future
release as it is redundant with theuser_id.
- server_timestamp:numberNot present for clients that support thesimplified_presence_eventsclient capability.The timestamp of when the Zulip server received the user's
presence as a UNIX timestamp.
- presence:objectNot present for clients that support thesimplified_presence_eventsclient capability.Object containing the presence data (legacy format) of of the modified
user.{client_name}:objectObject containing the details of the user's
presence.Changes: Starting with Zulip 7.0 (feature level 178), this
will always be"website"as the server no longer stores which
client submitted presence updates.Previously, the object key was the client's platform name, for
examplewebsiteorZulipDesktop.client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this
will always be"website"as the server no longer stores which
client submitted presence updates.status:stringThe status of the user on this client. Will be eitheridleoractive.timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Changes: Starting with Zulip 7.0 (feature level 178), this
will always befalseas the server no longer stores which
client submitted presence updates.
- {user_id}:objectPresence data (modern format) for the user with
the specified ID.active_timestamp:integerThe UNIX timestamp of the last time a client connected
to Zulip reported that the user was actually present
(e.g. via focusing a browser window or interacting
with a computer running the desktop app).Clients should display users with a currentactive_timestampas fully present.idle_timestamp:integerThe UNIX timestamp of the last time the user had a
client connected to Zulip, including idle clients
where the user hasn't interacted with the system
recently.The Zulip server has no way of distinguishing whether
an idle web app user is at their computer, but hasn't
interacted with the Zulip tab recently, or simply left
their desktop computer on when they left.Thus, clients should display users with a currentidle_timestampbut no currentactive_timestampas
potentially present.
- active_timestamp:integerThe UNIX timestamp of the last time a client connected
to Zulip reported that the user was actually present
(e.g. via focusing a browser window or interacting
with a computer running the desktop app).Clients should display users with a currentactive_timestampas fully present.
- idle_timestamp:integerThe UNIX timestamp of the last time the user had a
client connected to Zulip, including idle clients
where the user hasn't interacted with the system
recently.The Zulip server has no way of distinguishing whether
an idle web app user is at their computer, but hasn't
interacted with the Zulip tab recently, or simply left
their desktop computer on when they left.Thus, clients should display users with a currentidle_timestampbut no currentactive_timestampas
potentially present.
- {client_name}:objectObject containing the details of the user's
presence.Changes: Starting with Zulip 7.0 (feature level 178), this
will always be"website"as the server no longer stores which
client submitted presence updates.Previously, the object key was the client's platform name, for
examplewebsiteorZulipDesktop.client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this
will always be"website"as the server no longer stores which
client submitted presence updates.status:stringThe status of the user on this client. Will be eitheridleoractive.timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Changes: Starting with Zulip 7.0 (feature level 178), this
will always befalseas the server no longer stores which
client submitted presence updates.
- client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this
will always be"website"as the server no longer stores which
client submitted presence updates.
- status:stringThe status of the user on this client. Will be eitheridleoractive.
- timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.
- pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Changes: Starting with Zulip 7.0 (feature level 178), this
will always befalseas the server no longer stores which
client submitted presence updates.
Example

```
{"email":"user10@zulip.testserver","id":0,"presence":{"website":{"client":"website","pushable":false,"status":"idle","timestamp":1594825445}},"server_timestamp":1594825445.3200784,"type":"presence","user_id":10}
```

```
{"email":"user10@zulip.testserver","id":0,"presence":{"website":{"client":"website","pushable":false,"status":"idle","timestamp":1594825445}},"server_timestamp":1594825445.3200784,"type":"presence","user_id":10}
```

### streamop: create
Event sent when a new channel is created to users who can see
the new channel exists (for private channels, only subscribers and
organization administrators will receive this event).
This event is also sent when a user gains access to a channel they
previouslycould not access, such as
when theirrolechanges, a
private channel is made public, or a guest user is subscribed
to a public (or private) channel.
This event is also sent when a channel is unarchived but only
to clients that did not declare thearchived_channelsclient
capability.
Note that organization administrators who are not subscribed will
not be able to see content on the channel; just that it exists.
Changes: Prior to Zulip 11.0 (feature level 378), this
event was sent to all the users who could see the channel when it
was unarchived.
Prior to Zulip 8.0 (feature level 220), this event was incorrectly
not sent to guest users a web-public channel was created.
Prior to Zulip 8.0 (feature level 205), this event was not sent
when a user gained access to a channel due to their role changing.
Prior to Zulip 8.0 (feature level 192), this event was not sent
when guest users gained access to a public channel by being
subscribed.
Prior to Zulip 6.0 (feature level 134), this event was not sent
when a private channel was made public.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- streams:(object)[]Array of objects, each containing
details about the newly added channel(s).stream_id:integerThe unique ID of the channel.name:stringThe name of the channel.is_archived:booleanA boolean indicating whether the channel isarchived.Changes: New in Zulip 10.0 (feature level 315).
Previously, this endpoint never returned archived channels.description:stringThe short description of the channel inZulip-flavored Markdownformat,
intended to be used to prepopulate UI for editing a channel's
description.SeeMarkdown message formattingfor details on Zulip's HTML format.date_created:integerThe UNIX timestamp for when the channel was created, in UTC seconds.Changes: New in Zulip 4.0 (feature level 30).creator_id:integer | nullThe ID of the user who created this channel.Anullvalue means the channel has no recorded creator, which is often
because the channel is very old, was created during realm creation or
because it was created via a data import tool ormanagement command.Changes: New in Zulip 9.0 (feature level 254).invite_only:booleanSpecifies whether the channel is private or not.
Only people who have been invited can access a private channel.rendered_description:stringThe short description of the channel rendered as HTML, intended to
be used when displaying the channel description in a UI.One should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax
work correctly. And any client-side security logic for
user-generated message content should be applied when displaying
this HTML as though it were the body of a Zulip message.is_web_public:booleanWhether the channel has been configured to allow unauthenticated
access to its message history from the web.Changes: New in Zulip 2.1.0.stream_post_policy:integerA deprecated representation of a superset of the users who
have permission to post messages to the channel available
for backwards-compatibility. Clients should usecan_send_message_groupinstead.It is an enum with the following possible values, corresponding
to roles/system groups:1 = Any user can post.2 = Only administrators can post.3 = Onlyfull memberscan post.4 = Only moderators can post.Changes: Deprecated in Zulip 10.0 (feature level 333) and
replaced bycan_send_message_group, which supports finer
resolution of configurations, resulting in this property being
inaccurate following that transition.New in Zulip 3.0 (feature level 1), replacing the previousis_announcement_onlyboolean.message_retention_days:integer | nullNumber of days that messages sent to this channel will be stored
before being automatically deleted by themessage retention
policy. There are two special values:null, the default, means the channel will inherit the organization
  level setting.-1encodes retaining messages in this channel forever.Changes: New in Zulip 3.0 (feature level 17).history_public_to_subscribers:booleanWhether the history of the channel is public to its subscribers.Currently always true for public channels (i.e."invite_only": falseimplies"history_public_to_subscribers": true), but clients should not make that
assumption, as we may change that behavior in the future.topics_policy:stringWhethernamed topicsand the empty
topic (i.e.,"general chat" topic)
are enabled in this channel."inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty topic in this
  channel."allow_empty_topic": Messages can be sent to both named topics and
  the empty topic in this channel."disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty topic is disabled."empty_topic_only": Messages can be sent to the empty topic in this
  channel, but named topics are disabled. See"general chat"
  channels.The"empty_topic_only"policy can only be set if all existing messages
in the channel are already in the empty topic.When creating a new channel, if thetopics_policyis not specified, the"inherit"option will be set.Changes: In Zulip 11.0 (feature level 404), the"empty_topic_only"option was added.New in Zulip 11.0 (feature level 392).first_message_id:integer | nullThe ID of the first message in the channel.Intended to help clients determine whether they need to display
UI like the "show all topics" widget that would suggest the channel
has older history that can be accessed.Isnullfor channels with no message history.Changes: New in Zulip 2.1.0.folder_id:integer | nullThe ID of the folder to which the channel belongs.Isnullif channel does not belong to any folder.Changes: New in Zulip 11.0 (feature level 389).is_recently_active:booleanWhether the channel has recent message activity. Clients should use this to implementhide inactive channelsifdemote_inactive_streamsis enabled.Changes: New in Zulip 10.0 (feature level 323). Previously, clients implemented the
demote_inactive_streams from local message history, resulting in a choppy loading
experience.is_announcement_only:booleanWhether the given channel is announcement only or not.Changes: Deprecated in Zulip 3.0 (feature level 1). Clients
should usestream_post_policyinstead.can_add_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to add subscribers to this channel.Users who can administer the channel or have similar realm-level
permissions can add subscribers to a public channel regardless
of the value of this setting.Users in this group need not be subscribed to a private channel to
add subscribers to it.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 342). Previously, there was no
channel-level setting for this permission.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_remove_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to remove subscribers from this channel.Organization administrators can unsubscribe others from a channel as though
they were in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349), channel administrators
could not unsubscribe other users if they were not an organization
administrator or part ofcan_remove_subscribers_group. Realm administrators
were not allowed to unsubscribe other users from a private channel if they
were not subscribed to that channel.Prior to Zulip 10.0 (feature level 320), this value was always the integer
ID of a system group.Before Zulip 8.0 (feature level 197), thecan_remove_subscribers_groupsetting was namedcan_remove_subscribers_group_id.New in Zulip 6.0 (feature level 142).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_administer_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to administer this channel.Organization administrators can administer every channel as though they were
in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349) a user needed tohave content accessto a channel in
order to modify it. The exception to this rule was that organization
administrators can edit channel names and descriptions without
having full access to the channel.New in Zulip 10.0 (feature level 325). Prior to this
change, the permission to administer channels was limited to realm
administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_delete_any_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete any message in the channel.Note that a user musthave content accessto a
channel in order to delete any message in the channel.Users present in the organization-levelcan_delete_any_message_groupsetting can always delete any message in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users incan_delete_any_message_groupwere able
delete any message in the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_delete_own_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete the messages that they have sent in the channel.Note that a user musthave content accessto a
channel in order to delete their own message in the channel.Users with permission to delete any message in the channel
and users present in the organization-levelcan_delete_own_message_groupsetting
can always delete their own messages in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users in the organization-levelcan_delete_any_message_groupandcan_delete_own_message_groupsettings were able delete their own messages in
the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_move_messages_out_of_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages out of this channel.Note that a user musthave content accessto a
channel in order to move messages out of the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_channels_groupsetting can always move messages
out of the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_channels_groupwere able
move messages between channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_move_messages_within_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages within this channel.Note that a user musthave content accessto a
channel in order to move messages within the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_topics_groupsetting can always move messages
within the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_topics_groupwere able
move messages between topics of a channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_send_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to post in this channel.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Note that using this permission to send a message to a new topic requires
also having permission to create new topics in the channel.Changes: New in Zulip 10.0 (feature level 333). Previouslystream_post_policyfield used to control the permission to
post in the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_subscribe_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to subscribe themselves to this channel.Everyone, excluding guests, can subscribe to any public channel
irrespective of this setting.Users in this group can subscribe to a private channel as well.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 357).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_resolve_topics_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to resolve topics in the channel.Users who have similar realm-level permissions can resolve topics
in a channel regardless of the value of this setting.Changes: New in Zulip 11.0 (feature level 402).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_create_topic_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to create a new topic in this channel.Note that using this permission requires also having permission to
send messages in the channel.Note that this must be therole:everyonesystem groupforprivate channels with protected history.Changes: New in Zulip 12.0 (feature level 441). Previously,
if you could send messages in a channel, you could create topics in
the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.subscriber_count:numberThe total number of non-deactivated users (including bots) who
are subscribed to the channel. Clients are responsible for updating
this value usingpeer_addandpeer_removeevents.The server's internals cannot guarantee this value is correctly
synced withpeer_addandpeer_removeevents for the channel. As
a result, if a (rare) race occurs between a change in the channel's
subscribers and fetching this value, it is possible for a client
that is correctly following the events protocol to end up with a
permanently off-by-one error in the channel's subscriber count.Clients are recommended to fetch full subscriber data for a channel
in contexts where it is important to avoid this risk. The official
web application, for example, uses this field primarily while
waiting to fetch a given channel's full subscriber list from the
server.Changes: New in Zulip 11.0 (feature level 394).stream_weekly_traffic:integer | nullThe average number of messages sent to the channel per week, as
estimated based on recent weeks, rounded to the nearest integer.Ifnull, no information is provided on the average traffic.
This can be because the channel was recently created and there
is insufficient data to make an estimate, or because the server
wishes to omit this information for this client, this realm, or
this endpoint or type of event.Changes: New in Zulip 8.0 (feature level 199). Previously, this
statistic was available only in subscription objects.
- stream_id:integerThe unique ID of the channel.
- name:stringThe name of the channel.
- is_archived:booleanA boolean indicating whether the channel isarchived.Changes: New in Zulip 10.0 (feature level 315).
Previously, this endpoint never returned archived channels.
- description:stringThe short description of the channel inZulip-flavored Markdownformat,
intended to be used to prepopulate UI for editing a channel's
description.SeeMarkdown message formattingfor details on Zulip's HTML format.
- date_created:integerThe UNIX timestamp for when the channel was created, in UTC seconds.Changes: New in Zulip 4.0 (feature level 30).
- creator_id:integer | nullThe ID of the user who created this channel.Anullvalue means the channel has no recorded creator, which is often
because the channel is very old, was created during realm creation or
because it was created via a data import tool ormanagement command.Changes: New in Zulip 9.0 (feature level 254).
- invite_only:booleanSpecifies whether the channel is private or not.
Only people who have been invited can access a private channel.
- rendered_description:stringThe short description of the channel rendered as HTML, intended to
be used when displaying the channel description in a UI.One should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax
work correctly. And any client-side security logic for
user-generated message content should be applied when displaying
this HTML as though it were the body of a Zulip message.
- is_web_public:booleanWhether the channel has been configured to allow unauthenticated
access to its message history from the web.Changes: New in Zulip 2.1.0.
- stream_post_policy:integerA deprecated representation of a superset of the users who
have permission to post messages to the channel available
for backwards-compatibility. Clients should usecan_send_message_groupinstead.It is an enum with the following possible values, corresponding
to roles/system groups:1 = Any user can post.2 = Only administrators can post.3 = Onlyfull memberscan post.4 = Only moderators can post.Changes: Deprecated in Zulip 10.0 (feature level 333) and
replaced bycan_send_message_group, which supports finer
resolution of configurations, resulting in this property being
inaccurate following that transition.New in Zulip 3.0 (feature level 1), replacing the previousis_announcement_onlyboolean.
- message_retention_days:integer | nullNumber of days that messages sent to this channel will be stored
before being automatically deleted by themessage retention
policy. There are two special values:null, the default, means the channel will inherit the organization
  level setting.-1encodes retaining messages in this channel forever.Changes: New in Zulip 3.0 (feature level 17).
- history_public_to_subscribers:booleanWhether the history of the channel is public to its subscribers.Currently always true for public channels (i.e."invite_only": falseimplies"history_public_to_subscribers": true), but clients should not make that
assumption, as we may change that behavior in the future.
- topics_policy:stringWhethernamed topicsand the empty
topic (i.e.,"general chat" topic)
are enabled in this channel."inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty topic in this
  channel."allow_empty_topic": Messages can be sent to both named topics and
  the empty topic in this channel."disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty topic is disabled."empty_topic_only": Messages can be sent to the empty topic in this
  channel, but named topics are disabled. See"general chat"
  channels.The"empty_topic_only"policy can only be set if all existing messages
in the channel are already in the empty topic.When creating a new channel, if thetopics_policyis not specified, the"inherit"option will be set.Changes: In Zulip 11.0 (feature level 404), the"empty_topic_only"option was added.New in Zulip 11.0 (feature level 392).
- first_message_id:integer | nullThe ID of the first message in the channel.Intended to help clients determine whether they need to display
UI like the "show all topics" widget that would suggest the channel
has older history that can be accessed.Isnullfor channels with no message history.Changes: New in Zulip 2.1.0.
- folder_id:integer | nullThe ID of the folder to which the channel belongs.Isnullif channel does not belong to any folder.Changes: New in Zulip 11.0 (feature level 389).
- is_recently_active:booleanWhether the channel has recent message activity. Clients should use this to implementhide inactive channelsifdemote_inactive_streamsis enabled.Changes: New in Zulip 10.0 (feature level 323). Previously, clients implemented the
demote_inactive_streams from local message history, resulting in a choppy loading
experience.
- is_announcement_only:booleanWhether the given channel is announcement only or not.Changes: Deprecated in Zulip 3.0 (feature level 1). Clients
should usestream_post_policyinstead.
- can_add_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to add subscribers to this channel.Users who can administer the channel or have similar realm-level
permissions can add subscribers to a public channel regardless
of the value of this setting.Users in this group need not be subscribed to a private channel to
add subscribers to it.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 342). Previously, there was no
channel-level setting for this permission.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_remove_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to remove subscribers from this channel.Organization administrators can unsubscribe others from a channel as though
they were in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349), channel administrators
could not unsubscribe other users if they were not an organization
administrator or part ofcan_remove_subscribers_group. Realm administrators
were not allowed to unsubscribe other users from a private channel if they
were not subscribed to that channel.Prior to Zulip 10.0 (feature level 320), this value was always the integer
ID of a system group.Before Zulip 8.0 (feature level 197), thecan_remove_subscribers_groupsetting was namedcan_remove_subscribers_group_id.New in Zulip 6.0 (feature level 142).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_administer_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to administer this channel.Organization administrators can administer every channel as though they were
in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349) a user needed tohave content accessto a channel in
order to modify it. The exception to this rule was that organization
administrators can edit channel names and descriptions without
having full access to the channel.New in Zulip 10.0 (feature level 325). Prior to this
change, the permission to administer channels was limited to realm
administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_delete_any_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete any message in the channel.Note that a user musthave content accessto a
channel in order to delete any message in the channel.Users present in the organization-levelcan_delete_any_message_groupsetting can always delete any message in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users incan_delete_any_message_groupwere able
delete any message in the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_delete_own_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete the messages that they have sent in the channel.Note that a user musthave content accessto a
channel in order to delete their own message in the channel.Users with permission to delete any message in the channel
and users present in the organization-levelcan_delete_own_message_groupsetting
can always delete their own messages in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users in the organization-levelcan_delete_any_message_groupandcan_delete_own_message_groupsettings were able delete their own messages in
the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_move_messages_out_of_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages out of this channel.Note that a user musthave content accessto a
channel in order to move messages out of the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_channels_groupsetting can always move messages
out of the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_channels_groupwere able
move messages between channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_move_messages_within_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages within this channel.Note that a user musthave content accessto a
channel in order to move messages within the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_topics_groupsetting can always move messages
within the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_topics_groupwere able
move messages between topics of a channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_send_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to post in this channel.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Note that using this permission to send a message to a new topic requires
also having permission to create new topics in the channel.Changes: New in Zulip 10.0 (feature level 333). Previouslystream_post_policyfield used to control the permission to
post in the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_subscribe_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to subscribe themselves to this channel.Everyone, excluding guests, can subscribe to any public channel
irrespective of this setting.Users in this group can subscribe to a private channel as well.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 357).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_resolve_topics_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to resolve topics in the channel.Users who have similar realm-level permissions can resolve topics
in a channel regardless of the value of this setting.Changes: New in Zulip 11.0 (feature level 402).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_create_topic_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to create a new topic in this channel.Note that using this permission requires also having permission to
send messages in the channel.Note that this must be therole:everyonesystem groupforprivate channels with protected history.Changes: New in Zulip 12.0 (feature level 441). Previously,
if you could send messages in a channel, you could create topics in
the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- subscriber_count:numberThe total number of non-deactivated users (including bots) who
are subscribed to the channel. Clients are responsible for updating
this value usingpeer_addandpeer_removeevents.The server's internals cannot guarantee this value is correctly
synced withpeer_addandpeer_removeevents for the channel. As
a result, if a (rare) race occurs between a change in the channel's
subscribers and fetching this value, it is possible for a client
that is correctly following the events protocol to end up with a
permanently off-by-one error in the channel's subscriber count.Clients are recommended to fetch full subscriber data for a channel
in contexts where it is important to avoid this risk. The official
web application, for example, uses this field primarily while
waiting to fetch a given channel's full subscriber list from the
server.Changes: New in Zulip 11.0 (feature level 394).
- stream_weekly_traffic:integer | nullThe average number of messages sent to the channel per week, as
estimated based on recent weeks, rounded to the nearest integer.Ifnull, no information is provided on the average traffic.
This can be because the channel was recently created and there
is insufficient data to make an estimate, or because the server
wishes to omit this information for this client, this realm, or
this endpoint or type of event.Changes: New in Zulip 8.0 (feature level 199). Previously, this
statistic was available only in subscription objects.
- 1 = Any user can post.
- 2 = Only administrators can post.
- 3 = Onlyfull memberscan post.
- 4 = Only moderators can post.
- null, the default, means the channel will inherit the organization
  level setting.
- -1encodes retaining messages in this channel forever.
- "inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty topic in this
  channel.
- "allow_empty_topic": Messages can be sent to both named topics and
  the empty topic in this channel.
- "disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty topic is disabled.
- "empty_topic_only": Messages can be sent to the empty topic in this
  channel, but named topics are disabled. See"general chat"
  channels.

```
realm_topics_policy
```
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
Example

```
{"id":0,"op":"create","streams":[{"can_add_subscribers_group":2,"can_remove_subscribers_group":2,"can_subscribe_group":2,"creator_id":11,"date_created":1691057093,"description":"","first_message_id":null,"folder_id":1,"history_public_to_subscribers":false,"invite_only":true,"is_announcement_only":false,"is_archived":false,"is_recently_active":true,"is_web_public":false,"message_retention_days":null,"name":"private","rendered_description":"","stream_id":12,"stream_post_policy":1,"stream_weekly_traffic":null,"subscriber_count":0}],"type":"stream"}
```

```
{"id":0,"op":"create","streams":[{"can_add_subscribers_group":2,"can_remove_subscribers_group":2,"can_subscribe_group":2,"creator_id":11,"date_created":1691057093,"description":"","first_message_id":null,"folder_id":1,"history_public_to_subscribers":false,"invite_only":true,"is_announcement_only":false,"is_archived":false,"is_recently_active":true,"is_web_public":false,"message_retention_days":null,"name":"private","rendered_description":"","stream_id":12,"stream_post_policy":1,"stream_weekly_traffic":null,"subscriber_count":0}],"type":"stream"}
```

### streamop: delete
Event sent when a user loses access to a channel they previouslycould accessbecause they are
unsubscribed from a private channel or theirrolehas changed.
This event is also sent when a channel is archived but only
to clients that did not declare thearchived_channelsclient
capability.
Changes: Prior to Zulip 11.0 (feature level 378), this
event was sent to all the users who could see the channel when it
was archived.
Prior to Zulip 8.0 (feature level 205), this event was not sent
when a user lost access to a channel due to their role changing.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- streams:(object)[]Array of objects, each containing ID of the channel that was deleted.Changes:Deprecatedin Zulip 10.0 (feature level 343)
and will be removed in a future release. Previously, these
objects additionally contained all the standard fields for a
channel object.stream_id:integerID of the deleted channel.
- stream_ids:(integer)[]Array containing the IDs of the channels that were deleted.Changes: New in Zulip 10.0 (feature level 343). Previously,
these IDs were available only via the legacystreamsarray.
- stream_id:integerID of the deleted channel.
Example

```
{"id":0,"op":"delete","stream_ids":[1,2],"streams":[{"stream_id":1},{"stream_id":2}],"type":"stream"}
```

```
{"id":0,"op":"delete","stream_ids":[1,2],"streams":[{"stream_id":1},{"stream_id":2}],"type":"stream"}
```

### streamop: update
Event sent to all users who can see that a channel exists
when a property of that channel changes. SeeGET /streamsresponse
for details on the various properties of a channel.
This event is also sent when archiving or unarchiving a
channel to all the users who can see that channel exists
but only to the clients that declared thearchived_channelsclient capability.
Changes: Prior to Zulip 11.0 (feature level 378),
this event was never sent when archiving or unarchiving
a channel.
Before Zulip 9.0 (feature level 256), this event was never
sent when thefirst_message_idproperty of a channel was
updated because the oldest message that had been sent to it
changed.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- stream_id:integerThe ID of the channel whose details have changed.
- name:stringThe name of the channel whose details have changed.
- property:stringThe property of the channel which has changed. SeeGET /streamsresponse for details
on the various properties of a channel.Clients should handle an "unknown" property received here without
crashing, since that can happen when connecting to a server running a
newer version of Zulip with new features.
- value:object | integer | boolean | string | nullThe new value of the changed property.Changes: Starting with Zulip 11.0 (feature level 389),
this value can benullwhen a channel is removed from the folder.Starting with Zulip 10.0 (feature level 320), this
field can be an object forcan_remove_subscribers_groupproperty,
which is agroup-setting value, when the setting
is set to a combination of users and groups.If an object, it will be agroup-setting valuewith these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- rendered_description:stringNote: Only present if the changed property wasdescription.The short description of the channel rendered as HTML, intended to
be used when displaying the channel description in a UI.One should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax
work correctly. And any client-side security logic for
user-generated message content should be applied when displaying
this HTML as though it were the body of a Zulip message.SeeMarkdown message formattingfor details on Zulip's HTML format.
- history_public_to_subscribers:booleanNote: Only present if the changed property wasinvite_only.Whether the history of the channel is public to its subscribers.Currently always true for public channels (i.e."invite_only": falseimplies"history_public_to_subscribers": true), but clients should not make that
assumption, as we may change that behavior in the future.
- is_web_public:booleanNote: Only present if the changed property wasinvite_only.Whether the channel's history is now readable by web-public spectators.Changes: New in Zulip 5.0 (feature level 71).
- If an object, it will be agroup-setting valuewith these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
Example

```
{"history_public_to_subscribers":true,"id":0,"is_web_public":false,"name":"test","op":"update","property":"invite_only","stream_id":11,"type":"stream","value":true}
```

```
{"history_public_to_subscribers":true,"id":0,"is_web_public":false,"name":"test","op":"update","property":"invite_only","stream_id":11,"type":"stream","value":true}
```

### reactionop: add
Event sent when a reaction is added to a message.
Sent to all users who were recipients of the message.
- emoji_name:stringName of the emoji.
- emoji_code:stringA unique identifier, defining the specific emoji codepoint requested,
within the namespace of thereaction_type.
- reaction_type:stringA string indicating the type of emoji. Each emojireaction_typehas an independent namespace for values ofemoji_code.Must be one of the following values:unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").
- user_id:integerThe ID of the user who added the reaction.Changes: New in Zulip 3.0 (feature level 2). Theuserobject is deprecated and will be removed in the future.
- user:objectDictionary with data on the user who added the
reaction, including the user ID as theuser_idfield.Changes: This field was re-added in Zulip 10.0 (feature
level 339) after having been removed in Zulip 10.0 (feature
level 328). It remains deprecated; it was re-added because the
React Native mobile app was still using it.Deprecatedand to be removed in a future release once core
clients have migrated to use the adjacentuser_idfield, which
was introduced in Zulip 3.0 (feature level 2). Clients
supporting older Zulip server versions should use the user ID
mentioned in the description above as they would theuser_idfield.user_id:integerID of the user.email:stringZulip API email of the user.full_name:stringFull name of the user.is_mirror_dummy:booleanWhether the user is a mirror dummy.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- message_id:integerThe ID of the message to which a reaction was
added.
- unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.
- realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.
- zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").
- user_id:integerID of the user.
- email:stringZulip API email of the user.
- full_name:stringFull name of the user.
- is_mirror_dummy:booleanWhether the user is a mirror dummy.
Example

```
{"emoji_code":"1f389","emoji_name":"tada","id":0,"message_id":32,"op":"add","reaction_type":"unicode_emoji","type":"reaction","user":{"email":"user10@zulip.testserver","full_name":"King Hamlet","user_id":10},"user_id":10}
```

```
{"emoji_code":"1f389","emoji_name":"tada","id":0,"message_id":32,"op":"add","reaction_type":"unicode_emoji","type":"reaction","user":{"email":"user10@zulip.testserver","full_name":"King Hamlet","user_id":10},"user_id":10}
```

### reactionop: remove
Event sent when a reaction is removed from a message.
Sent to all users who were recipients of the message.
- emoji_name:stringName of the emoji.
- emoji_code:stringA unique identifier, defining the specific emoji codepoint requested,
within the namespace of thereaction_type.
- reaction_type:stringA string indicating the type of emoji. Each emojireaction_typehas an independent namespace for values ofemoji_code.Must be one of the following values:unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").
- user_id:integerThe ID of the user who added the reaction.Changes: New in Zulip 3.0 (feature level 2). Theuserobject is deprecated and will be removed in the future.
- user:objectDictionary with data on the user who added the
reaction, including the user ID as theuser_idfield.Changes: This field was re-added in Zulip 10.0 (feature
level 339) after having been removed in Zulip 10.0 (feature
level 328). It remains deprecated; it was re-added because the
React Native mobile app was still using it.Deprecatedand to be removed in a future release once core
clients have migrated to use the adjacentuser_idfield, which
was introduced in Zulip 3.0 (feature level 2). Clients
supporting older Zulip server versions should use the user ID
mentioned in the description above as they would theuser_idfield.user_id:integerID of the user.email:stringZulip API email of the user.full_name:stringFull name of the user.is_mirror_dummy:booleanWhether the user is a mirror dummy.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- message_id:integerThe ID of the message from which the reaction was
removed.
- unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.
- realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.
- zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").
- user_id:integerID of the user.
- email:stringZulip API email of the user.
- full_name:stringFull name of the user.
- is_mirror_dummy:booleanWhether the user is a mirror dummy.
Example

```
{"emoji_code":"1f389","emoji_name":"tada","id":0,"message_id":52,"op":"remove","reaction_type":"unicode_emoji","type":"reaction","user":{"email":"user10@zulip.testserver","full_name":"King Hamlet","user_id":10},"user_id":10}
```

```
{"emoji_code":"1f389","emoji_name":"tada","id":0,"message_id":52,"op":"remove","reaction_type":"unicode_emoji","type":"reaction","user":{"email":"user10@zulip.testserver","full_name":"King Hamlet","user_id":10},"user_id":10}
```

### attachmentop: add
Event sent to a user's clients when the user uploads a new file
in a Zulip message. Useful to implement live update in UI showing all files
the current user has uploaded.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- attachment:objectDictionary containing details of a file uploaded by a user.id:integerThe unique ID for the attachment.name:stringName of the uploaded file.path_id:stringA representation of the path of the file within the
repository of user-uploaded files. If thepath_idof a
file is{realm_id}/ab/cdef/temp_file.py, its URL will be:{server_url}/user_uploads/{realm_id}/ab/cdef/temp_file.py.size:integerSize of the file in bytes.create_time:integerTime when the attachment was uploaded as a UNIX timestamp.Changes: Before Zulip 12.0 (feature level 443), this value
was milliseconds since the epoch, not seconds.Changed in Zulip 3.0 (feature level 22). This field was
previously a floating point number.message_ids:(integer)[]Array containing the IDs of messages that reference thisuploaded file. This includes messages
sent by any user in the Zulip organization who sent a
message containing a link to the uploaded file.Changes: In Zulip 12.0 (feature level 472), this
replaced the previousmessagesfield, which was an array
of objects containing bothidanddate_sentproperties.
- upload_space_used:integerThe total size of all files uploaded by in the organization,
in bytes.
- id:integerThe unique ID for the attachment.
- name:stringName of the uploaded file.
- path_id:stringA representation of the path of the file within the
repository of user-uploaded files. If thepath_idof a
file is{realm_id}/ab/cdef/temp_file.py, its URL will be:{server_url}/user_uploads/{realm_id}/ab/cdef/temp_file.py.
- size:integerSize of the file in bytes.
- create_time:integerTime when the attachment was uploaded as a UNIX timestamp.Changes: Before Zulip 12.0 (feature level 443), this value
was milliseconds since the epoch, not seconds.Changed in Zulip 3.0 (feature level 22). This field was
previously a floating point number.
- message_ids:(integer)[]Array containing the IDs of messages that reference thisuploaded file. This includes messages
sent by any user in the Zulip organization who sent a
message containing a link to the uploaded file.Changes: In Zulip 12.0 (feature level 472), this
replaced the previousmessagesfield, which was an array
of objects containing bothidanddate_sentproperties.
Example

```
{"attachment":{"create_time":1594825414,"id":1,"message_ids":[],"name":"zulip.txt","path_id":"2/ce/2Xpnnwgh8JWKxBXtTfD6BHKV/zulip.txt","size":6},"id":0,"op":"add","type":"attachment","upload_space_used":6}
```

```
{"attachment":{"create_time":1594825414,"id":1,"message_ids":[],"name":"zulip.txt","path_id":"2/ce/2Xpnnwgh8JWKxBXtTfD6BHKV/zulip.txt","size":6},"id":0,"op":"add","type":"attachment","upload_space_used":6}
```

### attachmentop: update
Event sent to a user's clients when details of a file that user
uploaded are changed. Most updates will be changes in the list of
messages that reference the uploaded file.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- attachment:objectDictionary containing details of a file uploaded by a user.id:integerThe unique ID for the attachment.name:stringName of the uploaded file.path_id:stringA representation of the path of the file within the
repository of user-uploaded files. If thepath_idof a
file is{realm_id}/ab/cdef/temp_file.py, its URL will be:{server_url}/user_uploads/{realm_id}/ab/cdef/temp_file.py.size:integerSize of the file in bytes.create_time:integerTime when the attachment was uploaded as a UNIX timestamp.Changes: Before Zulip 12.0 (feature level 443), this value
was milliseconds since the epoch, not seconds.Changed in Zulip 3.0 (feature level 22). This field was
previously a floating point number.message_ids:(integer)[]Array containing the IDs of messages that reference thisuploaded file. This includes messages
sent by any user in the Zulip organization who sent a
message containing a link to the uploaded file.Changes: In Zulip 12.0 (feature level 472), this
replaced the previousmessagesfield, which was an array
of objects containing bothidanddate_sentproperties.
- upload_space_used:integerThe total size of all files uploaded by in the organization,
in bytes.
- id:integerThe unique ID for the attachment.
- name:stringName of the uploaded file.
- path_id:stringA representation of the path of the file within the
repository of user-uploaded files. If thepath_idof a
file is{realm_id}/ab/cdef/temp_file.py, its URL will be:{server_url}/user_uploads/{realm_id}/ab/cdef/temp_file.py.
- size:integerSize of the file in bytes.
- create_time:integerTime when the attachment was uploaded as a UNIX timestamp.Changes: Before Zulip 12.0 (feature level 443), this value
was milliseconds since the epoch, not seconds.Changed in Zulip 3.0 (feature level 22). This field was
previously a floating point number.
- message_ids:(integer)[]Array containing the IDs of messages that reference thisuploaded file. This includes messages
sent by any user in the Zulip organization who sent a
message containing a link to the uploaded file.Changes: In Zulip 12.0 (feature level 472), this
replaced the previousmessagesfield, which was an array
of objects containing bothidanddate_sentproperties.
Example

```
{"attachment":{"create_time":1594825414,"id":1,"message_ids":[],"name":"zulip.txt","path_id":"2/ce/2Xpnnwgh8JWKxBXtTfD6BHKV/zulip.txt","size":6},"id":0,"op":"update","type":"attachment","upload_space_used":6}
```

```
{"attachment":{"create_time":1594825414,"id":1,"message_ids":[],"name":"zulip.txt","path_id":"2/ce/2Xpnnwgh8JWKxBXtTfD6BHKV/zulip.txt","size":6},"id":0,"op":"update","type":"attachment","upload_space_used":6}
```

### attachmentop: remove
Event sent to a user's clients when the user deletes a file
they had uploaded. Useful primarily for UI showing all the files
the current user has uploaded.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- attachment:objectDictionary containing the ID of the deleted attachment.id:integerThe ID of the deleted attachment.
- upload_space_used:integerThe total size of all files uploaded by in the organization,
in bytes.
- id:integerThe ID of the deleted attachment.
Example

```
{"attachment":{"id":1},"id":0,"op":"remove","type":"attachment","upload_space_used":0}
```

```
{"attachment":{"id":1},"id":0,"op":"remove","type":"attachment","upload_space_used":0}
```

### deviceop: add
Event sent to a user's clients when theyregister a device.
Helps clients to live-update thedevicesdictionary
returned inPOST /registerresponse.

```
POST /register
```
Changes: New in Zulip 12.0 (feature level 468).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- device_id:integerThe ID of the new registered device.
Example

```
{"device_id":1144,"id":1,"op":"add","type":"device"}
```

```
{"device_id":1144,"id":1,"op":"add","type":"device"}
```

### deviceop: remove
Event sent to a user's clients when they deregister a device.
Helps clients to live-update thedevicesdictionary
returned inPOST /registerresponse.

```
POST /register
```
Changes: New in Zulip 12.0 (feature level 468).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- device_id:integerThe ID of the device which deregistered.
Example

```
{"device_id":1144,"id":1,"op":"remove","type":"device"}
```

```
{"device_id":1144,"id":1,"op":"remove","type":"device"}
```

### deviceop: update
Event sent to a user's clients when the metadata in thedevicesdictionary for the user changes.
Helps clients to live-update thedevicesdictionary
returned inPOST /registerresponse.

```
POST /register
```
Besidesid,type,op, anddevice_id, all other fields
are optional. Only fields whose values needs to be updated are
included in the event.
Changes: New in Zulip 12.0 (feature level 468).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- device_id:integerThe ID of the registered device whose metadata changed.
- push_key_id:integerID to reference the encryption key used to encrypt
push notifications sent to the device.
- push_token_id:string | nullID to reference the token provided by FCM/APNs to the device,
which is registered to the push bouncer service.Anullvalue means the referenced token expired.
- pending_push_token_id:string | nullID to reference the token provided by FCM/APNs to the device,
whose registration is in progress to the push bouncer service.Anullvalue means the pending registration succeeded.
- push_token_last_updated_timestamp:integerThe UNIX timestamp for the last time whenpending_push_token_idwas set to a new non-null value, in UTC seconds.
- push_registration_error_code:string | nullIf the push registration failed, aZulip API error codeindicating the type of failure that occurred.The following error codes have recommended client behavior:"INVALID_BOUNCER_PUBLIC_KEY"- Inform the user to update app."REQUEST_EXPIRED- Retry with a fresh payload.
- "INVALID_BOUNCER_PUBLIC_KEY"- Inform the user to update app.
- "REQUEST_EXPIRED- Retry with a fresh payload.
Example

```
{"device_id":12,"id":2,"op":"update","push_key_id":57,"type":"device"}
```

```
{"device_id":12,"id":2,"op":"update","push_key_id":57,"type":"device"}
```

### submessage
Event sent when a submessage is added to a message.
Submessages are anexperimentalAPI used for widgets such as the/pollwidget in Zulip.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- msg_type:stringThe type of the message.
- content:stringThe new content of the submessage.
- message_id:integerThe ID of the message to which the submessage has been added.
- sender_id:integerThe ID of the user who sent the message.
- submessage_id:integerThe ID of the submessage.
Example

```
{"content":"{\"type\":\"vote\",\"key\":\"58,1\",\"vote\":1}","id":28,"message_id":970461,"msg_type":"widget","sender_id":58,"submessage_id":4737,"type":"submessage"}
```

```
{"content":"{\"type\":\"vote\",\"key\":\"58,1\",\"vote\":1}","id":28,"message_id":970461,"msg_type":"widget","sender_id":58,"submessage_id":4737,"type":"submessage"}
```

### user_status
Event sent to all users who can access the modified
user when the status of a user changes.
Changes: Prior to Zulip 8.0 (feature level 228),
this event was sent to all users in the organization.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- away:booleanWhether the user has marked themself "away" with this status.Changes: Deprecated in Zulip 6.0 (feature level 148);
starting with that feature level,awayis a legacy way to
access the user'spresence_enabledsetting, withaway = !presence_enabled. To be removed in a future release.
- status_text:stringThe text content of the status message.This will be""for users who set a status without selecting
or writing a message.
- emoji_name:stringTheemoji namefor
the emoji the user selected for their new status.This will be""for users who set a status without selecting
an emoji.Changes: New in Zulip 5.0 (feature level 86).
- emoji_code:stringTheemoji codefor
the emoji the user selected for their new status.This will be""for users who set a status without selecting
an emoji.Changes: New in Zulip 5.0 (feature level 86).
- reaction_type:stringTheemoji typefor
the emoji the user selected for their new status.This will be""for users who set a status without selecting
an emoji.Changes: New in Zulip 5.0 (feature level 86).
- user_id:integerThe ID of the user whose status changed.
Example

```
{"away":true,"emoji_code":"1f697","emoji_name":"car","id":0,"reaction_type":"unicode_emoji","status_text":"out to lunch","type":"user_status","user_id":10}
```

```
{"away":true,"emoji_code":"1f697","emoji_name":"car","id":0,"reaction_type":"unicode_emoji","status_text":"out to lunch","type":"user_status","user_id":10}
```

### custom_profile_fields
Event sent to all users in a Zulip organization when new custom
profile field types are configured for that Zulip organization.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- fields:(object)[]An array of dictionaries where each dictionary contains
details of a single new custom profile field for the Zulip
organization.id:integerThe ID of the custom profile field. This will be referenced in the custom
profile fields section of user objects.type:integerAn integer indicating the type of the custom profile field, which determines
how it is configured and displayed to users.See theCustom profile fieldsarticle for details on what each type means.1: Short text2: Paragraph3: Dropdown4: Date picker5: Link6: Person picker7: External account8: PronounsChanges: Field type8added in Zulip 6.0 (feature level 151).order:integerCustom profile fields are displayed in both settings UI and
UI showing users' profiles in increasingorder.name:stringThe name of the custom profile field.hint:stringThe help text to be displayed for the custom profile field in user-facing
settings UI for configuring custom profile fields.field_data:stringField types 3 (Dropdown) and 7 (External account) support storing
additional configuration for the field type in thefield_dataattribute.For field type 3 (Dropdown), this attribute is a JSON dictionary
defining the choices and the order they will be displayed in the
dropdown UI for individual users to select an option.The interface for field type 7 is not yet stabilized.display_in_profile_summary:booleanWhether the custom profile field, display or not on the user card.Must be false forPerson pickerprofile field types.This field is only included when its value istrue.Changes: Before Zulip 12.0 (feature level 476), the
"Paragraph" field type was not supported.New in Zulip 6.0 (feature level 146).required:booleanWhether an organization administrator has configured this profile field as
required.Because the required property is mutable, clients cannot assume that a required
custom profile field has a value. The Zulip web application displays a prominent
banner to any user who has not set a value for a required field.Changes: New in Zulip 9.0 (feature level 244).editable_by_user:booleanWhether regular users can edit this profile field on their own account.Note that organization administrators can edit custom profile fields for any user
regardless of this setting.Changes: New in Zulip 10.0 (feature level 296).use_for_user_matching:booleanWhether this custom profile field should be used to match users in typeahead
suggestions. Only allowed for Short Text and External Accountprofile field types.This field is only included when its value istrue.Changes: New in Zulip 12.0 (feature level 455).
- id:integerThe ID of the custom profile field. This will be referenced in the custom
profile fields section of user objects.
- type:integerAn integer indicating the type of the custom profile field, which determines
how it is configured and displayed to users.See theCustom profile fieldsarticle for details on what each type means.1: Short text2: Paragraph3: Dropdown4: Date picker5: Link6: Person picker7: External account8: PronounsChanges: Field type8added in Zulip 6.0 (feature level 151).
- order:integerCustom profile fields are displayed in both settings UI and
UI showing users' profiles in increasingorder.
- name:stringThe name of the custom profile field.
- hint:stringThe help text to be displayed for the custom profile field in user-facing
settings UI for configuring custom profile fields.
- field_data:stringField types 3 (Dropdown) and 7 (External account) support storing
additional configuration for the field type in thefield_dataattribute.For field type 3 (Dropdown), this attribute is a JSON dictionary
defining the choices and the order they will be displayed in the
dropdown UI for individual users to select an option.The interface for field type 7 is not yet stabilized.
- display_in_profile_summary:booleanWhether the custom profile field, display or not on the user card.Must be false forPerson pickerprofile field types.This field is only included when its value istrue.Changes: Before Zulip 12.0 (feature level 476), the
"Paragraph" field type was not supported.New in Zulip 6.0 (feature level 146).
- required:booleanWhether an organization administrator has configured this profile field as
required.Because the required property is mutable, clients cannot assume that a required
custom profile field has a value. The Zulip web application displays a prominent
banner to any user who has not set a value for a required field.Changes: New in Zulip 9.0 (feature level 244).
- editable_by_user:booleanWhether regular users can edit this profile field on their own account.Note that organization administrators can edit custom profile fields for any user
regardless of this setting.Changes: New in Zulip 10.0 (feature level 296).
- use_for_user_matching:booleanWhether this custom profile field should be used to match users in typeahead
suggestions. Only allowed for Short Text and External Accountprofile field types.This field is only included when its value istrue.Changes: New in Zulip 12.0 (feature level 455).
- 1: Short text
- 2: Paragraph
- 3: Dropdown
- 4: Date picker
- 5: Link
- 6: Person picker
- 7: External account
- 8: Pronouns
Example

```
{"fields":[{"editable_by_user":true,"field_data":"","hint":"","id":1,"name":"Phone number","order":1,"required":true,"type":1},{"editable_by_user":true,"field_data":"","hint":"What are you known for?","id":2,"name":"Biography","order":2,"required":true,"type":2},{"editable_by_user":true,"field_data":"","hint":"Or drink, if you'd prefer","id":3,"name":"Favorite food","order":3,"required":false,"type":1},{"display_in_profile_summary":true,"editable_by_user":true,"field_data":"{\"0\":{\"text\":\"Vim\",\"order\":\"1\"},\"1\":{\"text\":\"Emacs\",\"order\":\"2\"}}","hint":"","id":4,"name":"Favorite editor","order":4,"required":true,"type":3},{"editable_by_user":false,"field_data":"","hint":"","id":5,"name":"Birthday","order":5,"required":false,"type":4},{"display_in_profile_summary":true,"editable_by_user":true,"field_data":"","hint":"Or your personal blog's URL","id":6,"name":"Favorite website","order":6,"required":false,"type":5},{"editable_by_user":false,"field_data":"","hint":"","id":7,"name":"Mentor","order":7,"required":true,"type":6},{"editable_by_user":true,"field_data":"{\"subtype\":\"github\"}","hint":"Enter your GitHub username","id":8,"name":"GitHub","order":8,"required":true,"type":7,"use_for_user_matching":true}],"id":0,"type":"custom_profile_fields"}
```

```
{"fields":[{"editable_by_user":true,"field_data":"","hint":"","id":1,"name":"Phone number","order":1,"required":true,"type":1},{"editable_by_user":true,"field_data":"","hint":"What are you known for?","id":2,"name":"Biography","order":2,"required":true,"type":2},{"editable_by_user":true,"field_data":"","hint":"Or drink, if you'd prefer","id":3,"name":"Favorite food","order":3,"required":false,"type":1},{"display_in_profile_summary":true,"editable_by_user":true,"field_data":"{\"0\":{\"text\":\"Vim\",\"order\":\"1\"},\"1\":{\"text\":\"Emacs\",\"order\":\"2\"}}","hint":"","id":4,"name":"Favorite editor","order":4,"required":true,"type":3},{"editable_by_user":false,"field_data":"","hint":"","id":5,"name":"Birthday","order":5,"required":false,"type":4},{"display_in_profile_summary":true,"editable_by_user":true,"field_data":"","hint":"Or your personal blog's URL","id":6,"name":"Favorite website","order":6,"required":false,"type":5},{"editable_by_user":false,"field_data":"","hint":"","id":7,"name":"Mentor","order":7,"required":true,"type":6},{"editable_by_user":true,"field_data":"{\"subtype\":\"github\"}","hint":"Enter your GitHub username","id":8,"name":"GitHub","order":8,"required":true,"type":7,"use_for_user_matching":true}],"id":0,"type":"custom_profile_fields"}
```

### default_stream_groups
Event sent to all users in a Zulip organization when an organization
administrator changes the organization's configured default channel groups.
Default channel groups are anexperimentalfeature that is not yet
stabilized.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- default_stream_groups:(object)[]An array of dictionaries where each dictionary
contains details about a single default channel group.name:stringName of the default channel group.description:stringDescription of the default channel group.id:integerThe ID of the default channel group.streams:(integer)[]An array of IDs of all the channels in the default stream group.Changes: Before Zulip 10.0 (feature level 330), we sent array
of dictionaries where each dictionary contained details about a
single stream in the default stream group.
- name:stringName of the default channel group.
- description:stringDescription of the default channel group.
- id:integerThe ID of the default channel group.
- streams:(integer)[]An array of IDs of all the channels in the default stream group.Changes: Before Zulip 10.0 (feature level 330), we sent array
of dictionaries where each dictionary contained details about a
single stream in the default stream group.
Example

```
{"default_stream_groups":[{"description":"New description","id":2,"name":"group1","streams":[3,1,5]}],"id":0,"type":"default_stream_groups"}
```

```
{"default_stream_groups":[{"description":"New description","id":2,"name":"group1","streams":[3,1,5]}],"id":0,"type":"default_stream_groups"}
```

### default_streams
Event sent to all users in a Zulip organization when the
default channels in the organization are changed by an
organization administrator.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- default_streams:(integer)[]An array of IDs of all thedefault channelsin the organization.Changes: Before Zulip 10.0 (feature level 330),
we sent array of dictionaries where each dictionary
contained details about a single default stream for
the Zulip organization.
Example

```
{"default_streams":[2,3],"id":0,"type":"default_streams"}
```

```
{"default_streams":[2,3],"id":0,"type":"default_streams"}
```

### delete_message
Event sent when a message has been deleted.
Sent to all users who currently are subscribed to the messages'
recipient. May also be sent to additional users who had access to
the deleted message, including, in particular, an administrator user
deleting messages in a channel that they are not subscribed to, but
have content access to. Clients can thus reliably remove the
messages from whatever view the administrator was using to delete
them.
Clients will receive an event of this type for message deletions
that the client itself initiated if and only if the user previously
had access to the deleted messages. (Some moderation actions, such
as deleting all messages sent by a user, allow deleting DMs or
private channel messages that the acting user cannot themselves
access. The user will not receive deletion events for such
inaccessible messages).
This event is also sent when the user loses access to a message,
such as when it ismoved to a channelthat
the user does nothave permission to access.
Changes: Before Zulip 12.0 (feature level 457), an
administrator who initiated the deletion of messages that they did
not have permission to access could theoretically receive this event
for inaccessible messages. However, no Zulip feature actually
generated events of that type.
Prior to Zulip 12.0 (feature level 452) messages deleted via a
message retention policy incorrectly failed to generatedelete_messageevents.
Before Zulip 9.0 (feature level 274), this event was only sent to
subscribers of the message's recipient.
Before Zulip 5.0 (feature level 77), events
for direct messages contained additionalsender_idandrecipient_idfields.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- message_ids:(integer)[]Only present for clients that support thebulk_message_deletionclient capability.A sorted list containing the IDs of the newly deleted messages.Changes: Before Zulip 11.0 (feature level 393), this list was
not guaranteed to be sorted.
- message_id:integerOnly present for clients that do not support thebulk_message_deletionclient capability.The ID of the newly deleted message.
- message_type:stringThe type of message. Either"stream"or"private".
- stream_id:integerOnly present ifmessage_typeis"stream".The ID of the channel to which the message was sent.
- topic:stringOnly present ifmessage_typeis"stream".The topic to which the message was sent.For clients that don't support theempty_topic_nameclient capability,
if the actual topic name was empty string, this field's value will instead
be the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse.Changes: Before 10.0 (feature level 334),empty_topic_nameclient capability didn't exist and empty string as the topic name for
channel messages wasn't allowed.

```
POST /register
```
Example

```
{"id":0,"message_id":37,"message_type":"private","type":"delete_message"}
```

```
{"id":0,"message_id":37,"message_type":"private","type":"delete_message"}
```

### muted_topics
Event sent to a user's clients when that user's set of
configured muted topics have changed.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- muted_topics:((string | integer)[])[]Array of tuples, where each tuple describes a muted topic.
The first element of the tuple is the channel name in which the topic
has to be muted, the second element is the topic name to be muted
and the third element is an integer UNIX timestamp representing
when the topic was muted.Changes: Deprecated in Zulip 6.0 (feature level
134). Starting with this version, clients that explicitly
requested the replacementuser_topicevent type when
registering their event queue will not receive this legacy
event type.Before Zulip 3.0 (feature level 1), themuted_topicsarray objects were 2-item tuples and did not include the timestamp
information for when the topic was muted.
Example

```
{"id":0,"muted_topics":[["Denmark","topic",1594825442]],"type":"muted_topics"}
```

```
{"id":0,"muted_topics":[["Denmark","topic",1594825442]],"type":"muted_topics"}
```

### user_topic
Event sent to a user's clients when the user mutes/unmutes
a topic, or otherwise modifies their personal per-topic
configuration.
Changes: New in Zulip 6.0 (feature level 134). Previously,
clients were notified about changes in muted topic
configuration via themuted_topicsevent type.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- stream_id:integerThe ID of the channel to which the topic belongs.
- topic_name:stringThe name of the topic.For clients that don't support theempty_topic_nameclient capability,
if the actual topic name is empty string, this field's value will instead
be the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse.Changes: Before 10.0 (feature level 334),empty_topic_nameclient capability didn't exist and empty string as the topic name for
channel messages wasn't allowed.
- last_updated:integerAn integer UNIX timestamp representing when the user-topic
relationship was last changed.
- visibility_policy:integerAn integer indicating the user's visibility
preferences for the topic, such as whether the topic
is muted.0 = None. Used to indicate that the user no
  longer has a special visibility policy for this topic.1 = Muted. Used to recordmuted topics.2 = Unmuted. Used to record unmuted topics.3 = Followed. Used to recordfollowed topics.Changes: In Zulip 7.0 (feature level 219), added followed as
a visibility policy option.In Zulip 7.0 (feature level 170), added unmuted as a visibility
policy option.

```
POST /register
```
- 0 = None. Used to indicate that the user no
  longer has a special visibility policy for this topic.
- 1 = Muted. Used to recordmuted topics.
- 2 = Unmuted. Used to record unmuted topics.
- 3 = Followed. Used to recordfollowed topics.
Example

```
{"id":1,"last_updated":1594825442,"stream_id":1,"topic_name":"topic","type":"user_topic","visibility_policy":1}
```

```
{"id":1,"last_updated":1594825442,"stream_id":1,"topic_name":"topic","type":"user_topic","visibility_policy":1}
```

### muted_users
Event sent to a user's clients when that user's set of
configuredmuted usershave changed.
Changes: New in Zulip 4.0 (feature level 48).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- muted_users:(object)[]A list of dictionaries where each dictionary describes
a muted user.id:integerThe ID of the muted user.timestamp:integerAn integer UNIX timestamp representing when the user was muted.
- id:integerThe ID of the muted user.
- timestamp:integerAn integer UNIX timestamp representing when the user was muted.
Example

```
{"id":0,"muted_users":[{"id":1,"timestamp":1594825442},{"id":22,"timestamp":1654865392}],"type":"muted_users"}
```

```
{"id":0,"muted_users":[{"id":1,"timestamp":1594825442},{"id":22,"timestamp":1654865392}],"type":"muted_users"}
```

### heartbeat
Heartbeat events are sent by the server to avoid
longpolling connections being affected by networks that
kill idle HTTP connections.
Clients do not need to do anything to process these
events, beyond the commonlast_event_idaccounting.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
Example

```
{"id":0,"type":"heartbeat"}
```

```
{"id":0,"type":"heartbeat"}
```

### onboarding_steps
Event sent when the set of onboarding steps to show for the current user
has changed (e.g. because the user dismissed one).
Clients that feature a similar tutorial experience to the Zulip web app
may want to handle these events.
Changes: Before Zulip 8.0 (feature level 233), this event was namedhotspots. Prior to this feature level, one-time notice onboarding
steps were not supported.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- onboarding_steps:(object)[]An array of dictionaries where each dictionary contains details about a
single onboarding step.Changes: Before Zulip 8.0 (feature level 233), this array was namedhotspots. Prior to this feature level, one-time notice onboarding
steps were not supported, and thetypefield in these objects did not
exist as all onboarding steps were implicitly hotspots.type:stringThe type of the onboarding step. Valid value is"one_time_notice".Changes: Removed type"hotspot"in Zulip 9.0 (feature level 259).New in Zulip 8.0 (feature level 233).name:stringThe name of the onboarding step.
- type:stringThe type of the onboarding step. Valid value is"one_time_notice".Changes: Removed type"hotspot"in Zulip 9.0 (feature level 259).New in Zulip 8.0 (feature level 233).
- name:stringThe name of the onboarding step.
Example

```
{"id":0,"onboarding_steps":[{"name":"visibility_policy_banner","type":"one_time_notice"}],"type":"onboarding_steps"}
```

```
{"id":0,"onboarding_steps":[{"name":"visibility_policy_banner","type":"one_time_notice"}],"type":"onboarding_steps"}
```

### update_message
Event sent when a message's content, topic and/or
channel has been edited or when a message's content
has a rendering update, such as for aninline URL preview.
Sent to all users who had received the original
message.
Changes: In Zulip 10.0 (feature level 284), removed theprev_rendered_content_versionfield as it is an internal
server implementation detail not used by any client.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- user_id:integer | nullThe ID of the user who sent the message.Will benullwhen event is for a rendering update of the original
message, such as for aninline URL preview.Changes: Prior to Zulip 5.0 (feature level 114), this field was
omitted forinline URL previewupdates.
- rendering_only:booleanWhether the event only updates the rendered content of the message.This field should be used by clients to determine if the event
only provides a rendering update to the message content,
such as for aninline URL preview.
Whentrue, the event does not reflect a user-generated edit
and does not modify the message history.Changes: New in Zulip 5.0 (feature level 114). Clients can
correctly identify these rendering update events prior to this
feature level by checking whether theuser_idfield was omitted.
- message_id:integerThe ID of the message which was edited or updated.This field should be used to apply content edits to the client's
cached message history, or to apply rendered content updates.If the channel or topic was changed, the set of moved messages is
encoded in the separatemessage_idsfield, which is guaranteed
to includemessage_id.
- message_ids:(integer)[]A sorted list of IDs of messages to which any channel or topic
changes encoded in this event should be applied.This list always includesmessage_id, even when there are no
channel or topic changes to apply.These messages are guaranteed to have all been previously sent
to channelstream_idwith topicorig_subject, and have been
moved tonew_stream_idwith topicsubject(if those fields
are present in the event).Clients processing these events should update all cached message
history associated with the moved messages (including adjustingunread_msgsdata structures, where the client may not have the
message itself in its history) to reflect the new channel and
topic.Content changes should be applied only to the single message
indicated bymessage_id.Changes: Before Zulip 11.0 (feature level 393), this list
was not guaranteed to be sorted.
- flags:(string)[]The user's personalmessage flagsfor the
message with IDmessage_idfollowing the edit.A client application should compare these to the original flags
to identify cases where a mention or alert word was added by the
edit.Changes: In Zulip 8.0 (feature level 224), thewildcard_mentionedflag was deprecated in favor of thestream_wildcard_mentionedandtopic_wildcard_mentionedflags. Thewildcard_mentionedflag exists
for backwards compatibility with older clients and equalsstream_wildcard_mentioned || topic_wildcard_mentioned. Clients
supporting older server versions should treat this field as a previous
name for thestream_wildcard_mentionedflag as topic wildcard mentions
were not available prior to this feature level.
- edit_timestamp:integerThe UNIX timestamp when this message edit operation was processed by
the server, in UTC seconds.Changes: Prior to Zulip 5.0 (feature level 114), this field
was omitted forinline URL previewupdates.
- stream_name:stringOnly present if the message was edited and originally sent to a channel.The name of the channel that the message was sent to. Clients
are recommended to use thestream_idfield instead.
- stream_id:integerOnly present if the message was edited and originally sent to a channel.The pre-edit channel for all of the messages with IDs inmessage_ids.Changes: As of Zulip 5.0 (feature level 112), this field
is present for all edits to a channel message. Previously, it
was not present when only the content of the channel message was
edited.
- new_stream_id:integerOnly present if message(s) were moved to a different channel.The post-edit channel for all of the messages with IDs inmessage_ids.
- propagate_mode:stringOnly present if this event moved messages to a different
topic and/or channel.The choice the editing user made about which messages should be
affected by a channel/topic edit:"change_one": Just change the one indicated inmessage_id."change_later": Change messages in the same topic that had
  been sent after this one."change_all": Change all messages in that topic.This parameter should be used to decide whether to change
navigation and compose box state in response to the edit. For
example, if the user was previously in topic narrow, and the
topic was edited with"change_later"or"change_all", the Zulip
web app will automatically navigate to the new topic narrow.
Similarly, a message being composed to the old topic should
have its recipient changed to the new topic.This navigation makes it much more convenient to move content
between topics without disruption or messages continuing
to be sent to the pre-edit topic by accident.
- orig_subject:stringOnly present if this event moved messages to a different
topic and/or channel.The pre-edit topic for all of the messages with IDs inmessage_ids.For clients that don't support theempty_topic_nameclient capability,
if the actual pre-edit topic name is empty string, this field's value will instead
be the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse.Changes: Before 10.0 (feature level 334),empty_topic_nameclient capability didn't exist and empty string as the topic name for
channel messages wasn't allowed.
- subject:stringOnly present if this event moved messages to a different topic;
this field will not be present when moving messages to the same
topic name in a different channel.The post-edit topic for all of the messages with IDs inmessage_ids.For clients that don't support theempty_topic_nameclient capability,
if the actual post-edit topic name is empty string, this field's value will instead
be the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse.Changes: Before 10.0 (feature level 334),empty_topic_nameclient capability didn't exist and empty string as the topic name for
channel messages wasn't allowed.
- topic_links:(object)[]Only present if this event moved messages to a different topic;
this field will not be present when moving messages to the same
topic name in a different channel.Data on any links to be included in thetopicline (these are generated bycustom linkification filterthat match content in the message's topic.), corresponding
to the post-edit topic.Changes: This field contained a list of urls before
Zulip 4.0 (feature level 46).New in Zulip 3.0 (feature level 1). Previously, this field
was calledsubject_links; clients are recommended to
renamesubject_linkstotopic_linksif present for
compatibility with older Zulip servers.text:stringThe original link text present in the topic.url:stringThe expanded target url which the link points to.
- orig_content:stringOnly present if this event changed the message content.The original content of the message with IDmessage_idimmediately prior to this edit, in the originalZulip-flavored Markdownformat.
- orig_rendered_content:stringOnly present if this event changed the message content.The original content of the message with IDmessage_idimmediately prior to this edit, rendered as HTML.SeeMarkdown message formattingfor details on Zulip's HTML format.
- content:stringOnly present if this event changed the message content or
updated the message content for aninline URL preview.The new content of the message with IDmessage_id, in the
originalZulip-flavored Markdownformat.
- rendered_content:stringOnly present if this event changed the message content or
updated the message content for aninline URL preview.The new content of the message with IDmessage_id,
rendered in HTML.SeeMarkdown message formattingfor details on Zulip's HTML format.
- is_me_message:booleanOnly present if this event changed the message content.Whether the message with IDmessage_idis now a/me status message.
- "change_one": Just change the one indicated inmessage_id.
- "change_later": Change messages in the same topic that had
  been sent after this one.
- "change_all": Change all messages in that topic.

```
POST /register
```

```
POST /register
```
- text:stringThe original link text present in the topic.
- url:stringThe expanded target url which the link points to.
Example

```
{"content":"new content","edit_timestamp":1594825451,"flags":[],"id":0,"is_me_message":false,"message_id":58,"message_ids":[57,58],"orig_content":"hello","orig_rendered_content":"<p>hello</p>","orig_subject":"test","propagate_mode":"change_all","rendered_content":"<p>new content</p>","rendering_only":false,"stream_id":5,"stream_name":"Verona","subject":"new_topic","topic_links":[],"type":"update_message","user_id":10}
```

```
{"content":"new content","edit_timestamp":1594825451,"flags":[],"id":0,"is_me_message":false,"message_id":58,"message_ids":[57,58],"orig_content":"hello","orig_rendered_content":"<p>hello</p>","orig_subject":"test","propagate_mode":"change_all","rendered_content":"<p>new content</p>","rendering_only":false,"stream_id":5,"stream_name":"Verona","subject":"new_topic","topic_links":[],"type":"update_message","user_id":10}
```

### typingop: start
Event sent when a user starts typing a message.
Sent to all clients for users who would receive the
message being typed, with the additional rule that typing
notifications for channel messages are only sent to clients
that includedstream_typing_notificationsin theirclient capabilitieswhen registering
the event queue.
SeePOST /typingendpoint for more details.
Changes: Typing notifications for channel messages are new in
Zulip 4.0 (feature level 58).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- message_type:stringType of message being composed. Must be"stream"or"direct".Changes: In Zulip 8.0 (feature level 215), replaced the
value"private"with"direct".New in Zulip 4.0 (feature level 58). Previously, all typing
notifications were implicitly direct messages.
- sender:objectObject describing the user who is typing the message.user_id:integerThe user's ID.email:stringThe Zulip API email address for the user.
- recipients:(object)[]Only present ifmessage_typeis"direct".Array of dictionaries describing the set of users who would be
recipients of the message being typed. Each dictionary contains
details about one of the recipients. The sending user is guaranteed
to appear among the recipients.user_id:integerThe ID of the user.email:stringThe Zulip API email address for the user.
- stream_id:integerOnly present ifmessage_typeis"stream".The unique ID of the channel to which message is being typed.Changes: New in Zulip 4.0 (feature level 58). Previously,
typing notifications were only for direct messages.
- topic:stringOnly present ifmessage_typeis"stream".Topic within the channel where the message is being typed.For clients that don't support theempty_topic_nameclient capability,
if the actual topic name is empty string, this field's value will instead
be the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse.Changes: Before 10.0 (feature level 334),empty_topic_nameclient capability didn't exist and empty string as the topic name for
channel messages wasn't allowed.New in Zulip 4.0 (feature level 58). Previously, typing notifications
were only for direct messages.
- user_id:integerThe user's ID.
- email:stringThe Zulip API email address for the user.
- user_id:integerThe ID of the user.
- email:stringThe Zulip API email address for the user.

```
POST /register
```
Example

```
{"id":0,"message_type":"direct","op":"start","recipients":[{"email":"user8@zulip.testserver","user_id":8},{"email":"user10@zulip.testserver","user_id":10}],"sender":{"email":"user10@zulip.testserver","user_id":10},"type":"typing"}
```

```
{"id":0,"message_type":"direct","op":"start","recipients":[{"email":"user8@zulip.testserver","user_id":8},{"email":"user10@zulip.testserver","user_id":10}],"sender":{"email":"user10@zulip.testserver","user_id":10},"type":"typing"}
```

### typingop: stop
Event sent when a user stops typing a message.
Sent to all clients for users who would receive the message
that was previously being typed, with the additional rule
that typing notifications for channel messages are only sent to
clients that includedstream_typing_notificationsin theirclient capabilitieswhen registering
the event queue.
SeePOST /typingendpoint for more details.
Changes: Typing notifications for channel messages are new in
Zulip 4.0 (feature level 58).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- message_type:stringType of message being composed. Must be"stream"or"direct".Changes: In Zulip 8.0 (feature level 215), replaced the
value"private"with"direct".New in Zulip 4.0 (feature level 58). Previously all typing
notifications were implicitly direct messages.
- sender:objectObject describing the user who was previously typing the message.user_id:integerThe user's ID.email:stringThe Zulip API email address for the user.
- recipients:(object)[]Only present ifmessage_typeis"direct".Array of dictionaries describing the set of users who would be
recipients of the message that was previously being typed. Each
dictionary contains details about one of the recipients. The
sending user is guaranteed to appear among the recipients.user_id:integerThe ID of the user.email:stringThe Zulip API email address for the user.
- stream_id:integerOnly present ifmessage_typeis"stream".The unique ID of the channel to which message is being typed.Changes: New in Zulip 4.0 (feature level 58). Previously,
typing notifications were only for direct messages.
- topic:stringOnly present ifmessage_typeis"stream".Topic within the channel where the message is being typed.Changes: New in Zulip 4.0 (feature level 58). Previously,
typing notifications were only for direct messages.
- user_id:integerThe user's ID.
- email:stringThe Zulip API email address for the user.
- user_id:integerThe ID of the user.
- email:stringThe Zulip API email address for the user.
Example

```
{"id":0,"message_type":"direct","op":"stop","recipients":[{"email":"user8@zulip.testserver","user_id":8},{"email":"user10@zulip.testserver","user_id":10}],"sender":{"email":"user10@zulip.testserver","user_id":10},"type":"typing"}
```

```
{"id":0,"message_type":"direct","op":"stop","recipients":[{"email":"user8@zulip.testserver","user_id":8},{"email":"user10@zulip.testserver","user_id":10}],"sender":{"email":"user10@zulip.testserver","user_id":10},"type":"typing"}
```

### typing_edit_messageop: start
Event sent when a user starts editing a message.
Event sent when a user starts typing in a textarea to edit the
content of a message. See theedit message typing notifications
endpoint.
Clients requestingtyping_edit_messageevent type that havereceives_typing_notificationsenabled will receive this event if
they would have been notified if the message's content edit were to
be saved (E.g., because they were a direct message recipient or
are a subscribe to the channel).
Changes: New in Zulip 10.0 (feature level 351). Previously,
typing notifications were not available when editing messages.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- sender_id:integerThe ID of the user who is typing the edit of the
message.Clients should be careful to display this user as the person who
is typing, not that of the sender of the message, in case a
collaborative editing feature be might be added in the future.
- message_id:integerIndicates the message id of the message that is being edited.
- recipient:objectObject containing details about recipients of message edit typing notification.type:stringType of message being composed. Must be"channel"or"direct".channel_id:integerOnly present iftypeis"channel".The unique ID of the channel to which message is being edited.topic:stringOnly present iftypeis"channel".Topic within the channel where the message is being edited.user_ids:(integer)[]Present only iftypeisdirect.The user IDs of every recipient of this direct message.
- type:stringType of message being composed. Must be"channel"or"direct".
- channel_id:integerOnly present iftypeis"channel".The unique ID of the channel to which message is being edited.
- topic:stringOnly present iftypeis"channel".Topic within the channel where the message is being edited.
- user_ids:(integer)[]Present only iftypeisdirect.The user IDs of every recipient of this direct message.
Example

```
{"id":0,"message_id":7,"op":"start","recipient":{"type":"direct","user_ids":[8,10]},"sender_id":10,"type":"typing_edit_message"}
```

```
{"id":0,"message_id":7,"op":"start","recipient":{"type":"direct","user_ids":[8,10]},"sender_id":10,"type":"typing_edit_message"}
```

### typing_edit_messageop: stop
Event sent when a user stops typing in a textarea to edit the
content of a message. See theedit message typing notifications
endpoint.
Clients requestingtyping_edit_messageevent type that havereceives_typing_notificationsenabled will receive this event if
they would have been notified if the message's content edit were to
be saved (E.g., because they were a direct message recipient or
are a subscribe to the channel).
Changes: New in Zulip 10.0 (feature level 351). Previously,
typing notifications were not available when editing messages.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- sender_id:integerThe ID of the user who sent the message.
- message_id:integerIndicates the message id of the message that is being edited.
- recipient:objectObject containing details about recipients of message edit typing notification.type:stringType of message being composed. Must be"channel"or"direct".channel_id:integerOnly present iftypeis"channel".The unique ID of the channel to which message is being edited.topic:stringOnly present iftypeis"channel".Topic within the channel where the message is being edited.user_ids:(integer)[]Present only iftypeisdirect.The user IDs of every recipient of this direct message.
- type:stringType of message being composed. Must be"channel"or"direct".
- channel_id:integerOnly present iftypeis"channel".The unique ID of the channel to which message is being edited.
- topic:stringOnly present iftypeis"channel".Topic within the channel where the message is being edited.
- user_ids:(integer)[]Present only iftypeisdirect.The user IDs of every recipient of this direct message.
Example

```
{"id":0,"message_id":31,"op":"stop","recipient":{"type":"direct","user_ids":[8,10]},"sender_id":10,"type":"typing_edit_message"}
```

```
{"id":0,"message_id":31,"op":"stop","recipient":{"type":"direct","user_ids":[8,10]},"sender_id":10,"type":"typing_edit_message"}
```

### update_message_flagsop: add
Event sent to a user whenmessage flagsare added
to messages.
This can reflect a direct user action, or can be the indirect
consequence of another action. Whatever the cause, if there's a change
in the set of message flags that the user has for a message, then anupdate_message_flagsevent will be sent with the change. Note
that this applies when the user already had access to the message, and
continues to have access to it. When a message newly appears or
disappears, amessageordelete_messageevent is sent instead.

```
delete_message
```
Some examples of actions that trigger anupdate_message_flagsevent:
- The"starred"flag is added when the user chooses tostar a
  message.
- The"read"flag is added when the user marks messages as read by
  scrolling through them, or usesMark all messages as readon a conversation.
- The"read"flag is added when the usermutesa
  message's sender.
- The"read"flag is added after the user unsubscribes from a channel,
  or messages are moved to a not-subscribed channel, provided the user
  can still access the messages at all. Note adelete_messageevent is sent in the case where the
  user can no longer access the messages.

```
delete_message
```
In some cases, a change in message flags that's caused by another change
may happen a short while after the original change, rather than
simultaneously. For example, when messages that were unread are moved to
a channel where the user is not subscribed, the resulting change in
message flags (and the correspondingupdate_message_flagsevent with
flag"read") may happen later than the message move itself. The delay
in that example is typically at most a few hundred milliseconds and can
in rare cases be minutes or longer.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- operation:stringOld name for theopfield in this event type.Deprecatedin Zulip 4.0 (feature level 32), and
replaced by theopfield.
- flag:stringTheflagthat was added.
- messages:(integer)[]Array containing the IDs of all messages to which
the flag was added.
- all:booleanWhether the specified flag was added to all messages.
This field is only relevant for the"read"flag, and
will befalsefor all other flags.Whentruefor the"read"flag, then themessagesarray will be empty.
Example

```
{"all":false,"flag":"starred","id":0,"messages":[63],"op":"add","operation":"add","type":"update_message_flags"}
```

```
{"all":false,"flag":"starred","id":0,"messages":[63],"op":"add","operation":"add","type":"update_message_flags"}
```

### update_message_flagsop: remove
Event sent to a user whenmessage flagsare
removed from messages.
See the description for theupdate_message_flagsop:addevent for
more details about these events.

```
update_message_flags
```
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- operation:stringOld name for theopfield in this event type.Deprecatedin Zulip 4.0 (feature level 32), and
replaced by theopfield.
- flag:stringTheflagto be removed.
- messages:(integer)[]Array containing the IDs of the messages from which the flag
was removed.
- all:booleanWill befalsefor all specified flags.Deprecatedand will be removed in a future release.
- message_details:objectOnly present if the specifiedflagis"read".A set of data structures describing the messages that
are being marked as unread with additional details to
allow clients to update theunread_msgsdata
structure for these messages (which may not be
otherwise known to the client).Changes: New in Zulip 5.0 (feature level 121). Previously,
marking already read messages as unread was not
supported by the Zulip API.{message_id}:objectObject containing details about the
message with the specified ID.type:stringThe type of this message. Either"stream"or"private".mentioned:booleanA flag which indicates whether the message contains a mention
of the user.Present only if the message mentions the current user.user_ids:(integer)[]Present only iftypeisprivate.The user IDs of every recipient of this direct message, excluding yourself.
Will be the empty list for a message you had sent to only yourself.stream_id:integerPresent only iftypeis"stream".The ID of the channel where the message was sent.topic:stringPresent only iftypeis"stream".Name of the topic where the message was sent.For clients that don't support theempty_topic_nameclient capability,
if the actual topic name is empty string, this field's value will instead
be the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse.Changes: Before 10.0 (feature level 334),empty_topic_nameclient capability didn't exist and empty string as the topic name for
channel messages wasn't allowed.unmuted_stream_msg:booleanDeprecatedinternal implementation detail. Clients should
ignore this field as it will be removed in the future.
- {message_id}:objectObject containing details about the
message with the specified ID.type:stringThe type of this message. Either"stream"or"private".mentioned:booleanA flag which indicates whether the message contains a mention
of the user.Present only if the message mentions the current user.user_ids:(integer)[]Present only iftypeisprivate.The user IDs of every recipient of this direct message, excluding yourself.
Will be the empty list for a message you had sent to only yourself.stream_id:integerPresent only iftypeis"stream".The ID of the channel where the message was sent.topic:stringPresent only iftypeis"stream".Name of the topic where the message was sent.For clients that don't support theempty_topic_nameclient capability,
if the actual topic name is empty string, this field's value will instead
be the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse.Changes: Before 10.0 (feature level 334),empty_topic_nameclient capability didn't exist and empty string as the topic name for
channel messages wasn't allowed.unmuted_stream_msg:booleanDeprecatedinternal implementation detail. Clients should
ignore this field as it will be removed in the future.
- type:stringThe type of this message. Either"stream"or"private".
- mentioned:booleanA flag which indicates whether the message contains a mention
of the user.Present only if the message mentions the current user.
- user_ids:(integer)[]Present only iftypeisprivate.The user IDs of every recipient of this direct message, excluding yourself.
Will be the empty list for a message you had sent to only yourself.
- stream_id:integerPresent only iftypeis"stream".The ID of the channel where the message was sent.
- topic:stringPresent only iftypeis"stream".Name of the topic where the message was sent.For clients that don't support theempty_topic_nameclient capability,
if the actual topic name is empty string, this field's value will instead
be the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse.Changes: Before 10.0 (feature level 334),empty_topic_nameclient capability didn't exist and empty string as the topic name for
channel messages wasn't allowed.
- unmuted_stream_msg:booleanDeprecatedinternal implementation detail. Clients should
ignore this field as it will be removed in the future.

```
POST /register
```
Example

```
{"all":false,"flag":"starred","id":0,"message_details":{"63":{"stream_id":22,"topic":"lunch","type":"stream"}},"messages":[63],"op":"remove","operation":"remove","type":"update_message_flags"}
```

```
{"all":false,"flag":"starred","id":0,"message_details":{"63":{"stream_id":22,"topic":"lunch","type":"stream"}},"messages":[63],"op":"remove","operation":"remove","type":"update_message_flags"}
```

### user_groupop: add
Event sent to users in an organization when auser groupis created.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- group:objectObject containing the user group's attributes.name:stringThe name of the user group.date_created:integer | nullThe UNIX timestamp for when the user group was created, in UTC seconds.Anullvalue means the user group has no recorded date, which is often
because the user group is very old, or because it was created via a data
import tool ormanagement command.Changes: New in Zulip 10.0 (feature level 292).creator_id:integer | nullThe ID of the user who created this user group.Anullvalue means the user group has no recorded creator, which is often
because the user group is very old, or because it was created via a data
import tool ormanagement command.Changes: New in Zulip 10.0 (feature level 292).description:stringThe description of the user group.members:(integer)[]Array containing the ID of the users who are
members of this user group.Changes: Prior to Zulip 10.0 (feature level 303), this
list also included deactivated users who were members of
the user group before being deactivated.direct_subgroup_ids:(integer)[]Array containing the ID of the direct_subgroups of
this user group.Changes: New in Zulip 6.0 (feature level 131).
Introduced in feature level 127 assubgroups, but
clients can ignore older events as this feature level
predates subgroups being fully implemented.id:integerThe ID of the user group.is_system_group:booleanWhether the user group is a system group which cannot be
directly modified by users.Changes: New in Zulip 5.0 (feature level 93).can_add_members_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to add members to this user group.Changes: New in Zulip 10.0 (feature level 305). Previously, this
permission was controlled by thecan_manage_groupsetting.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_join_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to join this user group.Changes: New in Zulip 10.0 (feature level 301).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_leave_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to leave this user group.Changes: New in Zulip 10.0 (feature level 308).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_manage_group:integer | objectAgroup-setting valuedefining the set of users who
have permission tomanage this user group.Changes: New in Zulip 10.0 (feature level 283).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_mention_group:integer | objectAgroup-setting valuedefining the set of users who
have permission tomention this user group.Changes: Before Zulip 9.0 (feature level 258), this setting was
always the integer form of agroup-setting value.Before Zulip 8.0 (feature level 198), this setting was namedcan_mention_group_id.New in Zulip 8.0 (feature level 191). Previously, groups could be
mentioned only if they were notsystem groups.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_remove_members_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to remove members from this user group.Changes: New in Zulip 10.0 (feature level 324). Previously, this
permission was controlled by thecan_manage_groupsetting.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.deactivated:booleanWhether the user group is deactivated. Deactivated groups
cannot be used as a subgroup of another group or used for
any other purpose.Changes: New in Zulip 10.0 (feature level 290).
- name:stringThe name of the user group.
- date_created:integer | nullThe UNIX timestamp for when the user group was created, in UTC seconds.Anullvalue means the user group has no recorded date, which is often
because the user group is very old, or because it was created via a data
import tool ormanagement command.Changes: New in Zulip 10.0 (feature level 292).
- creator_id:integer | nullThe ID of the user who created this user group.Anullvalue means the user group has no recorded creator, which is often
because the user group is very old, or because it was created via a data
import tool ormanagement command.Changes: New in Zulip 10.0 (feature level 292).
- description:stringThe description of the user group.
- members:(integer)[]Array containing the ID of the users who are
members of this user group.Changes: Prior to Zulip 10.0 (feature level 303), this
list also included deactivated users who were members of
the user group before being deactivated.
- direct_subgroup_ids:(integer)[]Array containing the ID of the direct_subgroups of
this user group.Changes: New in Zulip 6.0 (feature level 131).
Introduced in feature level 127 assubgroups, but
clients can ignore older events as this feature level
predates subgroups being fully implemented.
- id:integerThe ID of the user group.
- is_system_group:booleanWhether the user group is a system group which cannot be
directly modified by users.Changes: New in Zulip 5.0 (feature level 93).
- can_add_members_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to add members to this user group.Changes: New in Zulip 10.0 (feature level 305). Previously, this
permission was controlled by thecan_manage_groupsetting.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_join_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to join this user group.Changes: New in Zulip 10.0 (feature level 301).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_leave_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to leave this user group.Changes: New in Zulip 10.0 (feature level 308).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_manage_group:integer | objectAgroup-setting valuedefining the set of users who
have permission tomanage this user group.Changes: New in Zulip 10.0 (feature level 283).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_mention_group:integer | objectAgroup-setting valuedefining the set of users who
have permission tomention this user group.Changes: Before Zulip 9.0 (feature level 258), this setting was
always the integer form of agroup-setting value.Before Zulip 8.0 (feature level 198), this setting was namedcan_mention_group_id.New in Zulip 8.0 (feature level 191). Previously, groups could be
mentioned only if they were notsystem groups.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_remove_members_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to remove members from this user group.Changes: New in Zulip 10.0 (feature level 324). Previously, this
permission was controlled by thecan_manage_groupsetting.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- deactivated:booleanWhether the user group is deactivated. Deactivated groups
cannot be used as a subgroup of another group or used for
any other purpose.Changes: New in Zulip 10.0 (feature level 290).
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
Example

```
{"group":{"can_add_members_group":16,"can_join_group":16,"can_leave_group":15,"can_manage_group":16,"can_mention_group":11,"can_remove_members_group":16,"creator_id":9,"date_created":1717484476,"description":"Backend team","id":2,"is_system_group":false,"members":[12],"name":"backend"},"id":0,"op":"add","type":"user_group"}
```

```
{"group":{"can_add_members_group":16,"can_join_group":16,"can_leave_group":15,"can_manage_group":16,"can_mention_group":11,"can_remove_members_group":16,"creator_id":9,"date_created":1717484476,"description":"Backend team","id":2,"is_system_group":false,"members":[12],"name":"backend"},"id":0,"op":"add","type":"user_group"}
```

### user_groupop: update
Event sent to all users in a Zulip organization
when a property of a user group is changed.
For group deactivation, this event is only sent
ifinclude_deactivated_groupsclient capability
is set totrue.
This event is also sent when deactivating or reactivating
a user for settings set to anonymous user groups which the
user is direct member of. When deactivating the user, event
is only sent to users who cannot access the deactivated user.
Changes: Starting with Zulip 10.0 (feature level 303), this
event can also be sent when deactivating or reactivating a user.
Prior to Zulip 10.0 (feature level 294), this event was sent to
all clients when a user group was deactivated.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- group_id:integerThe ID of the user group whose details have changed.
- data:objectDictionary containing the changed details of the user group.name:stringThe new name of the user group. Only present if the group's name changed.description:stringThe new description of the group. Only present if the description
changed.can_add_members_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to add members to this group. Only present if this user
group permission setting changed.Changes: New in Zulip 10.0 (feature level 305). Previously, this
permission was controlled by thecan_manage_groupsetting.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_join_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to join this group. Only present if this user group
permission setting changed.Changes: New in Zulip 10.0 (feature level 301).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_leave_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to leave this group. Only present if this user group
permission setting changed.Changes: New in Zulip 10.0 (feature level 308).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_manage_group:integer | objectAgroup-setting valuedefining the set of users who
have permission tomanage this group. Only present
if this user group permission setting changed.Changes: New in Zulip 10.0 (feature level 283).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_mention_group:integer | objectAgroup-setting valuedefining the set of users who
have permission tomention this user group. Only present
if this user group permission setting changed.Changes: Before Zulip 9.0 (feature level 258), this setting was
always the integer form of agroup-setting value.Before Zulip 8.0 (feature level 198), this setting was namedcan_mention_group_id.New in Zulip 8.0 (feature level 191). Previously, groups could be
mentioned only if they were notsystem groups.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_remove_members_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to remove members from this group. Only present if this
user group permission setting changed.Changes: New in Zulip 10.0 (feature level 324). Previously, this
permission was controlled by thecan_manage_groupsetting.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.deactivated:booleanWhether the user group is deactivated. Deactivated groups
cannot be used as a subgroup of another group or used for
any other purpose.Changes: New in Zulip 10.0 (feature level 290).
- name:stringThe new name of the user group. Only present if the group's name changed.
- description:stringThe new description of the group. Only present if the description
changed.
- can_add_members_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to add members to this group. Only present if this user
group permission setting changed.Changes: New in Zulip 10.0 (feature level 305). Previously, this
permission was controlled by thecan_manage_groupsetting.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_join_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to join this group. Only present if this user group
permission setting changed.Changes: New in Zulip 10.0 (feature level 301).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_leave_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to leave this group. Only present if this user group
permission setting changed.Changes: New in Zulip 10.0 (feature level 308).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_manage_group:integer | objectAgroup-setting valuedefining the set of users who
have permission tomanage this group. Only present
if this user group permission setting changed.Changes: New in Zulip 10.0 (feature level 283).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_mention_group:integer | objectAgroup-setting valuedefining the set of users who
have permission tomention this user group. Only present
if this user group permission setting changed.Changes: Before Zulip 9.0 (feature level 258), this setting was
always the integer form of agroup-setting value.Before Zulip 8.0 (feature level 198), this setting was namedcan_mention_group_id.New in Zulip 8.0 (feature level 191). Previously, groups could be
mentioned only if they were notsystem groups.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_remove_members_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to remove members from this group. Only present if this
user group permission setting changed.Changes: New in Zulip 10.0 (feature level 324). Previously, this
permission was controlled by thecan_manage_groupsetting.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- deactivated:booleanWhether the user group is deactivated. Deactivated groups
cannot be used as a subgroup of another group or used for
any other purpose.Changes: New in Zulip 10.0 (feature level 290).
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
Example

```
{"data":{"description":"Mention this group to get the security team's attention."},"group_id":2,"id":0,"op":"update","type":"user_group"}
```

```
{"data":{"description":"Mention this group to get the security team's attention."},"group_id":2,"id":0,"op":"update","type":"user_group"}
```

### user_groupop: add_members
Event sent to all users when users have been added to a user group.
This event is also sent when reactivating a user for all the user
groups the reactivated user was a member of before being deactivated.
Changes: Starting with Zulip 10.0 (feature level 303), this
event can also be sent when reactivating a user.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- group_id:integerThe ID of the user group with new members.
- user_ids:(integer)[]Array containing the IDs of the users who have been added
to the user group.
Example

```
{"group_id":2,"id":0,"op":"add_members","type":"user_group","user_ids":[10]}
```

```
{"group_id":2,"id":0,"op":"add_members","type":"user_group","user_ids":[10]}
```

### user_groupop: remove_members
Event sent to all users when users have been removed from
a user group.
This event is also sent when deactivating a user, for all
the user groups the deactivated user is a member of, but only
to the users who cannot access the deactivated user.
Changes: Starting with Zulip 10.0 (feature level 303),
this event can also be sent when deactivating a user.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- group_id:integerThe ID of the user group whose details have changed.
- user_ids:(integer)[]Array containing the IDs of the users who have been removed
from the user group.
Example

```
{"group_id":2,"id":0,"op":"remove_members","type":"user_group","user_ids":[10]}
```

```
{"group_id":2,"id":0,"op":"remove_members","type":"user_group","user_ids":[10]}
```

### user_groupop: add_subgroups
Event sent to all users when subgroups have been added to
a user group.
Changes: New in Zulip 6.0 (feature level 127).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- group_id:integerThe ID of the user group whose details have changed.
- direct_subgroup_ids:(integer)[]Array containing the IDs of the subgroups that have been added
to the user group.Changes: New in Zulip 6.0 (feature level 131).
Previously, this was calledsubgroup_ids, but
clients can ignore older events as this feature level
predates subgroups being fully implemented.
Example

```
{"direct_subgroup_ids":[10],"group_id":2,"id":0,"op":"add_subgroups","type":"user_group"}
```

```
{"direct_subgroup_ids":[10],"group_id":2,"id":0,"op":"add_subgroups","type":"user_group"}
```

### user_groupop: remove_subgroups
Event sent to all users when subgroups have been removed from
a user group.
Changes: New in Zulip 6.0 (feature level 127).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- group_id:integerThe ID of the user group whose details have changed.
- direct_subgroup_ids:(integer)[]Array containing the IDs of the subgroups that have been
removed from the user group.Changes: New in Zulip 6.0 (feature level 131).
Previously, this was calledsubgroup_ids, but
clients can ignore older events as this feature level
predates subgroups being fully implemented.
Example

```
{"direct_subgroup_ids":[10],"group_id":2,"id":0,"op":"remove_subgroups","type":"user_group"}
```

```
{"direct_subgroup_ids":[10],"group_id":2,"id":0,"op":"remove_subgroups","type":"user_group"}
```

### user_groupop: remove
Event sent when a user group is deactivated but only to clients
withinclude_deactivated_groupsclient capability set tofalse.
Changes: Prior to Zulip 10.0 (feature level 294), this
event was sent when a user group was deleted.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- group_id:integerThe ID of the group which has been deleted.
Example

```
{"group_id":2,"id":0,"op":"remove","type":"user_group"}
```

```
{"group_id":2,"id":0,"op":"remove","type":"user_group"}
```

### realm_linkifiers
Event sent to all users in a Zulip organization when the
set of configuredlinkifiersfor the organization has changed.
Processing this event is important for doing Markdown local echo
correctly.
Clients will not receive this event unless the event queue is
registered with the client capability{"linkifier_url_template": true}.
SeePOST /registerfor how client capabilities can be specified.

```
POST /register
```
Changes: Before Zulip 7.0 (feature level 176), thelinkifier_url_templateclient capability was not required. The
requirement was added because linkifiers were updated to contain
a URL template instead of a URL format string, which was not a
backwards-compatible change.
New in Zulip 4.0 (feature level 54), replacing the deprecatedrealm_filtersevent type.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- realm_linkifiers:(object)[]An ordered array of dictionaries where each dictionary contains
details about a single linkifier.Clients should always process linkifiers in the order given;
this is important if the realm has linkifiers with overlapping
patterns. The order can be modified usingPATCH
/realm/linkifiers.pattern:stringThePython regular expressionthat represents the pattern that should be linkified by this linkifier.url_template:stringTheRFC 6570compliant
URL template to be used for linkifying matches.Changes: New in Zulip 7.0 (feature level 176). This replacedurl_format,
which contained a URL format string.id:integerThe ID of the linkifier.example_input:string | nullAn example input string that matches the linkifier's pattern.
This is required for reverse linkifiers.Changes: New in Zulip 12.0 (feature level 471).reverse_template:string | nullA simple template using{variable}for variables that can
be used to generate the Markdown linkifier syntax, given a
URL matching the URL template.{{/}}can be used for literal{/}characters.Changes: New in Zulip 12.0 (feature level 471).alternative_url_templates:(string)[]An array of additionalRFC 6570compliant URL
template strings that are used for reverse linkification
(converting pasted URLs to linkifier pattern text). These
templates have no effect on forward linkification.Changes: New in Zulip 12.0 (feature level e2b257).

```
PATCH
/realm/linkifiers
```
- pattern:stringThePython regular expressionthat represents the pattern that should be linkified by this linkifier.
- url_template:stringTheRFC 6570compliant
URL template to be used for linkifying matches.Changes: New in Zulip 7.0 (feature level 176). This replacedurl_format,
which contained a URL format string.
- id:integerThe ID of the linkifier.
- example_input:string | nullAn example input string that matches the linkifier's pattern.
This is required for reverse linkifiers.Changes: New in Zulip 12.0 (feature level 471).
- reverse_template:string | nullA simple template using{variable}for variables that can
be used to generate the Markdown linkifier syntax, given a
URL matching the URL template.{{/}}can be used for literal{/}characters.Changes: New in Zulip 12.0 (feature level 471).
- alternative_url_templates:(string)[]An array of additionalRFC 6570compliant URL
template strings that are used for reverse linkification
(converting pasted URLs to linkifier pattern text). These
templates have no effect on forward linkification.Changes: New in Zulip 12.0 (feature level e2b257).
Example

```
{"id":0,"realm_linkifiers":[{"alternative_url_templates":["https://realm.com/my_realm_filter/issue/{id}"],"example_input":"#1234","id":1,"pattern":"#(?P<id>[123])","reverse_template":"#{id}","url_template":"https://realm.com/my_realm_filter/{id}"}],"type":"realm_linkifiers"}
```

```
{"id":0,"realm_linkifiers":[{"alternative_url_templates":["https://realm.com/my_realm_filter/issue/{id}"],"example_input":"#1234","id":1,"pattern":"#(?P<id>[123])","reverse_template":"#{id}","url_template":"https://realm.com/my_realm_filter/{id}"}],"type":"realm_linkifiers"}
```

### realm_filters
Legacy event type that is no longer sent to clients. Previously, sent
to all users in a Zulip organization when the set of configuredlinkifiersfor the organization was
changed.
Changes: Prior to Zulip 7.0 (feature level 176), this event type
was sent to clients.
Deprecatedin Zulip 4.0 (feature level 54), and replaced by therealm_linkifiersevent type, which has a clearer name and format.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- realm_filters:((integer | string)[])[]An array of tuples, where each tuple described a linkifier. The first
element of the tuple was a string regex pattern which represented the
pattern to be linkified on matching, for example"#(?P<id>[123])".
The second element was the URL format string that the pattern should be
linkified with. A URL format string for the above example would be"https://realm.com/my_realm_filter/%(id)s". And the third element
was the ID of the realm filter.
Example

```
{"id":0,"realm_filters":[],"type":"realm_filters"}
```

```
{"id":0,"realm_filters":[],"type":"realm_filters"}
```

### realm_playgrounds
Event sent to all users in a Zulip organization when the
set of configuredcode playgroundsfor the organization has changed.
Changes: New in Zulip 4.0 (feature level 49).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- realm_playgrounds:(object)[]An array of dictionaries where each dictionary contains
data about a single playground entry.id:integerThe unique ID for the realm playground.name:stringThe user-visible display name of the playground. Clients
should display this in UI for picking which playground to
open a code block in, to differentiate between multiple
configured playground options for a given pygments
language.Changes: New in Zulip 4.0 (feature level 49).pygments_language:stringThe name of the Pygments language lexer for that
programming language.url_template:stringTheRFC 6570compliant URL template for the playground. The template contains
exactly one variable namedcode, which determines how the
extracted code should be substituted in the playground URL.Changes: New in Zulip 8.0 (feature level 196). This replaced theurl_prefixparameter, which was used to construct URLs by just
concatenating url_prefix and code.
- id:integerThe unique ID for the realm playground.
- name:stringThe user-visible display name of the playground. Clients
should display this in UI for picking which playground to
open a code block in, to differentiate between multiple
configured playground options for a given pygments
language.Changes: New in Zulip 4.0 (feature level 49).
- pygments_language:stringThe name of the Pygments language lexer for that
programming language.
- url_template:stringTheRFC 6570compliant URL template for the playground. The template contains
exactly one variable namedcode, which determines how the
extracted code should be substituted in the playground URL.Changes: New in Zulip 8.0 (feature level 196). This replaced theurl_prefixparameter, which was used to construct URLs by just
concatenating url_prefix and code.
Example

```
{"id":0,"realm_playgrounds":[{"id":1,"name":"Python playground","pygments_language":"Python","url_template":"https://python.example.com"}],"type":"realm_playgrounds"}
```

```
{"id":0,"realm_playgrounds":[{"id":1,"name":"Python playground","pygments_language":"Python","url_template":"https://python.example.com"}],"type":"realm_playgrounds"}
```

### realm_emojiop: update
Event sent to all users in a Zulip organization when
acustom emojihas been updated,
typically when a new emoji has been added or an old one
has been deactivated. The event contains all custom emoji
configured for the organization, not just the updated
custom emoji.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- realm_emoji:objectAn object in which each key describes a realm emoji.{emoji_id}:objectObject containing details about the emoji with
the specified ID. It has the following properties:id:stringThe ID for this emoji, same as the object's key.name:stringThe user-friendly name for this emoji. Users in the organization
can use this emoji by writing this name between colons (:name :).source_url:stringThe path relative to the organization's URL where the
emoji's image can be found.still_url:string | nullOnly non-null when the emoji's image is animated.The path relative to the organization's URL where a still
(not animated) version of the emoji can be found. (This is
currently always the first frame of the animation).This is useful for clients to display the emoji in contexts
where continuously animating it would be a bad user experience
(E.g. because it would be distracting).Changes: New in Zulip 5.0 (added as optional field in
feature level 97 and then made mandatory, but nullable, in
feature level 113).deactivated:booleanWhether the emoji has been deactivated or not.author_id:integer | nullThe user ID of the user who uploaded the custom emoji.
Will benullif the uploader is unknown.Changes: New in Zulip 3.0 (feature level 7). Previously
was accessible via anauthorobject with anidfield.
- {emoji_id}:objectObject containing details about the emoji with
the specified ID. It has the following properties:id:stringThe ID for this emoji, same as the object's key.name:stringThe user-friendly name for this emoji. Users in the organization
can use this emoji by writing this name between colons (:name :).source_url:stringThe path relative to the organization's URL where the
emoji's image can be found.still_url:string | nullOnly non-null when the emoji's image is animated.The path relative to the organization's URL where a still
(not animated) version of the emoji can be found. (This is
currently always the first frame of the animation).This is useful for clients to display the emoji in contexts
where continuously animating it would be a bad user experience
(E.g. because it would be distracting).Changes: New in Zulip 5.0 (added as optional field in
feature level 97 and then made mandatory, but nullable, in
feature level 113).deactivated:booleanWhether the emoji has been deactivated or not.author_id:integer | nullThe user ID of the user who uploaded the custom emoji.
Will benullif the uploader is unknown.Changes: New in Zulip 3.0 (feature level 7). Previously
was accessible via anauthorobject with anidfield.
- id:stringThe ID for this emoji, same as the object's key.
- name:stringThe user-friendly name for this emoji. Users in the organization
can use this emoji by writing this name between colons (:name :).
- source_url:stringThe path relative to the organization's URL where the
emoji's image can be found.
- still_url:string | nullOnly non-null when the emoji's image is animated.The path relative to the organization's URL where a still
(not animated) version of the emoji can be found. (This is
currently always the first frame of the animation).This is useful for clients to display the emoji in contexts
where continuously animating it would be a bad user experience
(E.g. because it would be distracting).Changes: New in Zulip 5.0 (added as optional field in
feature level 97 and then made mandatory, but nullable, in
feature level 113).
- deactivated:booleanWhether the emoji has been deactivated or not.
- author_id:integer | nullThe user ID of the user who uploaded the custom emoji.
Will benullif the uploader is unknown.Changes: New in Zulip 3.0 (feature level 7). Previously
was accessible via anauthorobject with anidfield.
Example

```
{"id":0,"op":"update","realm_emoji":{"1":{"author_id":11,"deactivated":false,"id":"1","name":"green_tick","source_url":"/user_avatars/2/emoji/images/1.png"},"2":{"author_id":11,"deactivated":true,"id":"2","name":"my_emoji","source_url":"/user_avatars/2/emoji/images/2.png"}},"type":"realm_emoji"}
```

```
{"id":0,"op":"update","realm_emoji":{"1":{"author_id":11,"deactivated":false,"id":"1","name":"green_tick","source_url":"/user_avatars/2/emoji/images/1.png"},"2":{"author_id":11,"deactivated":true,"id":"2","name":"my_emoji","source_url":"/user_avatars/2/emoji/images/2.png"}},"type":"realm_emoji"}
```

### realm_domainsop: add
Event sent to all users in a Zulip organization when the set ofallowed domains for new usershas changed.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- realm_domain:objectObject containing details of the newly added domain.domain:stringThe new allowed domain.allow_subdomains:booleanWhether subdomains are allowed for this domain.
- domain:stringThe new allowed domain.
- allow_subdomains:booleanWhether subdomains are allowed for this domain.
Example

```
{"id":0,"op":"add","realm_domain":{"allow_subdomains":false,"domain":"zulip.org"},"type":"realm_domains"}
```

```
{"id":0,"op":"add","realm_domain":{"allow_subdomains":false,"domain":"zulip.org"},"type":"realm_domains"}
```

### realm_domainsop: change
Event sent to all users in a Zulip organization when the set ofallowed domains for new usershas changed.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- realm_domain:objectObject containing details of the edited domain.domain:stringThe domain whose settings have changed.allow_subdomains:booleanWhether subdomains are allowed for this domain.
- domain:stringThe domain whose settings have changed.
- allow_subdomains:booleanWhether subdomains are allowed for this domain.
Example

```
{"id":0,"op":"change","realm_domain":{"allow_subdomains":true,"domain":"zulip.org"},"type":"realm_domains"}
```

```
{"id":0,"op":"change","realm_domain":{"allow_subdomains":true,"domain":"zulip.org"},"type":"realm_domains"}
```

### realm_domainsop: remove
Event sent to all users in a Zulip organization when the set ofallowed domains for new usershas changed.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- domain:stringThe domain to be removed.
Example

```
{"domain":"zulip.org","id":0,"op":"remove","type":"realm_domains"}
```

```
{"domain":"zulip.org","id":0,"op":"remove","type":"realm_domains"}
```

### realm_export
Event sent to the user who requested adata exportwhen the status of the data export changes.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- exports:(object)[]An array of dictionaries where each dictionary contains
details about a data export of the organization.Changes: Prior to Zulip 10.0 (feature level 304),export_typeparameter was not present as only public data export was supported via API.id:integerThe ID of the data export.acting_user_id:integerThe ID of the user who created the data export.export_time:numberThe UNIX timestamp of when the data export was started.deleted_timestamp:number | nullThe UNIX timestamp of when the data export was deleted.Will benullif the data export has not been deleted.failed_timestamp:number | nullThe UNIX timestamp of when the data export failed.Will benullif the data export succeeded, or if it's
still being generated.export_url:string | nullThe URL to download the generated data export.Will benullif the data export failed, or if it's
still being generated.pending:booleanWhether the data export is pending, which indicates it
is still being generated, or if it succeeded, failed or
was deleted before being generated.Depending on the size of the organization, it can take
anywhere from seconds to an hour to generate the data
export.export_type:stringWhether the data export is public, full with consent, or full without consent.public= Public data export.full_with_consent= Public and private data export (with consent), which includes private data
  for users who have granted consent.full_without_consent= All public and private data, which includes private data for all users.Changes: Zulip 12.0 (feature level 449) changed the type of
this field from int to string with1being replaced bypublicand2being replaced byfull_with_consent. The optionfull_without_consentwas added for full exports without member consent.Changes: New in Zulip 10.0 (feature level 304). Previously,
the export type was not included in these objects because only
public data exports could be created or listed via the API or UI.
- id:integerThe ID of the data export.
- acting_user_id:integerThe ID of the user who created the data export.
- export_time:numberThe UNIX timestamp of when the data export was started.
- deleted_timestamp:number | nullThe UNIX timestamp of when the data export was deleted.Will benullif the data export has not been deleted.
- failed_timestamp:number | nullThe UNIX timestamp of when the data export failed.Will benullif the data export succeeded, or if it's
still being generated.
- export_url:string | nullThe URL to download the generated data export.Will benullif the data export failed, or if it's
still being generated.
- pending:booleanWhether the data export is pending, which indicates it
is still being generated, or if it succeeded, failed or
was deleted before being generated.Depending on the size of the organization, it can take
anywhere from seconds to an hour to generate the data
export.
- export_type:stringWhether the data export is public, full with consent, or full without consent.public= Public data export.full_with_consent= Public and private data export (with consent), which includes private data
  for users who have granted consent.full_without_consent= All public and private data, which includes private data for all users.Changes: Zulip 12.0 (feature level 449) changed the type of
this field from int to string with1being replaced bypublicand2being replaced byfull_with_consent. The optionfull_without_consentwas added for full exports without member consent.Changes: New in Zulip 10.0 (feature level 304). Previously,
the export type was not included in these objects because only
public data exports could be created or listed via the API or UI.
- public= Public data export.
- full_with_consent= Public and private data export (with consent), which includes private data
  for users who have granted consent.
- full_without_consent= All public and private data, which includes private data for all users.
Example

```
{"exports":[{"acting_user_id":10,"deleted_timestamp":null,"export_time":1594825443.656797,"export_type":"public","export_url":null,"failed_timestamp":1594825444.436336,"id":107,"pending":false}],"id":1,"type":"realm_export"}
```

```
{"exports":[{"acting_user_id":10,"deleted_timestamp":null,"export_time":1594825443.656797,"export_type":"public","export_url":null,"failed_timestamp":1594825444.436336,"id":107,"pending":false}],"id":1,"type":"realm_export"}
```

### realm_export_consent
Event sent to administrators when thedata export
consentstatus for a user changes, whether due
to a user changing their consent preferences or a user being created
or reactivated (since user creation/activation events do not contain
these data).
Changes: New in Zulip 10.0 (feature level 312). Previously,
there was not event available to administrators with these data.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- user_id:integerThe ID of the user whose setting was changed.
- consented:booleanWhether the user has consented for their private data export.
Example

```
{"consented":true,"type":"realm_export_consent","user_id":1}
```

```
{"consented":true,"type":"realm_export_consent","user_id":1}
```

### realm_botop: add
Event sent to users who can administer a newly created bot
user. Clients will also receive arealm_userevent that
contains basic details (but not the API key).
Therealm_userevents are sufficient for clients that
only need to interact with the bot; thisrealm_botevent
type is relevant only for administering bots.
Only organization administrators and the user who owns the bot will
receive this event.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- bot:objectObject containing details of a bot.Changes: Removedavatar_url,bot_type,email,full_name,is_activeandowner_idfields from the
dictionary in Zulip 12.0 (feature level 474). Clients
can get all these data from the corresponding user object.Removedapi_keyfield from the dictionary in
Zulip 12.0 (feature level 474). Clients now useGET /bots/{bot_id}/api_keyto get
api key for the bot.user_id:integerThe user ID of the bot.default_sending_stream:string | nullThe default sending channel of the bot. Ifnull, the bot doesn't
have a default sending channel.default_events_register_stream:string | nullThe default channel for which the bot receives events/register data.
Ifnull, the bot doesn't have such a default channel.default_all_public_streams:booleanWhether the bot can send messages to all channels by default.services:(object | object)[]An array containing extra configuration fields only relevant for
outgoing webhook bots and embedded bots. This is always a single-element
array.We consider this part of the Zulip API to be unstable; it is used only
for UI elements for administering bots and is likely to change.When the bot is an outgoing webhook.base_url:stringThe URL the outgoing webhook is configured to post to.token:stringA unique token that the third-party service can use to confirm
that the request is indeed coming from Zulip.interface:integerAn integer indicating what format requests are posted in:1 = Zulip's native outgoing webhook format.2 = Emulate the Slack outgoing webhook format.When the bot is an embedded bot.service_name:stringThe name of the bot.config_data:objectA dictionary of string key/value pairs, which describe the configuration
for the bot. These are usually details like API keys, and are unique to
the integration/bot. Can be an empty dictionary.{config_key}:stringDescription/value of the configuration data key.

```
GET /bots/{bot_id}/api_key
```
- user_id:integerThe user ID of the bot.
- default_sending_stream:string | nullThe default sending channel of the bot. Ifnull, the bot doesn't
have a default sending channel.
- default_events_register_stream:string | nullThe default channel for which the bot receives events/register data.
Ifnull, the bot doesn't have such a default channel.
- default_all_public_streams:booleanWhether the bot can send messages to all channels by default.
- services:(object | object)[]An array containing extra configuration fields only relevant for
outgoing webhook bots and embedded bots. This is always a single-element
array.We consider this part of the Zulip API to be unstable; it is used only
for UI elements for administering bots and is likely to change.When the bot is an outgoing webhook.base_url:stringThe URL the outgoing webhook is configured to post to.token:stringA unique token that the third-party service can use to confirm
that the request is indeed coming from Zulip.interface:integerAn integer indicating what format requests are posted in:1 = Zulip's native outgoing webhook format.2 = Emulate the Slack outgoing webhook format.When the bot is an embedded bot.service_name:stringThe name of the bot.config_data:objectA dictionary of string key/value pairs, which describe the configuration
for the bot. These are usually details like API keys, and are unique to
the integration/bot. Can be an empty dictionary.{config_key}:stringDescription/value of the configuration data key.
- When the bot is an outgoing webhook.base_url:stringThe URL the outgoing webhook is configured to post to.token:stringA unique token that the third-party service can use to confirm
that the request is indeed coming from Zulip.interface:integerAn integer indicating what format requests are posted in:1 = Zulip's native outgoing webhook format.2 = Emulate the Slack outgoing webhook format.
- When the bot is an embedded bot.service_name:stringThe name of the bot.config_data:objectA dictionary of string key/value pairs, which describe the configuration
for the bot. These are usually details like API keys, and are unique to
the integration/bot. Can be an empty dictionary.{config_key}:stringDescription/value of the configuration data key.
- base_url:stringThe URL the outgoing webhook is configured to post to.
- token:stringA unique token that the third-party service can use to confirm
that the request is indeed coming from Zulip.
- interface:integerAn integer indicating what format requests are posted in:1 = Zulip's native outgoing webhook format.2 = Emulate the Slack outgoing webhook format.
- 1 = Zulip's native outgoing webhook format.
- 2 = Emulate the Slack outgoing webhook format.
- service_name:stringThe name of the bot.
- config_data:objectA dictionary of string key/value pairs, which describe the configuration
for the bot. These are usually details like API keys, and are unique to
the integration/bot. Can be an empty dictionary.{config_key}:stringDescription/value of the configuration data key.
- {config_key}:stringDescription/value of the configuration data key.
Example

```
{"bot":{"default_all_public_streams":false,"default_events_register_stream":null,"default_sending_stream":null,"services":[],"user_id":36},"id":1,"op":"add","type":"realm_bot"}
```

```
{"bot":{"default_all_public_streams":false,"default_events_register_stream":null,"default_sending_stream":null,"services":[],"user_id":36},"id":1,"op":"add","type":"realm_bot"}
```

### realm_botop: update
Event sent to users who can administer a bot user when the bot is
configured. Clients may also receive arealm_userevent that
for changes in public data about the bot (name, etc.).
Therealm_userevents are sufficient for clients that
only need to interact with the bot; thisrealm_botevent
type is relevant only for administering bots.
Only organization administrators and the user who owns the bot will
receive this event.
Changes: Starting from Zulip 12.0 (feature level 474),
this event is not sent when updating bot's avatar, email, name or
owner and also when reactivating or deactivating a bot.
Starting from Zulip 12.0 (feature level 474), this event is
no longer sent when a bot's API key is regenerated. Clients now
useGET /bots/{bot_id}/api_keyto get
api key for the bot.

```
GET /bots/{bot_id}/api_key
```
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- bot:objectObject containing details about the changed bot.
It contains two properties: the user ID of the bot and
the property to be changed. The changed property is one
of the remaining properties listed below.user_id:integerThe user ID of the bot.default_sending_stream:string | nullThe default sending channel of the bot. Ifnull, the bot doesn't
have a default sending channel.default_events_register_stream:string | nullThe default channel for which the bot receives events/register data.
Ifnull, the bot doesn't have such a default channel.default_all_public_streams:booleanWhether the bot can send messages to all channels by default.services:(object | object)[]An array containing extra configuration fields only relevant for
outgoing webhook bots and embedded bots. This is always a single-element
array.We consider this part of the Zulip API to be unstable; it is used only
for UI elements for administering bots and is likely to change.When the bot is an outgoing webhook.base_url:stringThe URL the outgoing webhook is configured to post to.token:stringA unique token that the third-party service can use to confirm
that the request is indeed coming from Zulip.interface:integerAn integer indicating what format requests are posted in:1 = Zulip's native outgoing webhook format.2 = Emulate the Slack outgoing webhook format.When the bot is an embedded bot.service_name:stringThe name of the bot.config_data:objectA dictionary of string key/value pairs, which describe the configuration
for the bot. These are usually details like API keys, and are unique to
the integration/bot. Can be an empty dictionary.{config_key}:stringDescription/value of the configuration data key.
- user_id:integerThe user ID of the bot.
- default_sending_stream:string | nullThe default sending channel of the bot. Ifnull, the bot doesn't
have a default sending channel.
- default_events_register_stream:string | nullThe default channel for which the bot receives events/register data.
Ifnull, the bot doesn't have such a default channel.
- default_all_public_streams:booleanWhether the bot can send messages to all channels by default.
- services:(object | object)[]An array containing extra configuration fields only relevant for
outgoing webhook bots and embedded bots. This is always a single-element
array.We consider this part of the Zulip API to be unstable; it is used only
for UI elements for administering bots and is likely to change.When the bot is an outgoing webhook.base_url:stringThe URL the outgoing webhook is configured to post to.token:stringA unique token that the third-party service can use to confirm
that the request is indeed coming from Zulip.interface:integerAn integer indicating what format requests are posted in:1 = Zulip's native outgoing webhook format.2 = Emulate the Slack outgoing webhook format.When the bot is an embedded bot.service_name:stringThe name of the bot.config_data:objectA dictionary of string key/value pairs, which describe the configuration
for the bot. These are usually details like API keys, and are unique to
the integration/bot. Can be an empty dictionary.{config_key}:stringDescription/value of the configuration data key.
- When the bot is an outgoing webhook.base_url:stringThe URL the outgoing webhook is configured to post to.token:stringA unique token that the third-party service can use to confirm
that the request is indeed coming from Zulip.interface:integerAn integer indicating what format requests are posted in:1 = Zulip's native outgoing webhook format.2 = Emulate the Slack outgoing webhook format.
- When the bot is an embedded bot.service_name:stringThe name of the bot.config_data:objectA dictionary of string key/value pairs, which describe the configuration
for the bot. These are usually details like API keys, and are unique to
the integration/bot. Can be an empty dictionary.{config_key}:stringDescription/value of the configuration data key.
- base_url:stringThe URL the outgoing webhook is configured to post to.
- token:stringA unique token that the third-party service can use to confirm
that the request is indeed coming from Zulip.
- interface:integerAn integer indicating what format requests are posted in:1 = Zulip's native outgoing webhook format.2 = Emulate the Slack outgoing webhook format.
- 1 = Zulip's native outgoing webhook format.
- 2 = Emulate the Slack outgoing webhook format.
- service_name:stringThe name of the bot.
- config_data:objectA dictionary of string key/value pairs, which describe the configuration
for the bot. These are usually details like API keys, and are unique to
the integration/bot. Can be an empty dictionary.{config_key}:stringDescription/value of the configuration data key.
- {config_key}:stringDescription/value of the configuration data key.
Example

```
{"bot":{"services":[{"base_url":"http://hostname.domain2.com","interface":2,"token":"grr8I2APXRmVL0FRTMRYAE4DRPQ5Wlaw"}],"user_id":37},"id":0,"op":"update","type":"realm_bot"}
```

```
{"bot":{"services":[{"base_url":"http://hostname.domain2.com","interface":2,"token":"grr8I2APXRmVL0FRTMRYAE4DRPQ5Wlaw"}],"user_id":37},"id":0,"op":"update","type":"realm_bot"}
```

### realm_botop: remove
Event sent to all users when a bot has been deactivated.
Changes: Deprecated and no longer sent since Zulip 8.0 (feature level 222).
Previously, this event was sent to all users in a Zulip organization when a
bot was deactivated.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- bot:objectObject containing details about the deactivated bot.user_id:integerThe user ID of the deactivated bot.full_name:stringThe full name of the deactivated bot.
- user_id:integerThe user ID of the deactivated bot.
- full_name:stringThe full name of the deactivated bot.
Example

```
{"bot":{"full_name":"Foo Bot","user_id":35},"id":1,"op":"remove","type":"realm_bot"}
```

```
{"bot":{"full_name":"Foo Bot","user_id":35},"id":1,"op":"remove","type":"realm_bot"}
```

### realm_botop: delete
Event sent to all users when a bot has been deactivated.
Note that this is very similar to the bot_remove event
and one of them will be removed soon.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- bot:objectObject containing details about the deactivated bot.user_id:integerThe user ID of the deactivated bot.
- user_id:integerThe user ID of the deactivated bot.
Example

```
{"bot":{"user_id":35},"id":1,"op":"delete","type":"realm_bot"}
```

```
{"bot":{"user_id":35},"id":1,"op":"delete","type":"realm_bot"}
```

### realmop: update
The simpler of two possible event types sent to all users
in a Zulip organization when the configuration of the
organization (realm) has changed.
Often individual settings are migrated from this format to
therealm/update_dictevent format when additional realm
settings are added whose values are coupled to each other
in some way. The specific values supported by this event
type are documented in therealm/update_dictdocumentation.
A correct client implementation should convert these
events into the correspondingrealm/update_dictevent and then process that.
Changes: Removed therendered_descriptionproperty in
Zulip 12.0 (feature level 464). It had been briefly present only
since feature level 462 and can be safely ignored by all clients.
Removedextra_dataoptional property in Zulip 10.0 (feature level 306).
Theextra_dataused to include anupload_quotafield when changed
property wasplan_type. The server now sends a standardrealm/update_dictevent for plan changes.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- property:stringThe name of the property that was changed.
- value:string | boolean | integer | nullThe new value of the property.
Example

```
{"id":0,"op":"update","property":"disallow_disposable_email_addresses","type":"realm","value":false}
```

```
{"id":0,"op":"update","property":"disallow_disposable_email_addresses","type":"realm","value":false}
```

### realmop: deactivated
Event sent to all users in a Zulip organization when the
organization (realm) is deactivated. Its main purpose is to
flush active longpolling connections so clients can immediately
show the organization as deactivated.
Clients cannot rely on receiving this event, because they will
no longer be able to authenticate to the Zulip API due to the
deactivation, and thus can miss it if they did not have an active
longpolling connection at the moment of deactivation.
Correct handling of realm deactivations requires that clients
parse authentication errors from GET /events; if that is done
correctly, the client can ignore this event type and rely on its
handling of theGET /eventsrequest it will do immediately
after processing this batch of events.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- realm_id:integerThe ID of the deactivated realm.
Example

```
{"id":0,"op":"deactivated","realm_id":2,"type":"realm"}
```

```
{"id":0,"op":"deactivated","realm_id":2,"type":"realm"}
```

### restart
Event sent to all the users whenever the Zulip server restarts.
Specifically, this event is sent whenever the Tornado process
for the user is restarted; in particular, this will always happen
when the Zulip server is upgraded.
Clients should use this event to update their tracking of the
server's capabilities, and to decide if they wish to get a new
event queue after a server upgrade. Clients doing so must
implement a random delay strategy to spread such restarts over 5
minutes or more to avoid creating a synchronized thundering herd
effect.
Changes: Removed theimmediateflag, which was only used by
web clients in development, in Zulip 9.0 (feature level 240).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- zulip_version:stringThe Zulip version number, in the format where this appears
in theserver_settingsandregisterresponses.Changes: New in Zulip 4.0 (feature level 59).
- zulip_merge_base:stringThe Zulip merge base number, in the format where this appears
in theserver_settingsandregisterresponses.Changes: New in Zulip 5.0 (feature level 88).
- zulip_feature_level:integerTheZulip feature levelof the server
after the restart.Clients should use this to update their tracking of the
server's capabilities, and may choose to refetch their state
and create a new event queue when the API feature level has
changed in a way that the client finds significant. Clients
choosing to do so must implement a random delay strategy to
spread such restarts over 5 or more minutes to avoid creating
a synchronized thundering herd effect.Changes: New in Zulip 4.0 (feature level 59).
- server_generation:integerThe timestamp at which the server started.
Example

```
{"id":0,"server_generation":1619334181,"type":"restart","zulip_feature_level":57,"zulip_merge_base":"5.0-dev-1646-gea6b21cd8c","zulip_version":"5.0-dev-1650-gc3fd37755f"}
```

```
{"id":0,"server_generation":1619334181,"type":"restart","zulip_feature_level":57,"zulip_merge_base":"5.0-dev-1646-gea6b21cd8c","zulip_version":"5.0-dev-1650-gc3fd37755f"}
```

### web_reload_client
An event which signals the official Zulip web/desktop app to update,
by reloading the page and fetching a new queue; this will generally
follow arestartevent. Clients which do not obtain their code
from the server (e.g. mobile and terminal clients, which store their
code locally) should ignore this event.
Clients choosing to reload the application must implement a random
delay strategy to spread such restarts over 5 or more minutes to
avoid creating a synchronized thundering herd effect.
Changes: New in Zulip 9.0 (feature level 240).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- immediate:booleanWhether the client should fetch a new event queue immediately,
rather than using a backoff strategy to avoid thundering herds.
A Zulip development server uses this parameter to reload
clients immediately.
Example

```
{"id":0,"immediate":true,"type":"web_reload_client"}
```

```
{"id":0,"immediate":true,"type":"web_reload_client"}
```

### realmop: update_dict
The more general of two event types that may be used when
sending an event to all users in a Zulip organization when
the configuration of the organization (realm) has changed.
Unlike the simplerrealm/updateevent format, this
event type supports multiple properties being changed in a
single event.
This event is also sent when deactivating or reactivating a user
for settings set to anonymous user groups which the user is direct
member of. When deactivating the user, event is only sent to users
who cannot access the deactivated user.
Changes: Starting with Zulip 10.0 (feature level 303), this
event can also be sent when deactivating or reactivating a user.
In Zulip 7.0 (feature level 163), the realm settingemail_address_visibilitywas removed. It was replaced by auser
settingwith
arealm user default, with the encoding of different
values preserved. Clients can support all versions by supporting the
current API and treating every user as having the realm'semail_address_visibilityvalue.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- property:stringAlways"default". Present for backwards-compatibility with older
clients that predate theupdate_dictevent style.Deprecatedand will be removed in a future release.
- data:objectAn object containing the properties that have changed.Changes: In Zulip 10.0 (feature level 316),edit_topic_policyproperty was removed and replaced bycan_move_messages_between_topics_grouprealm setting.In Zulip 7.0 (feature level 183), thecommunity_topic_editing_limit_secondsproperty was removed.
It was documented as potentially returned as a changed property
in this event, but in fact it was only ever returned in thePOST /registerresponse.Before Zulip 6.0 (feature level 150), on changing any ofallow_message_editing,message_content_edit_limit_seconds, oredit_topic_policysettings, this object included all the three settings
irrespective of which of these settings were changed. Now, a separate event
is sent for each changed setting.allow_message_editing:booleanWhether this organization'smessage edit policyallows editing the content of messages.SeePATCH /messages/{message_id}for details and
history of how message editing permissions work.authentication_methods:objectDictionary of authentication method keys mapped to dictionaries that
describe the properties of the named authentication method for the
organization - its enabled status and availability for use by the
organization.Clients should use this to implement server-settings UI to change which
methods are enabled for the organization. For authentication UI itself,
clients should use the pre-authentication metadata returned byGET /server_settings.Changes: In Zulip 9.0 (feature level 243), the values in this
dictionary were changed. Previously, the values were a simple boolean
indicating whether the backend is enabled or not.Dictionary describing the properties of an authentication method for the
    organization - its enabled status and availability for use by the
    organization.enabled:booleanBoolean describing whether the authentication method (i.e. its key)
is enabled in this organization.available:booleanBoolean describing whether the authentication method is available for use.
If false, the organization is not eligible to enable the authentication
method.unavailable_reason:stringReason why the authentication method is unavailable. This field is optional
and is only present when 'available' is false.can_access_all_users_group:integer | objectAgroup-setting valuedefining the
set of users who are allowed to access all users in the
organization.Changes: Prior to Zulip 10.0 (feature level 314), this value used
to be of type integer and did not accept anonymous user groups.New in Zulip 8.0 (feature level 225).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_create_groups:integer | objectAgroup-setting valuedefining
the set of users who have permission to create user
groups in this organization.Changes: New in Zulip 10.0 (feature level 299). Previouslyuser_group_edit_policyfield used to control the permission
to create user groups.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_create_bots_group:integer | objectAgroup-setting valuedefining
the set of users who have permission to create all types of bot users
in the organization. See alsocan_create_write_only_bots_group.Changes: New in Zulip 10.0 (feature level 344). Previously, this
permission was controlled by the enumbot_creation_policy. Values
were 1=Members, 2=Generic bots limited to administrators, 3=Administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_create_write_only_bots_group:integer | objectAgroup-setting valuedefining
the set of users who have permission to create bot users that
can only send messages in the organization, i.e. incoming webhooks,
in addition to the users who are present incan_create_bots_group.Changes: New in Zulip 10.0 (feature level 344). Previously, this
permission was controlled by the enumbot_creation_policy. Values
were 1=Members, 2=Generic bots limited to administrators, 3=Administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_create_public_channel_group:integer | objectAgroup-setting valuedefining
the set of users who have permission to create public
channels in this organization.Changes: New in Zulip 9.0 (feature level 264). Previouslyrealm_create_public_stream_policyfield used to control the
permission to create public channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_create_private_channel_group:integer | objectAgroup-setting valuedefining
the set of users who have permission to create private
channels in this organization.Changes: New in Zulip 9.0 (feature level 266). Previouslyrealm_create_private_stream_policyfield used to control the
permission to create private channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_create_web_public_channel_group:integer | objectAgroup-setting valuedefining
the set of users who have permission to create web-public
channels in this organization.Changes: New in Zulip 10.0 (feature level 280). Previouslyrealm_create_web_public_stream_policyfield used to control
the permission to create web-public channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_add_custom_emoji_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to add custom emoji in the organization.Changes: New in Zulip 10.0 (feature level 307). Previously, this
permission was controlled by the enumadd_custom_emoji_policy. Values
were 1=Members, 2=Admins, 3=Full members, 4=Moderators.Before Zulip 5.0 (feature level 85), therealm_add_emoji_by_admins_onlyboolean setting controlled this permission;truecorresponded toAdmins,
andfalsetoEveryone.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_add_subscribers_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to add subscribers to channels in the organization.Changes: New in Zulip 10.0 (feature level 341). Previously, this
permission was controlled by the enuminvite_to_stream_policy. Values
were 1=Members, 2=Admins, 3=Full members, 4=Moderators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_delete_any_message_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to delete any message in the organization.Changes: New in Zulip 10.0 (feature level 281). Previously, this
permission was limited to administrators only and was uneditable.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_delete_own_message_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to delete messages that they have sent in the
organization.Changes: New in Zulip 10.0 (feature level 291). Previously, this
permission was controlled by the enumdelete_own_message_policy. Values
were 1=Members, 2=Admins, 3=Full members, 4=Moderators, 5=Everyone.Before Zulip 5.0 (feature level 101), theallow_message_deletingboolean
setting controlled this permission;truecorresponded toEveryone, andfalsetoAdmins.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_set_delete_message_policy_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to change per-channelcan_delete_any_message_groupandcan_delete_own_message_grouppermission settings. Note that the user
must be a member of both this group and thecan_administer_channel_groupof the channel whose message delete settings they want to change.Organization administrators can always change these settings of
every channel.Changes: New in Zulip 11.0 (feature level 407).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_set_topics_policy_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to change per-channeltopics_policysetting. Note that
the user must be a member of both this group and thecan_administer_channel_groupof the channel whosetopics_policythey want to change.Organization administrators can always change thetopics_policysetting of
every channel.Changes: New in Zulip 11.0 (feature level 392).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_invite_users_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to send email invitations for inviting other users
to the organization.Changes: New in Zulip 10.0 (feature level 321). Previously, this
permission was controlled by the enuminvite_to_realm_policy. Values
were 1=Members, 2=Admins, 3=Full members, 4=Moderators, 6=Nobody.Before Zulip 4.0 (feature level 50), theinvite_by_admins_onlyboolean
setting controlled this permission;truecorresponded toAdmins, andfalsetoMembers.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_mention_many_users_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to use wildcard mentions in large channels.All users will receive a warning/reminder when using mentions in large
channels, even when permitted to do so.Changes: New in Zulip 10.0 (feature level 352). Previously, this
permission was controlled by the enumwildcard_mention_policy.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_move_messages_between_channels_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to move messages from one channel to another
in the organization.Changes: New in Zulip 10.0 (feature level 310). Previously, this
permission was controlled by the enummove_messages_between_streams_policy.
Values were 1=Members, 2=Admins, 3=Full members, 4=Moderators, 6=Nobody.In Zulip 7.0 (feature level 159),Nobodywas added as an option tomove_messages_between_streams_policyenum.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_move_messages_between_topics_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to move messages from one topic to another
within a channel in the organization.Changes: New in Zulip 10.0 (feature level 316). Previously, this
permission was controlled by the enumedit_topic_policy. Values were
1=Members, 2=Admins, 3=Full members, 4=Moderators, 5=Everyone, 6=Nobody.In Zulip 7.0 (feature level 159),Nobodywas added as an option toedit_topic_policyenum.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_resolve_topics_group:integer | objectAgroup-setting valuedefining
the set of users who have permission toresolve topicsin the organization.Changes: New in Zulip 10.0 (feature level 367). Previously, permission to
resolve topics was controlled by the more general
can_move_messages_between_topics_group permission for moving messages.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_manage_all_groups:integer | objectAgroup-setting valuedefining the set of users who have permission to
administer all existing groups in this organization.Changes: Prior to Zulip 10.0 (feature level 305), only users who
were a member of the group or had the moderator role or above could
exercise the permission on a given group.New in Zulip 10.0 (feature level 299). Previously theuser_group_edit_policyfield controlled the permission
to manage user groups. Valid values were as follows:1 = All members can create and edit user groups2 = Only organization administrators can create and edit
  user groups3 = Onlyfull memberscan create and
  edit user groups.4 = Only organization administrators and moderators can
  create and edit user groups.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_manage_billing_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to manage plans and billing in the organization.Changes: New in Zulip 10.0 (feature level 363). Previously, only owners
and users withis_billing_adminproperty set totruewere allowed to
manage plans and billing.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_summarize_topics_group:integer | objectAgroup-setting valuedefining the
set of users who are allowed to use AI summarization.Changes: New in Zulip 10.0 (feature level 350).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.create_multiuse_invite_group:integer | objectAgroup-setting valuedefining the
set of users who are allowed to createreusable invitation
linksto the organization.Changes: Prior to Zulip 10.0 (feature level 314), this value used
to be of type integer and did not accept anonymous user groups.New in Zulip 8.0 (feature level 209).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.default_avatar_source:stringThe avatar data source type for new users."G" = Hosted by Gravatar"J" = Generated using JdenticonNote that "U" is not a supported value here, since there is
no such thing as a "default" user-uploaded avatar.Changes: New in Zulip 12.0 (feature level 456).default_code_block_language:stringThe default pygments language code to be used for code blocks in this
organization. If an empty string, no default has been set.Changes: Prior to Zulip 8.0 (feature level 195), a server bug meant
that bothnulland an empty string could represent that no default was
set for this realm setting in thePOST /registerresponse. The documentation for both that endpoint and this event
incorrectly stated that the only representation for no default language
wasnull. This event in fact uses the empty string to indicate that no
default has been set in all server versions.default_language:stringThe default language for the organization.description:stringThe description of the organization, used on login and registration pages.digest_emails_enabled:booleanWhether the organization has enabledweekly digest emails.digest_weekday:integerThe day of the week when the organization will send
its weekly digest email to inactive users.direct_message_initiator_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to start a new direct message conversation
involving other non-bot users. Users who are outside this group and attempt
to send the first direct message to a given collection of recipient users
will receive an error, unless all other recipients are bots or the sender.Changes: New in Zulip 9.0 (feature level 270).Previously, access to send direct messages was controlled by theprivate_message_policyrealm setting, which supported values of
1 (enabled) and 2 (disabled).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.direct_message_permission_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to fully use direct messages. Users outside
this group can only send direct messages to conversations where all the
recipients are in this group, are bots, or are the sender, ensuring that
every direct message conversation will be visible to at least one user in
this group.Changes: New in Zulip 9.0 (feature level 270).Previously, access to send direct messages was controlled by theprivate_message_policyrealm setting, which supported values of
1 (enabled) and 2 (disabled).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.disallow_disposable_email_addresses:booleanWhether the organization disallows disposable email
addresses.email_changes_disabled:booleanWhether users are allowed to change their own email address in this
organization. This is typically disabled for organizations that
synchronize accounts from LDAP or a similar corporate database.enable_read_receipts:booleanWhether read receipts is enabled in the organization or not.If disabled, read receipt data will be unavailable to clients, regardless
of individual users' personal read receipt settings. See also thesend_read_receiptssetting withinrealm_user_settings_defaults.Changes: New in Zulip 6.0 (feature level 137).emails_restricted_to_domains:booleanWhethernew users joiningthis organization are required to have an email
address in one of therealm_domainsconfigured for the organization.enable_guest_user_dm_warning:booleanWhether clients should show a warning when a user is composing
a DM to a guest user in this organization.Changes: New in Zulip 10.0 (feature level 348).enable_guest_user_indicator:booleanWhether clients should display "(guest)" after the names of
guest users to prominently highlight their status.Changes: New in Zulip 8.0 (feature level 216).enable_spectator_access:booleanWhether web-public channels are enabled in this organization.Can only be enabled if theWEB_PUBLIC_STREAMS_ENABLEDserver settingis enabled on the Zulip
server. See also thecan_create_web_public_channel_grouprealm setting.Changes: New in Zulip 5.0 (feature level 109).gif_rating_policy:integerMaximum rating of the GIFs that will be retrieved by the
GIPHY and Tenor integrations in this organization.Changes: Before Zulip 12.0 (feature level 453),
this was calledgiphy_rating.Before Zulip 12.0 (feature level 442), this was only used
for the Giphy integration.New in Zulip 4.0 (feature level 55).icon_source:stringString indicating whether the organization'sprofile iconwas uploaded
by a user or is the default. Useful for UI allowing editing the organization's icon."G" means generated by Gravatar (the default)."U" means uploaded by an organization administrator.icon_url:stringThe URL of the organization'sprofile icon.media_preview_size:integerThe organization's policy for the size of image and video
thumbnails in messages, expressed as a percentage of the
default height. Currently, only certain values are permitted.100: 100% height (the default).150: 150% height.200: 200% height.Changes: New in Zulip 12.0 (feature level 469).inline_image_preview:booleanWhether this organization has been configured to enablepreviews of linked images.inline_url_embed_preview:booleanWhether this organization has been configured to enablepreviews of linked websites.invite_required:booleanWhether an invitation is required to join this organization.jitsi_server_url:string | nullThe URL of the custom Jitsi Meet server configured in this organization's
settings.null, the default, means that the organization is using the should use the
server-level configuration,server_jitsi_server_url.Changes: New in Zulip 8.0 (feature level 212). Previously, this was only
available as a server-level configuration, and required a server restart to
change.logo_source:stringString indicating whether the organization'sprofile wide logowas uploaded
by a user or is the default. Useful for UI allowing editing the
organization's wide logo."D" means the logo is the default Zulip logo."U" means uploaded by an organization administrator.logo_url:stringThe URL of the organization's wide logo configured in theorganization profile.topics_policy:stringThe organization's default policy for sending channel messages to theempty "general chat" topic."allow_empty_topic": Channel messages can be sent to the empty topic."disable_empty_topic": Channel messages cannot be sent to the empty topic.Changes: New in Zulip 11.0 (feature level 392). Previously, this was
controlled by the boolean realmmandatory_topicssetting, which is now
deprecated.mandatory_topics:booleanWhethertopics are requiredfor messages in this
organization.Changes: Deprecated in Zulip 11.0 (feature level 392). This is now
controlled by the realmtopics_policysetting.max_file_upload_size_mib:integerThe new maximum file size that can be uploaded to this Zulip organization.Changes: New in Zulip 10.0 (feature level 306). Previously, this field of
the core state did not support being updated via the events system, as it was
typically hardcoded for a given Zulip installation.message_content_allowed_in_email_notifications:booleanWhether notification emails in this organization are allowed to
contain Zulip the message content, or simply indicate that a new
message was sent.message_content_delete_limit_seconds:integer | nullMessages sent more than this many seconds ago cannot be deleted
with this organization'smessage deletion policy.Will not be 0. Anullvalue means no limit: messages can be deleted
regardless of how long ago they were sent.Changes: No limit was represented using the
special value0before Zulip 5.0 (feature level 100).message_content_edit_limit_seconds:integer | nullMessages sent more than this many seconds ago cannot be edited
with this organization'smessage edit policy.Will not be0. Anullvalue means no limit, so messages can be edited
regardless of how long ago they were sent.SeePATCH /messages/{message_id}for details and
history of how message editing permissions work.Changes: Before Zulip 6.0 (feature level 138), no limit was
represented using the special value0.message_edit_history_visibility_policy:stringWhich type of message edit history is configured to allow users to
accessmessage edit history."all" = All edit history is visible."moves" = Only moves are visible."none" = No edit history is visible.Changes: New in Zulip 10.0 (feature level 358), replacing the previousallow_edit_historyboolean setting;truecorresponds toall,
andfalsetonone.moderation_request_channel_id:integerThe ID of the private channel to which messages flagged by users for
moderation are sent. Moderators can use this channel to review and
act on reported content.Will be-1if moderation requests are disabled.Clients should check whether moderation requests are disabled to
determine whether to present a "report message" feature in their UI
within a given organization.Changes: New in Zulip 10.0 (feature level 331). Previously,
no "report message" features existed in Zulip.move_messages_within_stream_limit_seconds:integer | nullMessages sent more than this many seconds ago cannot be moved within a
channel to another topic by users who have permission to do so based on this
organization'stopic edit policy. This
setting does not affect moderators and administrators.Will not be0. Anullvalue means no limit, so message topics can be
edited regardless of how long ago they were sent.SeePATCH /messages/{message_id}for details and
history of how message editing permissions work.Changes: New in Zulip 7.0 (feature level 162). Previously, this time
limit was always 72 hours for users who were not administrators or
moderators.move_messages_between_streams_limit_seconds:integer | nullMessages sent more than this many seconds ago cannot be moved between
channels by users who have permission to do so based on this organization'smessage move policy. This setting does
not affect moderators and administrators.Will not be0. Anullvalue means no limit, so messages can be moved
regardless of how long ago they were sent.SeePATCH /messages/{message_id}for details and
history of how message editing permissions work.Changes: New in Zulip 7.0 (feature level 162). Previously, there was
no time limit for moving messages between channels for users with permission
to do so.name:stringThe name of the organization, used in login pages etc.name_changes_disabled:booleanIndicates whether users areallowed to changetheir name
via the Zulip UI in this organization. Typically disabled
in organizations syncing this type of account information from
an external user database like LDAP.night_logo_source:stringString indicating whether the organization's dark themeprofile wide logowas uploaded
by a user or is the default. Useful for UI allowing editing the
organization's wide logo."D" means the logo is the default Zulip logo."U" means uploaded by an organization administrator.night_logo_url:stringThe URL of the organization's dark theme wide-format logo configured in theorganization profile.new_stream_announcements_stream_id:integerThe ID of the channel to which automated messages announcing thecreation of new channelsare sent.Will be-1if such automated messages are disabled.Since these automated messages are sent by the server, this field is
primarily relevant to clients containing UI for changing it.Changes: In Zulip 9.0 (feature level 241), renamednotifications_stream_idtonew_stream_announcements_stream_id.org_type:integerTheorganization typefor the realm.0 = Unspecified10 = Business20 = Open-source project30 = Education (non-profit)35 = Education (for-profit)40 = Research50 = Event or conference60 = Non-profit (registered)70 = Government80 = Political group90 = Community100 = Personal1000 = OtherChanges: New in Zulip 6.0 (feature level 128).plan_type:integerThe plan type of the organization.1 = Self-hosted organization (SELF_HOSTED)2 = Zulip Cloud free plan (LIMITED)3 = Zulip Cloud Standard plan (STANDARD)4 = Zulip Cloud Standard plan, sponsored for free (STANDARD_FREE)presence_disabled:booleanWhether online presence of other users is shown in this
organization.push_notifications_enabled:booleanWhether push notifications are enabled for this organization. Typicallytruefor Zulip Cloud and self-hosted realms that have a valid
registration for theMobile push notifications
service,
andfalsefor self-hosted servers that do not.Changes: New in Zulip 8.0 (feature level 231).
Previously, this value was never updated via events.push_notifications_enabled_end_timestamp:integer | nullIf the server expects the realm's push notifications access to end at a
definite time in the future, the time at which this is expected to happen.
Mobile clients should use this field to display warnings to users when the
indicated timestamp is near.Changes: New in Zulip 8.0 (feature level 231).rendered_description:stringNote: Only present if the changed property wasdescription.The organization description rendered as HTML, intended to
be used when displaying the organization description in a UI.One should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax
work correctly. And any client-side security logic for
user-generated message content should be applied when displaying
this HTML as though it were the body of a Zulip message.Changes: New in Zulip 12.0 (feature level 464). Previously
in feature levels 462-463, anupdateevent had been sent
when updating the realm'sdescription.require_e2ee_push_notifications:booleanWhether this realm is configured to disallow sending mobile
push notifications with message content through the legacy
mobile push notifications APIs. The new API uses end-to-end
encryption to protect message content and metadata from
being accessible to the push bouncer service, APNs, and
FCM. Clients that support the new E2EE API will use it
automatically regardless of this setting.Iftrue, mobile push notifications sent to clients that
lack support for E2EE push notifications will always have
"New message" as their content. Note that these legacy
mobile notifications will still contain metadata, which may
include the message's ID, the sender's name, email address,
and avatar.In a future release, once the official mobile apps have
implemented fully validated their E2EE protocol support,
this setting will become strict, and disable the legacy
protocol entirely.Changes: New in Zulip 11.0 (feature level 409). Previously,
this behavior was available only via thePUSH_NOTIFICATION_REDACT_CONTENTglobal server setting.require_unique_names:booleanIndicates whether the organization is configured to require users to have
unique full names. If true, the server will reject attempts to create a
new user, or change the name of an existing user, where doing so would
lead to two users whose names are identical modulo case and unicode
normalization.Changes: New in Zulip 9.0 (feature level 246). Previously, the Zulip
server could not be configured to enforce unique names.send_channel_events_messages:booleanIndicates whether channel event messages are sent in this organization.Changes: New in Zulip 12.0 (feature level 434). Previously,
channel events were sent unconditionally.send_welcome_emails:booleanWhether or not this organization is configured to send the standard Zulipwelcome emailsto new users joining the organization.signup_announcements_stream_id:integerThe ID of the channel to which automated messages announcing
thatnew users have joined the organizationare sent.Will be-1if such automated messages are disabled.Since these automated messages are sent by the server, this field is
primarily relevant to clients containing UI for changing it.Changes: In Zulip 9.0 (feature level 241), renamedsignup_notifications_stream_idtosignup_announcements_stream_id.upload_quota_mib:integer | nullThe new upload quota for the Zulip organization.Ifnull, there is no limit.Changes: New in Zulip 10.0 (feature level 306). Previously,
this was present changed via anupload_quotafield inextra_dataproperty
ofrealm/updateevent format forplan_typeevents.video_chat_provider:integerThe configuredvideo call providerfor the
organization.0 = None1 = Jitsi Meet3 = Zoom (User OAuth integration)4 = BigBlueButton5 = Zoom (Server to Server OAuth integration)6 = Constructor Groups7 = Nextcloud TalkNote that only one of theZoom integrationscan
be configured on a Zulip server.Changes: In Zulip 12.0 (feature level 465), added the
Constructor Groups option.In Zulip 12.0 (feature level 460), added the
Constructor Groups option.In Zulip 10.0 (feature level 353), added the Zoom Server
to Server OAuth option.In Zulip 3.0 (feature level 1), added the None option
to disable video call UI.waiting_period_threshold:integerMembers whose accounts have been created at least this many days ago
will be treated asfull membersfor the purpose of settings that restrict access to new members.want_advertise_in_communities_directory:booleanWhether the organization has given permission to be advertised in the
Zulipcommunities directory.Changes: New in Zulip 6.0 (feature level 129).welcome_message_custom_text:stringThis organization's configured custom message for Welcome Bot
to send to new user accounts, in Zulip Markdown format.Maximum length is 8000 Unicode code points.Changes: New in Zulip 11.0 (feature level 416).workplace_users_group:integer | objectAgroup-setting valuedefining the set of
users who will be considered as workplace users for billing.Changes: New in Zulip 12.0 (feature level 477).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.zulip_update_announcements_stream_id:integerThe ID of the channel to which automated messages announcing
new features or other end-user updates about the Zulip software are sent.Will be-1if such automated messages are disabled.Since these automated messages are sent by the server, this field is
primarily relevant to clients containing UI for changing it.Changes: New in Zulip 9.0 (feature level 242).

```
POST /register
```
- allow_message_editing:booleanWhether this organization'smessage edit policyallows editing the content of messages.SeePATCH /messages/{message_id}for details and
history of how message editing permissions work.
- authentication_methods:objectDictionary of authentication method keys mapped to dictionaries that
describe the properties of the named authentication method for the
organization - its enabled status and availability for use by the
organization.Clients should use this to implement server-settings UI to change which
methods are enabled for the organization. For authentication UI itself,
clients should use the pre-authentication metadata returned byGET /server_settings.Changes: In Zulip 9.0 (feature level 243), the values in this
dictionary were changed. Previously, the values were a simple boolean
indicating whether the backend is enabled or not.Dictionary describing the properties of an authentication method for the
    organization - its enabled status and availability for use by the
    organization.enabled:booleanBoolean describing whether the authentication method (i.e. its key)
is enabled in this organization.available:booleanBoolean describing whether the authentication method is available for use.
If false, the organization is not eligible to enable the authentication
method.unavailable_reason:stringReason why the authentication method is unavailable. This field is optional
and is only present when 'available' is false.
- can_access_all_users_group:integer | objectAgroup-setting valuedefining the
set of users who are allowed to access all users in the
organization.Changes: Prior to Zulip 10.0 (feature level 314), this value used
to be of type integer and did not accept anonymous user groups.New in Zulip 8.0 (feature level 225).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_create_groups:integer | objectAgroup-setting valuedefining
the set of users who have permission to create user
groups in this organization.Changes: New in Zulip 10.0 (feature level 299). Previouslyuser_group_edit_policyfield used to control the permission
to create user groups.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_create_bots_group:integer | objectAgroup-setting valuedefining
the set of users who have permission to create all types of bot users
in the organization. See alsocan_create_write_only_bots_group.Changes: New in Zulip 10.0 (feature level 344). Previously, this
permission was controlled by the enumbot_creation_policy. Values
were 1=Members, 2=Generic bots limited to administrators, 3=Administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_create_write_only_bots_group:integer | objectAgroup-setting valuedefining
the set of users who have permission to create bot users that
can only send messages in the organization, i.e. incoming webhooks,
in addition to the users who are present incan_create_bots_group.Changes: New in Zulip 10.0 (feature level 344). Previously, this
permission was controlled by the enumbot_creation_policy. Values
were 1=Members, 2=Generic bots limited to administrators, 3=Administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_create_public_channel_group:integer | objectAgroup-setting valuedefining
the set of users who have permission to create public
channels in this organization.Changes: New in Zulip 9.0 (feature level 264). Previouslyrealm_create_public_stream_policyfield used to control the
permission to create public channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_create_private_channel_group:integer | objectAgroup-setting valuedefining
the set of users who have permission to create private
channels in this organization.Changes: New in Zulip 9.0 (feature level 266). Previouslyrealm_create_private_stream_policyfield used to control the
permission to create private channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_create_web_public_channel_group:integer | objectAgroup-setting valuedefining
the set of users who have permission to create web-public
channels in this organization.Changes: New in Zulip 10.0 (feature level 280). Previouslyrealm_create_web_public_stream_policyfield used to control
the permission to create web-public channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_add_custom_emoji_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to add custom emoji in the organization.Changes: New in Zulip 10.0 (feature level 307). Previously, this
permission was controlled by the enumadd_custom_emoji_policy. Values
were 1=Members, 2=Admins, 3=Full members, 4=Moderators.Before Zulip 5.0 (feature level 85), therealm_add_emoji_by_admins_onlyboolean setting controlled this permission;truecorresponded toAdmins,
andfalsetoEveryone.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_add_subscribers_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to add subscribers to channels in the organization.Changes: New in Zulip 10.0 (feature level 341). Previously, this
permission was controlled by the enuminvite_to_stream_policy. Values
were 1=Members, 2=Admins, 3=Full members, 4=Moderators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_delete_any_message_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to delete any message in the organization.Changes: New in Zulip 10.0 (feature level 281). Previously, this
permission was limited to administrators only and was uneditable.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_delete_own_message_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to delete messages that they have sent in the
organization.Changes: New in Zulip 10.0 (feature level 291). Previously, this
permission was controlled by the enumdelete_own_message_policy. Values
were 1=Members, 2=Admins, 3=Full members, 4=Moderators, 5=Everyone.Before Zulip 5.0 (feature level 101), theallow_message_deletingboolean
setting controlled this permission;truecorresponded toEveryone, andfalsetoAdmins.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_set_delete_message_policy_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to change per-channelcan_delete_any_message_groupandcan_delete_own_message_grouppermission settings. Note that the user
must be a member of both this group and thecan_administer_channel_groupof the channel whose message delete settings they want to change.Organization administrators can always change these settings of
every channel.Changes: New in Zulip 11.0 (feature level 407).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_set_topics_policy_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to change per-channeltopics_policysetting. Note that
the user must be a member of both this group and thecan_administer_channel_groupof the channel whosetopics_policythey want to change.Organization administrators can always change thetopics_policysetting of
every channel.Changes: New in Zulip 11.0 (feature level 392).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_invite_users_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to send email invitations for inviting other users
to the organization.Changes: New in Zulip 10.0 (feature level 321). Previously, this
permission was controlled by the enuminvite_to_realm_policy. Values
were 1=Members, 2=Admins, 3=Full members, 4=Moderators, 6=Nobody.Before Zulip 4.0 (feature level 50), theinvite_by_admins_onlyboolean
setting controlled this permission;truecorresponded toAdmins, andfalsetoMembers.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_mention_many_users_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to use wildcard mentions in large channels.All users will receive a warning/reminder when using mentions in large
channels, even when permitted to do so.Changes: New in Zulip 10.0 (feature level 352). Previously, this
permission was controlled by the enumwildcard_mention_policy.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_move_messages_between_channels_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to move messages from one channel to another
in the organization.Changes: New in Zulip 10.0 (feature level 310). Previously, this
permission was controlled by the enummove_messages_between_streams_policy.
Values were 1=Members, 2=Admins, 3=Full members, 4=Moderators, 6=Nobody.In Zulip 7.0 (feature level 159),Nobodywas added as an option tomove_messages_between_streams_policyenum.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_move_messages_between_topics_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to move messages from one topic to another
within a channel in the organization.Changes: New in Zulip 10.0 (feature level 316). Previously, this
permission was controlled by the enumedit_topic_policy. Values were
1=Members, 2=Admins, 3=Full members, 4=Moderators, 5=Everyone, 6=Nobody.In Zulip 7.0 (feature level 159),Nobodywas added as an option toedit_topic_policyenum.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_resolve_topics_group:integer | objectAgroup-setting valuedefining
the set of users who have permission toresolve topicsin the organization.Changes: New in Zulip 10.0 (feature level 367). Previously, permission to
resolve topics was controlled by the more general
can_move_messages_between_topics_group permission for moving messages.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_manage_all_groups:integer | objectAgroup-setting valuedefining the set of users who have permission to
administer all existing groups in this organization.Changes: Prior to Zulip 10.0 (feature level 305), only users who
were a member of the group or had the moderator role or above could
exercise the permission on a given group.New in Zulip 10.0 (feature level 299). Previously theuser_group_edit_policyfield controlled the permission
to manage user groups. Valid values were as follows:1 = All members can create and edit user groups2 = Only organization administrators can create and edit
  user groups3 = Onlyfull memberscan create and
  edit user groups.4 = Only organization administrators and moderators can
  create and edit user groups.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_manage_billing_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to manage plans and billing in the organization.Changes: New in Zulip 10.0 (feature level 363). Previously, only owners
and users withis_billing_adminproperty set totruewere allowed to
manage plans and billing.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_summarize_topics_group:integer | objectAgroup-setting valuedefining the
set of users who are allowed to use AI summarization.Changes: New in Zulip 10.0 (feature level 350).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- create_multiuse_invite_group:integer | objectAgroup-setting valuedefining the
set of users who are allowed to createreusable invitation
linksto the organization.Changes: Prior to Zulip 10.0 (feature level 314), this value used
to be of type integer and did not accept anonymous user groups.New in Zulip 8.0 (feature level 209).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- default_avatar_source:stringThe avatar data source type for new users."G" = Hosted by Gravatar"J" = Generated using JdenticonNote that "U" is not a supported value here, since there is
no such thing as a "default" user-uploaded avatar.Changes: New in Zulip 12.0 (feature level 456).
- default_code_block_language:stringThe default pygments language code to be used for code blocks in this
organization. If an empty string, no default has been set.Changes: Prior to Zulip 8.0 (feature level 195), a server bug meant
that bothnulland an empty string could represent that no default was
set for this realm setting in thePOST /registerresponse. The documentation for both that endpoint and this event
incorrectly stated that the only representation for no default language
wasnull. This event in fact uses the empty string to indicate that no
default has been set in all server versions.
- default_language:stringThe default language for the organization.
- description:stringThe description of the organization, used on login and registration pages.
- digest_emails_enabled:booleanWhether the organization has enabledweekly digest emails.
- digest_weekday:integerThe day of the week when the organization will send
its weekly digest email to inactive users.
- direct_message_initiator_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to start a new direct message conversation
involving other non-bot users. Users who are outside this group and attempt
to send the first direct message to a given collection of recipient users
will receive an error, unless all other recipients are bots or the sender.Changes: New in Zulip 9.0 (feature level 270).Previously, access to send direct messages was controlled by theprivate_message_policyrealm setting, which supported values of
1 (enabled) and 2 (disabled).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_message_permission_group:integer | objectAgroup-setting valuedefining the set of
users who have permission to fully use direct messages. Users outside
this group can only send direct messages to conversations where all the
recipients are in this group, are bots, or are the sender, ensuring that
every direct message conversation will be visible to at least one user in
this group.Changes: New in Zulip 9.0 (feature level 270).Previously, access to send direct messages was controlled by theprivate_message_policyrealm setting, which supported values of
1 (enabled) and 2 (disabled).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- disallow_disposable_email_addresses:booleanWhether the organization disallows disposable email
addresses.
- email_changes_disabled:booleanWhether users are allowed to change their own email address in this
organization. This is typically disabled for organizations that
synchronize accounts from LDAP or a similar corporate database.
- enable_read_receipts:booleanWhether read receipts is enabled in the organization or not.If disabled, read receipt data will be unavailable to clients, regardless
of individual users' personal read receipt settings. See also thesend_read_receiptssetting withinrealm_user_settings_defaults.Changes: New in Zulip 6.0 (feature level 137).
- emails_restricted_to_domains:booleanWhethernew users joiningthis organization are required to have an email
address in one of therealm_domainsconfigured for the organization.
- enable_guest_user_dm_warning:booleanWhether clients should show a warning when a user is composing
a DM to a guest user in this organization.Changes: New in Zulip 10.0 (feature level 348).
- enable_guest_user_indicator:booleanWhether clients should display "(guest)" after the names of
guest users to prominently highlight their status.Changes: New in Zulip 8.0 (feature level 216).
- enable_spectator_access:booleanWhether web-public channels are enabled in this organization.Can only be enabled if theWEB_PUBLIC_STREAMS_ENABLEDserver settingis enabled on the Zulip
server. See also thecan_create_web_public_channel_grouprealm setting.Changes: New in Zulip 5.0 (feature level 109).
- gif_rating_policy:integerMaximum rating of the GIFs that will be retrieved by the
GIPHY and Tenor integrations in this organization.Changes: Before Zulip 12.0 (feature level 453),
this was calledgiphy_rating.Before Zulip 12.0 (feature level 442), this was only used
for the Giphy integration.New in Zulip 4.0 (feature level 55).
- icon_source:stringString indicating whether the organization'sprofile iconwas uploaded
by a user or is the default. Useful for UI allowing editing the organization's icon."G" means generated by Gravatar (the default)."U" means uploaded by an organization administrator.
- icon_url:stringThe URL of the organization'sprofile icon.
- media_preview_size:integerThe organization's policy for the size of image and video
thumbnails in messages, expressed as a percentage of the
default height. Currently, only certain values are permitted.100: 100% height (the default).150: 150% height.200: 200% height.Changes: New in Zulip 12.0 (feature level 469).
- inline_image_preview:booleanWhether this organization has been configured to enablepreviews of linked images.
- inline_url_embed_preview:booleanWhether this organization has been configured to enablepreviews of linked websites.
- invite_required:booleanWhether an invitation is required to join this organization.
- jitsi_server_url:string | nullThe URL of the custom Jitsi Meet server configured in this organization's
settings.null, the default, means that the organization is using the should use the
server-level configuration,server_jitsi_server_url.Changes: New in Zulip 8.0 (feature level 212). Previously, this was only
available as a server-level configuration, and required a server restart to
change.
- logo_source:stringString indicating whether the organization'sprofile wide logowas uploaded
by a user or is the default. Useful for UI allowing editing the
organization's wide logo."D" means the logo is the default Zulip logo."U" means uploaded by an organization administrator.
- logo_url:stringThe URL of the organization's wide logo configured in theorganization profile.
- topics_policy:stringThe organization's default policy for sending channel messages to theempty "general chat" topic."allow_empty_topic": Channel messages can be sent to the empty topic."disable_empty_topic": Channel messages cannot be sent to the empty topic.Changes: New in Zulip 11.0 (feature level 392). Previously, this was
controlled by the boolean realmmandatory_topicssetting, which is now
deprecated.
- mandatory_topics:booleanWhethertopics are requiredfor messages in this
organization.Changes: Deprecated in Zulip 11.0 (feature level 392). This is now
controlled by the realmtopics_policysetting.
- max_file_upload_size_mib:integerThe new maximum file size that can be uploaded to this Zulip organization.Changes: New in Zulip 10.0 (feature level 306). Previously, this field of
the core state did not support being updated via the events system, as it was
typically hardcoded for a given Zulip installation.
- message_content_allowed_in_email_notifications:booleanWhether notification emails in this organization are allowed to
contain Zulip the message content, or simply indicate that a new
message was sent.
- message_content_delete_limit_seconds:integer | nullMessages sent more than this many seconds ago cannot be deleted
with this organization'smessage deletion policy.Will not be 0. Anullvalue means no limit: messages can be deleted
regardless of how long ago they were sent.Changes: No limit was represented using the
special value0before Zulip 5.0 (feature level 100).
- message_content_edit_limit_seconds:integer | nullMessages sent more than this many seconds ago cannot be edited
with this organization'smessage edit policy.Will not be0. Anullvalue means no limit, so messages can be edited
regardless of how long ago they were sent.SeePATCH /messages/{message_id}for details and
history of how message editing permissions work.Changes: Before Zulip 6.0 (feature level 138), no limit was
represented using the special value0.
- message_edit_history_visibility_policy:stringWhich type of message edit history is configured to allow users to
accessmessage edit history."all" = All edit history is visible."moves" = Only moves are visible."none" = No edit history is visible.Changes: New in Zulip 10.0 (feature level 358), replacing the previousallow_edit_historyboolean setting;truecorresponds toall,
andfalsetonone.
- moderation_request_channel_id:integerThe ID of the private channel to which messages flagged by users for
moderation are sent. Moderators can use this channel to review and
act on reported content.Will be-1if moderation requests are disabled.Clients should check whether moderation requests are disabled to
determine whether to present a "report message" feature in their UI
within a given organization.Changes: New in Zulip 10.0 (feature level 331). Previously,
no "report message" features existed in Zulip.
- move_messages_within_stream_limit_seconds:integer | nullMessages sent more than this many seconds ago cannot be moved within a
channel to another topic by users who have permission to do so based on this
organization'stopic edit policy. This
setting does not affect moderators and administrators.Will not be0. Anullvalue means no limit, so message topics can be
edited regardless of how long ago they were sent.SeePATCH /messages/{message_id}for details and
history of how message editing permissions work.Changes: New in Zulip 7.0 (feature level 162). Previously, this time
limit was always 72 hours for users who were not administrators or
moderators.
- move_messages_between_streams_limit_seconds:integer | nullMessages sent more than this many seconds ago cannot be moved between
channels by users who have permission to do so based on this organization'smessage move policy. This setting does
not affect moderators and administrators.Will not be0. Anullvalue means no limit, so messages can be moved
regardless of how long ago they were sent.SeePATCH /messages/{message_id}for details and
history of how message editing permissions work.Changes: New in Zulip 7.0 (feature level 162). Previously, there was
no time limit for moving messages between channels for users with permission
to do so.
- name:stringThe name of the organization, used in login pages etc.
- name_changes_disabled:booleanIndicates whether users areallowed to changetheir name
via the Zulip UI in this organization. Typically disabled
in organizations syncing this type of account information from
an external user database like LDAP.
- night_logo_source:stringString indicating whether the organization's dark themeprofile wide logowas uploaded
by a user or is the default. Useful for UI allowing editing the
organization's wide logo."D" means the logo is the default Zulip logo."U" means uploaded by an organization administrator.
- night_logo_url:stringThe URL of the organization's dark theme wide-format logo configured in theorganization profile.
- new_stream_announcements_stream_id:integerThe ID of the channel to which automated messages announcing thecreation of new channelsare sent.Will be-1if such automated messages are disabled.Since these automated messages are sent by the server, this field is
primarily relevant to clients containing UI for changing it.Changes: In Zulip 9.0 (feature level 241), renamednotifications_stream_idtonew_stream_announcements_stream_id.
- org_type:integerTheorganization typefor the realm.0 = Unspecified10 = Business20 = Open-source project30 = Education (non-profit)35 = Education (for-profit)40 = Research50 = Event or conference60 = Non-profit (registered)70 = Government80 = Political group90 = Community100 = Personal1000 = OtherChanges: New in Zulip 6.0 (feature level 128).
- plan_type:integerThe plan type of the organization.1 = Self-hosted organization (SELF_HOSTED)2 = Zulip Cloud free plan (LIMITED)3 = Zulip Cloud Standard plan (STANDARD)4 = Zulip Cloud Standard plan, sponsored for free (STANDARD_FREE)
- presence_disabled:booleanWhether online presence of other users is shown in this
organization.
- push_notifications_enabled:booleanWhether push notifications are enabled for this organization. Typicallytruefor Zulip Cloud and self-hosted realms that have a valid
registration for theMobile push notifications
service,
andfalsefor self-hosted servers that do not.Changes: New in Zulip 8.0 (feature level 231).
Previously, this value was never updated via events.
- push_notifications_enabled_end_timestamp:integer | nullIf the server expects the realm's push notifications access to end at a
definite time in the future, the time at which this is expected to happen.
Mobile clients should use this field to display warnings to users when the
indicated timestamp is near.Changes: New in Zulip 8.0 (feature level 231).
- rendered_description:stringNote: Only present if the changed property wasdescription.The organization description rendered as HTML, intended to
be used when displaying the organization description in a UI.One should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax
work correctly. And any client-side security logic for
user-generated message content should be applied when displaying
this HTML as though it were the body of a Zulip message.Changes: New in Zulip 12.0 (feature level 464). Previously
in feature levels 462-463, anupdateevent had been sent
when updating the realm'sdescription.
- require_e2ee_push_notifications:booleanWhether this realm is configured to disallow sending mobile
push notifications with message content through the legacy
mobile push notifications APIs. The new API uses end-to-end
encryption to protect message content and metadata from
being accessible to the push bouncer service, APNs, and
FCM. Clients that support the new E2EE API will use it
automatically regardless of this setting.Iftrue, mobile push notifications sent to clients that
lack support for E2EE push notifications will always have
"New message" as their content. Note that these legacy
mobile notifications will still contain metadata, which may
include the message's ID, the sender's name, email address,
and avatar.In a future release, once the official mobile apps have
implemented fully validated their E2EE protocol support,
this setting will become strict, and disable the legacy
protocol entirely.Changes: New in Zulip 11.0 (feature level 409). Previously,
this behavior was available only via thePUSH_NOTIFICATION_REDACT_CONTENTglobal server setting.
- require_unique_names:booleanIndicates whether the organization is configured to require users to have
unique full names. If true, the server will reject attempts to create a
new user, or change the name of an existing user, where doing so would
lead to two users whose names are identical modulo case and unicode
normalization.Changes: New in Zulip 9.0 (feature level 246). Previously, the Zulip
server could not be configured to enforce unique names.
- send_channel_events_messages:booleanIndicates whether channel event messages are sent in this organization.Changes: New in Zulip 12.0 (feature level 434). Previously,
channel events were sent unconditionally.
- send_welcome_emails:booleanWhether or not this organization is configured to send the standard Zulipwelcome emailsto new users joining the organization.
- signup_announcements_stream_id:integerThe ID of the channel to which automated messages announcing
thatnew users have joined the organizationare sent.Will be-1if such automated messages are disabled.Since these automated messages are sent by the server, this field is
primarily relevant to clients containing UI for changing it.Changes: In Zulip 9.0 (feature level 241), renamedsignup_notifications_stream_idtosignup_announcements_stream_id.
- upload_quota_mib:integer | nullThe new upload quota for the Zulip organization.Ifnull, there is no limit.Changes: New in Zulip 10.0 (feature level 306). Previously,
this was present changed via anupload_quotafield inextra_dataproperty
ofrealm/updateevent format forplan_typeevents.
- video_chat_provider:integerThe configuredvideo call providerfor the
organization.0 = None1 = Jitsi Meet3 = Zoom (User OAuth integration)4 = BigBlueButton5 = Zoom (Server to Server OAuth integration)6 = Constructor Groups7 = Nextcloud TalkNote that only one of theZoom integrationscan
be configured on a Zulip server.Changes: In Zulip 12.0 (feature level 465), added the
Constructor Groups option.In Zulip 12.0 (feature level 460), added the
Constructor Groups option.In Zulip 10.0 (feature level 353), added the Zoom Server
to Server OAuth option.In Zulip 3.0 (feature level 1), added the None option
to disable video call UI.
- waiting_period_threshold:integerMembers whose accounts have been created at least this many days ago
will be treated asfull membersfor the purpose of settings that restrict access to new members.
- want_advertise_in_communities_directory:booleanWhether the organization has given permission to be advertised in the
Zulipcommunities directory.Changes: New in Zulip 6.0 (feature level 129).
- welcome_message_custom_text:stringThis organization's configured custom message for Welcome Bot
to send to new user accounts, in Zulip Markdown format.Maximum length is 8000 Unicode code points.Changes: New in Zulip 11.0 (feature level 416).
- workplace_users_group:integer | objectAgroup-setting valuedefining the set of
users who will be considered as workplace users for billing.Changes: New in Zulip 12.0 (feature level 477).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- zulip_update_announcements_stream_id:integerThe ID of the channel to which automated messages announcing
new features or other end-user updates about the Zulip software are sent.Will be-1if such automated messages are disabled.Since these automated messages are sent by the server, this field is
primarily relevant to clients containing UI for changing it.Changes: New in Zulip 9.0 (feature level 242).

```
PATCH /messages/{message_id}
```

```
GET /server_settings
```
- Dictionary describing the properties of an authentication method for the
    organization - its enabled status and availability for use by the
    organization.enabled:booleanBoolean describing whether the authentication method (i.e. its key)
is enabled in this organization.available:booleanBoolean describing whether the authentication method is available for use.
If false, the organization is not eligible to enable the authentication
method.unavailable_reason:stringReason why the authentication method is unavailable. This field is optional
and is only present when 'available' is false.
- enabled:booleanBoolean describing whether the authentication method (i.e. its key)
is enabled in this organization.
- available:booleanBoolean describing whether the authentication method is available for use.
If false, the organization is not eligible to enable the authentication
method.
- unavailable_reason:stringReason why the authentication method is unavailable. This field is optional
and is only present when 'available' is false.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- 1 = All members can create and edit user groups
- 2 = Only organization administrators can create and edit
  user groups
- 3 = Onlyfull memberscan create and
  edit user groups.
- 4 = Only organization administrators and moderators can
  create and edit user groups.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- "G" = Hosted by Gravatar
- "J" = Generated using Jdenticon

```
POST /register
```
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- "G" means generated by Gravatar (the default).
- "U" means uploaded by an organization administrator.
- 100: 100% height (the default).
- 150: 150% height.
- 200: 200% height.
- "D" means the logo is the default Zulip logo.
- "U" means uploaded by an organization administrator.
- "allow_empty_topic": Channel messages can be sent to the empty topic.
- "disable_empty_topic": Channel messages cannot be sent to the empty topic.

```
PATCH /messages/{message_id}
```
- "all" = All edit history is visible.
- "moves" = Only moves are visible.
- "none" = No edit history is visible.

```
PATCH /messages/{message_id}
```

```
PATCH /messages/{message_id}
```
- "D" means the logo is the default Zulip logo.
- "U" means uploaded by an organization administrator.
- 0 = Unspecified
- 10 = Business
- 20 = Open-source project
- 30 = Education (non-profit)
- 35 = Education (for-profit)
- 40 = Research
- 50 = Event or conference
- 60 = Non-profit (registered)
- 70 = Government
- 80 = Political group
- 90 = Community
- 100 = Personal
- 1000 = Other
- 1 = Self-hosted organization (SELF_HOSTED)
- 2 = Zulip Cloud free plan (LIMITED)
- 3 = Zulip Cloud Standard plan (STANDARD)
- 4 = Zulip Cloud Standard plan, sponsored for free (STANDARD_FREE)
- 0 = None
- 1 = Jitsi Meet
- 3 = Zoom (User OAuth integration)
- 4 = BigBlueButton
- 5 = Zoom (Server to Server OAuth integration)
- 6 = Constructor Groups
- 7 = Nextcloud Talk
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
Example

```
{"data":{"message_content_edit_limit_seconds":600},"id":0,"op":"update_dict","property":"default","type":"realm"}
```

```
{"data":{"message_content_edit_limit_seconds":600},"id":0,"op":"update_dict","property":"default","type":"realm"}
```

### realm_user_settings_defaultsop: update
Event sent to all users in a Zulip organization when thedefault settings for new usersof the organization (realm) have changed.
SeePATCH /realm/user_settings_defaultsfor details on possible properties.
Changes: New in Zulip 5.0 (feature level 95).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- property:stringThe name of the property that was changed.
- value:boolean | integer | stringThe new value of the property.
Example

```
{"id":0,"op":"update","property":"left_side_userlist","type":"realm_user_settings_defaults","value":false}
```

```
{"id":0,"op":"update","property":"left_side_userlist","type":"realm_user_settings_defaults","value":false}
```

### draftsop: add
Event containing details of newly created drafts.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- drafts:(object)[]An array containing objects for the newly created drafts.id:integerThe unique ID of the draft. It will only used whenever the drafts are
fetched. This field should not be specified when the draft is being
created or edited.type:stringThe type of the draft. Either unaddressed (empty string),"stream",
or"private"(for one-on-one and group direct messages).to:(integer)[]An array of the tentative target audience IDs. For channel
messages, this should contain exactly 1 ID, the ID of the
target channel. For direct messages, this should be an array
of target user IDs. For unaddressed drafts, this is ignored,
and clients should send an empty array.topic:stringFor channel message drafts, the tentative topic name. For direct
or unaddressed messages, this will be ignored and should ideally
be the empty string. Should not contain null bytes.content:stringThe body of the draft. Should not contain null bytes.timestamp:integerA Unix timestamp (seconds only) representing when the draft was
last edited. When creating a draft, this key need not be present
and it will be filled in automatically by the server.
- id:integerThe unique ID of the draft. It will only used whenever the drafts are
fetched. This field should not be specified when the draft is being
created or edited.
- type:stringThe type of the draft. Either unaddressed (empty string),"stream",
or"private"(for one-on-one and group direct messages).
- to:(integer)[]An array of the tentative target audience IDs. For channel
messages, this should contain exactly 1 ID, the ID of the
target channel. For direct messages, this should be an array
of target user IDs. For unaddressed drafts, this is ignored,
and clients should send an empty array.
- topic:stringFor channel message drafts, the tentative topic name. For direct
or unaddressed messages, this will be ignored and should ideally
be the empty string. Should not contain null bytes.
- content:stringThe body of the draft. Should not contain null bytes.
- timestamp:integerA Unix timestamp (seconds only) representing when the draft was
last edited. When creating a draft, this key need not be present
and it will be filled in automatically by the server.
Example

```
{"drafts":[{"content":"Hello there!","id":17,"timestamp":15954790200,"to":[6],"topic":"","type":"private"}],"op":"add","type":"drafts"}
```

```
{"drafts":[{"content":"Hello there!","id":17,"timestamp":15954790200,"to":[6],"topic":"","type":"private"}],"op":"add","type":"drafts"}
```

### draftsop: update
Event containing details for an edited draft.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- draft:objectA dictionary for representing a message draft.id:integerThe unique ID of the draft. It will only used whenever the drafts are
fetched. This field should not be specified when the draft is being
created or edited.type:stringThe type of the draft. Either unaddressed (empty string),"stream",
or"private"(for one-on-one and group direct messages).to:(integer)[]An array of the tentative target audience IDs. For channel
messages, this should contain exactly 1 ID, the ID of the
target channel. For direct messages, this should be an array
of target user IDs. For unaddressed drafts, this is ignored,
and clients should send an empty array.topic:stringFor channel message drafts, the tentative topic name. For direct
or unaddressed messages, this will be ignored and should ideally
be the empty string. Should not contain null bytes.content:stringThe body of the draft. Should not contain null bytes.timestamp:integerA Unix timestamp (seconds only) representing when the draft was
last edited. When creating a draft, this key need not be present
and it will be filled in automatically by the server.
- id:integerThe unique ID of the draft. It will only used whenever the drafts are
fetched. This field should not be specified when the draft is being
created or edited.
- type:stringThe type of the draft. Either unaddressed (empty string),"stream",
or"private"(for one-on-one and group direct messages).
- to:(integer)[]An array of the tentative target audience IDs. For channel
messages, this should contain exactly 1 ID, the ID of the
target channel. For direct messages, this should be an array
of target user IDs. For unaddressed drafts, this is ignored,
and clients should send an empty array.
- topic:stringFor channel message drafts, the tentative topic name. For direct
or unaddressed messages, this will be ignored and should ideally
be the empty string. Should not contain null bytes.
- content:stringThe body of the draft. Should not contain null bytes.
- timestamp:integerA Unix timestamp (seconds only) representing when the draft was
last edited. When creating a draft, this key need not be present
and it will be filled in automatically by the server.
Example

```
{"draft":{"content":"Hello everyone!","id":17,"timestamp":15954790200,"to":[6,7,8,9,10],"topic":"","type":"private"},"op":"update","type":"drafts"}
```

```
{"draft":{"content":"Hello everyone!","id":17,"timestamp":15954790200,"to":[6,7,8,9,10],"topic":"","type":"private"},"op":"update","type":"drafts"}
```

### draftsop: remove
Event containing the ID of a deleted draft.
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- draft_id:integerThe ID of the draft that was just deleted.
Example

```
{"draft_id":17,"op":"remove","type":"drafts"}
```

```
{"draft_id":17,"op":"remove","type":"drafts"}
```

### navigation_viewop: add
Event containing details of a newly configured navigation view.
Changes: New in Zulip 11.0 (feature level 390).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- navigation_view:objectRepresents a user's personal configuration for a specific
navigation view (displayed most visibly at the top of the web
application's left sidebar).Navigation views can be either an override to the default
behavior of a built-in view, or a custom view.Changes: New in Zulip 11.0 (feature level 390).fragment:stringA unique identifier for the view, used to determine navigation
behavior when clicked.Clients should use this value to navigate to the corresponding URL hash.is_pinned:booleanDetermines whether the view appears directly in the sidebar or
is hidden in the "More Views" menu.true- Pinned and visible in the sidebar.false- Hidden and accessible via the "More Views" menu.name:string | nullThe user-facing name for custom navigation views. Omit this
field for built-in views.
- fragment:stringA unique identifier for the view, used to determine navigation
behavior when clicked.Clients should use this value to navigate to the corresponding URL hash.
- is_pinned:booleanDetermines whether the view appears directly in the sidebar or
is hidden in the "More Views" menu.true- Pinned and visible in the sidebar.false- Hidden and accessible via the "More Views" menu.
- name:string | nullThe user-facing name for custom navigation views. Omit this
field for built-in views.
- true- Pinned and visible in the sidebar.
- false- Hidden and accessible via the "More Views" menu.
Example

```
{"navigation_view":{"fragment":"narrow/is/alerted","is_pinned":true,"name":"Alert Words"},"op":"add","type":"navigation_view"}
```

```
{"navigation_view":{"fragment":"narrow/is/alerted","is_pinned":true,"name":"Alert Words"},"op":"add","type":"navigation_view"}
```

### navigation_viewop: update
Event containing details of an update to an existing navigation view.
Changes: New in Zulip 11.0 (feature level 390).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- fragment:stringThe unique URL hash of the navigation view being updated.
- data:objectA dictionary containing the updated properties of the navigation view.name:string | nullThe user-facing name for custom navigation views. Omit this field for built-in views.is_pinned:boolean | nullDetermines whether the view is pinned (true) or hidden in the menu (false).
- name:string | nullThe user-facing name for custom navigation views. Omit this field for built-in views.
- is_pinned:boolean | nullDetermines whether the view is pinned (true) or hidden in the menu (false).
Example

```
{"data":{"is_pinned":false},"fragment":"narrow/is/alerted","op":"update","type":"navigation_view"}
```

```
{"data":{"is_pinned":false},"fragment":"narrow/is/alerted","op":"update","type":"navigation_view"}
```

### navigation_viewop: remove
Event containing the fragment of a deleted navigation view.
Changes: New in Zulip 11.0 (feature level 390).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- fragment:stringThe unique URL hash of the navigation view that was just deleted.
Example

```
{"fragment":"narrow/is/mentioned","op":"remove","type":"navigation_view"}
```

```
{"fragment":"narrow/is/mentioned","op":"remove","type":"navigation_view"}
```

### saved_snippetsop: add
Event containing details of a newly created saved snippet.
Changes: New in Zulip 10.0 (feature level 297).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- saved_snippet:objectObject containing the details of the saved snippet.id:integerThe unique ID of the saved snippet.title:stringThe title of the saved snippet.content:stringThe content of the saved snippet inZulip-flavored Markdownformat.Clients should insert this content into a message when using
a saved snippet.date_created:integerThe UNIX timestamp for when the saved snippet was created, in
UTC seconds.
- id:integerThe unique ID of the saved snippet.
- title:stringThe title of the saved snippet.
- content:stringThe content of the saved snippet inZulip-flavored Markdownformat.Clients should insert this content into a message when using
a saved snippet.
- date_created:integerThe UNIX timestamp for when the saved snippet was created, in
UTC seconds.
Example

```
{"op":"add","saved_snippet":{"content":"Welcome to the organization.","date_created":1681662420,"id":1,"title":"Example"},"type":"saved_snippets"}
```

```
{"op":"add","saved_snippet":{"content":"Welcome to the organization.","date_created":1681662420,"id":1,"title":"Example"},"type":"saved_snippets"}
```

### saved_snippetsop: update
Event containing details of the edited saved snippet.
Clients should update the existing saved snippet with the
ID provided in thesaved_snippetobject.
Changes: New in Zulip 10.0 (feature level 368).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- saved_snippet:objectObject containing the details of the saved snippet.id:integerThe unique ID of the saved snippet.title:stringThe title of the saved snippet.content:stringThe content of the saved snippet inZulip-flavored Markdownformat.Clients should insert this content into a message when using
a saved snippet.date_created:integerThe UNIX timestamp for when the saved snippet was created, in
UTC seconds.
- id:integerThe unique ID of the saved snippet.
- title:stringThe title of the saved snippet.
- content:stringThe content of the saved snippet inZulip-flavored Markdownformat.Clients should insert this content into a message when using
a saved snippet.
- date_created:integerThe UNIX timestamp for when the saved snippet was created, in
UTC seconds.
Example

```
{"op":"update","saved_snippet":{"content":"Welcome to the organization.","date_created":1681662420,"id":1,"title":"Example"},"type":"saved_snippets"}
```

```
{"op":"update","saved_snippet":{"content":"Welcome to the organization.","date_created":1681662420,"id":1,"title":"Example"},"type":"saved_snippets"}
```

### saved_snippetsop: remove
Event containing the ID of a deleted saved snippet.
Changes: New in Zulip 10.0 (feature level 297).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- saved_snippet_id:integerThe ID of the saved snippet that was just deleted.Changes: New in Zulip 10.0 (feature level 297).
Example

```
{"op":"remove","saved_snippet_id":17,"type":"saved_snippets"}
```

```
{"op":"remove","saved_snippet_id":17,"type":"saved_snippets"}
```

### remindersop: add
Event sent to a user's clients when a reminder is scheduled.
Changes: New in Zulip 11.0 (feature level 399).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- reminders:(object)[]An array of objects containing details of the newly created
reminders.reminder_id:integerThe unique ID of the reminder, which can be used to
delete the reminder.This is different from the unique ID that the message would have
after being sent.type:stringThe type of the reminder. Always set to"private".to:(integer)[]Contains the ID of the user who scheduled the reminder,
and to which the reminder will be sent.content:stringThe content/body of the reminder, inZulip-flavored Markdownformat.SeeMarkdown message formattingfor details on Zulip's HTML format.rendered_content:stringThe content/body of the reminder rendered in HTML.scheduled_delivery_timestamp:integerThe UNIX timestamp for when the message will be sent
by the server, in UTC seconds.failed:booleanWhether the server has tried to send the reminder
and it failed to successfully send.Clients that support unscheduling reminders
should display scheduled messages with"failed": truewith an
indicator that the server failed to send the message at the
scheduled time, so that the user is aware of the failure and can
get the content of the scheduled message.reminder_target_message_id:integerThe ID of the message that the reminder is created for.
- reminder_id:integerThe unique ID of the reminder, which can be used to
delete the reminder.This is different from the unique ID that the message would have
after being sent.
- type:stringThe type of the reminder. Always set to"private".
- to:(integer)[]Contains the ID of the user who scheduled the reminder,
and to which the reminder will be sent.
- content:stringThe content/body of the reminder, inZulip-flavored Markdownformat.SeeMarkdown message formattingfor details on Zulip's HTML format.
- rendered_content:stringThe content/body of the reminder rendered in HTML.
- scheduled_delivery_timestamp:integerThe UNIX timestamp for when the message will be sent
by the server, in UTC seconds.
- failed:booleanWhether the server has tried to send the reminder
and it failed to successfully send.Clients that support unscheduling reminders
should display scheduled messages with"failed": truewith an
indicator that the server failed to send the message at the
scheduled time, so that the user is aware of the failure and can
get the content of the scheduled message.
- reminder_target_message_id:integerThe ID of the message that the reminder is created for.
Example

```
{"op":"add","reminders":[{"content":"Hello there!","failed":false,"reminder_id":17,"reminder_target_message_id":42,"rendered_content":"<p>Hello there!</p>","scheduled_delivery_timestamp":1681662420,"to":[6],"type":"private"}],"type":"reminders"}
```

```
{"op":"add","reminders":[{"content":"Hello there!","failed":false,"reminder_id":17,"reminder_target_message_id":42,"rendered_content":"<p>Hello there!</p>","scheduled_delivery_timestamp":1681662420,"to":[6],"type":"private"}],"type":"reminders"}
```

### remindersop: remove
Event sent to a user's clients when a reminder
is deleted.
Changes: New in Zulip 11.0 (feature level 399).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- reminder_id:integerThe ID of the reminder that was deleted.
Example

```
{"op":"remove","reminder_id":17,"type":"reminders"}
```

```
{"op":"remove","reminder_id":17,"type":"reminders"}
```

### scheduled_messagesop: add
Event sent to a user's clients when scheduled messages
are created.
Changes: New in Zulip 7.0 (feature level 179).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- scheduled_messages:(object)[]An array of objects containing details of the newly created
scheduled messages.scheduled_message_id:integerThe unique ID of the scheduled message, which can be used to
modify or delete the scheduled message.This is different from the unique ID that the message will have
after it is sent.type:stringThe type of the scheduled message. Either"stream"or"private".to:integer | (integer)[]The scheduled message's tentative target audience.For channel messages, it will be the unique ID of the target
channel. For direct messages, it will be an array with the
target users' IDs.topic:stringOnly present iftypeis"stream".The topic for the channel message.content:stringThe content/body of the scheduled message, inZulip-flavored Markdownformat.SeeMarkdown message formattingfor details on Zulip's HTML format.rendered_content:stringThe content/body of the scheduled message rendered in HTML.scheduled_delivery_timestamp:integerThe UNIX timestamp for when the message will be sent
by the server, in UTC seconds.failed:booleanWhether the server has tried to send the scheduled message
and it failed to successfully send.Clients that support unscheduling and editing scheduled messages
should display scheduled messages with"failed": truewith an
indicator that the server failed to send the message at the
scheduled time, so that the user is aware of the failure and can
get the content of the scheduled message.Changes: New in Zulip 7.0 (feature level 181).
- scheduled_message_id:integerThe unique ID of the scheduled message, which can be used to
modify or delete the scheduled message.This is different from the unique ID that the message will have
after it is sent.
- type:stringThe type of the scheduled message. Either"stream"or"private".
- to:integer | (integer)[]The scheduled message's tentative target audience.For channel messages, it will be the unique ID of the target
channel. For direct messages, it will be an array with the
target users' IDs.
- topic:stringOnly present iftypeis"stream".The topic for the channel message.
- content:stringThe content/body of the scheduled message, inZulip-flavored Markdownformat.SeeMarkdown message formattingfor details on Zulip's HTML format.
- rendered_content:stringThe content/body of the scheduled message rendered in HTML.
- scheduled_delivery_timestamp:integerThe UNIX timestamp for when the message will be sent
by the server, in UTC seconds.
- failed:booleanWhether the server has tried to send the scheduled message
and it failed to successfully send.Clients that support unscheduling and editing scheduled messages
should display scheduled messages with"failed": truewith an
indicator that the server failed to send the message at the
scheduled time, so that the user is aware of the failure and can
get the content of the scheduled message.Changes: New in Zulip 7.0 (feature level 181).
Example

```
{"op":"add","scheduled_messages":[{"content":"Hello there!","failed":false,"rendered_content":"<p>Hello there!</p>","scheduled_delivery_timestamp":1681662420,"scheduled_message_id":17,"to":[6],"type":"private"}],"type":"scheduled_messages"}
```

```
{"op":"add","scheduled_messages":[{"content":"Hello there!","failed":false,"rendered_content":"<p>Hello there!</p>","scheduled_delivery_timestamp":1681662420,"scheduled_message_id":17,"to":[6],"type":"private"}],"type":"scheduled_messages"}
```

### scheduled_messagesop: update
Event sent to a user's clients when a scheduled message
is edited.
Changes: New in Zulip 7.0 (feature level 179).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- scheduled_message:objectObject containing details of the scheduled message.scheduled_message_id:integerThe unique ID of the scheduled message, which can be used to
modify or delete the scheduled message.This is different from the unique ID that the message will have
after it is sent.type:stringThe type of the scheduled message. Either"stream"or"private".to:integer | (integer)[]The scheduled message's tentative target audience.For channel messages, it will be the unique ID of the target
channel. For direct messages, it will be an array with the
target users' IDs.topic:stringOnly present iftypeis"stream".The topic for the channel message.content:stringThe content/body of the scheduled message, inZulip-flavored Markdownformat.SeeMarkdown message formattingfor details on Zulip's HTML format.rendered_content:stringThe content/body of the scheduled message rendered in HTML.scheduled_delivery_timestamp:integerThe UNIX timestamp for when the message will be sent
by the server, in UTC seconds.failed:booleanWhether the server has tried to send the scheduled message
and it failed to successfully send.Clients that support unscheduling and editing scheduled messages
should display scheduled messages with"failed": truewith an
indicator that the server failed to send the message at the
scheduled time, so that the user is aware of the failure and can
get the content of the scheduled message.Changes: New in Zulip 7.0 (feature level 181).
- scheduled_message_id:integerThe unique ID of the scheduled message, which can be used to
modify or delete the scheduled message.This is different from the unique ID that the message will have
after it is sent.
- type:stringThe type of the scheduled message. Either"stream"or"private".
- to:integer | (integer)[]The scheduled message's tentative target audience.For channel messages, it will be the unique ID of the target
channel. For direct messages, it will be an array with the
target users' IDs.
- topic:stringOnly present iftypeis"stream".The topic for the channel message.
- content:stringThe content/body of the scheduled message, inZulip-flavored Markdownformat.SeeMarkdown message formattingfor details on Zulip's HTML format.
- rendered_content:stringThe content/body of the scheduled message rendered in HTML.
- scheduled_delivery_timestamp:integerThe UNIX timestamp for when the message will be sent
by the server, in UTC seconds.
- failed:booleanWhether the server has tried to send the scheduled message
and it failed to successfully send.Clients that support unscheduling and editing scheduled messages
should display scheduled messages with"failed": truewith an
indicator that the server failed to send the message at the
scheduled time, so that the user is aware of the failure and can
get the content of the scheduled message.Changes: New in Zulip 7.0 (feature level 181).
Example

```
{"op":"update","scheduled_message":{"content":"Hello there!","failed":false,"rendered_content":"<p>Hello there!</p>","scheduled_delivery_timestamp":1681662420,"scheduled_message_id":17,"to":[6],"type":"private"},"type":"scheduled_messages"}
```

```
{"op":"update","scheduled_message":{"content":"Hello there!","failed":false,"rendered_content":"<p>Hello there!</p>","scheduled_delivery_timestamp":1681662420,"scheduled_message_id":17,"to":[6],"type":"private"},"type":"scheduled_messages"}
```

### scheduled_messagesop: remove
Event sent to a user's clients when a scheduled message
is deleted.
Changes: New in Zulip 7.0 (feature level 179).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- scheduled_message_id:integerThe ID of the scheduled message that was deleted.
Example

```
{"op":"remove","scheduled_message_id":17,"type":"scheduled_messages"}
```

```
{"op":"remove","scheduled_message_id":17,"type":"scheduled_messages"}
```

### channel_folderop: add
Event sent to users in an organization when a channel folder is created.
Changes: New in Zulip 11.0 (feature level 389).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- channel_folder:objectObject containing the channel folder's attributes.id:integerThe unique ID of the channel folder.name:stringThe name of the channel folder.order:integerThis value determines in which order the channel folder should be
displayed in the UI. The value is 0 indexed, and a channel folder with
a lower value should be displayed before channel folders with higher
values.Changes: New in Zulip 11.0 (feature level 414).date_created:integer | nullThe UNIX timestamp for when the channel folder was created,
in UTC seconds.creator_id:integer | nullThe ID of the user who created the channel folder.description:stringThe description of the channel folder. Can be an empty string.SeeMarkdown message formattingfor details
on Zulip's HTML format.rendered_description:stringThe description of the channel folder rendered as HTML, intended to be
used for UI that displays the channel folder description.Clients should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax work
correctly. And any client-side security logic for user-generated
message content should be applied when displaying this HTML as though
it were the body of a Zulip message.is_archived:booleanWhether the channel folder is archived or not.
- id:integerThe unique ID of the channel folder.
- name:stringThe name of the channel folder.
- order:integerThis value determines in which order the channel folder should be
displayed in the UI. The value is 0 indexed, and a channel folder with
a lower value should be displayed before channel folders with higher
values.Changes: New in Zulip 11.0 (feature level 414).
- date_created:integer | nullThe UNIX timestamp for when the channel folder was created,
in UTC seconds.
- creator_id:integer | nullThe ID of the user who created the channel folder.
- description:stringThe description of the channel folder. Can be an empty string.SeeMarkdown message formattingfor details
on Zulip's HTML format.
- rendered_description:stringThe description of the channel folder rendered as HTML, intended to be
used for UI that displays the channel folder description.Clients should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax work
correctly. And any client-side security logic for user-generated
message content should be applied when displaying this HTML as though
it were the body of a Zulip message.
- is_archived:booleanWhether the channel folder is archived or not.
Example

```
{"channel_folder":{"creator_id":9,"date_created":1717484476,"description":"Channels for frontend discussions","id":2,"is_archived":false,"name":"fronted","order":1,"rendered_description":"<p>Channels for frontend discussions</p>"},"id":0,"op":"add","type":"channel_folder"}
```

```
{"channel_folder":{"creator_id":9,"date_created":1717484476,"description":"Channels for frontend discussions","id":2,"is_archived":false,"name":"fronted","order":1,"rendered_description":"<p>Channels for frontend discussions</p>"},"id":0,"op":"add","type":"channel_folder"}
```

### channel_folderop: update
Event sent to users in an organization when a channel folder is updated.
Changes: New in Zulip 11.0 (feature level 389).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- channel_folder_id:numberID of the updated channel folder.
- data:objectDictionary containing the changed details of the channel folder.name:stringThe new name of the channel folder. Only present if the channel
folder's name changed.description:stringThe new description of the channel folder. Only present if the
description changed.SeeMarkdown message formattingfor details on Zulip's HTML format.rendered_description:stringThe new rendered description of the channel folder. Only present
if the description changed.is_archived:booleanWhether the channel folder is archived or not. Only present if
the channel folder is archived or unarchived.
- name:stringThe new name of the channel folder. Only present if the channel
folder's name changed.
- description:stringThe new description of the channel folder. Only present if the
description changed.SeeMarkdown message formattingfor details on Zulip's HTML format.
- rendered_description:stringThe new rendered description of the channel folder. Only present
if the description changed.
- is_archived:booleanWhether the channel folder is archived or not. Only present if
the channel folder is archived or unarchived.
Example

```
{"data":{"name":"New frontend"},"id":0,"op":"update","type":"channel_folder"}
```

```
{"data":{"name":"New frontend"},"id":0,"op":"update","type":"channel_folder"}
```

### channel_folderop: reorder
Event sent to users in an organization when channel folders are reordered.
Changes: New in Zulip 11.0 (feature level 418).
- id:integerThe ID of the event. Events appear in increasing order but may not be consecutive.
- type:stringThe event's type, relevant both for client-side dispatch and server-side
filtering by event type inPOST /register.
- order:(integer)[]A list of channel folder IDs representing the new order.
Example

```
{"id":0,"op":"reorder","order":[3,1,2],"type":"channel_folder"}
```

```
{"id":0,"op":"reorder","order":[3,1,2],"type":"channel_folder"}
```

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"events":[{"id":0,"message":{"avatar_url":"https://url/for/othello-bots/avatar","client":"website","content":"I come not, friends, to steal away your hearts.","content_type":"text/x-markdown","display_recipient":"Denmark","id":12345678,"recipient_id":12314,"sender_email":"othello-bot@example.com","sender_full_name":"Othello Bot","sender_id":13215,"sender_realm_str":"example","timestamp":1375978403,"topic_links":[],"type":"stream"},"type":"message"},{"id":1,"message":{"avatar_url":"https://url/for/othello-bots/avatar","client":"website","content":"With mirth and laughter let old wrinkles come.","content_type":"text/x-markdown","display_recipient":[{"email":"hamlet@example.com","full_name":"Hamlet of Denmark","id":31572}],"id":12345679,"recipient_id":18391,"sender_email":"othello-bot@example.com","sender_full_name":"Othello Bot","sender_id":13215,"sender_realm_str":"example","subject":"","timestamp":1375978404,"topic_links":[],"type":"private"},"type":"message"}],"msg":"","queue_id":"fb67bf8a-c031-47cc-84cf-ed80accacda8","result":"success"}
```

```
{"events":[{"id":0,"message":{"avatar_url":"https://url/for/othello-bots/avatar","client":"website","content":"I come not, friends, to steal away your hearts.","content_type":"text/x-markdown","display_recipient":"Denmark","id":12345678,"recipient_id":12314,"sender_email":"othello-bot@example.com","sender_full_name":"Othello Bot","sender_id":13215,"sender_realm_str":"example","timestamp":1375978403,"topic_links":[],"type":"stream"},"type":"message"},{"id":1,"message":{"avatar_url":"https://url/for/othello-bots/avatar","client":"website","content":"With mirth and laughter let old wrinkles come.","content_type":"text/x-markdown","display_recipient":[{"email":"hamlet@example.com","full_name":"Hamlet of Denmark","id":31572}],"id":12345679,"recipient_id":18391,"sender_email":"othello-bot@example.com","sender_full_name":"Othello Bot","sender_id":13215,"sender_realm_str":"example","subject":"","timestamp":1375978404,"topic_links":[],"type":"private"},"type":"message"}],"msg":"","queue_id":"fb67bf8a-c031-47cc-84cf-ed80accacda8","result":"success"}
```

#### BAD_EVENT_QUEUE_ID errors
This error occurs if the target event queue has been garbage collected.
A compliant client will handle this error by re-initializing itself
(e.g. a Zulip web app browser window will reload in this case).
Seethe /register endpoint docsfor details on how to
handle these correctly.
The following is the error response in such case:

```
{"code":"BAD_EVENT_QUEUE_ID","msg":"Bad event queue ID: fb67bf8a-c031-47cc-84cf-ed80accacda8","queue_id":"fb67bf8a-c031-47cc-84cf-ed80accacda8","result":"error"}
```

```
{"code":"BAD_EVENT_QUEUE_ID","msg":"Bad event queue ID: fb67bf8a-c031-47cc-84cf-ed80accacda8","queue_id":"fb67bf8a-c031-47cc-84cf-ed80accacda8","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.