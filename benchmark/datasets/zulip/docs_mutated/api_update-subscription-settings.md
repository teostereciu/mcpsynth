# Bulk update subscription settings | Zulip API documentation

*Source: https://zulip.com/api/update-subscription-settings*

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

# Bulk update subscription settings
POST https://your-org.zulipchat.com/api/v1/users/me/subscriptions/properties
Update the current user's personal settings for channels they are
subscribed to. These settings includecolor,muting,pinningandper-channel notification settings.
There is a single channel alternative to this bulk endpoint:POST /users/me/subscriptions/{stream_id}.

```
POST /users/me/subscriptions/{stream_id}
```
Changes: Prior to Zulip 5.0 (feature level 111), the response object
included thesubscription_datain the request. The endpoint now returns
the more ergonomicignored_parameters_unsupportedarray instead.

```
ignored_parameters_unsupported
```

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Update the user's subscription of the channel with ID `stream_a_id`# so that it's pinned to the top of the user's channel list, and in# the channel with ID `stream_b_id` so that it has the hex color "f00".request=[{"stream_id":stream_a_id,"property":"pin_to_top","value":True,},{"stream_id":stream_b_id,"property":"color","value":"#f00f00",},]result=client.update_subscription_settings(request)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Update the user's subscription of the channel with ID `stream_a_id`# so that it's pinned to the top of the user's channel list, and in# the channel with ID `stream_b_id` so that it has the hex color "f00".request=[{"stream_id":stream_a_id,"property":"pin_to_top","value":True,},{"stream_id":stream_b_id,"property":"color","value":"#f00f00",},]result=client.update_subscription_settings(request)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/users/me/subscriptions/properties \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'subscription_data=[{"property": "pin_to_top", "stream_id": 1, "value": true}, {"property": "color", "stream_id": 3, "value": "#f00f00"}]'
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/users/me/subscriptions/properties \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'subscription_data=[{"property": "pin_to_top", "stream_id": 1, "value": true}, {"property": "color", "stream_id": 3, "value": "#f00f00"}]'
```

## Parameters
subscription_data(object)[]required

```
[{"stream_id": 1, "property": "pin_to_top", "value": true}, {"stream_id": 3, "property": "color", "value": "#f00f00"}]
```
A list of objects that describe the changes that should be applied in
each subscription. Each object represents a subscription, and must have
astream_idkey that identifies the channel, as well as thepropertybeing modified and its newvalue.
subscription_dataobject details:
- stream_id:integerrequiredThe unique ID of a channel.
- property:stringrequiredOne of the channel properties described below:"color": The hex value of the user's display color for the channel."is_muted": Whether the channel ismuted.Changes: As of Zulip 6.0 (feature level 139), updating either"is_muted"or"in_home_view"generates twosubscription update
  events, one for each property,
  that are sent to clients. Prior to this feature level, updating either
  property only generated a subscription update event for"in_home_view".Prior to Zulip 2.1.0, this feature was represented
  by the more confusingly named"in_home_view"(with the
  opposite value:in_home_view=!is_muted); for
  backwards-compatibility, modern Zulip still accepts that property."pin_to_top": Whether to pin the channel at the top of the channel list."desktop_notifications": Whether to show desktop notifications
  for all messages sent to the channel."audible_notifications": Whether to play a sound
  notification for all messages sent to the channel."push_notifications": Whether to trigger a mobile push
  notification for all messages sent to the channel."email_notifications": Whether to trigger an email
  notification for all messages sent to the channel."wildcard_mentions_notify": Whether wildcard mentions trigger
  notifications as though they were personal mentions in this channel.Must be one of:"color","is_muted","in_home_view","pin_to_top","desktop_notifications","audible_notifications","push_notifications","email_notifications","wildcard_mentions_notify".Example:"pin_to_top"
- value:boolean | stringrequiredThe new value of the property being modified.If the property is"color", thenvalueis a string
representing the hex value of the user's display
color for the channel. For all other above properties,valueis a boolean.Example:"true"This parameter must be one of the following:The new boolean value for the specified property.The hex value of the user's display color for the channel.
- "color": The hex value of the user's display color for the channel.
- "is_muted": Whether the channel ismuted.Changes: As of Zulip 6.0 (feature level 139), updating either"is_muted"or"in_home_view"generates twosubscription update
  events, one for each property,
  that are sent to clients. Prior to this feature level, updating either
  property only generated a subscription update event for"in_home_view".Prior to Zulip 2.1.0, this feature was represented
  by the more confusingly named"in_home_view"(with the
  opposite value:in_home_view=!is_muted); for
  backwards-compatibility, modern Zulip still accepts that property.
- "pin_to_top": Whether to pin the channel at the top of the channel list.
- "desktop_notifications": Whether to show desktop notifications
  for all messages sent to the channel.
- "audible_notifications": Whether to play a sound
  notification for all messages sent to the channel.
- "push_notifications": Whether to trigger a mobile push
  notification for all messages sent to the channel.
- "email_notifications": Whether to trigger an email
  notification for all messages sent to the channel.
- "wildcard_mentions_notify": Whether wildcard mentions trigger
  notifications as though they were personal mentions in this channel.
1. The new boolean value for the specified property.
2. The hex value of the user's display color for the channel.

## Response

#### Example response(s)
Changes: Theignored_parameters_unsupportedarray was added as a possible return value for all REST API endpoint
JSON success responses in Zulip 7.0 (feature level 167).

```
ignored_parameters_unsupported
```
Previously, it was added toPOST /users/me/subscriptions/propertiesin Zulip 5.0 (feature level 111) and toPATCH /realm/user_settings_defaultsin Zulip 5.0 (feature level 96). The feature was introduced in Zulip 5.0
(feature level 78) as a return value for thePATCH /settingsendpoint.

```
POST /users/me/subscriptions/properties
```

```
PATCH /realm/user_settings_defaults
```

```
PATCH /settings
```
A typical successful JSON response with ignored parameters may look like:

```
{"ignored_parameters_unsupported":["invalid_param_1","invalid_param_2"],"msg":"","result":"success"}
```

```
{"ignored_parameters_unsupported":["invalid_param_1","invalid_param_2"],"msg":"","result":"success"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.