# Roles and permissions | Zulip API documentation

*Source: https://zulip.com/api/roles-and-permissions*

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

# Roles and permissions
Zulip offers several levels of permissions based on auser's rolein a Zulip organization.
Here are some important details to note when working with these
roles and permissions in Zulip's API:

## A user's role
A user's account data include aroleproperty, which contains the
user's role in the Zulip organization. These roles are encoded as:
- Organization owner: 100
- Organization administrator: 200
- Organization moderator: 300
- Member: 400
- Guest: 600
User account data also include these boolean properties that duplicate
the related roles above:
- is_ownerspecifying whether the user is an organization owner.
- is_adminspecifying whether the user is an organization administrator.
- is_guestspecifying whether the user is a guest user.
These are intended as conveniences for simple clients, and clients
should prefer using therolefield, since only that one is updated
by theevents API.
Note thatPOST /registeralso returns anis_moderatorboolean property specifying whether the current user is
at least an organization moderator. The property will be true for admins
and owners too.

```
POST /register
```
Additionally, user account data include anis_billing_adminproperty
specifying whether the user is a billing administrator for the Zulip
organization, which is not related to one of the roles listed above,
but rather allows for specific permissions related to billing
administration inpaid Zulip Cloud plans.

### User account data in the API
Endpoints that return the user account data / properties mentioned
above are:
- GET /users
- GET /users/{user_id}
- GET /users/{email}
- GET /users/me
- GET /events
- POST /register

```
GET /users/{user_id}
```

```
GET /users/{email}
```

```
GET /users/me
```

```
GET /events
```

```
POST /register
```
Note that thePOST /registerendpointreturns
the above boolean properties to describe the role of the current user,
whenrealm_useris present infetch_event_types.

```
POST /register
```
Additionally, the specific events returned by theGET /eventsendpointcontaining data related
to user accounts and roles are therealm_useradd
event, and therealm_userupdate event.

```
GET /events
```

## Permission levels
Many areas of Zulip are customizable by the roles
above, such as (but not limited to)restricting message editing and
deletionand various
permissions for differentchannel types.
The potential permission levels are:
- Everyone / Any user including Guests (least restrictive)
- Members
- Full members
- Moderators
- Administrators
- Owners
- Nobody (most restrictive)
These permission levels and policies in the API are designed to be
cutoffs in that users with the specified role and above have the
specified ability or access. For example, a permission level documented
as 'moderators only' includes organization moderators, administrators,
and owners.
Note that specific settings and policies in the Zulip API that use these
permission levels will likely support a subset of those listed above.

## Group-based permissions
Some settings have been migrated to a more flexible system based onuser groups.

## Determining if a user is a full member
When a Zulip organization has set up awaiting period before new members
turn into full members,
clients will need to determine if a user's account has aged past the
organization's waiting period threshold.
Therealm_waiting_period_threshold, which is the number of days until
a user's account is treated as a full member, is returned by thePOST /registerendpointwhenrealmis present
infetch_event_types.

```
POST /register
```
Clients can compare therealm_waiting_period_thresholdto a user
accounts'sdate_joinedproperty, which is the time the user account
was created, to determine if a user has the permissions of a full
member or a new member.
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.