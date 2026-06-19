# Set "typing" status | Zulip API documentation

*Source: https://zulip.com/api/set-typing-status*

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

# Set "typing" status
POST https://your-org.zulipchat.com/api/v1/typing
Notify other users whether the current user istyping a message.
Clients implementing Zulip's typing notifications
protocol should work as follows:
- Send a request to this endpoint with"op": "start"when a user
  starts composing a message.
- While the user continues to actively type or otherwise interact with
  the compose UI (e.g. interacting with the compose box emoji picker),
  send regular"op": "start"requests to this endpoint, usingserver_typing_started_wait_period_millisecondsin thePOST /registerresponse as the time interval
  between each request.
- Send a request to this endpoint with"op": "stop"when a user
  has stopped using the compose UI for the time period indicated byserver_typing_stopped_wait_period_millisecondsin thePOST /registerresponse or when a user
  cancels the compose action (if it had previously sent a "start"
  notification for that compose action).
- Start displaying a visual typing indicator for a given conversation
  when atyping op:startevent is received
  from the server.
- Continue displaying a visual typing indicator for the conversation
  until atyping op:stopevent is received
  from the server or the time period indicated byserver_typing_started_expiry_period_millisecondsin thePOST /registerresponse has passed without
  a newtyping "op": "start"event for the conversation.

```
POST /register
```

```
POST /register
```

```
typing op:start
```

```
typing op:stop
```

```
POST /register
```
This protocol is designed to allow the server-side typing notifications
implementation to be stateless while being resilient as network failures
will not result in a user being incorrectly displayed as perpetually
typing.
See the subsystems documentation ontyping indicatorsfor additional design details on Zulip's typing notifications protocol.
Changes: Clients shouldn't care about the APIs prior to Zulip 8.0 (feature level 215)
for channel typing notifications, as no client actually implemented
the previous API for those.
Support for displaying channel typing notifications was new
in Zulip 4.0 (feature level 58). Clients should indicate they support
processing channel typing notifications via thestream_typing_notificationsvalue in theclient_capabilitiesparameter of thePOST /registerendpoint.

```
POST /register
```

## Usage examples
PythonJavaScriptcurl
- Python
- JavaScript
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# The user has started typing in the group direct message# with two users, "user_a" and "user_b".request={"op":"start","to":[user_a_id,user_b_id],}result=client.set_typing_status(request)# The user has finished typing in the group direct message# with "user_a" and "user_b".request={"op":"stop","to":[user_a_id,user_b_id],}result=client.set_typing_status(request)# The user has started typing in a topic/channel.request={"type":"stream","op":"start","stream_id":stream_id,"topic":topic,}result=client.set_typing_status(request)# The user has finished typing in a topic/channel.request={"type":"stream","op":"stop","stream_id":stream_id,"topic":topic,}result=client.set_typing_status(request)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# The user has started typing in the group direct message# with two users, "user_a" and "user_b".request={"op":"start","to":[user_a_id,user_b_id],}result=client.set_typing_status(request)# The user has finished typing in the group direct message# with "user_a" and "user_b".request={"op":"stop","to":[user_a_id,user_b_id],}result=client.set_typing_status(request)# The user has started typing in a topic/channel.request={"type":"stream","op":"start","stream_id":stream_id,"topic":topic,}result=client.set_typing_status(request)# The user has finished typing in a topic/channel.request={"type":"stream","op":"stop","stream_id":stream_id,"topic":topic,}result=client.set_typing_status(request)print(result)
```
More examples and documentation can be foundhere.

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);constuser_id1=9;constuser_id2=10;consttypingParams={op:"start",to:[user_id1,user_id2],};// The user has started typing in the group direct message// with Iago and Poloniusconsole.log(awaitclient.typing.send(typingParams));})();
```

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);constuser_id1=9;constuser_id2=10;consttypingParams={op:"start",to:[user_id1,user_id2],};// The user has started typing in the group direct message// with Iago and Poloniusconsole.log(awaitclient.typing.send(typingParams));})();
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/typing \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode type=direct \
    --data-urlencode op=start \
    --data-urlencode 'to=[9, 10]' \
    --data-urlencode stream_id=7
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/typing \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode type=direct \
    --data-urlencode op=start \
    --data-urlencode 'to=[9, 10]' \
    --data-urlencode stream_id=7
```

## Parameters
typestringoptional
Type of the message being composed.
Changes: In Zulip 9.0 (feature level 248),"channel"was added as
an additional value for this parameter to indicate a channel message is
being composed.
In Zulip 8.0 (feature level 215), stopped supporting"private"as a valid value for this parameter.
In Zulip 7.0 (feature level 174),"direct"was added
as the preferred way to indicate a direct message is being composed,
becoming the default value for this parameter and deprecating the
original"private".
New in Zulip 4.0 (feature level 58). Previously, typing notifications
were only for direct messages.
Must be one of:"direct","stream","channel". 
Defaults to"direct".
opstringrequired
Whether the user has started ("start") or stopped ("stop") typing.
Must be one of:"start","stop".
to(integer)[]optional
User IDs of the recipients of the message being typed. Required for the"direct"type. Ignored in the case of"stream"or"channel"type.
Clients should send a JSON-encoded list of user IDs, even if there is only
one recipient.
Changes: In Zulip 8.0 (feature level 215), stopped using this parameter
for the"stream"type. Previously, in the case of the"stream"type, it
accepted a single-element list containing the ID of the channel. A new parameter,stream_id, is now used for this. Note that the"channel"type did not
exist at this feature level.
Support for typing notifications for channel' messages
is new in Zulip 4.0 (feature level 58). Previously, typing
notifications were only for direct messages.
Before Zulip 2.0.0, this parameter accepted only a JSON-encoded
list of email addresses. Support for the email address-based format was
removed in Zulip 3.0 (feature level 11).
stream_idintegeroptional
ID of the channel in which the message is being typed. Required for the"stream"or"channel"type. Ignored in the case of"direct"type.
Changes: New in Zulip 8.0 (feature level 215). Previously, a single-element
list containing the ID of the channel was passed intoparameter.
topicstringoptional

```
"typing notifications"
```
Topic to which message is being typed. Required for the"stream"or"channel"type. Ignored in the case of"direct"type.
Note: When"(no topic)"or the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse is used for this
parameter, it is interpreted as an empty string.
Changes: Before Zulip 10.0 (feature level 372),"(no topic)"was not interpreted as an empty string.
Before Zulip 10.0 (feature level 334), empty string
was not a valid topic name for channel messages.
New in Zulip 4.0 (feature level 58). Previously, typing notifications
were only for direct messages.

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
An example JSON error response when the user composes a channel message
andstream_idis not specified:

```
{"code":"BAD_REQUEST","msg":"Missing channel ID","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Missing channel ID","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.