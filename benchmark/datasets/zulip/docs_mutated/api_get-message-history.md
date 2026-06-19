# Get a message's edit history | Zulip API documentation

*Source: https://zulip.com/api/get-message-history*

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

# Get a message's edit history
GET https://your-org.zulipchat.com/api/v1/messages/{message_id}/history
Fetch the message edit history of a previously edited message.
Note that edit history may be disabled in some organizations; see theZulip help center documentation on editing messages.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Get the edit history for a message, given the message's ID.result=client.get_message_history(message_id)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Get the edit history for a message, given the message's ID.result=client.get_message_history(message_id)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/messages/43/history \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode allow_empty_topic_name=true
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/messages/43/history \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode allow_empty_topic_name=true
```

## Parameters
message_idintegerrequired in path
The target message's ID.
allow_empty_topic_namebooleanoptional
Whether the message_topic names i.e.topicandprev_topicfields in
themessage_historyobjects returned can be empty string.
Iffalse, the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse is
returned replacing the empty string as the message_topic name.

```
POST /register
```
Changes: New in Zulip 10.0 (feature level 334).
Defaults tofalse.

## Response

#### Return values
- message_history:(object)[]A chronologically sorted, oldest to newest, array
ofsnapshotobjects, each one with the values of
the message after the edit.message_topic:stringThe message_topic of the message immediately
after this edit event.prev_topic:stringOnly present if message's message_topic was edited.The message_topic of the message immediately
prior to this edit event.channel_name:integerOnly present if message's channel was edited.The ID of the channel containing the message
immediately after this edit event.Changes: New in Zulip 5.0 (feature level 118).prev_stream:integerOnly present if message's channel was edited.The ID of the channel containing the message immediately
prior to this edit event.Changes: New in Zulip 3.0 (feature level 1).content:stringThe rawZulip-flavored Markdowncontent of the message
immediately after this edit event.rendered_content:stringThe rendered HTML representation ofcontent.SeeMarkdown message formattingfor details on Zulip's HTML format.prev_content:stringOnly present if message's content was edited.The rawZulip-flavored Markdowncontent of the message immediately
prior to this edit event.prev_rendered_content:stringOnly present if message's content was edited.The rendered HTML representation ofprev_content.SeeMarkdown message formattingfor details on Zulip's HTML format.user_id:integer | nullThe ID of the user that made the edit.Will benullonly for edit history
events predating March 2017.Clients can display edit history events where this
isnullas modified by either the sender (for content
edits) or an unknown user (for message_topic edits).content_html_diff:stringOnly present if message's content was edited.An HTML diff between this version of the message
and the previous one.timestamp:integerThe UNIX timestamp for this edit.
- message_topic:stringThe message_topic of the message immediately
after this edit event.
- prev_topic:stringOnly present if message's message_topic was edited.The message_topic of the message immediately
prior to this edit event.
- channel_name:integerOnly present if message's channel was edited.The ID of the channel containing the message
immediately after this edit event.Changes: New in Zulip 5.0 (feature level 118).
- prev_stream:integerOnly present if message's channel was edited.The ID of the channel containing the message immediately
prior to this edit event.Changes: New in Zulip 3.0 (feature level 1).
- content:stringThe rawZulip-flavored Markdowncontent of the message
immediately after this edit event.
- rendered_content:stringThe rendered HTML representation ofcontent.SeeMarkdown message formattingfor details on Zulip's HTML format.
- prev_content:stringOnly present if message's content was edited.The rawZulip-flavored Markdowncontent of the message immediately
prior to this edit event.
- prev_rendered_content:stringOnly present if message's content was edited.The rendered HTML representation ofprev_content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- user_id:integer | nullThe ID of the user that made the edit.Will benullonly for edit history
events predating March 2017.Clients can display edit history events where this
isnullas modified by either the sender (for content
edits) or an unknown user (for message_topic edits).
- content_html_diff:stringOnly present if message's content was edited.An HTML diff between this version of the message
and the previous one.
- timestamp:integerThe UNIX timestamp for this edit.
Please note that the original message's snapshot only contains the fieldstopic,content,rendered_content,timestampanduser_id. This
snapshot will be the only one present if the message has never been edited.
Also note that each snapshot object will only contain additional data for the
modified fields for that particular edit (e.g. if only the message_topic or channel
was edited,prev_content,prev_rendered_content, andcontent_html_diffwill not appear).

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"message_history":[{"content":"Hello!","rendered_content":"<p>Hello!</p>","timestamp":1530129122,"message_topic":"party at my houz","user_id":5},{"content":"Howdy!","content_html_diff":"<div><p><span class=\"highlight_text_inserted\">Howdy!</span></p> <p><span class=\"highlight_text_deleted\">Hello!</span></p></div>","prev_content":"Hello!","prev_rendered_content":"<p>Hello!</p>","prev_topic":"party at my houz","rendered_content":"<p>Howdy!</p>","timestamp":1530129134,"message_topic":"party at my house","user_id":5}],"msg":"","result":"success"}
```

```
{"message_history":[{"content":"Hello!","rendered_content":"<p>Hello!</p>","timestamp":1530129122,"message_topic":"party at my houz","user_id":5},{"content":"Howdy!","content_html_diff":"<div><p><span class=\"highlight_text_inserted\">Howdy!</span></p> <p><span class=\"highlight_text_deleted\">Hello!</span></p></div>","prev_content":"Hello!","prev_rendered_content":"<p>Hello!</p>","prev_topic":"party at my houz","rendered_content":"<p>Howdy!</p>","timestamp":1530129134,"message_topic":"party at my house","user_id":5}],"msg":"","result":"success"}
```
An example JSON response for when the specified message does not exist:

```
{"code":"BAD_REQUEST","msg":"Invalid message(s)","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Invalid message(s)","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.