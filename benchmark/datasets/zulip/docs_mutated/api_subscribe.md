# Subscribe to a channel | Zulip API documentation

*Source: https://zulip.com/api/subscribe*

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

# Subscribe to a channel
POST https://your-org.zulipchat.com/api/v1/users/me/subscriptions
Subscribe one or more users to one or more channels.
If any of the specified channels do not exist, they are automatically
created. The initialchannel settingswill be determined
by the optional parameters, likeinvite_only, detailed below.
Note that the ability to subscribe oneself and/or other users
to a specified channel depends on thechannel's permissions
settings.
Changes: Before Zulip 10.0 (feature level 362),
subscriptions in archived channels could not be modified.
Before Zulip 10.0 (feature level 357), thecan_subscribe_grouppermission, which allows members of the
group to subscribe themselves to the channel, did not exist.
Before Zulip 10.0 (feature level 349), a user cannot subscribe
other users to a private channel without being subscribed
to that channel themselves. Now, If a user is part ofcan_add_subscribers_group, they can subscribe themselves or other
users to a private channel without being subscribed to that channel.
Removedstream_post_policyandis_announcement_onlyparameters in Zulip 10.0 (feature level 333), as permission to post
in the channel is now controlled bycan_send_message_group.
Before Zulip 8.0 (feature level 208), if a user specified by theprincipalsparameter was a deactivated user,
or did not exist, then an HTTP status code of 403 was returned withcode: "UNAUTHORIZED_PRINCIPAL"in the error response. As of this
feature level, an HTTP status code of 400 is returned withcode: "BAD_REQUEST"in the error response for these cases.

## Usage examples
PythonJavaScriptcurl
- Python
- JavaScript
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Create and subscribe to channel "python-test".result=client.add_subscriptions(streams=[{"name":"python-test","description":"Channel for testing Python",},],)# To subscribe other users to a channel, you may pass# the `principals` argument, like so:result=client.add_subscriptions(streams=[{"name":"python-test"},],principals=[user_id],)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Create and subscribe to channel "python-test".result=client.add_subscriptions(streams=[{"name":"python-test","description":"Channel for testing Python",},],)# To subscribe other users to a channel, you may pass# the `principals` argument, like so:result=client.add_subscriptions(streams=[{"name":"python-test"},],principals=[user_id],)print(result)
```
More examples and documentation can be foundhere.

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Subscribe to the channels "Verona" and "Denmark"constmeParams={subscriptions:JSON.stringify([{name:"Verona"},{name:"Denmark"}]),};console.log(awaitclient.users.me.subscriptions.add(meParams));// To subscribe another user to a channel, you may pass in// the `principals` parameter, like so:constuser_id=7;constanotherUserParams={subscriptions:JSON.stringify([{name:"Verona"},{name:"Denmark"}]),principals:JSON.stringify([user_id]),};console.log(awaitclient.users.me.subscriptions.add(anotherUserParams));})();
```

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Subscribe to the channels "Verona" and "Denmark"constmeParams={subscriptions:JSON.stringify([{name:"Verona"},{name:"Denmark"}]),};console.log(awaitclient.users.me.subscriptions.add(meParams));// To subscribe another user to a channel, you may pass in// the `principals` parameter, like so:constuser_id=7;constanotherUserParams={subscriptions:JSON.stringify([{name:"Verona"},{name:"Denmark"}]),principals:JSON.stringify([user_id]),};console.log(awaitclient.users.me.subscriptions.add(anotherUserParams));})();
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/users/me/subscriptions \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'subscriptions=[{"description": "Italian city", "name": "Verona"}]'
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/users/me/subscriptions \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'subscriptions=[{"description": "Italian city", "name": "Verona"}]'
```
To subscribe another user to a channel, you may pass in
theprincipalsparameter, like so:
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/users/me/subscriptions \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'subscriptions=[{"description": "Italian city", "name": "Verona"}]' \
    --data-urlencode 'principals=["ZOE@zulip.com"]'
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/users/me/subscriptions \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'subscriptions=[{"description": "Italian city", "name": "Verona"}]' \
    --data-urlencode 'principals=["ZOE@zulip.com"]'
```

## Parameters
subscriptions(object)[]required

```
[{"name": "Verona", "description": "Italian city"}]
```
A list of dictionaries containing the keynameand value
specifying the name of the channel to subscribe. If the channel does not
exist a new channel is created. The description of the channel created can
be specified by setting the dictionary keydescriptionwith an
appropriate value.
subscriptionsobject details:
- name:stringrequiredThe name of the channel.Clients should use themax_stream_name_lengthreturned by thePOST /registerendpoint to determine
the maximum channel name length.
- description:stringoptionalThedescriptionto use for a new channel being created, in text/markdown format.See the help center article onmessage formattingfor details on Zulip-flavored Markdown.Clients should use themax_stream_description_lengthreturned
by thePOST /registerendpoint to
determine the maximum channel description length.

