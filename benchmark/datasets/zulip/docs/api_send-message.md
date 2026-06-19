# Send a message | Zulip API documentation

*Source: https://zulip.com/api/send-message*

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

# Send a message
POST https://your-org.zulipchat.com/api/v1/messages
Send achannel messageor adirect message.

## Usage examples
PythonJavaScriptcurlzulip-send
- Python
- JavaScript
- curl
- zulip-send

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Send a channel message.request={"type":"stream","to":"Denmark","topic":"Castle","content":"I come not, friends, to steal away your hearts.",}result=client.send_message(request)# Send a direct message.request={"type":"private","to":[user_id],"content":"With mirth and laughter let old wrinkles come.",}result=client.send_message(request)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Send a channel message.request={"type":"stream","to":"Denmark","topic":"Castle","content":"I come not, friends, to steal away your hearts.",}result=client.send_message(request)# Send a direct message.request={"type":"private","to":[user_id],"content":"With mirth and laughter let old wrinkles come.",}result=client.send_message(request)print(result)
```
More examples and documentation can be foundhere.

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Send a channel messageletparams={to:"social",type:"stream",topic:"Castle",content:"I come not, friends, to steal away your hearts.",};console.log(awaitclient.messages.send(params));// Send a direct messageconstuser_id=9;params={to:[user_id],type:"direct",content:"With mirth and laughter let old wrinkles come.",};console.log(awaitclient.messages.send(params));})();
```

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Send a channel messageletparams={to:"social",type:"stream",topic:"Castle",content:"I come not, friends, to steal away your hearts.",};console.log(awaitclient.messages.send(params));// Send a direct messageconstuser_id=9;params={to:[user_id],type:"direct",content:"With mirth and laughter let old wrinkles come.",};console.log(awaitclient.messages.send(params));})();
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
# For channel messages
curl -X POST https://your-org.zulipchat.com/api/v1/messages \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode type=stream \
    --data-urlencode 'to="Denmark"' \
    --data-urlencode topic=Castle \
    --data-urlencode 'content=I come not, friends, to steal away your hearts.'

# For direct messages
curl -X POST https://your-org.zulipchat.com/api/v1/messages \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode type=direct \
    --data-urlencode 'to=[9]' \
    --data-urlencode 'content=With mirth and laughter let old wrinkles come.'
```

```
# For channel messages
curl -X POST https://your-org.zulipchat.com/api/v1/messages \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode type=stream \
    --data-urlencode 'to="Denmark"' \
    --data-urlencode topic=Castle \
    --data-urlencode 'content=I come not, friends, to steal away your hearts.'

# For direct messages
curl -X POST https://your-org.zulipchat.com/api/v1/messages \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode type=direct \
    --data-urlencode 'to=[9]' \
    --data-urlencode 'content=With mirth and laughter let old wrinkles come.'
