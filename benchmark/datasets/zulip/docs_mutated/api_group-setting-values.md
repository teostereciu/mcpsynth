# Group-setting values | Zulip API documentation

*Source: https://zulip.com/api/group-setting-values*

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

# Group-setting values
Settings defining permissions in Zulip are increasingly represented
usinguser groups, which offer much more flexible
configuration than the olderrolessystem.
Note: Many group-valued settings are configured to require
a single system group for their value viaserver_supported_permission_settings, pending web app UI
changes to fully support group-setting values.
Changes: Before Zulip 10.0 (feature level 309), only system
groups were permitted values for group-setting values in
production environments, regardless of the values inserver_supported_permission_settings.
In the API, these settings are represented using agroup-setting
value, which can take two forms:
- An integer user group ID, which can be either a named user group
  visible in the UI or arole-based system group.
- An object with fieldsdirect_members, containing a list of
  integer user IDs, anddirect_subgroups, containing a list of
  integer group IDs. The setting's value is the union of the
  identified collection of users and groups.
Group-setting values in the object form can be thought of as an
anonymous group. They function very much like a named user group
object, and remove the naming and UI overhead involved in creating
a visible user group just to store the value of a single setting.
The server will canonicalize an object with an emptydirect_memberslist and adirect_subgroupslist that contains just a single group
ID to the integer format.

## System groups
The Zulip server maintains a collection of system groups that
correspond to the users with a given role; this makes it convenient to
store concepts like "all administrators" in a group-setting
value. These use a special naming convention and can be recognized by
theis_system_groupproperty on their group object.
The following system groups are maintained by the Zulip server:
- role:internet: Everyone on the Internet has this permission; this
  is used to configure thepublic access
  option.
- role:everyone: All users, including guests.
- role:members: All users, excluding guests.
- role:fullmembers: Allfull
  membersof the organization.
- role:moderators: All users with at least the moderator role.
- role:administrators: All users with at least the administrator
  role.
- role:owners: All users with the owner role.
- role:nobody: The formal empty group. Used in the API to represent
  disabling a feature.
Client UI for setting a permission or displaying a group (when
silently mentioned, for example) is encouraged to display system
groups using their description, rather than using theirrole:}names, which are chosen to be unique and clear in the API.
System groups should generally not be displayed in UI for
administering an organization's user groups, since they are not
directly mutable.

## Updating group-setting values
The Zulip API uses a special format for modifying an existing setting
using a group-setting value.
Agroup-setting updateis an object with anewfield and an
optionaloldfield, each containing a group-setting value. The
setting's value will be set to the membership expressed by thenewfield.
Theoldfield expresses the client's understanding of the current
value of the setting. If theoldfield is present and does not match
the actual current value of the setting, then the request will fail
with error codeEXPECTATION_MISMATCHand no changes will be applied.
When a user edits the setting in a UI, the resulting API request
should generally always include theoldfield, giving the value
the list had when the user started editing. This accurately expresses
the user's intent, and if two users edit the same list around the
same time, it prevents a situation where the second change
accidentally reverts the first one without either user noticing.
Omittingoldis appropriate where the intent really is a new complete
list rather than an edit, for example in an integration that syncs the
list from an external source of truth.

## Permitted values
Not every possible group-setting value is a valid configuration for a
given group-based setting. For example, as a security hardening
measure, some administrative permissions should never be exercised by
guest users, and the system group for all users, including guests,
should not be offered to users as an option for those settings.
Others have restrictions to only permit system groups due to UI
components not yet having been migrated to support a broader set of
values. In order to avoid this configuration ending up hardcoded in
clients, every permission setting using this framework has an entry in
theserver_supported_permission_settingssection of thePOST
/registerresponse.

```
POST
/register
```
Clients that support mutating group-settings values must parse that
part of theregisterpayload in order to compute the set of
permitted values to offer to the user and avoid server-side errors
when trying to save a value.
Note specifically that theallow_everyone_groupfield, which
determines whether the setting can have the value of "all user
accounts, including guests" also controls whether guests users can
exercise the permission regardless of their membership in the
group-setting value.
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.