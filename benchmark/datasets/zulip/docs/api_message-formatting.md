# Message formatting | Zulip API documentation

*Source: https://zulip.com/api/message-formatting*

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

# Message formatting
Zulip supports an extended version of Markdown for messages, as well as
some HTML level special behavior. The Zulip help center article onmessage
formattingis the primary
documentation for Zulip's markup features. This article is currently a
changelog for updates to these features.
Therender a messageendpoint can be used to get
the current HTML version of any Markdown syntax for message content.

## Code blocks
Changes: As of Zulip 4.0 (feature level 33),code blockscan have adata-code-languageattribute attached to the outer HTMLdivelement, which records the programming language that was selected
for syntax highlighting. This field is used in theplaygroundsfeature for code blocks.

## Global times
Changes: In Zulip 12.0 (feature level 451), invalid timestamp formats
are now rendered as escaped literal text instead of a<span>element withtimestamp-errorclass and an error message.
Previously, an invalid timestamp string would be rendered as:

```
<spanclass="timestamp-error">Invalid time format: invalid</span>
```

```
<spanclass="timestamp-error">Invalid time format: invalid</span>
```
Now, it is rendered as:

```
&lt;time:invalid&gt;
```

```
&lt;time:invalid&gt;
```
Changes: In Zulip 3.0 (feature level 8), addedglobal time
mentionsto supported Markdown message formatting
features.

## Links to channels, topics, and messages
Zulip's markup supports special readable Markdown syntax forlinking
to channels, topics, and
messages. See alsoZulip
URLs
Sample HTML formats are as follows:

```
<!-- Syntax: #**announce** --><aclass="stream"data-stream-id="9"href="/#narrow/channel/9-announce">#announce</a><!-- Syntax: #**announce>Zulip updates** --><aclass="stream-topic"data-stream-id="9"href="/#narrow/channel/9-announce/topic/Zulip.20updates/with/214">#announce&gt;Zulip updates</a><!-- Syntax: #**announce>Zulip updates**Generated only if topic had no messages or the link was renderedbefore Zulip 10.0 (feature level 347) --><aclass="stream-topic"data-stream-id="9"href="/#narrow/channel/9-announce/topic/Zulip.20updates">#announce&gt;Zulip updates</a><!-- Syntax: #**announce>Zulip updates@214** --><aclass="message-link"href="/#narrow/channel/9-announce/topic/Zulip.20updates/near/214">#announce&gt;Zulip updates @ 💬</a>
```

```
<!-- Syntax: #**announce** --><aclass="stream"data-stream-id="9"href="/#narrow/channel/9-announce">#announce</a><!-- Syntax: #**announce>Zulip updates** --><aclass="stream-topic"data-stream-id="9"href="/#narrow/channel/9-announce/topic/Zulip.20updates/with/214">#announce&gt;Zulip updates</a><!-- Syntax: #**announce>Zulip updates**Generated only if topic had no messages or the link was renderedbefore Zulip 10.0 (feature level 347) --><aclass="stream-topic"data-stream-id="9"href="/#narrow/channel/9-announce/topic/Zulip.20updates">#announce&gt;Zulip updates</a><!-- Syntax: #**announce>Zulip updates@214** --><aclass="message-link"href="/#narrow/channel/9-announce/topic/Zulip.20updates/near/214">#announce&gt;Zulip updates @ 💬</a>
```
Thenearandwithoperators are documented in more detail in thesearch and URL documentation. When rendering
topic links with thewithoperator, the code doing the rendering may
pick the ID arbitrarily among messages accessible to the client and/or
acting user at the time of rendering. Currently, the server chooses
the message ID to use forwithoperators as the latest message ID in
the topic accessible to the user who wrote the message.
The older stream/topic link elements include adata-stream-id, which
historically was used in order to display the current channel name if
the channel had been renamed. That field isdeprecated, because
displaying an updated value for the most common forms of this syntax
requires parsing the URL to get the topic to use anyway.
When a topic is an empty string, it is replaced withrealm_empty_topic_display_namefound in thePOST /registerresponse and wrapped with the<em>tag.

```
POST /register
```
Sample HTML formats with"realm_empty_topic_display_name": "general chat"are as follows:

