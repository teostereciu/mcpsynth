# Get subscribed channels | Zulip API documentation

*Source: https://zulip.com/api/get-subscriptions*

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

# Get subscribed channels
GET https://your-org.zulipchat.com/api/v1/users/me/subscriptions
Get all channels that the user is subscribed to.

## Usage examples
PythonJavaScriptcurl
- Python
- JavaScript
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Get all channels that the user is subscribed to.result=client.get_subscriptions()print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Get all channels that the user is subscribed to.result=client.get_subscriptions()print(result)
```
More examples and documentation can be foundhere.

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Get all channels that the user is subscribed toconsole.log(awaitclient.streams.subscriptions.retrieve());})();
```

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Get all channels that the user is subscribed toconsole.log(awaitclient.streams.subscriptions.retrieve());})();
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/users/me/subscriptions \
    -u EMAIL_ADDRESS:API_KEY
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/users/me/subscriptions \
    -u EMAIL_ADDRESS:API_KEY
```
You may pass theinclude_subscribersquery parameter as follows:
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/users/me/subscriptions \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode include_subscribers=true
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/users/me/subscriptions \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode include_subscribers=true
```

## Parameters
include_subscribersstringoptional
Whether each returned channel object should include asubscribersfield containing a list of the user IDs of its subscribers.
Client apps supporting organizations with many thousands of users
should not passtrue, because the full subscriber matrix may be
several megabytes of data. Thepartialvalue, combined with thesubscriber_countand fetching subscribers for individual channels as
needed, is recommended to support client app features where
channel subscriber data is useful.
If a client passespartialfor this parameter, the server may,
for some channels, return a subset of the channel's subscribers
in thepartial_subscribersfield instead of thesubscribersfield,
which always contains the complete set of subscribers.
The server guarantees that it will always return asubscribersfield for channels with fewer than 250 total subscribers. When
returning apartial_subscribersfield, the server guarantees
that all bot users and users active within the last 14 days will
be included. For other cases, the server may use its discretion
to determine which channels and users to include, balancing between
payload size and usefulness of the data provided to the client.
Changes: Thepartialvalue is new in Zulip 11.0 (feature level 412).
New in Zulip 2.1.0.
Must be one of:"true","false","partial". 
Defaults to"false".

## Response

#### Return values
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

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"msg":"","result":"success","subscriptions":[{"audible_notifications":true,"color":"#e79ab5","creator_id":null,"description":"A Scandinavian country","desktop_notifications":true,"invite_only":false,"is_archived":false,"is_muted":false,"name":"Denmark","pin_to_top":false,"push_notifications":false,"stream_id":1,"subscribers":[7,10,11,12,14]},{"audible_notifications":true,"color":"#e79ab5","creator_id":8,"description":"Located in the United Kingdom","desktop_notifications":true,"invite_only":false,"is_archived":false,"is_muted":false,"name":"Scotland","pin_to_top":false,"push_notifications":false,"stream_id":3,"subscribers":[7,11,12,14]}]}
```

```
{"msg":"","result":"success","subscriptions":[{"audible_notifications":true,"color":"#e79ab5","creator_id":null,"description":"A Scandinavian country","desktop_notifications":true,"invite_only":false,"is_archived":false,"is_muted":false,"name":"Denmark","pin_to_top":false,"push_notifications":false,"stream_id":1,"subscribers":[7,10,11,12,14]},{"audible_notifications":true,"color":"#e79ab5","creator_id":8,"description":"Located in the United Kingdom","desktop_notifications":true,"invite_only":false,"is_archived":false,"is_muted":false,"name":"Scotland","pin_to_top":false,"push_notifications":false,"stream_id":3,"subscribers":[7,11,12,14]}]}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.