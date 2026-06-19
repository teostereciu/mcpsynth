# Get a single message

*Source: https://developers.hubspot.com/docs/api-reference/legacy/conversations/conversations/messages/get-conversation*

---

Messages

# Get a single message

Retrieve a single message from a thread using the message ID.

GET

/

conversations

/

v3

/

conversations

/

threads

/

{threadId}

/

messages

/

{messageId}

Try it

Get a single message

cURL


    curl --request GET \
      --url https://api.hubapi.com/conversations/v3/conversations/threads/{threadId}/messages/{messageId} \
      --header 'Authorization: Bearer <token>'

200

default


    {
      "type": "MESSAGE",
      "id": "<string>",
      "conversationsThreadId": "<string>",
      "createdAt": "2023-11-07T05:31:56Z",
      "createdBy": "<string>",
      "client": {
        "clientType": "HUBSPOT",
        "integrationAppId": 123
      },
      "senders": [
        {
          "actorId": "<string>",
          "deliveryIdentifier": {
            "type": "CHANNEL_SPECIFIC_OPAQUE_ID",
            "value": "<string>"
          },
          "name": "<string>",
          "senderField": "<string>"
        }
      ],
      "recipients": [
        {
          "deliveryIdentifier": {
            "type": "CHANNEL_SPECIFIC_OPAQUE_ID",
            "value": "<string>"
          },
          "actorId": "<string>",
          "name": "<string>",
          "recipientField": "<string>"
        }
      ],
      "archived": true,
      "text": "<string>",
      "attachments": [
        {
          "fileId": "<string>",
          "fileUsageType": "AUDIO",
          "type": "FILE",
          "name": "<string>",
          "url": "<string>"
        }
      ],
      "truncationStatus": "NOT_TRUNCATED",
      "direction": "INCOMING",
      "channelId": "<string>",
      "channelAccountId": "<string>",
      "updatedAt": "2023-11-07T05:31:56Z",
      "richText": "<string>",
      "subject": "<string>",
      "inReplyToId": "<string>",
      "status": {
        "statusType": "FAILED",
        "failureDetails": {
          "errorMessageTokens": {},
          "errorMessage": "<string>"
        }
      }
    }

Supported products

Required Scopes

#### Authorizations

oauth2private_appsoauth2private_apps

​

Authorization

string

header

required

The access token received from the authorization server in the OAuth 2.0 flow.

#### Path Parameters

​

messageId

string

required

​

threadId

integer<int64>

required

#### Query Parameters

​

property

string

#### Response

200

application/json

successful operation

  * Option 1

  * Option 2

  * Option 3

  * Option 4

  * Option 5

  * Option 6


​

type

enum<string>

default:MESSAGE

required

Available options:

`MESSAGE`

​

id

string

required

​

conversationsThreadId

string

required

​

createdAt

string<date-time>

required

​

createdBy

string

required

​

client

object

required

Show child attributes

​

senders

object[]

required

Show child attributes

​

recipients

object[]

required

Show child attributes

​

archived

boolean

required

​

text

string

required

​

attachments

(FILE · object | LOCATION · object | CONTACT · object | UNSUPPORTED_CONTENT · object | MESSAGE_HEADER · object | QUICK_REPLIES · object | WHATSAPP_TEMPLATE_METADATA · object | SOCIAL_MEDIA_METADATA · object)[]

required

  * FILE

  * LOCATION

  * CONTACT

  * UNSUPPORTED_CONTENT

  * MESSAGE_HEADER

  * QUICK_REPLIES

  * WHATSAPP_TEMPLATE_METADATA

  * SOCIAL_MEDIA_METADATA


Show child attributes

​

truncationStatus

enum<string>

required

Available options:

`NOT_TRUNCATED`,

`TRUNCATED_TO_MOST_RECENT_REPLY`,

`TRUNCATED`

​

direction

enum<string>

required

Available options:

`INCOMING`,

`OUTGOING`

​

channelId

string

required

​

channelAccountId

string

required

​

updatedAt

string<date-time>

​

richText

string

​

subject

string

​

inReplyToId

string

​

status

object

Show child attributes

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)