```
You can usezulip-send(available after youpip install zulip) to easily send Zulips from
the command-line, providing the message content via STDIN.

```
# For channel messageszulip-send--streamDenmark--subjectCastle\--userothello-bot@example.com--api-keya0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5# For direct messageszulip-sendhamlet@example.com\--userothello-bot@example.com--api-keya0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5
```

```
# For channel messageszulip-send--streamDenmark--subjectCastle\--userothello-bot@example.com--api-keya0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5# For direct messageszulip-sendhamlet@example.com\--userothello-bot@example.com--api-keya0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5
```

#### Passing in the message on the command-line
If you'd like, you can also provide the message on the command-line with the-mor--messageflag, as follows:

```
zulip-send--streamDenmark--subjectCastle\--message'I come not, friends, to steal away your hearts.'\--userothello-bot@example.com--api-keya0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5
```

```
zulip-send--streamDenmark--subjectCastle\--message'I come not, friends, to steal away your hearts.'\--userothello-bot@example.com--api-keya0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5
```
You can omit theuserandapi-keyparameters if you have a~/.zuliprcfile.

## Parameters
typestringrequired
The type of message to be sent.
"direct"for a direct message and"stream"or"channel"for a
channel message.
Changes: In Zulip 9.0 (feature level 248),"channel"was added as
an additional value for this parameter to request a channel message.
In Zulip 7.0 (feature level 174),"direct"was added as
the preferred way to request a direct message, deprecating the original"private". While"private"is still supported for requesting direct
messages, clients are encouraged to use to the modern convention with
servers that support it, because support for"private"will eventually
be removed.
Must be one of:"direct","channel","stream","private".
tostring | integer | (string)[] | (integer)[]required
For channel messages, either the name or integer ID of the channel. For
direct messages, either a list containing integer user IDs or a list
containing string Zulip API email addresses.
Changes: Support for using user/channel IDs was added in Zulip 2.0.0.
contentstringrequired
The content of the message.
Clients should use themax_message_lengthreturned by thePOST /registerendpoint to determine
the maximum message size.

```
POST /register
```
topicstringoptional
The topic of the message. Only required for channel messages
("type": "stream"or"type": "channel"), ignored otherwise.
Clients should use themax_topic_lengthreturned by thePOST /registerendpoint to determine
the maximum topic length.

```
POST /register
```
Note: When"(no topic)"or the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse is used for this
parameter, it is interpreted as an empty string.
Whentopics are required, this parameter can't
be"(no topic)", an empty string, or the value ofrealm_empty_topic_display_name.
Changes: Before Zulip 10.0 (feature level 370),"(no topic)"was not interpreted as an empty string.
Before Zulip 10.0 (feature level 334), empty string
was not a valid topic name for channel messages.
New in Zulip 2.0.0. Previous Zulip releases encoded
this assubject, which is currently a deprecated alias.
queue_idstringoptional

```
"fb67bf8a-c031-47cc-84cf-ed80accacda8"
```
For clients supportinglocal echo,
theevent queueID for the client.
If passed,local_idis required.
If the message is successfully sent, the server will includelocal_message_idin themessageeventthat
the client with thisqueue_idwill receive.
local_idstringoptional
For clients supportinglocal echo,
a unique string-format identifier chosen freely by the client.
If passed,queue_idis required.
If the message is successfully sent, the server will pass it back to
the client without inspecting it aslocal_message_idin themessageeventthat the client with the
abovequeue_idwill receive.
read_by_senderbooleanoptional
Whether the message should be initially marked read by its
sender. If unspecified, the server uses a heuristic based
on the client name.
Changes: New in Zulip 8.0 (feature level 236).

## Response

#### Return values
- id:integerThe unique ID assigned to the sent message.
- automatic_new_visibility_policy:integerIf the message's sender had configured theirvisibility policy settingsto potentially automatically follow or unmute topics when sending messages,
and one of these policies did in fact change the user's visibility policy
for the topic where this message was sent, the new value for that user's
visibility policy for the recipient topic.Only present if the sender's visibility was in fact changed.The value can be eitherunmuted or followed.Clients will also be notified about the change in policy via auser_topicevent as usual. This field is intended to be used by clients
to explicitly inform the user when a topic's visibility policy was changed
automatically due to sending a message.For example, the Zulip web application uses this field to decide whether
to display a warning or notice suggesting to unmute the topic after
sending a message to a muted channel. Such a notice would be confusing in
the event that the act of sending the message had already resulted in the
user automatically unmuting or following the topic in question.Changes: New in Zulip 8.0 (feature level 218).

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"automatic_new_visibility_policy":2,"id":42,"msg":"","result":"success"}
```

```
{"automatic_new_visibility_policy":2,"id":42,"msg":"","result":"success"}
```
A typical failed JSON response for when a channel message is sent to a channel
that does not exist:

```
{"code":"STREAM_DOES_NOT_EXIST","msg":"Channel 'nonexistent' does not exist","result":"error","stream":"nonexistent"}
```

```
{"code":"STREAM_DOES_NOT_EXIST","msg":"Channel 'nonexistent' does not exist","result":"error","stream":"nonexistent"}
```
A typical failed JSON response for when a direct message is sent to a user
that does not exist:

```
{"code":"BAD_REQUEST","msg":"Invalid email 'eeshan@zulip.com'","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Invalid email 'eeshan@zulip.com'","result":"error"}
```
An example JSON error response for when the message was rejected because
the message contains a stream wildcard mention, but the user doesn't have
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
the message contains a topic wildcard mention, but the user doesn't have
permission to use such a mention in this topic as the user is not present
incan_mention_many_users_groupand the topic contains a large number
of participants.
Changes: New in Zulip 8.0 (feature level 229). Previously,wildcard_mention_policywas not enforced for topic mentions.

```
{"code":"TOPIC_WILDCARD_MENTION_NOT_ALLOWED","msg":"You do not have permission to use topic wildcard mentions in this topic.","result":"error"}
```

```
{"code":"TOPIC_WILDCARD_MENTION_NOT_ALLOWED","msg":"You do not have permission to use topic wildcard mentions in this topic.","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.