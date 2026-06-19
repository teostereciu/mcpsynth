# Archive a batch of deals by ID

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/objects/deals/batch/delete-deals*

---

Batch

# Archive a batch of deals by ID

Archive multiple deals using their IDs.

POST

/

crm

/

objects

/

2026-03

/

{objectType}

/

batch

/

archive

Try it

Archive a batch of deals by ID

cURL


    curl --request POST \
      --url https://api.hubapi.com/crm/objects/2026-03/{objectType}/batch/archive \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "inputs": [
        {
          "id": "430001"
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

#### Path Parameters

​

objectType

string

required

#### Body

application/json

​

inputs

object[]

required

Show child attributes

#### Response

204

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)