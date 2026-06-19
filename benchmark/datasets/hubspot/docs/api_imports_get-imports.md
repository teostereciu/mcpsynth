# Retrieve imports

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/imports/get-imports*

---

Imports

# Retrieve imports

GET

/

crm

/

imports

/

2026-03

Try it

cURL

cURL


    curl --request GET \
      --url https://api.hubapi.com/crm/imports/2026-03 \
      --header 'Authorization: Bearer <token>'

200

default


    {
      "results": [
        {
          "createdAt": "2023-11-07T05:31:56Z",
          "id": "<string>",
          "mappedObjectTypeIds": [
            "<string>"
          ],
          "metadata": {
            "counters": {},
            "fileIds": [
              "<string>"
            ],
            "objectLists": [
              {
                "listId": "<string>",
                "objectType": "<string>"
              }
            ]
          },
          "optOutImport": true,
          "state": "CANCELED",
          "updatedAt": "2023-11-07T05:31:56Z",
          "importName": "<string>",
          "importRequestJson": {},
          "importSource": "API",
          "importTemplate": {
            "templateId": 123,
            "templateType": "admin_defined"
          }
        }
      ],
      "paging": {
        "next": {
          "after": "<string>",
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

The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.

​

limit

integer<int32>

The maximum number of results to display per page.

#### Response

200

application/json

successful operation

​

results

object[]

required

Show child attributes

​

paging

object

Show child attributes

Last modified on April 10, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)