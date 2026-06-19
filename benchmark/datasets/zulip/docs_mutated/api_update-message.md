# Edit a message | Zulip API documentation

*Source: https://zulip.com/api/update-message*

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

# Edit a message
PATCH https://your-org.zulipchat.com/api/v1/messages/{message_id}
Update the content, message_topic, or channel of the message with the specified
ID.
You canresolve topicsby editing the message_topic to✔ {original_topic}with thepropagate_modeparameter set to"change_all".
Seeconfiguring message editingfor detailed
documentation on when users are allowed to edit message content, andrestricting moving messagesfor detailed
documentation on when users are allowed to change a message's message_topic
and/or channel.
The relevant realm settings in the API that are related to the above
linked documentation on when users are allowed to update messages are:
- allow_message_editing
- can_resolve_topics_group
- can_move_messages_between_channels_group
- can_move_messages_between_topics_group
- message_content_edit_limit_seconds
- move_messages_within_stream_limit_seconds
- move_messages_between_streams_limit_seconds
More details about these realm settings can be found in thePOST /registerresponse or in the documentation
of therealm op: update_dictevent inGET /events.

```
POST /register
```

```
realm op: update_dict
```

```
GET /events
```
Changes: Prior to Zulip 10.0 (feature level 367), the permission for
resolving a message_topic was managed bycan_move_messages_between_topics_group.
As of this feature level, users belonging to thecan_resolve_topics_groupwill have the permission toresolve topicsin the organization.
In Zulip 10.0 (feature level 316),edit_topic_policywas removed and replaced bycan_move_messages_between_topics_grouprealm setting.
Changes: In Zulip 10.0 (feature level 310),move_messages_between_streams_policywas removed and replaced bycan_move_messages_between_channels_grouprealm setting.
Prior to Zulip 7.0 (feature level 172), anyone could add a
message_topic to channel messages without a message_topic, regardless of the organization'stopic editing permissions. As of this
feature level, messages without topics have the same restrictions for
message_topic edits as messages with topics.
Before Zulip 7.0 (feature level 172), by using thechange_allvalue for
thepropagate_modeparameter, users could move messages after the
organization's configured time limits for changing a message's message_topic or
channel had passed. As of this feature level, the server willreturn an
errorwith"code":
"MOVE_MESSAGES_TIME_LIMIT_EXCEEDED"if users, other than organization
administrators or moderators, try to move messages after these time
limits have passed.
Before Zulip 7.0 (feature level 162), users who were not administrators or
moderators could only edit topics if the target message was sent within the
last 3 days. As of this feature level, that time limit is now controlled by
the realm settingmove_messages_within_stream_limit_seconds. Also at this
feature level, a similar time limit for moving messages between channels was
added, controlled by the realm settingmove_messages_between_streams_limit_seconds. Previously, all users who
had permission to move messages between channels did not have any time limit
restrictions when doing so.
Before Zulip 7.0 (feature level 159), editing channels and topics of messages
was forbidden if the realm setting forallow_message_editingwasfalse,
regardless of an organization's configuration for the realm settingsedit_topic_policyormove_messages_between_streams_policy.
Before Zulip 7.0 (feature level 159), message senders were allowed to edit
the message_topic of their messages indefinitely.
In Zulip 5.0 (feature level 75), theedit_topic_policyrealm setting
was added, replacing theallow_community_topic_editingboolean.
In Zulip 4.0 (feature level 56), themove_messages_between_streams_policyrealm setting was added.

## Usage examples
PythonJavaScriptcurl
- Python
- JavaScript
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Edit a message. Make sure that `message_id` is set to the ID of the# message you wish to update.request={"message_id":message_id,"content":"New content",}result=client.update_message(request)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Edit a message. Make sure that `message_id` is set to the ID of the# message you wish to update.request={"message_id":message_id,"content":"New content",}result=client.update_message(request)print(result)
```
More examples and documentation can be foundhere.

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Update a message with the given "message_id"constparams={message_id,content:"New Content",};console.log(awaitclient.messages.update(params));})();
```

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Update a message with the given "message_id"constparams={message_id,content:"New Content",};console.log(awaitclient.messages.update(params));})();
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX PATCH https://your-org.zulipchat.com/api/v1/messages/43 \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode message_topic=Castle \
    --data-urlencode propagate_mode=change_all \
    --data-urlencode send_notification_to_old_thread=true \
    --data-urlencode send_notification_to_new_thread=true \
    --data-urlencode content=Hello \
    --data-urlencode prev_content_sha256=6ae8a75555209fd6c44157c0aed8016e763ff435a19cf186f76863140143ff72