```
<!-- Syntax: #**announce>** --><aclass="stream-topic"data-stream-id="9"href="/#narrow/channel/9-announce/topic/with/214">#announce&gt;<em>general chat</em></a><!-- Syntax: #**announce>**Generated only if topic had no messages or the link was renderedbefore Zulip 10.0 (feature level 347) --><aclass="stream-topic"data-stream-id="9"href="/#narrow/channel/9-announce/topic/">#announce&gt;<em>general chat</em></a><!-- Syntax: #**announce>@214** --><aclass="message-link"href="/#narrow/channel/9-announce/topic//near/214">#announce&gt;<em>general chat</em>@ 💬</a>
```

```
<!-- Syntax: #**announce>** --><aclass="stream-topic"data-stream-id="9"href="/#narrow/channel/9-announce/topic/with/214">#announce&gt;<em>general chat</em></a><!-- Syntax: #**announce>**Generated only if topic had no messages or the link was renderedbefore Zulip 10.0 (feature level 347) --><aclass="stream-topic"data-stream-id="9"href="/#narrow/channel/9-announce/topic/">#announce&gt;<em>general chat</em></a><!-- Syntax: #**announce>@214** --><aclass="message-link"href="/#narrow/channel/9-announce/topic//near/214">#announce&gt;<em>general chat</em>@ 💬</a>
```
Changes: In Zulip 11.0 (feature level 400), the server switched
its strategy forwithURL construction to choose the latest
accessible message ID in a topic. Previously, it used the oldest.
Before Zulip 10.0 (feature level 347), thewithfield
was never used in topic link URLs generated by the server; the markup
currently used only for empty topics was used for all topic links.
Before Zulip 10.0 (feature level 346), empty string
was not a valid topic name in syntaxes for linking to topics and
messages.
In Zulip 10.0 (feature level 319), added Markdown syntax
for linking to a specific message in a conversation. Declared thedata-stream-idfield to be deprecated as detailed above.
In Zulip 11.0 (feature level 383), clients can decide what
channel view a.stream channel link elements take you to -- i.e.,
the href for those is the default behavior of the link that also
encodes the channel alongside the data-stream-id field, but clients
can override that default based onweb_channel_default_viewsetting.

## Emoji
Zulip'semojisupport includes standard Unicode emoji, a
built-in Zulip custom emoji like:zulip:andcustom realm
emoji. To maximize legibility, emoji should be
displayed inline with text, at the maximum size that does not
interfere with line spacing.
Large emoji. Clients are recommended to display single-paragraph
messages that contain only emoji elements with a greatly increased
size. For example, Zulip the web app scales large emoji to be 2x the
size of other message emoji.
Unicode emoji, such as:smiling_face:(☺️ /263a), are represented
in the HTML by spans with the following format:

```
<spanaria-label="smiling face"class="emoji emoji-263a"role="img"title="smiling face">:smiling_face:</span>
```

```
<spanaria-label="smiling face"class="emoji emoji-263a"role="img"title="smiling face">:smiling_face:</span>
```
Note that Unicode emoji in messages that were originally sent on Zulip
versions older than Zulip 1.9.2 will not have theroleoraria-labelattributes. Thus, clients should not rely on those fields
existing.
Theserver_emoji_data_urlkey in thePOST
/registerresponse contains the server's
mapping between Unicode codepoints and emoji names.

```
POST
/register
```
Custom emoji are represented in the HTML by image tags that also use
the.emojiclass. ThesrcURL should be resolved with respect to
the Zulip server's hostname:

```
<--Configuredrealm-specificcustomemoji--><imgalt=":example_custom_emoji:"class="emoji"title="example_custom_emoji"src="/user_avatars/2/emoji/images/dbe43627.png"><--Built-incustomemojilike:zulip:--><imgalt=":zulip:"class="emoji"title="zulip"src="/static/generated/emoji/images/emoji/unicode/zulip.png">
```

```
<--Configuredrealm-specificcustomemoji--><imgalt=":example_custom_emoji:"class="emoji"title="example_custom_emoji"src="/user_avatars/2/emoji/images/dbe43627.png"><--Built-incustomemojilike:zulip:--><imgalt=":zulip:"class="emoji"title="zulip"src="/static/generated/emoji/images/emoji/unicode/zulip.png">
```
Changes: Large emoji are new in Zulip 12.0 (feature level 436).

