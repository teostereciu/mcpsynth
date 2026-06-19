# Delete meeting

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/activities/meetings/delete-meeting*

---

Meetings

# Delete meeting

Delete a meeting by ID.

DELETE

/

crm

/

objects

/

2026-03

/

{objectType}

/

{objectId}

Try it

Delete meeting

cURL


    curl --request DELETE \
      --url https://api.hubapi.com/crm/objects/2026-03/{objectType}/{objectId} \
      --header 'Authorization: Bearer <token>'

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

#### Path Parameters

​

objectId

string

required

​

objectType

string

required

#### Response

204

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)