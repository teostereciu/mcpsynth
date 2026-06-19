# Retrieve event occurrences

*Source: https://developers.hubspot.com/docs/api-reference/latest/events/retrieve-events/get-events*

---

Retrieve events

# Retrieve event occurrences

Retrieve event occurrences for the specified time frame. This endpoint allows filtering by various parameters such as object type, event type, and occurrence time. It supports pagination and sorting of results.

GET

/

events

/

event-occurrences

/

2026-03

Try it

Retrieve event occurrences

cURL


    curl --request GET \
      --url https://api.hubapi.com/events/event-occurrences/2026-03 \
      --header 'Authorization: Bearer <token>'

200

default


    {
      "results": [
        {
          "eventType": "<string>",
          "id": "<string>",
          "objectId": "<string>",
          "objectType": "<string>",
          "occurredAt": "2023-11-07T05:31:56Z",
          "properties": {}
        }
      ],
      "paging": {
        "next": {
          "after": "<string>",
          "link": "<string>"
        },
        "prev": {
          "before": "<string>",
          "link": "<string>"
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

#### Query Parameters

​

after

string

A cursor token for pagination. Use the value from the previous response's paging.next.after field.

​

before

string

A cursor token to retrieve results before a specific point.

​

eventType

string

The type of event to filter by.

​

id

string[]

An array of event IDs to filter by.

​

limit

integer<int32>

The maximum number of results to display per page.

​

objectId

integer<int64>

The unique identifier of the object associated with the events.

​

objectProperty.{propname}

object

Filter events by specific object properties.

​

objectType

string

The type of object associated with the events.

​

occurredAfter

string<date-time>

Filter events that occurred after this date-time.

​

occurredBefore

string<date-time>

Filter events that occurred before this date-time.

​

properties

string[]

An array of property names to include in the response.

​

property.{propname}

object

Filter events by specific event properties.

​

sort

string[]

An array of fields to sort the results by.

#### Response

200

application/json

successful operation

​

results

object[]

required

An array of ExternalUnifiedEvent objects, each representing an individual event occurrence.

Show child attributes

​

paging

object

Show child attributes

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)