## Images
When a Zulip message is sent with a link to an uploaded image, Zulip will
also insert an image preview element with the following format:

```
<divclass="message_inline_image"><ahref="/user_uploads/path/to/example.png"title="example.png"><imgdata-original-dimensions="1920x1080"data-original-content-type="image/png"src="/user_uploads/thumbnail/path/to/example.png/840x560.webp"></a></div>
```

```
<divclass="message_inline_image"><ahref="/user_uploads/path/to/example.png"title="example.png"><imgdata-original-dimensions="1920x1080"data-original-content-type="image/png"src="/user_uploads/thumbnail/path/to/example.png/840x560.webp"></a></div>
```
Clients can recognize if an image was thumbnailed by itssrcattribute starting with/user_uploads/thumbnail/.  Thehrefwill
always link to the originally-uploaded file, at its original
resolution.
When a Zulip message is sent referencing anuploaded imagein Markdown
image syntax, (e.g.,![example image](/user_uploads/path/to/example.png)),
Zulip will generate an image element with the following format:

```
<imgalt="example image"class="inline-image"data-original-dimensions="1050x700"data-original-content-type="image/png"data-original-src="/user_uploads/path/to/example.png"src="/user_uploads/thumbnail/path/to/example.png/840x560.webp">
```

```
<imgalt="example image"class="inline-image"data-original-dimensions="1050x700"data-original-content-type="image/png"data-original-src="/user_uploads/path/to/example.png"src="/user_uploads/thumbnail/path/to/example.png/840x560.webp">
```
Note that the Markdown image syntax is only supported/permitted for
uploaded images, not third-party image URLs.
As with link-derived image previews, clients can recognize if an image
was thumbnailed by itssrcattribute starting with/user_uploads/thumbnail/.  If an image is a thumbnail, thedata-original-srcattribute will always reference the
originally-uploaded file, at its original resolution.
Note that images generated using Markdown image syntax may appear
inside arbitrary block-level elements, unlike the image previews from
links, which will always be top-level elements.
Regardless of which form (link-derived preview, or Markdown image
syntax), thedata-original-dimensionsanddata-original-content-typeattributes will only be present if the
image was thumbnailed and the message was sent (or last edited)
after those attributes were added (seeChanges to image
formatting).  If the image isnota
thumbnail, clients should make a best-effort attempt to render the
givensrc, in a manner which minimizes layout shift when the
resource is loaded -- see the next section for a special case of this.
Changes: SeeChanges to image formatting.

### Image-loading placeholders
If the server has yet to generate thumbnails for the image by the time
the message is sent, theimgelement will temporarily reference a
loading indicator image and have theimage-loading-placeholderclass, which clients can use to identify loading indicators and
replace them with a more native loading indicator element if desired.
This spinner placeholder will havedata-original-dimensionsanddata-original-content-typeattributes
if the message was sent (or last edited) after those attributes were added
(seeChanges to image formatting).
In link-derived image previews, the placeholder is structured like this:

```
<divclass="message_inline_image"><ahref="/user_uploads/path/to/example.png"title="example.png"><imgclass="image-loading-placeholder"data-original-dimensions="1920x1080"data-original-content-type="image/png"src="/path/to/spinner.png"></a></div>
```

```
<divclass="message_inline_image"><ahref="/user_uploads/path/to/example.png"title="example.png"><imgclass="image-loading-placeholder"data-original-dimensions="1920x1080"data-original-content-type="image/png"src="/path/to/spinner.png"></a></div>
```
For image elements presented in Markdown image syntax, this placeholder
structure is used:

```
<imgalt="example image"class="inline-image image-loading-placeholder"data-original-content-type="image/png"data-original-dimensions="1050x700"data-original-src="/user_uploads/path/to/example.png"src="/path/to/spinner.png">
```

