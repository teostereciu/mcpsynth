# Send a batch of event occurrences

*Source: https://developers.hubspot.com/docs/api-reference/latest/events/send-event-data/batch-send-occurrences*

---

Send event data

# Send a batch of event occurrences

POST

/

events

/

custom

/

2026-03

/

send

/

batch

Try it

cURL

cURL


    curl --request POST \
      --url https://api.hubapi.com/events/custom/2026-03/send/batch \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "inputs": [
        {
          "eventName": "<string>",
          "properties": {},
          "email": "<string>",
          "objectId": "<string>",
          "occurredAt": "2026-01-20T21:14:16.512Z",
          "utk": "<string>",
          "uuid": "<string>"
        }
      ]
    }
    '

204

default


    This response has no body data.

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

inputs

object[]

required

Show child attributes

#### Response

204

Last modified on April 10, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)