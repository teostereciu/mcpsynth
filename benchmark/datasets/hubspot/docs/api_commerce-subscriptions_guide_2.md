# Subscriptions API

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/objects/commerce-subscriptions/guide*

---

Commerce Subscriptions

# Subscriptions API

Retrieve information about subscriptions.

Scope requirements

You can use the API endpoints listed below to create, update, and delete [commerce subscriptions](https://knowledge.hubspot.com/subscriptions/create-subscriptions) in an account.

**Please note:** if you’re looking to manage marketing email subscriptions instead, check out the [subscription preferences API](/docs/api-reference/legacy/communication-preferences/v3/guide).

##

​

Prerequisites

To use these APIs, the account must be set up to collect payments through either [HubSpot payments](https://knowledge.hubspot.com/payment-processing/set-up-payments) or [Stripe payment processing](https://knowledge.hubspot.com/payment-processing/connect-your-stripe-account-as-a-payment-processor-in-hubspot).

##

​

Scope Requirements

Based on your use-case, you’ll need to ensure that your app has authorized the following scopes:

  * `crm.objects.subscriptions.read`: grants access to view details about existing subscriptions.
  * `crm.objects.subscriptions.write`: grants access to create, update, and delete subscriptions.
  * `crm.schemas.subscriptions.read`: view details about property settings for subscriptions.
  * `crm.objects.line_items.read`: grants access to view details about existing line items.
  * `crm.objects.line_items.write`: grants access to create, update, and delete line items.
  * `crm.schemas.line_items.read`: view details about property settings for line items.


##

​

Create a subscription with a line item

To create a subscription, you’ll first need to create a line item, which you’ll then associate with the subscription. Once associated, you can associate additional CRM records such as contacts or companies with your subscription.

###

​

Create a line item

To create a line item, make a `POST` request to `/crm/objects/2026-03/line_items`. In the body of your request, include the line item’s details, such as its name, quantity, and price.


    {
      "properties": {
        "price": 10,
        "quantity": 1,
        "name": "New standalone line item"
      }
    }


Once you’ve successfully created a line item, the response will include its ID, which you can then use when you associate it with your subscription. Learn more about the [line items API](/docs/api-reference/latest/crm/objects/line-items/guide).

###

​

Create a subscription

To create a subscription, make a `POST` request to `/crm/objects/2026-03/subscriptions`. In the body of your request, include any details about your subscription, such as its name, collection process, and currency code. A list of common properties is provided in the table below. By default, a subscription is non-billable, which means its `hs_invoice_creation` property is set to `"off"`. Once your subscription has been created, you can set it to billable by following the instructions in the sections below. An example request body for a billable subscription is provided below:


    {
      "properties": {
        "hs_name": "New billable subscription",
        "hs_collection_process": "manual_payments",
        "hs_currency_code": "USD",
        "hs_net_payment_terms": "30",
        "hs_recurring_billing_start_date": {{startDate}},
        "hs_recurring_billing_frequency": "monthly"
      }
    }


###

​

Associate a subscription with your line item

With your subscription created, you can associate it with the line item you created. To create this association, make a `PUT` request to `/crm/objects/2026-03/subscriptions/{subscriptionId}/associations/line_item/{lineItemId}`, using the ID of your subscription as the `subscriptionId` and the ID of your line item as the `lineItemId`. In the request body, include the `associationCategory` and `associationTypeId` shown in the code block below that specifies the _Subscription to Line Item_ association:


    [
      {
        "associationCategory": "HUBSPOT_DEFINED",
        "associationTypeId": 301
      }
    ]


###

​

Associate a subscription with a CRM record

Now that your subscription is associated with a line item, you can also associate it with other CRM records, such as a contact or company. Learn more about the associations API in [this article](/docs/api-reference/latest/crm/associations/associate-records/guide), which provides a full list of association type ID values. For example, if you wanted to associate your subscription with a contact, you would make a `PUT` request to `/crm/objects/2026-03/subscriptions/{subscriptionId}/associations/contact/{contactId}`, using the ID of your subscription as the `subscriptionId` and the ID of the contact as the `contactId`. In the request body, include the `associationCategory` and `associationTypeId` shown below that specifies the _Subscription to Contact_ association:


    [
      {
        "associationCategory": "HUBSPOT_DEFINED",
        "associationTypeId": 295
      }
    ]


##

​

Make a subscription billable

To set the subscription as billable, make a `PATCH` request to `/crm/objects/2026-03/subscriptions/{subscriptionId}` and set the `hs_invoice_creation` property to `"on"` in the request body. The following properties can updated on a billable subscription once it’s been created:

  * `hs_name`
  * `hs_owner`
  * `hs_automatically_email_invoices`
  * `hs_allowed_payment_methods`
  * `hs_collect_address_types`
  * `hs_invoice_comments`
  * `hs_language`
  * `hs_locale`
  * `hs_name`
  * `hs_net_payment_terms`
  * `hs_recipient_billing_address`
  * `hs_recipient_billing_address2`
  * `hs_recipient_billing_city`
  * `hs_recipient_billing_country`
  * `hs_recipient_billing_state`
  * `hs_recipient_billing_zip`
  * `hs_payment_enabled`
  * `hs_tax_ids`
  * `hubspot_owner_id`

Billable subscriptions can only be deleted if they’ve expired or they’ve been cancelled.

##

​

Retrieve subscriptions

Depending on the information you need, there are a few ways to retrieve subscriptions:

  * To retrieve all subscriptions, make a `GET` request to `crm/objects/2026-03/subscriptions`.
  * To retrieve a specific subscription, make a `GET` request to the above URL and specify a subscription ID. For example: `crm/objects/2026-03/subscriptions/41112146008`.
  * To retrieve subscriptions that meet a specific set of criteria, you can make a `POST` request to the search endpoint and include filters in the request body. See an example of using the search endpoint below.

The response will include a few default properties, including the create date, last modified date.


    {
      "id": "41112146008",
      "properties": {
        "hs_createdate": "2023-03-08T14:54:17.333Z",
        "hs_lastmodifieddate": "2024-03-01T22:33:09.011Z",
        "hs_object_id": "44446244097"
      },
      "createdAt": "2023-03-08T14:54:17.333Z",
      "updatedAt": "2024-03-01T22:33:09.011Z",
      "archived": false
    }


###

​

Properties

To return specific properties, include a `properties` query parameter in the request URL along with comma-separated property names. For example, making a `GET` request to the following URL would result in the response below: `crm/objects/2026-03/subscriptions?properties=hs_status,hs_last_payment_amount`


    {
      "id": "41112146008",
      "properties": {
        "hs_createdate": "2022-09-02T15:03:40.828Z",
        "hs_last_payment_amount": "200.00",
        "hs_lastmodifieddate": "2024-02-27T15:03:53.620Z",
        "hs_object_id": "41112146008",
        "hs_status": "active"
      },
      "createdAt": "2022-09-02T15:03:40.828Z",
      "updatedAt": "2024-02-27T15:03:53.620Z",
      "archived": false
    }


To view all available subscription properties, make a `GET` request to `crm/properties/2026-03/subscriptions`. Learn more about using the [properties API](/docs/api-reference/latest/crm/properties/guide). Below are some common subscription properties that you may want to query.

Property name| Label in UI| Description
---|---|---
`hs_status`| [Status](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties#subscription-properties:~:text=the%20status%20of%20the%20subscription)| The current status of the subscription. Values include:

  * `active`
  * `past_due`
  * `canceled`
  * `expired`
  * `scheduled`


`hs_recurring_billing_start_date`| [Start date](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties#subscription-properties:~:text=for%20the%20subscription.-,Start%20date%3A,-the%20date%20the)| The date that the subscription is scheduled to start.
`hs_last_payment_amount`| [Last payment amount](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties#subscription-properties:~:text=is%20updated%20automatically.-,Last%20payment%20amount,-%3A%C2%A0the%20amount)| The amount that was charged during the most recent billing period.
`hs_next_payment_amount`| [Next payment amount](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties#subscription-properties:~:text=of%20the%20subscription.-,Next%20payment%20amount,-%3A%20the%20amount)| The amount that will be charged at the start of the next billing period.
`hs_next_payment_due_date`| [Next payment due date](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties#subscription-properties:~:text=Next%20payment%20due%20date)| The date that the next payment is due.

###

​

Search for subscriptions by properties

You can use the search endpoint to retrieve subscriptions that meet a specific set of [filter criteria](/docs/api-reference/latest/crm/search-the-crm#filter-search-results). This will be a `POST` request that includes your filter criteria in the request body. For example, to search for all currently active subscriptions, you would make a `POST` request to `crm/objects/2026-03/subscriptions/search` with the following request body:


    {
      "filterGroups": [
        {
          "filters": [
            {
              "propertyName": "hs_status",
              "value": "active",
              "operator": "EQ"
            }
          ]
        }
      ],
      "properties": ["hs_status", "hs_last_payment_amount"]
    }


Note that the `filters` array specifies the search criteria, while the `properties` array specifies which properties to return.

##

​

Associations

While you cannot set associations using this API, you can retrieve association information by making a GET request to the following URL: `crm/objects/2026-03/subscriptions/{hs_object_id}/associations/{associatedObjectName}` Associated objects can include [contacts](/docs/api-reference/latest/crm/objects/contacts/guide), [companies](/docs/api-reference/latest/crm/objects/companies/guide), [deals](/docs/api-reference/latest/crm/objects/deals/guide), [quotes](/docs/api-reference/latest/crm/objects/quotes/guide), [line items](/docs/api-reference/latest/crm/objects/line-items/guide), [payments](/docs/api-reference/latest/crm/objects/commerce-payments/guide), [discounts](/docs/api-reference/latest/crm/objects/discounts/guide), [fees](/docs/api-reference/latest/crm/objects/fees/guide), and [taxes](/docs/api-reference/latest/crm/objects/taxes/guide). These associations are typically set by the payment link or quote associated with the initial subscription payment. To manage these associations, you can [update the subscription in HubSpot](https://knowledge.hubspot.com/subscriptions/create-subscriptions#edit-a-subscription). Below is an example of how you might use this API combined with another API to get a specific set of association information.

**Please note:** Line items belong to one single parent object. For example, if retrieving line items from a subscription, the line item ID’s will be different to those on a deal, or a quote.

###

​

Retrieving a subscription with associated line items

To retrieve a subscription and the line items associated with it, make a `GET` request to: `/crm/objects/2026-03/subscriptions/{hs_object_id}/associations/line_items` This will return the IDs of the currently associated line items, along with meta information about the association type.


    {
      "results": [
        {
          "id": "1459694380",
          "type": "subscription_to_line_item"
        },
        {
          "id": "1459694381",
          "type": "subscription_to_line_item"
        }
      ]
    }


You can then use the returned IDs to request more information about the line items through the [line items API](/docs/api-reference/latest/crm/objects/line-items/guide). For example, you could batch retrieve line items by ID with the following `POST` request: `/crm/objects/2026-03/line_items/batch/read`


    {
      "inputs": [
        {
          "id": "1459694380"
        },
        {
          "id": "1459694381"
        }
      ],
      "properties": ["name", "amount"]
    }


The response would be formatted as follows:


    {
      "status": "COMPLETE",
      "results": [
        {
          "id": "1459694381",
          "properties": {
            "amount": "100.00",
            "createdate": "2023-11-08T18:23:06.361Z",
            "hs_lastmodifieddate": "2023-11-08T18:23:06.361Z",
            "hs_object_id": "1459694381",
            "name": "Recurring line item 2"
          },
          "createdAt": "2023-11-08T18:23:06.361Z",
          "updatedAt": "2023-11-08T18:23:06.361Z",
          "archived": false
        },
        {
          "id": "1459694380",
          "properties": {
            "amount": "100.00",
            "createdate": "2023-11-08T18:23:06.361Z",
            "hs_lastmodifieddate": "2023-11-08T18:23:06.361Z",
            "hs_object_id": "1459694380",
            "name": "Recurring line item 1"
          },
          "createdAt": "2023-11-08T18:23:06.361Z",
          "updatedAt": "2023-11-08T18:23:06.361Z",
          "archived": false
        }
      ],
      "startedAt": "2024-03-14T15:43:53.179Z",
      "completedAt": "2024-03-14T15:43:53.186Z"
    }


##

​

Update a subscription

To update other properties of a subscription after you’ve created it, you can make a `PATCH` request to `/crm/objects/2026-03/subscriptions/{subscriptionId}`, using the ID of the subscription as the `subscriptionId`, and including any fields you want to change in the properties field of the request body. For example, the following request body would change several address fields for the subscription:


    {
      "properties": {
        "hs_recipient_billing_address_source": "from_subscription",
        "hs_recipient_address": "2 Canal Park",
        "hs_recipient_city": "Cambridge",
        "hs_recipient_country": "US",
        "hs_recipient_state": "MA",
        "hs_recipient_zip": "02141"
      }
    }


##

​

Delete a subscription

To delete a subscription, make a `DELETE` request to `/crm/objects/2026-03/subscriptions/{subscriptionId}` using the ID of the subscription you want to delete as the subscriptionId:

  * If you’re attempting to delete a billable subscription, keep in mind that you can only delete subscriptions that have expired or that’ve been cancelled.
  * All non-billable subscriptions can be deleted, regardless of their status.


##

​

Pause a subscription

To pause a subscription, make a `POST` request to `/payments-subscriptions/v1/subscriptions/crm/{subscriptionId}/pause` using the ID of the subscription you want to pause as the `subscriptionId`.

##

​

Unpause a subscription

To unpause a subscription, make a `POST` request to `/payments-subscriptions/v1/subscriptions/crm/{subscriptionId}/unpause` using the ID of the subscription you want to unpause as the `subscriptionId`.

##

​

Cancel a subscription

To cancel a subscription, make a `POST` request to `/payments-subscriptions/v1/subscriptions/crm/{subscriptionId}/cancel` using the ID of the subscription you want to cancel as the `subscriptionId`.

Last modified on March 31, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)