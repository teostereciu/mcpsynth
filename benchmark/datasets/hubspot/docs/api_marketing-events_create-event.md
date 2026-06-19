# Create an event

*Source: https://developers.hubspot.com/docs/api-reference/legacy/marketing/marketing-events/create-event*

---

Marketing Events

# Create an event

Creates a new marketing event in HubSpot

POST

/

marketing

/

v3

/

marketing-events

/

events

Try it

Create a marketing event

cURL


    curl --request POST \
      --url https://api.hubapi.com/marketing/v3/marketing-events/events \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "customProperties": [
        {
          "dataSensitivity": "high",
          "isEncrypted": true,
          "isLargeValue": true,
          "name": "<string>",
          "persistenceTimestamp": 123,
          "requestId": "<string>",
          "selectedByUser": true,
          "selectedByUserTimestamp": 123,
          "source": "ACADEMY",
          "sourceId": "<string>",
          "sourceLabel": "<string>",
          "sourceMetadata": "<string>",
          "sourceUpstreamDeployable": "<string>",
          "sourceVid": [
            123
          ],
          "timestamp": 123,
          "unit": "<string>",
          "updatedByUserId": 123,
          "useTimestampAsPersistenceTimestamp": true,
          "value": "<string>"
        }
      ],
      "eventName": "<string>",
      "eventOrganizer": "<string>",
      "externalAccountId": "<string>",
      "externalEventId": "<string>",
      "endDateTime": "2023-11-07T05:31:56Z",
      "eventCancelled": true,
      "eventCompleted": true,
      "eventDescription": "<string>",
      "eventType": "<string>",
      "eventUrl": "<string>",
      "startDateTime": "2023-11-07T05:31:56Z"
    }
    '

200

default


    {
      "customProperties": [
        {
          "dataSensitivity": "high",
          "isEncrypted": true,
          "isLargeValue": true,
          "name": "<string>",
          "persistenceTimestamp": 123,
          "requestId": "<string>",
          "selectedByUser": true,
          "selectedByUserTimestamp": 123,
          "source": "ACADEMY",
          "sourceId": "<string>",
          "sourceLabel": "<string>",
          "sourceMetadata": "<string>",
          "sourceUpstreamDeployable": "<string>",
          "sourceVid": [
            123
          ],
          "timestamp": 123,
          "unit": "<string>",
          "updatedByUserId": 123,
          "useTimestampAsPersistenceTimestamp": true,
          "value": "<string>"
        }
      ],
      "eventName": "<string>",
      "eventOrganizer": "<string>",
      "endDateTime": "2023-11-07T05:31:56Z",
      "eventCancelled": true,
      "eventCompleted": true,
      "eventDescription": "<string>",
      "eventType": "<string>",
      "eventUrl": "<string>",
      "objectId": "<string>",
      "startDateTime": "2023-11-07T05:31:56Z"
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

#### Body

application/json

​

customProperties

object[]

required

A list of PropertyValues. These can be whatever kind of property names and values you want. However, they must already exist on the HubSpot account's definition of the MarketingEvent Object. If they don't they will be filtered out and not set. In order to do this you'll need to create a new PropertyGroup on the HubSpot account's MarketingEvent object for your specific app and create the Custom Property you want to track on that HubSpot account. Do not create any new default properties on the MarketingEvent object as that will apply to all HubSpot accounts.

Show child attributes

​

eventName

string

required

The name of the marketing event.

​

eventOrganizer

string

required

The name of the organizer of the marketing event.

​

externalAccountId

string

required

The accountId that is associated with this marketing event in the external event application.

​

externalEventId

string

required

The id of the marketing event in the external event application.

​

endDateTime

string<date-time>

The end date and time of the marketing event.

​

eventCancelled

boolean

Indicates if the marketing event has been cancelled. Defaults to `false`

​

eventCompleted

boolean

Indicates if the marketing event has been completed. Defaults to `false`

​

eventDescription

string

The description of the marketing event.

​

eventType

string

Describes what type of event this is. For example: `WEBINAR`, `CONFERENCE`, `WORKSHOP`

​

eventUrl

string

A URL in the external event application where the marketing event can be managed.

​

startDateTime

string<date-time>

The start date and time of the marketing event.

#### Response

200

application/json

successful operation

​

customProperties

object[]

required

A list of PropertyValues. These can be whatever kind of property names and values you want. However, they must already exist on the HubSpot account's definition of the MarketingEvent Object. If they don't they will be filtered out and not set. In order to do this you'll need to create a new PropertyGroup on the HubSpot account's MarketingEvent object for your specific app and create the Custom Property you want to track on that HubSpot account. Do not create any new default properties on the MarketingEvent object as that will apply to all HubSpot accounts.

Show child attributes

​

eventName

string

required

The name of the marketing event.

​

eventOrganizer

string

required

The name of the organizer of the marketing event.

​

endDateTime

string<date-time>

The end date and time of the marketing event.

​

eventCancelled

boolean

Indicates if the marketing event has been cancelled.

​

eventCompleted

boolean

Indicates if the marketing event has been completed.

​

eventDescription

string

The description of the marketing event.

​

eventType

string

The type of the marketing event.

​

eventUrl

string

The URL in the external event application where the marketing event can be managed.

​

objectId

string

The ID of the marketing event CRM object

​

startDateTime

string<date-time>

The start date and time of the marketing event.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)