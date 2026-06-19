# Activities | Postal Mail

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/activities/postal-mail/guide*

---

Postal mail

# Activities | Postal Mail

Use the postal mail engagement API to log any postal mail you’ve sent to or received from contacts or companies on their CRM records.

Scope requirements

Use the postal mail engagement API to log and manage postal mail on CRM records. You can log the mail you’ve sent or received [in HubSpot](https://knowledge.hubspot.com/records/manually-log-activities-on-records) or through the postal mail API. You can also retrieve, update, or delete existing postal mail engagements. Below, learn the basic methods of managing postal mail through the API.

##

​

Create a postal mail engagement

To create a postal mail engagement, make a `POST` request to `/crm/objects/2026-03/postal_mail`. In the request body, add postal mail details in a **properties** object. You can also add an **associations** object to associate your new postal mail with an existing record (e.g., contacts, companies).

###

​

Properties

In the properties object, you can include the following fields:

Field| Description
---|---
`hs_timestamp`| The date that the postal mail was sent or received.
`hs_postal_mail_body`| The body text of the postal mail engagement.
`hubspot_owner_id`| The ID of the user that created the postal mail engagement.
`hs_attachment_ids`| The IDs of any attachments to the postal mail engagement. Multiple attachment IDs are separated by a semi-colon.

###

​

Associations

To create and associate a postal mail engagement with existing records, include an associations object in your request. For example, to create postal mail and associate it with two contacts, your request body might look similar to the following:


    {
      "properties": {
        "hs_timestamp": "2021-11-12",
        "hs_postal_mail_body": "Sent copy of contract to decision maker John",
        "hubspot_owner_id": "9274996",
        "hs_attachment_ids": "24332474034"
      },
      "associations": [
        {
          "to": {
            "id": 501
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 453
            }
          ]
        },
        {
          "to": {
            "id": 502
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 453
            }
          ]
        }
      ]
    }


In the associations object, you should include the following:

Parameter| Description
---|---
`to`| The record you want to associate with the postal mail, specified by its unique `id` value.
`types`| The type of the association between the postal mail and the record. Include the `associationCategory`and `associationTypeId`. Default association type IDs are listed [here](/docs/api-reference/latest/crm/associations/associate-records/guide#association-type-id-values), or you can retrieve the value for custom association types (i.e. labels) via the [associations API](/docs/api-reference/latest/crm/associations/associate-records/guide#retrieve-association-types).

##

​

Retrieve postal mail engagements

You can retrieve postal mail engagements individually or in bulk. To retrieve an individual postal mail engagement, make a `GET` request to `/crm/objects/2026-03/postal_mail/{postalMailId}`. You can include the following parameters in the request:

Parameter| Description
---|---
`properties`| A comma separated list of the properties to be returned. If a requested property isn’t defined, it won’t be included in the response. If a requested property is defined but a postal mail doesn’t have a value, it will be returned as `null`.
`associations`| A comma separated list of object types to retrieve associated IDs for. Any specified associations that don’t exist will not be returned in the response. Learn more about the [associations API.](/docs/api-reference/latest/crm/associations/associate-records/guide)

To retrieve a list of the postal mail engagements in your account, make a `GET` request to `/crm/objects/2026-03/postal_mail`. You can include the following parameters in the request:

Parameter| Description
---|---
`limit`| The maximum number of results to display per page.
`properties`| A comma separated list of the properties to be returned. If a requested property isn’t defined, it won’t be included in the response. If a requested property is defined but a postal mail doesn’t have a value, it will be returned as `null`.

When you make a successful batch request, the response will include the ID of each postal mail engagement, which you can use to retrieve, update, and delete postal mail engagements.

##

​

Update postal mail engagements

You can update postal mail engagements individually or in batches. To update an individual engagement by its ID, make a `PATCH` request to `/crm/objects/2026-03/postal_mail/{postalMailId}`. In the request body, include the properties that you want to update. For example, to update the body of the engagement, your request body might look similar to the following:


    {
      "properties": {
        "hs_postal_mail_body": "Sent copy of contract to decision maker John. Received  a call in response."
      }
    }


HubSpot will ignore values for read-only and non-existent properties. To clear a property value, pass an empty string for the property in the request body. Learn more about batch updating by checking out the [reference documentation](/docs/api-reference/latest/crm/activities/postal-mail/batch/update-postal-mail).

###

​

Associate existing postal mail with records

You can associate postal mail engagements with contact, company, deal, or ticket records. To associate postal mail with records, make a `PUT` request to `/crm/objects/2026-03/postal_mail/{postalMail}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`.

Parameter| Description
---|---
`postalMail`| The unique ID of the postal mail engagement.
`toObjectType`| The type of object that you want to associate the postal mail with (e.g., `contact` or `company`).
`toObjectId`| The ID of the record that you want to associate the postal mail with.
`associationTypeId`| A unique identifier to indicate the association type between the postal mail and the other object. The ID can be represented numerically or in snake case (e.g., `POSTAL_MAIL_TO_CONTACT`). You can retrieve the value through the [associations API](/docs/api-reference/latest/crm/associations/associate-records/guide).

For example, your request URL might look similar to the following: `https://api.hubspot.com/crm/objects/2026-03/postal_mail/25727582880/associations/contact/104901/POSTAL_MAIL_TO_CONTACT`

###

​

Remove an association

To remove an association between a postal mail engagement and a record, make a `DELETE` request to: `/crm/objects/2026-03/postal_mail/{postalMail}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`

##

​

Pin a postal mail engagement on a record

You can [pin a postal mail engagement](https://knowledge.hubspot.com/records/pin-an-activity-on-a-record) on a record so it remains on the top of the record’s timeline. The postal mail must already be associated with the record prior to pinning, and you can only pin one activity per record. To pin postal mail, include the postal mail’s `id` in the `hs_pinned_engagement_id` field when creating or updating a record via the object APIs. Learn more about using the [companies,](/docs/api-reference/latest/crm/objects/companies/guide#pin-an-activity-on-a-company-record)[contacts](/docs/api-reference/latest/crm/objects/contacts/guide#pin-an-activity-on-a-contact-record), [deals](/docs/api-reference/latest/crm/objects/deals/guide#pin-an-activity-on-a-deal-record), [tickets](/docs/api-reference/latest/crm/objects/tickets/guide#pin-an-activity-on-a-ticket-record), and [custom objects](/docs/api-reference/latest/crm/objects/custom-objects/guide) APIs.

##

​

Delete postal mail engagements

You can delete a postal mail engagement individually or in bulk, which will add the engagement to the recycling bin in HubSpot. You can later [restore the engagement from the record timeline](https://knowledge.hubspot.com/records/restore-deleted-activity-in-a-record). To delete an individual postal mail engagement by its ID, make a `DELETE` request to `/crm/objects/2026-03/postal_mail/{postalMailId}`.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)