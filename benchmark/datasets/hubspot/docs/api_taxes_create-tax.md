# Create

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/objects/taxes/create-tax*

---

Taxes

# Create

Create a tax with the given properties and return a copy of the object, including the ID. Documentation and examples for creating standard taxes is provided.

POST

/

crm

/

objects

/

2026-03

/

{objectType}

Try it

Create

cURL


    curl --request POST \
      --url https://api.hubapi.com/crm/objects/2026-03/{objectType} \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "associations": [
        {
          "to": {
            "id": "<string>"
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 123
            }
          ]
        }
      ],
      "properties": {}
    }
    '

201

default


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

Is the input object used to create a new CRM object, containing the properties to be set and optional associations to link the new record with other CRM objects.

​

associations

object[]

required

Show child attributes

​

properties

object

required

Key-value pairs for setting properties for the new object.

Show child attributes

#### Response

201

application/json

successful operation

A simple public object.

​

archived

boolean

required

Whether the object is archived.

​

createdAt

string<date-time>

required

The timestamp when the object was created, in ISO 8601 format.

​

id

string

required

The unique ID of the object.

​

properties

object

required

Key-value pairs representing the properties of the object.

Show child attributes

​

updatedAt

string<date-time>

required

The timestamp when the object was last updated, in ISO 8601 format.

​

archivedAt

string<date-time>

The timestamp when the object was archived, in ISO 8601 format.

​

objectWriteTraceId

string

An identifier used for tracing the write request for the object.

​

propertiesWithHistory

object

Key-value pairs representing the properties of the object along with their history.

Show child attributes

​

url

string

The URL associated with the object.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)