```
<imgalt="example image"class="inline-image image-loading-placeholder"data-original-content-type="image/png"data-original-dimensions="1050x700"data-original-src="/user_uploads/path/to/example.png"src="/path/to/spinner.png">
```
Once the server has a working thumbnail, such messages will be updated
via anupdate_messageevent, with therendering_only: trueflag
(telling clients not to adjust message edit history), with appropriate
adjustedrendered_content. A client should process those events by
just using the updated rendering. If thumbnailing failed, the same
type of event will edit the message's rendered form to remove the
image preview element, so no special client-side logic should be
required to process such errors.
Note that in the uncommon situation that the thumbnailing system is
backlogged, an individual message containing multiple image previews
may be re-rendered multiple times as each image finishes thumbnailing
and triggers a message update.
Clients displaying message-edit history should rewrite image-loading
placeholder images in edit history to the generic deleted-file image
(/static/images/errors/image-not-exist.png).

### Transcoded images
Image elements whose formats are not widely supported by web browsers
(e.g., HEIC and TIFF) may contain adata-transcoded-imageattribute,
which specifies a high-resolution thumbnail format that clients may
opt to present instead of the original image. If thedata-transcoded-imageattribute is present, clients should use thedata-original-content-typeattribute to decide whether to display the
original image or use the transcoded version.
Transcoded images are presented with this structure in image previews:

```
<divclass="message_inline_image"><ahref="/user_uploads/path/to/example.heic"title="example.heic"><imgdata-original-dimensions="1920x1080"data-original-content-type="image/heic"data-transcoded-image="1920x1080.webp"src="/user_uploads/thumbnail/path/to/example.heic/840x560.webp"></a></div>
```

```
<divclass="message_inline_image"><ahref="/user_uploads/path/to/example.heic"title="example.heic"><imgdata-original-dimensions="1920x1080"data-original-content-type="image/heic"data-transcoded-image="1920x1080.webp"src="/user_uploads/thumbnail/path/to/example.heic/840x560.webp"></a></div>
```
Transcoded images presented in Markdown image syntax are structured like this:

```
<imgalt="example HEIC image"class="inline-image"data-original-dimensions="1920x1080"data-original-content-type="image/heic"data-original-src="/user_uploads/path/to/example.heic"data-transcoded-image="1920x1080.webp"src="/user_uploads/thumbnail/path/to/example.heic/840x560.webp">
```

```
<imgalt="example HEIC image"class="inline-image"data-original-dimensions="1920x1080"data-original-content-type="image/heic"data-original-src="/user_uploads/path/to/example.heic"data-transcoded-image="1920x1080.webp"src="/user_uploads/thumbnail/path/to/example.heic/840x560.webp">
```

### Recommended client processing of image previews
Clients are recommended to do the following when processing image
previews:
- Clients that would like to use the image's aspect ratio to lay out
  one or more images in the message feed may use thedata-original-dimensionsattribute, which is present even if the
  image is a placeholder spinner.  This attribute encodes the
  dimensions of the original image as{width}x{height}.  These
  dimensions are for the image as rendered,afterany EXIF rotation
  and mirroring has been applied.
- If the client would like to control the thumbnail resolution used,
  it can replace the final section of the URL (840x560.webpin the
  example above) with thenameof its preferred format from the set
  of supported formats provided by the server in theserver_thumbnail_formatsportion of theregisterresponse. Clients should not make any assumptions about what format
  the server will use as the "default" thumbnail resolution, as it may
  change over time.
- Download button type elements should provide the original image
  (encoded via thehrefof the containingatag).
- The content-type of the original image is provided on adata-original-content-typeattribute, so clients can decide if
  they are capable of rendering the original image.
- For images whose formats which are not widely-accepted by browsers
  (e.g., HEIC and TIFF), the image may contain adata-transcoded-imageattribute, which specifies a high-resolution
  thumbnail format which clients may use instead of the original
  image.
- Lightbox elements for viewing an image should be designed to
  immediately display any already-downloaded thumbnail while fetching
  the original-quality image or an appropriate higher-quality
  thumbnail from the server, to be transparently swapped in once it is
  available. Clients that would like to size the lightbox based on the
  size of the original image can use thedata-original-dimensionsattribute, as described above.
- Animated images will have adata-animatedattribute on theimgtag. As detailed inserver_thumbnail_formats, both animated and
  still images are available for clients to use, depending on their
  preference. See, for example, theweb settingto control whether animated images are autoplayed in the message
  feed.
- Clients should not assume that the requested format is the format
  that they will receive; in rare cases where the client has an
  out-of-date list ofserver_thumbnail_formats, the server will
  provide an approximation of the client's requested format.  Because
  of this, clients should not assume that the pixel dimensions or file
  format match what they requested.
