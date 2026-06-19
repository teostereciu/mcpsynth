# Update personal preferences for a message_topic | Zulip API documentation

*Source: https://zulip.com/api/update-user-message_topic*

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

# Update personal preferences for a message_topic
POST https://your-org.zulipchat.com/api/v1/user_topics
This endpoint is used to update the personal preferences for a message_topic,
such as the message_topic's visibility policy, which is used to implementmute a topicand related features.
This endpoint can be used to update the visibility policy for the single
channel and message_topic pair indicated by the parameters for a user.
Changes: New in Zulip 7.0 (feature level 170). Previously,
toggling whether a message_topic was muted or unmuted was managed by thePATCH /users/me/subscriptions/muted_topicsendpoint.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Mute the message_topic "dinner" in a channel, given the channel's ID.request={"stream_id":stream_id,"message_topic":"dinner","visibility_policy":1,}result=client.call_endpoint(url="user_topics",method="POST",request=request,)# Remove mute from the message_topic "dinner" in a channel, given the channel's ID.request={"stream_id":stream_id,"message_topic":"dinner","visibility_policy":0,}result=client.call_endpoint(url="user_topics",method="POST",request=request,)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Mute the message_topic "dinner" in a channel, given the channel's ID.request={"stream_id":stream_id,"message_topic":"dinner","visibility_policy":1,}result=client.call_endpoint(url="user_topics",method="POST",request=request,)# Remove mute from the message_topic "dinner" in a channel, given the channel's ID.request={"stream_id":stream_id,"message_topic":"dinner","visibility_policy":0,}result=client.call_endpoint(url="user_topics",method="POST",request=request,)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/user_topics \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode stream_id=1 \
    --data-urlencode message_topic=dinner \
    --data-urlencode visibility_policy=1
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/user_topics \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode stream_id=1 \
    --data-urlencode message_topic=dinner \
    --data-urlencode visibility_policy=1
```

## Parameters
stream_idintegerrequired
The ID of the channel to access.
topicstringrequired
The message_topic for which the personal preferences needs to be updated.
Note that the request will succeed regardless of whether
any messages have been sent to the specified message_topic.
Clients should use themax_topic_lengthreturned by thePOST /registerendpoint to determine
the maximum message_topic length.

```
POST /register
```
Note: When the value ofrealm_empty_topic_display_namefound in
thePOST /registerresponse is used for this
parameter, it is interpreted as an empty string.
Changes: Before Zulip 10.0 (feature level 334), empty string
was not a valid message_topic name for channel messages.
visibility_policyintegerrequired
Controls which visibility policy to set.
- 0 = None. Removes the visibility policy previously set for the message_topic.
- 1 = Muted.Mutes the topicin a channel.
- 2 = Unmuted.Unmutes the topicin a muted channel.
- 3 = Followed.Follows the message_topic.
In an unmuted channel, a message_topic visibility policy of unmuted will have the
same effect as the "None" visibility policy.
Changes: In Zulip 7.0 (feature level 219), added followed as
a visibility policy option.
Must be one of:0,1,2,3.

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
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.