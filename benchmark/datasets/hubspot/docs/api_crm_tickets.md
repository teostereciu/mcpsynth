# CRM API | Tickets

*Source: https://developers.hubspot.com/docs/api/crm/tickets*

---

Tickets

# CRM API | Tickets

A ticket represents a customer request for support. The tickets endpoints allow you to manage this data and sync it between HubSpot and other systems.

Scope requirements

In HubSpot, tickets represents customer requests for help. Tickets are tracked through your support process in [pipeline statuses](https://knowledge.hubspot.com/object-settings/set-up-and-customize-pipelines) until they’re closed. The tickets endpoints allow you to manage create and manage ticket records, as well as sync ticket data between HubSpot and other systems. Learn more about objects, records, properties, and associations APIs in the [Understanding the CRM](/docs/guides/crm/understanding-the-crm) guide. For more general information about objects and records in HubSpot, [learn how to manage your CRM database](https://knowledge.hubspot.com/get-started/manage-your-crm-database).

##

​

Create tickets

To create new tickets, make a `POST` request to `/crm/v3/objects/tickets`. In your request, include your ticket data in a properties object. You can also add an associations object to associate your new ticket with existing records (e.g., contacts, companies), or activities (e.g., meetings, notes).

###

​

Properties

Ticket details are stored in ticket properties. There are [default HubSpot ticket properties](https://knowledge.hubspot.com/properties/hubspots-default-ticket-properties), but you can also [create custom properties](https://knowledge.hubspot.com/properties/create-and-edit-properties). When creating a new ticket, you should include the following properties in your request: `subject` (the ticket’s name), `hs_pipeline_stage` (the ticket’s status) and if you have multiple pipelines, `hs_pipeline`. If a pipeline isn’t specified, the default pipeline will be used. To view all available properties, you can retrieve a list of your account’s ticket properties by making a `GET` request to `/crm/v3/properties/tickets`. Learn more about the [properties API](/docs/api-reference/legacy/crm/properties/guide).

**Please note:** You must use the internal ID of a ticket status or pipeline when creating a ticket via the API. The internal ID is a number, which will also be returned when you retrieve tickets via the API. You can find a ticket status or pipeline’s internal ID in your [ticket pipeline settings.](https://knowledge.hubspot.com/object-settings/set-up-and-customize-pipelines)

For example, to create a new ticket, your request may look similar to the following:


    ///Example request body
    {
      "properties": {
        "hs_pipeline": "0",
        "hs_pipeline_stage": "1",
        "hs_ticket_priority": "HIGH",
        "subject": "troubleshoot report"
      }
    }


###

​

Associations

When creating a new ticket, you can also associate the ticket with [existing records](https://knowledge.hubspot.com/records/associate-records) or [activities](https://knowledge.hubspot.com/records/associate-activities-with-records) by including an associations object. For example, to associate a new ticket with an existing contact and company, your request would look like the following:


    {
      "properties": {
        "hs_pipeline": "0",
        "hs_pipeline_stage": "1",
        "hs_ticket_priority": "HIGH",
        "subject": "troubleshoot report"
      },
      "associations": [
        {
          "to": {
            "id": 201
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 16
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
              "associationTypeId": 26
            }
          ]
        }
      ]
    }


In the associations object, you should include the following:

Parameter| Description
---|---
`to`| The record or activity you want to associate with the ticket, specified by its unique `id` value.
`types`| The type of the association between the ticket and the record/activity. Include the `associationCategory`and `associationTypeId`. Default association type IDs are listed [here](/docs/api-reference/legacy/crm/associations/associate-records/guide#association-type-id-values), or you can retrieve the value for custom association types (i.e. labels) via the [associations API](/docs/api-reference/legacy/crm/associations/associate-records/guide#retrieve-association-types).

##

​

Retrieve tickets

You can retrieve tickets individually or in batches.

  * To retrieve an individual ticket, make a `GET` request to `/crm/v3/objects/tickets/{ticketId}`.
  * To request a list of all tickets, make a `GET` request to `/crm/v3/objects/tickets`.

For these endpoints, you can include the following query parameters in the request URL:

Parameter| Description
---|---
`properties`| A comma separated list of the properties to be returned in the response. If a requested property isn’t defined, it won’t be included in the response. If a requested property is defined but a ticket doesn’t have a value, it will be returned as `null`.
`propertiesWithHistory`| A comma separated list of the current and historical properties to be returned in the response. If a requested property isn’t defined, it won’t be included in the response. If a requested property is defined but a ticket doesn’t have a value, it will be returned as `null`.
`associations`| A comma separated list of objects to retrieve associated IDs for. Any specified associations that don’t exist will not be returned in the response. Learn more about the [associations API.](/docs/api-reference/legacy/crm/associations/associate-records/guide)

  * To retrieve a batch of specific tickets by record ID or a [custom unique identifier property](/docs/api-reference/legacy/crm/properties/guide#create-unique-identifier-properties), make a `POST` request to `crm/v3/objects/tickets/batch/read`. The batch endpoint _cannot_ retrieve associations. Learn how to batch read associations with the [associations API](/docs/api-reference/legacy/crm/associations/associate-records/guide).

For the batch read endpoint, you can also use the optional `idProperty` parameter to retrieve tickets by a custom [unique identifier property](/docs/api-reference/legacy/crm/properties/guide#create-unique-identifier-properties). By default, the `id` values in the request refer to the record ID (`hs_object_id`), so the `idProperty` parameter is not required when retrieving by record ID. To use a custom unique value property to retrieve tickets, you must include the `idProperty` parameter. For example, to retrieve a batch of tickets, your request could look like either of the following:


    {
      "properties": ["subject", "hs_pipeline_stage", "hs_pipeline"],
      "inputs": [
        {
          "id": "4444888856"
        },
        {
          "id": "666699988"
        }
      ]
    }


    {
      "properties": ["subject", "hs_pipeline_stage", "hs_pipeline"],
      "idProperty": "uniquepropertyexample",
      "inputs": [
        {
          "id": "abc"
        },
        {
          "id": "def"
        }
      ]
    }


To retrieve tickets with current and historical values for a property, your request could look like:


    {
      "propertiesWithHistory": ["hs_pipeline_stage"],
      "inputs": [
        {
          "id": "4444888856"
        },
        {
          "id": "666699988"
        }
      ]
    }


##

​

Update tickets

You can update tickets individually or in batches. For existing tickets, the record ID is a default unique value that you can use to update the ticket via API, but you can also identify and update tickets using [custom unique identifier properties.](/docs/api-reference/legacy/crm/properties/guide#create-unique-identifier-properties)

  * To update an individual ticket by its record ID, make a `PATCH` request to `/crm/v3/objects/tickets/{ticketId}`, and include the data you want to update.
  * To update multiple tickets, make a `POST` request to `/crm/v3/objects/tickets/batch/update`. In the request body, include an array with the identifiers for the tickets and the properties you want to update.


###

​

Associate existing tickets with records or activities

To associate a ticket with other CRM records or an activity, make a `PUT` request to `/crm/v3/objects/tickets/{ticketId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`.

To retrieve the `associationTypeId` value, refer to [this list](/docs/api-reference/legacy/crm/associations/associate-records/guide#association-type-id-values) of default values, or make a `GET` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`.

Learn more about the [associations API.](/docs/api-reference/legacy/crm/associations/associate-records/guide)

###

​

Remove an association

To remove an association between a ticket and a record or activity, make a `DELETE` request to the following URL: `/crm/v3/objects/tickets/{ticketId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`.

##

​

Pin an activity on a ticket record

You can pin an activity on a ticket record via API by including the `hs_pinned_engagement_id` field in your request. In the field, include the `id` of the activity to pin, which can be retrieved via the [engagements APIs](/docs/api-reference/latest/overview). You can pin one activity per record, and the activity must already be associated with the ticket prior to pinning. To set or update a ticket’s pinned activity, your request could look like:


    {
      "properties": {
        "hs_pinned_engagement_id": 123456789
      }
    }


You can also create a ticket, associate it with an existing activity, and pin the activity in the same request. For example:


    {
      "properties": {
        "hs_pipeline": "0",
        "hs_pipeline_stage": "1",
        "hs_ticket_priority": "HIGH",
        "subject": "troubleshoot report",
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
              "associationTypeId": 227
            }
          ]
        }
      ]
    }


##

​

Delete tickets

You can delete tickets individually or in batches, which will add the ticket to the recycling bin in HubSpot. You can later [restore the ticket within HubSpot](https://knowledge.hubspot.com/records/restore-deleted-records). To delete an individual ticket by its ID, make a `DELETE` request to `/crm/v3/objects/tickets/{ticketId}`. Learn more about deleting tickets in the [reference documentation](/docs/api-reference/legacy/crm/objects/tickets/guide#delete-%2Fcrm%2Fv3%2Fobjects%2Ftickets%2F%7Bticketid%7D).

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)