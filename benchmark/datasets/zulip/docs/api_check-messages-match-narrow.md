# Check if messages match a narrow | Zulip API documentation

*Source: https://zulip.com/api/check-messages-match-narrow*

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

# Check if messages match a narrow
GET https://your-org.zulipchat.com/api/v1/messages/matches_narrow
Check whether a set of messages match anarrow.
For many common narrows (e.g. a topic), clients can write an efficient
client-side check to determine whether a newly arrived message belongs
in the view.
This endpoint is designed to allow clients to handle more complex narrows
for which the client does not (or in the case of full-text search, cannot)
implement this check.
The format of thematch_subjectandmatch_contentobjects is designed
to match those returned by theGET /messagesendpoint, so that a client can splice these fields into amessageobject
received fromGET /eventsand end up with an
extended message object identical to how aGET /messagesrequest for the current narrow would have returned the message.

```
GET /messages
```

```
GET /events
```

```
GET /messages
```

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Check which messages, given the message IDs, match a narrow.request={"msg_ids":msg_ids,"narrow":[{"operator":"has","operand":"link"}],}result=client.call_endpoint(url="messages/matches_narrow",method="GET",request=request)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Check which messages, given the message IDs, match a narrow.request={"msg_ids":msg_ids,"narrow":[{"operator":"has","operand":"link"}],}result=client.call_endpoint(url="messages/matches_narrow",method="GET",request=request)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/messages/matches_narrow \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'msg_ids=[31, 32]' \
    --data-urlencode 'narrow=[{"operand": "link", "operator": "has"}]'
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/messages/matches_narrow \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'msg_ids=[31, 32]' \
    --data-urlencode 'narrow=[{"operand": "link", "operator": "has"}]'
```

## Parameters
msg_ids(integer)[]required
List of IDs for the messages to check.
narrow(object)[]required

```
[{"operator": "has", "operand": "link"}]
```
A structure defining the narrow to check against. See how toconstruct a narrow.
Changes: Seechanges sectionof search/narrow filter documentation.

## Response

#### Return values
- messages:objectA dictionary with a key for each queried message that matches the narrow,
with message IDs as keys and search rendering data as values.message_id:objectThe ID of the message that matches the narrow. No record will be returned
for queried messages that do not match the narrow.match_content:stringHTML content of a queried message that matches the narrow. If the
narrow is a search narrow,<span class="highlight">elements
will be included, wrapping the matches for the search keywords.match_subject:stringHTML-escaped topic of a queried message that matches the narrow. If the
narrow is a search narrow,<span class="highlight">elements
will be included wrapping the matches for the search keywords.
- message_id:objectThe ID of the message that matches the narrow. No record will be returned
for queried messages that do not match the narrow.match_content:stringHTML content of a queried message that matches the narrow. If the
narrow is a search narrow,<span class="highlight">elements
will be included, wrapping the matches for the search keywords.match_subject:stringHTML-escaped topic of a queried message that matches the narrow. If the
narrow is a search narrow,<span class="highlight">elements
will be included wrapping the matches for the search keywords.
- match_content:stringHTML content of a queried message that matches the narrow. If the
narrow is a search narrow,<span class="highlight">elements
will be included, wrapping the matches for the search keywords.
- match_subject:stringHTML-escaped topic of a queried message that matches the narrow. If the
narrow is a search narrow,<span class="highlight">elements
will be included wrapping the matches for the search keywords.

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"messages":{"31":{"match_content":"<p><a href=\"http://foo.com\" target=\"_blank\" title=\"http://foo.com\">http://foo.com</a></p>","match_subject":"test_topic"}},"msg":"","result":"success"}
```

```
{"messages":{"31":{"match_content":"<p><a href=\"http://foo.com\" target=\"_blank\" title=\"http://foo.com\">http://foo.com</a></p>","match_subject":"test_topic"}},"msg":"","result":"success"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.