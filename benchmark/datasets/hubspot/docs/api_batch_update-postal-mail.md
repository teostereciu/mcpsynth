# Set default association

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/activities/postal-mail/batch/update-postal-mail*

---

Batch

# Set default association

PUT

/

crm

/

objects

/

2026-03

/

{fromObjectType}

/

{fromObjectId}

/

associations

/

default

/

{toObjectType}

/

{toObjectId}

Try it

cURL

cURL


    curl --request PUT \
      --url https://api.hubapi.com/crm/objects/2026-03/{fromObjectType}/{fromObjectId}/associations/default/{toObjectType}/{toObjectId} \
      --header 'Authorization: Bearer <token>'

200

default


    {
      "completedAt": "2023-11-07T05:31:56Z",
      "results": [
        {
          "associationSpec": {
            "associationCategory": "HUBSPOT_DEFINED",
            "associationTypeId": 123
          },
          "from": {
            "id": "<string>"
          },
          "to": {
            "id": "<string>"
          }
        }
      ],
      "startedAt": "2023-11-07T05:31:56Z",
      "status": "CANCELED",
      "errors": [
        {
          "category": "<string>",
          "context": {},
          "errors": [
            {
              "message": "<string>",
              "code": "<string>",
              "context": "{missingScopes=[scope1, scope2]}",
              "in": "<string>",
              "subCategory": "<string>"
            }
          ],
          "links": {},
          "message": "<string>",
          "status": "<string>",
          "id": "<string>",
          "subCategory": {}
        }
      ],
      "links": {},
      "numErrors": 123,
      "requestedAt": "2023-11-07T05:31:56Z"
    }

Supported products

Required Scopes

#### Authorizations

oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2private_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_apps_legacyoauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2oauth2private_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_apps_legacy

​

Authorization

string

header

required

The access token received from the authorization server in the OAuth 2.0 flow.

#### Path Parameters

​

fromObjectId

string

required

​

fromObjectType

string

required

​

toObjectId

string

required

​

toObjectType

string

required

#### Response

200

application/json

successful operation

The response returned after performing a batch operation on associations.

​

completedAt

string<date-time>

required

The timestamp when the batch process was completed, in ISO 8601 format.

​

results

object[]

required

Show child attributes

​

startedAt

string<date-time>

required

The timestamp when the batch process began execution, in ISO 8601 format.

​

status

enum<string>

required

The status of the batch processing request. Can be: "PENDING", "PROCESSING", "CANCELED", or "COMPLETE".

Available options:

`CANCELED`,

`COMPLETE`,

`PENDING`,

`PROCESSING`

​

errors

object[]

Show child attributes

​

links

object

An object containing relevant links related to the batch request.

Show child attributes

​

numErrors

integer<int32>

The total number of errors that occurred during the operation.

​

requestedAt

string<date-time>

The timestamp when the batch process was initiated, in ISO 8601 format.

Last modified on April 10, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)