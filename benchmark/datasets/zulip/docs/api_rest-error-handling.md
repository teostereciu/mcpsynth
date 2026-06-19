# Error handling | Zulip API documentation

*Source: https://zulip.com/api/rest-error-handling*

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

# Error handling
Zulip's API will always return a JSON format response.
The HTTP status code indicates whether the request was successful
(200 = success, 4xx = user error, 5xx = server error).
Every response, both success and error responses, will contain at least
two keys:
- msg: an internationalized, human-readable error message string.
- result: either"error"or"success", which is redundant with the
  HTTP status code, but is convenient when print debugging.
Every error response will also contain an additional key:
- code: a machine-readable error string, with a default value of"BAD_REQUEST"for general errors.
Clients should always checkcode, rather thanmsg, when looking for
specific error conditions. The string values formsgare
internationalized (e.g., the server will send the error message
translated into French if the user has a French locale), so checking
those strings will result in buggy code.
If a client needs information that is only present in the string value
 ofmsgfor a particular error response, then the developers
 implementing the client shouldstart a conversation herein order to discuss getting a specific errorcodeand/or relevant
 additional key/value pairs for that error response.
In addition to the keys described above, some error responses will
contain other keys with further details that are useful for clients. The
specific keys present depend on the errorcode, and are documented at
the API endpoints where these particular errors appear.
Changes: Before Zulip 5.0 (feature level 76), all error responses
did not contain acodekey, and its absence indicated that no specific
errorcodehad been allocated for that error.

## Common error responses
Documented below are some error responses that are common to many
endpoints:

### Invalid API key
A typical failed JSON response for when the API key is invalid.

```
{"code":"INVALID_API_KEY","msg":"Invalid API key","result":"error"}
```

```
{"code":"INVALID_API_KEY","msg":"Invalid API key","result":"error"}
```

### Missing request parameter
A typical failed JSON response for when a required request parameter
is not supplied.
The value ofvar_namecontains information about the missing parameter.

```
{"code":"REQUEST_VARIABLE_MISSING","msg":"Missing 'content' argument","result":"error","var_name":"content"}
```

```
{"code":"REQUEST_VARIABLE_MISSING","msg":"Missing 'content' argument","result":"error","var_name":"content"}
```

### Incompatible request parameters
A typical failed JSON response for when two or more, optional
parameters are supplied that are incompatible with each other.
The value ofparametersin the response is string containing
the parameters, separated by commas, that are incompatible.

```
{"code":"BAD_REQUEST","msg":"Unsupported parameter combination: object_id, object_name","parameters":"object_id, object_name","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Unsupported parameter combination: object_id, object_name","parameters":"object_id, object_name","result":"error"}
```

### User not authorized for query
A typical failed JSON response for when the user is not authorized for
a query.

```
{"code":"BAD_REQUEST","msg":"User not authorized for this query","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"User not authorized for this query","result":"error"}
```

### User account deactivated
A typical failed json response for when user's account is deactivated.
Changes: As of Zulip 5.0 (feature level 76), these errors use the
HTTP 401 status code. Before this feature level, they used the HTTP 403
status code.

```
{"code":"USER_DEACTIVATED","msg":"Account is deactivated","result":"error"}
```

```
{"code":"USER_DEACTIVATED","msg":"Account is deactivated","result":"error"}
```

### Realm deactivated
A typical failed json response for when user's organization is deactivated.
Changes: As of Zulip 5.0 (feature level 76), these errors use the
HTTP 401 status code. Before this feature level, they used the HTTP 403
status code.

```
{"code":"REALM_DEACTIVATED","msg":"This organization is deactivated","result":"error"}
```

```
{"code":"REALM_DEACTIVATED","msg":"This organization is deactivated","result":"error"}
```

### Rate limit exceeded
A typical failed JSON response for when a rate limit is exceeded.
Zulip sets a fewHTTP response headersto help with preventing rate limit errors.
The value ofretry-afterin the response indicates how many
seconds the client must wait before making additional requests.
Changes: Before Zulip 4.0 (feature level 36), thecodekey
was not present in rate limit errors.

```
{"code":"RATE_LIMIT_HIT","msg":"API usage exceeded rate limit","result":"error","retry-after":28.706807374954224}
```

```
{"code":"RATE_LIMIT_HIT","msg":"API usage exceeded rate limit","result":"error","retry-after":28.706807374954224}
```

## Ignored Parameters
In JSON success responses, all Zulip REST API endpoints may return
an array of parameters sent in the request that are not supported
by that specific endpoint.
While this can be expected, e.g., when sending both current and legacy
names for a parameter to a Zulip server of unknown version, this often
indicates either a bug in the client implementation or an attempt to
configure a new feature while connected to an older Zulip server that
does not support said feature.
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