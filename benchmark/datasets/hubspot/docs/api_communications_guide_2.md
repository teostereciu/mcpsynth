# Engagements | Communications

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/objects/communications/guide*

---

Communications

# Engagements | Communications

Learn how to use the communication APIs, which allow you to log WhatsApp, LinkedIn, and SMS messages to the CRM record timeline.

Scope requirements

You can log external communications via WhatsApp, LinkedIn, or SMS messages on CRM records to add information about the message to the record timeline. You can [log a message directly in your HubSpot account](https://knowledge.hubspot.com/records/manually-log-activities-on-records) or using the API endpoints below.

**Please note:** the Communications API does not apply to marketing SMS messages. Learn how to create and view [marketing SMS messages in HubSpot](https://knowledge.hubspot.com/sms/create-and-send-sms-messages).

##

​

Create a WhatsApp, LinkedIn, or SMS message

To create a message, make a `POST` request to `/crm/objects/2026-03/communications`. In the request body, add message details in a **properties** object. You can also add an **associations** object to associate your new message with an existing record (e.g., contacts, companies).

###

​

Properties

In the properties object, you can include the following fields:

Parameter| Description
---|---
`hs_communication_channel_type`| The channel type of the message that you sent or received from the contact. Supported values are `WHATS_APP`, `LINKEDIN_MESSAGE`, or `SMS`.
`hs_communication_logged_from`| Enum used to differentiate between conversations objects. This must be set to `CRM` in your request.
`hs_communication_body`| The text body of the message.
`hubspot_owner_id`| The [ID of the owner](/docs/api-reference/latest/crm/owners/guide) associated with the message. This field determines the user listed as the message creator on the record timeline.
`hs_timestamp`| This field marks the message’s time of creation and determines where the message appears on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format.

###

​

Associations

To create and associate a postal mail engagement with existing records, include an associations object in your request. For example, if you want to log an SMS message and associate it with a contact and company, your request body might resemble the following:


    {
      "properties": {
        "hs_communication_channel_type": "SMS",
        "hs_communication_logged_from": "CRM",
        "hs_communication_body": "Texted Linda to confirm that we're ready to move forward with the contract.",
        "hs_timestamp": "2022-11-12T15:48:22Z",
        "hubspot_owner_id": 1234567
      },
      "associations": [
        {
          "to": {
            "id": 9001
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 87
            }
          ]
        },
        {
          "to": {
            "id": 1234
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 81
            }
          ]
        }
      ]
    }


In the associations object, you should include the following:

