# CRM API | Contacts

*Source: https://developers.hubspot.com/docs/api/crm/contacts*

---

Contacts

# CRM API | Contacts

Contact records store information about individuals. The contacts endpoints allow you to manage this data and sync it between HubSpot and other systems.

Scope requirements

In HubSpot, contacts store information about the individual people that interact with your business. The contacts endpoints allow you to create and manage contact records in your HubSpot account, as well as sync contact data between HubSpot and other systems. Learn more about objects, records, properties, and associations APIs in the [Understanding the CRM](/docs/guides/crm/understanding-the-crm) guide. For more general information about objects and records in HubSpot, [learn how to manage your CRM database](http://knowledge.hubspot.com/contacts-user-guide).

##

​

Create contacts

To create new contacts:

  * To create one contact, make a `POST` request to `/crm/v3/objects/contacts`.
  * To create multiple contacts, make a `POST` request to `/crm/v3/objects/contacts/batch/create`.

In your request, include your contact data in a `properties` object. You can also add an `associations` object to associate your new contact with existing records (e.g., companies, deals), or activities (e.g., meetings, notes).

For batch create actions, you can enable multi-status errors which tell you which records were successfully created and which were not. Learn more about [setting up multi-status error handling](/docs/api-reference/error-handling#multi-status-errors).

###

​

Create contacts with property values

When creating a contact, you must include contact properties to store the contact’s details. There are [default HubSpot contact properties](https://knowledge.hubspot.com/properties/hubspots-default-contact-properties), but you can also [create custom contact properties](https://knowledge.hubspot.com/properties/create-and-edit-properties). For example, to create a new contact, your request may look similar to the following:


    {
      "properties": {
        "email": "example@hubspot.com",
        "firstname": "Jane",
        "lastname": "Doe"
      }
    }


When creating a new contact, it’s required to include at least one of the following properties:

Property| Type| Description
---|---|---
`email`| `string`| The contact’s email address. It’s recommended to always include `email`, because email address is the [primary unique identifier](https://knowledge.hubspot.com/records/deduplication-of-records#automatic-deduplication-in-hubspot) to avoid duplicate contacts in HubSpot.
`firstname`| `string`| The contact’s first name.
`lastname`| `string`| The contact’s last name.

You can also include other properties as needed. Expand the section below to view a list of commonly used properties.

Recommended properties

​

lifecyclestage

enumeration

The contact’s [lifecycle stage](https://knowledge.hubspot.com/records/use-lifecycle-stages). Default options include `subscriber`, `lead`, `marketingqualifiedlead`, `evangelist`, `salesqualifiedlead`, `opportunity`, and `customer`.To retrieve custom lifecycle stage values, make a `GET` request to `crm/v3/properties/0-1/lifecyclestage`.

​

phone

string

The contact’s phone number.

​

mobilephone

string

The contact’s mobile phone number.

​

fax

string

The contact’s fax number.

​

jobtitle

string

The contact’s job title.

​

address

string

The contacts’ street address.

​

city

string

The city in which the contact is located.

​

state

string

The state in which the contact is located,

​

country

string

The country in which the contact is located.

​

zip

string

The postal code in which the contact is located.

​

hs_timezone

enumeration

The time zone in which the contact is located. This can be set manually or automatically based on a contact’s IP address.To retrieve all available time zone values, make a `GET` request to `crm/v3/properties/0-1/hs_timezone`.

To view all available contact properties in your account, make a `GET` request to `/crm/v3/properties/0-1`. Learn more about the [properties API](/docs/api-reference/legacy/crm/properties/guide).

When including enumeration properties, you must use internal names to set values. The internal name stays the same even if you’ve changed a default value’s label.

###

​

Create contacts with associations

When creating a new contact, you can also associate the contact with [existing records](https://knowledge.hubspot.com/records/associate-records) or [activities](https://knowledge.hubspot.com/records/associate-activities-with-records) by including an associations object. In the associations object, you should include the following:

Parameter| Description
---|---
`to`| The record or activity you want to associate with the contact, specified by its unique `id` value.
`types`| The type of the association between the contact and the record/activity. Include the `associationCategory`and `associationTypeId`. Default association type IDs are listed on the [associations API guide](/docs/api-reference/legacy/crm/associations/v3/associate-records#association-type-id-values), or you can retrieve the value for custom association types (i.e. labels) via the [associations API](/docs/api-reference/legacy/crm/associations/v3/associate-records#retrieve-association-types).

For example, to associate a new contact with an existing company and email, your request would look like the following:


    {
      "properties": {
        "email": "example@hubspot.com",
        "firstname": "Jane",
        "lastname": "Doe",
        "phone": "+18884827768",
        "company": "HubSpot",
        "website": "hubspot.com",
        "lifecyclestage": "marketingqualifiedlead"
      },
      "associations": [
        {
          "to": {
            "id": 123456
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 279
            }
          ]
        },
        {
          "to": {
            "id": 556677
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 197
            }
          ]
        }
      ]
    }


##

​

Retrieve contacts

You can retrieve contacts individually or in batches. You can include the following query parameters in your request URLs to retrieve certain data.

Parameter| Description
---|---
`properties`| A comma separated list of the properties to be returned in the response. If a requested property isn’t defined, it won’t be included in the response. If a requested property is defined but a contact doesn’t have a value, it will be returned as `null`.
`propertiesWithHistory`| A comma separated list of the current and historical properties to be returned in the response. If a requested property isn’t defined, it won’t be included in the response. If a requested property is defined but a contact doesn’t have a value, it will be returned as `null`.
`associations`| Supported when retrieving an individual contact or all contacts, a comma separated list of objects to retrieve associated IDs for. Any specified associations that don’t exist will not be returned in the response. Learn more about the [associations API.](/docs/api-reference/legacy/crm/associations/v3/associate-records)

###

​

Retrieve an individual contact

You can retrieve individual contacts using the contact’s Record ID value or their email address.

  * To retrieve an individual contact by Record ID, make a `GET` request to `/crm/v3/objects/contacts/{recordId}`.
  * To retrieve a contact by their email address, make a `GET` request to `/crm/v3/objects/contacts/{email}?idProperty=email`.

To retrieve contacts based on other property values, use the [search API](/docs/api-reference/legacy/crm/search-the-crm).

###

​

Retrieve all contacts

To request a list of all contacts, make a `GET` request to `/crm/v3/objects/contacts`. You can retrieve up to 100 contacts in one request.

  * To retrieve a specific amount under 100, add a value to the `limit` parameter. For example, `?limit=50`.
  * To retrieve additional contacts in subsequent requests (i.e. the contacts after the limit was reached in your request), include the `after` parameter with the `after` value returned from the previous request. This value is the Record ID of the next contact. For example, `?after=123456`.

For example, to retrieve 50 contacts, your request URL would be `GET` `/crm/v3/objects/contacts?limit=50`. In your response, under the `paging` object below the list of returned contacts, the `after` value is the `id` of the next contact that would’ve been returned. To request 50 more contacts, starting with the next returned value, make a `GET` request to `/crm/v3/objects/contacts?limit=50&after={id}`. The `after` field is highlighted in the example response below:


    {
      "results": [
        {
          "id": "33451",
          "properties": {
            "createdate": "2022-06-01T14:31:48.469Z",
            "email": "lorelai@thedragonfly.com",
            "firstname": "Lorelai",
            "hs_object_id": "33451",
            "lastmodifieddate": "2025-07-07T20:27:17.947Z",
            "lastname": "Gilmore"
          },
          "createdAt": "2022-06-01T14:31:48.469Z",
          "updatedAt": "2025-07-07T20:27:17.947Z",
          "archived": false
        }
      ],
      "paging": {
        "next": {
          "after": "33452",
          "link": "https://api.hubspot.com/crm/objects/v3/contacts?limit=1"
        }
      }
    }


###

​

Retrieve a batch of contacts

When retrieving contacts in batches, you can request contacts by their Record ID (`id`), email address (`email`), or by a [custom unique identifier property](/docs/api-reference/legacy/crm/properties/guide#create-unique-identifier-properties). To request a batch of contacts, make a `POST` request to `crm/v3/objects/contacts/batch/read`. For the batch read endpoint, to retrieve by email or custom [unique identifier property](/docs/api-reference/legacy/crm/properties/guide#create-unique-identifier-properties), you must use the `idProperty`. By default, the `id` values in the request refer to the Record ID, so the `idProperty` parameter is not required when retrieving by Record ID, but always required when retrieving by email or a custom unique ID property.

The batch endpoint _cannot_ retrieve associations. To view associations for a specific batch of contacts, you must retrieve the contacts’ `id` values first, then include them in a `GET` request to the batch read associations API endpoint. Learn how to retrieve associations with the [associations API](/docs/api-reference/legacy/crm/associations/v3/associate-records).

For example, to retrieve a batch of contacts based on their record ID values, your request could look like the following (current values only, or current and historical values):

  * Retrieve by Record ID with properties

  * Retrieve by Record ID with property history


    {
      "properties": ["email", "lifecyclestage", "jobtitle"],
      "inputs": [
        {
          "id": "1234567"
        },
        {
          "id": "987456"
        }
      ]
    }


    {
      "propertiesWithHistory": ["lifecyclestage", "hs_lead_status"],
      "inputs": [
        {
          "id": "1234567"
        },
        {
          "id": "987456"
        }
      ]
    }


To retrieve contacts based on their email address or value for a custom unique identifier property (e.g., a customer ID number unique for your business), your request would look like:

  * Retrieve by email

  * Retrieve by custom identifier property


    {
      "properties": ["email", "lifecyclestage", "jobtitle"],
      "idProperty": "email",
      "inputs": [
        {
          "id": "lgilmore@thedragonfly.com"
        },
        {
          "id": "sstjames@thedragonfly.com"
        }
      ]
    }


    {
      "properties": ["email", "lifecyclestage", "jobtitle"],
      "idProperty": "internalcustomerid",
      "inputs": [
        {
          "id": "12345"
        },
        {
          "id": "67891"
        }
      ]
    }


##

​

Update contacts

You can update contacts individually or in batches.

If updating the `lifecyclestage` property, you can only set the value _forward_ in the stage order. To set the lifecycle stage backward, you’ll first need to clear the record’s existing lifecycle stage value. The value can be [cleared manually](https://knowledge.hubspot.com/records/update-a-property-value-for-a-record), or may be automatically cleared via a [workflow](https://knowledge.hubspot.com/records/change-record-lifecycle-stages-in-bulk) or an integration that syncs contact data.

###

​

Update an individual contact

To update individual contacts, you can use Record ID (`id`) or the contact’s email address (`email`).

  * To update an individual contact by its Record ID, make a `PATCH` request to `/crm/v3/objects/contacts/{contactId}`, and include the data you want to update.
  * To update an individual contact by its email, make a `PATCH` request to `/crm/v3/objects/contacts/{email}?idProperty=email`, and include the data you want to update.

For example:


    {
      "properties": {
        "favorite_food": "burger",
        "jobtitle": "Manager",
        "lifecyclestage": "customer"
      }
    }


###

​

Update a batch of contacts

To update contacts in batches, you must use the contacts’ Record ID values (`id`). To update multiple contacts, make a `POST` request to `/crm/v3/objects/contacts/batch/update`. In your request body, include each contact’s Record ID as the `id` ​and include the properties you want to update. For example:


    {
      "inputs": [
        {
          "id": "123456789",
          "properties": {
            "favorite_food": "burger"
          }
        },
        {
          "id": "56789123",
          "properties": {
            "favorite_food": "Donut"
          }
        }
      ]
    }


##

​

Upsert contacts

You can also batch create and update contacts at the same time using the upsert endpoint. For this endpoint, you can use `email` or a [custom unique identifier property](/docs/api-reference/legacy/crm/properties/guide#create-unique-identifier-properties). Following the request, if the contacts already exist, they’ll be updated and if the contacts don’t exist, they’ll be created. To upsert contacts, make a `POST` request to `/crm/v3/objects/contacts/batch/upsert`. In your request body, include the `idProperty` parameter to identify whether you’re using `email` or a custom unique identifier property. Include that property’s value as the `id` ​and add the other properties you want to set or update.

Partial upserts are not supported when using `email` as the `idProperty` for contacts. To complete a partial upsert, use a custom unique identifier property as the `idProperty` instead.

For example, your request could look like the following:


    {
      "inputs": [
        {
          "properties": {
            "phone": "+18884827768"
          },
          "id": "test@test.com",
          "idProperty": "email"
        },
        {
          "properties": {
            "phone": "+18888888888"
          },
          "id": "example@hubspot.com",
          "idProperty": "email"
        }
      ]
    }


##

​

Associate existing contacts with records or activities

To associate a contact with other CRM records or an activity, make a `PUT` request to `/crm/v3/objects/contacts/{contactId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`.

To retrieve the `associationTypeId` value, refer to [this list](/docs/api-reference/legacy/crm/associations/v3/associate-records#association-type-id-values) of default values, or make a `GET` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`.

Learn more about the [associations API.](/docs/api-reference/legacy/crm/associations/v3/associate-records)

###

​

Remove an association

To remove an association between a contact and a record or activity, make a `DELETE` request to the following URL: `/crm/v3/objects/contacts/{contactID}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`.

##

​

Pin an activity on a contact record

You can [pin an activity](https://knowledge.hubspot.com/records/pin-an-activity-on-a-record) on a contact record by including the `hs_pinned_engagement_id` field in your request. In the field, include the `id` of the activity to pin, which can be retrieved via the [engagements APIs](/docs/api-reference/latest/overview). You can pin one activity per record, and the activity must already be associated with the contact prior to pinning. To set or update a contact’s pinned activity, your request could look like:


    {
      "properties": {
        "hs_pinned_engagement_id": 123456789
      }
    }


You can also create a contact, associate it with an existing activity, and pin the activity in the same request. For example:


    {
      "properties": {
        "email": "example@hubspot.com",
        "firstname": "Jane",
        "lastname": "Doe",
        "phone": "+18884827768",
        "hs_pinned_engagement_id": 123456789
      },
      "associations": [
        {
          "to": {
            "id": 123456789
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 201
            }
          ]
        }
      ]
    }


##

​

Delete contacts

You can delete contacts individually or in batches, which will add the contact to the recycling bin in HubSpot. You can later [restore the contact within HubSpot](https://knowledge.hubspot.com/records/restore-deleted-records). To delete an individual contact by its ID, make a `DELETE` request to `/crm/v3/objects/contacts/{contactId}`. Learn more about batch deleting contacts in the [reference documentation](/docs/api-reference/legacy/crm/objects/contacts/guide).

##

​

Additional emails

Additional email addresses are used when a contact has more than one email. These can be added [manually on a contact record in HubSpot](https://knowledge.hubspot.com/records/add-multiple-email-addresses-to-a-contact) or can be added automatically following a [contact merge](https://knowledge.hubspot.com/records/merge-records#contact-merge-exceptions). Additional emails are still unique identifiers for contacts, so multiple contacts cannot have the same additional email addresses. To view additional emails for contacts, when you retrieve all or individual contacts, include the `properties` parameter with the properties `email` and `hs_additional_emails`. A contact’s primary email address will be displayed in the `email` field and additional emails will be displayed in the `hs_additional_emails` field.

##

​

Limits

Batch operations are limited to 100 records at a time. For example, you cannot batch update more than 100 contacts in one request. There are also limits for [contacts and form submissions](https://developers.hubspot.com/docs#limits_contacts).

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)