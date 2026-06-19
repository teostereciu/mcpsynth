# Schemas API guide

*Source: https://developers.hubspot.com/docs/api-reference/legacy/crm/objects/schemas/guide*

---

# Schemas API guide

Use the schemas API to define new custom objects, and retrieve or edit custom object schema details.

Supported products

Required Scopes

In each HubSpot account, there are standard CRM objects, such as contacts, companies, deals, and tickets. To represent and organize your CRM data based on unique business needs, you can create custom objects. You can [create a custom object](https://knowledge.hubspot.com/object-settings/create-custom-objects) in HubSpot, or use the schemas API to define custom objects, properties, and associations with other objects. Below, learn how to create and manage custom objects through the API, and see a walkthrough of creating an example custom object. To create and manage custom object records once a custom object is defined, use the [objects API](/docs/api-reference/legacy/crm/objects/custom-objects/guide).

**Please note:** custom objects are specific to each account, and depending on your subscription, there are limits on the number of custom objects you can create. Learn more about your limits in the [HubSpot Products & Services catalog](https://legal.hubspot.com/hubspot-product-and-services-catalog).

##

​

Create a custom object

To create a custom object, you’ll first need to define the object schema. The schema includes the object name, properties, and associations to other CRM objects. To define the custom object, make a `POST` request to `/crm-object-schemas/v3/schemas`. In the request body, include definitions for your object schema, including its name, properties, and associations. Include the following fields in your request:

Field| Field type| Description
---|---|---
`name`| `string`| The object’s unique internal name. Once set, this cannot be changed. The name can only contain letters, numbers, and underscores, and the first character must be a letter.
`description`| `string`| A description that explains what the object stores. This field is optional.
`labels`| `object`| The word for the object’s records, singular and plural. In the `labels` object, define the labels with the `labels.plural`and `labels.singular` fields. Long labels may be cut off in certain parts of the HubSpot UI.
`properties`| `object[]`| Fields that store information on individual custom object records.
`primaryDisplayProperty`| `string`| The property used for naming individual custom object records.
`searchableProperties`| `string[]`| The properties that are indexed for searching in HubSpot.
`secondaryDisplayProperties`| `string[]`| The properties that appear on individual records under the `primaryDisplayProperty`. The first property listed in `secondaryDisplayProperties` is also added as a fourth filter on the object index page (if a `string`, `number`, `enumeration`, `boolean`, or `datetime`.)
`requiredProperties`| `string[]`| The properties that are required when creating a new custom object record.
`associatedObjects`| `string[]`| The objects with which you’ll associated custom objects. Adding objects in this field means you’ll be able to associate custom object records with records of that object.
`allowSensitiveProperties`| `boolean`| If `true`, you can create [Sensitive Data properties](https://knowledge.hubspot.com/account-security/store-sensitive-data#create-properties-to-store-sensitive-data) for the object.

Below, learn more about the defining the object’s properties and associations. Review a full walkthrough example of defining a custom object.

###

​

Properties

In the `properties` object, create the properties that will store information on individual custom object records. By default, when creating properties through the schema request, property `type` is set to `string` and the `fieldType` is set to `text`. Learn more about the types of properties you can create on the [properties API guide](/docs/api-reference/legacy/crm/properties/guide#property-type-and-fieldtype-values). Use your defined properties to populate the `requiredProperties`, `searchableProperties` `primaryDisplayProperty`, and `secondaryDisplayProperties` fields.

###

​

Associations

Custom objects automatically have associations defined with emails, meetings, notes, tasks, calls, and conversations, so you can associate custom object records with activities. To associate custom object records with other object records, you must define those associations in the schema. In the create schema request, include the `associatedObjects` field with the `objectTypeId` values of objects with which you want to associate your custom object. For example, the following custom object can be associated with contacts, companies, and another custom object’s records.


    "associatedObjects": ["0-1", "0-2", "2-3453932"]


##

​

Retrieve existing custom object schemas

To retrieve all custom object schemas, make a `GET` request to `/crm-object-schemas/v3/schemas`. To retrieve a specific custom object schema, make a `GET` request to one of the following:

  * `/crm-object-schemas/v3/schemas/{fullyQualifiedName}`
  * `/crm-object-schemas/v3/schemas/{objectTypeId}`

You can find an object’s `fullyQualifiedName` (formatted as `p{Hub_ID}_{object_name}`) and `objectTypeId` in its schema. You can find your account’s Hub ID using the [account information API](/docs/api-reference/legacy/account/account-information/guide). For example, for an account with a Hub ID of `1234`, to retrieve an object named `lender` with the `objectTypeId` value `2-7282133`, your request URL could look like either of the following:

  * `/crm-object-schemas/v3/schemas/p1234_lender`
  * `/crm-object-schemas/v3/schemas/2-7282133`


##

​

Update an existing custom object schema

To update an object’s schema, make a `PATCH` request to `/crm-object-schemas/v3/schemas/{objectTypeId}`. Once your custom object is defined:

  * The object’s `name` _cannot_ be changed via API.
  * To set a new property as a required, searchable, or display property, you must create the property prior to updating the schema.
  * To create and edit custom object properties, you can either manage properties [in HubSpot](https://knowledge.hubspot.com/properties/create-and-edit-properties#view-and-edit-properties) or via the [properties API](/docs/api-reference/legacy/crm/properties/guide).


##

​

Delete a custom object schema

To delete a custom object, make a `DELETE` request to `/crm-object-schemas/v3/schemas/{objectType}`. You can only delete a custom object after all records, associations, and properties are deleted. If you need to create a new custom object with the same name as the deleted object, hard delete the schema by making a `DELETE` request to `/crm-object-schemas/v3/schemas/{objectType}?archived=true`.

##

​

Custom object example

The following is a walkthrough of creating an example custom object. This walkthrough covers:

  1. Creating a custom object schema.
  2. Creating a custom object record.
  3. Associating a custom object record with a contact.
  4. Creating a new property definition.
  5. Updating the object schema (i.e. `secondaryDisplayProperties`) with the new property.

**Goal:** a car dealership called CarSpot wants to store their inventory in HubSpot using a custom object. To track vehicle ownership and purchases, they’ll associate cars with contact records. Along the way, they’ll also track vehicle maintenance using HubSpot tickets and custom properties.

###

​

Create the object schema

CarSpot needs to create an object schema that can represent the following attributes as properties:

  1. **Condition (new or used):** `enumeration`
  2. **Date received at dealership:** `date`
  3. **Year:** `number`
  4. **Make:** `string`
  5. **Model:** `string`
  6. **VIN:** `string` (unique value)
  7. **Color:** `string`
  8. **Mileage:** `number`
  9. **Price:** `number`
  10. **Notes:** `string`

They also add a description to provide context about how to use the object, and define an association between their custom object and the standard contacts object so that they can connect cars to potential buyers. With their data model finalized, they create the object schema by making a `POST` request to `/crm-object-schemas/v3/schemas` with the following request body:


    {
      "name": "cars",
      "description": "Cars keeps track of cars currently or previously held in our inventory.",
      "labels": {
        "singular": "Car",
        "plural": "Cars"
      },
      "primaryDisplayProperty": "model",
      "secondaryDisplayProperties": ["make"],
      "searchableProperties": ["year", "make", "VIN", "model"],
      "requiredProperties": ["year", "make", "VIN", "model"],
      "properties": [
        {
          "name": "condition",
          "label": "Condition",
          "type": "enumeration",
          "fieldType": "select",
          "options": [
            {
              "label": "New",
              "value": "new"
            },
            {
              "label": "Used",
              "value": "used"
            }
          ]
        },
        {
          "name": "date_received",
          "label": "Date received",
          "type": "date",
          "fieldType": "date"
        },
        {
          "name": "year",
          "label": "Year",
          "type": "number",
          "fieldType": "number"
        },
        {
          "name": "make",
          "label": "Make",
          "type": "string",
          "fieldType": "text"
        },
        {
          "name": "model",
          "label": "Model",
          "type": "string",
          "fieldType": "text"
        },
        {
          "name": "VIN",
          "label": "VIN",
          "type": "string",
          "hasUniqueValue": true,
          "fieldType": "text"
        },
        {
          "name": "color",
          "label": "Color",
          "type": "string",
          "fieldType": "text"
        },
        {
          "name": "mileage",
          "label": "Mileage",
          "type": "number",
          "fieldType": "number"
        },
        {
          "name": "price",
          "label": "Price",
          "type": "number",
          "fieldType": "number"
        },
        {
          "name": "notes",
          "label": "Notes",
          "type": "string",
          "fieldType": "text"
        }
      ],
      "associatedObjects": ["0-1"]
    }


After creating the object schema, CarSpot makes sure to note the new object’s `{objectTypeId}` field, as they’ll use this for fetching and updating the object later. They can also use the `{fullyQualifiedName}` value, if they prefer.

###

​

Create a custom object record

With the custom object schema created, CarSpot can now create records for each car in their inventory. Learn more about [creating custom object records](/docs/api-reference/legacy/crm/objects/custom-objects/guide). They create their first car by making a `POST` request to `/crm/v3/objects/2-3465404` with the following request body:


    {
      "properties": {
        "condition": "used",
        "date_received": "1582416000000",
        "year": "2014",
        "make": "Nissan",
        "model": "Frontier",
        "VIN": "4Y1SL65848Z411439",
        "color": "White",
        "mileage": "80000",
        "price": "12000",
        "notes": "Excellent condition. No accidents."
      }
    }


The response for this API call would look similar to:


    {
      "id": "181308",
      "properties": {
        "color": "White",
        "condition": "used",
        "make": "Nissan",
        "mileage": "80000",
        "model": "Frontier",
        "VIN": "4Y1SL65848Z411439",
        "notes": "Excellent condition. No accidents.",
        "price": "12000",
        "year": "2014",
        "date_received": "1582416000000"
      },
      "createdAt": "2020-02-23T01:44:11.035Z",
      "updatedAt": "2020-02-23T01:44:11.035Z",
      "archived": false
    }


With the record created, they can use the `id` value to later associate the car with an existing contact. To later retrieve this record along with specific properties, they can make a `GET` request to `/crm/v3/objects/2-3465404/181308?&properties=year&properties=make&properties=model`.

###

​

Associate the custom object record to another record

CarSpot can use the ID of the new car record (`181308`) and the ID of another record to associate a custom object record with a record of another object. To create an association, make a `PUT` request to `/crm/v3/objects/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}/{associationType}`. If the object relationship is already defined, to determine the `associationType` value, make a `GET` request to `/crm-object-schemas/v3/schemas/{objectType}`. For example, with the contact ID `51` and the association type `75`, CarSpot can associate the car record with a contact. Using the above IDs, they’d make a `PUT` request to `/crm/v3/objects/2-3465404/181308/associations/contacts/51/75`

###

​

Define a new property

As they continue to track maintenance, CarSpot sees an opportunity to bundle maintenance services into packages. To track these maintenance packages on individual car records, they create a new `enumeration` property containing the available packages. To define a new property, they make a `POST` request to `/crm/v3/properties/2-3465404` with the following request body:


    {
      "groupName": "car_information",
      "name": "maintenance_package",
      "label": "Maintenance Package",
      "type": "enumeration",
      "fieldType": "select",
      "options": [
        {
          "label": "Basic",
          "value": "basic"
        },
        {
          "label": "Oil change only",
          "value": "oil_change_only"
        },
        {
          "label": "Scheduled",
          "value": "scheduled"
        }
      ]
    }


The response for this API call would look similar to:


    {
      "updatedAt": "2020-02-23T02:08:20.055Z",
      "createdAt": "2020-02-23T02:08:20.055Z",
      "name": "maintenance_package",
      "label": "Maintenance Package",
      "type": "enumeration",
      "fieldType": "select",
      "groupName": "car_information",
      "options": [
        {
          "label": "Basic",
          "value": "basic",
          "displayOrder": -1,
          "hidden": false
        },
        {
          "label": "Oil change only",
          "value": "oil_change_only",
          "displayOrder": -1,
          "hidden": false
        },
        {
          "label": "Scheduled",
          "value": "scheduled",
          "displayOrder": -1,
          "hidden": false
        }
      ],
      "displayOrder": -1,
      "calculated": false,
      "externalOptions": false,
      "archived": false,
      "hasUniqueValue": false,
      "hidden": false,
      "modificationMetadata": {
        "archivable": true,
        "readOnlyDefinition": false,
        "readOnlyValue": false
      },
      "formField": false
    }


Now that the property has been created, they want it to appear in the sidebar of each car record so that the information is readily available to their sales reps and technicians. To do this, they add the property to `secondaryDisplayProperties` by making a `PATCH` request to `/crm-object-schemas/v3/schemas/2-3465404` with the following request body:


    {
      "secondaryDisplayProperties": ["maintenance_package"]
    }


The response for this API call would look similar to:


    {
      "id": "3465404",
      "createdAt": "2020-02-23T01:24:54.537Z",
      "updatedAt": "2020-02-23T02:12:24.175874Z",
      "labels": {
        "singular": "Car",
        "plural": "Cars"
      },
      "requiredProperties": ["year", "model", "VIN", "make"],
      "searchableProperties": ["year", "model", "VIN", "make"],
      "primaryDisplayProperty": "model",
      "secondaryDisplayProperties": ["maintenance_package"],
      "name": "car"
    }


Now, when a technician opens a contact record that has an associated car, the property will be displayed in the custom object card in the sidebar:

As CarSpot continues to use HubSpot, they may find additional ways to refine and expand this custom object and more using HubSpot’s API. To learn more about ways to use and scale custom objects, check out the following [post](https://developers.hubspot.com/blog/how-to-think-like-an-architect-by-building-scalable-custom-objects) on the HubSpot developer blog.

Last modified on April 10, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)