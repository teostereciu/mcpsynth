# Real-time events API | Zulip API documentation

*Source: https://zulip.com/api/real-time-events*

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

# Real-time events API
Zulip's real-time events API lets you write software that reacts
immediately to events happening in Zulip.  This API is what powers the
real-time updates in the Zulip web and mobile apps.  As a result, the
events available via this API cover all changes to data displayed in
the Zulip product, from new messages to channel descriptions to
emoji reactions to changes in user or organization-level settings.

## Using the events API
The simplest way to use Zulip's real-time events API is by usingcall_on_each_eventfrom our Python bindings.  You just need to write
a Python function (in the examples below, thelambdas) and pass it
intocall_on_each_event; your function will be called whenever a new
event matching the specified parameters (event_types,filter_spec,
etc.) occurs in Zulip.
call_on_each_eventtakes care of all the potentially tricky details
of long-polling, error handling, exponential backoff in retries, etc.
It's cousin,call_on_each_message, provides an even simpler
interface for processing Zulip messages.
More complex applications (like a Zulip terminal client) may need to
instead use the rawregisterandeventsendpoints.

## Usage examples
Python
- Python

```
#!/usr/bin/env pythonimportsysimportzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Print every message the current user would receive# This is a blocking call that will run foreverclient.call_on_each_message(lambdamsg:sys.stdout.write(str(msg)+"\n"))# Print every event relevant to the user# This is a blocking call that will run foreverclient.call_on_each_event(lambdaevent:sys.stdout.write(str(event)+"\n"))
```

```
#!/usr/bin/env pythonimportsysimportzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Print every message the current user would receive# This is a blocking call that will run foreverclient.call_on_each_message(lambdamsg:sys.stdout.write(str(msg)+"\n"))# Print every event relevant to the user# This is a blocking call that will run foreverclient.call_on_each_event(lambdaevent:sys.stdout.write(str(event)+"\n"))
```

## Parameters
You may also pass in the following keyword arguments tocall_on_each_event:
event_types(string)[]optional

```
["message"]
```
A JSON-encoded array indicating which types of events you're interested
in. Values that you might find useful include:
- message(messages)
- subscription(changes in your subscriptions)
- realm_user(changes to users in the organization and
  their properties, such as their name).
If you do not specify this parameter, you will receive all
events, and have to filter out the events not relevant to
your client in your client code. For most applications, one
is only interested in messages, so one specifies:"event_types": ["message"]
Event types not supported by the server are ignored, in order to simplify
the implementation of client apps that support multiple server versions.
filter_spec((string)[])[]optional

```
[["channel", "Denmark"]]
```
A JSON-encoded array of arrays of length 2 indicating thenarrow filter(s)for which you'd
like to receive events for.
For example, to receive events for direct messages (including
group direct messages) received by the user, one can use"filter_spec": [["is", "dm"]].
Unlike the API forfetching messages,
this filter_spec parameter is simply a filter on messages that the
user receives through their channel subscriptions (or because
they are a recipient of a direct message).
This means that a client that requests anarrowfilter of[["channel", "Denmark"]]will receive events for new messages
sent to that channel while the user is subscribed to that
channel. The client will not receive any message events at all
if the user is not subscribed to"Denmark".
Newly created bot users are not usually subscribed to any
channels, so bots using this API need to besubscribedto any channels whose messages
you'd like them to process using this endpoint.
See theall_public_streamsparameter for how to process all
public channel messages in an organization.
Changes: Seechanges sectionof search/filter_spec filter documentation.
Defaults to[].
all_public_streamsbooleanoptional
Whether you would like to request message events from all public
channels. Useful for workflow bots that you'd like to see all new messages
sent to public channels. (You can also subscribe the user to private channels).
Defaults tofalse.
See theGET /eventsdocumentation for
more details on the format of individual events.
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.