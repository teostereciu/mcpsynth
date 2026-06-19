# Create a new custom object schema.

*Source: https://developers.hubspot.com/docs/api-reference/legacy/crm/objects/schemas/create-schema*

---

Schemas

# Create a new custom object schema.

Create a new custom object schema by defining its properties and associations.

POST

/

crm-object-schemas

/

v3

/

schemas

Try it

Create a new custom object schema.

cURL


    curl --request POST \
      --url https://api.hubapi.com/crm-object-schemas/v3/schemas \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "associatedObjects": [
        "CONTACT"
      ],
      "labels": {
        "plural": "My objects",
        "singular": "My object"
      },
      "metaType": "PORTAL_SPECIFIC",
      "name": "my_object",
      "primaryDisplayProperty": "my_object_property",
      "properties": [
        {
          "isPrimaryDisplayLabel": true,
          "label": "My object property",
          "name": "my_object_property"
        }
      ],
      "requiredProperties": [
        "my_object_property"
      ]
    }
    '

201

default


    {
      "associations": [
        {
          "fromObjectTypeId": "2-123456",
          "id": "123",
          "name": "my_object_to_contact",
          "toObjectTypeId": "0-1"
        }
      ],
      "createdAt": "2020-02-20T18:07:11.390Z",
      "fullyQualifiedName": "p7878787_my_object\"",
      "id": "123456",
      "labels": {
        "plural": "My objects",
        "singular": "My object"
      },
      "metaType": "PORTAL_SPECIFIC",
      "name": "my_object",
      "primaryDisplayProperty": "my_object_property",
      "properties": [
        {
          "archived": false,
          "calculated": false,
          "createdAt": "2020-02-20T18:07:11.802Z",
          "displayOrder": -1,
          "externalOptions": false,
          "fieldType": "text",
          "groupName": "my_object_information",
          "hasUniqueValue": false,
          "label": "My object property",
          "name": "my_object_property",
          "type": "string",
          "updatedAt": "2020-02-20T18:07:11.802Z"
        }
      ],
      "requiredProperties": [
        "my_object_property"
      ],
      "searchableProperties": [
        "my_object_property"
      ],
      "updatedAt": "2020-02-20T18:09:07.555Z"
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

#### Body

application/json

Object schema definition, including properties and associations.

Defines a new object type, its properties, and associations.

​

associatedObjects

string[]

required

Associations defined for this object type.

​

labels

object

required

Singular and plural labels for the object. Used in CRM display.

Show child attributes

Example:


    {
      "plural": "My objects",
      "singular": "My object"
    }

​

name

string

required

A unique name for this object. For internal use only.

​

properties

object[]

required

Properties defined for this object type.

Show child attributes

​

requiredProperties

string[]

required

The names of properties that should be required when creating an object of this type.

​

allowsSensitiveProperties

boolean

Determines if the object type can include properties that are marked as sensitive.

​

description

string

A brief explanation of the object type.

​

primaryDisplayProperty

string

The name of the primary property for this object. This will be displayed as primary on the HubSpot record page for this object type.

​

searchableProperties

string[]

Names of properties that will be indexed for this object type in by HubSpot's product search.

​

secondaryDisplayProperties

string[]

The names of secondary properties for this object. These will be displayed as secondary on the HubSpot record page for this object type.

#### Response

201

application/json

successful operation

Defines an object schema, including its properties and associations.

​

associations

object[]

required

Associations defined for a given object type.

Show child attributes

​

id

string

required

A unique ID for this schema's object type. Will be defined as {meta-type}-{unique ID}.

​

labels

object

required

Singular and plural labels for the object. Used in CRM display.

Show child attributes

Example:


    {
      "plural": "My objects",
      "singular": "My object"
    }

​

name

string

required

A unique name for the schema's object type.

​

properties

object[]

required

Properties defined for this object type.

Show child attributes

​

requiredProperties

string[]

required

The names of properties that should be required when creating an object of this type.

​

allowsSensitiveProperties

boolean

​

archived

boolean

​

createdAt

string<date-time>

When the object schema was created.

​

createdByUserId

integer<int32>

​

description

string

​

fullyQualifiedName

string

An assigned unique ID for the object, including portal ID and object name.

​

objectTypeId

string

​

primaryDisplayProperty

string

The name of the primary property for this object. This will be displayed as primary on the HubSpot record page for this object type.

​

searchableProperties

string[]

Names of properties that will be indexed for this object type in by HubSpot's product search.

​

secondaryDisplayProperties

string[]

The names of secondary properties for this object. These will be displayed as secondary on the HubSpot record page for this object type.

​

updatedAt

string<date-time>

When the object schema was last updated.

​

updatedByUserId

integer<int32>

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)