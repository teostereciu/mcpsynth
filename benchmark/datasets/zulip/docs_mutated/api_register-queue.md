# Register an event queue | Zulip API documentation

*Source: https://zulip.com/api/register-queue*

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

# Register an event queue
POST https://your-org.zulipchat.com/api/v1/register
This powerful endpoint can be used to register a Zulip "event queue"
(subscribed to certain types of "events", or updates to the messages
and other Zulip data the current user has access to), as well as to
fetch the current state of that data.
(registeralso powers thecall_on_each_eventPython API, and is
intended primarily for complex applications for which the more convenientcall_on_each_eventAPI is insufficient).
This endpoint returns aqueue_idand alast_event_id; these can be
used in subsequent calls to the"events" endpointto request events from
the Zulip server using long-polling.
The server will queue events for up to 10 minutes of inactivity.
After 10 minutes, your event queue will be garbage-collected. The
server will sendheartbeatevents every minute, which makes it easy
to implement a robust client that does not miss events unless the
client loses network connectivity with the Zulip server for 10 minutes
or longer.
Once the server garbage-collects your event queue, the server willreturn an errorwith a code ofBAD_EVENT_QUEUE_IDif you try to fetch events from
the event queue. Your software will need to handle that error
condition by re-initializing itself (e.g. this is what triggers your
browser reloading the Zulip web app when your laptop comes back online
after being offline for more than 10 minutes).
When prototyping with this API, we recommend first callingregisterwith noevent_typesparameter to see all the available data from all
supported event types. Before using your client in production, you
should set appropriateevent_typesandfetch_event_typesfilters
so that your client only requests the data it needs. A few minutes
doing this often saves 90% of the total bandwidth and other resources
consumed by a client using this API.
See theevents system developer documentationif you need deeper details about how the Zulip event queue system
works, avoids clients needing to worry about large classes of
potentially messy races, etc.
Changes: Removeddense_modesetting in Zulip 10.0 (feature level 364)
as we now haveweb_font_size_pxandweb_line_height_percentsettings for more control.
Before Zulip 7.0 (feature level 183), therealm_community_topic_editing_limit_secondsproperty
was returned by the response. It was removed because it
had not been in use since the realm settingmove_messages_within_stream_limit_secondswas introduced
in feature level 162.
In Zulip 7.0 (feature level 163), the realm settingemail_address_visibilitywas removed. It was replaced by auser
settingwith
arealm user default, with the encoding of different
values preserved. Clients can support all versions by supporting the
current API and treating every user as having the realm'semail_address_visibilityvalue.