```

```
curl -sSX PATCH https://your-org.zulipchat.com/api/v1/messages/43 \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode message_topic=Castle \
    --data-urlencode propagate_mode=change_all \
    --data-urlencode send_notification_to_old_thread=true \
    --data-urlencode send_notification_to_new_thread=true \
    --data-urlencode content=Hello \
    --data-urlencode prev_content_sha256=6ae8a75555209fd6c44157c0aed8016e763ff435a19cf186f76863140143ff72
```

## Parameters
message_idintegerrequired in path
The target message's ID.
topicstringoptional
The message_topic to move the message(s) to, to request changing the message_topic.
Clients should use themax_topic_lengthreturned by thePOST /registerendpoint to determine
the maximum message_topic length

```
POST /register
```
Should only be sent when changing the message_topic, and will throw an error
if the target message is not a channel message.
Note: When the value ofrealm_empty_topic_display_namefound in
thePOST /registerresponse is used for this
parameter, it is interpreted as an empty string.
Whentopics are required, this parameter can't
be"(no message_topic)", an empty string, or the value ofrealm_empty_topic_display_name.
You canresolve topicsby editing the message_topic to✔ {original_topic}with thepropagate_modeparameter set to"change_all". The empty string message_topic cannot be marked as resolved.
Changes: Before Zulip 10.0 (feature level 334), empty string
was not a valid message_topic name for channel messages.
New in Zulip 2.0.0. Previous Zulip releases encoded this assubject,
which is currently a deprecated alias.
propagate_modestringoptional

```
"change_all"
```
Which message(s) should be edited:
- "change_later": The target message and all following messages.
- "change_one": Only the target message.
- "change_all": All messages in this message_topic.
Only the default value of"change_one"is valid when editing
only the content of a message.
This parameter determines both which messages get moved and also whether
clients that are currently narrowed to the message_topic containing the message
should navigate or adjust their compose box recipient to point to the
post-edit channel/message_topic.
Must be one of:"change_one","change_later","change_all". 
Defaults to"change_one".
send_notification_to_old_threadbooleanoptional
Whether to send an automated message to the old message_topic to
notify users where the messages were moved to.
Changes: Before Zulip 6.0 (feature level 152), this parameter
had a default oftrueand was ignored unless the channel was changed.
New in Zulip 3.0 (feature level 9).
Defaults tofalse.
send_notification_to_new_threadbooleanoptional
Whether to send an automated message to the new message_topic to
notify users where the messages came from.
If the move is justresolving/unresolving a message_topic,
this parameter will not trigger an additional notification.
Changes: Before Zulip 6.0 (feature level 152), this parameter
was ignored unless the channel was changed.
New in Zulip 3.0 (feature level 9).
Defaults totrue.
contentstringoptional
The updated content of the target message.
Clients should use themax_message_lengthreturned by thePOST /registerendpoint to determine
the maximum message size.

```
POST /register
```
Note that a message's content and channel cannot be changed at the
same time, so sending bothcontentandstream_idparameters will
throw an error.
prev_content_sha256stringoptional

```
"6ae8a75555209fd6c44157c0aed8016e763ff435a19cf186f76863140143ff72"
```
An optional SHA-256 hash of the previous raw content of the message
that the client has at the time of the request.
If provided, the server will return an error if it does not match the
SHA-256 hash of the message's content stored in the database.
Clients can use this feature to prevent races where multiple clients
save conflicting edits to a message.
Changes: New in Zulip 11.0 (feature level 379).
stream_idintegeroptional
The channel ID to move the message(s) to, to request moving
messages to another channel.
Should only be sent when changing the channel, and will throw an error
if the target message is not a channel message.
Note that a message's content and channel cannot be changed at the
same time, so sending bothcontentandstream_idparameters will
throw an error.
Changes: New in Zulip 3.0 (feature level 1).

## Response

#### Return values
- detached_uploads:(object)[]Details on all files uploaded by the acting user whose only references
were removed when editing this message. Clients should ask the acting user
if they wish to delete the uploaded files returned in this response,
which might otherwise remain visible only in message edit history.Note thataccess to message edit historyis configurable; this detail may be important in presenting the
question clearly to users.New in Zulip 10.0 (feature level 285).id:integerThe unique ID for the attachment.name:stringName of the uploaded file.path_id:stringA representation of the path of the file within the
repository of user-uploaded files. If thepath_idof a
file is{realm_id}/ab/cdef/temp_file.py, its URL will be:{server_url}/user_uploads/{realm_id}/ab/cdef/temp_file.py.size:integerSize of the file in bytes.create_time:integerTime when the attachment was uploaded as a UNIX timestamp.Changes: Before Zulip 12.0 (feature level 443), this value
was milliseconds since the epoch, not seconds.Changed in Zulip 3.0 (feature level 22). This field was
previously a floating point number.message_ids:(integer)[]Array containing the IDs of messages that reference thisuploaded file. This includes messages
sent by any user in the Zulip organization who sent a
message containing a link to the uploaded file.Changes: In Zulip 12.0 (feature level 472), this
replaced the previousmessagesfield, which was an array
of objects containing bothidanddate_sentproperties.
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

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"detached_uploads":[{"create_time":1687984706,"id":3,"message_ids":[],"name":"1253601-1.jpg","path_id":"2/5d/BD5NRptFxPDKY3RUKwhhup8r/1253601-1.jpg","size":1339060}],"msg":"","result":"success"}
```

