# Retrieve event types

*Source: https://developers.hubspot.com/docs/api-reference/latest/events/retrieve-events/get-event-types*

---

Retrieve events

# Retrieve event types

Retrieve a list of visible external event type names for the specified event occurrences in March 2026. This endpoint is useful for identifying the types of events that are available for analysis or reporting within your HubSpot account.

GET

/

events

/

event-occurrences

/

2026-03

/

event-types

Try it

Retrieve event types

cURL


    curl --request GET \
      --url https://api.hubapi.com/events/event-occurrences/2026-03/event-types \
      --header 'Authorization: Bearer <token>'

200

default


    {
      "eventTypes": [
        "<string>"
      ]
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

#### Response

200

application/json

successful operation

​

eventTypes

string[]

required

List of event type names.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)