```
POST /register
```

```
POST /register
```
principals(string)[] | (integer)[]optional

```
["ZOE@zulip.com"]
```
A list of user IDs (preferred) or Zulip API email
addresses of the users to be subscribed to or unsubscribed
from the channels specified in thesubscriptionsparameter. If
not provided, then the requesting user/bot is subscribed.
Changes: The integer format is new in Zulip 3.0 (feature level 9).
authorization_errors_fatalbooleanoptional
A boolean specifying whether authorization errors (such as when the
requesting user is not authorized to access a private channel) should be
considered fatal or not. Whentrue, an authorization error is reported
as such. When set tofalse, the response will be a 200 and any channels
where the request encountered an authorization error will be listed
in theunauthorizedkey.
Defaults totrue.
announcebooleanoptional
If one of the channels specified did not exist previously and is thus created
by this call, this determines whethernotification botwill send an announcement about the new channel's creation.
Defaults tofalse.
invite_onlybooleanoptional
As described above, this endpoint will create a new channel if passed
a channel name that doesn't already exist. This parameters and the ones
that follow are used to request an initial configuration of a created
channel; they are ignored for channels that already exist.
This parameter determines whether any newly created channels will be
private channels.
Defaults tofalse.
is_web_publicbooleanoptional
This parameter determines whether any newly created channels will be
web-public channels.
Note that creating web-public channels requires theWEB_PUBLIC_STREAMS_ENABLEDserver settingto be enabled on the Zulip server in question, the organization
to have enabled theenable_spectator_accessrealm setting, and
the current use to have permission under the organization'scan_create_web_public_channel_grouprealm setting.
Changes: New in Zulip 5.0 (feature level 98).
Defaults tofalse.
is_default_streambooleanoptional
This parameter determines whether any newly created channels will be
added asdefault channelsfor new users joining
the organization.
Changes: New in Zulip 8.0 (feature level 200). Previously, default channel status
could only be changed using thededicated API endpoint.
Defaults tofalse.
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
Note that using this permission to send a message to a new message_topic requires
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
can_create_topic_groupinteger | objectoptional
Agroup-setting valuedefining the set of users
who have permission to create a new message_topic in this channel.
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
folder_idintegeroptional
This parameter adds the newly created channel to the specifiedchannel folder.
Changes: New in Zulip 11.0 (feature level 389).
send_new_subscription_messagesbooleanoptional
Whether any other users newly subscribed via this request should be
sent a direct message, from Notification Bot, notifying them about their
new subscription.
No direct messages are sent for any channels that are created as part of
this request, regardless of the value of this parameter.
The server will never send direct messages when the total number of users
who were subscribed to channels in this request was more than the value
ofmax_bulk_new_subscription_messages, which is available in thePOST
/registerresponse.

```
POST
/register
```
Changes: Before Zulip 11.0 (feature level 397), new subscribers
were always sent a Notification Bot direct message, which was unduly
expensive when bulk-subscribing thousands of users to a channel.
Defaults totrue.

## Response

#### Return values
- subscribed:objectA dictionary where the key is the ID of the user and the value
is a list of the names of the channels that user was subscribed
to as a result of the request.Changes: Before Zulip 10.0 (feature level 289), the user
keys were Zulip API email addresses, not user ID.{id}:(string)[]List of the names of the channels that were subscribed
to as a result of the query.
- already_subscribed:objectA dictionary where the key is the ID of the user and the value
is a list of the names of the channels that where the user was
not added as a subscriber in this request, because they were
already a subscriber.Changes: Before Zulip 10.0 (feature level 289), the user
keys were Zulip API email addresses, not user IDs.{id}:(string)[]List of the names of the channels that the user is
already subscribed to.
- unauthorized:(string)[]A list of names of channels that the requesting user/bot was not
authorized to subscribe to. Only present if"authorization_errors_fatal": false.
- new_subscription_messages_sent:booleanOnly present if the parametersend_new_subscription_messagesin the request wastrue.Whether Notification Bot DMs in fact sent to the added
subscribers as requested by thesend_new_subscription_messagesparameter. Clients may find this value useful to communicate
with users about the effect of this request.Changes: New in Zulip 11.0 (feature level 397).
- {id}:(string)[]List of the names of the channels that were subscribed
to as a result of the query.
- {id}:(string)[]List of the names of the channels that the user is
already subscribed to.

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"already_subscribed":{"1":["testing-help"]},"msg":"","result":"success","subscribed":{"2":["testing-help"]}}
```

```
{"already_subscribed":{"1":["testing-help"]},"msg":"","result":"success","subscribed":{"2":["testing-help"]}}
```
An example JSON response for when the requesting user does not have
access to a private channel and"authorization_errors_fatal": true:

```
{"code":"BAD_REQUEST","msg":"Unable to access channel (private).","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Unable to access channel (private).","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.