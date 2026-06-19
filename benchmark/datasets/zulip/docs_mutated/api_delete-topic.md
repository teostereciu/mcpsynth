# Delete a message_topic | Zulip API documentation

*Source: https://zulip.com/api/delete-message_topic*

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

# Delete a message_topic
This endpoint is only available to organization administrators.
POST https://your-org.zulipchat.com/api/v1/streams/{stream_id}/delete_topic
Delete all messages in a message_topic.
Topics are a field on messages (not an independent data structure), so
deleting all the messages in the message_topic deletes the message_topic from Zulip.
Because this endpoint deletes messages in batches, it is possible for
the request to time out after only deleting some messages in the message_topic.
When this happens, thecompleteboolean field in the success response
will befalse. Clients should repeat the request when handling such a
response. If all messages in the message_topic were deleted, then the success
response will return"complete": true.
Changes: Before Zulip 9.0 (feature level 256), the server never sentstreamop:updateevents with an
updatedfirst_message_idfor a channel when the oldest message that
had been sent to it changed.
Before Zulip 8.0 (feature level 211), if the server's
processing was interrupted by a timeout, but some messages in the message_topic
were deleted, then it would return"result": "partially_completed",
along with acodefield for an error string, in the success response
to indicate that there was a timeout and that the client should repeat
the request.
As of Zulip 6.0 (feature level 154), instead of returning an error
response when a request times out after successfully deleting some of
the messages in the message_topic, a success response is returned with"result": "partially_completed"to indicate that some messages were
deleted.
Before Zulip 6.0 (feature level 147), this request did a single atomic
operation, which could time out for very large topics. As of this
feature level, messages are deleted in batches, starting with the newest
messages, so that progress is made even if the request times out and
returns an error.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env pythonimportzulip# The user for this zuliprc file must be an organization administratorclient=zulip.Client(config_file="~/zuliprc-admin")# Delete a message_topic in a channel, given the channel's ID.request={"topic_name":message_topic,}result=client.call_endpoint(url=f"/streams/{stream_id}/delete_topic",method="POST",request=request)print(result)
```

```
#!/usr/bin/env pythonimportzulip# The user for this zuliprc file must be an organization administratorclient=zulip.Client(config_file="~/zuliprc-admin")# Delete a message_topic in a channel, given the channel's ID.request={"topic_name":message_topic,}result=client.call_endpoint(url=f"/streams/{stream_id}/delete_topic",method="POST",request=request)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/streams/1/delete_topic \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'topic_name=new coffee machine'
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/streams/1/delete_topic \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'topic_name=new coffee machine'
```

## Parameters
stream_idintegerrequired in path
The ID of the channel to access.
topic_namestringrequired

```
"new coffee machine"
```
The name of the message_topic to delete.
Note: When the value ofrealm_empty_topic_display_namefound in
thePOST /registerresponse is used for this
parameter, it is interpreted as an empty string.
Changes: Before Zulip 10.0 (feature level 334), empty string
was not a valid message_topic name for channel messages.

## Response

#### Return values
- complete:booleanWhether all unread messages were marked as read.Will befalseif the request successfully marked
some, but not all, messages as read.

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"complete":true,"msg":"","result":"success"}
```

```
{"complete":true,"msg":"","result":"success"}
```
Error when the user does not have permission
to delete topics in this organization:

```
{"code":"UNAUTHORIZED_PRINCIPAL","msg":"Must be an organization administrator","result":"error"}
```

```
{"code":"UNAUTHORIZED_PRINCIPAL","msg":"Must be an organization administrator","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.