- No other processing of the URLs is recommended.

### Changes to image formatting
In Zulip 12.0(feature level 467), limited the Markdown
image syntax to only support uploaded images, not linking to
third-party image URLs.
In Zulip 12.0(feature level 437), added support for Markdown
image syntax, in addition to the previous link-derived image previews;
these can be inserted into any block-level element.
In Zulip 10.0(feature level 336), addeddata-original-content-typeattribute to convey the type of the
original image, and optionaldata-transcoded-imageattribute for
images with formats which are not widely supported by browsers.
In Zulip 9.2(feature levels 278-279, and 287+), addeddata-original-dimensionsto theimage-loading-placeholderspinner
images, containing the dimensions of the original image.
In Zulip 9.0(feature level 276), addeddata-original-dimensionsattribute to images that have been thumbnailed, containing the
dimensions of the full-size version of the image. Thumbnailing itself
was reintroduced at feature level 275.
Previously, with the exception of Zulip servers that used the beta
Thumbor-based implementation years ago, all image previews in Zulip
messages were not thumbnailed; theatag and theimgtag would both
point to the original image.
Clients that correctly implement the current API should handle
Thumbor-based older thumbnails correctly, as long as they do not
assume thatdata-original-dimensionsis present. Clients should not
assume that messages sent prior to the introduction of thumbnailing
have been re-rendered to use the new format or have thumbnails
available.

## Video embeddings and previews
When a Zulip message is sent linking to an uploaded video, Zulip may
generate a video preview element with the following format.

```
<divclass="message_inline_image message_inline_video"><ahref="/user_uploads/path/to/video.mp4"><videopreload="metadata"src="/user_uploads/path/to/video.mp4"></video></a></div>
```

```
<divclass="message_inline_image message_inline_video"><ahref="/user_uploads/path/to/video.mp4"><videopreload="metadata"src="/user_uploads/path/to/video.mp4"></video></a></div>
```

## Audio Players
When the Markdown media syntax is used with an uploaded file with an
audioContent-Type, Zulip will generate an HTML5<audio>player
element. Supported MIME types are currentlyaudio/aac,audio/flac,audio/mpeg, andaudio/wav.
For example,![file.mp3](/user_uploads/path/to/file.mp3)renders as:

```
<audiocontrolspreload="metadata"src="/user_uploads/path/to/file.mp3"title="file.mp3"></audio>
```

```
<audiocontrolspreload="metadata"src="/user_uploads/path/to/file.mp3"title="file.mp3"></audio>
```
If the Zulip server has rewritten the URL of the audio file, it will
provide the URL in adata-original-urlparameter. The Zulip server
does this for all non-uploaded file audio URLs.

```
<audiocontrolspreload="metadata"data-original-url="https://example.com/path/to/original/file.mp3"src="https://zulipcdn.example.com/path/to/playable/file.mp3"title="file.mp3"></audio>
```

```
<audiocontrolspreload="metadata"data-original-url="https://example.com/path/to/original/file.mp3"src="https://zulipcdn.example.com/path/to/playable/file.mp3"title="file.mp3"></audio>
```
Clients that cannot render an audio player are recommended to convert
audio elements into a link to the original URL.
The Zulip server does not validate whether uploaded files with an
audioContent-Typeare actually playable.
Changes: New in Zulip 11.0 (feature level 405).

