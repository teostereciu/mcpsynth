# Conversations Media Resource

*Source: https://www.twilio.com/docs/conversations/api/media-resource*

---

# Conversations Media Resource

Positive FeedbackNegative Feedback

* * *

The Media resource in Twilio's Media Content Service allows you to upload/download files for use in other Twilio products. You can attach these media files to [Conversation Messages](/docs/conversations/api/conversation-message-resource "Conversation Messages") as part of the [Media Messaging](/docs/conversations/media-support-conversations "Media Messaging") feature.

**Note:** The Media REST resource is accessed via a separate sub-domain from Chat and other Twilio products. The base URL for Media via the Media Content Service (MCS) is:

Copy code block


    https://mcs.us1.twilio.com/v1

* * *

## Authentication

authentication page anchor

Positive FeedbackNegative Feedback

To authenticate requests to the Twilio APIs, Twilio supports [HTTP Basic authentication(link takes you to an external page)](https://en.wikipedia.org/wiki/Basic_access_authentication "HTTP Basic authentication"). Use your _API key_ as the username and your _API key secret_ as the password. You can create an API key either [in the Twilio Console](/docs/iam/api-keys/keys-in-console "in the Twilio Console") or [using the API](/docs/iam/api-keys/key-resource-v1 "using the API").

**Note** : Twilio recommends using API keys for authentication in production apps. For local testing, you can use your Account SID as the username and your Auth token as the password. You can find your Account SID and Auth Token in the [Twilio Console(link takes you to an external page)](https://www.twilio.com/console "Twilio Console").

Learn more about [Twilio API authentication](/docs/usage/requests-to-twilio "Twilio API authentication").

Copy code block


    1

    curl -G https://mcs.us1.twilio.com/v1/Services \


    2

        -u $TWILIO_API_KEY:$TWILIO_API_KEY_SECRET

(information)

## Info

You can't use the Twilio server-side SDKs or the Twilio CLI to make requests to the Media resource.

* * *

## Properties

properties page anchor

Positive FeedbackNegative Feedback

Each Media resource instance has these properties:

name| description
---|---
sid| A 34-character string that uniquely identifies this resource.
account_sid| The unique id of the [Account](/docs/iam/api/account "Account") responsible for this message.
service_sid| The unique id of the [Chat Service](/docs/chat/rest/service-resource "Chat Service") this message belongs to.
date_created| The date that this resource was created.
date_updated| The date that this resource was last updated, `null` if the message has not been edited.
channel_sid| The unique id of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") (same as the underlying [Chat Channel](/docs/chat/channels "Chat Channel")) containing the [Message](/docs/conversations/api/conversation-message-resource "Message") that this media instance was added to.
message_sid| The unique id of the [Conversation Message](/docs/conversations/api/conversation-message-resource "Conversation Message") this media instance was added to.
size| The size of the file this Media instance represents in BYTES
content_type| The MIME type of the file this Media instance represents. Please refer to the [MIME Types(link takes you to an external page)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types "MIME Types") for a list of valid MIME types.
file_name| The filename of the underlying media file as specified when uploaded
author| The identity of the [User](/docs/conversations/api/user-resource "User") that uploaded the Media instance. This is automatically set to `sender` when using the REST API.
url| An absolute URL for this media instance
links| Links to access the underlying media file (`content`) and a temporary URL to use to access this (`content_direct_temporary`)

* * *

## Create/Upload a new Media resource

createupload-a-new-media-resource page anchor

Positive FeedbackNegative Feedback

Copy code block


    POST /Services/{Chat Service SID}/Media

**Note** : The Chat Service SID must be the Chat Service Instance that this Media instance will be used for. You can find the Chat Service SID as a property of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") to which you want to add a new media message.

To create a new media instance, you should upload the media file itself as content on the `POST` request. (See Curl Example below.)

Ultimately, this will be converted into a `POST` request, containing the following headers and the file itself as the request body.

### Headers

headers page anchor

Positive FeedbackNegative Feedback

name| description
---|---
`Content-Type`| The MIME type of the file this Media instance represents. Please refer to the [MIME Types(link takes you to an external page)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types "MIME Types") for a list of valid MIME types. This should be set explicitly by the API caller or automatically detected by the client.
`Content-Size`| The size of the media (the file) being uploaded in bytes

### Body

body page anchor

Positive FeedbackNegative Feedback

The body or content of the `POST` must be the file itself in binary format.

### Curl Example

curl-example page anchor

Positive FeedbackNegative Feedback

Copy code block


    curl -u "<account_sid>:<account_secret>" --data-binary @<filename.png> -H "Content-Type: <content-type of upload>" https://mcs.us1.twilio.com/v1/Services/<chat_service_sid>/Media

* * *

## Retrieve a Media resource

retrieve-a-media-resource page anchor

Positive FeedbackNegative Feedback

You can retrieve an uploaded Media resource by issuing a `GET` request with the SID of the media instance:

Copy code block


    GET /Services/{Chat Service SID}/Media/{Media SID}

### Curl Example for retrieving a media resource

curl-example-for-retrieving-a-media-resource page anchor

Positive FeedbackNegative Feedback

Copy code block


    curl -u "<account_sid>:<account_secret>" -G https://mcs.us1.twilio.com/v1/Services/<chat_service_sid>/Media/<Media SID>