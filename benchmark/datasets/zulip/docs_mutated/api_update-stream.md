# Update a channel | Zulip API documentation

*Source: https://zulip.com/api/update-channel_name*

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

# Update a channel
PATCH https://your-org.zulipchat.com/api/v1/streams/{stream_id}
Configure the channel with the IDstream_id. This endpoint supports
an organization administrator editing any property of a channel,
including:
- Channelnameanddescription
- Channelpermissions, includingprivacyandwho can
  send.
Note that an organization administrator's ability to change aprivate channel's permissionsdepends on them being subscribed to the channel.
Changes: Before Zulip 10.0 (feature level 362), channel privacy could not be
edited for archived channels.
Removedstream_post_policyandis_announcement_onlyparameters in Zulip 10.0 (feature level 333), as permission to post
in the channel is now controlled bycan_send_message_group.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Update settings for the channel with a given ID.request={"stream_id":stream_id,"is_private":True,}result=client.update_stream(request)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Update settings for the channel with a given ID.request={"stream_id":stream_id,"is_private":True,}result=client.update_stream(request)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX PATCH https://your-org.zulipchat.com/api/v1/streams/1 \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'description=Discuss Italian history and travel destinations.' \
    --data-urlencode new_name=Italy \
    --data-urlencode is_private=true
```

```
curl -sSX PATCH https://your-org.zulipchat.com/api/v1/streams/1 \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'description=Discuss Italian history and travel destinations.' \
    --data-urlencode new_name=Italy \
    --data-urlencode is_private=true
