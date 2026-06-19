# CRM API | Deals

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/objects/deals/guide*

---

Deals

# CRM API | Deals

A deal stores data about an ongoing transaction. The deals endpoints allow you to manage this data and sync it between HubSpot and other systems.

Scope requirements

In HubSpot, deals represent transactions with contacts or companies. Deals are tracked through your sales process in [pipeline stages](https://knowledge.hubspot.com/object-settings/set-up-and-customize-pipelines) until they’re won or lost. The deals endpoints allow you to manage create and manage deal records, as well as sync deal data between HubSpot and other systems. Learn more about objects, records, properties, and associations APIs in the [Understanding the CRM](/docs/guides/crm/understanding-the-crm) guide. For more general information about objects and records in HubSpot, [learn how to manage your CRM database](https://knowledge.hubspot.com/get-started/manage-your-crm-database).

##

​

Create deals

To create new deals, make a `POST` request to `/crm/objects/2026-03/deals`. In the request body, include your deal data in a `properties` object. You can also add an `associations` object to associate your new deal with existing records (e.g., contacts, companies), or activities (e.g., meetings, notes).

###

​

Properties

Deal details are stored in deal properties. HubSpot provides a set of [default deal properties](https://knowledge.hubspot.com/properties/hubspots-default-deal-properties), but you can also [create custom properties](https://knowledge.hubspot.com/properties/create-and-edit-properties). When creating a new deal, you should include the following properties in the request: `dealname`, `dealstage`, and if you have multiple pipelines, `pipeline`. If a pipeline isn’t specified, the default pipeline will be used. To view all available properties, you can retrieve a list of your account’s deal properties by making a `GET` request to `/crm/properties/2026-03/deals`. Learn more about the [properties API](/docs/api-reference/latest/crm/properties/guide).

**Please note:** You must use the internal ID of a deal stage or pipeline when creating a deal via the API. The internal ID will also be returned when you retrieve deals via the API. You can find a deal stage’s or pipeline’s internal ID in your [deal pipeline settings](https://knowledge.hubspot.com/object-settings/set-up-and-customize-pipelines#edit-or-delete-pipelines).

For example, to create a new deal, your request may look similar to the following:


    {
      "properties": {
        "amount": "1500.00",
        "closedate": "2019-12-07T16:50:06.678Z",
        "dealname": "New deal",
        "pipeline": "default",
        "dealstage": "contractsent",
        "hubspot_owner_id": "910901",
        "hs_all_collaborator_owner_ids": ";12345678;9101112"
      }
    }


###

​

Associations

When creating a new deal, you can also associate the deal with [existing records](https://knowledge.hubspot.com/records/associate-records) or [activities](https://knowledge.hubspot.com/records/associate-activities-with-records) in an `associations` object. For example, to associate a new deal with an existing contact and company, your request would look like the following:


    {
      "properties": {
        "amount": "1500.00",
        "closedate": "2019-12-07T16:50:06.678Z",
        "dealname": "New deal",
        "pipeline": "default",
        "dealstage": "contractsent",
        "hubspot_owner_id": "910901"
      },
      "associations": [
        {
          "to": {
            "id": 201
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 5
            }
          ]
        },
        {
          "to": {
            "id": 301
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 3
            }
          ]
        }
      ]
    }


In the `associations` object, you should include the following:

Parameter| Description
---|---
`to`| The record or activity you want to associate with the deal, specified by its unique `id` value.
`types`| The type of the association between the deal and the record/activity. Include the `associationCategory`and `associationTypeId`. Default association type IDs are listed [here](/docs/api-reference/latest/crm/associations/associate-records/guide#association-type-id-values), or you can retrieve the value for custom association types (i.e. labels) via the [associations API](/docs/api-reference/latest/crm/associations/associate-records/guide#retrieve-association-types).

##

​

Retrieve deals

You can retrieve deals individually or in batches.

  * To retrieve an individual deal, make a `GET` request to `/crm/objects/2026-03/deals/{dealId}`.
  * To request a list of all deals, make a `GET` request to `/crm/objects/2026-03/deals`.

For these endpoints, you can include the following query parameters in the request URL:

Parameter| Description
---|---
`properties`| A comma separated list of the properties to be returned in the response. If a requested property isn’t defined, it won’t be included in the response. If a requested property is defined but a deal doesn’t have a value, it will be returned as `null`.
`propertiesWithHistory`| A comma separated list of the current and historical properties to be returned in the response. If a requested property isn’t defined, it won’t be included in the response. If a requested property is defined but a deal doesn’t have a value, it will be returned as `null`.
`associations`| A comma separated list of objects to retrieve associated IDs for. Any specified associations that don’t exist will not be returned in the response. Learn more about the [associations API.](/docs/api-reference/latest/crm/associations/associate-records/guide)

  * To retrieve a batch of specific deals by record ID or a [custom unique identifier property](/docs/api-reference/latest/crm/properties/guide#create-unique-identifier-properties), make a `POST` request to `crm/objects/2026-03/deals/batch/read`.
    * The batch endpoint _cannot_ retrieve associations. Learn how to batch read associations with the [associations API](/docs/api-reference/latest/crm/associations/associate-records/guide).
    * To retrieve deals by a custom [unique identifier property](/docs/api-reference/latest/crm/properties/guide#create-unique-identifier-properties) rather than the deal ID, include the `idProperty` parameter in the request body to specify the property name. Then, in the `inputs` array, include the values of the unique identifier property rather than the deal ID.

For example, to retrieve a batch of deals, your request could look like either of the following:

get by id.txt

get by unique property.txt


    {
    "properties": ["dealname", "dealstage", "pipeline"],
    "inputs": [
    {
    "id": "7891023"
    },
    {
    "id": "987654"
    }
    ]
    }


To retrieve deals with current and historical values for a specific property, you can include the `propertiesWithHistory` parameter in the request body, as shown below.


    {
      "propertiesWithHistory": ["dealstage"],
      "inputs": [
        {
          "id": "7891023"
        },
        {
          "id": "987654"
        }
      ]
    }


##

​

Update deals

You can update deals individually or in batches. For existing deals, the deal ID is a default unique value that you can use to update the deal via API, but you can also identify deals using [custom unique identifier properties.](/docs/api-reference/latest/crm/properties/guide#create-unique-identifier-properties)

  * To update an individual deal by its record ID, make a `PATCH` request to `/crm/objects/2026-03/deals/{dealId}`, and include the data you want to update.
  * To update multiple deals, make a `POST` request to `/crm/objects/2026-03/deals/batch/update`. In the request body, include an array with the identifiers for the deals and the properties you want to update.


###

​

Associate existing deals with records or activities

To associate a deal with other CRM records or an activity, make a `PUT` request to `/crm/objects/2026-03/deals/{dealId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`.

To retrieve the `associationTypeId` value, refer to [this list](/docs/api-reference/latest/crm/associations/associate-records/guide#association-type-id-values) of default values, or make a `GET` request to `/crm/associations/2026-03/{fromObjectType}/{toObjectType}/labels`.

Learn more about associating records with the [associations API](/docs/api-reference/latest/crm/associations/associate-records/guide).

###

​

Remove an association

To remove an association between a deal and a record or activity, make a `DELETE` request to the following URL: `/crm/objects/2026-03/deals/{dealId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`.

##

​

Pin an activity on a deal record

You can pin an activity on a deal record via API by including the `hs_pinned_engagement_id` parameter in the request. For the value of the parameter, specify the ID of the activity to pin, which can be retrieved via the [engagements APIs](/docs/api-reference/latest/overview). You can pin one activity per record, and the activity must already be associated with the deal prior to pinning. To set or update a deal’s pinned activity, your request could look like:


    {
      "properties": {
        "hs_pinned_engagement_id": 123456789
      }
    }


You can also create a deal, associate it with an existing activity, and pin the activity in the same request. For example:


    {
      "properties": {
        "dealname": "New deal",
        "pipelines": "default",
        "dealstage": "contractsent",
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
              "associationTypeId": 213
            }
          ]
        }
      ]
    }


##

​

Delete deals

You can delete deals individually or in batches, which will add the deal to the recycling bin in HubSpot. You can later [restore the deal within HubSpot](https://knowledge.hubspot.com/records/restore-deleted-records).

  * To [delete an individual deal](/docs/api-reference/latest/crm/objects/deals/batch/delete-deals) by its ID, make a `DELETE` request to `/crm/objects/2026-03/deals/{dealId}`. No request body is needed for this request.
  * To [batch delete deals](/docs/api-reference/latest/crm/objects/deals/batch/delete-deals), make a `POST` request to `/crm/objects/2026-03/deals/batch/archive`. In the request body, include the deal ID values as the `id` inputs, as shown in the example request body below.


    {
      "inputs": [
        {
          "id": "123456"
        },
        {
          "id": "7891011"
        },
        {
          "id": "12123434"
        }
      ]
    }


Last modified on March 31, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)