# Get a single actor

*Source: https://developers.hubspot.com/docs/api-reference/legacy/conversations/conversations/actors/get-actor*

---

Actors

# Get a single actor

Retrieve details of a single actor using the actor ID.

GET

/

conversations

/

v3

/

conversations

/

actors

/

{actorId}

Try it

Get a single actor

cURL


    curl --request GET \
      --url https://api.hubapi.com/conversations/v3/conversations/actors/{actorId} \
      --header 'Authorization: Bearer <token>'

200

default


    {
      "type": "AGENT",
      "id": "<string>",
      "name": "<string>",
      "email": "<string>",
      "avatar": "<string>"
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

actorId

string

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

  * Option 7


​

type

enum<string>

default:AGENT

required

Available options:

`AGENT`

​

id

string

required

​

name

string

​

email

string

​

avatar

string

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)