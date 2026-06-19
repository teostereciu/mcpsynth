# Retrieve emails

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/activities/emails/batch/get-emails*

---

Batch

# Retrieve emails

Retrieve a batch of emails by record ID or include the `idProperty` parameter to retrieve records by a custom unique value property.

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

read

Try it

Retrieve emails

cURL


    curl --request POST \
      --url https://api.hubapi.com/crm/objects/2026-03/{objectType}/batch/read \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "inputs": [
        {
          "id": "430001"
        }
      ],
      "properties": [
        "<string>"
      ],
      "propertiesWithHistory": [
        "<string>"
      ],
      "idProperty": "<string>"
    }
    '

200

default


    {
      "completedAt": "2023-11-07T05:31:56Z",
      "results": [
        {
          "archived": true,
          "createdAt": "2023-11-07T05:31:56Z",
          "id": "<string>",
          "properties": {},
          "updatedAt": "2023-11-07T05:31:56Z",
          "archivedAt": "2023-11-07T05:31:56Z",
          "objectWriteTraceId": "<string>",
          "propertiesWithHistory": {},
          "url": "<string>"
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

#### Query Parameters

​

archived

boolean

default:false

Whether to return only results that have been archived.

#### Body

application/json

Specifies the input for reading a batch of CRM objects, including arrays of object IDs, requested property names (with optional history), and an optional unique identifying property.

​

inputs

object[]

required

Show child attributes

​

properties

string[]

required

Key-value pairs for setting properties for the new object.

​

propertiesWithHistory

string[]

required

Key-value pairs for setting properties for the new object and their histories.

​

idProperty

string

When using a custom unique value property to retrieve records, the name of the property. Do not include this parameter if retrieving by record ID.

#### Response

200

application/json

successful operation

A public object batch response object

​

completedAt

string<date-time>

required

The timestamp when the batch processing was completed, in ISO 8601 format.

​

results

object[]

required

Show child attributes

​

startedAt

string<date-time>

required

The timestamp when the batch processing began, in ISO 8601 format.

​

status

enum<string>

required

The status of the batch processing request: "PENDING", "PROCESSING", "CANCELLED", or "COMPLETE"

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

The total number of errors that occurred during the batch operation.

​

requestedAt

string<date-time>

The timestamp when the batch request was initially made, in ISO 8601 format.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)