## Usage examples
PythonJavaScriptcurl
- Python
- JavaScript
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Register the queue.result=client.register(event_types=["message","realm_emoji"],)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Register the queue.result=client.register(event_types=["message","realm_emoji"],)print(result)
```
More examples and documentation can be foundhere.

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Register a queueconstparams={event_types:["message"],};console.log(awaitclient.queues.register(params));})();
```

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Register a queueconstparams={event_types:["message"],};console.log(awaitclient.queues.register(params));})();
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/register \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'event_types=["message"]'
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/register \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'event_types=["message"]'
```

## Parameters
apply_markdownbooleanoptional
Set totrueif you would like the content to be rendered in HTML
format (otherwise the API will return the raw text that the user
entered)
Defaults tofalse.
client_gravatarbooleanoptional
Whether the client supports computing gravatars URLs. If
enabled,avatar_urlwill be included in the response only
if there is a Zulip avatar, and will benullfor users who
are using gravatar as their avatar. This option
significantly reduces the compressed size of user data,
since gravatar URLs are long, random strings and thus do not
compress well. Theclient_gravatarfield is set totrueif
clients can compute their own gravatars.
The default value istruefor authenticated requests andfalseforunauthenticated
requests. Passingtruein
an unauthenticated request is an error.
Changes: Before Zulip 6.0 (feature level 149), this
parameter was silently ignored and processed as though it
werefalsein unauthenticated requests.
include_subscribersstringoptional
Whether each returned channel object should include asubscribersfield containing a list of the user IDs of its subscribers.
Client apps supporting organizations with many thousands of users
should not passtrue, because the full subscriber matrix may be
several megabytes of data. Thepartialvalue, combined with thesubscriber_countand fetching subscribers for individual channels as
needed, is recommended to support client app features where channel
subscriber data is useful.
If a client passespartialfor this parameter, the server may,
for some channels, return a subset of the channel's subscribers
in thepartial_subscribersfield instead of thesubscribersfield,
which always contains the complete set of subscribers.
The server guarantees that it will always return asubscribersfield for channels with fewer than 250 total subscribers. When
returning apartial_subscribersfield, the server guarantees
that all bot users and users active within the last 14 days will
be included. For other cases, the server may use its discretion
to determine which channels and users to include, balancing between
payload size and usefulness of the data provided to the client.
Passingtruein anunauthenticated
requestis an error.
Changes: Thepartialvalue is new in Zulip 11.0 (feature level 412).
Before Zulip 6.0 (feature level 149), this parameter was silently
ignored and processed as though it werefalsein unauthenticated
requests.
New in Zulip 2.1.0.
Must be one of:"true","false","partial". 
Defaults to"false".
slim_presencebooleanoptional
Iftrue, thepresencesobject returned in the response will be keyed
by user ID and the entry for each user's presence data will be in the
modern format.
Changes: New in Zulip 3.0 (no feature level; API unstable).
Defaults tofalse.
presence_history_limit_daysintegeroptional
Limits how far back in time to fetch user presence data. If not specified,
defaults to 14 days. A value of N means that the oldest presence data
fetched will be from at most N days ago.
Changes: New in Zulip 10.0 (feature level 288).
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
all_public_streamsbooleanoptional
Whether you would like to request message events from all public
channels. Useful for workflow bots that you'd like to see all new messages
sent to public channels. (You can also subscribe the user to private channels).
Defaults tofalse.
client_capabilitiesobjectoptional

```
{"notification_settings_null": true}
```
Dictionary containing details on features the client supports that are
relevant to the format of responses sent by the server.
- notification_settings_null: Boolean for whether the
  client can handle the current API withnullvalues for
  channel-level notification settings (which means the channel
  is not customized and should inherit the user's global
  notification settings for channel messages).Changes: New in Zulip 2.1.0. In earlier Zulip releases,
  channel-level notification settings were simple booleans.
- bulk_message_deletion: Boolean for whether the client's
  handler for thedelete_messageevent type has been
  updated to process the new bulk format (with amessage_ids, rather than a singletonmessage_id).
  Otherwise, the server will senddelete_messageevents
  in a loop.Changes: New in Zulip 3.0 (feature level 13). This
  capability is for backwards-compatibility; it will be
  required in a future server release.
- user_avatar_url_field_optional: Boolean for whether the
  client required avatar URLs for all users, or supports
  usingGET /avatar/{user_id}to access user avatars. If the
  client has this capability, the server may skip sending aavatar_urlfield in therealm_userat its sole discretion
  to optimize network performance. This is an important optimization
  in organizations with 10,000s of users.Changes: New in Zulip 3.0 (feature level 18).
- stream_typing_notifications: Boolean for whether the client
  supports channel typing notifications.Changes: New in Zulip 4.0 (feature level 58). This capability is
  for backwards-compatibility; it will be required in a
  future server release.
- user_settings_object: Has no effect with modern servers. Previously,
  this was a boolean for whether the client supported the modernuser_settingsevent typeand
  the top-leveluser_settingsobject in this endpoint's response.Changes: Prior to Zulip 12.0 (feature level 439), if false, the
  server would additionally send the legacyupdate_global_notificationsandupdate_display_settingsevent types, if requested.New in Zulip 5.0 (feature level 89). Because the feature level 89 API
  changes were merged together, clients could safely make a request with
  this client capability, and also request all three event types
  (user_settings,update_display_settings, andupdate_global_notifications), and then use thezulip_feature_levelin this endpoint's response or the presence/absence of auser_settingskey to determine where to look for the data.
- linkifier_url_template: Boolean for whether the client acceptslinkifiersthat useRFC 6570compliant
  URL templates for linkifying matches. If false or unset, then therealm_linkifiersarray in the/registerresponse will be empty
  if present, and norealm_linkifierseventswill be sent to the client.Changes: New in Zulip 7.0 (feature level 176). This capability
  is for backwards-compatibility.
- user_list_incomplete: Boolean for whether the client supports not having an
  incomplete user database. If true, then therealm_usersarray in theregisterresponse will not include data for inaccessible users and clients of guest users will
  not receiverealm_user op:addevents for newly created users that are not accessible
  to the current user.Changes: New in Zulip 8.0 (feature level 232). This
  capability is for backwards-compatibility.
- include_deactivated_groups: Boolean for whether the client can handle
  deactivated user groups by themselves. If false, then therealm_user_groupsarray in the/registerresponse will only include active groups, clients
  will receive aremoveevent instead ofupdateevent when a group is
  deactivated and noupdateevent will be sent to the client if a deactivated
  user group is renamed.Changes: New in Zulip 10.0 (feature level 294). This
  capability is for backwards-compatibility.
- archived_channels: Boolean for whether the client supports processingarchived channelsin thestreamandsubscriptionevent types. Iffalse, the server will not include data
  related to archived channels in theregisterresponse or in events.Changes: New in Zulip 10.0 (feature level 315). This allows clients to
  access archived channels, without breaking backwards-compatibility for
  existing clients.
- empty_topic_name: Boolean for whether the client supports processing
  the empty string as a message_topic name. Clients not declaring this capability
  will be sent the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse instead of the empty string
  wherever message_topic names appear in the register response or events involving
  message_topic names.Changes: New in Zulip 10.0 (feature level 334). Previously,
  the empty string was not a valid message_topic name.
- simplified_presence_events: Boolean for whether the client supports
  receiving thepresenceevent typewith
  user presence data in the modern format. If true, the server will
  send these events with thepresencesfield that has the user presence
  data in the modern format. Otherwise, these event will contain fields
  with legacy format user presence data.Changes: New in Zulip 11.0 (feature level 419).

```
user_settings
```
fetch_event_types(string)[]optional

```
["message"]
```
Same as theevent_typesparameter except that the values infetch_event_typesare used to fetch initial data. Iffetch_event_typesis not provided,event_typesis used and ifevent_typesis not provided, this parameter defaults tonull.
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

## Response

#### Return values
- queue_id:string | nullThe ID of the queue that has been allocated for your client.Will benullonly for unauthenticated access in realms that have
enabled thepublic access option.
- last_event_id:integerThe initial value oflast_event_idto pass toGET /api/v1/events.
- zulip_feature_level:integerThe server's currentZulip feature level.Changes: As of Zulip 3.0 (feature level 3), this is always present
in the endpoint's response. Previously, it was only present ifevent_typesincludedzulip_version.New in Zulip 3.0 (feature level 1).
- zulip_version:stringThe server's version number. This is often a release version number,
like2.1.7. But for a server running aversion from Git,
it will be a Git reference to the commit, like5.0-dev-1650-gc3fd37755f.Changes: As of Zulip 3.0 (feature level 3), this is always present
in the endpoint's response. Previously, it was only present ifevent_typesincludedzulip_version.
- zulip_merge_base:stringThegit merge-basebetweenzulip_versionand official branches
in the publicZulip server and web app repository,
in the same format aszulip_version. This will equalzulip_versionif the server is not running a fork of the Zulip server.This will be""if the server does not know itsmerge-base.Changes: New in Zulip 5.0 (feature level 88).
- alert_words:(string)[]Present ifalert_wordsis present infetch_event_types.An array of strings, each analert wordthat the current user has configured.
- custom_profile_fields:(object)[]Present ifcustom_profile_fieldsis present infetch_event_types.An array of dictionaries where each dictionary contains the
details of a single custom profile field that is available to users
in this Zulip organization. This must be combined with the custom profile
field values on individual user objects to display users' profiles.id:integerThe ID of the custom profile field. This will be referenced in the custom
profile fields section of user objects.type:integerAn integer indicating the type of the custom profile field, which determines
how it is configured and displayed to users.See theCustom profile fieldsarticle for details on what each type means.1: Short text2: Paragraph3: Dropdown4: Date picker5: Link6: Person picker7: External account8: PronounsChanges: Field type8added in Zulip 6.0 (feature level 151).order:integerCustom profile fields are displayed in both settings UI and
UI showing users' profiles in increasingorder.name:stringThe name of the custom profile field.hint:stringThe help text to be displayed for the custom profile field in user-facing
settings UI for configuring custom profile fields.field_data:stringField types 3 (Dropdown) and 7 (External account) support storing
additional configuration for the field type in thefield_dataattribute.For field type 3 (Dropdown), this attribute is a JSON dictionary
defining the choices and the order they will be displayed in the
dropdown UI for individual users to select an option.The interface for field type 7 is not yet stabilized.display_in_profile_summary:booleanWhether the custom profile field, display or not on the user card.Must be false forPerson pickerprofile field types.This field is only included when its value istrue.Changes: Before Zulip 12.0 (feature level 476), the
"Paragraph" field type was not supported.New in Zulip 6.0 (feature level 146).required:booleanWhether an organization administrator has configured this profile field as
required.Because the required property is mutable, clients cannot assume that a required
custom profile field has a value. The Zulip web application displays a prominent
banner to any user who has not set a value for a required field.Changes: New in Zulip 9.0 (feature level 244).editable_by_user:booleanWhether regular users can edit this profile field on their own account.Note that organization administrators can edit custom profile fields for any user
regardless of this setting.Changes: New in Zulip 10.0 (feature level 296).use_for_user_matching:booleanWhether this custom profile field should be used to match users in typeahead
suggestions. Only allowed for Short Text and External Accountprofile field types.This field is only included when its value istrue.Changes: New in Zulip 12.0 (feature level 455).
- custom_profile_field_types:objectPresent ifcustom_profile_fieldsis present infetch_event_types.An array of objects; each object describes a type of custom profile field
that could be configured on this Zulip server. Each custom profile type
has an ID and thetypeproperty of a custom profile field is equal
to one of these IDs.This attribute is only useful for clients containing UI for changing
the set of configured custom profile fields in a Zulip organization.{FIELD_TYPE}:objectDictionary which contains the details
of the field type with the field type as the name of the
property itself. The current supported field types are as follows:SHORT_TEXTLONG_TEXTDATEfor date-based fields.SELECTfor a list of options.URLfor links.EXTERNAL_ACCOUNTfor external accounts.USERfor selecting a user for the field.PRONOUNSfor a short text field with convenient typeahead for one's preferred pronouns.Changes:PRONOUNStype added in Zulip 6.0 (feature level 151).id:integerThe ID of the custom profile field type.name:stringThe name of the custom profile field type.
- realm_date_created:integerPresent ifrealmis present infetch_event_types.The UNIX timestamp (UTC) for when the organization was
created.Changes: New in Zulip 8.0 (feature level 203).
- demo_organization_scheduled_deletion_date:integerPresent ifrealmis present infetch_event_types,
and the realm is a demo organization.The UNIX timestamp (UTC) when the demo organization will be
automatically deleted. Clients should use this to display a
prominent warning to the user that the organization will be
deleted at the indicated time.Changes: New in Zulip 5.0 (feature level 94).
- drafts:(object)[]An array containing draft objects for the user. These drafts are being
stored on the backend for the purpose of syncing across devices. This
array will be empty ifenable_drafts_synchronizationis set tofalse.id:integerThe unique ID of the draft. It will only used whenever the drafts are
fetched. This field should not be specified when the draft is being
created or edited.type:stringThe type of the draft. Either unaddressed (empty string),"channel_name",
or"private"(for one-on-one and group direct messages).to:(integer)[]An array of the tentative target audience IDs. For channel
messages, this should contain exactly 1 ID, the ID of the
target channel. For direct messages, this should be an array
of target user IDs. For unaddressed drafts, this is ignored,
and clients should send an empty array.message_topic:stringFor channel message drafts, the tentative message_topic name. For direct
or unaddressed messages, this will be ignored and should ideally
be the empty string. Should not contain null bytes.content:stringThe body of the draft. Should not contain null bytes.timestamp:integerA Unix timestamp (seconds only) representing when the draft was
last edited. When creating a draft, this key need not be present
and it will be filled in automatically by the server.
- onboarding_steps:(object)[]Present ifonboarding_stepsis present infetch_event_types.An array of dictionaries, where each dictionary contains details about
a single onboarding step that should be shown to the user.We expect that only official Zulip clients will interact with this data.Changes: Before Zulip 8.0 (feature level 233), this array was namedhotspots. Prior to this feature level, one-time notice onboarding
steps were not supported, and thetypefield in these objects did not
exist as all onboarding steps were implicitly hotspots.type:stringThe type of the onboarding step. Valid value is"one_time_notice".Changes: Removed type"hotspot"in Zulip 9.0 (feature level 259).New in Zulip 8.0 (feature level 233).name:stringThe name of the onboarding step.
- navigation_tour_video_url:string | nullPresent ifonboarding_stepsis present infetch_event_types.URL of the navigation tour video to display to new users during
onboarding. Ifnull, the onboarding video experience is disabled.Changes: New in Zulip 10.0 (feature level 369).
- max_message_id:integerPresent ifmessageis present infetch_event_types.The highest message ID among all messages the user has received as of the
moment of this request.Deprecated: This field may be removed in future versions as it no
longer has a clear purpose. Clients wishing to fetch the latest messages
should pass"start_message_id": "latest"toGET /messages.
- max_reminder_note_length:integerThe maximum allowed length for a reminder note, in Unicode code points.Changes: New in Zulip 11.0 (feature level 415).
- max_stream_name_length:integerPresent ifrealmis present infetch_event_types.The maximum allowed length for a channel name, in Unicode code
points. Clients should use this property rather than hardcoding
field sizes.Changes: New in Zulip 4.0 (feature level 53). Previously,
this requiredstreaminfetch_event_types, was calledstream_name_max_length, and always had a value of 60.
- max_stream_description_length:integerPresent ifrealmis present infetch_event_types.The maximum allowed length for a channel description, in Unicode
code points. Clients should use this property rather than hardcoding
field sizes.Changes: New in Zulip 4.0 (feature level 53). Previously,
this requiredstreaminfetch_event_types, was calledstream_description_max_length, and always had a value of 1024.
- max_channel_folder_name_length:integerPresent ifrealmis present infetch_event_types.The maximum allowed length for a channel folder name, in Unicode
code points. Clients should use this property rather than hardcoding
field sizes.Changes: New in Zulip 11.0 (feature level 410). Clients should use
60 as a fallback value on previous feature levels.
- max_channel_folder_description_length:integerPresent ifrealmis present infetch_event_types.The maximum allowed length for a channel folder description, in
Unicode code points. Clients should use this property rather than
hardcoding field sizes.Changes: New in Zulip 11.0 (feature level 410). Clients should use
1024 as a fallback value on previous feature levels.
- max_topic_length:integerPresent ifrealmis present infetch_event_types.The maximum allowed length for a message_topic, in Unicode code points.
Clients should use this property rather than hardcoding field
sizes.Changes: New in Zulip 4.0 (feature level 53). Previously,
this property always had a value of 60.
- max_message_length:integerPresent ifrealmis present infetch_event_types.The maximum allowed length for a message, in Unicode code points.
Clients should use this property rather than hardcoding field
sizes.Changes: New in Zulip 4.0 (feature level 53). Previously,
this property always had a value of 10000.
- server_min_deactivated_realm_deletion_days:integer | nullPresent ifrealmis present infetch_event_types.The minimum permitted number of days before full data deletion
(users, channels, messages, etc.) of a deactivated organization.
Ifnull, then a deactivated organization's data can be
deleted immediately.Changes: New in Zulip 10.0 (feature level 332)
- server_max_deactivated_realm_deletion_days:integer | nullPresent ifrealmis present infetch_event_types.The maximum permitted number of days before full data deletion
(users, channels, messages, etc.) of a deactivated organization.
Ifnull, then a deactivated organization's data can be
retained indefinitely.Changes: New in Zulip 10.0 (feature level 332).
- server_presence_ping_interval_seconds:integerPresent ifrealmis present infetch_event_types.For clients implementing thepresencesystem,
the time interval the client should use for sending presence requests
to the server (and thus receive presence updates from the server).It is important for presence implementations to use both this andserver_presence_offline_threshold_secondscorrectly, so that a Zulip
server can change these values to manage the trade-off between load and
freshness of presence data.Changes: New in Zulip 7.0 (feature level 164). Clients should use 60
for older Zulip servers, since that's the value that was hardcoded in the
Zulip mobile apps prior to this parameter being introduced.
- server_presence_offline_threshold_seconds:integerPresent ifrealmis present infetch_event_types.How old a presence timestamp for a given user can be before the user
should be displayed as offline by clients displaying Zulip presence
data. See the relatedserver_presence_ping_interval_secondsfor details.Changes: New in Zulip 7.0 (feature level 164). Clients should use 140
for older Zulip servers, since that's the value that was hardcoded in the
Zulip client apps prior to this parameter being introduced.
- server_typing_started_expiry_period_milliseconds:integerPresent ifrealmis present infetch_event_types.For clients implementingtyping notificationsprotocol, the time interval in milliseconds that the client should wait
for additionaltyping startevents from
the server before removing an active typing indicator.Changes: New in Zulip 8.0 (feature level 204). Clients should use 15000
for older Zulip servers, since that's the value that was hardcoded in the
Zulip apps prior to this parameter being introduced.
- server_typing_stopped_wait_period_milliseconds:integerPresent ifrealmis present infetch_event_types.For clients implementingtyping notificationsprotocol, the time interval in milliseconds that the client should wait
when a user stops interacting with the compose UI before sending a stop
notification to the server.Changes: New in Zulip 8.0 (feature level 204). Clients should use 5000
for older Zulip servers, since that's the value that was hardcoded in the
Zulip apps prior to this parameter being introduced.
- server_typing_started_wait_period_milliseconds:integerPresent ifrealmis present infetch_event_types.For clients implementingtyping notificationsprotocol, the time interval in milliseconds that the client should use
to send regular start notifications to the server to indicate that the
user is still actively interacting with the compose UI.Changes: New in Zulip 8.0 (feature level 204). Clients should use 10000
for older Zulip servers, since that's the value that was hardcoded in the
Zulip apps prior to this parameter being introduced.
- scheduled_messages:(object)[]Present ifscheduled_messagesis present infetch_event_types.An array of all undelivered scheduled messages by the user.Changes: New in Zulip 7.0 (feature level 179).scheduled_message_id:integerThe unique ID of the scheduled message, which can be used to
modify or delete the scheduled message.This is different from the unique ID that the message will have
after it is sent.type:stringThe type of the scheduled message. Either"channel_name"or"private".to:integer | (integer)[]The scheduled message's tentative target audience.For channel messages, it will be the unique ID of the target
channel. For direct messages, it will be an array with the
target users' IDs.message_topic:stringOnly present iftypeis"channel_name".The message_topic for the channel message.content:stringThe content/body of the scheduled message, inZulip-flavored Markdownformat.SeeMarkdown message formattingfor details on Zulip's HTML format.rendered_content:stringThe content/body of the scheduled message rendered in HTML.scheduled_delivery_timestamp:integerThe UNIX timestamp for when the message will be sent
by the server, in UTC seconds.failed:booleanWhether the server has tried to send the scheduled message
and it failed to successfully send.Clients that support unscheduling and editing scheduled messages
should display scheduled messages with"failed": truewith an
indicator that the server failed to send the message at the
scheduled time, so that the user is aware of the failure and can
get the content of the scheduled message.Changes: New in Zulip 7.0 (feature level 181).
- reminders:(object)[]Present ifremindersis present infetch_event_types.An array of all undelivered reminders scheduled by the user.Changes: New in Zulip 11.0 (feature level 399).scheduled_message_id:integerThe unique ID of the scheduled message, which can be used to
modify or delete the scheduled message.This is different from the unique ID that the message will have
after it is sent.type:stringThe type of the scheduled message. Either"channel_name"or"private".to:integer | (integer)[]The scheduled message's tentative target audience.For channel messages, it will be the unique ID of the target
channel. For direct messages, it will be an array with the
target users' IDs.message_topic:stringOnly present iftypeis"channel_name".The message_topic for the channel message.content:stringThe content/body of the scheduled message, inZulip-flavored Markdownformat.SeeMarkdown message formattingfor details on Zulip's HTML format.rendered_content:stringThe content/body of the scheduled message rendered in HTML.scheduled_delivery_timestamp:integerThe UNIX timestamp for when the message will be sent
by the server, in UTC seconds.failed:booleanWhether the server has tried to send the scheduled message
and it failed to successfully send.Clients that support unscheduling and editing scheduled messages
should display scheduled messages with"failed": truewith an
indicator that the server failed to send the message at the
scheduled time, so that the user is aware of the failure and can
get the content of the scheduled message.Changes: New in Zulip 7.0 (feature level 181).
- muted_topics:((string | integer)[])[]Present ifmuted_topicsis present infetch_event_types.Array of tuples, where each tuple describes a muted message_topic.
The first element of the tuple is the channel name in which the message_topic
has to be muted, the second element is the message_topic name to be muted
and the third element is an integer UNIX timestamp representing
when the message_topic was muted.Changes: Deprecated in Zulip 6.0 (feature level 134). Starting
with this version,muted_topicswill only be present in the
response if theuser_topicobject, which generalizes and replaces
this field, is not explicitly requested viafetch_event_types.Before Zulip 3.0 (feature level 1), themuted_topicsarray objects were 2-item tuples and did not include the timestamp
information for when the message_topic was muted.
- muted_users:(object)[]Present ifmuted_usersis present infetch_event_types.A list of dictionaries where each dictionary describes
amuted user.Changes: New in Zulip 4.0 (feature level 48).id:integerThe ID of the muted user.timestamp:integerAn integer UNIX timestamp representing when the user was muted.
- presences:objectPresent ifpresenceis present infetch_event_types.A dictionary where each entry describes the presence details of a
user in the Zulip organization.The format of the entry (modern or legacy) depends on the value ofslim_presence.Users who have been offline for multiple weeks may not appear in this object.Will be one of these two formats (modern or legacy) for user
    presence data:{user_id}:objectPresence data (modern format) for the user with
the specified ID.active_timestamp:integerThe UNIX timestamp of the last time a client connected
to Zulip reported that the user was actually present
(e.g. via focusing a browser window or interacting
with a computer running the desktop app).Clients should display users with a currentactive_timestampas fully present.idle_timestamp:integerThe UNIX timestamp of the last time the user had a
client connected to Zulip, including idle clients
where the user hasn't interacted with the system
recently.The Zulip server has no way of distinguishing whether
an idle web app user is at their computer, but hasn't
interacted with the Zulip tab recently, or simply left
their desktop computer on when they left.Thus, clients should display users with a currentidle_timestampbut no currentactive_timestampas
potentially present.{user_email}:objectPresence data (legacy format) for the user with
the specified Zulip API email.{client_name}or"aggregated":objectObject containing the details of the user's
presence.Changes: Starting with Zulip 7.0 (feature level 178), this will always
contain two keys,"website"and"aggregated", with identical data. The
server no longer stores which client submitted presence updates.Previously, the{client_name}keys for these objects were the names of the
different clients where the user was logged in, for examplewebsiteorZulipDesktop.client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this will
always be"website"as the server no longer stores which client
submitted presence data.status:stringThe status of the user on this client. Will be either"idle"or"active".timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Not present in objects with the"aggregated"key.Changes: Starting with Zulip 7.0 (feature level 178), alwaysfalsewhen present as the server no longer stores which client
submitted presence data.
- presence_last_update_id:integerPresent ifpresenceis present infetch_event_types.Provides thelast_update_idvalue of the latest presence data fetched by
the server and included in the response inpresences. This can be used
as the value of thepresence_last_update_idparameter when polling
for presence data at the/users/me/presenceendpoint
to tell the server to only fetch the relevant newer data in order to skip
redundant already-known presence information.Changes: New in Zulip 9.0 (feature level 263).
- server_timestamp:numberPresent ifpresenceis present infetch_event_types.The time when the server fetched thepresencesdata included in the response.
Matches the similar field in presence
responses.Changes: New in Zulip 5.0 (feature level 70).
- realm_domains:(object)[]Present ifrealm_domainsis present infetch_event_types.An array of dictionaries where each dictionary describes a domain within
which users can join the organization without and invitation.domain:stringThe new allowed domain.allow_subdomains:booleanWhether subdomains are allowed for this domain.
- realm_emoji:objectPresent ifrealm_emojiis present infetch_event_types.A dictionary of objects where each object describes a custom
emoji that has been uploaded in this Zulip organization.{emoji_id}:objectObject containing details about the emoji with
the specified ID. It has the following properties:id:stringThe ID for this emoji, same as the object's key.name:stringThe user-friendly name for this emoji. Users in the organization
can use this emoji by writing this name between colons (:name :).source_url:stringThe path relative to the organization's URL where the
emoji's image can be found.still_url:string | nullOnly non-null when the emoji's image is animated.The path relative to the organization's URL where a still
(not animated) version of the emoji can be found. (This is
currently always the first frame of the animation).This is useful for clients to display the emoji in contexts
where continuously animating it would be a bad user experience
(E.g. because it would be distracting).Changes: New in Zulip 5.0 (added as optional field in
feature level 97 and then made mandatory, but nullable, in
feature level 113).deactivated:booleanWhether the emoji has been deactivated or not.author_id:integer | nullThe user ID of the user who uploaded the custom emoji.
Will benullif the uploader is unknown.Changes: New in Zulip 3.0 (feature level 7). Previously
was accessible via anauthorobject with anidfield.
- realm_linkifiers:(object)[]Present ifrealm_linkifiersis present infetch_event_types.An ordered array of objects where each object describes a singlelinkifier.The order of the array reflects the order that each
linkifier should be processed when linkifying messages
and topics. By default, new linkifiers are ordered
last. This order can be modified withPATCH
/realm/linkifiers.Clients will receive an empty array unless the event queue is
registered with the client capability{"linkifier_url_template": true}.
Seeclient_capabilitiesparameter for how this can be specified.Changes: Before Zulip 7.0 (feature level 176), thelinkifier_url_templateclient capability was not required. The
requirement was added because linkifiers were updated to contain
a URL template instead of a URL format string, which was a not
backwards-compatible change.New in Zulip 4.0 (feature level 54). Clients can access this data for
servers on earlier feature levels via the legacyrealm_filtersproperty.pattern:stringThePython regular expressionpattern which represents the pattern that should be linkified on matching.url_template:stringTheRFC 6570compliant URL
template with which the pattern matching string should be linkified.Changes: New in Zulip 7.0 (feature level 176). This replacedurl_format,
which contained a URL format string.id:integerThe ID of the linkifier.
- realm_filters:((integer | string)[])[]Legacy property forlinkifiers.
Present ifrealm_filtersis present infetch_event_types.When present, this is always an empty array.Changes: Prior to Zulip 7.0 (feature level 176), this was
an array of tuples, where each tuple described a linkifier. The first
element of the tuple was a string regex pattern which represented the
pattern to be linkified on matching, for example"#(?P<id>[123])".
The second element was a URL format string that the pattern should be
linkified with. A URL format string for the above example would be"https://realm.com/my_realm_filter/%(id)s". And the third element
was the ID of the realm filter.Deprecatedin Zulip 4.0 (feature level 54), replaced by therealm_linkifierskey.
- realm_playgrounds:(object)[]Present ifrealm_playgroundsis present infetch_event_types.An array of dictionaries where each dictionary describes acode playgroundconfigured for this Zulip organization.Changes: New in Zulip 4.0 (feature level 49).id:integerThe unique ID for the realm playground.name:stringThe user-visible display name of the playground. Clients
should display this in UI for picking which playground to
open a code block in, to differentiate between multiple
configured playground options for a given pygments
language.Changes: New in Zulip 4.0 (feature level 49).pygments_language:stringThe name of the Pygments language lexer for that
programming language.url_template:stringTheRFC 6570compliant URL template for the playground. The template contains
exactly one variable namedcode, which determines how the
extracted code should be substituted in the playground URL.Changes: New in Zulip 8.0 (feature level 196). This replaced theurl_prefixparameter, which was used to construct URLs by just
concatenating url_prefix and code.
- realm_user_groups:(object)[]Present ifrealm_user_groupsis present infetch_event_types.An array of dictionaries where each dictionary describes auser groupin the Zulip organization.Deactivated groups will only be included ifinclude_deactivated_groupsclient capability is set totrue.Changes: Prior to Zulip 10.0 (feature level 294), deactivated
groups were included for all the clients.name:stringThe name of the user group.date_created:integer | nullThe UNIX timestamp for when the user group was created, in UTC seconds.Anullvalue means the user group has no recorded date, which is often
because the user group is very old, or because it was created via a data
import tool ormanagement command.Changes: New in Zulip 10.0 (feature level 292).creator_id:integer | nullThe ID of the user who created this user group.Anullvalue means the user group has no recorded creator, which is often
because the user group is very old, or because it was created via a data
import tool ormanagement command.Changes: New in Zulip 10.0 (feature level 292).description:stringThe description of the user group.members:(integer)[]Array containing the ID of the users who are
members of this user group.Changes: Prior to Zulip 10.0 (feature level 303), this
list also included deactivated users who were members of
the user group before being deactivated.direct_subgroup_ids:(integer)[]Array containing the ID of the direct_subgroups of
this user group.Changes: New in Zulip 6.0 (feature level 131).
Introduced in feature level 127 assubgroups, but
clients can ignore older events as this feature level
predates subgroups being fully implemented.id:integerThe ID of the user group.is_system_group:booleanWhether the user group is a system group which cannot be
directly modified by users.Changes: New in Zulip 5.0 (feature level 93).can_add_members_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to add members to this user group.Changes: New in Zulip 10.0 (feature level 305). Previously, this
permission was controlled by thecan_manage_groupsetting.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_join_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to join this user group.Changes: New in Zulip 10.0 (feature level 301).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_leave_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to leave this user group.Changes: New in Zulip 10.0 (feature level 308).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_manage_group:integer | objectAgroup-setting valuedefining the set of users who
have permission tomanage this user group.Changes: New in Zulip 10.0 (feature level 283).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_mention_group:integer | objectAgroup-setting valuedefining the set of users who
have permission tomention this user group.Changes: Before Zulip 9.0 (feature level 258), this setting was
always the integer form of agroup-setting value.Before Zulip 8.0 (feature level 198), this setting was namedcan_mention_group_id.New in Zulip 8.0 (feature level 191). Previously, groups could be
mentioned only if they were notsystem groups.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_remove_members_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to remove members from this user group.Changes: New in Zulip 10.0 (feature level 324). Previously, this
permission was controlled by thecan_manage_groupsetting.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.deactivated:booleanWhether the user group is deactivated. Deactivated groups
cannot be used as a subgroup of another group or used for
any other purpose.Changes: New in Zulip 10.0 (feature level 290).
- realm_bots:(object)[]Present ifrealm_botis present infetch_event_types.An array of dictionaries where each dictionary describes a bot that the
current user can administer. If the current user is an organization
administrator, this will include all bots in the organization. Otherwise,
it will only include bots owned by the user (either because the user created
the bot or an administrator transferred the bot's ownership to the user).Changes: Removedavatar_url,bot_type,email,full_name,is_activeandowner_idfields from the dictionary in Zulip 12.0 (feature level 474).
Clients can get all these data from the corresponding user object.Removedapi_keyfield from the dictionary in Zulip 12.0 (feature level 474).
Clients now useGET /bots/{bot_id}/api_keyto get api key for the bot.user_id:integerThe user ID of the bot.default_sending_stream:string | nullThe default sending channel of the bot. Ifnull, the bot doesn't
have a default sending channel.default_events_register_stream:string | nullThe default channel for which the bot receives events/register data.
Ifnull, the bot doesn't have such a default channel.default_all_public_streams:booleanWhether the bot can send messages to all channels by default.services:(object | object)[]An array containing extra configuration fields only relevant for
outgoing webhook bots and embedded bots. This is always a single-element
array.We consider this part of the Zulip API to be unstable; it is used only
for UI elements for administering bots and is likely to change.When the bot is an outgoing webhook.base_url:stringThe URL the outgoing webhook is configured to post to.token:stringA unique token that the third-party service can use to confirm
that the request is indeed coming from Zulip.interface:integerAn integer indicating what format requests are posted in:1 = Zulip's native outgoing webhook format.2 = Emulate the Slack outgoing webhook format.When the bot is an embedded bot.service_name:stringThe name of the bot.config_data:objectA dictionary of string key/value pairs, which describe the configuration
for the bot. These are usually details like API keys, and are unique to
the integration/bot. Can be an empty dictionary.{config_key}:stringDescription/value of the configuration data key.
- realm_embedded_bots:(object)[]Present ifrealm_embedded_botsis present infetch_event_types.An array of dictionaries where each dictionary describes an type of embedded
bot that is available to be configured on this Zulip server.Clients only need these data if they contain UI for creating or administering bots.name:stringThe name of the bot.config:objectA dictionary of string key/value pairs, which describe the configuration
for the bot. These are usually details like API keys, and are unique to
the integration/bot. Can be an empty dictionary.{config_key}:stringDescription/value of the configuration data key.
- realm_incoming_webhook_bots:(object)[]Present ifrealm_incoming_webhook_botsis present infetch_event_types.An array of dictionaries where each dictionary describes a type of incoming webhook
integration that is available to be configured on this Zulip server.Clients only need these data if they contain UI for creating or administering bots.name:stringA machine-readable unique name identifying the integration, all-lower-case without
spaces.display_name:stringA human-readable display name identifying the integration that this bot implements,
intended to be used in menus for selecting which integration to create.Changes: New in Zulip 8.0 (feature level 207).all_event_types:(string)[]For incoming webhook integrations that support the Zulip server filtering incoming
events, the list of event types supported by it.A null value will be present if this incoming webhook integration doesn't support
such filtering.Changes: New in Zulip 8.0 (feature level 207).config_options:(object)[]An array of configuration options that can be set when creating
a bot user for this incoming webhook integration.This is an unstable API. Please discuss in chat.zulip.org before
using it.Changes: As of Zulip 11.0 (feature level 403), this
object is reserved for integration-specific configuration options
that can be set when creating a bot user. Previously, this object
also included optional webhook URL parameters, which are now
specified in theurl_optionsobject.Before Zulip 10.0 (feature level 318), this field was namedconfig,
and was reserved for configuration data key-value pairs.key:stringA key for the configuration option.label:stringA human-readable label of the configuration option.validator:stringThe name of the validator function for the configuration
option.url_options:(object)[]An array of optional URL parameter options for the incoming webhook
integration. In the web app, these are used whengenerating a URL for an integration.This is an unstable API expected to be used only by the Zulip web
app. Please discuss in chat.zulip.org before using it.Changes: New in Zulip 11.0 (feature level 403). Previously,
these optional URL parameter options were included in theconfig_optionsobject.key:stringThe parameter variable to encode the users input for this
option in the integrations webhook URL.label:stringA human-readable label of the url option.validator:stringThe name of the validator function for the configuration
option.
- recent_private_conversations:(object)[]Present ifrecent_private_conversationsis present infetch_event_types.An array of dictionaries containing data on all direct message and group direct message
conversations that the user has received (or sent) messages in, organized by
conversation. This data set is designed to support UI elements such as the
"Direct messages" widget in the web application showing recent direct message
conversations that the user has participated in."Recent" is defined as the server's discretion; the original implementation
interpreted that as "the 1000 most recent direct messages the user received".max_message_id:integerThe highest message ID of the conversation, intended to support sorting
the conversations by recency.user_ids:(integer)[]The list of users other than the current user in the direct message
conversation. This will be an empty list for direct messages sent to
oneself.
- navigation_views:(object)[]Present ifnavigation_viewsis present infetch_event_types.
An array of dictionaries containing data on all of the current user's
navigation views.Changes: New in Zulip 11.0 (feature level 390).fragment:stringA unique identifier for the view, used to determine navigation
behavior when clicked.Clients should use this value to navigate to the corresponding URL hash.is_pinned:booleanDetermines whether the view appears directly in the sidebar or
is hidden in the "More Views" menu.true- Pinned and visible in the sidebar.false- Hidden and accessible via the "More Views" menu.name:string | nullThe user-facing name for custom navigation views. Omit this
field for built-in views.
- saved_snippets:(object)[]Present ifsaved_snippetsis present infetch_event_types.An array of dictionaries containing data on all of the current user's
saved snippets.Changes: New in Zulip 10.0 (feature level 297).id:integerThe unique ID of the saved snippet.title:stringThe title of the saved snippet.content:stringThe content of the saved snippet inZulip-flavored Markdownformat.Clients should insert this content into a message when using
a saved snippet.date_created:integerThe UNIX timestamp for when the saved snippet was created, in
UTC seconds.
- subscriptions:(object)[]Present ifsubscriptionis present infetch_event_types.A array of dictionaries where each dictionary describes the properties
of a channel the user is subscribed to (as well as that user's
personal per-channel settings).Changes: Removedemail_addressfield from the dictionary
in Zulip 8.0 (feature level 226).Removedrolefield from the dictionary
in Zulip 6.0 (feature level 133).stream_id:integerThe unique ID of a channel.name:stringThe name of a channel.description:stringThedescriptionof the channel inZulip-flavored Markdownformat,
intended to be used to prepopulate UI for editing a channel's
description.SeeMarkdown message formattingfor details on Zulip's HTML format.See alsorendered_description.rendered_description:stringThedescriptionof the channel rendered as HTML, intended to
be used when displaying the channel description in a UI.One should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax
work correctly. And any client-side security logic for
user-generated message content should be applied when displaying
this HTML as though it were the body of a Zulip message.See alsodescription.date_created:integerThe UNIX timestamp for when the channel was created, in UTC seconds.Changes: New in Zulip 4.0 (feature level 30).creator_id:integer | nullThe ID of the user who created this channel.Anullvalue means the channel has no recorded creator, which is often
because the channel is very old, was created during realm creation or
because it was created via a data import tool ormanagement command.Changes: New in Zulip 9.0 (feature level 254).invite_only:booleanSpecifies whether the channel is private or not.
Only people who have been invited can access a private channel.subscribers:(integer)[]A list of user IDs of users who are also subscribed
to a given channel. Included only ifinclude_subscribersistrue.partial_subscribers:(integer)[]Ifinclude_subscribers="partial"was requested, the server may, at its discretion, send apartial_subscriberslist rather than asubscriberslist
for channels with a large number of subscribers.Thepartial_subscriberslist contains an arbitrary
subset of the channel's subscribers that is guaranteed
to include all bot user subscribers as well as all
users who have been active in the last 14 days, but
otherwise can be chosen arbitrarily by the server.Changes: New in Zulip 11.0 (feature level 412).desktop_notifications:boolean | nullA boolean specifying whether desktop notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_desktop_notifications, for
this channel.email_notifications:boolean | nullA boolean specifying whether email notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_email_notifications, for
this channel.wildcard_mentions_notify:boolean | nullA boolean specifying whether wildcard mentions
trigger notifications as though they were personal
mentions in this channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting, wildcard_mentions_notify, for
this channel.push_notifications:boolean | nullA boolean specifying whether push notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_push_notifications, for
this channel.audible_notifications:boolean | nullA boolean specifying whether audible notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_audible_notifications, for
this channel.pin_to_top:booleanA boolean specifying whether the given channel has been pinned
to the top.is_muted:booleanWhether the user has muted the channel. Muted channels do
not count towards your total unread count and do not show
up in theCombined feedview (previously known asAll messages).Changes: Prior to Zulip 2.1.0, this feature was
represented by the more confusingly namedin_home_view(with the
opposite value,in_home_view=!is_muted).in_home_view:booleanLegacy property for if the given channel is muted, with inverted meaning.Changes: Deprecated in Zulip 2.1.0. Clients should useis_mutedwhere available.is_announcement_only:booleanWhether only organization administrators can post to the channel.Changes: Deprecated in Zulip 3.0 (feature level 1). Clients
should usestream_post_policyinstead.is_web_public:booleanWhether the channel has been configured to allow unauthenticated
access to its message history from the web.color:stringThe user's personal color for the channel.stream_post_policy:integerA deprecated representation of a superset of the users who
have permission to post messages to the channel available
for backwards-compatibility. Clients should usecan_send_message_groupinstead.It is an enum with the following possible values, corresponding
to roles/system groups:1 = Any user can post.2 = Only administrators can post.3 = Onlyfull memberscan post.4 = Only moderators can post.Changes: Deprecated in Zulip 10.0 (feature level 333) and
replaced bycan_send_message_group, which supports finer
resolution of configurations, resulting in this property being
inaccurate following that transition.New in Zulip 3.0 (feature level 1), replacing the previousis_announcement_onlyboolean.message_retention_days:integer | nullNumber of days that messages sent to this channel will be stored
before being automatically deleted by themessage retention
policy. There are two special values:null, the default, means the channel will inherit the organization
  level setting.-1encodes retaining messages in this channel forever.Changes: New in Zulip 3.0 (feature level 17).history_public_to_subscribers:booleanWhether the history of the channel is public to its subscribers.Currently always true for public channels (i.e."invite_only": falseimplies"history_public_to_subscribers": true), but clients should not make that
assumption, as we may change that behavior in the future.first_message_id:integer | nullThe ID of the first message in the channel.Intended to help clients determine whether they need to display
UI like the "show all topics" widget that would suggest the channel
has older history that can be accessed.Isnullfor channels with no message history.folder_id:integer | nullThe ID of the folder to which the channel belongs.Isnullif channel does not belong to any folder.Changes: New in Zulip 11.0 (feature level 389).topics_policy:stringWhethernamed topicsand the empty
message_topic (i.e.,"general chat" message_topic)
are enabled in this channel."inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty message_topic in this
  channel."allow_empty_topic": Messages can be sent to both named topics and
  the empty message_topic in this channel."disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty message_topic is disabled."empty_topic_only": Messages can be sent to the empty message_topic in this
  channel, but named topics are disabled. See"general chat"
  channels.The"empty_topic_only"policy can only be set if all existing messages
in the channel are already in the empty message_topic.When creating a new channel, if thetopics_policyis not specified, the"inherit"option will be set.Changes: In Zulip 11.0 (feature level 404), the"empty_topic_only"option was added.New in Zulip 11.0 (feature level 392).is_recently_active:booleanWhether the channel has recent message activity. Clients should use this to implementhiding inactive channels.Changes: New in Zulip 10.0 (feature level 323). Previously, clients implemented the
demote_inactive_streams from local message history, resulting in a choppy loading
experience.stream_weekly_traffic:integer | nullThe average number of messages sent to the channel per week, as
estimated based on recent weeks, rounded to the nearest integer.Ifnull, the channel was recently created and there is
insufficient data to estimate the average traffic.can_add_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to add subscribers to this channel.Users who can administer the channel or have similar realm-level
permissions can add subscribers to a public channel regardless
of the value of this setting.Users in this group need not be subscribed to a private channel to
add subscribers to it.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 342). Previously, there was no
channel-level setting for this permission.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_remove_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to remove subscribers from this channel.Organization administrators can unsubscribe others from a channel as though
they were in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349), channel administrators
could not unsubscribe other users if they were not an organization
administrator or part ofcan_remove_subscribers_group. Realm administrators
were not allowed to unsubscribe other users from a private channel if they
were not subscribed to that channel.Prior to Zulip 10.0 (feature level 320), this value was always the integer
ID of a system group.Before Zulip 8.0 (feature level 197), thecan_remove_subscribers_groupsetting was namedcan_remove_subscribers_group_id.New in Zulip 6.0 (feature level 142).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_administer_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to administer this channel.Organization administrators can administer every channel as though they were
in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349) a user needed tohave content accessto a channel in
order to modify it. The exception to this rule was that organization
administrators can edit channel names and descriptions without
having full access to the channel.New in Zulip 10.0 (feature level 325). Prior to this
change, the permission to administer channels was limited to realm
administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_delete_any_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete any message in the channel.Note that a user musthave content accessto a
channel in order to delete any message in the channel.Users present in the organization-levelcan_delete_any_message_groupsetting can always delete any message in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users incan_delete_any_message_groupwere able
delete any message in the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_delete_own_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete the messages that they have sent in the channel.Note that a user musthave content accessto a
channel in order to delete their own message in the channel.Users with permission to delete any message in the channel
and users present in the organization-levelcan_delete_own_message_groupsetting
can always delete their own messages in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users in the organization-levelcan_delete_any_message_groupandcan_delete_own_message_groupsettings were able delete their own messages in
the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_move_messages_out_of_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages out of this channel.Note that a user musthave content accessto a
channel in order to move messages out of the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_channels_groupsetting can always move messages
out of the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_channels_groupwere able
move messages between channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_move_messages_within_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages within this channel.Note that a user musthave content accessto a
channel in order to move messages within the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_topics_groupsetting can always move messages
within the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_topics_groupwere able
move messages between topics of a channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_send_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to post in this channel.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Note that using this permission to send a message to a new message_topic requires
also having permission to create new topics in the channel.Changes: New in Zulip 10.0 (feature level 333). Previouslystream_post_policyfield used to control the permission to
post in the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_subscribe_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to subscribe themselves to this channel.Everyone, excluding guests, can subscribe to any public channel
irrespective of this setting.Users in this group can subscribe to a private channel as well.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 357).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_resolve_topics_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to resolve topics in the channel.Users who have similar realm-level permissions can resolve topics
in a channel regardless of the value of this setting.Changes: New in Zulip 11.0 (feature level 402).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_create_topic_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to create a new message_topic in this channel.Note that using this permission requires also having permission to
send messages in the channel.Note that this must be therole:everyonesystem groupforprivate channels with protected history.Changes: New in Zulip 12.0 (feature level 441). Previously,
if you could send messages in a channel, you could create topics in
the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.is_archived:booleanA boolean indicating whether the channel isarchived.Changes: New in Zulip 10.0 (feature level 315).
Previously, subscriptions only included active
channels. Note that some endpoints will never return archived
channels unless the client declares explicit support for
them via thearchived_channelsclient capability.subscriber_count:numberThe total number of non-deactivated users (including bots) who
are subscribed to the channel. Clients are responsible for updating
this value usingpeer_addandpeer_removeevents.The server's internals cannot guarantee this value is correctly
synced withpeer_addandpeer_removeevents for the channel. As
a result, if a (rare) race occurs between a change in the channel's
subscribers and fetching this value, it is possible for a client
that is correctly following the events protocol to end up with a
permanently off-by-one error in the channel's subscriber count.Clients are recommended to fetch full subscriber data for a channel
in contexts where it is important to avoid this risk. The official
web application, for example, uses this field primarily while
waiting to fetch a given channel's full subscriber list from the
server.Changes: New in Zulip 11.0 (feature level 394).
- unsubscribed:(object)[]Present ifsubscriptionis present infetch_event_types.A array of dictionaries where each dictionary describes one of the
channels the user has unsubscribed from but was previously subscribed to
along with the subscription details.Unlikenever_subscribed, the user might have messages in their personal
message history that were sent to these channels.Changes: Prior to Zulip 10.0 (feature level 349), if a user was
incan_administer_channel_groupof a channel that they had
unsubscribed from, but not an organization administrator, the channel
in question would not be part of this array.Removedemail_addressfield from the dictionary
in Zulip 8.0 (feature level 226).Removedrolefield from the dictionary
in Zulip 6.0 (feature level 133).stream_id:integerThe unique ID of a channel.name:stringThe name of a channel.description:stringThedescriptionof the channel inZulip-flavored Markdownformat,
intended to be used to prepopulate UI for editing a channel's
description.SeeMarkdown message formattingfor details on Zulip's HTML format.See alsorendered_description.rendered_description:stringThedescriptionof the channel rendered as HTML, intended to
be used when displaying the channel description in a UI.One should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax
work correctly. And any client-side security logic for
user-generated message content should be applied when displaying
this HTML as though it were the body of a Zulip message.See alsodescription.date_created:integerThe UNIX timestamp for when the channel was created, in UTC seconds.Changes: New in Zulip 4.0 (feature level 30).creator_id:integer | nullThe ID of the user who created this channel.Anullvalue means the channel has no recorded creator, which is often
because the channel is very old, was created during realm creation or
because it was created via a data import tool ormanagement command.Changes: New in Zulip 9.0 (feature level 254).invite_only:booleanSpecifies whether the channel is private or not.
Only people who have been invited can access a private channel.subscribers:(integer)[]A list of user IDs of users who are also subscribed
to a given channel. Included only ifinclude_subscribersistrue.partial_subscribers:(integer)[]Ifinclude_subscribers="partial"was requested, the server may, at its discretion, send apartial_subscriberslist rather than asubscriberslist
for channels with a large number of subscribers.Thepartial_subscriberslist contains an arbitrary
subset of the channel's subscribers that is guaranteed
to include all bot user subscribers as well as all
users who have been active in the last 14 days, but
otherwise can be chosen arbitrarily by the server.Changes: New in Zulip 11.0 (feature level 412).desktop_notifications:boolean | nullA boolean specifying whether desktop notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_desktop_notifications, for
this channel.email_notifications:boolean | nullA boolean specifying whether email notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_email_notifications, for
this channel.wildcard_mentions_notify:boolean | nullA boolean specifying whether wildcard mentions
trigger notifications as though they were personal
mentions in this channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting, wildcard_mentions_notify, for
this channel.push_notifications:boolean | nullA boolean specifying whether push notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_push_notifications, for
this channel.audible_notifications:boolean | nullA boolean specifying whether audible notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_audible_notifications, for
this channel.pin_to_top:booleanA boolean specifying whether the given channel has been pinned
to the top.is_muted:booleanWhether the user has muted the channel. Muted channels do
not count towards your total unread count and do not show
up in theCombined feedview (previously known asAll messages).Changes: Prior to Zulip 2.1.0, this feature was
represented by the more confusingly namedin_home_view(with the
opposite value,in_home_view=!is_muted).in_home_view:booleanLegacy property for if the given channel is muted, with inverted meaning.Changes: Deprecated in Zulip 2.1.0. Clients should useis_mutedwhere available.is_announcement_only:booleanWhether only organization administrators can post to the channel.Changes: Deprecated in Zulip 3.0 (feature level 1). Clients
should usestream_post_policyinstead.is_web_public:booleanWhether the channel has been configured to allow unauthenticated
access to its message history from the web.color:stringThe user's personal color for the channel.stream_post_policy:integerA deprecated representation of a superset of the users who
have permission to post messages to the channel available
for backwards-compatibility. Clients should usecan_send_message_groupinstead.It is an enum with the following possible values, corresponding
to roles/system groups:1 = Any user can post.2 = Only administrators can post.3 = Onlyfull memberscan post.4 = Only moderators can post.Changes: Deprecated in Zulip 10.0 (feature level 333) and
replaced bycan_send_message_group, which supports finer
resolution of configurations, resulting in this property being
inaccurate following that transition.New in Zulip 3.0 (feature level 1), replacing the previousis_announcement_onlyboolean.message_retention_days:integer | nullNumber of days that messages sent to this channel will be stored
before being automatically deleted by themessage retention
policy. There are two special values:null, the default, means the channel will inherit the organization
  level setting.-1encodes retaining messages in this channel forever.Changes: New in Zulip 3.0 (feature level 17).history_public_to_subscribers:booleanWhether the history of the channel is public to its subscribers.Currently always true for public channels (i.e."invite_only": falseimplies"history_public_to_subscribers": true), but clients should not make that
assumption, as we may change that behavior in the future.first_message_id:integer | nullThe ID of the first message in the channel.Intended to help clients determine whether they need to display
UI like the "show all topics" widget that would suggest the channel
has older history that can be accessed.Isnullfor channels with no message history.folder_id:integer | nullThe ID of the folder to which the channel belongs.Isnullif channel does not belong to any folder.Changes: New in Zulip 11.0 (feature level 389).topics_policy:stringWhethernamed topicsand the empty
message_topic (i.e.,"general chat" message_topic)
are enabled in this channel."inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty message_topic in this
  channel."allow_empty_topic": Messages can be sent to both named topics and
  the empty message_topic in this channel."disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty message_topic is disabled."empty_topic_only": Messages can be sent to the empty message_topic in this
  channel, but named topics are disabled. See"general chat"
  channels.The"empty_topic_only"policy can only be set if all existing messages
in the channel are already in the empty message_topic.When creating a new channel, if thetopics_policyis not specified, the"inherit"option will be set.Changes: In Zulip 11.0 (feature level 404), the"empty_topic_only"option was added.New in Zulip 11.0 (feature level 392).is_recently_active:booleanWhether the channel has recent message activity. Clients should use this to implementhiding inactive channels.Changes: New in Zulip 10.0 (feature level 323). Previously, clients implemented the
demote_inactive_streams from local message history, resulting in a choppy loading
experience.stream_weekly_traffic:integer | nullThe average number of messages sent to the channel per week, as
estimated based on recent weeks, rounded to the nearest integer.Ifnull, the channel was recently created and there is
insufficient data to estimate the average traffic.can_add_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to add subscribers to this channel.Users who can administer the channel or have similar realm-level
permissions can add subscribers to a public channel regardless
of the value of this setting.Users in this group need not be subscribed to a private channel to
add subscribers to it.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 342). Previously, there was no
channel-level setting for this permission.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_remove_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to remove subscribers from this channel.Organization administrators can unsubscribe others from a channel as though
they were in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349), channel administrators
could not unsubscribe other users if they were not an organization
administrator or part ofcan_remove_subscribers_group. Realm administrators
were not allowed to unsubscribe other users from a private channel if they
were not subscribed to that channel.Prior to Zulip 10.0 (feature level 320), this value was always the integer
ID of a system group.Before Zulip 8.0 (feature level 197), thecan_remove_subscribers_groupsetting was namedcan_remove_subscribers_group_id.New in Zulip 6.0 (feature level 142).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_administer_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to administer this channel.Organization administrators can administer every channel as though they were
in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349) a user needed tohave content accessto a channel in
order to modify it. The exception to this rule was that organization
administrators can edit channel names and descriptions without
having full access to the channel.New in Zulip 10.0 (feature level 325). Prior to this
change, the permission to administer channels was limited to realm
administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_delete_any_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete any message in the channel.Note that a user musthave content accessto a
channel in order to delete any message in the channel.Users present in the organization-levelcan_delete_any_message_groupsetting can always delete any message in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users incan_delete_any_message_groupwere able
delete any message in the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_delete_own_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete the messages that they have sent in the channel.Note that a user musthave content accessto a
channel in order to delete their own message in the channel.Users with permission to delete any message in the channel
and users present in the organization-levelcan_delete_own_message_groupsetting
can always delete their own messages in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users in the organization-levelcan_delete_any_message_groupandcan_delete_own_message_groupsettings were able delete their own messages in
the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_move_messages_out_of_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages out of this channel.Note that a user musthave content accessto a
channel in order to move messages out of the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_channels_groupsetting can always move messages
out of the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_channels_groupwere able
move messages between channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_move_messages_within_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages within this channel.Note that a user musthave content accessto a
channel in order to move messages within the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_topics_groupsetting can always move messages
within the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_topics_groupwere able
move messages between topics of a channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_send_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to post in this channel.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Note that using this permission to send a message to a new message_topic requires
also having permission to create new topics in the channel.Changes: New in Zulip 10.0 (feature level 333). Previouslystream_post_policyfield used to control the permission to
post in the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_subscribe_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to subscribe themselves to this channel.Everyone, excluding guests, can subscribe to any public channel
irrespective of this setting.Users in this group can subscribe to a private channel as well.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 357).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_resolve_topics_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to resolve topics in the channel.Users who have similar realm-level permissions can resolve topics
in a channel regardless of the value of this setting.Changes: New in Zulip 11.0 (feature level 402).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_create_topic_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to create a new message_topic in this channel.Note that using this permission requires also having permission to
send messages in the channel.Note that this must be therole:everyonesystem groupforprivate channels with protected history.Changes: New in Zulip 12.0 (feature level 441). Previously,
if you could send messages in a channel, you could create topics in
the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.is_archived:booleanA boolean indicating whether the channel isarchived.Changes: New in Zulip 10.0 (feature level 315).
Previously, subscriptions only included active
channels. Note that some endpoints will never return archived
channels unless the client declares explicit support for
them via thearchived_channelsclient capability.subscriber_count:numberThe total number of non-deactivated users (including bots) who
are subscribed to the channel. Clients are responsible for updating
this value usingpeer_addandpeer_removeevents.The server's internals cannot guarantee this value is correctly
synced withpeer_addandpeer_removeevents for the channel. As
a result, if a (rare) race occurs between a change in the channel's
subscribers and fetching this value, it is possible for a client
that is correctly following the events protocol to end up with a
permanently off-by-one error in the channel's subscriber count.Clients are recommended to fetch full subscriber data for a channel
in contexts where it is important to avoid this risk. The official
web application, for example, uses this field primarily while
waiting to fetch a given channel's full subscriber list from the
server.Changes: New in Zulip 11.0 (feature level 394).
- never_subscribed:(object)[]Present ifsubscriptionis present infetch_event_types.A array of dictionaries where each dictionary describes one of the
channels that is visible to the user and the user has never been subscribed
to.Important for clients containing UI where one can browse channels to subscribe
to.Changes: Before Zulip 10.0 (feature level 362), archived channels did
not appear in this list, even if thearchived_channelsclient
capabilitywas declared by the client.Prior to Zulip 10.0 (feature level 349), if a user was
incan_administer_channel_groupof a channel that they never
subscribed to, but not an organization administrator, the channel
in question would not be part of this array.stream_id:integerThe unique ID of the channel.name:stringThe name of the channel.is_archived:booleanA boolean indicating whether the channel isarchived.Changes: New in Zulip 10.0 (feature level 315).
Previously, this endpoint never returned archived channels.description:stringThe short description of the channel inZulip-flavored Markdownformat,
intended to be used to prepopulate UI for editing a channel's
description.SeeMarkdown message formattingfor details on Zulip's HTML format.date_created:integerThe UNIX timestamp for when the channel was created, in UTC seconds.Changes: New in Zulip 4.0 (feature level 30).creator_id:integer | nullThe ID of the user who created this channel.Anullvalue means the channel has no recorded creator, which is often
because the channel is very old, was created during realm creation or
because it was created via a data import tool ormanagement command.Changes: New in Zulip 9.0 (feature level 254).invite_only:booleanSpecifies whether the channel is private or not.
Only people who have been invited can access a private channel.rendered_description:stringThe short description of the channel rendered as HTML, intended to
be used when displaying the channel description in a UI.One should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax
work correctly. And any client-side security logic for
user-generated message content should be applied when displaying
this HTML as though it were the body of a Zulip message.is_web_public:booleanWhether the channel has been configured to allow unauthenticated
access to its message history from the web.Changes: New in Zulip 2.1.0.stream_post_policy:integerA deprecated representation of a superset of the users who
have permission to post messages to the channel available
for backwards-compatibility. Clients should usecan_send_message_groupinstead.It is an enum with the following possible values, corresponding
to roles/system groups:1 = Any user can post.2 = Only administrators can post.3 = Onlyfull memberscan post.4 = Only moderators can post.Changes: Deprecated in Zulip 10.0 (feature level 333) and
replaced bycan_send_message_group, which supports finer
resolution of configurations, resulting in this property being
inaccurate following that transition.New in Zulip 3.0 (feature level 1), replacing the previousis_announcement_onlyboolean.message_retention_days:integer | nullNumber of days that messages sent to this channel will be stored
before being automatically deleted by themessage retention
policy. There are two special values:null, the default, means the channel will inherit the organization
  level setting.-1encodes retaining messages in this channel forever.Changes: New in Zulip 3.0 (feature level 17).history_public_to_subscribers:booleanWhether the history of the channel is public to its subscribers.Currently always true for public channels (i.e."invite_only": falseimplies"history_public_to_subscribers": true), but clients should not make that
assumption, as we may change that behavior in the future.topics_policy:stringWhethernamed topicsand the empty
message_topic (i.e.,"general chat" message_topic)
are enabled in this channel."inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty message_topic in this
  channel."allow_empty_topic": Messages can be sent to both named topics and
  the empty message_topic in this channel."disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty message_topic is disabled."empty_topic_only": Messages can be sent to the empty message_topic in this
  channel, but named topics are disabled. See"general chat"
  channels.The"empty_topic_only"policy can only be set if all existing messages
in the channel are already in the empty message_topic.When creating a new channel, if thetopics_policyis not specified, the"inherit"option will be set.Changes: In Zulip 11.0 (feature level 404), the"empty_topic_only"option was added.New in Zulip 11.0 (feature level 392).first_message_id:integer | nullThe ID of the first message in the channel.Intended to help clients determine whether they need to display
UI like the "show all topics" widget that would suggest the channel
has older history that can be accessed.Isnullfor channels with no message history.Changes: New in Zulip 2.1.0.folder_id:integer | nullThe ID of the folder to which the channel belongs.Isnullif channel does not belong to any folder.Changes: New in Zulip 11.0 (feature level 389).is_recently_active:booleanWhether the channel has recent message activity. Clients should use this to implementhide inactive channelsifdemote_inactive_streamsis enabled.Changes: New in Zulip 10.0 (feature level 323). Previously, clients implemented the
demote_inactive_streams from local message history, resulting in a choppy loading
experience.is_announcement_only:booleanWhether the given channel is announcement only or not.Changes: Deprecated in Zulip 3.0 (feature level 1). Clients
should usestream_post_policyinstead.can_add_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to add subscribers to this channel.Users who can administer the channel or have similar realm-level
permissions can add subscribers to a public channel regardless
of the value of this setting.Users in this group need not be subscribed to a private channel to
add subscribers to it.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 342). Previously, there was no
channel-level setting for this permission.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_remove_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to remove subscribers from this channel.Organization administrators can unsubscribe others from a channel as though
they were in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349), channel administrators
could not unsubscribe other users if they were not an organization
administrator or part ofcan_remove_subscribers_group. Realm administrators
were not allowed to unsubscribe other users from a private channel if they
were not subscribed to that channel.Prior to Zulip 10.0 (feature level 320), this value was always the integer
ID of a system group.Before Zulip 8.0 (feature level 197), thecan_remove_subscribers_groupsetting was namedcan_remove_subscribers_group_id.New in Zulip 6.0 (feature level 142).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_administer_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to administer this channel.Organization administrators can administer every channel as though they were
in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349) a user needed tohave content accessto a channel in
order to modify it. The exception to this rule was that organization
administrators can edit channel names and descriptions without
having full access to the channel.New in Zulip 10.0 (feature level 325). Prior to this
change, the permission to administer channels was limited to realm
administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_delete_any_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete any message in the channel.Note that a user musthave content accessto a
channel in order to delete any message in the channel.Users present in the organization-levelcan_delete_any_message_groupsetting can always delete any message in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users incan_delete_any_message_groupwere able
delete any message in the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_delete_own_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete the messages that they have sent in the channel.Note that a user musthave content accessto a
channel in order to delete their own message in the channel.Users with permission to delete any message in the channel
and users present in the organization-levelcan_delete_own_message_groupsetting
can always delete their own messages in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users in the organization-levelcan_delete_any_message_groupandcan_delete_own_message_groupsettings were able delete their own messages in
the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_move_messages_out_of_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages out of this channel.Note that a user musthave content accessto a
channel in order to move messages out of the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_channels_groupsetting can always move messages
out of the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_channels_groupwere able
move messages between channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_move_messages_within_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages within this channel.Note that a user musthave content accessto a
channel in order to move messages within the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_topics_groupsetting can always move messages
within the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_topics_groupwere able
move messages between topics of a channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_send_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to post in this channel.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Note that using this permission to send a message to a new message_topic requires
also having permission to create new topics in the channel.Changes: New in Zulip 10.0 (feature level 333). Previouslystream_post_policyfield used to control the permission to
post in the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_subscribe_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to subscribe themselves to this channel.Everyone, excluding guests, can subscribe to any public channel
irrespective of this setting.Users in this group can subscribe to a private channel as well.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 357).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_resolve_topics_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to resolve topics in the channel.Users who have similar realm-level permissions can resolve topics
in a channel regardless of the value of this setting.Changes: New in Zulip 11.0 (feature level 402).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_create_topic_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to create a new message_topic in this channel.Note that using this permission requires also having permission to
send messages in the channel.Note that this must be therole:everyonesystem groupforprivate channels with protected history.Changes: New in Zulip 12.0 (feature level 441). Previously,
if you could send messages in a channel, you could create topics in
the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.subscriber_count:numberThe total number of non-deactivated users (including bots) who
are subscribed to the channel. Clients are responsible for updating
this value usingpeer_addandpeer_removeevents.The server's internals cannot guarantee this value is correctly
synced withpeer_addandpeer_removeevents for the channel. As
a result, if a (rare) race occurs between a change in the channel's
subscribers and fetching this value, it is possible for a client
that is correctly following the events protocol to end up with a
permanently off-by-one error in the channel's subscriber count.Clients are recommended to fetch full subscriber data for a channel
in contexts where it is important to avoid this risk. The official
web application, for example, uses this field primarily while
waiting to fetch a given channel's full subscriber list from the
server.Changes: New in Zulip 11.0 (feature level 394).stream_weekly_traffic:integer | nullThe average number of messages sent to the channel per week, as
estimated based on recent weeks, rounded to the nearest integer.Ifnull, the channel was recently created and there is
insufficient data to estimate the average traffic.subscribers:(integer)[]A list of user IDs of users who are subscribed
to the channel. Included only ifinclude_subscribersistrue.If a user is not allowed to know the subscribers for
a channel, we will send an empty array. API authors
should use other data to determine whether users like
guest users are forbidden to know the subscribers.partial_subscribers:(integer)[]Ifinclude_subscribers="partial"was requested, the server may, at its discretion, send apartial_subscriberslist rather than asubscriberslist
for channels with a large number of subscribers.Thepartial_subscriberslist contains an arbitrary
subset of the channel's subscribers that is guaranteed
to include all bot user subscribers as well as all
users who have been active in the last 14 days, but
otherwise can be chosen arbitrarily by the server.If a user is not allowed to know the subscribers for
a channel, we will send an empty array. API authors
should use other data to determine whether users like
guest users are forbidden to know the subscribers.Changes: New in Zulip 11.0 (feature level 412).
- channel_folders:(object)[]Present ifchannel_foldersis present infetch_event_types.An array of dictionaries where each dictionary describes one
of the channel folders in the organization.Only channel folders with one or more public web channels are
visible to spectators.Changes: New in Zulip 11.0 (feature level 389).id:integerThe unique ID of the channel folder.name:stringThe name of the channel folder.order:integerThis value determines in which order the channel folder should be
displayed in the UI. The value is 0 indexed, and a channel folder with
a lower value should be displayed before channel folders with higher
values.Changes: New in Zulip 11.0 (feature level 414).date_created:integer | nullThe UNIX timestamp for when the channel folder was created,
in UTC seconds.creator_id:integer | nullThe ID of the user who created the channel folder.description:stringThe description of the channel folder. Can be an empty string.SeeMarkdown message formattingfor details
on Zulip's HTML format.rendered_description:stringThe description of the channel folder rendered as HTML, intended to be
used for UI that displays the channel folder description.Clients should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax work
correctly. And any client-side security logic for user-generated
message content should be applied when displaying this HTML as though
it were the body of a Zulip message.is_archived:booleanWhether the channel folder is archived or not.
- unread_msgs:objectPresent ifmessageandupdate_message_flagsare both present inevent_types.A set of data structures describing the conversations containing
the 50000 most recent unread messages the user has received. This will usually
contain every unread message the user has received, but clients should support
users with even more unread messages (and not hardcode the number 50000).count:integerThe total number of unread messages to display. This includes one-on-one and group
direct messages, as well as channel messages that are notmuted.Changes: Before Zulip 8.0 (feature level 213), the unmute and follow
message_topic features were not handled correctly in calculating this field.pms:(object)[]An array of objects where each object contains details of unread
one-on-one direct messages with a specific user.Note that it is possible for a message that the current user sent
to the specified user to be marked as unread and thus appear here.other_user_id:integerThe user ID of the other participant in this one-on-one direct
message conversation. Will be the current user's ID for messages
that they sent in a one-on-one direct message conversation with
themself.Changes: New in Zulip 5.0 (feature level 119), replacing
the less clearly namedsender_idfield.sender_id:integerOld name for theother_user_idfield. Clients should access
this field in Zulip server versions that do not yet supportother_user_id.Changes: Deprecated in Zulip 5.0 (feature level 119).
We expect to provide a next version of the fullunread_msgsAPI before removing this legacy name.unread_message_ids:(integer)[]The message IDs of the recent unread direct messages sent
by either user in this one-on-one direct message conversation,
sorted in ascending order.streams:(object)[]An array of dictionaries where each dictionary contains details of all
unread messages of a single subscribed channel. This includes muted channels
and muted topics, even though those messages are excluded fromcount.Changes: Prior to Zulip 5.0 (feature level 90), these objects
included asender_idsproperty, which listed the set of IDs of
users who had sent the unread messages.message_topic:stringThe message_topic under which the messages were sent.Note that the empty string message_topic may have been rewritten by the server
to the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse depending on the value
of theempty_topic_nameclient capability.Changes: Theempty_topic_nameclient capability is new in
Zulip 10.0 (feature level 334).stream_id:integerThe ID of the channel to which the messages were sent.unread_message_ids:(integer)[]The message IDs of the recent unread messages sent in this channel,
sorted in ascending order.huddles:(object)[]An array of objects where each object contains details of unread
group direct messages with a specific group of users.user_ids_string:stringA string containing the IDs of all users in the group
direct message conversation, including the current user,
separated by commas and sorted numerically; for example:"1,2,3".unread_message_ids:(integer)[]The message IDs of the recent unread messages which have been sent in
this group direct message conversation, sorted in ascending order.mentions:(integer)[]Array containing the IDs of all unread messages in which the user was
mentioned directly, and unreadnon-mutedmessages
in which the user was mentioned through a wildcard.Changes: Before Zulip 8.0 (feature level 213), the unmute and follow
message_topic features were not handled correctly in calculating this field.old_unreads_missing:booleanWhether this data set was truncated because the user has too many
unread messages. When truncation occurs, only the most recentMAX_UNREAD_MESSAGES(currently 50000) messages will be considered
when forming this response. Whentrue, we recommend that clients
display a warning, as they are likely to produce erroneous results
until reloaded with the user having fewer thanMAX_UNREAD_MESSAGESunread messages.Changes: New in Zulip 4.0 (feature level 44).
- starred_messages:(integer)[]Present ifstarred_messagesis present infetch_event_types.Array containing the IDs of all messages which have beenstarredby the user.
- streams:(object)[]Present ifstreamis present infetch_event_types.Array of dictionaries where each dictionary contains details about
a single channel in the organization that is visible to the user.For organization administrators, this will include all private channels
in the organization.Changes: Before Zulip 11.0 (feature level 378), archived channels
did not appear in this list, even if thearchived_channelsclient
capabilitywas declared by the client.As of Zulip 8.0 (feature level 205), this will include all web-public
channels in the organization as well.stream_id:integerThe unique ID of the channel.name:stringThe name of the channel.is_archived:booleanA boolean indicating whether the channel isarchived.Changes: New in Zulip 10.0 (feature level 315).
Previously, this endpoint never returned archived channels.description:stringThe short description of the channel inZulip-flavored Markdownformat,
intended to be used to prepopulate UI for editing a channel's
description.SeeMarkdown message formattingfor details on Zulip's HTML format.date_created:integerThe UNIX timestamp for when the channel was created, in UTC seconds.Changes: New in Zulip 4.0 (feature level 30).creator_id:integer | nullThe ID of the user who created this channel.Anullvalue means the channel has no recorded creator, which is often
because the channel is very old, was created during realm creation or
because it was created via a data import tool ormanagement command.Changes: New in Zulip 9.0 (feature level 254).invite_only:booleanSpecifies whether the channel is private or not.
Only people who have been invited can access a private channel.rendered_description:stringThe short description of the channel rendered as HTML, intended to
be used when displaying the channel description in a UI.One should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax
work correctly. And any client-side security logic for
user-generated message content should be applied when displaying
this HTML as though it were the body of a Zulip message.is_web_public:booleanWhether the channel has been configured to allow unauthenticated
access to its message history from the web.Changes: New in Zulip 2.1.0.stream_post_policy:integerA deprecated representation of a superset of the users who
have permission to post messages to the channel available
for backwards-compatibility. Clients should usecan_send_message_groupinstead.It is an enum with the following possible values, corresponding
to roles/system groups:1 = Any user can post.2 = Only administrators can post.3 = Onlyfull memberscan post.4 = Only moderators can post.Changes: Deprecated in Zulip 10.0 (feature level 333) and
replaced bycan_send_message_group, which supports finer
resolution of configurations, resulting in this property being
inaccurate following that transition.New in Zulip 3.0 (feature level 1), replacing the previousis_announcement_onlyboolean.message_retention_days:integer | nullNumber of days that messages sent to this channel will be stored
before being automatically deleted by themessage retention
policy. There are two special values:null, the default, means the channel will inherit the organization
  level setting.-1encodes retaining messages in this channel forever.Changes: New in Zulip 3.0 (feature level 17).history_public_to_subscribers:booleanWhether the history of the channel is public to its subscribers.Currently always true for public channels (i.e."invite_only": falseimplies"history_public_to_subscribers": true), but clients should not make that
assumption, as we may change that behavior in the future.topics_policy:stringWhethernamed topicsand the empty
message_topic (i.e.,"general chat" message_topic)
are enabled in this channel."inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty message_topic in this
  channel."allow_empty_topic": Messages can be sent to both named topics and
  the empty message_topic in this channel."disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty message_topic is disabled."empty_topic_only": Messages can be sent to the empty message_topic in this
  channel, but named topics are disabled. See"general chat"
  channels.The"empty_topic_only"policy can only be set if all existing messages
in the channel are already in the empty message_topic.When creating a new channel, if thetopics_policyis not specified, the"inherit"option will be set.Changes: In Zulip 11.0 (feature level 404), the"empty_topic_only"option was added.New in Zulip 11.0 (feature level 392).first_message_id:integer | nullThe ID of the first message in the channel.Intended to help clients determine whether they need to display
UI like the "show all topics" widget that would suggest the channel
has older history that can be accessed.Isnullfor channels with no message history.Changes: New in Zulip 2.1.0.folder_id:integer | nullThe ID of the folder to which the channel belongs.Isnullif channel does not belong to any folder.Changes: New in Zulip 11.0 (feature level 389).is_recently_active:booleanWhether the channel has recent message activity. Clients should use this to implementhide inactive channelsifdemote_inactive_streamsis enabled.Changes: New in Zulip 10.0 (feature level 323). Previously, clients implemented the
demote_inactive_streams from local message history, resulting in a choppy loading
experience.is_announcement_only:booleanWhether the given channel is announcement only or not.Changes: Deprecated in Zulip 3.0 (feature level 1). Clients
should usestream_post_policyinstead.can_add_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to add subscribers to this channel.Users who can administer the channel or have similar realm-level
permissions can add subscribers to a public channel regardless
of the value of this setting.Users in this group need not be subscribed to a private channel to
add subscribers to it.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 342). Previously, there was no
channel-level setting for this permission.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_remove_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to remove subscribers from this channel.Organization administrators can unsubscribe others from a channel as though
they were in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349), channel administrators
could not unsubscribe other users if they were not an organization
administrator or part ofcan_remove_subscribers_group. Realm administrators
were not allowed to unsubscribe other users from a private channel if they
were not subscribed to that channel.Prior to Zulip 10.0 (feature level 320), this value was always the integer
ID of a system group.Before Zulip 8.0 (feature level 197), thecan_remove_subscribers_groupsetting was namedcan_remove_subscribers_group_id.New in Zulip 6.0 (feature level 142).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_administer_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to administer this channel.Organization administrators can administer every channel as though they were
in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349) a user needed tohave content accessto a channel in
order to modify it. The exception to this rule was that organization
administrators can edit channel names and descriptions without
having full access to the channel.New in Zulip 10.0 (feature level 325). Prior to this
change, the permission to administer channels was limited to realm
administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_delete_any_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete any message in the channel.Note that a user musthave content accessto a
channel in order to delete any message in the channel.Users present in the organization-levelcan_delete_any_message_groupsetting can always delete any message in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users incan_delete_any_message_groupwere able
delete any message in the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_delete_own_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete the messages that they have sent in the channel.Note that a user musthave content accessto a
channel in order to delete their own message in the channel.Users with permission to delete any message in the channel
and users present in the organization-levelcan_delete_own_message_groupsetting
can always delete their own messages in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users in the organization-levelcan_delete_any_message_groupandcan_delete_own_message_groupsettings were able delete their own messages in
the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_move_messages_out_of_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages out of this channel.Note that a user musthave content accessto a
channel in order to move messages out of the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_channels_groupsetting can always move messages
out of the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_channels_groupwere able
move messages between channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_move_messages_within_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages within this channel.Note that a user musthave content accessto a
channel in order to move messages within the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_topics_groupsetting can always move messages
within the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_topics_groupwere able
move messages between topics of a channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_send_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to post in this channel.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Note that using this permission to send a message to a new message_topic requires
also having permission to create new topics in the channel.Changes: New in Zulip 10.0 (feature level 333). Previouslystream_post_policyfield used to control the permission to
post in the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_subscribe_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to subscribe themselves to this channel.Everyone, excluding guests, can subscribe to any public channel
irrespective of this setting.Users in this group can subscribe to a private channel as well.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 357).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_resolve_topics_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to resolve topics in the channel.Users who have similar realm-level permissions can resolve topics
in a channel regardless of the value of this setting.Changes: New in Zulip 11.0 (feature level 402).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_create_topic_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to create a new message_topic in this channel.Note that using this permission requires also having permission to
send messages in the channel.Note that this must be therole:everyonesystem groupforprivate channels with protected history.Changes: New in Zulip 12.0 (feature level 441). Previously,
if you could send messages in a channel, you could create topics in
the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.subscriber_count:numberThe total number of non-deactivated users (including bots) who
are subscribed to the channel. Clients are responsible for updating
this value usingpeer_addandpeer_removeevents.The server's internals cannot guarantee this value is correctly
synced withpeer_addandpeer_removeevents for the channel. As
a result, if a (rare) race occurs between a change in the channel's
subscribers and fetching this value, it is possible for a client
that is correctly following the events protocol to end up with a
permanently off-by-one error in the channel's subscriber count.Clients are recommended to fetch full subscriber data for a channel
in contexts where it is important to avoid this risk. The official
web application, for example, uses this field primarily while
waiting to fetch a given channel's full subscriber list from the
server.Changes: New in Zulip 11.0 (feature level 394).stream_weekly_traffic:integer | nullThe average number of messages sent to the channel per week, as
estimated based on recent weeks, rounded to the nearest integer.Ifnull, no information is provided on the average traffic.
This can be because the channel was recently created and there
is insufficient data to make an estimate, or because the server
wishes to omit this information for this client, this realm, or
this endpoint or type of event.Changes: New in Zulip 8.0 (feature level 199). Previously, this
statistic was available only in subscription objects.
- realm_default_streams:(integer)[]Present ifdefault_streamsis present infetch_event_types.An array of IDs of all thedefault channelsin the organization.Changes: Before Zulip 10.0 (feature level 330), we sent
array of dictionaries where each dictionary contained details
about a single default channel_name for the Zulip organization.
- realm_default_stream_groups:(object)[]Present ifdefault_stream_groupsis present infetch_event_types.An array of dictionaries where each dictionary contains details
about a single default channel group configured for this
Zulip organization.Default channel groups are an experimental feature.name:stringName of the default channel group.description:stringDescription of the default channel group.id:integerThe ID of the default channel group.streams:(integer)[]An array of IDs of all the channels in the default channel_name group.Changes: Before Zulip 10.0 (feature level 330), we sent array
of dictionaries where each dictionary contained details about a
single channel_name in the default channel_name group.
- stop_words:(string)[]Present ifstop_wordsis present infetch_event_types.An array containing the stop words used by the Zulip server's
full-text search implementation. Useful for showing helpful
error messages when a search returns limited results because
a stop word in the query was ignored.
- user_status:objectPresent ifuser_statusis present infetch_event_types.A dictionary which contains thestatusof all users in the Zulip organization who have set a status.Changes: The emoji parameters are new in Zulip 5.0 (feature level 86).
Previously, Zulip did not support emoji associated with statuses.{user_id}:objectObject containing the status details of a user
with the key of the object being the ID of the user.away:booleanIf present, the user has marked themself "away".Changes: Deprecated in Zulip 6.0 (feature level 148);
starting with that feature level,awayis a legacy way to
access the user'spresence_enabledsetting, withaway = !presence_enabled. To be removed in a future release.status_text:stringIf present, the text content of the user's status message.emoji_name:stringIf present, the name for the emoji to associate with the user's status.Changes: New in Zulip 5.0 (feature level 86).emoji_code:stringIf present, a unique identifier, defining the specific emoji codepoint
requested, within the namespace of thereaction_type.Changes: New in Zulip 5.0 (feature level 86).reaction_type:stringIf present, a string indicating the type of emoji. Each emojireaction_typehas an independent namespace for values ofemoji_code.Must be one of the following values:unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").Changes: New in Zulip 5.0 (feature level 86).
- user_settings:objectPresent ifuser_settingsis present infetch_event_types.A dictionary containing the user's personal settings.Changes: In Zulip 12.0 (feature level 439), removed deprecated,
duplicate copies of many of these user settings from the top-level object.
Previously, clients that did not include theuser_settings_objectclient capabilityand includedupdate_display_settingsorupdate_global_notificationsinfetch_event_typeswould receive those
user settings that predated feature level 89 in the top-level response.In Zulip 10.0 (feature level 364), removed thedense_modesetting as we
now haveweb_font_size_pxandweb_line_height_percentsettings for
more control.New in Zulip 5.0 (feature level 89). Previously, user settings appeared
in the top-level object; see theuser_settings_objectclient capabilityfor backwards-compatibility.twenty_four_hour_time:boolean | nullWhether time should bedisplayed in 24-hour notation.Anullvalue indicates that the client should use the default time
format for the user's locale.Changes: Prior to Zulip 11.0 (feature level 408),nullwas not a valid value for this setting. Note that it was not possible
to actually set the time format tonullat this feature level.web_mark_read_on_scroll_policy:integerWhether or not to mark messages as read when the user scrolls through their
feed.1 - Always2 - Only in conversation views3 - NeverChanges: New in Zulip 7.0 (feature level 175). Previously, there was no
way for the user to configure this behavior on the web, and the Zulip web and
desktop apps behaved like the "Always" setting when marking messages as read.web_channel_default_view:integerWeb/desktop app setting controlling the default navigation
behavior when clicking on a channel link.1 - Top message_topic in the channel2 - Channel feed3 - List of topics4 - Top unread message_topic in channelChanges: The "Top unread message_topic in channel" is new in Zulip 11.0
(feature level 401).The "List of topics" option is new in Zulip 11.0 (feature level 383).New in Zulip 9.0 (feature level 269). Previously, this
was not configurable, and every user had the "Channel feed" behavior.starred_message_counts:booleanWhether clients should display thenumber of starred
messages.receives_typing_notifications:booleanWhether the user is configured to receive typing notifications from
other users. The server will only deliver typing notifications events
to users who for whom this is enabled.Changes: New in Zulip 9.0 (feature level 253). Previously, there were
only options to disable sending typing notifications.web_suggest_update_timezone:booleanWhether the user should be shown an alert, offering to update theirprofile time zone, when the time displayed
for the profile time zone differs from the current time displayed by the
time zone configured on their device.Changes: New in Zulip 10.0 (feature level 329).fluid_layout_width:booleanWhether to use themaximum available screen widthfor the web app's center panel (message feed, recent conversations) on wide screens.high_contrast_mode:booleanThis setting is reserved for use to control variations in Zulip's design
to help visually impaired users.web_font_size_px:integerUser-configured primaryfont-sizefor the web application, in pixels.Changes: New in Zulip 9.0 (feature level 245). Previously, font size was
only adjustable via browser zoom. Note that this setting was not fully
implemented at this feature level.web_line_height_percent:integerUser-configured primaryline-heightfor the web application, in percent, so a
value of 120 represents aline-heightof 1.2.Changes: New in Zulip 9.0 (feature level 245). Previously, line height was
not user-configurable. Note that this setting was not fully implemented at this
feature level.color_scheme:integerControls whichcolor themeto use.1 - Automatic2 - Dark theme3 - Light themeAutomatic detection is implementing using the standardprefers-color-schememedia query.translate_emoticons:booleanWhether totranslate emoticons to emojiin messages the user sends.display_emoji_reaction_users:booleanWhether to display the names of reacting users on a message.When enabled, clients should display the names of reacting
users, rather than a count, for messages with few total
reactions. The ideal cutoff may depend on the space
available for displaying reactions; the official web
application displays names when 3 or fewer total reactions
are present with this setting enabled.Changes: New in Zulip 6.0 (feature level 125).default_language:stringWhatdefault languageto use for the account.This controls both the Zulip UI as well as email notifications sent to the user.The value needs to be a standard language code that the Zulip server has
translation data for; for example,"en"for English or"de"for German.web_home_view:stringThehome viewused when opening a new
Zulip web app window or hitting theEsckeyboard shortcut repeatedly."recent" - Recent conversations view"inbox" - Inbox view"all_messages" - Combined feed viewChanges: Before Zulip 12.0 (feature level 454), the Recent
view had"recent_topics"as its string encoding.New in Zulip 8.0 (feature level 219). Previously, this was
calleddefault_view, which was new in Zulip 4.0 (feature level 42).web_escape_navigates_to_home_view:booleanWhether the escape key navigates to theconfigured home view.Changes: New in Zulip 8.0 (feature level 219). Previously, this
was calledescape_navigates_to_default_view, which was new in Zulip
5.0 (feature level 107).left_side_userlist:booleanWhether the users list on left sidebar in filter_spec windows.This feature is not heavily used and is likely to be reworked.emojiset:stringThe user's configuredemoji set,
used to display emoji to the user everywhere they appear in the UI."google" - Google modern"twitter" - Twitter"text" - Plain textdemote_inactive_streams:integerWhether tohide inactive channelsin the left sidebar.1 - Automatic2 - Always3 - Neveruser_list_style:integerThe style selected by the user for the right sidebar user list.1 - Compact2 - With status3 - With avatar and statusChanges: New in Zulip 6.0 (feature level 141).web_animate_image_previews:stringControls how animated images should be played in the message feed in the web/desktop application."always" - Always play the animated images in the message feed."on_hover" - Play the animated images on hover over them in the message feed."never" - Never play animated images in the message feed.Changes: New in Zulip 9.0 (feature level 275).web_stream_unreads_count_display_policy:integerConfiguration for which channels should be displayed with a numeric unread count in the left sidebar.
Channels that do not have an unread count will have a simple dot indicator for whether there are any
unread messages.1 - All channels2 - Unmuted channels and topics3 - No channelsChanges: New in Zulip 8.0 (feature level 210).hide_ai_features:booleanControls whether user wants AI features like message_topic summarization to
be hidden in all Zulip clients.Changes: New in Zulip 10.0 (feature level 350).web_inbox_show_channel_folders:booleanDetermines whetherchannel foldersare used to organize how conversations with unread messages
are displayed in the web/desktop application's Inbox view.Changes: New in Zulip 12.0 (feature level 431).web_left_sidebar_show_channel_folders:booleanDetermines whetherchannel foldersare used to organize how channels are displayed in the
web/desktop application's left sidebar.Changes: New in Zulip 11.0 (feature level 411).web_left_sidebar_unreads_count_summary:booleanDetermines whether the web/desktop application's left sidebar displays
the unread message count summary.Changes: New in Zulip 11.0 (feature level 398).timezone:stringThe IANA identifier of the user'sprofile time zone,
which is used primarily to display the user's local time to other users.enter_sends:booleanWhether the user setting forsending on pressing Enterin the compose box is enabled.enable_drafts_synchronization:booleanA boolean parameter to control whether synchronizing drafts is enabled for
the user. When synchronization is disabled, all drafts stored in the server
will be automatically deleted from the server.This does not do anything (like sending events) to delete local copies of
drafts stored in clients.enable_stream_desktop_notifications:booleanEnable visual desktop notifications for channel messages.enable_stream_email_notifications:booleanEnable email notifications for channel messages.enable_stream_push_notifications:booleanEnable mobile notifications for channel messages.enable_stream_audible_notifications:booleanEnable audible desktop notifications for channel messages.notification_sound:stringNotification sound name.enable_desktop_notifications:booleanEnable visual desktop notifications for direct messages and @-mentions.enable_sounds:booleanEnable audible desktop notifications for direct messages and
@-mentions.enable_followed_topic_desktop_notifications:booleanEnable visual desktop notifications for messages sent to followed topics.Changes: New in Zulip 8.0 (feature level 189).enable_followed_topic_email_notifications:booleanEnable email notifications for messages sent to followed topics.Changes: New in Zulip 8.0 (feature level 189).enable_followed_topic_push_notifications:booleanEnable push notifications for messages sent to followed topics.Changes: New in Zulip 8.0 (feature level 189).enable_followed_topic_audible_notifications:booleanEnable audible desktop notifications for messages sent to followed topics.Changes: New in Zulip 8.0 (feature level 189).email_notifications_batching_period_seconds:integerThe duration (in seconds) for which the server should wait to batch
email notifications before sending them.enable_offline_email_notifications:booleanEnable email notifications for direct messages and @-mentions received
when the user is offline.enable_offline_push_notifications:booleanEnable mobile notification for direct messages and @-mentions received
when the user is offline.enable_online_push_notifications:booleanEnable mobile notification for direct messages and @-mentions received
when the user is online.enable_digest_emails:booleanEnable digest emails when the user is away.enable_marketing_emails:booleanEnable marketing emails. Has no function outside Zulip Cloud.enable_login_emails:booleanEnable email notifications for new logins to account.message_content_in_email_notifications:booleanInclude the message's content in email notifications for new messages.pm_content_in_desktop_notifications:booleanInclude content of direct messages in desktop notifications.wildcard_mentions_notify:booleanWhether wildcard mentions (E.g. @all) should send notifications
like a personal mention.enable_followed_topic_wildcard_mentions_notify:booleanWhether wildcard mentions (e.g., @all) in messages sent to followed topics
should send notifications like a personal mention.Changes: New in Zulip 8.0 (feature level 189).desktop_icon_count_display:integerUnread count badge (appears in desktop sidebar and browser tab)1 - All unread messages2 - DMs, mentions, and followed topics3 - DMs and mentions4 - NoneChanges: In Zulip 8.0 (feature level 227), addedDMs, mentions,
and followed topicsoption, renumbering the options to insert it in
order.realm_name_in_email_notifications_policy:integerWhether toinclude organization name in subject of message notification
emails.1 - Automatic2 - Always3 - NeverChanges: New in Zulip 7.0 (feature level 168), replacing the
previousrealm_name_in_notificationsboolean;truecorresponded toAlways, andfalsetoNever.automatically_follow_topics_policy:integerWhichtopics to follow automatically.1 - Topics the user participates in2 - Topics the user sends a message to3 - Topics the user starts4 - NeverChanges: New in Zulip 8.0 (feature level 214).automatically_unmute_topics_in_muted_streams_policy:integerWhichtopics to unmute automatically in muted channels.1 - Topics the user participates in2 - Topics the user sends a message to3 - Topics the user starts4 - NeverChanges: New in Zulip 8.0 (feature level 214).automatically_follow_topics_where_mentioned:booleanWhether the server will automatically mark the user as following
topics where the user is mentioned.Changes: New in Zulip 8.0 (feature level 235).resolved_topic_notice_auto_read_policy:stringControls whether the resolved-message_topic notices are marked as read."always" - Always mark resolved-message_topic notices as read."except_followed" - Mark resolved-message_topic notices as read in topics not followed by the user."never" - Never mark resolved-message_topic notices as read.Changes: New in Zulip 11.0 (feature level 385).presence_enabled:booleanDisplay the presence status to other users when online.available_notification_sounds:(string)[]Array containing the names of the notification sound options
supported by this Zulip server. Only relevant to support UI
for configuring notification sounds.emojiset_choices:(object)[]Array of dictionaries where each dictionary describes an emoji set
supported by this version of the Zulip server.Only relevant to clients with configuration UI for choosing an emoji set;
the currently selected emoji set is available in theemojisetkey.SeePATCH /settingsfor details on
the meaning of this setting.key:stringThe key or the name of the emoji set which will be the value
ofemojisetif this emoji set is chosen.text:stringThe text describing the emoji set.send_private_typing_notifications:booleanWhether the user has chosen to sendtyping
notificationswhen composing direct messages. The client should send typing
notifications for direct messages if and only if this setting is enabled.Changes: New in Zulip 5.0 (feature level 105).send_stream_typing_notifications:booleanWhether the user has chosen to sendtyping
notificationswhen composing channel messages. The client should send typing
notifications for channel messages if and only if this setting is enabled.Changes: New in Zulip 5.0 (feature level 105).send_read_receipts:booleanWhether other users are allowed to see whether you've
read messages.Changes: New in Zulip 5.0 (feature level 105).allow_private_data_export:booleanWhether organization administrators are allowed to
export your private data.Changes: New in Zulip 10.0 (feature level 293).email_address_visibility:integerThepolicyforwhich other usersin this organization can see the user's real email address.1 = Everyone2 = Members only3 = Administrators only4 = Nobody5 = Moderators onlyChanges: New in Zulip 7.0 (feature level 163), replacing the
realm-level setting.web_navigate_to_sent_message:booleanWeb/desktop app setting for whether the user's view should
automatically go to the conversation where they sent a message.Changes: New in Zulip 9.0 (feature level 268). Previously,
this behavior was not configurable.
- user_topics:(object)[]Present ifuser_topicis present infetch_event_types.Changes: New in Zulip 6.0 (feature level 134), deprecating and
replacing the previousmuted_topicsstructure.stream_id:integerThe ID of the channel to which the message_topic belongs.topic_name:stringThe name of the message_topic.Note that the empty string message_topic may have been rewritten by the server to
the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse depending on the value of theempty_topic_nameclient capability.Changes: Theempty_topic_nameclient capability is new in
Zulip 10.0 (feature level 334).last_updated:integerAn integer UNIX timestamp representing when the user-message_topic
relationship was changed.visibility_policy:integerAn integer indicating the user's visibility configuration for
the message_topic.1 = Muted. Used to recordmuted topics.2 = Unmuted. Used to recordunmuted topics.3 = Followed. Used to recordfollowed topics.Changes: In Zulip 7.0 (feature level 219), added followed as
a visibility policy option.In Zulip 7.0 (feature level 170), added unmuted as a visibility
policy option.
- has_zoom_token:booleanPresent ifvideo_callsis present infetch_event_types.A boolean which signifies whether the user has a Zoom token and has thus
completed OAuth flow for theZoom integration.
Clients need to know whether initiating Zoom OAuth is required before
creating a Zoom call.
- giphy_api_key:stringPresent ifgiphyis present infetch_event_types.GIPHY's client-side SDKs needs this API key to use the GIPHY API.
GIPHY API keys are not secret (their main purpose appears to be
allowing GIPHY to block a problematic app). Please don't use our API
key for an app unrelated to Zulip.Developers of clients should also read theGIPHY API TOSbefore using this API key.Changes: Added in Zulip 4.0 (feature level 47).
- tenor_api_key:stringPresent iftenoris present infetch_event_types.Tenor API keys are meant to be sent to the clients, see the
examples in theTenor Endpoints documentation.
Please don't use our API key for an app unrelated to Zulip.Developers of clients are recommended to use their Zulip client string,
likeZulipFlutter, as theclientin the Tenor API to differentiate
across clients as per theTenor Endpoints documentation.Developers of clients should also read theTenor API TOS.Changes: New in Zulip 12.0 (feature level 442).
- devices:objectPresent ifdeviceis present infetch_event_types.Dictionary where each entry describes the user's logged-in devices,
registered usingPOST /register_client_device.Changes: New in Zulip 12.0 (feature level 468).{device_id}:objectDictionary containing the details of
a device with the device ID as the key.push_key_id:integer | nullID to reference the encryption key used to encrypt
push notifications sent to the device.push_token_id:string | nullID to reference the token provided by FCM/APNs to the device,
which is registered to the push bouncer service.pending_push_token_id:string | nullID to reference the token provided by FCM/APNs to the device,
whose registration is in progress to the push bouncer service.push_token_last_updated_timestamp:integer | nullThe UNIX timestamp for the last time whenpending_push_token_idwas set to a new non-null value, in UTC seconds.push_registration_error_code:string | nullIf the push registration failed, aZulip API error
codeindicating the type of
failure that occurred.The following error codes have recommended client behavior:"INVALID_BOUNCER_PUBLIC_KEY"- Inform the user to update app."REQUEST_EXPIRED- Retry with a fresh payload.
- receives_typing_notifications:booleanWhether the user is configured to receive typing notifications from other
users. The server will only deliver typing notifications events to users who
for whom this is enabled.Changes: New in Zulip 9.0 (feature level 253). Previously, there were
only options to disable sending typing notifications.
- realm_message_edit_history_visibility_policy:stringPresent ifrealmis present infetch_event_types.What typesof message edit history are accessible to users viamessage edit history."all" = All edit history is visible."moves" = Only moves are visible."none" = No edit history is visible.Changes: New in Zulip 10.0 (feature level 358), replacing the previousallow_edit_historyboolean setting;truecorresponds toall,
andfalsetonone.
- realm_allow_edit_history:booleanPresent ifrealmis present infetch_event_types.Whether this organization is configured to allow users to accessmessage edit history.The value ofrealm_allow_edit_historyis set asfalseif therealm_message_edit_history_visibility_policyis configured as "None"
andtrueif it is configured as "Moves only" or "All".Changes: Deprecated in Zulip 10.0 (feature level 358) and will be
removed in the future, as it is an inaccurate versionrealm_message_edit_history_visibility_policy, which replaces this field.
- realm_can_add_custom_emoji_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the set of
users who have permission to add custom emoji in the organization.Changes: New in Zulip 10.0 (feature level 307). Previously, this
permission was controlled by the enumadd_custom_emoji_policy. Values
were 1=Members, 2=Admins, 3=Full members, 4=Moderators.Before Zulip 5.0 (feature level 85), therealm_add_emoji_by_admins_onlyboolean setting controlled this permission;truecorresponded toAdmins,
andfalsetoEveryone.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_add_subscribers_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the set of
users who have permission to add subscribers to channels in the organization.Changes: New in Zulip 10.0 (feature level 341). Previously, this
permission was controlled by the enuminvite_to_stream_policy. Values
were 1=Members, 2=Admins, 3=Full members, 4=Moderators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_delete_any_message_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the set of
users who have permission to delete any message in the organization.Note that a user must also be able to access the content of a message
in order to delete it. Seechannel permissionsfor information about content access for channel messages. For direct
messages, the user must have received or sent the direct message to
have content access.Changes: New in Zulip 10.0 (feature level 281). Previously, this
permission was limited to administrators only and was uneditable.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_delete_own_message_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the set of
users who have permission to delete messages that they have sent in the
organization.Changes: New in Zulip 10.0 (feature level 291). Previously, this
permission was controlled by the enumdelete_own_message_policy. Values
were 1=Members, 2=Admins, 3=Full members, 4=Moderators, 5=Everyone.Before Zulip 5.0 (feature level 101), theallow_message_deletingboolean
setting controlled this permission;truecorresponded toEveryone, andfalsetoAdmins.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_set_delete_message_policy_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the set of
users who have permission to change per-channelcan_delete_any_message_groupandcan_delete_own_message_grouppermission settings. Note that the user
must be a member of both this group and thecan_administer_channel_groupof the channel whose message delete settings they want to change.Organization administrators can always change these settings of
every channel.Changes: New in Zulip 11.0 (feature level 407).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_set_topics_policy_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the set of
users who have permission to change per-channeltopics_policysetting. Note that
the user must be a member of both this group and thecan_administer_channel_groupof the channel whosetopics_policythey want to change.Organization administrators can always change thetopics_policysetting of
every channel.Changes: New in Zulip 11.0 (feature level 392).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_invite_users_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the set of
users who have permission to send email invitations for inviting other users
to the organization.Changes: New in Zulip 10.0 (feature level 321). Previously, this
permission was controlled by the enuminvite_to_realm_policy. Values
were 1=Members, 2=Admins, 3=Full members, 4=Moderators, 6=Nobody.Before Zulip 4.0 (feature level 50), theinvite_by_admins_onlyboolean
setting controlled this permission;truecorresponded toAdmins, andfalsetoMembers.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_mention_many_users_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the set of
users who have permission to use wildcard mentions in large channels.All users will receive a warning/reminder when using mentions in large
channels, even when permitted to do so.Changes: New in Zulip 10.0 (feature level 352). Previously, this
permission was controlled by the enumwildcard_mention_policy.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_move_messages_between_channels_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the set of
users who have permission to move messages from one channel to another
in the organization.Changes: New in Zulip 10.0 (feature level 310). Previously, this
permission was controlled by the enummove_messages_between_streams_policy.
Values were 1=Members, 2=Admins, 3=Full members, 4=Moderators, 6=Nobody.In Zulip 7.0 (feature level 159),Nobodywas added as an option tomove_messages_between_streams_policyenum.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_move_messages_between_topics_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the set of
users who have permission to move messages from one message_topic to another
within a channel in the organization.Changes: New in Zulip 10.0 (feature level 316). Previously, this
permission was controlled by the enumedit_topic_policy. Values were
1=Members, 2=Admins, 3=Full members, 4=Moderators, 5=Everyone, 6=Nobody.In Zulip 7.0 (feature level 159),Nobodywas added as an option toedit_topic_policyenum.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_create_groups:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining
the set of users who have permission to create user
groups in this organization.Changes: New in Zulip 10.0 (feature level 299). Previouslyrealm_user_group_edit_policyfield used to control the
permission to create user groups.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_create_bots_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining
the set of users who have permission to create all types of bot users
in the organization. See alsocan_create_write_only_bots_group.Changes: New in Zulip 10.0 (feature level 344). Previously, this
permission was controlled by the enumbot_creation_policy. Values
were 1=Members, 2=Generic bots limited to administrators, 3=Administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_create_write_only_bots_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining
the set of users who have permission to create bot users that
can only send messages in the organization, i.e. incoming webhooks,
in addition to the users who are present incan_create_bots_group.Changes: New in Zulip 10.0 (feature level 344). Previously, this
permission was controlled by the enumbot_creation_policy. Values
were 1=Members, 2=Generic bots limited to administrators, 3=Administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_manage_all_groups:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the set of users who have permission to
administer all existing groups in this organization.Changes: Prior to Zulip 10.0 (feature level 305), only users who
were a member of the group or had the moderator role or above could
exercise the permission on a given group.New in Zulip 10.0 (feature level 299). Previously theuser_group_edit_policyfield controlled the permission
to manage user groups. Valid values were as follows:1 = All members can create and edit user groups2 = Only organization administrators can create and edit
  user groups3 = Onlyfull memberscan create and
  edit user groups.4 = Only organization administrators and moderators can
  create and edit user groups.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_manage_billing_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the set of
users who have permission to manage plans and billing in the organization.Changes: New in Zulip 10.0 (feature level 363). Previously, only owners
and users withis_billing_adminproperty set totruewere allowed to
manage plans and billing.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_create_public_channel_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining
the set of users who have permission to create public
channels in this organization.Changes: New in Zulip 9.0 (feature level 264). Previouslyrealm_create_public_stream_policyfield used to control the
permission to create public channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_create_private_channel_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining
the set of users who have permission to create private
channels in this organization.Changes: New in Zulip 9.0 (feature level 266). Previouslyrealm_create_private_stream_policyfield used to control the
permission to create private channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_create_web_public_channel_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining
the set of users who have permission to create web-public
channels in this organization.Has no effect and should not be displayed in settings UI
unless the Zulip server has theWEB_PUBLIC_STREAMS_ENABLEDserver-level setting enabled and the organization has enabled
theenable_spectator_accessrealm setting.Changes: New in Zulip 10.0 (feature level 280). Previouslyrealm_create_web_public_stream_policyfield used to control
the permission to create web-public channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_resolve_topics_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining
the set of users who have permission toresolve topicsin the organization.Changes: New in Zulip 10.0 (feature level 367). Previously, permission
to resolve topics was controlled by the more generalcan_move_messages_between_topics_group permission for moving messages.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_create_public_stream_policy:integerPresent ifrealmis present infetch_event_types.A deprecated representation of a superset of the users who
have permission to create public channels in the organization,
available for backwards-compatibility. Clients should usecan_create_public_channel_groupinstead.It is an enum with the following possible values, corresponding
to roles/system groups:1 = Members only2 = Admins only3 =Full membersonly4 = Admins and moderators onlyChanges: Deprecated in Zulip 9.0 (feature level 264) and
replaced byrealm_can_create_public_channel_group, which
supports finer resolution of configurations, resulting in this
property being inaccurate following that transition.Before Zulip 5.0 (feature level 102), permission to create
channels was controlled by therealm_create_stream_policysetting.
- realm_create_private_stream_policy:integerPresent ifrealmis present infetch_event_types.A deprecated representation of a superset of the users who
have permission to create private channels in the organization,
available for backwards-compatibility. Clients should usecan_create_private_channel_groupinstead.It is an enum with the following possible values, corresponding
to roles/system groups:1 = Members only2 = Admins only3 =Full membersonly4 = Admins and moderators onlyChanges: Deprecated in Zulip 9.0 (feature level 266) and
replaced byrealm_can_create_private_channel_group, which
supports finer resolution of configurations, resulting in this
property being inaccurate following that transition.Changes: Before Zulip 5.0 (feature level 102), permission to
create channels was controlled by therealm_create_stream_policysetting.
- realm_create_web_public_stream_policy:integerPresent ifrealmis present infetch_event_types.A deprecated representation of a superset of the users who
have permission to create web-public channels in the
organization, available for backwards-compatibility. Clients
should usecan_create_web_public_channel_groupinstead.It is an enum with the following possible values, corresponding
to roles/system groups:2 = Admins only4 = Admins and moderators only6 = Nobody7 = Owners onlyChanges: Deprecated in Zulip 10.0 (feature level 280) and
replaced byrealm_can_create_web_public_channel_group, which
supports finer resolution of configurations, resulting in this
property being inaccurate following that transition.Changes: Added in Zulip 5.0 (feature level 103).
- realm_wildcard_mention_policy:integerPresent ifrealmis present infetch_event_types.A deprecated representation of a superset of the users who
have permission to use wildcard mentions in large channels,
available for backwards-compatibility. Clients should usecan_mention_many_users_groupinstead.It is an enum with the following possible values, corresponding
to roles/system groups:1 = Any user can use wildcard mentions in large channels.2 = Only members can use wildcard mentions in large channels.3 = Onlyfull memberscan use wildcard mentions in large channels.5 = Only organization administrators can use wildcard mentions in large channels.6 = Nobody can use wildcard mentions in large channels.7 = Only organization administrators and moderators can use wildcard mentions in large channels.All users will receive a warning/reminder when using
mentions in large channels, even when permitted to do so.Changes: Deprecated in Zulip 10.0 (feature level 352) and
replaced byrealm_can_mention_many_users_group, which
supports finer resolution of configurations, resulting in this
property being inaccurate following that transition.Channel administrators option removed in Zulip 6.0 (feature level 133).Moderators option added in Zulip 4.0 (feature level 62).New in Zulip 4.0 (feature level 33).
- realm_default_language:stringPresent ifrealmis present infetch_event_types.Theorganization languagefor automated messages and invitation emails.
- realm_welcome_message_custom_text:stringPresent ifrealmis present infetch_event_types.This organization's configured custom message for Welcome Bot
to send to new user accounts, in Zulip Markdown format.Changes: New in Zulip 11.0 (feature level 416).
- realm_description:stringPresent ifrealmis present infetch_event_types.The description of the organization, used on login and registration pages.
- realm_digest_emails_enabled:booleanPresent ifrealmis present infetch_event_types.Whether the organization has enabledweekly digest emails.
- realm_disallow_disposable_email_addresses:booleanPresent ifrealmis present infetch_event_types.Whether the organization disallows disposable email
addresses.
- realm_email_changes_disabled:booleanPresent ifrealmis present infetch_event_types.Whether users are allowed to change their own email address in this
organization. This is typically disabled for organizations that
synchronize accounts from LDAP or a similar corporate database.
- realm_invite_required:booleanPresent ifrealmis present infetch_event_types.Whether an invitation is required to join this organization.
- realm_create_multiuse_invite_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the
set of users who are allowed to createreusable invitation
linksto the organization.Changes: Prior to Zulip 10.0 (feature level 314), this value used
to be of type integer and did not accept anonymous user groups.New in Zulip 8.0 (feature level 209).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_media_preview_size:integerPresent ifrealmis present infetch_event_types.The organization's policy for the size of image and video
thumbnails in messages, expressed as a percentage of the
default height. Currently, only certain values are permitted.100: 100% height (the default).150: 150% height.200: 200% height.Changes: New in Zulip 12.0 (feature level 469).
- realm_inline_image_preview:booleanPresent ifrealmis present infetch_event_types.Whether this organization has been configured to enablepreviews of linked images.
- realm_inline_url_embed_preview:booleanPresent ifrealmis present infetch_event_types.Whether this organization has been configured to enablepreviews of linked websites.
- realm_topics_policy:stringPresent ifrealmis present infetch_event_types.The organization's default policy for sending channel messages to theempty "general chat" message_topic."allow_empty_topic": Channel messages can be sent to the empty message_topic."disable_empty_topic": Channel messages cannot be sent to the empty message_topic.Changes: New in Zulip 11.0 (feature level 392). Previously, this was
controlled by the booleanrealm_mandatory_topicssetting, which is now
deprecated.
- realm_mandatory_topics:booleanPresent ifrealmis present infetch_event_types.Whethertopics are requiredfor messages in this
organization.Changes: Deprecated in Zulip 11.0 (feature level 392). This is now
controlled by the realmtopics_policysetting.
- realm_message_retention_days:integerPresent ifrealmis present infetch_event_types.The defaultmessage retention policyfor this organization. It can have one special value:-1denoting that the messages will be retained forever for this realm, by default.Changes: Prior to Zulip 3.0 (feature level 22), no limit was
encoded asnullinstead of-1. Clients can correctly handle all
server versions by treating both-1andnullas indicating
unlimited message retention.
- realm_name:stringPresent ifrealmis present infetch_event_types.The name of the organization, used in login pages etc.
- realm_require_e2ee_push_notifications:booleanPresent ifrealmis present infetch_event_types.Whether this realm is configured to disallow sending mobile
push notifications with message content through the legacy
mobile push notifications APIs. The new API uses end-to-end
encryption to protect message content and metadata from
being accessible to the push bouncer service, APNs, and
FCM. Clients that support the new E2EE API will use it
automatically regardless of this setting.Iftrue, mobile push notifications sent to clients that
lack support for E2EE push notifications will always have
"New message" as their content. Note that these legacy
mobile notifications will still contain metadata, which may
include the message's ID, the sender's name, email address,
and avatar.In a future release, once the official mobile apps have
implemented fully validated their E2EE protocol support,
this setting will become strict, and disable the legacy
protocol entirely.Changes: New in Zulip 11.0 (feature level 409). Previously,
this behavior was available only via thePUSH_NOTIFICATION_REDACT_CONTENTglobal server setting.
- realm_require_unique_names:booleanPresent ifrealmis present infetch_event_types.Indicates whether the organization is configured to require users
to have unique full names. If true, the server will reject attempts
to create a new user, or change the name of an existing user, where
doing so would lead to two users whose names are identical modulo
case and unicode normalization.Changes: New in Zulip 9.0 (feature level 246). Previously, the Zulip
server could not be configured to enforce unique names.
- realm_name_changes_disabled:booleanPresent ifrealmis present infetch_event_types.Indicates whether users areallowed to changetheir name
via the Zulip UI in this organization. Typically disabled
in organizations syncing this type of account information from
an external user database like LDAP.
- realm_avatar_changes_disabled:booleanPresent ifrealmis present infetch_event_types.Indicates whether users areallowed to changetheir avatar
via the Zulip UI in this organization. Typically disabled
in organizations syncing this type of account information from
an external user database like LDAP.
- realm_emails_restricted_to_domains:booleanPresent ifrealmis present infetch_event_types.Whethernew users joiningthis organization are required to have an email
address in one of therealm_domainsconfigured for the organization.
- realm_send_channel_events_messages:booleanPresent ifrealmis present infetch_event_types.Indicates whether channel event messages are sent in this organization.Changes: New in Zulip 12.0 (feature level 434). Previously,
channel events were sent unconditionally.
- realm_send_welcome_emails:booleanPresent ifrealmis present infetch_event_types.Whether or not this organization is configured to send the standard Zulipwelcome emailsto new users joining the organization.
- realm_message_content_allowed_in_email_notifications:booleanPresent ifrealmis present infetch_event_types.Whether notification emails in this organization are allowed to
contain Zulip the message content, or simply indicate that a new
message was sent.
- realm_enable_spectator_access:booleanPresent ifrealmis present infetch_event_types.Whether web-public channels and related anonymous access APIs/features
are enabled in this organization.Can only be enabled if theWEB_PUBLIC_STREAMS_ENABLEDserver settingis enabled on the Zulip
server. See also thecan_create_web_public_channel_grouprealm
setting.Changes: New in Zulip 5.0 (feature level 109).
- realm_want_advertise_in_communities_directory:booleanPresent ifrealmis present infetch_event_types.Whether the organization has given permission to be advertised in the
Zulipcommunities directory.Useful only to clients supporting changing this setting for the
organization.Giving permission via this setting does not guarantee that an
organization will be listed in the Zulip communities directory.Changes: New in Zulip 6.0 (feature level 129).
- realm_video_chat_provider:integerPresent ifrealmis present infetch_event_types.The configuredvideo call providerfor the
organization.0 = None1 = Jitsi Meet3 = Zoom (User OAuth integration)4 = BigBlueButton5 = Zoom (Server to Server OAuth integration)6 = Constructor Groups7 = Nextcloud TalkNote that only one of theZoom integrationscan
be configured on a Zulip server.Changes: In Zulip 12.0 (feature level 465), added the
Nextcloud Talk option.In Zulip 12.0 (feature level 460), added the
Constructor Groups option.In Zulip 10.0 (feature level 353), added the Zoom Server
to Server OAuth option.In Zulip 3.0 (feature level 1), added the None option
to disable video call UI.
- realm_jitsi_server_url:string | nullPresent ifrealmis present infetch_event_types.The URL of the custom Jitsi Meet server configured in this organization's
settings.null, the default, means that the organization is using the should use the
server-level configuration,server_jitsi_server_url. A correct client
supporting only the modern API should userealm_jitsi_server_url ||
server_jitsi_server_urlto create calls.Changes: New in Zulip 8.0 (feature level 212). Previously, this was only
available as a server-level configuration, which was available via thejitsi_server_urlfield.
- realm_gif_rating_policy:integerPresent ifrealmis present infetch_event_types.Maximum rating of the GIFs that will be retrieved by the
GIPHY and Tenor integrations in this organization.Changes: Before Zulip 12.0 (feature level 453), this was calledrealm_giphy_rating.Changes: Before Zulip 12.0 (feature level 442), this was only used by
the Giphy integration.New in Zulip 4.0 (feature level 55).
- realm_waiting_period_threshold:integerPresent ifrealmis present infetch_event_types.Members whose accounts have been created at least this many days ago
will be treated asfull membersfor the purpose of settings that restrict access to new members.
- realm_digest_weekday:integerPresent ifrealmis present infetch_event_types.The day of the week when the organization will send
its weekly digest email to inactive users.
- realm_direct_message_initiator_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the set of
users who have permission to start a new direct message conversation
involving other non-bot users. Users who are outside this group and attempt
to send the first direct message to a given collection of recipient users
will receive an error, unless all other recipients are bots or the sender.Changes: New in Zulip 9.0 (feature level 270).Previously, access to send direct messages was controlled by theprivate_message_policyrealm setting, which supported values of
1 (enabled) and 2 (disabled).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_direct_message_permission_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the set of
users who have permission to fully use direct messages. Users outside
this group can only send direct messages to conversations where all the
recipients are in this group, are bots, or are the sender, ensuring that
every direct message conversation will be visible to at least one user in
this group.Changes: New in Zulip 9.0 (feature level 270).Previously, access to send direct messages was controlled by theprivate_message_policyrealm setting, which supported values of
1 (enabled) and 2 (disabled).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_default_code_block_language:stringPresent ifrealmis present infetch_event_types.The default pygments language code to be used for code blocks in this
organization. If an empty string, no default has been set.Changes: Prior to Zulip 8.0 (feature level 195), a server bug meant
that bothnulland an empty string could represent that no default was
set for this realm setting. Clients supporting older server versions
should treat either value (nullor"") as no default being set.
- realm_message_content_delete_limit_seconds:integer | nullPresent ifrealmis present infetch_event_types.Messages sent more than this many seconds ago cannot be deleted
with this organization'smessage deletion policy.Will not be 0. Anullvalue means no limit: messages can be deleted
regardless of how long ago they were sent.Changes: No limit was represented using the
special value0before Zulip 5.0 (feature level 100).
- realm_authentication_methods:objectPresent ifrealmis present infetch_event_types.Dictionary of authentication method keys mapped to dictionaries that
describe the properties of the named authentication method for the
organization - its enabled status and availability for use by the
organization.Clients should use this to implement server-settings UI to change which
methods are enabled for the organization. For authentication UI itself,
clients should use the pre-authentication metadata returned byGET /server_settings.Changes: In Zulip 9.0 (feature level 241), the values in this
dictionary were changed. Previously, the values were a simple boolean
indicating whether the backend is enabled or not.Dictionary describing the properties of an authentication method for the
    organization - its enabled status and availability for use by the
    organization.enabled:booleanBoolean describing whether the authentication method (i.e. its key)
is enabled in this organization.available:booleanBoolean describing whether the authentication method is available for use.
If false, the organization is not eligible to enable the authentication
method.unavailable_reason:stringReason why the authentication method is unavailable. This field is optional
and is only present when 'available' is false.
- realm_allow_message_editing:booleanPresent ifrealmis present infetch_event_types.Whether this organization'smessage edit policyallows editing the content of messages.SeePATCH /messages/{message_id}for details and
history of how message editing permissions work.
- realm_message_content_edit_limit_seconds:integer | nullPresent ifrealmis present infetch_event_types.Messages sent more than this many seconds ago cannot be edited
with this organization'smessage edit policy.Will not be0. Anullvalue means no limit, so messages can be edited
regardless of how long ago they were sent.SeePATCH /messages/{message_id}for details and
history of how message editing permissions work.Changes: Before Zulip 6.0 (feature level 138), no limit was
represented using the special value0.
- realm_move_messages_within_stream_limit_seconds:integer | nullPresent ifrealmis present infetch_event_types.Messages sent more than this many seconds ago cannot be moved within a
channel to another message_topic by users who have permission to do so based on this
organization'stopic edit policy. This
setting does not affect moderators and administrators.Will not be0. Anullvalue means no limit, so message topics can be
edited regardless of how long ago they were sent.SeePATCH /messages/{message_id}for details and
history of how message editing permissions work.Changes: New in Zulip 7.0 (feature level 162). Previously, this time
limit was always 72 hours for users who were not administrators or
moderators.
- realm_move_messages_between_streams_limit_seconds:integer | nullPresent ifrealmis present infetch_event_types.Messages sent more than this many seconds ago cannot be moved between
channels by users who have permission to do so based on this organization'smessage move policy. This setting does
not affect moderators and administrators.Will not be0. Anullvalue means no limit, so messages can be moved
regardless of how long ago they were sent.SeePATCH /messages/{message_id}for details and
history of how message editing permissions work.Changes: New in Zulip 7.0 (feature level 162). Previously, there was
no time limit for moving messages between channels for users with permission
to do so.
- realm_enable_read_receipts:booleanPresent ifrealmis present infetch_event_types.Whether read receipts is enabled in the organization or not.If disabled, read receipt data will be unavailable to clients, regardless
of individual users' personal read receipt settings. See also thesend_read_receiptssetting withinrealm_user_settings_defaults.Changes: New in Zulip 6.0 (feature level 137).
- realm_icon_url:stringPresent ifrealmis present infetch_event_types.The URL of the organization'sprofile icon.
- realm_icon_source:stringPresent ifrealmis present infetch_event_types.String indicating whether the organization'sprofile iconwas uploaded
by a user or is the default. Useful for UI allowing editing the organization's icon."G" means generated by Gravatar (the default)."U" means uploaded by an organization administrator.
- realm_workplace_users_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the set of
users who will be considered as workplace users for billing.Changes: New in Zulip 12.0 (feature level 477).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- max_icon_file_size_mib:integerPresent ifrealmis present infetch_event_types.The maximum file size allowed for the organization's
icon. Useful for UI allowing editing the organization's icon.Changes: New in Zulip 5.0 (feature level 72). Previously,
this was calledmax_icon_file_size.
- realm_logo_url:stringPresent ifrealmis present infetch_event_types.The URL of the organization's wide logo configured in theorganization profile.
- realm_logo_source:stringPresent ifrealmis present infetch_event_types.String indicating whether the organization'sprofile wide logowas uploaded
by a user or is the default. Useful for UI allowing editing the
organization's wide logo."D" means the logo is the default Zulip logo."U" means uploaded by an organization administrator.
- realm_night_logo_url:stringPresent ifrealmis present infetch_event_types.The URL of the organization's dark theme wide-format logo configured in theorganization profile.
- realm_night_logo_source:stringPresent ifrealmis present infetch_event_types.String indicating whether the organization's dark themeprofile wide logowas uploaded
by a user or is the default. Useful for UI allowing editing the
organization's wide logo."D" means the logo is the default Zulip logo."U" means uploaded by an organization administrator.
- max_logo_file_size_mib:integerPresent ifrealmis present infetch_event_types.The maximum file size allowed for the uploaded organization logos.Changes: New in Zulip 5.0 (feature level 72). Previously,
this was calledmax_logo_file_size.
- realm_bot_domain:stringPresent ifrealmis present infetch_event_types.The fake email domain that will be used for new bots created this
organization. Useful for UI for creating bots.
- realm_uri:stringPresent ifrealmis present infetch_event_types.The URL for the organization. Alias ofrealm_url.Changes: Deprecated in Zulip 9.0 (feature level 257). The term
"URI" is deprecated inweb standards.
- realm_url:stringPresent ifrealmis present infetch_event_types.The URL for the organization.Changes: New in Zulip 9.0 (feature level 257), replacing the
deprecatedrealm_uri.
- realm_uuid:stringPresent ifrealmis present infetch_event_types.A unique identifier for the organization, expected to be stable
even if the organization migrates between hosting environments.Used as the salt for Jdenticon avatars; Clients that prefer to compute
Jdenticon avatars may use{realm_uuid}:{user_id}as the Jdenticon key.Changes: New in Zulip 12.0 (feature level 466).
- realm_available_video_chat_providers:objectPresent ifrealmis present infetch_event_types.Dictionary where each entry describes a supportedvideo call
providerthat is configured on this
server and could be selected by an organization administrator.Useful for administrative settings UI that allows changing the realm
settingvideo_chat_provider.{provider_name}:objectDictionary containing the details of the
video call provider with the name of the chat provider as
the key.name:stringThe name of the video call provider.id:integerThe ID of the video call provider.
- realm_presence_disabled:booleanPresent ifrealmis present infetch_event_types.Whether online presence of other users is shown in this
organization.
- settings_send_digest_emails:booleanPresent ifrealmis present infetch_event_types.Whether this Zulip server is configured to allow organizations to
enabledigest emails.Relevant for administrative settings UI that can change the digest
email settings.
- realm_email_auth_enabled:booleanPresent ifrealmis present infetch_event_types.Whether the organization has enabled Zulip's default email and password
authentication feature. Determines whether Zulip stores a password
for the user and clients should offer any UI for changing the user's
Zulip password.
- realm_password_auth_enabled:booleanPresent ifrealmis present infetch_event_types.Whether the organization allows any sort of password-based
authentication (whether via EmailAuthBackend or LDAP passwords).Determines whether a client might ever need to display a password prompt
(clients will primarily look at this attribute inserver_settingsbefore presenting a login page).
- realm_push_notifications_enabled:booleanPresent ifrealmis present infetch_event_types.Whether push notifications are enabled for this organization. Typicallytruefor Zulip Cloud and self-hosted realms that have a valid
registration for theMobile push notifications
service,
andfalsefor self-hosted servers that do not.Changes: Before Zulip 8.0 (feature level 231), this incorrectly wastruefor servers that were partly configured to use the Mobile Push
Notifications Service but not properly registered.
- realm_push_notifications_enabled_end_timestamp:integer | nullPresent ifrealmis present infetch_event_types.If the server expects the realm's push notifications access to end at a
definite time in the future, the UNIX timestamp (UTC) at which this is
expected to happen. Mobile clients should use this field to display warnings
to users when the indicated timestamp is near.Changes: New in Zulip 8.0 (feature level 231).
- realm_upload_quota_mib:integer | nullPresent ifrealmis present infetch_event_types.The total quota for uploaded files in this organization.Clients are not responsible for checking this quota; it is included
in the API only for display purposes.Ifnull, there is no limit.Changes: Before Zulip 9.0 (feature level 251), this field
was incorrectly measured in bytes, not MiB.New in Zulip 5.0 (feature level 72). Previously,
this was calledrealm_upload_quota.
- realm_org_type:integerPresent ifrealmis present infetch_event_types.Theorganization typefor the realm.
Useful only to clients supporting changing this setting for the
organization, or clients implementing onboarding content or
other features that varies with organization type.0 = Unspecified10 = Business20 = Open-source project30 = Education (non-profit)35 = Education (for-profit)40 = Research50 = Event or conference60 = Non-profit (registered)70 = Government80 = Political group90 = Community100 = Personal1000 = OtherChanges: New in Zulip 6.0 (feature level 128).
- realm_owner_full_content_access:booleanPresent ifrealmis present infetch_event_types.Whether the organization's security model allows owners to access
all private content in this organization.Note that this security model configuration can only be changed
via a command-line management command.Changes: New in Zulip 12.0 (feature level 438).
- realm_plan_type:integerPresent ifrealmis present infetch_event_types.The plan type of the organization.1 = Self-hosted organization (SELF_HOSTED)2 = Zulip Cloud free plan (LIMITED)3 = Zulip Cloud Standard plan (STANDARD)4 = Zulip Cloud Standard plan, sponsored for free (STANDARD_FREE)
- realm_enable_guest_user_dm_warning:booleanPresent ifrealmis present infetch_event_types.Whether clients should show a warning when a user is composing
a DM to a guest user in this organization.Changes: New in Zulip 10.0 (feature level 348).
- realm_enable_guest_user_indicator:booleanPresent ifrealmis present infetch_event_types.Whether clients should display "(guest)" after the names of
guest users to prominently highlight their status.Changes: New in Zulip 8.0 (feature level 216).
- realm_can_access_all_users_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the
set of users who are allowed to access all users in the
organization.Changes: Prior to Zulip 10.0 (feature level 314), this value used
to be of type integer and did not accept anonymous user groups.New in Zulip 8.0 (feature level 225).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- realm_can_summarize_topics_group:integer | objectPresent ifrealmis present infetch_event_types.Agroup-setting valuedefining the
set of users who are allowed to use AI summarization.Changes: New in Zulip 10.0 (feature level 350).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- zulip_plan_is_not_limited:booleanPresent ifrealmis present infetch_event_types.Whether the organization is using a limited (Zulip Cloud Free) plan.
- upgrade_text_for_wide_organization_logo:stringPresent ifrealmis present infetch_event_types.Text to use when displaying UI for wide organization logos, a feature
that is currently not available on the Zulip Cloud Free plan.Useful only for clients supporting administrative UI for uploading
a new wide organization logo to brand the organization.
- realm_default_external_accounts:objectPresent ifrealmis present infetch_event_types.Dictionary where each entry describes a default external
account type that can be configured with Zulip'scustom
profile fields feature.Changes: New in Zulip 2.1.0.{site_name}:objectDictionary containing the details of the
default external account provider with the name of the
website as the key.name:stringThe name of the external account providertext:stringThe text describing the external account.hint:stringThe help text to be displayed for the
custom profile field in user-facing
settings UI for configuring custom
profile fields for this account.url_pattern:stringThe regex pattern of the URL of a profile page
on the external site.
- realm_default_avatar_source:stringPresent ifrealmis present infetch_event_types.The avatar data source type for new users."G" = Hosted by Gravatar"J" = Generated using JdenticonNote that "U" is not a supported value here, since there is
no such thing as a "default" user-uploaded avatar.Changes: New in Zulip 12.0 (feature level 456).
- jitsi_server_url:stringPresent ifrealmis present infetch_event_types.The base URL to be used to create Jitsi video calls. Equalsrealm_jitsi_server_url || server_jitsi_server_url.Changes: Deprecated in Zulip 8.0 (feature level 212) and will
eventually be removed. Previously, the Jitsi server to use was not
configurable on a per-realm basis, and this field contained the server's
configured Jitsi server. (Which is now provided asserver_jitsi_server_url). Clients supporting older versions should fall
back to this field when creating calls: usingrealm_jitsi_server_url ||
server_jitsi_server_urlwith newer servers and usingjitsi_server_urlwith servers below feature level 212.
- development_environment:booleanPresent ifrealmis present infetch_event_types.Whether this Zulip server is a development environment. Used
to control certain features or UI (such as error popups)
that should only apply when connected to a Zulip development
environment.
- server_generation:integerPresent ifrealmis present infetch_event_types.A timestamp indicating when the process hosting this
event queue was started. Clients will likely only find
this value useful for inclusion in detailed error reports.
- password_min_length:integerPresent ifrealmis present infetch_event_types.This Zulip server's configured minimum required length for passwords.
Necessary for password change UI to show whether the password
will be accepted.
- password_max_length:integerPresent ifrealmis present infetch_event_types.This Zulip server's configured maximum length for passwords.
Necessary for password change UI to show whether the password
will be accepted.Changes: New in Zulip 10.0 (feature level 338).
- password_min_guesses:integerPresent ifrealmis present infetch_event_types.This Zulip server's configured minimumzxcvbnminimum guesses.
Necessary for password change UI to show whether the password
will be accepted.
- gif_rating_policy_options:objectPresent ifrealmis present infetch_event_types.Dictionary where each entry describes a valid rating configuration
that is available on this server and could be selected by an
organization administrator.Useful for administrative settings UI that allows changing the
allowed rating of GIFs.Changes: Before Zulip 12.0 (feature level 453), this was
calledgif_rating_options.Changes: Before Zulip 12.0 (feature level 442), this was calledgiphy_rating_optionsand only supported the original GIPHY gif picker
integration.giphy_rating_optionswas new in Zulip 4.0 (feature level 55).{rating_name}:objectDictionary containing the details of the
rating with the name of the rating as
the key.name:stringThe description of the rating option.id:integerThe ID of the rating option.
- max_file_upload_size_mib:integerPresent ifrealmis present infetch_event_types.The maximum file size that can be uploaded to this Zulip organization.
- max_avatar_file_size_mib:integerPresent ifrealmis present infetch_event_types.The maximum avatar size that can be uploaded to this Zulip server.
- server_inline_image_preview:booleanPresent ifrealmis present infetch_event_types.Whether the server is configured with support for inline image previews.
Clients containing administrative UI for changingrealm_inline_image_previewshould consult this field before offering
that feature.
- server_inline_url_embed_preview:booleanPresent ifrealmis present infetch_event_types.Whether the server is configured with support for inline URL previews.
Clients containing administrative UI for changingrealm_inline_url_embed_previewshould consult this field before offering
that feature.
- server_thumbnail_formats:(object)[]Present ifrealmis present infetch_event_types.A list describing the image formats that uploaded
images will be thumbnailed into. Any image with a
source starting with/user_uploads/thumbnail/can
have its last path component replaced with any of the
names contained in this list, to obtain the desired
thumbnail size.SeeImages in Markdown messagesfor details of how Zulip renders images, and how
clients should handle them.Changes: New in Zulip 9.0 (feature level 273).name:stringThe file path component of the thumbnail format.max_width:integerThe maximum width of this format.max_height:integerThe maximum height of this format.format:stringThe extension of this format.animated:booleanIf this file format is animated. These formats
are only generated for uploaded images which
themselves are animated.
- server_avatar_changes_disabled:booleanPresent ifrealmis present infetch_event_types.Whether the server allows avatar changes. Similar torealm_avatar_changes_disabledbut based on theAVATAR_CHANGES_DISABLEDZulip server level setting.
- server_name_changes_disabled:booleanPresent ifrealmis present infetch_event_types.Whether the server allows name changes. Similar torealm_name_changes_disabledbut based on theNAME_CHANGES_DISABLEDZulip server level setting.
- server_needs_upgrade:booleanPresent ifrealmis present infetch_event_types.Whether the server is running an old version based on the Zulipserver release lifecycle,
such that the web app will display to the current user a prominent warning.Changes: New in Zulip 5.0 (feature level 74).
- server_web_public_streams_enabled:booleanPresent ifrealmis present infetch_event_types.The value of theWEB_PUBLIC_STREAMS_ENABLEDZulip server level
setting. A server that has disabled this setting intends to not offerweb
public channelsto realms it hosts. (Zulip Cloud
defaults totrue; self-hosted servers default tofalse).Clients should use this to determine whether to offer UI for the
realm-level setting for enabling web-public channels
(realm_enable_spectator_access).Changes: New in Zulip 5.0 (feature level 110).
- server_emoji_data_url:stringPresent ifrealmis present infetch_event_types.The URL to a JSON file that describes which emoji names map to which
emoji codes, for all Unicode emoji this Zulip server accepts.The data at the given URL is a JSON object with one property,code_to_names.
The value of that property is a JSON object where each key is anemoji codefor an available
Unicode emoji, and each value is the correspondingemoji namesfor this emoji,
with the canonical name for the emoji always appearing first.The HTTP response at that URL will have appropriate HTTP caching headers, such
any HTTP implementation should get a cached version if emoji haven't changed
since the last request.Changes: New in Zulip 6.0 (feature level 140).
- server_jitsi_server_url:string | nullPresent ifrealmis present infetch_event_types.The URL of the Jitsi server that the Zulip server is configured to use by
default; the organization-level settingrealm_jitsi_server_urltakes
precedence over this setting when both are set.Changes: New in Zulip 8.0 (feature level 212). Previously, this value
was available as the now-deprecatedjitsi_server_url.
- server_can_summarize_topics:booleanPresent ifrealmis present infetch_event_typesWhether message_topic summarization is enabled in the server or
not depending upon whetherTOPIC_SUMMARIZATION_MODELis set or not.Changes: New in Zulip 10.0 (feature level 350).
- event_queue_longpoll_timeout_seconds:integerPresent ifrealmis present infetch_event_types.Recommended client-side HTTP request timeout forGET /eventscalls.
This is guaranteed to be somewhat greater than the heartbeat frequency. It is important
that clients respect this parameter, so that increases in the heartbeat frequency do not
break clients.Changes: New in Zulip 5.0 (feature level 74). Previously,
this was hardcoded to 90 seconds, and clients should use that as a fallback
value when interacting with servers where this field is not present.
- realm_billing:objectPresent ifrealm_billingis present infetch_event_types.A dictionary containing billing information of the organization.Changes: New in Zulip 10.0 (feature level 363).has_pending_sponsorship_request:booleanWhether there is a pending sponsorship request for the organization. Note that
this field will always befalseif the user is not incan_manage_billing_group.Changes: New in Zulip 10.0 (feature level 363).
- realm_moderation_request_channel_id:integerPresent ifrealmis present infetch_event_types.The ID of the private channel to which messages flagged by users for
moderation are sent. Moderators can use this channel to review and
act on reported content.Will be-1if moderation requests are disabled.Clients should check whether moderation requests are disabled to
determine whether to present a "report message" feature in their UI
within a given organization.Changes: New in Zulip 10.0 (feature level 331). Previously,
no "report message" feature existed in Zulip.
- realm_new_stream_announcements_stream_id:integerPresent ifrealmis present infetch_event_types.The ID of the channel to which automated messages announcing thecreation of new channelsare sent.Will be-1if such automated messages are disabled.Since these automated messages are sent by the server, this field is
primarily relevant to clients containing UI for changing it.Changes: In Zulip 9.0 (feature level 241), renamed 'realm_notifications_stream_id'
torealm_new_stream_announcements_stream_id.
- realm_signup_announcements_stream_id:integerPresent ifrealmis present infetch_event_types.The ID of the channel to which automated messages announcing
thatnew users have joined the organizationare sent.Will be-1if such automated messages are disabled.Since these automated messages are sent by the server, this field is
primarily relevant to clients containing UI for changing it.Changes: In Zulip 9.0 (feature level 241), renamed
'realm_signup_notifications_stream_id' torealm_signup_announcements_stream_id.
- realm_zulip_update_announcements_stream_id:integerPresent ifrealmis present infetch_event_types.The ID of the channel to which automated messages announcing
new features or other end-user updates about the Zulip software are sent.Will be-1if such automated messages are disabled.Since these automated messages are sent by the server, this field is
primarily relevant to clients containing UI for changing it.Changes: New in Zulip 9.0 (feature level 242).
- realm_empty_topic_display_name:stringPresent ifrealmis present infetch_event_types.Clients declaring theempty_topic_nameclient capability
should use the value ofrealm_empty_topic_display_nameto
determine how to display the empty string message_topic.Clients not declaring theempty_topic_nameclient capability
receiverealm_empty_topic_display_namevalue as the message_topic name
replacing empty string.Changes: New in Zulip 10.0 (feature level 334). Previously,
the empty string was not a valid message_topic name.
- realm_user_settings_defaults:objectPresent ifrealm_user_settings_defaultsis present infetch_event_types.A dictionary containing the default values of settings for new users.Changes: New in Zulip 5.0 (feature level 95).twenty_four_hour_time:boolean | nullWhether time should bedisplayed in 24-hour notation.Anullvalue indicates that the client should use the default time
format for the user's locale.Changes: Prior to Zulip 11.0 (feature level 408),nullwas not a valid value for this setting. Note that it was not possible
to actually set the time format tonullat this feature level.New in Zulip 5.0 (feature level 99). This value was previously
available asrealm_default_twenty_four_hour_timein the top-level
response object (only whenrealmwas present infetch_event_types).web_mark_read_on_scroll_policy:integerWhether or not to mark messages as read when the user scrolls through their
feed.1 - Always2 - Only in conversation views3 - NeverChanges: New in Zulip 7.0 (feature level 175). Previously, there was no
way for the user to configure this behavior on the web, and the Zulip web and
desktop apps behaved like the "Always" setting when marking messages as read.web_channel_default_view:integerWeb/desktop app setting controlling the default navigation
behavior when clicking on a channel link.1 - Top message_topic in the channel2 - Channel feed3 - List of topics4 - Top unread message_topic in channelChanges: The "Top unread message_topic in channel" is new in Zulip 11.0
(feature level 401).In Zulip 11.0 (feature level 383), we added a new option "List of topics"
to this setting.New in Zulip 9.0 (feature level 269). Previously, this
was not configurable, and every user had the "Channel feed" behavior.starred_message_counts:booleanWhether clients should display thenumber of starred
messages.receives_typing_notifications:booleanWhether the user is configured to receive typing notifications from
other users. The server will only deliver typing notifications events
to users who for whom this is enabled.Changes: New in Zulip 9.0 (feature level 253). Previously, there were
only options to disable sending typing notifications.web_suggest_update_timezone:booleanWhether the user should be shown an alert, offering to update theirprofile time zone, when the time displayed
for the profile time zone differs from the current time displayed by the
time zone configured on their device.Changes: New in Zulip 10.0 (feature level 329).fluid_layout_width:booleanWhether to use themaximum available screen widthfor the web app's center panel (message feed, recent conversations) on wide screens.high_contrast_mode:booleanThis setting is reserved for use to control variations in Zulip's design
to help visually impaired users.web_font_size_px:integerUser-configured primaryfont-sizefor the web application, in pixels.Changes: New in Zulip 9.0 (feature level 245). Previously, font size was
only adjustable via browser zoom. Note that this setting was not fully
implemented at this feature level.web_line_height_percent:integerUser-configured primaryline-heightfor the web application, in percent, so a
value of 120 represents aline-heightof 1.2.Changes: New in Zulip 9.0 (feature level 245). Previously, line height was
not user-configurable. Note that this setting was not fully implemented at this
feature level.color_scheme:integerControls whichcolor themeto use.1 - Automatic2 - Dark theme3 - Light themeAutomatic detection is implementing using the standardprefers-color-schememedia query.translate_emoticons:booleanWhether totranslate emoticons to emojiin messages the user sends.display_emoji_reaction_users:booleanWhether to display the names of reacting users on a message.When enabled, clients should display the names of reacting
users, rather than a count, for messages with few total
reactions. The ideal cutoff may depend on the space
available for displaying reactions; the official web
application displays names when 3 or fewer total reactions
are present with this setting enabled.Changes: New in Zulip 6.0 (feature level 125).default_language:stringWhatdefault languageto use for the account.This controls both the Zulip UI as well as email notifications sent to the user.The value needs to be a standard language code that the Zulip server has
translation data for; for example,"en"for English or"de"for German.web_home_view:stringThehome viewused when opening a new
Zulip web app window or hitting theEsckeyboard shortcut repeatedly."recent" - Recent conversations view"inbox" - Inbox view"all_messages" - Combined feed viewChanges: Before Zulip 12.0 (feature level 454), the Recent
view had"recent_topics"as its string encoding.New in Zulip 8.0 (feature level 219). Previously, this was
calleddefault_view, which was new in Zulip 4.0 (feature level 42).web_escape_navigates_to_home_view:booleanWhether the escape key navigates to theconfigured home view.Changes: New in Zulip 8.0 (feature level 219). Previously, this
was calledescape_navigates_to_default_view, which was new in Zulip
5.0 (feature level 107).left_side_userlist:booleanWhether the users list on left sidebar in filter_spec windows.This feature is not heavily used and is likely to be reworked.emojiset:stringThe user's configuredemoji set,
used to display emoji to the user everywhere they appear in the UI."google" - Google modern"twitter" - Twitter"text" - Plain textdemote_inactive_streams:integerWhether tohide inactive channelsin the left sidebar.1 - Automatic2 - Always3 - Neveruser_list_style:integerThe style selected by the user for the right sidebar user list.1 - Compact2 - With status3 - With avatar and statusChanges: New in Zulip 6.0 (feature level 141).web_animate_image_previews:stringControls how animated images should be played in the message feed in the web/desktop application."always" - Always play the animated images in the message feed."on_hover" - Play the animated images on hover over them in the message feed."never" - Never play animated images in the message feed.Changes: New in Zulip 9.0 (feature level 275).web_stream_unreads_count_display_policy:integerConfiguration for which channels should be displayed with a numeric unread count in the left sidebar.
Channels that do not have an unread count will have a simple dot indicator for whether there are any
unread messages.1 - All channels2 - Unmuted channels and topics3 - No channelsChanges: New in Zulip 8.0 (feature level 210).hide_ai_features:booleanControls whether user wants AI features like message_topic summarization to
be hidden in all Zulip clients.Changes: New in Zulip 10.0 (feature level 350).web_inbox_show_channel_folders:booleanDetermines whetherchannel foldersare used to organize how conversations with unread messages
are displayed in the web/desktop application's Inbox view.Changes: New in Zulip 12.0 (feature level 431).web_left_sidebar_show_channel_folders:booleanDetermines whetherchannel foldersare used to organize how channels are displayed in the
web/desktop application's left sidebar.Changes: New in Zulip 11.0 (feature level 411).web_left_sidebar_unreads_count_summary:booleanDetermines whether the web/desktop application's left sidebar displays
the unread message count summary.Changes: New in Zulip 11.0 (feature level 398).enable_stream_desktop_notifications:booleanEnable visual desktop notifications for channel messages.enable_stream_email_notifications:booleanEnable email notifications for channel messages.enable_stream_push_notifications:booleanEnable mobile notifications for channel messages.enable_stream_audible_notifications:booleanEnable audible desktop notifications for channel messages.notification_sound:stringNotification sound name.enable_desktop_notifications:booleanEnable visual desktop notifications for direct messages and @-mentions.enable_sounds:booleanEnable audible desktop notifications for direct messages and
@-mentions.enable_offline_email_notifications:booleanEnable email notifications for direct messages and @-mentions received
when the user is offline.enable_offline_push_notifications:booleanEnable mobile notification for direct messages and @-mentions received
when the user is offline.enable_online_push_notifications:booleanEnable mobile notification for direct messages and @-mentions received
when the user is online.enable_followed_topic_desktop_notifications:booleanEnable visual desktop notifications for messages sent to followed topics.Changes: New in Zulip 8.0 (feature level 189).enable_followed_topic_email_notifications:booleanEnable email notifications for messages sent to followed topics.Changes: New in Zulip 8.0 (feature level 189).enable_followed_topic_push_notifications:booleanEnable push notifications for messages sent to followed topics.Changes: New in Zulip 8.0 (feature level 189).enable_followed_topic_audible_notifications:booleanEnable audible desktop notifications for messages sent to followed topics.Changes: New in Zulip 8.0 (feature level 189).enable_digest_emails:booleanEnable digest emails when the user is away.enable_marketing_emails:booleanEnable marketing emails. Has no function outside Zulip Cloud.enable_login_emails:booleanEnable email notifications for new logins to account.message_content_in_email_notifications:booleanInclude the message's content in email notifications for new messages.pm_content_in_desktop_notifications:booleanInclude content of direct messages in desktop notifications.wildcard_mentions_notify:booleanWhether wildcard mentions (E.g. @all) should send notifications
like a personal mention.enable_followed_topic_wildcard_mentions_notify:booleanWhether wildcard mentions (e.g., @all) in messages sent to followed topics
should send notifications like a personal mention.Changes: New in Zulip 8.0 (feature level 189).desktop_icon_count_display:integerUnread count badge (appears in desktop sidebar and browser tab)1 - All unread messages2 - DMs, mentions, and followed topics3 - DMs and mentions4 - NoneChanges: In Zulip 8.0 (feature level 227), addedDMs, mentions,
and followed topicsoption, renumbering the options to insert it in
order.realm_name_in_email_notifications_policy:integerWhether toinclude organization name in subject of message notification
emails.1 - Automatic2 - Always3 - NeverChanges: New in Zulip 7.0 (feature level 168), replacing the
previousrealm_name_in_notificationsboolean;truecorresponded toAlways, andfalsetoNever.automatically_follow_topics_policy:integerWhichtopics to follow automatically.1 - Topics the user participates in2 - Topics the user sends a message to3 - Topics the user starts4 - NeverChanges: New in Zulip 8.0 (feature level 214).automatically_unmute_topics_in_muted_streams_policy:integerWhichtopics to unmute automatically in muted channels.1 - Topics the user participates in2 - Topics the user sends a message to3 - Topics the user starts4 - NeverChanges: New in Zulip 8.0 (feature level 214).automatically_follow_topics_where_mentioned:booleanWhether the server will automatically mark the user as following
topics where the user is mentioned.Changes: New in Zulip 8.0 (feature level 235).resolved_topic_notice_auto_read_policy:stringControls whether the resolved-message_topic notices are marked as read."always" - Always mark resolved-message_topic notices as read."except_followed" - Mark resolved-message_topic notices as read in topics not followed by the user."never" - Never mark resolved-message_topic notices as read.Changes: New in Zulip 11.0 (feature level 385).presence_enabled:booleanDisplay the presence status to other users when online.enter_sends:booleanWhether the user setting forsending on pressing Enterin the compose box is enabled.enable_drafts_synchronization:booleanA boolean parameter to control whether synchronizing drafts is enabled for
the user. When synchronization is disabled, all drafts stored in the server
will be automatically deleted from the server.This does not do anything (like sending events) to delete local copies of
drafts stored in clients.email_notifications_batching_period_seconds:integerThe duration (in seconds) for which the server should wait to batch
email notifications before sending them.available_notification_sounds:(string)[]Array containing the names of the notification sound options
supported by this Zulip server. Only relevant to support UI
for configuring notification sounds.emojiset_choices:(object)[]Array of dictionaries where each dictionary describes an emoji set
supported by this version of the Zulip server.Only relevant to clients with configuration UI for choosing an emoji set;
the currently selected emoji set is available in theemojisetkey.SeePATCH /settingsfor details on
the meaning of this setting.key:stringThe key or the name of the emoji set which will be the value
ofemojisetif this emoji set is chosen.text:stringThe text describing the emoji set.send_private_typing_notifications:booleanWhethertyping notificationsbe sent when composing
direct messages.Changes: New in Zulip 5.0 (feature level 105).send_stream_typing_notifications:booleanWhethertyping notificationsbe sent when composing
channel messages.Changes: New in Zulip 5.0 (feature level 105).send_read_receipts:booleanWhether other users are allowed to see whether you've
read messages.Changes: New in Zulip 5.0 (feature level 105).allow_private_data_export:booleanWhether organization administrators are allowed to
export your private data.Changes: New in Zulip 10.0 (feature level 293).email_address_visibility:integerThepolicyforwhich other usersin this organization can see the user's real email address.1 = Everyone2 = Members only3 = Administrators only4 = Nobody5 = Moderators onlyChanges: New in Zulip 7.0 (feature level 163), replacing the
realm-level setting.web_navigate_to_sent_message:booleanWeb/desktop app setting for whether the user's view should
automatically go to the conversation where they sent a message.Changes: New in Zulip 9.0 (feature level 268). Previously,
this behavior was not configurable.
- realm_users:(object)[]Present ifrealm_useris present infetch_event_types.A array of dictionaries where each entry describes a user
whose account has not been deactivated. Note that unlike
the usual User dictionary, this does not contain theis_activekey, as all the users present in this array have active accounts.If the current user is a guest whose access to users is limited by acan_access_all_users_grouppolicy, and the event queue was registered
with theuser_list_incompleteclient capability, then users that the
current user cannot access will not be included in this array. If the
current user's access to a user is restricted but the client lacks this
capability, then that inaccessible user will appear in the users array as
an "Unknown user" object with the usual format but placeholder data whose
only variable content is the user ID.See alsocross_realm_botsandrealm_non_active_users.Changes: Before Zulip 8.0 (feature level 232), theuser_list_incompleteclient capability did not exist, and so all
clients whose access to a new user was prevented bycan_access_all_users_grouppolicy would receive a fake "Unknown
user" event for such users.user_id:integerThe unique ID of the user.delivery_email:string | nullThe user's real email address. This value will benullif you cannot
access user's real email address. For bot users, this field is always
set to the real email of the bot, because bot users always haveemail_address_visibilityset to everyone.Changes: Prior to Zulip 7.0 (feature level 163), this field was
present only whenemail_address_visibilitywas restricted and you had
access to the user's real email. As of this feature level, this field
is always present, including the case whenemail_address_visibilityis set to everyone (and therefore not restricted).email:stringThe Zulip API email address of the user or bot.If you do not have permission to view the email address of the target user,
this will be a fake email address that is usable for the Zulip API but nothing else.full_name:stringFull name of the user or bot, used for all display purposes.date_joined:stringThe time when the user joined. For users imported from other
applications and users created via the API, this is set to the
account creation time until the user logs in for the first time,
after which it is updated to that login time.For imported users, clients can use theis_imported_stubflag
to determine how to display this field: whenis_imported_stubistrue, the user has not yet logged in and this value is the
account creation time during import; whenis_imported_stubisfalse, this value reflects when the user first logged in.Changes: Starting with Zulip 12.0 (feature level 475),
this field is updated when an imported stub user or a user created
via the API logs in for the first time.is_active:booleanA boolean specifying whether the user account has been deactivated.is_owner:booleanA boolean specifying whether the user is an organization owner.
If true,is_adminwill also be true.Changes: New in Zulip 3.0 (feature level 8).is_admin:booleanA boolean specifying whether the user is an organization administrator.is_guest:booleanA boolean specifying whether the user is a guest user.is_bot:booleanA boolean specifying whether the user is a bot or full account.bot_type:integer | nullAn integer describing the type of bot:nullif the user isn't a bot.1for aGenericbot.2for anIncoming webhookbot.3for anOutgoing webhookbot.4for anEmbeddedbot.bot_owner_id:integer | nullIf the user is a bot (i.e.is_botis true), thenbot_owner_idis the user ID of the bot's owner (usually, whoever created the bot).Will benullfor legacy bots that do not have an owner.Changes: New in Zulip 3.0 (feature level 1). In previous
versions, there was abot_ownerfield containing the email
address of the bot's owner.role:integerOrganization-level roleof the user.
Possible values are:100 = Organization owner200 = Organization administrator300 = Organization moderator400 = Member600 = GuestChanges: New in Zulip 4.0 (feature level 59).timezone:stringThe IANA identifier of the user'sprofile time zone,
which is used primarily to display the user's local time to other users.avatar_url:string | nullURL for the user's avatar.Will benullif theclient_gravatarquery parameter was set totrue, the current user has access to
this user's real email address, and this user's avatar is hosted by
the Gravatar provider (i.e. this user has never uploaded an avatar).Changes: Before Zulip 7.0 (feature level 163), access to a
user's real email address was a realm-level setting. As of this
feature level,email_address_visibilityis a user setting.In Zulip 3.0 (feature level 18), if the client has theuser_avatar_url_field_optionalcapability, this will be missing at
the server's sole discretion.avatar_version:integerVersion for the user's avatar. Used for cache-busting requests
for the user's avatar. Clients generally shouldn't need to use this;
most avatar URLs sent by Zulip will already end with?v={avatar_version}.is_imported_stub:booleanIndicates whether this user object is a stub account imported from
another chat system. Stub accounts are used to represent the senders
for imported messages. Stub accounts can be converted to regular Zulip
accounts when the user starts using Zulip, preserving that imported
user's message history.Changes: New in Zulip 12.0 (feature level 433).profile_data:objectOnly present ifis_botis false; bots can't have custom profile fields.A dictionary containing custom profile field data for the user. Each entry
maps the integer ID of a custom profile field in the organization to a
dictionary containing the user's data for that field. Generally the data
includes just a singlevaluekey; for those custom profile fields
supporting Markdown, arendered_valuekey will also be present.{id}:objectObject with data about what value the user filled in the custom
profile field with that ID.value:stringUser's personal value for this custom profile field.rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- realm_non_active_users:(object)[]Present ifrealm_useris present infetch_event_types.A array of dictionaries where each entry describes a user
whose account has been deactivated. Note that unlike
the usual User dictionary this does not contain theis_activekey as all the users present in this array have deactivated
accounts.user_id:integerThe unique ID of the user.delivery_email:string | nullThe user's real email address. This value will benullif you cannot
access user's real email address. For bot users, this field is always
set to the real email of the bot, because bot users always haveemail_address_visibilityset to everyone.Changes: Prior to Zulip 7.0 (feature level 163), this field was
present only whenemail_address_visibilitywas restricted and you had
access to the user's real email. As of this feature level, this field
is always present, including the case whenemail_address_visibilityis set to everyone (and therefore not restricted).email:stringThe Zulip API email address of the user or bot.If you do not have permission to view the email address of the target user,
this will be a fake email address that is usable for the Zulip API but nothing else.full_name:stringFull name of the user or bot, used for all display purposes.date_joined:stringThe time when the user joined. For users imported from other
applications and users created via the API, this is set to the
account creation time until the user logs in for the first time,
after which it is updated to that login time.For imported users, clients can use theis_imported_stubflag
to determine how to display this field: whenis_imported_stubistrue, the user has not yet logged in and this value is the
account creation time during import; whenis_imported_stubisfalse, this value reflects when the user first logged in.Changes: Starting with Zulip 12.0 (feature level 475),
this field is updated when an imported stub user or a user created
via the API logs in for the first time.is_active:booleanA boolean specifying whether the user account has been deactivated.is_owner:booleanA boolean specifying whether the user is an organization owner.
If true,is_adminwill also be true.Changes: New in Zulip 3.0 (feature level 8).is_admin:booleanA boolean specifying whether the user is an organization administrator.is_guest:booleanA boolean specifying whether the user is a guest user.is_bot:booleanA boolean specifying whether the user is a bot or full account.bot_type:integer | nullAn integer describing the type of bot:nullif the user isn't a bot.1for aGenericbot.2for anIncoming webhookbot.3for anOutgoing webhookbot.4for anEmbeddedbot.bot_owner_id:integer | nullIf the user is a bot (i.e.is_botis true), thenbot_owner_idis the user ID of the bot's owner (usually, whoever created the bot).Will benullfor legacy bots that do not have an owner.Changes: New in Zulip 3.0 (feature level 1). In previous
versions, there was abot_ownerfield containing the email
address of the bot's owner.role:integerOrganization-level roleof the user.
Possible values are:100 = Organization owner200 = Organization administrator300 = Organization moderator400 = Member600 = GuestChanges: New in Zulip 4.0 (feature level 59).timezone:stringThe IANA identifier of the user'sprofile time zone,
which is used primarily to display the user's local time to other users.avatar_url:string | nullURL for the user's avatar.Will benullif theclient_gravatarquery parameter was set totrue, the current user has access to
this user's real email address, and this user's avatar is hosted by
the Gravatar provider (i.e. this user has never uploaded an avatar).Changes: Before Zulip 7.0 (feature level 163), access to a
user's real email address was a realm-level setting. As of this
feature level,email_address_visibilityis a user setting.In Zulip 3.0 (feature level 18), if the client has theuser_avatar_url_field_optionalcapability, this will be missing at
the server's sole discretion.avatar_version:integerVersion for the user's avatar. Used for cache-busting requests
for the user's avatar. Clients generally shouldn't need to use this;
most avatar URLs sent by Zulip will already end with?v={avatar_version}.is_imported_stub:booleanIndicates whether this user object is a stub account imported from
another chat system. Stub accounts are used to represent the senders
for imported messages. Stub accounts can be converted to regular Zulip
accounts when the user starts using Zulip, preserving that imported
user's message history.Changes: New in Zulip 12.0 (feature level 433).profile_data:objectOnly present ifis_botis false; bots can't have custom profile fields.A dictionary containing custom profile field data for the user. Each entry
maps the integer ID of a custom profile field in the organization to a
dictionary containing the user's data for that field. Generally the data
includes just a singlevaluekey; for those custom profile fields
supporting Markdown, arendered_valuekey will also be present.{id}:objectObject with data about what value the user filled in the custom
profile field with that ID.value:stringUser's personal value for this custom profile field.rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- avatar_source:stringPresent ifrealm_useris present infetch_event_types.The avatar data source type for the current user. Valid values are:"G" = Hosted by Gravatar"J" = Generated using Jdenticon"U" = Uploaded by userChanges: The "J" value is new in Zulip 12.0 (feature level 466).
The avatar data source type for the current user.
- avatar_url_medium:stringPresent ifrealm_useris present infetch_event_types.The avatar URL for the current user at 500x500 resolution, appropriate
for use in settings UI showing the user's avatar.
- avatar_url:stringPresent ifrealm_useris present infetch_event_types.The URL of the avatar for the current user at 100x100
resolution. See alsoavatar_url_medium.
- can_create_streams:booleanPresent ifrealm_useris present infetch_event_types.Whether the current user is allowed to create at least one type
of channel with the organization'schannel creation
policy. Its value will
always equalcan_create_public_streams || can_create_private_streams.Changes: Deprecated in Zulip 5.0 (feature level 102), when
the newcreate_private_stream_policyandcreate_public_stream_policyproperties introduced the
possibility that a user could only create one type of channel.This field will be removed in a future release.
- can_create_public_streams:booleanPresent ifrealm_useris present infetch_event_types.Whether the current user is allowed to create public channels with
the organization'schannel creation policy.Changes: New in Zulip 5.0 (feature level 102). In older
versions, the deprecatedcan_create_streamsproperty should be
used to determine whether the user can create public channels.
- can_create_private_streams:booleanPresent ifrealm_useris present infetch_event_types.Whether the current user is allowed to create private channels with
the organization'schannel creation policy.Changes: New in Zulip 5.0 (feature level 102). In older
versions, the deprecatedcan_create_streamsproperty should be
used to determine whether the user can create private channels.
- can_create_web_public_streams:booleanPresent ifrealm_useris present infetch_event_types.Whether the current user is allowed to create public channels with
the organization'schannel creation policy.Note that this will be false if the Zulip server does not have theWEB_PUBLIC_STREAMS_ENABLEDsetting enabled or if the organization has
not enabled theenable_spectator_accessrealm setting.Changes: New in Zulip 5.0 (feature level 103).
- can_subscribe_other_users:booleanPresent ifrealm_useris present infetch_event_types.Whether the current user is allowed to subscribe other users to channels with
the organization'schannels policy.
- can_invite_others_to_realm:booleanPresent ifrealm_useris present infetch_event_types.Whether the current useris allowed to invite othersto the organization.Changes: New in Zulip 4.0 (feature level 51).
- is_admin:booleanPresent ifrealm_useris present infetch_event_types.Whether the current user is at least anorganization administrator.
- is_owner:booleanPresent ifrealm_useris present infetch_event_types.Whether the current user is anorganization owner.Changes: New in Zulip 3.0 (feature level 11).
- is_moderator:booleanPresent ifrealm_useris present infetch_event_types.Whether the current user is at least anorganization moderator.Changes: Prior to Zulip 11.0 (feature level 380), this was only true
for users whose role was exactly the moderator role.New in Zulip 4.0 (feature level 60).
- is_guest:booleanPresent ifrealm_useris present infetch_event_types.Whether the current user is aguest user.
- user_id:integerPresent ifrealm_useris present infetch_event_types.The unique ID for the current user.
- email:stringPresent ifrealm_useris present infetch_event_types.The Zulip API email address for the current user. See alsodelivery_email; these may be the same or different depending
on the user'semail_address_visibilitypolicy.
- delivery_email:stringPresent ifrealm_useris present infetch_event_types.The user's email address, appropriate for UI for changing
the user's email address. See alsoemail.
- full_name:stringPresent ifrealm_useris present infetch_event_types.The full name of the current user.
- cross_realm_bots:(object)[]Present ifrealm_useris present infetch_event_types.Array of dictionaries where each dictionary contains details of
a single cross realm bot. Cross-realm bots are special system bot accounts
like Notification Bot.Most clients will want to combine this withrealm_usersin many
contexts.user_id:integerThe unique ID of the user.delivery_email:string | nullThe user's real email address. This value will benullif you cannot
access user's real email address. For bot users, this field is always
set to the real email of the bot, because bot users always haveemail_address_visibilityset to everyone.Changes: Prior to Zulip 7.0 (feature level 163), this field was
present only whenemail_address_visibilitywas restricted and you had
access to the user's real email. As of this feature level, this field
is always present, including the case whenemail_address_visibilityis set to everyone (and therefore not restricted).email:stringThe Zulip API email address of the user or bot.If you do not have permission to view the email address of the target user,
this will be a fake email address that is usable for the Zulip API but nothing else.full_name:stringFull name of the user or bot, used for all display purposes.date_joined:stringThe time when the user joined. For users imported from other
applications and users created via the API, this is set to the
account creation time until the user logs in for the first time,
after which it is updated to that login time.For imported users, clients can use theis_imported_stubflag
to determine how to display this field: whenis_imported_stubistrue, the user has not yet logged in and this value is the
account creation time during import; whenis_imported_stubisfalse, this value reflects when the user first logged in.Changes: Starting with Zulip 12.0 (feature level 475),
this field is updated when an imported stub user or a user created
via the API logs in for the first time.is_active:booleanA boolean specifying whether the user account has been deactivated.is_owner:booleanA boolean specifying whether the user is an organization owner.
If true,is_adminwill also be true.Changes: New in Zulip 3.0 (feature level 8).is_admin:booleanA boolean specifying whether the user is an organization administrator.is_guest:booleanA boolean specifying whether the user is a guest user.is_bot:booleanA boolean specifying whether the user is a bot or full account.bot_type:integer | nullAn integer describing the type of bot:nullif the user isn't a bot.1for aGenericbot.2for anIncoming webhookbot.3for anOutgoing webhookbot.4for anEmbeddedbot.bot_owner_id:integer | nullIf the user is a bot (i.e.is_botis true), thenbot_owner_idis the user ID of the bot's owner (usually, whoever created the bot).Will benullfor legacy bots that do not have an owner.Changes: New in Zulip 3.0 (feature level 1). In previous
versions, there was abot_ownerfield containing the email
address of the bot's owner.role:integerOrganization-level roleof the user.
Possible values are:100 = Organization owner200 = Organization administrator300 = Organization moderator400 = Member600 = GuestChanges: New in Zulip 4.0 (feature level 59).timezone:stringThe IANA identifier of the user'sprofile time zone,
which is used primarily to display the user's local time to other users.avatar_url:string | nullURL for the user's avatar.Will benullif theclient_gravatarquery parameter was set totrue, the current user has access to
this user's real email address, and this user's avatar is hosted by
the Gravatar provider (i.e. this user has never uploaded an avatar).Changes: Before Zulip 7.0 (feature level 163), access to a
user's real email address was a realm-level setting. As of this
feature level,email_address_visibilityis a user setting.In Zulip 3.0 (feature level 18), if the client has theuser_avatar_url_field_optionalcapability, this will be missing at
the server's sole discretion.avatar_version:integerVersion for the user's avatar. Used for cache-busting requests
for the user's avatar. Clients generally shouldn't need to use this;
most avatar URLs sent by Zulip will already end with?v={avatar_version}.is_imported_stub:booleanIndicates whether this user object is a stub account imported from
another chat system. Stub accounts are used to represent the senders
for imported messages. Stub accounts can be converted to regular Zulip
accounts when the user starts using Zulip, preserving that imported
user's message history.Changes: New in Zulip 12.0 (feature level 433).is_system_bot:booleanWhether the user is a system bot. System bots are special
bot user accounts that are managed by the system, rather than
the organization's administrators.Changes: This field was calledis_cross_realm_botbefore Zulip 5.0 (feature level 83).
- server_report_message_types:(object)[]Present ifrealmis present infetch_event_types.A list of objects where each object describes a supported
report type for themessage reportfeature.Changes: New in Zulip 12.0 (feature level 435).key:stringThe unique ID for the report message type.name:stringThe user-facing string for the report message type, to be
displayed in the report message UI, in the user's language.
Note that the actual report will use the name for this type
in the organization's default language.
- server_supported_permission_settings:objectPresent ifrealmis present infetch_event_types.Metadata detailing the valid values for permission settings that
usegroup-setting values. Clients
should use these data as explained in themain documentationto determine what values to present as possible values for these
settings in UI components.Changes: Before Zulip 10.0 (feature level 326), this part of
the response had a documented-as-unstable format not suitable
for general client use, and should be ignored.New in Zulip 8.0 (feature level 221).realm:objectConfiguration for realm level group permission settings.Configuration for a group permission setting specifying the groups
    to which the setting can be set to and the default values for the
    setting.Changes: Removedallow_owners_groupfield in Zulip 10.0 (feature level 326), as we now
support anonymous user groups. Previously, therole:ownerssystem group was
not offered whenallow_owners_groupwas false.Removed unnecessaryid_field_namefield in Zulip 10.0 (feature level 326). Previously,
this always had the value of"{setting_name}_id"; it was an internal implementation
detail of the server not intended to be included in the API.require_system_group:booleanWhether the setting can only be set to a system user group.allow_internet_group:booleanWhether the setting can be set torole:internetsystem group.allow_nobody_group:booleanWhether the setting can be set torole:nobodysystem group.allow_everyone_group:booleanWhether the setting can be set torole:everyonesystem group.If false, guest users cannot exercise this permission even if they are part of
thegroup-setting valuefor this setting.default_group_name:stringName of the default system group for the setting.For some channel settings, this can also bechannel_creator.
In that case:If the channel'screator_idis notnull, default for the
  setting is an anonymous group with the channel creator as
  the only member.If the channel'screator_idisnull, default for the setting
  isrole:nobodysystem group.Changes: In Zulip 12.0 (feature level 427), renamedstream_creator_or_nobodyvalue tochannel_creator.default_for_system_groups:string | nullName of the default group for the setting for system groups.This is non-null only for group-level settings.allowed_system_groups:(string)[]An array of names of system groups to which the setting can
be set to.If the list is empty, the setting can be set to system groups
based on the other boolean fields.Changes: New in Zulip 8.0 (feature level 225).channel_name:objectConfiguration for channel level group permission settings.Configuration for a group permission setting specifying the groups
    to which the setting can be set to and the default values for the
    setting.Changes: Removedallow_owners_groupfield in Zulip 10.0 (feature level 326), as we now
support anonymous user groups. Previously, therole:ownerssystem group was
not offered whenallow_owners_groupwas false.Removed unnecessaryid_field_namefield in Zulip 10.0 (feature level 326). Previously,
this always had the value of"{setting_name}_id"; it was an internal implementation
detail of the server not intended to be included in the API.require_system_group:booleanWhether the setting can only be set to a system user group.allow_internet_group:booleanWhether the setting can be set torole:internetsystem group.allow_nobody_group:booleanWhether the setting can be set torole:nobodysystem group.allow_everyone_group:booleanWhether the setting can be set torole:everyonesystem group.If false, guest users cannot exercise this permission even if they are part of
thegroup-setting valuefor this setting.default_group_name:stringName of the default system group for the setting.For some channel settings, this can also bechannel_creator.
In that case:If the channel'screator_idis notnull, default for the
  setting is an anonymous group with the channel creator as
  the only member.If the channel'screator_idisnull, default for the setting
  isrole:nobodysystem group.Changes: In Zulip 12.0 (feature level 427), renamedstream_creator_or_nobodyvalue tochannel_creator.default_for_system_groups:string | nullName of the default group for the setting for system groups.This is non-null only for group-level settings.allowed_system_groups:(string)[]An array of names of system groups to which the setting can
be set to.If the list is empty, the setting can be set to system groups
based on the other boolean fields.Changes: New in Zulip 8.0 (feature level 225).group:objectConfiguration for group level group permission settings.Configuration for a group permission setting specifying the groups
    to which the setting can be set to and the default values for the
    setting.Changes: Removedallow_owners_groupfield in Zulip 10.0 (feature level 326), as we now
support anonymous user groups. Previously, therole:ownerssystem group was
not offered whenallow_owners_groupwas false.Removed unnecessaryid_field_namefield in Zulip 10.0 (feature level 326). Previously,
this always had the value of"{setting_name}_id"; it was an internal implementation
detail of the server not intended to be included in the API.require_system_group:booleanWhether the setting can only be set to a system user group.allow_internet_group:booleanWhether the setting can be set torole:internetsystem group.allow_nobody_group:booleanWhether the setting can be set torole:nobodysystem group.allow_everyone_group:booleanWhether the setting can be set torole:everyonesystem group.If false, guest users cannot exercise this permission even if they are part of
thegroup-setting valuefor this setting.default_group_name:stringName of the default system group for the setting.For some channel settings, this can also bechannel_creator.
In that case:If the channel'screator_idis notnull, default for the
  setting is an anonymous group with the channel creator as
  the only member.If the channel'screator_idisnull, default for the setting
  isrole:nobodysystem group.Changes: In Zulip 12.0 (feature level 427), renamedstream_creator_or_nobodyvalue tochannel_creator.default_for_system_groups:string | nullName of the default group for the setting for system groups.This is non-null only for group-level settings.allowed_system_groups:(string)[]An array of names of system groups to which the setting can
be set to.If the list is empty, the setting can be set to system groups
based on the other boolean fields.Changes: New in Zulip 8.0 (feature level 225).
- max_bulk_new_subscription_messages:numberMaximum number of new subscribers for which the server will
respect thesend_new_subscription_messagesparameter whenadding subscribers to a channel.Changes: New in Zulip 11.0 (feature level 397).
- id:integerThe ID of the custom profile field. This will be referenced in the custom
profile fields section of user objects.
- type:integerAn integer indicating the type of the custom profile field, which determines
how it is configured and displayed to users.See theCustom profile fieldsarticle for details on what each type means.1: Short text2: Paragraph3: Dropdown4: Date picker5: Link6: Person picker7: External account8: PronounsChanges: Field type8added in Zulip 6.0 (feature level 151).
- order:integerCustom profile fields are displayed in both settings UI and
UI showing users' profiles in increasingorder.
- name:stringThe name of the custom profile field.
- hint:stringThe help text to be displayed for the custom profile field in user-facing
settings UI for configuring custom profile fields.
- field_data:stringField types 3 (Dropdown) and 7 (External account) support storing
additional configuration for the field type in thefield_dataattribute.For field type 3 (Dropdown), this attribute is a JSON dictionary
defining the choices and the order they will be displayed in the
dropdown UI for individual users to select an option.The interface for field type 7 is not yet stabilized.
- display_in_profile_summary:booleanWhether the custom profile field, display or not on the user card.Must be false forPerson pickerprofile field types.This field is only included when its value istrue.Changes: Before Zulip 12.0 (feature level 476), the
"Paragraph" field type was not supported.New in Zulip 6.0 (feature level 146).
- required:booleanWhether an organization administrator has configured this profile field as
required.Because the required property is mutable, clients cannot assume that a required
custom profile field has a value. The Zulip web application displays a prominent
banner to any user who has not set a value for a required field.Changes: New in Zulip 9.0 (feature level 244).
- editable_by_user:booleanWhether regular users can edit this profile field on their own account.Note that organization administrators can edit custom profile fields for any user
regardless of this setting.Changes: New in Zulip 10.0 (feature level 296).
- use_for_user_matching:booleanWhether this custom profile field should be used to match users in typeahead
suggestions. Only allowed for Short Text and External Accountprofile field types.This field is only included when its value istrue.Changes: New in Zulip 12.0 (feature level 455).
- 1: Short text
- 2: Paragraph
- 3: Dropdown
- 4: Date picker
- 5: Link
- 6: Person picker
- 7: External account
- 8: Pronouns
- {FIELD_TYPE}:objectDictionary which contains the details
of the field type with the field type as the name of the
property itself. The current supported field types are as follows:SHORT_TEXTLONG_TEXTDATEfor date-based fields.SELECTfor a list of options.URLfor links.EXTERNAL_ACCOUNTfor external accounts.USERfor selecting a user for the field.PRONOUNSfor a short text field with convenient typeahead for one's preferred pronouns.Changes:PRONOUNStype added in Zulip 6.0 (feature level 151).id:integerThe ID of the custom profile field type.name:stringThe name of the custom profile field type.
- SHORT_TEXT
- LONG_TEXT
- DATEfor date-based fields.
- SELECTfor a list of options.
- URLfor links.
- EXTERNAL_ACCOUNTfor external accounts.
- USERfor selecting a user for the field.
- PRONOUNSfor a short text field with convenient typeahead for one's preferred pronouns.
- id:integerThe ID of the custom profile field type.
- name:stringThe name of the custom profile field type.
- id:integerThe unique ID of the draft. It will only used whenever the drafts are
fetched. This field should not be specified when the draft is being
created or edited.
- type:stringThe type of the draft. Either unaddressed (empty string),"channel_name",
or"private"(for one-on-one and group direct messages).
- to:(integer)[]An array of the tentative target audience IDs. For channel
messages, this should contain exactly 1 ID, the ID of the
target channel. For direct messages, this should be an array
of target user IDs. For unaddressed drafts, this is ignored,
and clients should send an empty array.
- message_topic:stringFor channel message drafts, the tentative message_topic name. For direct
or unaddressed messages, this will be ignored and should ideally
be the empty string. Should not contain null bytes.
- content:stringThe body of the draft. Should not contain null bytes.
- timestamp:integerA Unix timestamp (seconds only) representing when the draft was
last edited. When creating a draft, this key need not be present
and it will be filled in automatically by the server.
- type:stringThe type of the onboarding step. Valid value is"one_time_notice".Changes: Removed type"hotspot"in Zulip 9.0 (feature level 259).New in Zulip 8.0 (feature level 233).
- name:stringThe name of the onboarding step.
- scheduled_message_id:integerThe unique ID of the scheduled message, which can be used to
modify or delete the scheduled message.This is different from the unique ID that the message will have
after it is sent.
- type:stringThe type of the scheduled message. Either"channel_name"or"private".
- to:integer | (integer)[]The scheduled message's tentative target audience.For channel messages, it will be the unique ID of the target
channel. For direct messages, it will be an array with the
target users' IDs.
- message_topic:stringOnly present iftypeis"channel_name".The message_topic for the channel message.
- content:stringThe content/body of the scheduled message, inZulip-flavored Markdownformat.SeeMarkdown message formattingfor details on Zulip's HTML format.
- rendered_content:stringThe content/body of the scheduled message rendered in HTML.
- scheduled_delivery_timestamp:integerThe UNIX timestamp for when the message will be sent
by the server, in UTC seconds.
- failed:booleanWhether the server has tried to send the scheduled message
and it failed to successfully send.Clients that support unscheduling and editing scheduled messages
should display scheduled messages with"failed": truewith an
indicator that the server failed to send the message at the
scheduled time, so that the user is aware of the failure and can
get the content of the scheduled message.Changes: New in Zulip 7.0 (feature level 181).
- scheduled_message_id:integerThe unique ID of the scheduled message, which can be used to
modify or delete the scheduled message.This is different from the unique ID that the message will have
after it is sent.
- type:stringThe type of the scheduled message. Either"channel_name"or"private".
- to:integer | (integer)[]The scheduled message's tentative target audience.For channel messages, it will be the unique ID of the target
channel. For direct messages, it will be an array with the
target users' IDs.
- message_topic:stringOnly present iftypeis"channel_name".The message_topic for the channel message.
- content:stringThe content/body of the scheduled message, inZulip-flavored Markdownformat.SeeMarkdown message formattingfor details on Zulip's HTML format.
- rendered_content:stringThe content/body of the scheduled message rendered in HTML.
- scheduled_delivery_timestamp:integerThe UNIX timestamp for when the message will be sent
by the server, in UTC seconds.
- failed:booleanWhether the server has tried to send the scheduled message
and it failed to successfully send.Clients that support unscheduling and editing scheduled messages
should display scheduled messages with"failed": truewith an
indicator that the server failed to send the message at the
scheduled time, so that the user is aware of the failure and can
get the content of the scheduled message.Changes: New in Zulip 7.0 (feature level 181).
- id:integerThe ID of the muted user.
- timestamp:integerAn integer UNIX timestamp representing when the user was muted.

```
slim_presence
```
- Will be one of these two formats (modern or legacy) for user
    presence data:{user_id}:objectPresence data (modern format) for the user with
the specified ID.active_timestamp:integerThe UNIX timestamp of the last time a client connected
to Zulip reported that the user was actually present
(e.g. via focusing a browser window or interacting
with a computer running the desktop app).Clients should display users with a currentactive_timestampas fully present.idle_timestamp:integerThe UNIX timestamp of the last time the user had a
client connected to Zulip, including idle clients
where the user hasn't interacted with the system
recently.The Zulip server has no way of distinguishing whether
an idle web app user is at their computer, but hasn't
interacted with the Zulip tab recently, or simply left
their desktop computer on when they left.Thus, clients should display users with a currentidle_timestampbut no currentactive_timestampas
potentially present.{user_email}:objectPresence data (legacy format) for the user with
the specified Zulip API email.{client_name}or"aggregated":objectObject containing the details of the user's
presence.Changes: Starting with Zulip 7.0 (feature level 178), this will always
contain two keys,"website"and"aggregated", with identical data. The
server no longer stores which client submitted presence updates.Previously, the{client_name}keys for these objects were the names of the
different clients where the user was logged in, for examplewebsiteorZulipDesktop.client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this will
always be"website"as the server no longer stores which client
submitted presence data.status:stringThe status of the user on this client. Will be either"idle"or"active".timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Not present in objects with the"aggregated"key.Changes: Starting with Zulip 7.0 (feature level 178), alwaysfalsewhen present as the server no longer stores which client
submitted presence data.
- {user_id}:objectPresence data (modern format) for the user with
the specified ID.active_timestamp:integerThe UNIX timestamp of the last time a client connected
to Zulip reported that the user was actually present
(e.g. via focusing a browser window or interacting
with a computer running the desktop app).Clients should display users with a currentactive_timestampas fully present.idle_timestamp:integerThe UNIX timestamp of the last time the user had a
client connected to Zulip, including idle clients
where the user hasn't interacted with the system
recently.The Zulip server has no way of distinguishing whether
an idle web app user is at their computer, but hasn't
interacted with the Zulip tab recently, or simply left
their desktop computer on when they left.Thus, clients should display users with a currentidle_timestampbut no currentactive_timestampas
potentially present.
- {user_email}:objectPresence data (legacy format) for the user with
the specified Zulip API email.{client_name}or"aggregated":objectObject containing the details of the user's
presence.Changes: Starting with Zulip 7.0 (feature level 178), this will always
contain two keys,"website"and"aggregated", with identical data. The
server no longer stores which client submitted presence updates.Previously, the{client_name}keys for these objects were the names of the
different clients where the user was logged in, for examplewebsiteorZulipDesktop.client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this will
always be"website"as the server no longer stores which client
submitted presence data.status:stringThe status of the user on this client. Will be either"idle"or"active".timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Not present in objects with the"aggregated"key.Changes: Starting with Zulip 7.0 (feature level 178), alwaysfalsewhen present as the server no longer stores which client
submitted presence data.
- active_timestamp:integerThe UNIX timestamp of the last time a client connected
to Zulip reported that the user was actually present
(e.g. via focusing a browser window or interacting
with a computer running the desktop app).Clients should display users with a currentactive_timestampas fully present.
- idle_timestamp:integerThe UNIX timestamp of the last time the user had a
client connected to Zulip, including idle clients
where the user hasn't interacted with the system
recently.The Zulip server has no way of distinguishing whether
an idle web app user is at their computer, but hasn't
interacted with the Zulip tab recently, or simply left
their desktop computer on when they left.Thus, clients should display users with a currentidle_timestampbut no currentactive_timestampas
potentially present.
- {client_name}or"aggregated":objectObject containing the details of the user's
presence.Changes: Starting with Zulip 7.0 (feature level 178), this will always
contain two keys,"website"and"aggregated", with identical data. The
server no longer stores which client submitted presence updates.Previously, the{client_name}keys for these objects were the names of the
different clients where the user was logged in, for examplewebsiteorZulipDesktop.client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this will
always be"website"as the server no longer stores which client
submitted presence data.status:stringThe status of the user on this client. Will be either"idle"or"active".timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Not present in objects with the"aggregated"key.Changes: Starting with Zulip 7.0 (feature level 178), alwaysfalsewhen present as the server no longer stores which client
submitted presence data.
- client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this will
always be"website"as the server no longer stores which client
submitted presence data.
- status:stringThe status of the user on this client. Will be either"idle"or"active".
- timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.
- pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Not present in objects with the"aggregated"key.Changes: Starting with Zulip 7.0 (feature level 178), alwaysfalsewhen present as the server no longer stores which client
submitted presence data.
- domain:stringThe new allowed domain.
- allow_subdomains:booleanWhether subdomains are allowed for this domain.
- {emoji_id}:objectObject containing details about the emoji with
the specified ID. It has the following properties:id:stringThe ID for this emoji, same as the object's key.name:stringThe user-friendly name for this emoji. Users in the organization
can use this emoji by writing this name between colons (:name :).source_url:stringThe path relative to the organization's URL where the
emoji's image can be found.still_url:string | nullOnly non-null when the emoji's image is animated.The path relative to the organization's URL where a still
(not animated) version of the emoji can be found. (This is
currently always the first frame of the animation).This is useful for clients to display the emoji in contexts
where continuously animating it would be a bad user experience
(E.g. because it would be distracting).Changes: New in Zulip 5.0 (added as optional field in
feature level 97 and then made mandatory, but nullable, in
feature level 113).deactivated:booleanWhether the emoji has been deactivated or not.author_id:integer | nullThe user ID of the user who uploaded the custom emoji.
Will benullif the uploader is unknown.Changes: New in Zulip 3.0 (feature level 7). Previously
was accessible via anauthorobject with anidfield.
- id:stringThe ID for this emoji, same as the object's key.
- name:stringThe user-friendly name for this emoji. Users in the organization
can use this emoji by writing this name between colons (:name :).
- source_url:stringThe path relative to the organization's URL where the
emoji's image can be found.
- still_url:string | nullOnly non-null when the emoji's image is animated.The path relative to the organization's URL where a still
(not animated) version of the emoji can be found. (This is
currently always the first frame of the animation).This is useful for clients to display the emoji in contexts
where continuously animating it would be a bad user experience
(E.g. because it would be distracting).Changes: New in Zulip 5.0 (added as optional field in
feature level 97 and then made mandatory, but nullable, in
feature level 113).
- deactivated:booleanWhether the emoji has been deactivated or not.
- author_id:integer | nullThe user ID of the user who uploaded the custom emoji.
Will benullif the uploader is unknown.Changes: New in Zulip 3.0 (feature level 7). Previously
was accessible via anauthorobject with anidfield.

```
PATCH
/realm/linkifiers
```

```
client_capabilities
```
- pattern:stringThePython regular expressionpattern which represents the pattern that should be linkified on matching.
- url_template:stringTheRFC 6570compliant URL
template with which the pattern matching string should be linkified.Changes: New in Zulip 7.0 (feature level 176). This replacedurl_format,
which contained a URL format string.
- id:integerThe ID of the linkifier.
- id:integerThe unique ID for the realm playground.
- name:stringThe user-visible display name of the playground. Clients
should display this in UI for picking which playground to
open a code block in, to differentiate between multiple
configured playground options for a given pygments
language.Changes: New in Zulip 4.0 (feature level 49).
- pygments_language:stringThe name of the Pygments language lexer for that
programming language.
- url_template:stringTheRFC 6570compliant URL template for the playground. The template contains
exactly one variable namedcode, which determines how the
extracted code should be substituted in the playground URL.Changes: New in Zulip 8.0 (feature level 196). This replaced theurl_prefixparameter, which was used to construct URLs by just
concatenating url_prefix and code.
- name:stringThe name of the user group.
- date_created:integer | nullThe UNIX timestamp for when the user group was created, in UTC seconds.Anullvalue means the user group has no recorded date, which is often
because the user group is very old, or because it was created via a data
import tool ormanagement command.Changes: New in Zulip 10.0 (feature level 292).
- creator_id:integer | nullThe ID of the user who created this user group.Anullvalue means the user group has no recorded creator, which is often
because the user group is very old, or because it was created via a data
import tool ormanagement command.Changes: New in Zulip 10.0 (feature level 292).
- description:stringThe description of the user group.
- members:(integer)[]Array containing the ID of the users who are
members of this user group.Changes: Prior to Zulip 10.0 (feature level 303), this
list also included deactivated users who were members of
the user group before being deactivated.
- direct_subgroup_ids:(integer)[]Array containing the ID of the direct_subgroups of
this user group.Changes: New in Zulip 6.0 (feature level 131).
Introduced in feature level 127 assubgroups, but
clients can ignore older events as this feature level
predates subgroups being fully implemented.
- id:integerThe ID of the user group.
- is_system_group:booleanWhether the user group is a system group which cannot be
directly modified by users.Changes: New in Zulip 5.0 (feature level 93).
- can_add_members_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to add members to this user group.Changes: New in Zulip 10.0 (feature level 305). Previously, this
permission was controlled by thecan_manage_groupsetting.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_join_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to join this user group.Changes: New in Zulip 10.0 (feature level 301).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_leave_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to leave this user group.Changes: New in Zulip 10.0 (feature level 308).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_manage_group:integer | objectAgroup-setting valuedefining the set of users who
have permission tomanage this user group.Changes: New in Zulip 10.0 (feature level 283).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_mention_group:integer | objectAgroup-setting valuedefining the set of users who
have permission tomention this user group.Changes: Before Zulip 9.0 (feature level 258), this setting was
always the integer form of agroup-setting value.Before Zulip 8.0 (feature level 198), this setting was namedcan_mention_group_id.New in Zulip 8.0 (feature level 191). Previously, groups could be
mentioned only if they were notsystem groups.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_remove_members_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to remove members from this user group.Changes: New in Zulip 10.0 (feature level 324). Previously, this
permission was controlled by thecan_manage_groupsetting.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- deactivated:booleanWhether the user group is deactivated. Deactivated groups
cannot be used as a subgroup of another group or used for
any other purpose.Changes: New in Zulip 10.0 (feature level 290).
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.

```
GET /bots/{bot_id}/api_key
```
- user_id:integerThe user ID of the bot.
- default_sending_stream:string | nullThe default sending channel of the bot. Ifnull, the bot doesn't
have a default sending channel.
- default_events_register_stream:string | nullThe default channel for which the bot receives events/register data.
Ifnull, the bot doesn't have such a default channel.
- default_all_public_streams:booleanWhether the bot can send messages to all channels by default.
- services:(object | object)[]An array containing extra configuration fields only relevant for
outgoing webhook bots and embedded bots. This is always a single-element
array.We consider this part of the Zulip API to be unstable; it is used only
for UI elements for administering bots and is likely to change.When the bot is an outgoing webhook.base_url:stringThe URL the outgoing webhook is configured to post to.token:stringA unique token that the third-party service can use to confirm
that the request is indeed coming from Zulip.interface:integerAn integer indicating what format requests are posted in:1 = Zulip's native outgoing webhook format.2 = Emulate the Slack outgoing webhook format.When the bot is an embedded bot.service_name:stringThe name of the bot.config_data:objectA dictionary of string key/value pairs, which describe the configuration
for the bot. These are usually details like API keys, and are unique to
the integration/bot. Can be an empty dictionary.{config_key}:stringDescription/value of the configuration data key.
- When the bot is an outgoing webhook.base_url:stringThe URL the outgoing webhook is configured to post to.token:stringA unique token that the third-party service can use to confirm
that the request is indeed coming from Zulip.interface:integerAn integer indicating what format requests are posted in:1 = Zulip's native outgoing webhook format.2 = Emulate the Slack outgoing webhook format.
- When the bot is an embedded bot.service_name:stringThe name of the bot.config_data:objectA dictionary of string key/value pairs, which describe the configuration
for the bot. These are usually details like API keys, and are unique to
the integration/bot. Can be an empty dictionary.{config_key}:stringDescription/value of the configuration data key.
- base_url:stringThe URL the outgoing webhook is configured to post to.
- token:stringA unique token that the third-party service can use to confirm
that the request is indeed coming from Zulip.
- interface:integerAn integer indicating what format requests are posted in:1 = Zulip's native outgoing webhook format.2 = Emulate the Slack outgoing webhook format.
- 1 = Zulip's native outgoing webhook format.
- 2 = Emulate the Slack outgoing webhook format.
- service_name:stringThe name of the bot.
- config_data:objectA dictionary of string key/value pairs, which describe the configuration
for the bot. These are usually details like API keys, and are unique to
the integration/bot. Can be an empty dictionary.{config_key}:stringDescription/value of the configuration data key.
- {config_key}:stringDescription/value of the configuration data key.
- name:stringThe name of the bot.
- config:objectA dictionary of string key/value pairs, which describe the configuration
for the bot. These are usually details like API keys, and are unique to
the integration/bot. Can be an empty dictionary.{config_key}:stringDescription/value of the configuration data key.
- {config_key}:stringDescription/value of the configuration data key.
- name:stringA machine-readable unique name identifying the integration, all-lower-case without
spaces.
- display_name:stringA human-readable display name identifying the integration that this bot implements,
intended to be used in menus for selecting which integration to create.Changes: New in Zulip 8.0 (feature level 207).
- all_event_types:(string)[]For incoming webhook integrations that support the Zulip server filtering incoming
events, the list of event types supported by it.A null value will be present if this incoming webhook integration doesn't support
such filtering.Changes: New in Zulip 8.0 (feature level 207).
- config_options:(object)[]An array of configuration options that can be set when creating
a bot user for this incoming webhook integration.This is an unstable API. Please discuss in chat.zulip.org before
using it.Changes: As of Zulip 11.0 (feature level 403), this
object is reserved for integration-specific configuration options
that can be set when creating a bot user. Previously, this object
also included optional webhook URL parameters, which are now
specified in theurl_optionsobject.Before Zulip 10.0 (feature level 318), this field was namedconfig,
and was reserved for configuration data key-value pairs.key:stringA key for the configuration option.label:stringA human-readable label of the configuration option.validator:stringThe name of the validator function for the configuration
option.
- url_options:(object)[]An array of optional URL parameter options for the incoming webhook
integration. In the web app, these are used whengenerating a URL for an integration.This is an unstable API expected to be used only by the Zulip web
app. Please discuss in chat.zulip.org before using it.Changes: New in Zulip 11.0 (feature level 403). Previously,
these optional URL parameter options were included in theconfig_optionsobject.key:stringThe parameter variable to encode the users input for this
option in the integrations webhook URL.label:stringA human-readable label of the url option.validator:stringThe name of the validator function for the configuration
option.
- key:stringA key for the configuration option.
- label:stringA human-readable label of the configuration option.
- validator:stringThe name of the validator function for the configuration
option.
- key:stringThe parameter variable to encode the users input for this
option in the integrations webhook URL.
- label:stringA human-readable label of the url option.
- validator:stringThe name of the validator function for the configuration
option.
- max_message_id:integerThe highest message ID of the conversation, intended to support sorting
the conversations by recency.
- user_ids:(integer)[]The list of users other than the current user in the direct message
conversation. This will be an empty list for direct messages sent to
oneself.
- fragment:stringA unique identifier for the view, used to determine navigation
behavior when clicked.Clients should use this value to navigate to the corresponding URL hash.
- is_pinned:booleanDetermines whether the view appears directly in the sidebar or
is hidden in the "More Views" menu.true- Pinned and visible in the sidebar.false- Hidden and accessible via the "More Views" menu.
- name:string | nullThe user-facing name for custom navigation views. Omit this
field for built-in views.
- true- Pinned and visible in the sidebar.
- false- Hidden and accessible via the "More Views" menu.
- id:integerThe unique ID of the saved snippet.
- title:stringThe title of the saved snippet.
- content:stringThe content of the saved snippet inZulip-flavored Markdownformat.Clients should insert this content into a message when using
a saved snippet.
- date_created:integerThe UNIX timestamp for when the saved snippet was created, in
UTC seconds.
- stream_id:integerThe unique ID of a channel.
- name:stringThe name of a channel.
- description:stringThedescriptionof the channel inZulip-flavored Markdownformat,
intended to be used to prepopulate UI for editing a channel's
description.SeeMarkdown message formattingfor details on Zulip's HTML format.See alsorendered_description.
- rendered_description:stringThedescriptionof the channel rendered as HTML, intended to
be used when displaying the channel description in a UI.One should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax
work correctly. And any client-side security logic for
user-generated message content should be applied when displaying
this HTML as though it were the body of a Zulip message.See alsodescription.
- date_created:integerThe UNIX timestamp for when the channel was created, in UTC seconds.Changes: New in Zulip 4.0 (feature level 30).
- creator_id:integer | nullThe ID of the user who created this channel.Anullvalue means the channel has no recorded creator, which is often
because the channel is very old, was created during realm creation or
because it was created via a data import tool ormanagement command.Changes: New in Zulip 9.0 (feature level 254).
- invite_only:booleanSpecifies whether the channel is private or not.
Only people who have been invited can access a private channel.
- subscribers:(integer)[]A list of user IDs of users who are also subscribed
to a given channel. Included only ifinclude_subscribersistrue.
- partial_subscribers:(integer)[]Ifinclude_subscribers="partial"was requested, the server may, at its discretion, send apartial_subscriberslist rather than asubscriberslist
for channels with a large number of subscribers.Thepartial_subscriberslist contains an arbitrary
subset of the channel's subscribers that is guaranteed
to include all bot user subscribers as well as all
users who have been active in the last 14 days, but
otherwise can be chosen arbitrarily by the server.Changes: New in Zulip 11.0 (feature level 412).
- desktop_notifications:boolean | nullA boolean specifying whether desktop notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_desktop_notifications, for
this channel.
- email_notifications:boolean | nullA boolean specifying whether email notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_email_notifications, for
this channel.
- wildcard_mentions_notify:boolean | nullA boolean specifying whether wildcard mentions
trigger notifications as though they were personal
mentions in this channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting, wildcard_mentions_notify, for
this channel.
- push_notifications:boolean | nullA boolean specifying whether push notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_push_notifications, for
this channel.
- audible_notifications:boolean | nullA boolean specifying whether audible notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_audible_notifications, for
this channel.
- pin_to_top:booleanA boolean specifying whether the given channel has been pinned
to the top.
- is_muted:booleanWhether the user has muted the channel. Muted channels do
not count towards your total unread count and do not show
up in theCombined feedview (previously known asAll messages).Changes: Prior to Zulip 2.1.0, this feature was
represented by the more confusingly namedin_home_view(with the
opposite value,in_home_view=!is_muted).
- in_home_view:booleanLegacy property for if the given channel is muted, with inverted meaning.Changes: Deprecated in Zulip 2.1.0. Clients should useis_mutedwhere available.
- is_announcement_only:booleanWhether only organization administrators can post to the channel.Changes: Deprecated in Zulip 3.0 (feature level 1). Clients
should usestream_post_policyinstead.
- is_web_public:booleanWhether the channel has been configured to allow unauthenticated
access to its message history from the web.
- color:stringThe user's personal color for the channel.
- stream_post_policy:integerA deprecated representation of a superset of the users who
have permission to post messages to the channel available
for backwards-compatibility. Clients should usecan_send_message_groupinstead.It is an enum with the following possible values, corresponding
to roles/system groups:1 = Any user can post.2 = Only administrators can post.3 = Onlyfull memberscan post.4 = Only moderators can post.Changes: Deprecated in Zulip 10.0 (feature level 333) and
replaced bycan_send_message_group, which supports finer
resolution of configurations, resulting in this property being
inaccurate following that transition.New in Zulip 3.0 (feature level 1), replacing the previousis_announcement_onlyboolean.
- message_retention_days:integer | nullNumber of days that messages sent to this channel will be stored
before being automatically deleted by themessage retention
policy. There are two special values:null, the default, means the channel will inherit the organization
  level setting.-1encodes retaining messages in this channel forever.Changes: New in Zulip 3.0 (feature level 17).
- history_public_to_subscribers:booleanWhether the history of the channel is public to its subscribers.Currently always true for public channels (i.e."invite_only": falseimplies"history_public_to_subscribers": true), but clients should not make that
assumption, as we may change that behavior in the future.
- first_message_id:integer | nullThe ID of the first message in the channel.Intended to help clients determine whether they need to display
UI like the "show all topics" widget that would suggest the channel
has older history that can be accessed.Isnullfor channels with no message history.
- folder_id:integer | nullThe ID of the folder to which the channel belongs.Isnullif channel does not belong to any folder.Changes: New in Zulip 11.0 (feature level 389).
- topics_policy:stringWhethernamed topicsand the empty
message_topic (i.e.,"general chat" message_topic)
are enabled in this channel."inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty message_topic in this
  channel."allow_empty_topic": Messages can be sent to both named topics and
  the empty message_topic in this channel."disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty message_topic is disabled."empty_topic_only": Messages can be sent to the empty message_topic in this
  channel, but named topics are disabled. See"general chat"
  channels.The"empty_topic_only"policy can only be set if all existing messages
in the channel are already in the empty message_topic.When creating a new channel, if thetopics_policyis not specified, the"inherit"option will be set.Changes: In Zulip 11.0 (feature level 404), the"empty_topic_only"option was added.New in Zulip 11.0 (feature level 392).
- is_recently_active:booleanWhether the channel has recent message activity. Clients should use this to implementhiding inactive channels.Changes: New in Zulip 10.0 (feature level 323). Previously, clients implemented the
demote_inactive_streams from local message history, resulting in a choppy loading
experience.
- stream_weekly_traffic:integer | nullThe average number of messages sent to the channel per week, as
estimated based on recent weeks, rounded to the nearest integer.Ifnull, the channel was recently created and there is
insufficient data to estimate the average traffic.
- can_add_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to add subscribers to this channel.Users who can administer the channel or have similar realm-level
permissions can add subscribers to a public channel regardless
of the value of this setting.Users in this group need not be subscribed to a private channel to
add subscribers to it.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 342). Previously, there was no
channel-level setting for this permission.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_remove_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to remove subscribers from this channel.Organization administrators can unsubscribe others from a channel as though
they were in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349), channel administrators
could not unsubscribe other users if they were not an organization
administrator or part ofcan_remove_subscribers_group. Realm administrators
were not allowed to unsubscribe other users from a private channel if they
were not subscribed to that channel.Prior to Zulip 10.0 (feature level 320), this value was always the integer
ID of a system group.Before Zulip 8.0 (feature level 197), thecan_remove_subscribers_groupsetting was namedcan_remove_subscribers_group_id.New in Zulip 6.0 (feature level 142).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_administer_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to administer this channel.Organization administrators can administer every channel as though they were
in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349) a user needed tohave content accessto a channel in
order to modify it. The exception to this rule was that organization
administrators can edit channel names and descriptions without
having full access to the channel.New in Zulip 10.0 (feature level 325). Prior to this
change, the permission to administer channels was limited to realm
administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_delete_any_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete any message in the channel.Note that a user musthave content accessto a
channel in order to delete any message in the channel.Users present in the organization-levelcan_delete_any_message_groupsetting can always delete any message in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users incan_delete_any_message_groupwere able
delete any message in the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_delete_own_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete the messages that they have sent in the channel.Note that a user musthave content accessto a
channel in order to delete their own message in the channel.Users with permission to delete any message in the channel
and users present in the organization-levelcan_delete_own_message_groupsetting
can always delete their own messages in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users in the organization-levelcan_delete_any_message_groupandcan_delete_own_message_groupsettings were able delete their own messages in
the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_move_messages_out_of_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages out of this channel.Note that a user musthave content accessto a
channel in order to move messages out of the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_channels_groupsetting can always move messages
out of the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_channels_groupwere able
move messages between channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_move_messages_within_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages within this channel.Note that a user musthave content accessto a
channel in order to move messages within the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_topics_groupsetting can always move messages
within the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_topics_groupwere able
move messages between topics of a channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_send_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to post in this channel.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Note that using this permission to send a message to a new message_topic requires
also having permission to create new topics in the channel.Changes: New in Zulip 10.0 (feature level 333). Previouslystream_post_policyfield used to control the permission to
post in the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_subscribe_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to subscribe themselves to this channel.Everyone, excluding guests, can subscribe to any public channel
irrespective of this setting.Users in this group can subscribe to a private channel as well.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 357).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_resolve_topics_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to resolve topics in the channel.Users who have similar realm-level permissions can resolve topics
in a channel regardless of the value of this setting.Changes: New in Zulip 11.0 (feature level 402).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_create_topic_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to create a new message_topic in this channel.Note that using this permission requires also having permission to
send messages in the channel.Note that this must be therole:everyonesystem groupforprivate channels with protected history.Changes: New in Zulip 12.0 (feature level 441). Previously,
if you could send messages in a channel, you could create topics in
the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- is_archived:booleanA boolean indicating whether the channel isarchived.Changes: New in Zulip 10.0 (feature level 315).
Previously, subscriptions only included active
channels. Note that some endpoints will never return archived
channels unless the client declares explicit support for
them via thearchived_channelsclient capability.
- subscriber_count:numberThe total number of non-deactivated users (including bots) who
are subscribed to the channel. Clients are responsible for updating
this value usingpeer_addandpeer_removeevents.The server's internals cannot guarantee this value is correctly
synced withpeer_addandpeer_removeevents for the channel. As
a result, if a (rare) race occurs between a change in the channel's
subscribers and fetching this value, it is possible for a client
that is correctly following the events protocol to end up with a
permanently off-by-one error in the channel's subscriber count.Clients are recommended to fetch full subscriber data for a channel
in contexts where it is important to avoid this risk. The official
web application, for example, uses this field primarily while
waiting to fetch a given channel's full subscriber list from the
server.Changes: New in Zulip 11.0 (feature level 394).

```
include_subscribers="partial"
```
- 1 = Any user can post.
- 2 = Only administrators can post.
- 3 = Onlyfull memberscan post.
- 4 = Only moderators can post.
- null, the default, means the channel will inherit the organization
  level setting.
- -1encodes retaining messages in this channel forever.
- "inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty message_topic in this
  channel.
- "allow_empty_topic": Messages can be sent to both named topics and
  the empty message_topic in this channel.
- "disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty message_topic is disabled.
- "empty_topic_only": Messages can be sent to the empty message_topic in this
  channel, but named topics are disabled. See"general chat"
  channels.

```
realm_topics_policy
```
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- stream_id:integerThe unique ID of a channel.
- name:stringThe name of a channel.
- description:stringThedescriptionof the channel inZulip-flavored Markdownformat,
intended to be used to prepopulate UI for editing a channel's
description.SeeMarkdown message formattingfor details on Zulip's HTML format.See alsorendered_description.
- rendered_description:stringThedescriptionof the channel rendered as HTML, intended to
be used when displaying the channel description in a UI.One should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax
work correctly. And any client-side security logic for
user-generated message content should be applied when displaying
this HTML as though it were the body of a Zulip message.See alsodescription.
- date_created:integerThe UNIX timestamp for when the channel was created, in UTC seconds.Changes: New in Zulip 4.0 (feature level 30).
- creator_id:integer | nullThe ID of the user who created this channel.Anullvalue means the channel has no recorded creator, which is often
because the channel is very old, was created during realm creation or
because it was created via a data import tool ormanagement command.Changes: New in Zulip 9.0 (feature level 254).
- invite_only:booleanSpecifies whether the channel is private or not.
Only people who have been invited can access a private channel.
- subscribers:(integer)[]A list of user IDs of users who are also subscribed
to a given channel. Included only ifinclude_subscribersistrue.
- partial_subscribers:(integer)[]Ifinclude_subscribers="partial"was requested, the server may, at its discretion, send apartial_subscriberslist rather than asubscriberslist
for channels with a large number of subscribers.Thepartial_subscriberslist contains an arbitrary
subset of the channel's subscribers that is guaranteed
to include all bot user subscribers as well as all
users who have been active in the last 14 days, but
otherwise can be chosen arbitrarily by the server.Changes: New in Zulip 11.0 (feature level 412).
- desktop_notifications:boolean | nullA boolean specifying whether desktop notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_desktop_notifications, for
this channel.
- email_notifications:boolean | nullA boolean specifying whether email notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_email_notifications, for
this channel.
- wildcard_mentions_notify:boolean | nullA boolean specifying whether wildcard mentions
trigger notifications as though they were personal
mentions in this channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting, wildcard_mentions_notify, for
this channel.
- push_notifications:boolean | nullA boolean specifying whether push notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_push_notifications, for
this channel.
- audible_notifications:boolean | nullA boolean specifying whether audible notifications
are enabled for the given channel.Anullvalue means the value of this setting
should be inherited from the user-level default
setting,enable_stream_audible_notifications, for
this channel.
- pin_to_top:booleanA boolean specifying whether the given channel has been pinned
to the top.
- is_muted:booleanWhether the user has muted the channel. Muted channels do
not count towards your total unread count and do not show
up in theCombined feedview (previously known asAll messages).Changes: Prior to Zulip 2.1.0, this feature was
represented by the more confusingly namedin_home_view(with the
opposite value,in_home_view=!is_muted).
- in_home_view:booleanLegacy property for if the given channel is muted, with inverted meaning.Changes: Deprecated in Zulip 2.1.0. Clients should useis_mutedwhere available.
- is_announcement_only:booleanWhether only organization administrators can post to the channel.Changes: Deprecated in Zulip 3.0 (feature level 1). Clients
should usestream_post_policyinstead.
- is_web_public:booleanWhether the channel has been configured to allow unauthenticated
access to its message history from the web.
- color:stringThe user's personal color for the channel.
- stream_post_policy:integerA deprecated representation of a superset of the users who
have permission to post messages to the channel available
for backwards-compatibility. Clients should usecan_send_message_groupinstead.It is an enum with the following possible values, corresponding
to roles/system groups:1 = Any user can post.2 = Only administrators can post.3 = Onlyfull memberscan post.4 = Only moderators can post.Changes: Deprecated in Zulip 10.0 (feature level 333) and
replaced bycan_send_message_group, which supports finer
resolution of configurations, resulting in this property being
inaccurate following that transition.New in Zulip 3.0 (feature level 1), replacing the previousis_announcement_onlyboolean.
- message_retention_days:integer | nullNumber of days that messages sent to this channel will be stored
before being automatically deleted by themessage retention
policy. There are two special values:null, the default, means the channel will inherit the organization
  level setting.-1encodes retaining messages in this channel forever.Changes: New in Zulip 3.0 (feature level 17).
- history_public_to_subscribers:booleanWhether the history of the channel is public to its subscribers.Currently always true for public channels (i.e."invite_only": falseimplies"history_public_to_subscribers": true), but clients should not make that
assumption, as we may change that behavior in the future.
- first_message_id:integer | nullThe ID of the first message in the channel.Intended to help clients determine whether they need to display
UI like the "show all topics" widget that would suggest the channel
has older history that can be accessed.Isnullfor channels with no message history.
- folder_id:integer | nullThe ID of the folder to which the channel belongs.Isnullif channel does not belong to any folder.Changes: New in Zulip 11.0 (feature level 389).
- topics_policy:stringWhethernamed topicsand the empty
message_topic (i.e.,"general chat" message_topic)
are enabled in this channel."inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty message_topic in this
  channel."allow_empty_topic": Messages can be sent to both named topics and
  the empty message_topic in this channel."disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty message_topic is disabled."empty_topic_only": Messages can be sent to the empty message_topic in this
  channel, but named topics are disabled. See"general chat"
  channels.The"empty_topic_only"policy can only be set if all existing messages
in the channel are already in the empty message_topic.When creating a new channel, if thetopics_policyis not specified, the"inherit"option will be set.Changes: In Zulip 11.0 (feature level 404), the"empty_topic_only"option was added.New in Zulip 11.0 (feature level 392).
- is_recently_active:booleanWhether the channel has recent message activity. Clients should use this to implementhiding inactive channels.Changes: New in Zulip 10.0 (feature level 323). Previously, clients implemented the
demote_inactive_streams from local message history, resulting in a choppy loading
experience.
- stream_weekly_traffic:integer | nullThe average number of messages sent to the channel per week, as
estimated based on recent weeks, rounded to the nearest integer.Ifnull, the channel was recently created and there is
insufficient data to estimate the average traffic.
- can_add_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to add subscribers to this channel.Users who can administer the channel or have similar realm-level
permissions can add subscribers to a public channel regardless
of the value of this setting.Users in this group need not be subscribed to a private channel to
add subscribers to it.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 342). Previously, there was no
channel-level setting for this permission.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_remove_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to remove subscribers from this channel.Organization administrators can unsubscribe others from a channel as though
they were in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349), channel administrators
could not unsubscribe other users if they were not an organization
administrator or part ofcan_remove_subscribers_group. Realm administrators
were not allowed to unsubscribe other users from a private channel if they
were not subscribed to that channel.Prior to Zulip 10.0 (feature level 320), this value was always the integer
ID of a system group.Before Zulip 8.0 (feature level 197), thecan_remove_subscribers_groupsetting was namedcan_remove_subscribers_group_id.New in Zulip 6.0 (feature level 142).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_administer_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to administer this channel.Organization administrators can administer every channel as though they were
in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349) a user needed tohave content accessto a channel in
order to modify it. The exception to this rule was that organization
administrators can edit channel names and descriptions without
having full access to the channel.New in Zulip 10.0 (feature level 325). Prior to this
change, the permission to administer channels was limited to realm
administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_delete_any_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete any message in the channel.Note that a user musthave content accessto a
channel in order to delete any message in the channel.Users present in the organization-levelcan_delete_any_message_groupsetting can always delete any message in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users incan_delete_any_message_groupwere able
delete any message in the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_delete_own_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete the messages that they have sent in the channel.Note that a user musthave content accessto a
channel in order to delete their own message in the channel.Users with permission to delete any message in the channel
and users present in the organization-levelcan_delete_own_message_groupsetting
can always delete their own messages in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users in the organization-levelcan_delete_any_message_groupandcan_delete_own_message_groupsettings were able delete their own messages in
the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_move_messages_out_of_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages out of this channel.Note that a user musthave content accessto a
channel in order to move messages out of the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_channels_groupsetting can always move messages
out of the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_channels_groupwere able
move messages between channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_move_messages_within_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages within this channel.Note that a user musthave content accessto a
channel in order to move messages within the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_topics_groupsetting can always move messages
within the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_topics_groupwere able
move messages between topics of a channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_send_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to post in this channel.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Note that using this permission to send a message to a new message_topic requires
also having permission to create new topics in the channel.Changes: New in Zulip 10.0 (feature level 333). Previouslystream_post_policyfield used to control the permission to
post in the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_subscribe_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to subscribe themselves to this channel.Everyone, excluding guests, can subscribe to any public channel
irrespective of this setting.Users in this group can subscribe to a private channel as well.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 357).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_resolve_topics_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to resolve topics in the channel.Users who have similar realm-level permissions can resolve topics
in a channel regardless of the value of this setting.Changes: New in Zulip 11.0 (feature level 402).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_create_topic_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to create a new message_topic in this channel.Note that using this permission requires also having permission to
send messages in the channel.Note that this must be therole:everyonesystem groupforprivate channels with protected history.Changes: New in Zulip 12.0 (feature level 441). Previously,
if you could send messages in a channel, you could create topics in
the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- is_archived:booleanA boolean indicating whether the channel isarchived.Changes: New in Zulip 10.0 (feature level 315).
Previously, subscriptions only included active
channels. Note that some endpoints will never return archived
channels unless the client declares explicit support for
them via thearchived_channelsclient capability.
- subscriber_count:numberThe total number of non-deactivated users (including bots) who
are subscribed to the channel. Clients are responsible for updating
this value usingpeer_addandpeer_removeevents.The server's internals cannot guarantee this value is correctly
synced withpeer_addandpeer_removeevents for the channel. As
a result, if a (rare) race occurs between a change in the channel's
subscribers and fetching this value, it is possible for a client
that is correctly following the events protocol to end up with a
permanently off-by-one error in the channel's subscriber count.Clients are recommended to fetch full subscriber data for a channel
in contexts where it is important to avoid this risk. The official
web application, for example, uses this field primarily while
waiting to fetch a given channel's full subscriber list from the
server.Changes: New in Zulip 11.0 (feature level 394).

```
include_subscribers="partial"
```
- 1 = Any user can post.
- 2 = Only administrators can post.
- 3 = Onlyfull memberscan post.
- 4 = Only moderators can post.
- null, the default, means the channel will inherit the organization
  level setting.
- -1encodes retaining messages in this channel forever.
- "inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty message_topic in this
  channel.
- "allow_empty_topic": Messages can be sent to both named topics and
  the empty message_topic in this channel.
- "disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty message_topic is disabled.
- "empty_topic_only": Messages can be sent to the empty message_topic in this
  channel, but named topics are disabled. See"general chat"
  channels.

```
realm_topics_policy
```
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- stream_id:integerThe unique ID of the channel.
- name:stringThe name of the channel.
- is_archived:booleanA boolean indicating whether the channel isarchived.Changes: New in Zulip 10.0 (feature level 315).
Previously, this endpoint never returned archived channels.
- description:stringThe short description of the channel inZulip-flavored Markdownformat,
intended to be used to prepopulate UI for editing a channel's
description.SeeMarkdown message formattingfor details on Zulip's HTML format.
- date_created:integerThe UNIX timestamp for when the channel was created, in UTC seconds.Changes: New in Zulip 4.0 (feature level 30).
- creator_id:integer | nullThe ID of the user who created this channel.Anullvalue means the channel has no recorded creator, which is often
because the channel is very old, was created during realm creation or
because it was created via a data import tool ormanagement command.Changes: New in Zulip 9.0 (feature level 254).
- invite_only:booleanSpecifies whether the channel is private or not.
Only people who have been invited can access a private channel.
- rendered_description:stringThe short description of the channel rendered as HTML, intended to
be used when displaying the channel description in a UI.One should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax
work correctly. And any client-side security logic for
user-generated message content should be applied when displaying
this HTML as though it were the body of a Zulip message.
- is_web_public:booleanWhether the channel has been configured to allow unauthenticated
access to its message history from the web.Changes: New in Zulip 2.1.0.
- stream_post_policy:integerA deprecated representation of a superset of the users who
have permission to post messages to the channel available
for backwards-compatibility. Clients should usecan_send_message_groupinstead.It is an enum with the following possible values, corresponding
to roles/system groups:1 = Any user can post.2 = Only administrators can post.3 = Onlyfull memberscan post.4 = Only moderators can post.Changes: Deprecated in Zulip 10.0 (feature level 333) and
replaced bycan_send_message_group, which supports finer
resolution of configurations, resulting in this property being
inaccurate following that transition.New in Zulip 3.0 (feature level 1), replacing the previousis_announcement_onlyboolean.
- message_retention_days:integer | nullNumber of days that messages sent to this channel will be stored
before being automatically deleted by themessage retention
policy. There are two special values:null, the default, means the channel will inherit the organization
  level setting.-1encodes retaining messages in this channel forever.Changes: New in Zulip 3.0 (feature level 17).
- history_public_to_subscribers:booleanWhether the history of the channel is public to its subscribers.Currently always true for public channels (i.e."invite_only": falseimplies"history_public_to_subscribers": true), but clients should not make that
assumption, as we may change that behavior in the future.
- topics_policy:stringWhethernamed topicsand the empty
message_topic (i.e.,"general chat" message_topic)
are enabled in this channel."inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty message_topic in this
  channel."allow_empty_topic": Messages can be sent to both named topics and
  the empty message_topic in this channel."disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty message_topic is disabled."empty_topic_only": Messages can be sent to the empty message_topic in this
  channel, but named topics are disabled. See"general chat"
  channels.The"empty_topic_only"policy can only be set if all existing messages
in the channel are already in the empty message_topic.When creating a new channel, if thetopics_policyis not specified, the"inherit"option will be set.Changes: In Zulip 11.0 (feature level 404), the"empty_topic_only"option was added.New in Zulip 11.0 (feature level 392).
- first_message_id:integer | nullThe ID of the first message in the channel.Intended to help clients determine whether they need to display
UI like the "show all topics" widget that would suggest the channel
has older history that can be accessed.Isnullfor channels with no message history.Changes: New in Zulip 2.1.0.
- folder_id:integer | nullThe ID of the folder to which the channel belongs.Isnullif channel does not belong to any folder.Changes: New in Zulip 11.0 (feature level 389).
- is_recently_active:booleanWhether the channel has recent message activity. Clients should use this to implementhide inactive channelsifdemote_inactive_streamsis enabled.Changes: New in Zulip 10.0 (feature level 323). Previously, clients implemented the
demote_inactive_streams from local message history, resulting in a choppy loading
experience.
- is_announcement_only:booleanWhether the given channel is announcement only or not.Changes: Deprecated in Zulip 3.0 (feature level 1). Clients
should usestream_post_policyinstead.
- can_add_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to add subscribers to this channel.Users who can administer the channel or have similar realm-level
permissions can add subscribers to a public channel regardless
of the value of this setting.Users in this group need not be subscribed to a private channel to
add subscribers to it.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 342). Previously, there was no
channel-level setting for this permission.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_remove_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to remove subscribers from this channel.Organization administrators can unsubscribe others from a channel as though
they were in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349), channel administrators
could not unsubscribe other users if they were not an organization
administrator or part ofcan_remove_subscribers_group. Realm administrators
were not allowed to unsubscribe other users from a private channel if they
were not subscribed to that channel.Prior to Zulip 10.0 (feature level 320), this value was always the integer
ID of a system group.Before Zulip 8.0 (feature level 197), thecan_remove_subscribers_groupsetting was namedcan_remove_subscribers_group_id.New in Zulip 6.0 (feature level 142).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_administer_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to administer this channel.Organization administrators can administer every channel as though they were
in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349) a user needed tohave content accessto a channel in
order to modify it. The exception to this rule was that organization
administrators can edit channel names and descriptions without
having full access to the channel.New in Zulip 10.0 (feature level 325). Prior to this
change, the permission to administer channels was limited to realm
administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_delete_any_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete any message in the channel.Note that a user musthave content accessto a
channel in order to delete any message in the channel.Users present in the organization-levelcan_delete_any_message_groupsetting can always delete any message in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users incan_delete_any_message_groupwere able
delete any message in the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_delete_own_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete the messages that they have sent in the channel.Note that a user musthave content accessto a
channel in order to delete their own message in the channel.Users with permission to delete any message in the channel
and users present in the organization-levelcan_delete_own_message_groupsetting
can always delete their own messages in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users in the organization-levelcan_delete_any_message_groupandcan_delete_own_message_groupsettings were able delete their own messages in
the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_move_messages_out_of_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages out of this channel.Note that a user musthave content accessto a
channel in order to move messages out of the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_channels_groupsetting can always move messages
out of the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_channels_groupwere able
move messages between channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_move_messages_within_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages within this channel.Note that a user musthave content accessto a
channel in order to move messages within the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_topics_groupsetting can always move messages
within the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_topics_groupwere able
move messages between topics of a channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_send_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to post in this channel.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Note that using this permission to send a message to a new message_topic requires
also having permission to create new topics in the channel.Changes: New in Zulip 10.0 (feature level 333). Previouslystream_post_policyfield used to control the permission to
post in the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_subscribe_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to subscribe themselves to this channel.Everyone, excluding guests, can subscribe to any public channel
irrespective of this setting.Users in this group can subscribe to a private channel as well.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 357).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_resolve_topics_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to resolve topics in the channel.Users who have similar realm-level permissions can resolve topics
in a channel regardless of the value of this setting.Changes: New in Zulip 11.0 (feature level 402).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_create_topic_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to create a new message_topic in this channel.Note that using this permission requires also having permission to
send messages in the channel.Note that this must be therole:everyonesystem groupforprivate channels with protected history.Changes: New in Zulip 12.0 (feature level 441). Previously,
if you could send messages in a channel, you could create topics in
the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- subscriber_count:numberThe total number of non-deactivated users (including bots) who
are subscribed to the channel. Clients are responsible for updating
this value usingpeer_addandpeer_removeevents.The server's internals cannot guarantee this value is correctly
synced withpeer_addandpeer_removeevents for the channel. As
a result, if a (rare) race occurs between a change in the channel's
subscribers and fetching this value, it is possible for a client
that is correctly following the events protocol to end up with a
permanently off-by-one error in the channel's subscriber count.Clients are recommended to fetch full subscriber data for a channel
in contexts where it is important to avoid this risk. The official
web application, for example, uses this field primarily while
waiting to fetch a given channel's full subscriber list from the
server.Changes: New in Zulip 11.0 (feature level 394).
- stream_weekly_traffic:integer | nullThe average number of messages sent to the channel per week, as
estimated based on recent weeks, rounded to the nearest integer.Ifnull, the channel was recently created and there is
insufficient data to estimate the average traffic.
- subscribers:(integer)[]A list of user IDs of users who are subscribed
to the channel. Included only ifinclude_subscribersistrue.If a user is not allowed to know the subscribers for
a channel, we will send an empty array. API authors
should use other data to determine whether users like
guest users are forbidden to know the subscribers.
- partial_subscribers:(integer)[]Ifinclude_subscribers="partial"was requested, the server may, at its discretion, send apartial_subscriberslist rather than asubscriberslist
for channels with a large number of subscribers.Thepartial_subscriberslist contains an arbitrary
subset of the channel's subscribers that is guaranteed
to include all bot user subscribers as well as all
users who have been active in the last 14 days, but
otherwise can be chosen arbitrarily by the server.If a user is not allowed to know the subscribers for
a channel, we will send an empty array. API authors
should use other data to determine whether users like
guest users are forbidden to know the subscribers.Changes: New in Zulip 11.0 (feature level 412).
- 1 = Any user can post.
- 2 = Only administrators can post.
- 3 = Onlyfull memberscan post.
- 4 = Only moderators can post.
- null, the default, means the channel will inherit the organization
  level setting.
- -1encodes retaining messages in this channel forever.
- "inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty message_topic in this
  channel.
- "allow_empty_topic": Messages can be sent to both named topics and
  the empty message_topic in this channel.
- "disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty message_topic is disabled.
- "empty_topic_only": Messages can be sent to the empty message_topic in this
  channel, but named topics are disabled. See"general chat"
  channels.

```
realm_topics_policy
```
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.

```
include_subscribers="partial"
```
- id:integerThe unique ID of the channel folder.
- name:stringThe name of the channel folder.
- order:integerThis value determines in which order the channel folder should be
displayed in the UI. The value is 0 indexed, and a channel folder with
a lower value should be displayed before channel folders with higher
values.Changes: New in Zulip 11.0 (feature level 414).
- date_created:integer | nullThe UNIX timestamp for when the channel folder was created,
in UTC seconds.
- creator_id:integer | nullThe ID of the user who created the channel folder.
- description:stringThe description of the channel folder. Can be an empty string.SeeMarkdown message formattingfor details
on Zulip's HTML format.
- rendered_description:stringThe description of the channel folder rendered as HTML, intended to be
used for UI that displays the channel folder description.Clients should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax work
correctly. And any client-side security logic for user-generated
message content should be applied when displaying this HTML as though
it were the body of a Zulip message.
- is_archived:booleanWhether the channel folder is archived or not.
- count:integerThe total number of unread messages to display. This includes one-on-one and group
direct messages, as well as channel messages that are notmuted.Changes: Before Zulip 8.0 (feature level 213), the unmute and follow
message_topic features were not handled correctly in calculating this field.
- pms:(object)[]An array of objects where each object contains details of unread
one-on-one direct messages with a specific user.Note that it is possible for a message that the current user sent
to the specified user to be marked as unread and thus appear here.other_user_id:integerThe user ID of the other participant in this one-on-one direct
message conversation. Will be the current user's ID for messages
that they sent in a one-on-one direct message conversation with
themself.Changes: New in Zulip 5.0 (feature level 119), replacing
the less clearly namedsender_idfield.sender_id:integerOld name for theother_user_idfield. Clients should access
this field in Zulip server versions that do not yet supportother_user_id.Changes: Deprecated in Zulip 5.0 (feature level 119).
We expect to provide a next version of the fullunread_msgsAPI before removing this legacy name.unread_message_ids:(integer)[]The message IDs of the recent unread direct messages sent
by either user in this one-on-one direct message conversation,
sorted in ascending order.
- streams:(object)[]An array of dictionaries where each dictionary contains details of all
unread messages of a single subscribed channel. This includes muted channels
and muted topics, even though those messages are excluded fromcount.Changes: Prior to Zulip 5.0 (feature level 90), these objects
included asender_idsproperty, which listed the set of IDs of
users who had sent the unread messages.message_topic:stringThe message_topic under which the messages were sent.Note that the empty string message_topic may have been rewritten by the server
to the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse depending on the value
of theempty_topic_nameclient capability.Changes: Theempty_topic_nameclient capability is new in
Zulip 10.0 (feature level 334).stream_id:integerThe ID of the channel to which the messages were sent.unread_message_ids:(integer)[]The message IDs of the recent unread messages sent in this channel,
sorted in ascending order.
- huddles:(object)[]An array of objects where each object contains details of unread
group direct messages with a specific group of users.user_ids_string:stringA string containing the IDs of all users in the group
direct message conversation, including the current user,
separated by commas and sorted numerically; for example:"1,2,3".unread_message_ids:(integer)[]The message IDs of the recent unread messages which have been sent in
this group direct message conversation, sorted in ascending order.
- mentions:(integer)[]Array containing the IDs of all unread messages in which the user was
mentioned directly, and unreadnon-mutedmessages
in which the user was mentioned through a wildcard.Changes: Before Zulip 8.0 (feature level 213), the unmute and follow
message_topic features were not handled correctly in calculating this field.
- old_unreads_missing:booleanWhether this data set was truncated because the user has too many
unread messages. When truncation occurs, only the most recentMAX_UNREAD_MESSAGES(currently 50000) messages will be considered
when forming this response. Whentrue, we recommend that clients
display a warning, as they are likely to produce erroneous results
until reloaded with the user having fewer thanMAX_UNREAD_MESSAGESunread messages.Changes: New in Zulip 4.0 (feature level 44).
- other_user_id:integerThe user ID of the other participant in this one-on-one direct
message conversation. Will be the current user's ID for messages
that they sent in a one-on-one direct message conversation with
themself.Changes: New in Zulip 5.0 (feature level 119), replacing
the less clearly namedsender_idfield.
- sender_id:integerOld name for theother_user_idfield. Clients should access
this field in Zulip server versions that do not yet supportother_user_id.Changes: Deprecated in Zulip 5.0 (feature level 119).
We expect to provide a next version of the fullunread_msgsAPI before removing this legacy name.
- unread_message_ids:(integer)[]The message IDs of the recent unread direct messages sent
by either user in this one-on-one direct message conversation,
sorted in ascending order.
- message_topic:stringThe message_topic under which the messages were sent.Note that the empty string message_topic may have been rewritten by the server
to the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse depending on the value
of theempty_topic_nameclient capability.Changes: Theempty_topic_nameclient capability is new in
Zulip 10.0 (feature level 334).
- stream_id:integerThe ID of the channel to which the messages were sent.
- unread_message_ids:(integer)[]The message IDs of the recent unread messages sent in this channel,
sorted in ascending order.

```
POST /register
```
- user_ids_string:stringA string containing the IDs of all users in the group
direct message conversation, including the current user,
separated by commas and sorted numerically; for example:"1,2,3".
- unread_message_ids:(integer)[]The message IDs of the recent unread messages which have been sent in
this group direct message conversation, sorted in ascending order.
- stream_id:integerThe unique ID of the channel.
- name:stringThe name of the channel.
- is_archived:booleanA boolean indicating whether the channel isarchived.Changes: New in Zulip 10.0 (feature level 315).
Previously, this endpoint never returned archived channels.
- description:stringThe short description of the channel inZulip-flavored Markdownformat,
intended to be used to prepopulate UI for editing a channel's
description.SeeMarkdown message formattingfor details on Zulip's HTML format.
- date_created:integerThe UNIX timestamp for when the channel was created, in UTC seconds.Changes: New in Zulip 4.0 (feature level 30).
- creator_id:integer | nullThe ID of the user who created this channel.Anullvalue means the channel has no recorded creator, which is often
because the channel is very old, was created during realm creation or
because it was created via a data import tool ormanagement command.Changes: New in Zulip 9.0 (feature level 254).
- invite_only:booleanSpecifies whether the channel is private or not.
Only people who have been invited can access a private channel.
- rendered_description:stringThe short description of the channel rendered as HTML, intended to
be used when displaying the channel description in a UI.One should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax
work correctly. And any client-side security logic for
user-generated message content should be applied when displaying
this HTML as though it were the body of a Zulip message.
- is_web_public:booleanWhether the channel has been configured to allow unauthenticated
access to its message history from the web.Changes: New in Zulip 2.1.0.
- stream_post_policy:integerA deprecated representation of a superset of the users who
have permission to post messages to the channel available
for backwards-compatibility. Clients should usecan_send_message_groupinstead.It is an enum with the following possible values, corresponding
to roles/system groups:1 = Any user can post.2 = Only administrators can post.3 = Onlyfull memberscan post.4 = Only moderators can post.Changes: Deprecated in Zulip 10.0 (feature level 333) and
replaced bycan_send_message_group, which supports finer
resolution of configurations, resulting in this property being
inaccurate following that transition.New in Zulip 3.0 (feature level 1), replacing the previousis_announcement_onlyboolean.
- message_retention_days:integer | nullNumber of days that messages sent to this channel will be stored
before being automatically deleted by themessage retention
policy. There are two special values:null, the default, means the channel will inherit the organization
  level setting.-1encodes retaining messages in this channel forever.Changes: New in Zulip 3.0 (feature level 17).
- history_public_to_subscribers:booleanWhether the history of the channel is public to its subscribers.Currently always true for public channels (i.e."invite_only": falseimplies"history_public_to_subscribers": true), but clients should not make that
assumption, as we may change that behavior in the future.
- topics_policy:stringWhethernamed topicsand the empty
message_topic (i.e.,"general chat" message_topic)
are enabled in this channel."inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty message_topic in this
  channel."allow_empty_topic": Messages can be sent to both named topics and
  the empty message_topic in this channel."disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty message_topic is disabled."empty_topic_only": Messages can be sent to the empty message_topic in this
  channel, but named topics are disabled. See"general chat"
  channels.The"empty_topic_only"policy can only be set if all existing messages
in the channel are already in the empty message_topic.When creating a new channel, if thetopics_policyis not specified, the"inherit"option will be set.Changes: In Zulip 11.0 (feature level 404), the"empty_topic_only"option was added.New in Zulip 11.0 (feature level 392).
- first_message_id:integer | nullThe ID of the first message in the channel.Intended to help clients determine whether they need to display
UI like the "show all topics" widget that would suggest the channel
has older history that can be accessed.Isnullfor channels with no message history.Changes: New in Zulip 2.1.0.
- folder_id:integer | nullThe ID of the folder to which the channel belongs.Isnullif channel does not belong to any folder.Changes: New in Zulip 11.0 (feature level 389).
- is_recently_active:booleanWhether the channel has recent message activity. Clients should use this to implementhide inactive channelsifdemote_inactive_streamsis enabled.Changes: New in Zulip 10.0 (feature level 323). Previously, clients implemented the
demote_inactive_streams from local message history, resulting in a choppy loading
experience.
- is_announcement_only:booleanWhether the given channel is announcement only or not.Changes: Deprecated in Zulip 3.0 (feature level 1). Clients
should usestream_post_policyinstead.
- can_add_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to add subscribers to this channel.Users who can administer the channel or have similar realm-level
permissions can add subscribers to a public channel regardless
of the value of this setting.Users in this group need not be subscribed to a private channel to
add subscribers to it.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 342). Previously, there was no
channel-level setting for this permission.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_remove_subscribers_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to remove subscribers from this channel.Organization administrators can unsubscribe others from a channel as though
they were in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349), channel administrators
could not unsubscribe other users if they were not an organization
administrator or part ofcan_remove_subscribers_group. Realm administrators
were not allowed to unsubscribe other users from a private channel if they
were not subscribed to that channel.Prior to Zulip 10.0 (feature level 320), this value was always the integer
ID of a system group.Before Zulip 8.0 (feature level 197), thecan_remove_subscribers_groupsetting was namedcan_remove_subscribers_group_id.New in Zulip 6.0 (feature level 142).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_administer_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to administer this channel.Organization administrators can administer every channel as though they were
in this group without being explicitly listed here.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Changes: Prior to Zulip 10.0 (feature level 349) a user needed tohave content accessto a channel in
order to modify it. The exception to this rule was that organization
administrators can edit channel names and descriptions without
having full access to the channel.New in Zulip 10.0 (feature level 325). Prior to this
change, the permission to administer channels was limited to realm
administrators.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_delete_any_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete any message in the channel.Note that a user musthave content accessto a
channel in order to delete any message in the channel.Users present in the organization-levelcan_delete_any_message_groupsetting can always delete any message in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users incan_delete_any_message_groupwere able
delete any message in the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_delete_own_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to delete the messages that they have sent in the channel.Note that a user musthave content accessto a
channel in order to delete their own message in the channel.Users with permission to delete any message in the channel
and users present in the organization-levelcan_delete_own_message_groupsetting
can always delete their own messages in the channel if theyhave content accessto that channel.Changes: New in Zulip 11.0 (feature level 407). Prior to this
change, only the users in the organization-levelcan_delete_any_message_groupandcan_delete_own_message_groupsettings were able delete their own messages in
the organization.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_move_messages_out_of_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages out of this channel.Note that a user musthave content accessto a
channel in order to move messages out of the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_channels_groupsetting can always move messages
out of the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_channels_groupwere able
move messages between channels.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_move_messages_within_channel_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to move messages within this channel.Note that a user musthave content accessto a
channel in order to move messages within the channel.Channel administrators and users present in the organization-levelcan_move_messages_between_topics_groupsetting can always move messages
within the channel if theyhave content accessto
the channel.Changes: New in Zulip 11.0 (feature level 396). Prior to this
change, only the users incan_move_messages_between_topics_groupwere able
move messages between topics of a channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_send_message_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to post in this channel.Note that a user must have metadata access to a channel and permission
to administer the channel in order to modify this setting.Note that using this permission to send a message to a new message_topic requires
also having permission to create new topics in the channel.Changes: New in Zulip 10.0 (feature level 333). Previouslystream_post_policyfield used to control the permission to
post in the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_subscribe_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to subscribe themselves to this channel.Everyone, excluding guests, can subscribe to any public channel
irrespective of this setting.Users in this group can subscribe to a private channel as well.Note that a user musthave content accessto a channel and permission to administer the channel in order to
modify this setting.Changes: New in Zulip 10.0 (feature level 357).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_resolve_topics_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to resolve topics in the channel.Users who have similar realm-level permissions can resolve topics
in a channel regardless of the value of this setting.Changes: New in Zulip 11.0 (feature level 402).The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_create_topic_group:integer | objectAgroup-setting valuedefining the set of users
who have permission to create a new message_topic in this channel.Note that using this permission requires also having permission to
send messages in the channel.Note that this must be therole:everyonesystem groupforprivate channels with protected history.Changes: New in Zulip 12.0 (feature level 441). Previously,
if you could send messages in a channel, you could create topics in
the channel.The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- subscriber_count:numberThe total number of non-deactivated users (including bots) who
are subscribed to the channel. Clients are responsible for updating
this value usingpeer_addandpeer_removeevents.The server's internals cannot guarantee this value is correctly
synced withpeer_addandpeer_removeevents for the channel. As
a result, if a (rare) race occurs between a change in the channel's
subscribers and fetching this value, it is possible for a client
that is correctly following the events protocol to end up with a
permanently off-by-one error in the channel's subscriber count.Clients are recommended to fetch full subscriber data for a channel
in contexts where it is important to avoid this risk. The official
web application, for example, uses this field primarily while
waiting to fetch a given channel's full subscriber list from the
server.Changes: New in Zulip 11.0 (feature level 394).
- stream_weekly_traffic:integer | nullThe average number of messages sent to the channel per week, as
estimated based on recent weeks, rounded to the nearest integer.Ifnull, no information is provided on the average traffic.
This can be because the channel was recently created and there
is insufficient data to make an estimate, or because the server
wishes to omit this information for this client, this realm, or
this endpoint or type of event.Changes: New in Zulip 8.0 (feature level 199). Previously, this
statistic was available only in subscription objects.
- 1 = Any user can post.
- 2 = Only administrators can post.
- 3 = Onlyfull memberscan post.
- 4 = Only moderators can post.
- null, the default, means the channel will inherit the organization
  level setting.
- -1encodes retaining messages in this channel forever.
- "inherit": Messages can be sent to named topics in this channel,
  and theorganization-levelrealm_topics_policyis used for whether messages can be sent to the empty message_topic in this
  channel.
- "allow_empty_topic": Messages can be sent to both named topics and
  the empty message_topic in this channel.
- "disable_empty_topic": Messages can be sent to named topics in this
  channel, but the empty message_topic is disabled.
- "empty_topic_only": Messages can be sent to the empty message_topic in this
  channel, but named topics are disabled. See"general chat"
  channels.

```
realm_topics_policy
```
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- name:stringName of the default channel group.
- description:stringDescription of the default channel group.
- id:integerThe ID of the default channel group.
- streams:(integer)[]An array of IDs of all the channels in the default channel_name group.Changes: Before Zulip 10.0 (feature level 330), we sent array
of dictionaries where each dictionary contained details about a
single channel_name in the default channel_name group.
- {user_id}:objectObject containing the status details of a user
with the key of the object being the ID of the user.away:booleanIf present, the user has marked themself "away".Changes: Deprecated in Zulip 6.0 (feature level 148);
starting with that feature level,awayis a legacy way to
access the user'spresence_enabledsetting, withaway = !presence_enabled. To be removed in a future release.status_text:stringIf present, the text content of the user's status message.emoji_name:stringIf present, the name for the emoji to associate with the user's status.Changes: New in Zulip 5.0 (feature level 86).emoji_code:stringIf present, a unique identifier, defining the specific emoji codepoint
requested, within the namespace of thereaction_type.Changes: New in Zulip 5.0 (feature level 86).reaction_type:stringIf present, a string indicating the type of emoji. Each emojireaction_typehas an independent namespace for values ofemoji_code.Must be one of the following values:unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").Changes: New in Zulip 5.0 (feature level 86).
- away:booleanIf present, the user has marked themself "away".Changes: Deprecated in Zulip 6.0 (feature level 148);
starting with that feature level,awayis a legacy way to
access the user'spresence_enabledsetting, withaway = !presence_enabled. To be removed in a future release.
- status_text:stringIf present, the text content of the user's status message.
- emoji_name:stringIf present, the name for the emoji to associate with the user's status.Changes: New in Zulip 5.0 (feature level 86).
- emoji_code:stringIf present, a unique identifier, defining the specific emoji codepoint
requested, within the namespace of thereaction_type.Changes: New in Zulip 5.0 (feature level 86).
- reaction_type:stringIf present, a string indicating the type of emoji. Each emojireaction_typehas an independent namespace for values ofemoji_code.Must be one of the following values:unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").Changes: New in Zulip 5.0 (feature level 86).
- unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.
- realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.
- zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").
- twenty_four_hour_time:boolean | nullWhether time should bedisplayed in 24-hour notation.Anullvalue indicates that the client should use the default time
format for the user's locale.Changes: Prior to Zulip 11.0 (feature level 408),nullwas not a valid value for this setting. Note that it was not possible
to actually set the time format tonullat this feature level.
- web_mark_read_on_scroll_policy:integerWhether or not to mark messages as read when the user scrolls through their
feed.1 - Always2 - Only in conversation views3 - NeverChanges: New in Zulip 7.0 (feature level 175). Previously, there was no
way for the user to configure this behavior on the web, and the Zulip web and
desktop apps behaved like the "Always" setting when marking messages as read.
- web_channel_default_view:integerWeb/desktop app setting controlling the default navigation
behavior when clicking on a channel link.1 - Top message_topic in the channel2 - Channel feed3 - List of topics4 - Top unread message_topic in channelChanges: The "Top unread message_topic in channel" is new in Zulip 11.0
(feature level 401).The "List of topics" option is new in Zulip 11.0 (feature level 383).New in Zulip 9.0 (feature level 269). Previously, this
was not configurable, and every user had the "Channel feed" behavior.
- starred_message_counts:booleanWhether clients should display thenumber of starred
messages.
- receives_typing_notifications:booleanWhether the user is configured to receive typing notifications from
other users. The server will only deliver typing notifications events
to users who for whom this is enabled.Changes: New in Zulip 9.0 (feature level 253). Previously, there were
only options to disable sending typing notifications.
- web_suggest_update_timezone:booleanWhether the user should be shown an alert, offering to update theirprofile time zone, when the time displayed
for the profile time zone differs from the current time displayed by the
time zone configured on their device.Changes: New in Zulip 10.0 (feature level 329).
- fluid_layout_width:booleanWhether to use themaximum available screen widthfor the web app's center panel (message feed, recent conversations) on wide screens.
- high_contrast_mode:booleanThis setting is reserved for use to control variations in Zulip's design
to help visually impaired users.
- web_font_size_px:integerUser-configured primaryfont-sizefor the web application, in pixels.Changes: New in Zulip 9.0 (feature level 245). Previously, font size was
only adjustable via browser zoom. Note that this setting was not fully
implemented at this feature level.
- web_line_height_percent:integerUser-configured primaryline-heightfor the web application, in percent, so a
value of 120 represents aline-heightof 1.2.Changes: New in Zulip 9.0 (feature level 245). Previously, line height was
not user-configurable. Note that this setting was not fully implemented at this
feature level.
- color_scheme:integerControls whichcolor themeto use.1 - Automatic2 - Dark theme3 - Light themeAutomatic detection is implementing using the standardprefers-color-schememedia query.
- translate_emoticons:booleanWhether totranslate emoticons to emojiin messages the user sends.
- display_emoji_reaction_users:booleanWhether to display the names of reacting users on a message.When enabled, clients should display the names of reacting
users, rather than a count, for messages with few total
reactions. The ideal cutoff may depend on the space
available for displaying reactions; the official web
application displays names when 3 or fewer total reactions
are present with this setting enabled.Changes: New in Zulip 6.0 (feature level 125).
- default_language:stringWhatdefault languageto use for the account.This controls both the Zulip UI as well as email notifications sent to the user.The value needs to be a standard language code that the Zulip server has
translation data for; for example,"en"for English or"de"for German.
- web_home_view:stringThehome viewused when opening a new
Zulip web app window or hitting theEsckeyboard shortcut repeatedly."recent" - Recent conversations view"inbox" - Inbox view"all_messages" - Combined feed viewChanges: Before Zulip 12.0 (feature level 454), the Recent
view had"recent_topics"as its string encoding.New in Zulip 8.0 (feature level 219). Previously, this was
calleddefault_view, which was new in Zulip 4.0 (feature level 42).
- web_escape_navigates_to_home_view:booleanWhether the escape key navigates to theconfigured home view.Changes: New in Zulip 8.0 (feature level 219). Previously, this
was calledescape_navigates_to_default_view, which was new in Zulip
5.0 (feature level 107).
- left_side_userlist:booleanWhether the users list on left sidebar in filter_spec windows.This feature is not heavily used and is likely to be reworked.
- emojiset:stringThe user's configuredemoji set,
used to display emoji to the user everywhere they appear in the UI."google" - Google modern"twitter" - Twitter"text" - Plain text
- demote_inactive_streams:integerWhether tohide inactive channelsin the left sidebar.1 - Automatic2 - Always3 - Never
- user_list_style:integerThe style selected by the user for the right sidebar user list.1 - Compact2 - With status3 - With avatar and statusChanges: New in Zulip 6.0 (feature level 141).
- web_animate_image_previews:stringControls how animated images should be played in the message feed in the web/desktop application."always" - Always play the animated images in the message feed."on_hover" - Play the animated images on hover over them in the message feed."never" - Never play animated images in the message feed.Changes: New in Zulip 9.0 (feature level 275).
- web_stream_unreads_count_display_policy:integerConfiguration for which channels should be displayed with a numeric unread count in the left sidebar.
Channels that do not have an unread count will have a simple dot indicator for whether there are any
unread messages.1 - All channels2 - Unmuted channels and topics3 - No channelsChanges: New in Zulip 8.0 (feature level 210).
- hide_ai_features:booleanControls whether user wants AI features like message_topic summarization to
be hidden in all Zulip clients.Changes: New in Zulip 10.0 (feature level 350).
- web_inbox_show_channel_folders:booleanDetermines whetherchannel foldersare used to organize how conversations with unread messages
are displayed in the web/desktop application's Inbox view.Changes: New in Zulip 12.0 (feature level 431).
- web_left_sidebar_show_channel_folders:booleanDetermines whetherchannel foldersare used to organize how channels are displayed in the
web/desktop application's left sidebar.Changes: New in Zulip 11.0 (feature level 411).
- web_left_sidebar_unreads_count_summary:booleanDetermines whether the web/desktop application's left sidebar displays
the unread message count summary.Changes: New in Zulip 11.0 (feature level 398).
- timezone:stringThe IANA identifier of the user'sprofile time zone,
which is used primarily to display the user's local time to other users.
- enter_sends:booleanWhether the user setting forsending on pressing Enterin the compose box is enabled.
- enable_drafts_synchronization:booleanA boolean parameter to control whether synchronizing drafts is enabled for
the user. When synchronization is disabled, all drafts stored in the server
will be automatically deleted from the server.This does not do anything (like sending events) to delete local copies of
drafts stored in clients.
- enable_stream_desktop_notifications:booleanEnable visual desktop notifications for channel messages.
- enable_stream_email_notifications:booleanEnable email notifications for channel messages.
- enable_stream_push_notifications:booleanEnable mobile notifications for channel messages.
- enable_stream_audible_notifications:booleanEnable audible desktop notifications for channel messages.
- notification_sound:stringNotification sound name.
- enable_desktop_notifications:booleanEnable visual desktop notifications for direct messages and @-mentions.
- enable_sounds:booleanEnable audible desktop notifications for direct messages and
@-mentions.
- enable_followed_topic_desktop_notifications:booleanEnable visual desktop notifications for messages sent to followed topics.Changes: New in Zulip 8.0 (feature level 189).
- enable_followed_topic_email_notifications:booleanEnable email notifications for messages sent to followed topics.Changes: New in Zulip 8.0 (feature level 189).
- enable_followed_topic_push_notifications:booleanEnable push notifications for messages sent to followed topics.Changes: New in Zulip 8.0 (feature level 189).
- enable_followed_topic_audible_notifications:booleanEnable audible desktop notifications for messages sent to followed topics.Changes: New in Zulip 8.0 (feature level 189).
- email_notifications_batching_period_seconds:integerThe duration (in seconds) for which the server should wait to batch
email notifications before sending them.
- enable_offline_email_notifications:booleanEnable email notifications for direct messages and @-mentions received
when the user is offline.
- enable_offline_push_notifications:booleanEnable mobile notification for direct messages and @-mentions received
when the user is offline.
- enable_online_push_notifications:booleanEnable mobile notification for direct messages and @-mentions received
when the user is online.
- enable_digest_emails:booleanEnable digest emails when the user is away.
- enable_marketing_emails:booleanEnable marketing emails. Has no function outside Zulip Cloud.
- enable_login_emails:booleanEnable email notifications for new logins to account.
- message_content_in_email_notifications:booleanInclude the message's content in email notifications for new messages.
- pm_content_in_desktop_notifications:booleanInclude content of direct messages in desktop notifications.
- wildcard_mentions_notify:booleanWhether wildcard mentions (E.g. @all) should send notifications
like a personal mention.
- enable_followed_topic_wildcard_mentions_notify:booleanWhether wildcard mentions (e.g., @all) in messages sent to followed topics
should send notifications like a personal mention.Changes: New in Zulip 8.0 (feature level 189).
- desktop_icon_count_display:integerUnread count badge (appears in desktop sidebar and browser tab)1 - All unread messages2 - DMs, mentions, and followed topics3 - DMs and mentions4 - NoneChanges: In Zulip 8.0 (feature level 227), addedDMs, mentions,
and followed topicsoption, renumbering the options to insert it in
order.
- realm_name_in_email_notifications_policy:integerWhether toinclude organization name in subject of message notification
emails.1 - Automatic2 - Always3 - NeverChanges: New in Zulip 7.0 (feature level 168), replacing the
previousrealm_name_in_notificationsboolean;truecorresponded toAlways, andfalsetoNever.
- automatically_follow_topics_policy:integerWhichtopics to follow automatically.1 - Topics the user participates in2 - Topics the user sends a message to3 - Topics the user starts4 - NeverChanges: New in Zulip 8.0 (feature level 214).
- automatically_unmute_topics_in_muted_streams_policy:integerWhichtopics to unmute automatically in muted channels.1 - Topics the user participates in2 - Topics the user sends a message to3 - Topics the user starts4 - NeverChanges: New in Zulip 8.0 (feature level 214).
- automatically_follow_topics_where_mentioned:booleanWhether the server will automatically mark the user as following
topics where the user is mentioned.Changes: New in Zulip 8.0 (feature level 235).
- resolved_topic_notice_auto_read_policy:stringControls whether the resolved-message_topic notices are marked as read."always" - Always mark resolved-message_topic notices as read."except_followed" - Mark resolved-message_topic notices as read in topics not followed by the user."never" - Never mark resolved-message_topic notices as read.Changes: New in Zulip 11.0 (feature level 385).
- presence_enabled:booleanDisplay the presence status to other users when online.
- available_notification_sounds:(string)[]Array containing the names of the notification sound options
supported by this Zulip server. Only relevant to support UI
for configuring notification sounds.
- emojiset_choices:(object)[]Array of dictionaries where each dictionary describes an emoji set
supported by this version of the Zulip server.Only relevant to clients with configuration UI for choosing an emoji set;
the currently selected emoji set is available in theemojisetkey.SeePATCH /settingsfor details on
the meaning of this setting.key:stringThe key or the name of the emoji set which will be the value
ofemojisetif this emoji set is chosen.text:stringThe text describing the emoji set.
- send_private_typing_notifications:booleanWhether the user has chosen to sendtyping
notificationswhen composing direct messages. The client should send typing
notifications for direct messages if and only if this setting is enabled.Changes: New in Zulip 5.0 (feature level 105).
- send_stream_typing_notifications:booleanWhether the user has chosen to sendtyping
notificationswhen composing channel messages. The client should send typing
notifications for channel messages if and only if this setting is enabled.Changes: New in Zulip 5.0 (feature level 105).
- send_read_receipts:booleanWhether other users are allowed to see whether you've
read messages.Changes: New in Zulip 5.0 (feature level 105).
- allow_private_data_export:booleanWhether organization administrators are allowed to
export your private data.Changes: New in Zulip 10.0 (feature level 293).
- email_address_visibility:integerThepolicyforwhich other usersin this organization can see the user's real email address.1 = Everyone2 = Members only3 = Administrators only4 = Nobody5 = Moderators onlyChanges: New in Zulip 7.0 (feature level 163), replacing the
realm-level setting.
- web_navigate_to_sent_message:booleanWeb/desktop app setting for whether the user's view should
automatically go to the conversation where they sent a message.Changes: New in Zulip 9.0 (feature level 268). Previously,
this behavior was not configurable.
- 1 - Always
- 2 - Only in conversation views
- 3 - Never
- 1 - Top message_topic in the channel
- 2 - Channel feed
- 3 - List of topics
- 4 - Top unread message_topic in channel
- 1 - Automatic
- 2 - Dark theme
- 3 - Light theme
- "recent" - Recent conversations view
- "inbox" - Inbox view
- "all_messages" - Combined feed view
- "google" - Google modern
- "twitter" - Twitter
- "text" - Plain text
- 1 - Automatic
- 2 - Always
- 3 - Never
- 1 - Compact
- 2 - With status
- 3 - With avatar and status
- "always" - Always play the animated images in the message feed.
- "on_hover" - Play the animated images on hover over them in the message feed.
- "never" - Never play animated images in the message feed.
- 1 - All channels
- 2 - Unmuted channels and topics
- 3 - No channels
- 1 - All unread messages
- 2 - DMs, mentions, and followed topics
- 3 - DMs and mentions
- 4 - None
- 1 - Automatic
- 2 - Always
- 3 - Never
- 1 - Topics the user participates in
- 2 - Topics the user sends a message to
- 3 - Topics the user starts
- 4 - Never
- 1 - Topics the user participates in
- 2 - Topics the user sends a message to
- 3 - Topics the user starts
- 4 - Never
- "always" - Always mark resolved-message_topic notices as read.
- "except_followed" - Mark resolved-message_topic notices as read in topics not followed by the user.
- "never" - Never mark resolved-message_topic notices as read.
- key:stringThe key or the name of the emoji set which will be the value
ofemojisetif this emoji set is chosen.
- text:stringThe text describing the emoji set.
- 1 = Everyone
- 2 = Members only
- 3 = Administrators only
- 4 = Nobody
- 5 = Moderators only
- stream_id:integerThe ID of the channel to which the message_topic belongs.
- topic_name:stringThe name of the message_topic.Note that the empty string message_topic may have been rewritten by the server to
the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse depending on the value of theempty_topic_nameclient capability.Changes: Theempty_topic_nameclient capability is new in
Zulip 10.0 (feature level 334).
- last_updated:integerAn integer UNIX timestamp representing when the user-message_topic
relationship was changed.
- visibility_policy:integerAn integer indicating the user's visibility configuration for
the message_topic.1 = Muted. Used to recordmuted topics.2 = Unmuted. Used to recordunmuted topics.3 = Followed. Used to recordfollowed topics.Changes: In Zulip 7.0 (feature level 219), added followed as
a visibility policy option.In Zulip 7.0 (feature level 170), added unmuted as a visibility
policy option.

```
POST /register
```
- 1 = Muted. Used to recordmuted topics.
- 2 = Unmuted. Used to recordunmuted topics.
- 3 = Followed. Used to recordfollowed topics.

```
POST /register_client_device
```
- {device_id}:objectDictionary containing the details of
a device with the device ID as the key.push_key_id:integer | nullID to reference the encryption key used to encrypt
push notifications sent to the device.push_token_id:string | nullID to reference the token provided by FCM/APNs to the device,
which is registered to the push bouncer service.pending_push_token_id:string | nullID to reference the token provided by FCM/APNs to the device,
whose registration is in progress to the push bouncer service.push_token_last_updated_timestamp:integer | nullThe UNIX timestamp for the last time whenpending_push_token_idwas set to a new non-null value, in UTC seconds.push_registration_error_code:string | nullIf the push registration failed, aZulip API error
codeindicating the type of
failure that occurred.The following error codes have recommended client behavior:"INVALID_BOUNCER_PUBLIC_KEY"- Inform the user to update app."REQUEST_EXPIRED- Retry with a fresh payload.
- push_key_id:integer | nullID to reference the encryption key used to encrypt
push notifications sent to the device.
- push_token_id:string | nullID to reference the token provided by FCM/APNs to the device,
which is registered to the push bouncer service.
- pending_push_token_id:string | nullID to reference the token provided by FCM/APNs to the device,
whose registration is in progress to the push bouncer service.
- push_token_last_updated_timestamp:integer | nullThe UNIX timestamp for the last time whenpending_push_token_idwas set to a new non-null value, in UTC seconds.
- push_registration_error_code:string | nullIf the push registration failed, aZulip API error
codeindicating the type of
failure that occurred.The following error codes have recommended client behavior:"INVALID_BOUNCER_PUBLIC_KEY"- Inform the user to update app."REQUEST_EXPIRED- Retry with a fresh payload.
- "INVALID_BOUNCER_PUBLIC_KEY"- Inform the user to update app.
- "REQUEST_EXPIRED- Retry with a fresh payload.
- "all" = All edit history is visible.
- "moves" = Only moves are visible.
- "none" = No edit history is visible.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- 1 = All members can create and edit user groups
- 2 = Only organization administrators can create and edit
  user groups
- 3 = Onlyfull memberscan create and
  edit user groups.
- 4 = Only organization administrators and moderators can
  create and edit user groups.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- 1 = Members only
- 2 = Admins only
- 3 =Full membersonly
- 4 = Admins and moderators only
- 1 = Members only
- 2 = Admins only
- 3 =Full membersonly
- 4 = Admins and moderators only
- 2 = Admins only
- 4 = Admins and moderators only
- 6 = Nobody
- 7 = Owners only
- 1 = Any user can use wildcard mentions in large channels.
- 2 = Only members can use wildcard mentions in large channels.
- 3 = Onlyfull memberscan use wildcard mentions in large channels.
- 5 = Only organization administrators can use wildcard mentions in large channels.
- 6 = Nobody can use wildcard mentions in large channels.
- 7 = Only organization administrators and moderators can use wildcard mentions in large channels.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- 100: 100% height (the default).
- 150: 150% height.
- 200: 200% height.
- "allow_empty_topic": Channel messages can be sent to the empty message_topic.
- "disable_empty_topic": Channel messages cannot be sent to the empty message_topic.
- -1denoting that the messages will be retained forever for this realm, by default.
- 0 = None
- 1 = Jitsi Meet
- 3 = Zoom (User OAuth integration)
- 4 = BigBlueButton
- 5 = Zoom (Server to Server OAuth integration)
- 6 = Constructor Groups
- 7 = Nextcloud Talk
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.

```
GET /server_settings
```
- Dictionary describing the properties of an authentication method for the
    organization - its enabled status and availability for use by the
    organization.enabled:booleanBoolean describing whether the authentication method (i.e. its key)
is enabled in this organization.available:booleanBoolean describing whether the authentication method is available for use.
If false, the organization is not eligible to enable the authentication
method.unavailable_reason:stringReason why the authentication method is unavailable. This field is optional
and is only present when 'available' is false.
- enabled:booleanBoolean describing whether the authentication method (i.e. its key)
is enabled in this organization.
- available:booleanBoolean describing whether the authentication method is available for use.
If false, the organization is not eligible to enable the authentication
method.
- unavailable_reason:stringReason why the authentication method is unavailable. This field is optional
and is only present when 'available' is false.

```
PATCH /messages/{message_id}
```

```
PATCH /messages/{message_id}
```

```
PATCH /messages/{message_id}
```

```
PATCH /messages/{message_id}
```
- "G" means generated by Gravatar (the default).
- "U" means uploaded by an organization administrator.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- "D" means the logo is the default Zulip logo.
- "U" means uploaded by an organization administrator.
- "D" means the logo is the default Zulip logo.
- "U" means uploaded by an organization administrator.
- {provider_name}:objectDictionary containing the details of the
video call provider with the name of the chat provider as
the key.name:stringThe name of the video call provider.id:integerThe ID of the video call provider.
- name:stringThe name of the video call provider.
- id:integerThe ID of the video call provider.
- 0 = Unspecified
- 10 = Business
- 20 = Open-source project
- 30 = Education (non-profit)
- 35 = Education (for-profit)
- 40 = Research
- 50 = Event or conference
- 60 = Non-profit (registered)
- 70 = Government
- 80 = Political group
- 90 = Community
- 100 = Personal
- 1000 = Other
- 1 = Self-hosted organization (SELF_HOSTED)
- 2 = Zulip Cloud free plan (LIMITED)
- 3 = Zulip Cloud Standard plan (STANDARD)
- 4 = Zulip Cloud Standard plan, sponsored for free (STANDARD_FREE)
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- {site_name}:objectDictionary containing the details of the
default external account provider with the name of the
website as the key.name:stringThe name of the external account providertext:stringThe text describing the external account.hint:stringThe help text to be displayed for the
custom profile field in user-facing
settings UI for configuring custom
profile fields for this account.url_pattern:stringThe regex pattern of the URL of a profile page
on the external site.
- name:stringThe name of the external account provider
- text:stringThe text describing the external account.
- hint:stringThe help text to be displayed for the
custom profile field in user-facing
settings UI for configuring custom
profile fields for this account.
- url_pattern:stringThe regex pattern of the URL of a profile page
on the external site.
- "G" = Hosted by Gravatar
- "J" = Generated using Jdenticon
- {rating_name}:objectDictionary containing the details of the
rating with the name of the rating as
the key.name:stringThe description of the rating option.id:integerThe ID of the rating option.
- name:stringThe description of the rating option.
- id:integerThe ID of the rating option.
- name:stringThe file path component of the thumbnail format.
- max_width:integerThe maximum width of this format.
- max_height:integerThe maximum height of this format.
- format:stringThe extension of this format.
- animated:booleanIf this file format is animated. These formats
are only generated for uploaded images which
themselves are animated.

```
GET /events
```
- has_pending_sponsorship_request:booleanWhether there is a pending sponsorship request for the organization. Note that
this field will always befalseif the user is not incan_manage_billing_group.Changes: New in Zulip 10.0 (feature level 363).
- twenty_four_hour_time:boolean | nullWhether time should bedisplayed in 24-hour notation.Anullvalue indicates that the client should use the default time
format for the user's locale.Changes: Prior to Zulip 11.0 (feature level 408),nullwas not a valid value for this setting. Note that it was not possible
to actually set the time format tonullat this feature level.New in Zulip 5.0 (feature level 99). This value was previously
available asrealm_default_twenty_four_hour_timein the top-level
response object (only whenrealmwas present infetch_event_types).
- web_mark_read_on_scroll_policy:integerWhether or not to mark messages as read when the user scrolls through their
feed.1 - Always2 - Only in conversation views3 - NeverChanges: New in Zulip 7.0 (feature level 175). Previously, there was no
way for the user to configure this behavior on the web, and the Zulip web and
desktop apps behaved like the "Always" setting when marking messages as read.
- web_channel_default_view:integerWeb/desktop app setting controlling the default navigation
behavior when clicking on a channel link.1 - Top message_topic in the channel2 - Channel feed3 - List of topics4 - Top unread message_topic in channelChanges: The "Top unread message_topic in channel" is new in Zulip 11.0
(feature level 401).In Zulip 11.0 (feature level 383), we added a new option "List of topics"
to this setting.New in Zulip 9.0 (feature level 269). Previously, this
was not configurable, and every user had the "Channel feed" behavior.
- starred_message_counts:booleanWhether clients should display thenumber of starred
messages.
- receives_typing_notifications:booleanWhether the user is configured to receive typing notifications from
other users. The server will only deliver typing notifications events
to users who for whom this is enabled.Changes: New in Zulip 9.0 (feature level 253). Previously, there were
only options to disable sending typing notifications.
- web_suggest_update_timezone:booleanWhether the user should be shown an alert, offering to update theirprofile time zone, when the time displayed
for the profile time zone differs from the current time displayed by the
time zone configured on their device.Changes: New in Zulip 10.0 (feature level 329).
- fluid_layout_width:booleanWhether to use themaximum available screen widthfor the web app's center panel (message feed, recent conversations) on wide screens.
- high_contrast_mode:booleanThis setting is reserved for use to control variations in Zulip's design
to help visually impaired users.
- web_font_size_px:integerUser-configured primaryfont-sizefor the web application, in pixels.Changes: New in Zulip 9.0 (feature level 245). Previously, font size was
only adjustable via browser zoom. Note that this setting was not fully
implemented at this feature level.
- web_line_height_percent:integerUser-configured primaryline-heightfor the web application, in percent, so a
value of 120 represents aline-heightof 1.2.Changes: New in Zulip 9.0 (feature level 245). Previously, line height was
not user-configurable. Note that this setting was not fully implemented at this
feature level.
- color_scheme:integerControls whichcolor themeto use.1 - Automatic2 - Dark theme3 - Light themeAutomatic detection is implementing using the standardprefers-color-schememedia query.
- translate_emoticons:booleanWhether totranslate emoticons to emojiin messages the user sends.
- display_emoji_reaction_users:booleanWhether to display the names of reacting users on a message.When enabled, clients should display the names of reacting
users, rather than a count, for messages with few total
reactions. The ideal cutoff may depend on the space
available for displaying reactions; the official web
application displays names when 3 or fewer total reactions
are present with this setting enabled.Changes: New in Zulip 6.0 (feature level 125).
- default_language:stringWhatdefault languageto use for the account.This controls both the Zulip UI as well as email notifications sent to the user.The value needs to be a standard language code that the Zulip server has
translation data for; for example,"en"for English or"de"for German.
- web_home_view:stringThehome viewused when opening a new
Zulip web app window or hitting theEsckeyboard shortcut repeatedly."recent" - Recent conversations view"inbox" - Inbox view"all_messages" - Combined feed viewChanges: Before Zulip 12.0 (feature level 454), the Recent
view had"recent_topics"as its string encoding.New in Zulip 8.0 (feature level 219). Previously, this was
calleddefault_view, which was new in Zulip 4.0 (feature level 42).
- web_escape_navigates_to_home_view:booleanWhether the escape key navigates to theconfigured home view.Changes: New in Zulip 8.0 (feature level 219). Previously, this
was calledescape_navigates_to_default_view, which was new in Zulip
5.0 (feature level 107).
- left_side_userlist:booleanWhether the users list on left sidebar in filter_spec windows.This feature is not heavily used and is likely to be reworked.
- emojiset:stringThe user's configuredemoji set,
used to display emoji to the user everywhere they appear in the UI."google" - Google modern"twitter" - Twitter"text" - Plain text
- demote_inactive_streams:integerWhether tohide inactive channelsin the left sidebar.1 - Automatic2 - Always3 - Never
- user_list_style:integerThe style selected by the user for the right sidebar user list.1 - Compact2 - With status3 - With avatar and statusChanges: New in Zulip 6.0 (feature level 141).
- web_animate_image_previews:stringControls how animated images should be played in the message feed in the web/desktop application."always" - Always play the animated images in the message feed."on_hover" - Play the animated images on hover over them in the message feed."never" - Never play animated images in the message feed.Changes: New in Zulip 9.0 (feature level 275).
- web_stream_unreads_count_display_policy:integerConfiguration for which channels should be displayed with a numeric unread count in the left sidebar.
Channels that do not have an unread count will have a simple dot indicator for whether there are any
unread messages.1 - All channels2 - Unmuted channels and topics3 - No channelsChanges: New in Zulip 8.0 (feature level 210).
- hide_ai_features:booleanControls whether user wants AI features like message_topic summarization to
be hidden in all Zulip clients.Changes: New in Zulip 10.0 (feature level 350).
- web_inbox_show_channel_folders:booleanDetermines whetherchannel foldersare used to organize how conversations with unread messages
are displayed in the web/desktop application's Inbox view.Changes: New in Zulip 12.0 (feature level 431).
- web_left_sidebar_show_channel_folders:booleanDetermines whetherchannel foldersare used to organize how channels are displayed in the
web/desktop application's left sidebar.Changes: New in Zulip 11.0 (feature level 411).
- web_left_sidebar_unreads_count_summary:booleanDetermines whether the web/desktop application's left sidebar displays
the unread message count summary.Changes: New in Zulip 11.0 (feature level 398).
- enable_stream_desktop_notifications:booleanEnable visual desktop notifications for channel messages.
- enable_stream_email_notifications:booleanEnable email notifications for channel messages.
- enable_stream_push_notifications:booleanEnable mobile notifications for channel messages.
- enable_stream_audible_notifications:booleanEnable audible desktop notifications for channel messages.
- notification_sound:stringNotification sound name.
- enable_desktop_notifications:booleanEnable visual desktop notifications for direct messages and @-mentions.
- enable_sounds:booleanEnable audible desktop notifications for direct messages and
@-mentions.
- enable_offline_email_notifications:booleanEnable email notifications for direct messages and @-mentions received
when the user is offline.
- enable_offline_push_notifications:booleanEnable mobile notification for direct messages and @-mentions received
when the user is offline.
- enable_online_push_notifications:booleanEnable mobile notification for direct messages and @-mentions received
when the user is online.
- enable_followed_topic_desktop_notifications:booleanEnable visual desktop notifications for messages sent to followed topics.Changes: New in Zulip 8.0 (feature level 189).
- enable_followed_topic_email_notifications:booleanEnable email notifications for messages sent to followed topics.Changes: New in Zulip 8.0 (feature level 189).
- enable_followed_topic_push_notifications:booleanEnable push notifications for messages sent to followed topics.Changes: New in Zulip 8.0 (feature level 189).
- enable_followed_topic_audible_notifications:booleanEnable audible desktop notifications for messages sent to followed topics.Changes: New in Zulip 8.0 (feature level 189).
- enable_digest_emails:booleanEnable digest emails when the user is away.
- enable_marketing_emails:booleanEnable marketing emails. Has no function outside Zulip Cloud.
- enable_login_emails:booleanEnable email notifications for new logins to account.
- message_content_in_email_notifications:booleanInclude the message's content in email notifications for new messages.
- pm_content_in_desktop_notifications:booleanInclude content of direct messages in desktop notifications.
- wildcard_mentions_notify:booleanWhether wildcard mentions (E.g. @all) should send notifications
like a personal mention.
- enable_followed_topic_wildcard_mentions_notify:booleanWhether wildcard mentions (e.g., @all) in messages sent to followed topics
should send notifications like a personal mention.Changes: New in Zulip 8.0 (feature level 189).
- desktop_icon_count_display:integerUnread count badge (appears in desktop sidebar and browser tab)1 - All unread messages2 - DMs, mentions, and followed topics3 - DMs and mentions4 - NoneChanges: In Zulip 8.0 (feature level 227), addedDMs, mentions,
and followed topicsoption, renumbering the options to insert it in
order.
- realm_name_in_email_notifications_policy:integerWhether toinclude organization name in subject of message notification
emails.1 - Automatic2 - Always3 - NeverChanges: New in Zulip 7.0 (feature level 168), replacing the
previousrealm_name_in_notificationsboolean;truecorresponded toAlways, andfalsetoNever.
- automatically_follow_topics_policy:integerWhichtopics to follow automatically.1 - Topics the user participates in2 - Topics the user sends a message to3 - Topics the user starts4 - NeverChanges: New in Zulip 8.0 (feature level 214).
- automatically_unmute_topics_in_muted_streams_policy:integerWhichtopics to unmute automatically in muted channels.1 - Topics the user participates in2 - Topics the user sends a message to3 - Topics the user starts4 - NeverChanges: New in Zulip 8.0 (feature level 214).
- automatically_follow_topics_where_mentioned:booleanWhether the server will automatically mark the user as following
topics where the user is mentioned.Changes: New in Zulip 8.0 (feature level 235).
- resolved_topic_notice_auto_read_policy:stringControls whether the resolved-message_topic notices are marked as read."always" - Always mark resolved-message_topic notices as read."except_followed" - Mark resolved-message_topic notices as read in topics not followed by the user."never" - Never mark resolved-message_topic notices as read.Changes: New in Zulip 11.0 (feature level 385).
- presence_enabled:booleanDisplay the presence status to other users when online.
- enter_sends:booleanWhether the user setting forsending on pressing Enterin the compose box is enabled.
- enable_drafts_synchronization:booleanA boolean parameter to control whether synchronizing drafts is enabled for
the user. When synchronization is disabled, all drafts stored in the server
will be automatically deleted from the server.This does not do anything (like sending events) to delete local copies of
drafts stored in clients.
- email_notifications_batching_period_seconds:integerThe duration (in seconds) for which the server should wait to batch
email notifications before sending them.
- available_notification_sounds:(string)[]Array containing the names of the notification sound options
supported by this Zulip server. Only relevant to support UI
for configuring notification sounds.
- emojiset_choices:(object)[]Array of dictionaries where each dictionary describes an emoji set
supported by this version of the Zulip server.Only relevant to clients with configuration UI for choosing an emoji set;
the currently selected emoji set is available in theemojisetkey.SeePATCH /settingsfor details on
the meaning of this setting.key:stringThe key or the name of the emoji set which will be the value
ofemojisetif this emoji set is chosen.text:stringThe text describing the emoji set.
- send_private_typing_notifications:booleanWhethertyping notificationsbe sent when composing
direct messages.Changes: New in Zulip 5.0 (feature level 105).
- send_stream_typing_notifications:booleanWhethertyping notificationsbe sent when composing
channel messages.Changes: New in Zulip 5.0 (feature level 105).
- send_read_receipts:booleanWhether other users are allowed to see whether you've
read messages.Changes: New in Zulip 5.0 (feature level 105).
- allow_private_data_export:booleanWhether organization administrators are allowed to
export your private data.Changes: New in Zulip 10.0 (feature level 293).
- email_address_visibility:integerThepolicyforwhich other usersin this organization can see the user's real email address.1 = Everyone2 = Members only3 = Administrators only4 = Nobody5 = Moderators onlyChanges: New in Zulip 7.0 (feature level 163), replacing the
realm-level setting.
- web_navigate_to_sent_message:booleanWeb/desktop app setting for whether the user's view should
automatically go to the conversation where they sent a message.Changes: New in Zulip 9.0 (feature level 268). Previously,
this behavior was not configurable.
- 1 - Always
- 2 - Only in conversation views
- 3 - Never
- 1 - Top message_topic in the channel
- 2 - Channel feed
- 3 - List of topics
- 4 - Top unread message_topic in channel
- 1 - Automatic
- 2 - Dark theme
- 3 - Light theme
- "recent" - Recent conversations view
- "inbox" - Inbox view
- "all_messages" - Combined feed view
- "google" - Google modern
- "twitter" - Twitter
- "text" - Plain text
- 1 - Automatic
- 2 - Always
- 3 - Never
- 1 - Compact
- 2 - With status
- 3 - With avatar and status
- "always" - Always play the animated images in the message feed.
- "on_hover" - Play the animated images on hover over them in the message feed.
- "never" - Never play animated images in the message feed.
- 1 - All channels
- 2 - Unmuted channels and topics
- 3 - No channels
- 1 - All unread messages
- 2 - DMs, mentions, and followed topics
- 3 - DMs and mentions
- 4 - None
- 1 - Automatic
- 2 - Always
- 3 - Never
- 1 - Topics the user participates in
- 2 - Topics the user sends a message to
- 3 - Topics the user starts
- 4 - Never
- 1 - Topics the user participates in
- 2 - Topics the user sends a message to
- 3 - Topics the user starts
- 4 - Never
- "always" - Always mark resolved-message_topic notices as read.
- "except_followed" - Mark resolved-message_topic notices as read in topics not followed by the user.
- "never" - Never mark resolved-message_topic notices as read.
- key:stringThe key or the name of the emoji set which will be the value
ofemojisetif this emoji set is chosen.
- text:stringThe text describing the emoji set.
- 1 = Everyone
- 2 = Members only
- 3 = Administrators only
- 4 = Nobody
- 5 = Moderators only
- user_id:integerThe unique ID of the user.
- delivery_email:string | nullThe user's real email address. This value will benullif you cannot
access user's real email address. For bot users, this field is always
set to the real email of the bot, because bot users always haveemail_address_visibilityset to everyone.Changes: Prior to Zulip 7.0 (feature level 163), this field was
present only whenemail_address_visibilitywas restricted and you had
access to the user's real email. As of this feature level, this field
is always present, including the case whenemail_address_visibilityis set to everyone (and therefore not restricted).
- email:stringThe Zulip API email address of the user or bot.If you do not have permission to view the email address of the target user,
this will be a fake email address that is usable for the Zulip API but nothing else.
- full_name:stringFull name of the user or bot, used for all display purposes.
- date_joined:stringThe time when the user joined. For users imported from other
applications and users created via the API, this is set to the
account creation time until the user logs in for the first time,
after which it is updated to that login time.For imported users, clients can use theis_imported_stubflag
to determine how to display this field: whenis_imported_stubistrue, the user has not yet logged in and this value is the
account creation time during import; whenis_imported_stubisfalse, this value reflects when the user first logged in.Changes: Starting with Zulip 12.0 (feature level 475),
this field is updated when an imported stub user or a user created
via the API logs in for the first time.
- is_active:booleanA boolean specifying whether the user account has been deactivated.
- is_owner:booleanA boolean specifying whether the user is an organization owner.
If true,is_adminwill also be true.Changes: New in Zulip 3.0 (feature level 8).
- is_admin:booleanA boolean specifying whether the user is an organization administrator.
- is_guest:booleanA boolean specifying whether the user is a guest user.
- is_bot:booleanA boolean specifying whether the user is a bot or full account.
- bot_type:integer | nullAn integer describing the type of bot:nullif the user isn't a bot.1for aGenericbot.2for anIncoming webhookbot.3for anOutgoing webhookbot.4for anEmbeddedbot.
- bot_owner_id:integer | nullIf the user is a bot (i.e.is_botis true), thenbot_owner_idis the user ID of the bot's owner (usually, whoever created the bot).Will benullfor legacy bots that do not have an owner.Changes: New in Zulip 3.0 (feature level 1). In previous
versions, there was abot_ownerfield containing the email
address of the bot's owner.
- role:integerOrganization-level roleof the user.
Possible values are:100 = Organization owner200 = Organization administrator300 = Organization moderator400 = Member600 = GuestChanges: New in Zulip 4.0 (feature level 59).
- timezone:stringThe IANA identifier of the user'sprofile time zone,
which is used primarily to display the user's local time to other users.
- avatar_url:string | nullURL for the user's avatar.Will benullif theclient_gravatarquery parameter was set totrue, the current user has access to
this user's real email address, and this user's avatar is hosted by
the Gravatar provider (i.e. this user has never uploaded an avatar).Changes: Before Zulip 7.0 (feature level 163), access to a
user's real email address was a realm-level setting. As of this
feature level,email_address_visibilityis a user setting.In Zulip 3.0 (feature level 18), if the client has theuser_avatar_url_field_optionalcapability, this will be missing at
the server's sole discretion.
- avatar_version:integerVersion for the user's avatar. Used for cache-busting requests
for the user's avatar. Clients generally shouldn't need to use this;
most avatar URLs sent by Zulip will already end with?v={avatar_version}.
- is_imported_stub:booleanIndicates whether this user object is a stub account imported from
another chat system. Stub accounts are used to represent the senders
for imported messages. Stub accounts can be converted to regular Zulip
accounts when the user starts using Zulip, preserving that imported
user's message history.Changes: New in Zulip 12.0 (feature level 433).
- profile_data:objectOnly present ifis_botis false; bots can't have custom profile fields.A dictionary containing custom profile field data for the user. Each entry
maps the integer ID of a custom profile field in the organization to a
dictionary containing the user's data for that field. Generally the data
includes just a singlevaluekey; for those custom profile fields
supporting Markdown, arendered_valuekey will also be present.{id}:objectObject with data about what value the user filled in the custom
profile field with that ID.value:stringUser's personal value for this custom profile field.rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- nullif the user isn't a bot.
- 1for aGenericbot.
- 2for anIncoming webhookbot.
- 3for anOutgoing webhookbot.
- 4for anEmbeddedbot.
- 100 = Organization owner
- 200 = Organization administrator
- 300 = Organization moderator
- 400 = Member
- 600 = Guest
- {id}:objectObject with data about what value the user filled in the custom
profile field with that ID.value:stringUser's personal value for this custom profile field.rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- value:stringUser's personal value for this custom profile field.
- rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- user_id:integerThe unique ID of the user.
- delivery_email:string | nullThe user's real email address. This value will benullif you cannot
access user's real email address. For bot users, this field is always
set to the real email of the bot, because bot users always haveemail_address_visibilityset to everyone.Changes: Prior to Zulip 7.0 (feature level 163), this field was
present only whenemail_address_visibilitywas restricted and you had
access to the user's real email. As of this feature level, this field
is always present, including the case whenemail_address_visibilityis set to everyone (and therefore not restricted).
- email:stringThe Zulip API email address of the user or bot.If you do not have permission to view the email address of the target user,
this will be a fake email address that is usable for the Zulip API but nothing else.
- full_name:stringFull name of the user or bot, used for all display purposes.
- date_joined:stringThe time when the user joined. For users imported from other
applications and users created via the API, this is set to the
account creation time until the user logs in for the first time,
after which it is updated to that login time.For imported users, clients can use theis_imported_stubflag
to determine how to display this field: whenis_imported_stubistrue, the user has not yet logged in and this value is the
account creation time during import; whenis_imported_stubisfalse, this value reflects when the user first logged in.Changes: Starting with Zulip 12.0 (feature level 475),
this field is updated when an imported stub user or a user created
via the API logs in for the first time.
- is_active:booleanA boolean specifying whether the user account has been deactivated.
- is_owner:booleanA boolean specifying whether the user is an organization owner.
If true,is_adminwill also be true.Changes: New in Zulip 3.0 (feature level 8).
- is_admin:booleanA boolean specifying whether the user is an organization administrator.
- is_guest:booleanA boolean specifying whether the user is a guest user.
- is_bot:booleanA boolean specifying whether the user is a bot or full account.
- bot_type:integer | nullAn integer describing the type of bot:nullif the user isn't a bot.1for aGenericbot.2for anIncoming webhookbot.3for anOutgoing webhookbot.4for anEmbeddedbot.
- bot_owner_id:integer | nullIf the user is a bot (i.e.is_botis true), thenbot_owner_idis the user ID of the bot's owner (usually, whoever created the bot).Will benullfor legacy bots that do not have an owner.Changes: New in Zulip 3.0 (feature level 1). In previous
versions, there was abot_ownerfield containing the email
address of the bot's owner.
- role:integerOrganization-level roleof the user.
Possible values are:100 = Organization owner200 = Organization administrator300 = Organization moderator400 = Member600 = GuestChanges: New in Zulip 4.0 (feature level 59).
- timezone:stringThe IANA identifier of the user'sprofile time zone,
which is used primarily to display the user's local time to other users.
- avatar_url:string | nullURL for the user's avatar.Will benullif theclient_gravatarquery parameter was set totrue, the current user has access to
this user's real email address, and this user's avatar is hosted by
the Gravatar provider (i.e. this user has never uploaded an avatar).Changes: Before Zulip 7.0 (feature level 163), access to a
user's real email address was a realm-level setting. As of this
feature level,email_address_visibilityis a user setting.In Zulip 3.0 (feature level 18), if the client has theuser_avatar_url_field_optionalcapability, this will be missing at
the server's sole discretion.
- avatar_version:integerVersion for the user's avatar. Used for cache-busting requests
for the user's avatar. Clients generally shouldn't need to use this;
most avatar URLs sent by Zulip will already end with?v={avatar_version}.
- is_imported_stub:booleanIndicates whether this user object is a stub account imported from
another chat system. Stub accounts are used to represent the senders
for imported messages. Stub accounts can be converted to regular Zulip
accounts when the user starts using Zulip, preserving that imported
user's message history.Changes: New in Zulip 12.0 (feature level 433).
- profile_data:objectOnly present ifis_botis false; bots can't have custom profile fields.A dictionary containing custom profile field data for the user. Each entry
maps the integer ID of a custom profile field in the organization to a
dictionary containing the user's data for that field. Generally the data
includes just a singlevaluekey; for those custom profile fields
supporting Markdown, arendered_valuekey will also be present.{id}:objectObject with data about what value the user filled in the custom
profile field with that ID.value:stringUser's personal value for this custom profile field.rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- nullif the user isn't a bot.
- 1for aGenericbot.
- 2for anIncoming webhookbot.
- 3for anOutgoing webhookbot.
- 4for anEmbeddedbot.
- 100 = Organization owner
- 200 = Organization administrator
- 300 = Organization moderator
- 400 = Member
- 600 = Guest
- {id}:objectObject with data about what value the user filled in the custom
profile field with that ID.value:stringUser's personal value for this custom profile field.rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- value:stringUser's personal value for this custom profile field.
- rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- "G" = Hosted by Gravatar
- "J" = Generated using Jdenticon
- "U" = Uploaded by user
- user_id:integerThe unique ID of the user.
- delivery_email:string | nullThe user's real email address. This value will benullif you cannot
access user's real email address. For bot users, this field is always
set to the real email of the bot, because bot users always haveemail_address_visibilityset to everyone.Changes: Prior to Zulip 7.0 (feature level 163), this field was
present only whenemail_address_visibilitywas restricted and you had
access to the user's real email. As of this feature level, this field
is always present, including the case whenemail_address_visibilityis set to everyone (and therefore not restricted).
- email:stringThe Zulip API email address of the user or bot.If you do not have permission to view the email address of the target user,
this will be a fake email address that is usable for the Zulip API but nothing else.
- full_name:stringFull name of the user or bot, used for all display purposes.
- date_joined:stringThe time when the user joined. For users imported from other
applications and users created via the API, this is set to the
account creation time until the user logs in for the first time,
after which it is updated to that login time.For imported users, clients can use theis_imported_stubflag
to determine how to display this field: whenis_imported_stubistrue, the user has not yet logged in and this value is the
account creation time during import; whenis_imported_stubisfalse, this value reflects when the user first logged in.Changes: Starting with Zulip 12.0 (feature level 475),
this field is updated when an imported stub user or a user created
via the API logs in for the first time.
- is_active:booleanA boolean specifying whether the user account has been deactivated.
- is_owner:booleanA boolean specifying whether the user is an organization owner.
If true,is_adminwill also be true.Changes: New in Zulip 3.0 (feature level 8).
- is_admin:booleanA boolean specifying whether the user is an organization administrator.
- is_guest:booleanA boolean specifying whether the user is a guest user.
- is_bot:booleanA boolean specifying whether the user is a bot or full account.
- bot_type:integer | nullAn integer describing the type of bot:nullif the user isn't a bot.1for aGenericbot.2for anIncoming webhookbot.3for anOutgoing webhookbot.4for anEmbeddedbot.
- bot_owner_id:integer | nullIf the user is a bot (i.e.is_botis true), thenbot_owner_idis the user ID of the bot's owner (usually, whoever created the bot).Will benullfor legacy bots that do not have an owner.Changes: New in Zulip 3.0 (feature level 1). In previous
versions, there was abot_ownerfield containing the email
address of the bot's owner.
- role:integerOrganization-level roleof the user.
Possible values are:100 = Organization owner200 = Organization administrator300 = Organization moderator400 = Member600 = GuestChanges: New in Zulip 4.0 (feature level 59).
- timezone:stringThe IANA identifier of the user'sprofile time zone,
which is used primarily to display the user's local time to other users.
- avatar_url:string | nullURL for the user's avatar.Will benullif theclient_gravatarquery parameter was set totrue, the current user has access to
this user's real email address, and this user's avatar is hosted by
the Gravatar provider (i.e. this user has never uploaded an avatar).Changes: Before Zulip 7.0 (feature level 163), access to a
user's real email address was a realm-level setting. As of this
feature level,email_address_visibilityis a user setting.In Zulip 3.0 (feature level 18), if the client has theuser_avatar_url_field_optionalcapability, this will be missing at
the server's sole discretion.
- avatar_version:integerVersion for the user's avatar. Used for cache-busting requests
for the user's avatar. Clients generally shouldn't need to use this;
most avatar URLs sent by Zulip will already end with?v={avatar_version}.
- is_imported_stub:booleanIndicates whether this user object is a stub account imported from
another chat system. Stub accounts are used to represent the senders
for imported messages. Stub accounts can be converted to regular Zulip
accounts when the user starts using Zulip, preserving that imported
user's message history.Changes: New in Zulip 12.0 (feature level 433).
- is_system_bot:booleanWhether the user is a system bot. System bots are special
bot user accounts that are managed by the system, rather than
the organization's administrators.Changes: This field was calledis_cross_realm_botbefore Zulip 5.0 (feature level 83).
- nullif the user isn't a bot.
- 1for aGenericbot.
- 2for anIncoming webhookbot.
- 3for anOutgoing webhookbot.
- 4for anEmbeddedbot.
- 100 = Organization owner
- 200 = Organization administrator
- 300 = Organization moderator
- 400 = Member
- 600 = Guest
- key:stringThe unique ID for the report message type.
- name:stringThe user-facing string for the report message type, to be
displayed in the report message UI, in the user's language.
Note that the actual report will use the name for this type
in the organization's default language.
- realm:objectConfiguration for realm level group permission settings.Configuration for a group permission setting specifying the groups
    to which the setting can be set to and the default values for the
    setting.Changes: Removedallow_owners_groupfield in Zulip 10.0 (feature level 326), as we now
support anonymous user groups. Previously, therole:ownerssystem group was
not offered whenallow_owners_groupwas false.Removed unnecessaryid_field_namefield in Zulip 10.0 (feature level 326). Previously,
this always had the value of"{setting_name}_id"; it was an internal implementation
detail of the server not intended to be included in the API.require_system_group:booleanWhether the setting can only be set to a system user group.allow_internet_group:booleanWhether the setting can be set torole:internetsystem group.allow_nobody_group:booleanWhether the setting can be set torole:nobodysystem group.allow_everyone_group:booleanWhether the setting can be set torole:everyonesystem group.If false, guest users cannot exercise this permission even if they are part of
thegroup-setting valuefor this setting.default_group_name:stringName of the default system group for the setting.For some channel settings, this can also bechannel_creator.
In that case:If the channel'screator_idis notnull, default for the
  setting is an anonymous group with the channel creator as
  the only member.If the channel'screator_idisnull, default for the setting
  isrole:nobodysystem group.Changes: In Zulip 12.0 (feature level 427), renamedstream_creator_or_nobodyvalue tochannel_creator.default_for_system_groups:string | nullName of the default group for the setting for system groups.This is non-null only for group-level settings.allowed_system_groups:(string)[]An array of names of system groups to which the setting can
be set to.If the list is empty, the setting can be set to system groups
based on the other boolean fields.Changes: New in Zulip 8.0 (feature level 225).
- channel_name:objectConfiguration for channel level group permission settings.Configuration for a group permission setting specifying the groups
    to which the setting can be set to and the default values for the
    setting.Changes: Removedallow_owners_groupfield in Zulip 10.0 (feature level 326), as we now
support anonymous user groups. Previously, therole:ownerssystem group was
not offered whenallow_owners_groupwas false.Removed unnecessaryid_field_namefield in Zulip 10.0 (feature level 326). Previously,
this always had the value of"{setting_name}_id"; it was an internal implementation
detail of the server not intended to be included in the API.require_system_group:booleanWhether the setting can only be set to a system user group.allow_internet_group:booleanWhether the setting can be set torole:internetsystem group.allow_nobody_group:booleanWhether the setting can be set torole:nobodysystem group.allow_everyone_group:booleanWhether the setting can be set torole:everyonesystem group.If false, guest users cannot exercise this permission even if they are part of
thegroup-setting valuefor this setting.default_group_name:stringName of the default system group for the setting.For some channel settings, this can also bechannel_creator.
In that case:If the channel'screator_idis notnull, default for the
  setting is an anonymous group with the channel creator as
  the only member.If the channel'screator_idisnull, default for the setting
  isrole:nobodysystem group.Changes: In Zulip 12.0 (feature level 427), renamedstream_creator_or_nobodyvalue tochannel_creator.default_for_system_groups:string | nullName of the default group for the setting for system groups.This is non-null only for group-level settings.allowed_system_groups:(string)[]An array of names of system groups to which the setting can
be set to.If the list is empty, the setting can be set to system groups
based on the other boolean fields.Changes: New in Zulip 8.0 (feature level 225).
- group:objectConfiguration for group level group permission settings.Configuration for a group permission setting specifying the groups
    to which the setting can be set to and the default values for the
    setting.Changes: Removedallow_owners_groupfield in Zulip 10.0 (feature level 326), as we now
support anonymous user groups. Previously, therole:ownerssystem group was
not offered whenallow_owners_groupwas false.Removed unnecessaryid_field_namefield in Zulip 10.0 (feature level 326). Previously,
this always had the value of"{setting_name}_id"; it was an internal implementation
detail of the server not intended to be included in the API.require_system_group:booleanWhether the setting can only be set to a system user group.allow_internet_group:booleanWhether the setting can be set torole:internetsystem group.allow_nobody_group:booleanWhether the setting can be set torole:nobodysystem group.allow_everyone_group:booleanWhether the setting can be set torole:everyonesystem group.If false, guest users cannot exercise this permission even if they are part of
thegroup-setting valuefor this setting.default_group_name:stringName of the default system group for the setting.For some channel settings, this can also bechannel_creator.
In that case:If the channel'screator_idis notnull, default for the
  setting is an anonymous group with the channel creator as
  the only member.If the channel'screator_idisnull, default for the setting
  isrole:nobodysystem group.Changes: In Zulip 12.0 (feature level 427), renamedstream_creator_or_nobodyvalue tochannel_creator.default_for_system_groups:string | nullName of the default group for the setting for system groups.This is non-null only for group-level settings.allowed_system_groups:(string)[]An array of names of system groups to which the setting can
be set to.If the list is empty, the setting can be set to system groups
based on the other boolean fields.Changes: New in Zulip 8.0 (feature level 225).
- Configuration for a group permission setting specifying the groups
    to which the setting can be set to and the default values for the
    setting.Changes: Removedallow_owners_groupfield in Zulip 10.0 (feature level 326), as we now
support anonymous user groups. Previously, therole:ownerssystem group was
not offered whenallow_owners_groupwas false.Removed unnecessaryid_field_namefield in Zulip 10.0 (feature level 326). Previously,
this always had the value of"{setting_name}_id"; it was an internal implementation
detail of the server not intended to be included in the API.require_system_group:booleanWhether the setting can only be set to a system user group.allow_internet_group:booleanWhether the setting can be set torole:internetsystem group.allow_nobody_group:booleanWhether the setting can be set torole:nobodysystem group.allow_everyone_group:booleanWhether the setting can be set torole:everyonesystem group.If false, guest users cannot exercise this permission even if they are part of
thegroup-setting valuefor this setting.default_group_name:stringName of the default system group for the setting.For some channel settings, this can also bechannel_creator.
In that case:If the channel'screator_idis notnull, default for the
  setting is an anonymous group with the channel creator as
  the only member.If the channel'screator_idisnull, default for the setting
  isrole:nobodysystem group.Changes: In Zulip 12.0 (feature level 427), renamedstream_creator_or_nobodyvalue tochannel_creator.default_for_system_groups:string | nullName of the default group for the setting for system groups.This is non-null only for group-level settings.allowed_system_groups:(string)[]An array of names of system groups to which the setting can
be set to.If the list is empty, the setting can be set to system groups
based on the other boolean fields.Changes: New in Zulip 8.0 (feature level 225).
- require_system_group:booleanWhether the setting can only be set to a system user group.
- allow_internet_group:booleanWhether the setting can be set torole:internetsystem group.
- allow_nobody_group:booleanWhether the setting can be set torole:nobodysystem group.
- allow_everyone_group:booleanWhether the setting can be set torole:everyonesystem group.If false, guest users cannot exercise this permission even if they are part of
thegroup-setting valuefor this setting.
- default_group_name:stringName of the default system group for the setting.For some channel settings, this can also bechannel_creator.
In that case:If the channel'screator_idis notnull, default for the
  setting is an anonymous group with the channel creator as
  the only member.If the channel'screator_idisnull, default for the setting
  isrole:nobodysystem group.Changes: In Zulip 12.0 (feature level 427), renamedstream_creator_or_nobodyvalue tochannel_creator.
- default_for_system_groups:string | nullName of the default group for the setting for system groups.This is non-null only for group-level settings.
- allowed_system_groups:(string)[]An array of names of system groups to which the setting can
be set to.If the list is empty, the setting can be set to system groups
based on the other boolean fields.Changes: New in Zulip 8.0 (feature level 225).
- If the channel'screator_idis notnull, default for the
  setting is an anonymous group with the channel creator as
  the only member.
- If the channel'screator_idisnull, default for the setting
  isrole:nobodysystem group.
- Configuration for a group permission setting specifying the groups
    to which the setting can be set to and the default values for the
    setting.Changes: Removedallow_owners_groupfield in Zulip 10.0 (feature level 326), as we now
support anonymous user groups. Previously, therole:ownerssystem group was
not offered whenallow_owners_groupwas false.Removed unnecessaryid_field_namefield in Zulip 10.0 (feature level 326). Previously,
this always had the value of"{setting_name}_id"; it was an internal implementation
detail of the server not intended to be included in the API.require_system_group:booleanWhether the setting can only be set to a system user group.allow_internet_group:booleanWhether the setting can be set torole:internetsystem group.allow_nobody_group:booleanWhether the setting can be set torole:nobodysystem group.allow_everyone_group:booleanWhether the setting can be set torole:everyonesystem group.If false, guest users cannot exercise this permission even if they are part of
thegroup-setting valuefor this setting.default_group_name:stringName of the default system group for the setting.For some channel settings, this can also bechannel_creator.
In that case:If the channel'screator_idis notnull, default for the
  setting is an anonymous group with the channel creator as
  the only member.If the channel'screator_idisnull, default for the setting
  isrole:nobodysystem group.Changes: In Zulip 12.0 (feature level 427), renamedstream_creator_or_nobodyvalue tochannel_creator.default_for_system_groups:string | nullName of the default group for the setting for system groups.This is non-null only for group-level settings.allowed_system_groups:(string)[]An array of names of system groups to which the setting can
be set to.If the list is empty, the setting can be set to system groups
based on the other boolean fields.Changes: New in Zulip 8.0 (feature level 225).
- require_system_group:booleanWhether the setting can only be set to a system user group.
- allow_internet_group:booleanWhether the setting can be set torole:internetsystem group.
- allow_nobody_group:booleanWhether the setting can be set torole:nobodysystem group.
- allow_everyone_group:booleanWhether the setting can be set torole:everyonesystem group.If false, guest users cannot exercise this permission even if they are part of
thegroup-setting valuefor this setting.
- default_group_name:stringName of the default system group for the setting.For some channel settings, this can also bechannel_creator.
In that case:If the channel'screator_idis notnull, default for the
  setting is an anonymous group with the channel creator as
  the only member.If the channel'screator_idisnull, default for the setting
  isrole:nobodysystem group.Changes: In Zulip 12.0 (feature level 427), renamedstream_creator_or_nobodyvalue tochannel_creator.
- default_for_system_groups:string | nullName of the default group for the setting for system groups.This is non-null only for group-level settings.
- allowed_system_groups:(string)[]An array of names of system groups to which the setting can
be set to.If the list is empty, the setting can be set to system groups
based on the other boolean fields.Changes: New in Zulip 8.0 (feature level 225).
- If the channel'screator_idis notnull, default for the
  setting is an anonymous group with the channel creator as
  the only member.
- If the channel'screator_idisnull, default for the setting
  isrole:nobodysystem group.
- Configuration for a group permission setting specifying the groups
    to which the setting can be set to and the default values for the
    setting.Changes: Removedallow_owners_groupfield in Zulip 10.0 (feature level 326), as we now
support anonymous user groups. Previously, therole:ownerssystem group was
not offered whenallow_owners_groupwas false.Removed unnecessaryid_field_namefield in Zulip 10.0 (feature level 326). Previously,
this always had the value of"{setting_name}_id"; it was an internal implementation
detail of the server not intended to be included in the API.require_system_group:booleanWhether the setting can only be set to a system user group.allow_internet_group:booleanWhether the setting can be set torole:internetsystem group.allow_nobody_group:booleanWhether the setting can be set torole:nobodysystem group.allow_everyone_group:booleanWhether the setting can be set torole:everyonesystem group.If false, guest users cannot exercise this permission even if they are part of
thegroup-setting valuefor this setting.default_group_name:stringName of the default system group for the setting.For some channel settings, this can also bechannel_creator.
In that case:If the channel'screator_idis notnull, default for the
  setting is an anonymous group with the channel creator as
  the only member.If the channel'screator_idisnull, default for the setting
  isrole:nobodysystem group.Changes: In Zulip 12.0 (feature level 427), renamedstream_creator_or_nobodyvalue tochannel_creator.default_for_system_groups:string | nullName of the default group for the setting for system groups.This is non-null only for group-level settings.allowed_system_groups:(string)[]An array of names of system groups to which the setting can
be set to.If the list is empty, the setting can be set to system groups
based on the other boolean fields.Changes: New in Zulip 8.0 (feature level 225).
- require_system_group:booleanWhether the setting can only be set to a system user group.
- allow_internet_group:booleanWhether the setting can be set torole:internetsystem group.
- allow_nobody_group:booleanWhether the setting can be set torole:nobodysystem group.
- allow_everyone_group:booleanWhether the setting can be set torole:everyonesystem group.If false, guest users cannot exercise this permission even if they are part of
thegroup-setting valuefor this setting.
- default_group_name:stringName of the default system group for the setting.For some channel settings, this can also bechannel_creator.
In that case:If the channel'screator_idis notnull, default for the
  setting is an anonymous group with the channel creator as
  the only member.If the channel'screator_idisnull, default for the setting
  isrole:nobodysystem group.Changes: In Zulip 12.0 (feature level 427), renamedstream_creator_or_nobodyvalue tochannel_creator.
- default_for_system_groups:string | nullName of the default group for the setting for system groups.This is non-null only for group-level settings.
- allowed_system_groups:(string)[]An array of names of system groups to which the setting can
be set to.If the list is empty, the setting can be set to system groups
based on the other boolean fields.Changes: New in Zulip 8.0 (feature level 225).
- If the channel'screator_idis notnull, default for the
  setting is an anonymous group with the channel creator as
  the only member.
- If the channel'screator_idisnull, default for the setting
  isrole:nobodysystem group.

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"last_event_id":-1,"msg":"","queue_id":"fb67bf8a-c031-47cc-84cf-ed80accacda8","realm_emoji":{"1":{"author_id":5,"deactivated":false,"id":"1","name":"green_tick","source_url":"/user_avatars/1/emoji/images/1.png"},"2":{"author_id":3,"deactivated":false,"id":"2","name":"animated_img","source_url":"/user_avatars/1/emoji/images/animated_img.gif","still_url":"/user_avatars/1/emoji/images/still/animated_img.png"}},"result":"success","zulip_feature_level":2,"zulip_merge_base":"5.0-dev-1646-gea6b21cd8c","zulip_version":"5.0-dev-1650-gc3fd37755f"}
```

```
{"last_event_id":-1,"msg":"","queue_id":"fb67bf8a-c031-47cc-84cf-ed80accacda8","realm_emoji":{"1":{"author_id":5,"deactivated":false,"id":"1","name":"green_tick","source_url":"/user_avatars/1/emoji/images/1.png"},"2":{"author_id":3,"deactivated":false,"id":"2","name":"animated_img","source_url":"/user_avatars/1/emoji/images/animated_img.gif","still_url":"/user_avatars/1/emoji/images/still/animated_img.png"}},"result":"success","zulip_feature_level":2,"zulip_merge_base":"5.0-dev-1646-gea6b21cd8c","zulip_version":"5.0-dev-1650-gc3fd37755f"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.