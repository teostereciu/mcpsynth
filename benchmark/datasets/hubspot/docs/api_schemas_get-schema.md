# Retrieve the schema of a specified custom object.

*Source: https://developers.hubspot.com/docs/api-reference/legacy/crm/objects/schemas/get-schema*

---

Schemas

# Retrieve the schema of a specified custom object.

Retrieve details of a custom object schema, including its properties and associations, using the object type ID or fully qualified name.

GET

/

crm-object-schemas

/

v3

/

schemas

/

{objectType}

Try it

Retrieve the schema of a specified custom object.

cURL


    curl --request GET \
      --url https://api.hubapi.com/crm-object-schemas/v3/schemas/{objectType} \
      --header 'Authorization: Bearer <token>'

200

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

oauth2oauth2oauth2oauth2oauth2private_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsoauth2oauth2oauth2oauth2oauth2private_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_appsprivate_apps

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

Fully qualified name or object type ID of your schema.

#### Query Parameters

​

includeAssociationDefinitions

boolean

default:true

​

includeAuditMetadata

boolean

default:true

​

includePropertyDefinitions

boolean

default:true

#### Response

200

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