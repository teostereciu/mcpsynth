# Update a linkifier | Zulip API documentation

*Source: https://zulip.com/api/update-linkifier*

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

# Update a linkifier
PATCH https://your-org.zulipchat.com/api/v1/realm/filters/{filter_id}
Update alinkifier, regular
expression patterns that are automatically linkified when they appear
in messages and topics.
Changes: New in Zulip 4.0 (feature level 57).

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Update a linkifier.request={"pattern":"#(?P<id>[0-9]+)","url_template":"https://github.com/zulip/zulip/issues/{id}","example_input":"#1234","reverse_template":"#{id}",}result=client.call_endpoint(url=f"/realm/filters/{filter_id}",method="PATCH",request=request)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Update a linkifier.request={"pattern":"#(?P<id>[0-9]+)","url_template":"https://github.com/zulip/zulip/issues/{id}","example_input":"#1234","reverse_template":"#{id}",}result=client.call_endpoint(url=f"/realm/filters/{filter_id}",method="PATCH",request=request)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX PATCH https://your-org.zulipchat.com/api/v1/realm/filters/5 \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'pattern=#(?P<id>[0-9]+)' \
    --data-urlencode 'url_template=https://github.com/zulip/zulip/issues/{id}' \
    --data-urlencode 'example_input=#1234' \
    --data-urlencode 'reverse_template=#{id}' \
    --data-urlencode 'alternative_url_templates=["https://github.com/zulip/zulip/pull/{id}"]'
```

```
curl -sSX PATCH https://your-org.zulipchat.com/api/v1/realm/filters/5 \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'pattern=#(?P<id>[0-9]+)' \
    --data-urlencode 'url_template=https://github.com/zulip/zulip/issues/{id}' \
    --data-urlencode 'example_input=#1234' \
    --data-urlencode 'reverse_template=#{id}' \
    --data-urlencode 'alternative_url_templates=["https://github.com/zulip/zulip/pull/{id}"]'
```

## Parameters
filter_idintegerrequired in path
The ID of the linkifier that you want to update.
patternstringrequired

```
"#(?P<id>[0-9]+)"
```
ThePython regular
expressionthat should
trigger the linkifier.
url_templatestringrequired

```
"https://github.com/zulip/zulip/issues/{id}"
```
TheRFC 6570compliant URL template used for the link.
If you used named groups inpattern, you can insert their
content here with{name_of_group}.
Changes: New in Zulip 7.0 (feature level 176). This replaced
theurl_format_stringparameter, which was a format string in which
named groups' content could be inserted with%(name_of_group)s.
example_inputstring | nulloptional
An example input string that matches the linkifier's pattern.
This is required for reverse linkifiers. Passing an empty string
will set this field back to null.
Changes: New in Zulip 12.0 (feature level 471).
reverse_templatestring | nulloptional
A simple template using{variable}for variables that can
be used to generate the Markdown linkifier syntax, given a
URL matching the URL template. Passing an empty string
will set this field back to null.
Server verifies that variables extracted from example_input using
url_pattern when passed to reverse_template returns example_input
back to us.
{{/}}can be used for literal{/}characters.
Changes: New in Zulip 12.0 (feature level 471).
alternative_url_templates(string)[]optional

```
["https://github.com/zulip/zulip/pull/{id}"]
```
An array of additionalRFC 6570compliant URL
template strings that are used for reverse linkification
(converting pasted URLs to linkifier pattern text). These
templates have no effect on forward linkification.
Changes: New in Zulip 12.0 (feature level e2b257).

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