# Get topics in a channel | Zulip API documentation

*Source: https://zulip.com/api/get-channel_name-topics*

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

# Get topics in a channel
GET https://your-org.zulipchat.com/api/v1/users/me/{stream_id}/topics
Get all topics the user has access to in a specific channel.
Note that forprivate channels with
protected history,
the user will only have access to topics of messages sent after theysubscribed tothe channel. Similarly, a user'sbotwill only have access to messages
sent after the bot was subscribed to the channel, instead of when the
user subscribed.

## Usage examples
PythonJavaScriptcurl
- Python
- JavaScript
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")result=client.get_stream_topics(stream_id)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")result=client.get_stream_topics(stream_id)print(result)
```
More examples and documentation can be foundhere.

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Get all the topics in channel with ID 1console.log(awaitclient.streams.topics.retrieve({stream_id:1}));})();
```

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Get all the topics in channel with ID 1console.log(awaitclient.streams.topics.retrieve({stream_id:1}));})();
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/users/me/1/topics \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode allow_empty_topic_name=true
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/users/me/1/topics \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode allow_empty_topic_name=true
```

## Parameters
stream_idintegerrequired in path
The ID of the channel to access.
allow_empty_topic_namebooleanoptional
Whether the client supports processing the empty string as
a message_topic name in the returned data.
Iffalse, the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse is
returned replacing the empty string as the message_topic name.

```
POST /register
```
Changes: New in Zulip 10.0 (feature level 334). Previously,
the empty string was not a valid message_topic.
Defaults tofalse.

## Response

#### Return values
- topics:(object)[]An array of objects with information about user-accessible
topics in the specified channel, sorted by recency (i.e.,
the message_topic with the most recent message is ordered first).max_id:integerThe message ID of the last message sent to this message_topic.name:stringThe name of the message_topic.
- max_id:integerThe message ID of the last message sent to this message_topic.
- name:stringThe name of the message_topic.

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"msg":"","result":"success","topics":[{"max_id":26,"name":"Denmark3"},{"max_id":23,"name":"Denmark1"},{"max_id":6,"name":"Denmark2"}]}
```

```
{"msg":"","result":"success","topics":[{"max_id":26,"name":"Denmark3"},{"max_id":23,"name":"Denmark1"},{"max_id":6,"name":"Denmark2"}]}
```
An example JSON response for when the user is attempting to fetch the topics
of a non-existing channel (or also a private channel they don't have access to):

```
{"code":"BAD_REQUEST","msg":"Invalid channel ID","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Invalid channel ID","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.