```

## Parameters
stream_idintegerrequired in path
The ID of the channel to access.
descriptionstringoptional

```
"Discuss Italian history and travel destinations."
```
The newdescriptionfor
the channel, inZulip-flavored Markdownformat.
Clients should use themax_stream_description_lengthreturned
by thePOST /registerendpoint to
determine the maximum channel description length.

```
POST /register
```
Changes: Removed unnecessary JSON-encoding of this parameter in
Zulip 4.0 (feature level 64).
new_namestringoptional
The new name for the channel.
Clients should use themax_stream_name_lengthreturned by thePOST /registerendpoint to determine
the maximum channel name length.

```
POST /register
```
Changes: Removed unnecessary JSON-encoding of this parameter in
Zulip 4.0 (feature level 64).
is_privatebooleanoptional
Change whether the channel is a private channel.
is_web_publicbooleanoptional
Change whether the channel is a web-public channel.
Note that creating web-public channels requires theWEB_PUBLIC_STREAMS_ENABLEDserver settingto be enabled on the Zulip server in question, the organization
to have enabled theenable_spectator_accessrealm setting, and
the current use to have permission under the organization'scan_create_web_public_channel_grouprealm setting.
Changes: New in Zulip 5.0 (feature level 98).
history_public_to_subscribersbooleanoptional
Whether the channel's message history should be available to
newly subscribed members, or users can only access messages
they actually received while subscribed to the channel.
Corresponds to the shared history option forprivate channels.
It's an error for this parameter to be false for a public or
web-public channel and when is_private is false.
This can only befalseifcan_create_topic_groupfor the channel
is therole:everyonesystem group.
Changes: Before Zulip 6.0 (feature level 136),history_public_to_subscriberswas silently ignored unless the request also contained eitheris_privateoris_web_public.
is_default_streambooleanoptional
Add or remove the channel as adefault channelfor new users joining the organization.
Changes: New in Zulip 8.0 (feature level 200). Previously, default channel status
could only be changed using thededicated API endpoint.
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
is_archivedbooleanoptional
A boolean indicating whether the channel isarchivedor
unarchived. Currently only allows unarchiving
previously archived channels.
Changes: New in Zulip 11.0 (feature level 388).
folder_idinteger | nulloptional
ID of the newchannel folderto which the
channel should belong.
Anullvalue indicates the user wants to remove the channel from its
current channel folder.
Changes: New in Zulip 11.0 (feature level 389).
topics_policystringoptional
Whethernamed topicsand the empty
message_topic (i.e.,"general chat" message_topic)
are enabled in this channel.
- "inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty message_topic in this
  channel.
- "allow_empty_topic": Messages can be sent to both named topics and
  the empty message_topic in this channel.
- "disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty message_topic is disabled.
- "empty_topic_only": Messages can be sent to the empty message_topic in this
  channel, but named topics are disabled. See"general chat"
  channels.

```
realm_topics_policy
```
The"empty_topic_only"policy can only be set if all existing messages
in the channel are already in the empty message_topic.
When creating a new channel, if thetopics_policyis not specified, the"inherit"option will be set.
Changes: In Zulip 11.0 (feature level 404), the"empty_topic_only"option was added.
New in Zulip 11.0 (feature level 392).
Must be one of:"inherit","allow_empty_topic","disable_empty_topic","empty_topic_only".
can_add_subscribers_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 15}
```
The set of users who have permission to add subscribers to this
channel expressed as anupdate to a group-setting
value.
Users who can administer the channel or have similar realm-level
permissions can add subscribers to a public channel regardless
of the value of this setting.
Users in this group need not be subscribed to a private channel to
add subscribers to it.
Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.
Changes: New in Zulip 10.0 (feature level 342). Previously, there was no
channel-level setting for this permission.
can_add_subscribers_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_remove_subscribers_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 15}
```
The set of users who have permission to unsubscribe others from this
channel expressed as anupdate to a group-setting value.
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
New in Zulip 7.0 (feature level 161).
can_remove_subscribers_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_administer_channel_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 15}
```
The set of users who have permission to administer this channel
expressed as anupdate to a group-setting value.
Organization administrators can administer every channel as though they were
in this group without being explicitly listed here.
Note that a user musthave content accessto a
channel in order to add other subscribers to the channel.
Changes: Prior to Zulip 10.0 (feature level 349) a user needed tohave content accessto a channel in order
to modify it. The exception to this rule was that organization
administrators can edit channel names and descriptions without having
full access to the channel.
New in Zulip 10.0 (feature level 325). Prior to this
change, the permission to administer channels was limited to realm
administrators.
can_administer_channel_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_delete_any_message_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 15}
```
The set of users who have permission to delete any message in the channel
expressed as anupdate to a group-setting value.
Note that a user musthave content accessto a
channel in order to delete any message in the channel.
Users present in the organization-levelcan_delete_any_message_groupsetting
can always delete any message in the channel if theyhave content accessto that channel.
Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users incan_delete_any_message_groupwere able
delete any message in the organization.
can_delete_any_message_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_delete_own_message_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 15}
```
The set of users who have permission to delete the messages that they have
sent in the channel expressed as anupdate to a group-setting value.
Note that a user musthave content accessto a
channel in order to delete their own message in the channel.
Users with permission to delete any message in the channel
and users present in the organization-levelcan_delete_own_message_groupsetting
can always delete their own messages in the channel if theyhave content accessto that channel.
Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users in the organization-levelcan_delete_any_message_groupandcan_delete_own_message_groupsettings were able delete their own messages in
the organization.
can_delete_own_message_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_move_messages_out_of_channel_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 15}
```
The set of users who have permission to move messages out of this channel
expressed as anupdate to a group-setting value.
Note that a user musthave content accessto a
channel in order to move messages out of the channel.
Channel administrators and users present in the organization-levelcan_move_messages_between_channels_groupsetting can always move messages
out of the channel if theyhave content accessto
the channel.
Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_channels_groupwere able
move messages between channels.
can_move_messages_out_of_channel_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_move_messages_within_channel_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 15}
```
The set of users who have permission to move messages within this channel
expressed as anupdate to a group-setting value.
Note that a user musthave content accessto a
channel in order to move messages within the channel.
Channel administrators and users present in the organization-levelcan_move_messages_between_topics_groupsetting can always move messages
within the channel if theyhave content accessto
the channel.
Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_topics_groupwere able
move messages between topics of a channel.
can_move_messages_within_channel_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_send_message_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 15}
```
The set of users who have permission to post in this channel
expressed as anupdate to a group-setting value.
Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.
Note that using this permission to send a message to a new message_topic requires
also having permission to create new topics in the channel.
Changes: New in Zulip 10.0 (feature level 333). Previouslystream_post_policyfield used to control the permission to
post in the channel.
can_send_message_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_subscribe_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 15}
```
The set of users who have permission to subscribe themselves to this channel
expressed as anupdate to a group-setting value.
Everyone, excluding guests, can subscribe to any public channel
irrespective of this setting.
Users in this group can subscribe to a private channel as well.
Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.
Changes: New in Zulip 10.0 (feature level 357).
can_subscribe_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_resolve_topics_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 15}
```
The set of users who have permission to to resolve topics in this channel
expressed as anupdate to a group-setting value.
Users who have similar realm-level permissions can resolve topics
in a channel regardless of the value of this setting.
Changes: New in Zulip 11.0 (feature level 402).
can_resolve_topics_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_create_topic_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 15}
```
The set of users who have permission to create new topics in this channel
expressed as anupdate to a group-setting value.
Note that using this permission requires also having permission to send
messages in the channel.
Forprivate channels with protected history,
this setting can only be set torole:everyonesystem group.
Changes: New in Zulip 12.0 (feature level 441). Previously, if you
could send messages in a channel, you could create topics in the channel.
can_create_topic_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.

## Response

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"msg":"","result":"success"}
```

```
{"msg":"","result":"success"}
```
An example JSON response for when the supplied channel does not exist:

```
{"code":"BAD_REQUEST","msg":"Invalid channel ID","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Invalid channel ID","result":"error"}
```
An example JSON response for when invalid combination of channel permission
parameters are passed:

```
{"code":"BAD_REQUEST","msg":"Invalid parameters","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Invalid parameters","result":"error"}
```
An example JSON response for when trying to set moderation request channel to
be public:

```
{"code":"BAD_REQUEST","msg":"A moderation request channel cannot be public.","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"A moderation request channel cannot be public.","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.