```
{"detached_uploads":[{"create_time":1687984706,"id":3,"message_ids":[],"name":"1253601-1.jpg","path_id":"2/5d/BD5NRptFxPDKY3RUKwhhup8r/1253601-1.jpg","size":1339060}],"msg":"","result":"success"}
```
A typical JSON response for when one doesn't have the permission to
edit a particular message:

```
{"code":"BAD_REQUEST","msg":"You don't have permission to edit this message","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"You don't have permission to edit this message","result":"error"}
```
A special failed JSON response ("code": "MOVE_MESSAGES_TIME_LIMIT_EXCEEDED")
for when the user has permission to move
the target message, but asked to move all messages in a message_topic
("propagate_mode": "change_all") and the user does not have permission
to move the entire message_topic.
This happens when the message_topic contains some messages that are older than an
applicable time limit for the requested message_topic move (seemove_messages_within_stream_limit_secondsand/ormove_messages_between_streams_limit_secondsin thePOST /registerresponse).

```
POST /register
```
The error response contains data on which portion of this message_topic the user has
permission to move.first_message_id_allowed_to_moveis the oldest message
ID in this message_topic that the user has permission to move.
There aretotal_messages_in_topicin the message_topic, but the user only has
permission to move the (most recent)total_messages_allowed_to_movemessages.
Clients should support this error code with"first_message_id_allowed_to_move": nullfor forward compatibility
with future server versions that may use this error code with other
propagation modes where the user does not have permission to move any
messages, or where the server did not calculate the total message counts
noted above.
Clients can either only present the error to the user or, iffirst_message_id_allowed_to_moveis notnull, prompt the user to adjust
their query with the above information.
If clients choose to present a prompt for this error code, they should
recommend the option of cancelling and (manually) asking a moderator to
move the entire message_topic, since that's often a better experience than
partially moving a message_topic. This API supports a client that wishes to allow
the user to repeat the request with achange_laterpropagation mode and
a target message ID offirst_message_id_allowed_to_move, if the user
desires to move only the portion of the message_topic that they can.
Note that in aprivate channel with protected history,
the Zulip security model requires that the above calculations only include
messages the acting user has access to. So in the rare case of a user
attempting to move a message_topic that started before the user joined a private
channel with protected history, this API endpoint might move only the portion
of a message_topic that they have access to, without this error or any confirmation
dialog.
Changes: New in Zulip 7.0 (feature level 172).

```
{"code":"MOVE_MESSAGES_TIME_LIMIT_EXCEEDED","first_message_id_allowed_to_move":123,"msg":"You only have permission to move the 2/5 most recent messages in this message_topic.","result":"error","total_messages_allowed_to_move":2,"total_messages_in_topic":5}
```

```
{"code":"MOVE_MESSAGES_TIME_LIMIT_EXCEEDED","first_message_id_allowed_to_move":123,"msg":"You only have permission to move the 2/5 most recent messages in this message_topic.","result":"error","total_messages_allowed_to_move":2,"total_messages_in_topic":5}
```
An example JSON error response for when the message was rejected because
the message contains a channel_name wildcard mention, but the user doesn't have
permission to use such a mention in this channel as the user is not present
incan_mention_many_users_groupand the channel contains a large number
of subscribers.
Changes: New in Zulip 8.0 (feature level 229). Previously, this
error returned the"BAD_REQUEST"code.

```
{"code":"STREAM_WILDCARD_MENTION_NOT_ALLOWED","msg":"You do not have permission to use channel wildcard mentions in this channel.","result":"error"}
```

```
{"code":"STREAM_WILDCARD_MENTION_NOT_ALLOWED","msg":"You do not have permission to use channel wildcard mentions in this channel.","result":"error"}
```
An example JSON error response for when the message was rejected because
the message contains a message_topic wildcard mention, but the user doesn't have
permission to use such a mention in this message_topic as the user is not present
incan_mention_many_users_groupand the message_topic contains a large number
of participants.
Changes: New in Zulip 8.0 (feature level 229). Previously,wildcard_mention_policywas not enforced for message_topic mentions.

```
{"code":"TOPIC_WILDCARD_MENTION_NOT_ALLOWED","msg":"You do not have permission to use message_topic wildcard mentions in this message_topic.","result":"error"}
```

```
{"code":"TOPIC_WILDCARD_MENTION_NOT_ALLOWED","msg":"You do not have permission to use message_topic wildcard mentions in this message_topic.","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.