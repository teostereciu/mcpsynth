# Create a channel | Zulip API documentation

*Source: https://zulip.com/api/create-channel*

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

# Create a channel
POST https://your-org.zulipchat.com/api/v1/channels/create
Create a newchannel, and optionally subscribe
users to the newly created channel.
The initialchannel settingswill be determined
by the optional parameters, likeinvite_only, detailed below.
Changes: New in Zulip 11.0 (feature level 417). Previously, this was
only possible via thePOST /api/subscribeendpoint,
which handles both channel subscription and creation.

```
POST /api/subscribe
```

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Create a new channel.request={"name":"music_group","description":"Channel for discussing and learning about music.","subscribers":[12],}result=client.call_endpoint(url="channels/create",method="POST",request=request,)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Create a new channel.request={"name":"music_group","description":"Channel for discussing and learning about music.","subscribers":[12],}result=client.call_endpoint(url="channels/create",method="POST",request=request,)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/channels/create \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode name=music \
    --data-urlencode 'subscribers=[17, 12]'
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/channels/create \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode name=music \
    --data-urlencode 'subscribers=[17, 12]'
```

## Parameters
namestringrequired
The name of the new channel.
Clients should use themax_stream_name_lengthreturned by thePOST /registerendpoint to determine
the maximum channel name length.

```
POST /register
```
descriptionstringoptional

```
"Channel for discussing all things music!"
```
Thedescriptionto use for the new channel being created, in text/markdown format.
Clients should use themax_stream_description_lengthreturned
by thePOST /registerendpoint to
determine the maximum channel description length.

```
POST /register
```
subscribers(integer)[]required
A list of user IDs of the users to be subscribed to the new channel.
announcebooleanoptional
This determines whethernotification botwill send an announcement about the new channel's creation.
Defaults tofalse.
invite_onlybooleanoptional
This parameter and the ones that follow are used to request an initial
configuration of the new channel.
This parameter determines whether the newly created channel will be
aprivate channel.
Defaults tofalse.
is_web_publicbooleanoptional
This parameter determines whether the newly created channel will be
a web-public channel.
Note that creating web-public channels requires theWEB_PUBLIC_STREAMS_ENABLEDserver settingto be enabled on the Zulip server in question, the organization
to have enabled theenable_spectator_accessrealm setting, and
the current user to have permission under the organization'scan_create_web_public_channel_grouprealm setting.
Defaults tofalse.
is_default_streambooleanoptional
This parameter determines whether the newly created channel will be
added as adefault channelfor new users joining
the organization.
Defaults tofalse.
folder_idintegeroptional
This parameter adds the newly created channel to the specifiedchannel folder.
Changes: New in Zulip 11.0 (feature level 389).
topics_policystringoptional
Whethernamed topicsand the empty
topic (i.e.,"general chat" topic)
are enabled in this channel.
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
The"empty_topic_only"policy can only be set if all existing messages
in the channel are already in the empty topic.
When creating a new channel, if thetopics_policyis not specified, the"inherit"option will be set.
Changes: In Zulip 11.0 (feature level 404), the"empty_topic_only"option was added.
New in Zulip 11.0 (feature level 392).
Must be one of:"inherit","allow_empty_topic","disable_empty_topic","empty_topic_only".
history_public_to_subscribersbooleanoptional
Whether the channel's message history should be available to
newly subscribed members, or users can only access messages
they actually received while subscribed to the channel.
Corresponds to the shared history option forprivate channels.
message_retention_daysstring | integeroptional
Number of days that messages sent to this channel will be stored
before being automatically deleted by themessage retention
policy. Two special string format
values are supported:
- "realm_default": Return to the organization-level setting.
- "unlimited": Retain messages forever.
Changes: Prior to Zulip 5.0 (feature level 91), retaining
messages forever was encoded using"forever"instead of"unlimited".
New in Zulip 3.0 (feature level 17).
can_add_subscribers_groupinteger | objectoptional
Agroup-setting valuedefining the set of users
who have permission to add subscribers to this channel.
Users who can administer the channel or have similar realm-level
permissions can add subscribers to a public channel regardless
of the value of this setting.
Users in this group need not be subscribed to a private channel to
add subscribers to it.
Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.
Changes: New in Zulip 10.0 (feature level 342). Previously, there was no
channel-level setting for this permission.
This parameter must be one of the following:
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_create_topic_groupinteger | objectoptional
Agroup-setting valuedefining the set of users
who have permission to create a new topic in this channel.
Note that using this permission requires also having permission to
send messages in the channel.
Note that this must be therole:everyonesystem groupforprivate channels with protected history.
Changes: New in Zulip 12.0 (feature level 441). Previously,
if you could send messages in a channel, you could create topics in
the channel.
This parameter must be one of the following:
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_delete_any_message_groupinteger | objectoptional
Agroup-setting valuedefining the set of users
who have permission to delete any message in the channel.
Note that a user musthave content accessto a
channel in order to delete any message in the channel.
Users present in the organization-levelcan_delete_any_message_groupsetting can always delete any message in the channel if theyhave content accessto that channel.
Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users incan_delete_any_message_groupwere able
delete any message in the organization.
This parameter must be one of the following:
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_delete_own_message_groupinteger | objectoptional
Agroup-setting valuedefining the set of users
who have permission to delete the messages that they have sent in the channel.
Note that a user musthave content accessto a
channel in order to delete their own message in the channel.
Users with permission to delete any message in the channel
and users present in the organization-levelcan_delete_own_message_groupsetting
can always delete their own messages in the channel if theyhave content accessto that channel.
Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users in the organization-levelcan_delete_any_message_groupandcan_delete_own_message_groupsettings were able delete their own messages in
the organization.
This parameter must be one of the following:
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_remove_subscribers_groupinteger | objectoptional
Agroup-setting valuedefining the set of users
who have permission to remove subscribers from this channel.
Organization administrators can unsubscribe others from a channel as though
they were in this group without being explicitly listed here.
Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.
Changes: Prior to Zulip 10.0 (feature level 349), channel administrators
could not unsubscribe other users if they were not an organization
administrator or part ofcan_remove_subscribers_group. Realm administrators
were not allowed to unsubscribe other users from a private channel if they
were not subscribed to that channel.
Prior to Zulip 10.0 (feature level 320), this value was always the integer
ID of a system group.
Before Zulip 8.0 (feature level 197), thecan_remove_subscribers_groupsetting was namedcan_remove_subscribers_group_id.
New in Zulip 6.0 (feature level 142).
This parameter must be one of the following:
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_administer_channel_groupinteger | objectoptional
Agroup-setting valuedefining the set of users
who have permission to administer this channel.
Organization administrators can administer every channel as though they were
in this group without being explicitly listed here.
Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.
Changes: Prior to Zulip 10.0 (feature level 349) a user needed tohave content accessto a channel in
order to modify it. The exception to this rule was that organization
administrators can edit channel names and descriptions without
having full access to the channel.
New in Zulip 10.0 (feature level 325). Prior to this
change, the permission to administer channels was limited to realm
administrators.
This parameter must be one of the following:
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_move_messages_out_of_channel_groupinteger | objectoptional
Agroup-setting valuedefining the set of users
who have permission to move messages out of this channel.
Note that a user musthave content accessto a
channel in order to move messages out of the channel.
Channel administrators and users present in the organization-levelcan_move_messages_between_channels_groupsetting can always move messages
out of the channel if theyhave content accessto
the channel.
Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_channels_groupwere able
move messages between channels.
This parameter must be one of the following:
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_move_messages_within_channel_groupinteger | objectoptional
Agroup-setting valuedefining the set of users
who have permission to move messages within this channel.
Note that a user musthave content accessto a
channel in order to move messages within the channel.
Channel administrators and users present in the organization-levelcan_move_messages_between_topics_groupsetting can always move messages
within the channel if theyhave content accessto
the channel.
Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_topics_groupwere able
move messages between topics of a channel.
This parameter must be one of the following:
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_send_message_groupinteger | objectoptional
Agroup-setting valuedefining the set of users
who have permission to post in this channel.
Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.
Note that using this permission to send a message to a new topic requires
also having permission to create new topics in the channel.
Changes: New in Zulip 10.0 (feature level 333). Previouslystream_post_policyfield used to control the permission to
post in the channel.
This parameter must be one of the following:
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_subscribe_groupinteger | objectoptional
Agroup-setting valuedefining the set of users
who have permission to subscribe themselves to this channel.
Everyone, excluding guests, can subscribe to any public channel
irrespective of this setting.
Users in this group can subscribe to a private channel as well.
Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.
Changes: New in Zulip 10.0 (feature level 357).
This parameter must be one of the following:
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_resolve_topics_groupinteger | objectoptional
Agroup-setting valuedefining the set of users
who have permission to resolve topics in the channel.
Users who have similar realm-level permissions can resolve topics
in a channel regardless of the value of this setting.
Changes: New in Zulip 11.0 (feature level 402).
This parameter must be one of the following:
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.

## Response

#### Return values
- id:integerThe ID of the newly created channel.

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"id":50,"msg":"","result":"success"}
```

```
{"id":50,"msg":"","result":"success"}
```
An example JSON error response for when a channel with the submitted
name already exists.

```
{"code":"CHANNEL_ALREADY_EXISTS","msg":"Channel 'discussions' already exists","result":"error"}
```

```
{"code":"CHANNEL_ALREADY_EXISTS","msg":"Channel 'discussions' already exists","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.