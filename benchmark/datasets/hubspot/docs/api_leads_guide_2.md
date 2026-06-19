# CRM API | Leads

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/objects/leads/guide*

---

Leads

# CRM API | Leads

Leads are contacts or companies that are potential customers who have shown interest in your products or services. The leads endpoints allow you to manage this data and sync it between HubSpot and other systems.

Scope requirements

In HubSpot, [leads](https://knowledge.hubspot.com/object-settings/sync-lead-ownership-and-activities) are contacts or companies that are potential customers who have shown interest in your products or services. The leads endpoints allow you to create and manage lead records in your HubSpot account, as well as sync lead data between HubSpot and other systems. Before using the API, be sure leads have been [set up in your account](https://knowledge.hubspot.com/object-settings/sync-lead-ownership-and-activities). Learn more about objects, records, properties, and associations APIs in the [Understanding the CRM](/docs/guides/crm/understanding-the-crm) guide. For more general information about objects and records in HubSpot, [learn how to manage your CRM database](https://knowledge.hubspot.com/contacts-user-guide).

##

​

Create leads

To create new leads, make a `POST` request to `/crm/objects/2026-03/leads`. In the request body, include any details about the lead in a `properties` object. Your new lead:

  * Must have a lead name, specified using the `hs_lead_name` property.
  * Must be associated with an existing contact.
  * Should only be assigned to a user with a [seat](https://knowledge.hubspot.com/account-management/manage-seats). (Leads can only be worked via the workspace).


###

​

Properties

Lead details are stored in lead properties. There are [default HubSpot lead properties](https://knowledge.hubspot.com/properties/hubspots-default-lead-properties), but you can also [create custom lead properties](https://knowledge.hubspot.com/properties/create-and-edit-properties). To view all available properties, you can retrieve a list of your account’s lead properties by making a `GET` request to `/crm/properties/2026-03/leads`. See the table below for some common properties for leads:

Property| Description
---|---
`hs_lead_name`| The full name of the lead.
`hs_lead_type`| A dropdown list of lead types. You can edit or add new types in your [lead property settings.](https://knowledge.hubspot.com/properties/create-and-edit-properties#view-and-edit-properties)
`hs_lead_label`| The current status of the lead. You can edit or add new labels in your [lead property settings.](https://knowledge.hubspot.com/properties/create-and-edit-properties#view-and-edit-properties)

###

​

Associations

When creating a new lead you must associate the lead with [existing records](https://knowledge.hubspot.com/records/associate-records) in an associations object provided in the request body. In the associations object, you should include the following:

Parameter| Description
---|---
`to`| The record you want to associate with the lead, specified by its unique `id` value.
`types`| The type of the association between the lead and the record/activity. Include the `associationCategory`and `associationTypeId`. Default association type IDs are listed [here](/docs/api-reference/latest/crm/associations/associate-records/guide#association-type-id-values), or you can retrieve the value for custom association types (i.e. labels) via the [associations API](/docs/api-reference/latest/crm/associations/associate-records/guide#retrieve-association-types).

For example, to create a warm lead named “Jane Doe” who has a type of _New Business_ , your request body would resemble the following:


    {
      "associations": [
        {
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 578
            }
          ],
          "to": {
            "id": "12345"
          }
        }
      ],
      "properties": {
        "hs_lead_name": "Jane Doe",
        "hs_lead_type": "NEW BUSINESS",
        "hs_lead_label": "WARM"
      }
    }


##

​

Retrieve leads

You can retrieve leads individually or in batches.

  * To retrieve an individual lead, make a `GET` request to `/crm/objects/2026-03/leads/{leadsId}`.
  * To request a list of all leads, make a `GET` request to `/crm/objects/2026-03/leads`.

For these endpoints, you can include the following query parameters in the request URL:

Parameter| Description
---|---
`properties`| A comma separated list of the properties to be returned in the response. If a requested property isn’t defined, it won’t be included in the response. If a requested property is defined but a lead doesn’t have a value, it will be returned as `null`.
`propertiesWithHistory`| A comma separated list of the current and historical properties to be returned in the response. If a requested property isn’t defined, it won’t be included in the response. If a requested property is defined but a lead doesn’t have a value, it will be returned as `null`.
`associations`| A comma separated list of objects to retrieve associated IDs for. Any specified associations that don’t exist will not be returned in the response. Learn more about the [associations API.](/docs/api-reference/latest/crm/associations/associate-records/guide)

  * To retrieve a batch of specific leads by ID, make a `POST` request to `crm/objects/2026-03/leads/batch/read`. The batch endpoint _can’t_ retrieve associations. Learn how to batch read associations with the [associations API](/docs/api-reference/latest/crm/associations/associate-records/guide).

For the batch read endpoint, you can use the optional `Property` parameter to retrieve leads by `leadID` or a custom [unique identifier property](/docs/api-reference/latest/crm/properties/guide#create-unique-identifier-properties). By default, the `id` values in the request refer to the record ID (`hs_object_id`), so the `idProperty` parameter isn’t required when retrieving by record ID. If you’re using a custom unique value property to retrieve leads, you must include the `idProperty` parameter.

##

​

Update leads

You can update leads individually or in batches. For existing leads, the leads ID is a unique value, so you can use `leadsId` to update leads via the API. To update an individual lead by its lead ID, make a `PATCH` request to `/crm/objects/2026-03/leads/{leadsId}`, and include the data you want to update in the request body.

###

​

Associate existing leads with records

To associate a lead with other CRM records or an activity, make a `PUT` request to `/crm/objects/2026-03/leads/{leadsId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`.

To retrieve the `associationTypeId` value, refer to [this list](/docs/api-reference/latest/crm/associations/associate-records/guide#association-type-id-values) of default values, or make a `GET` request to `/crm/associations/2026-03/{fromObjectType}/{toObjectType}/labels`.

Learn more about the [associations API.](/docs/api-reference/latest/crm/associations/associate-records/guide)

###

​

Remove an association

To remove an association between a lead and a record or activity, make a `DELETE` request to the following URL: `/crm/objects/2026-03/leads/{leadId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`. If you remove all primary associations to the lead, the lead will automatically be deleted.

##

​

Delete leads

You can delete leads individually or in batches, which will add the lead to the recycling bin in HubSpot. You can later [restore the lead within HubSpot](https://knowledge.hubspot.com/records/restore-deleted-records). To delete an individual lead by its ID, make a `DELETE` request to `/crm/objects/2026-03/leads/{leadId}`. Learn more about deleting leads in the [reference documentation](/docs/api-reference/latest/crm/objects/leads/delete-lead).

##

​

Limits

Batch operations for creating, updating, and archiving are limited to batches of 100.

Last modified on March 31, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)