## Mentions and silent mentions
Zulip markup supportsmentioningusers, user groups, and a few special "wildcard" mentions (the three
spellings of a channel wildcard mention:@**all**,@**everyone**,@**channel**and the topic wildcard mention@**topic**).
Mentions result in a message being highlighted for the target user(s),
both in the UI and in notifications, and may also result in the target
user(s) following the conversation,depending on their
settings.
Silent mentions of users or groups have none of those side effects,
but nonetheless uniquely identify the user or group
identified. (There's no such thing as a silent wildcard mention).
Permissions for mentioning users work as follows:
- Any user can mention any other user, though mentions bymuted
usersare automatically marked as read and thus do
not trigger notifications or otherwise get highlighted like unread
mentions.
- Wildcard mentions are permitted except whereorganization-level
restrictionsapply.
- User groups can be mentioned if and only if the acting user is in
thecan_mention_groupgroup for that group. All user groups can be
silently mentioned by any user.
- System groups, when (silently) mentioned, should be displayed using
their description, not theirrole:nobodystyle API names; see the
mainsystem group
documentationfor
details. System groups can only be silently mentioned right now,
because they happen to all use the emptyNobodygroup forcan_mention_group; clients should just usecan_mention_groupto
determine which groups to offer in typeahead in similar contexts.
- Requests to send or edit a message that are impermissible due to
including a mention where the acting user does not have permission to
mention the target will return an error. Mention syntax that does not
correspond to a real user or group is ignored.
Sample markup for@**Example User**:

```
<spanclass="user-mention"data-user-id="31">@Example User</span>
```

```
<spanclass="user-mention"data-user-id="31">@Example User</span>
```
Sample markup for@_**Example User**:

```
<spanclass="user-mention silent"data-user-id="31">Example User</span>
```

```
<spanclass="user-mention silent"data-user-id="31">Example User</span>
```
Sample markup for@**topic**:

```
<spanclass="topic-mention">@topic</span>
```

```
<spanclass="topic-mention">@topic</span>
```
Sample markup for@**channel**:

```
<spanclass="user-mention channel-wildcard-mention"data-user-id="*">@channel</span>
```

```
<spanclass="user-mention channel-wildcard-mention"data-user-id="*">@channel</span>
```
Sample markup for@*support*, assuming "support" is a valid group:

```
<spanclass="user-group-mention"data-user-group-id="17">@support</span>
```

```
<spanclass="user-group-mention"data-user-group-id="17">@support</span>
```
Sample markup for@_*support*, assuming "support" is a valid group:

```
<spanclass="user-group-mention silent"data-user-group-id="17">support</span>
```

```
<spanclass="user-group-mention silent"data-user-group-id="17">support</span>
```
Sample markup for@_*role:administrators*:

```
<spanclass="user-group-mention silent"data-user-group-id="5">Administrators</span>
```

```
<spanclass="user-group-mention silent"data-user-group-id="5">Administrators</span>
```
When processing mentions, clients should look up the user or group
referenced by ID, and update the textual name for the mention to the
current name for the user or group with that ID. Note that for system
groups, this requires special logic to look up the user-facing name
for that group; seesystem
groupsfor details.
Changes: Prior to Zulip 10.0 (feature level 333), it was not
possible to silently mentionsystem
groups.
In Zulip 9.0 (feature level 247),channelwas added to the supportedwildcardoptions used in thementionsMarkdown message formatting feature.

## Spoilers
Changes: In Zulip 3.0 (feature level 15), addedspoilersto supported Markdown message formatting
features.

## Removed features

### Removed legacy Dropbox link preview markup
In Zulip 11.0 (feature level 395), the Zulip server stopped generating
legacy Dropbox link previews. Dropbox links are now previewed just
like standard Zulip image/link previews. However, some legacy Dropbox
previews may exist in existing messages.
Clients are recommended to prune these previews from message HTML;
since they always appear after the actual link, there is no loss of
information/functionality. They can be recognized via the classesmessage_inline_ref,message_inline_image_desc, andmessage_inline_image_title:

```
<divclass="message_inline_ref"><ahref="https://www.dropbox.com/sh/cm39k9e04z7fhim/AAAII5NK-9daee3FcF41anEua?dl="title="Saves"><imgsrc="/path/to/folder_dropbox.png"></a><div><divclass="message_inline_image_title">Saves</div><descclass="message_inline_image_desc"></desc></div></div>
```

```
<divclass="message_inline_ref"><ahref="https://www.dropbox.com/sh/cm39k9e04z7fhim/AAAII5NK-9daee3FcF41anEua?dl="title="Saves"><imgsrc="/path/to/folder_dropbox.png"></a><div><divclass="message_inline_image_title">Saves</div><descclass="message_inline_image_desc"></desc></div></div>
```

### Removed legacy avatar markup
In Zulip 4.0 (feature level 24), the rarely used!avatar()and!gravatar()markup syntax, which was never documented and had an
inconsistent syntax, were removed.

## Related articles
- Markdown formatting
- Send a message
- Render a message
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.