Field| Description
---|---
`to`| The record you want to associate with the message, specified by its unique `id` value.
`types`| The type of the association between the message and the record. Include the `associationCategory`and `associationTypeId`. Default association type IDs are listed [here](/docs/api-reference/latest/crm/associations/associate-records/guide#association-type-id-values), or you can retrieve the value for custom association types (i.e. labels) via the [associations API](/docs/api-reference/latest/crm/associations/associate-records/guide#retrieve-association-types).

The response to your request will include an ID that you can use to update or associate the message with a record:


    // Example response from POST request to https://api.hubapi.com/crm/objects/2026-03/communications
    {
      "id": "12021896773",
      "properties": {
        "hs_communication_channel_type": "SMS ",
        "hs_communication_logged_from": "CRM",
        "hs_communication_body": "Texted John to confirm that we're ready to move forward with the contract.",
        "hs_timestamp": "2022-11-12T15:48:22Z",
        "hs_createdate": "2022-11-29T18:35:00.484Z",
        "hs_lastmodifieddate": "2022-11-29T18:35:00.484Z",
        "hs_object_id": "12021896773"
      },
      "createdAt": "2022-11-29T18:35:00.484Z",
      "updatedAt": "2022-11-29T18:35:00.484Z",
      "archived": false
    }


##

​

Retrieve messages

You can retrieve messages individually or in batches. To retrieve an individual messages, make a `GET` request to `/crm/objects/2026-03/communication/{communicationId}`. To request a list of all of logged WhatsApp, LinkedIn, and SMS messages, make a `GET` request to `/crm/objects/2026-03/communications`. For both endpoints, you can include the following query parameters in the request URL:

Parameter| Description
---|---
`properties`| A comma separated list of the properties to be returned in the response. If a requested property isn’t defined, it won’t be included in the response. If a requested property is defined but a communication doesn’t have a value, it will be returned as `null`.
`associations`| A comma separated list of object types to retrieve associated IDs for. Any specified associations that don’t exist will not be returned in the response. Learn more about the [associations API.](/docs/api-reference/latest/crm/associations/associate-records/guide)

For example, to retrieve messages with their text content and any associated contact IDs, your request URL might look similar to the following: `https://api.hubapi.com/crm/objects/2026-03/communications?limit=10&properties=hs_communication_body&associations=contact&archived=false`. Learn more about retrieving a batch of messages by internal ID or unique property value in the [reference documentation](/docs/api-reference/latest/crm/objects/communications/batch/get-communications).

##

​

Update messages

You can update messages individually or in batches. To update an individual message by its communication ID, make a `PATCH` request to `/crm/objects/2026-03/communications/{communicationId}`. In the request body, include the message properties that you want to update:


    // Example PATCH request to https://api.hubapi.com/crm/objects/2026-03/communications/{communicationId}
    {
      "properties": {
        "hs_communication_body": "Sent a follow-up message to Carla."
      }
    }


HubSpot will ignore values for read-only and non-existent properties. To clear a property value, pass an empty string for the property in the request body. Learn more about batch updating messages in the [reference documentation](/docs/api-reference/latest/crm/objects/communications/batch/update-communications).

###

​

Associate an existing message with a record

To associate a message with other CRM records, such as a contact, make a `PUT` request to `/crm/objects/2026-03/communications/{communicationId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`. The request URL contains the following fields:

Field| Description
---|---
`communicationId`| The ID of your WhatsApp, LinkedIn, or SMS message.
`toObjectType`| The type of object that you want to associate the message with (e.g., contact or company)
`toObjectId`| The ID of the record that you want to associate the message with.
`associationTypeId`| A unique identifier to indicate the association type between the message and the other object. The ID can be represented numerically or in snake case (e.g., `communication_to_contact`). You can retrieve the value through the [associations API](/docs/api-reference/latest/crm/associations/associate-records/guide).

For example, your request URL might look similar to the following: `https://api.hubapi.com/crm/objects/2026-03/communications/12021896773/associations/contact/581751/communication_to_contact`

###

​

Remove an association

To remove an association between a message and a record, make a `DELETE` request to the same URL as above: `/crm/objects/2026-03/communications/{communicationId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`

##

​

Pin a message on a record

You can [pin a message](https://knowledge.hubspot.com/records/pin-an-activity-on-a-record) on a record so it remains on the top of the record’s timeline. The message must already be associated with the record prior to pinning, and you can only pin one activity per record. To pin a message, include the message’s `id` in the `hs_pinned_engagement_id` field when creating or updating a record via the object APIs. Learn more about using the [companies,](/docs/api-reference/latest/crm/objects/companies/guide#pin-an-activity-on-a-company-record)[contacts](/docs/api-reference/latest/crm/objects/contacts/guide#pin-an-activity-on-a-contact-record), [deals](/docs/api-reference/latest/crm/objects/deals/guide#pin-an-activity-on-a-deal-record), [tickets](/docs/api-reference/latest/crm/objects/tickets/guide#pin-an-activity-on-a-ticket-record), and [custom objects](/docs/api-reference/latest/crm/objects/custom-objects/guide) APIs.

##

​

Delete messages

You can delete messages individually or in batches, which will add the message to the recycling bin in HubSpot. You can later [restore the message from the record timeline](https://knowledge.hubspot.com/records/restore-deleted-activity-in-a-record). To delete an individual message by its ID, make a `DELETE` request to `/crm/objects/2026-03/communications/{communicationId}`.

Last modified on March 31, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)