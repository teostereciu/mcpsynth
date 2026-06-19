# Payments API

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/objects/commerce-payments/guide*

---

Commerce Payments

# Payments API

Retrieve information about payments.

Scope requirements

If you’ve set up payment processing through either [HubSpot payments](https://knowledge.hubspot.com/payment-processing/set-up-payments) or [Stripe payment processing](https://knowledge.hubspot.com/payment-processing/connect-your-stripe-account-as-a-payment-processor-in-hubspot), you can use the payments API to create and manage data related to [payments](https://knowledge.hubspot.com/payments/manage-payments) in HubSpot. This API includes endpoints for creating new payments, updating existing payments, retrieving payment data, and deleting payments. For example, use this API to:

  * Create a payment record when a customer completes a transaction in an external system.
  * Associate completed payment records with invoices to mark them as paid.
  * Retrieve all refunded payments.


##

​

Limitations

  * To use this API, the account must be set up to collect payments through either [HubSpot payments](https://knowledge.hubspot.com/payment-processing/set-up-payments) or [Stripe payment processing](https://knowledge.hubspot.com/payment-processing/connect-your-stripe-account-as-a-payment-processor-in-hubspot).
  * Payments created through Commerce Hub payment processing (i.e., HubSpot payments or Stripe payment processing) cannot be modified or deleted via this API.
  * This API cannot be used to create payments intended for payment processing. Rather, this API is intended for tracking payment data that represents revenue received outside of Commerce Hub.


##

​

Create payments

To create a payment, make a `POST` request to `/crm/objects/2026-03/commerce_payments`.

  * At a minimum, the request body will need to include the `properties` object with values for the `hs_initial_amount` and `hs_initiated_date` properties. You can include other properties as needed. Note that some properties are read-only and cannot be set via the API.
  * You can also include an `associations` array to set associations with other CRM records at the time of creation (e.g., contacts and orders).

For example, the `POST` request body below would create a payment with basic details that’s associated with a specific contact and order.


    {
      "properties": {
        "hs_initial_amount": "99.99",
        "hs_initiated_date": "2024-03-27T18:04:11.823Z",
        "hs_customer_email": "customer@example.com"
      },
      "associations": [
        {
          "to": {
            "id": 70791348501
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 387
            }
          ]
        },
        {
          "to": {
            "id": 44446244097
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 542
            }
          ]
        }
      ]
    }


Field| Type| Description
---|---|---
`properties`| Object| An object containing key-value pairs for each property to set.
`associations`| Array| An array containing association details.
`to`| Object| An object containing the ID of the CRM record you want to associate the payment with.
`types`| Array| An array containing association type details.
`associationCategory`| String| The [type of association](/docs/api-reference/latest/crm/associations/associate-records/guide#associate-records-with-a-label) (`HUBSPOT_DEFINED` or `USER_DEFINED`).
`associationTypeId`| Number| A unique identifier to indicate the association type between the payment and the other object.

The response will include information you provided during creation along with the payment ID and other HubSpot-set properties.


    {
      "id": "383552769679",
      "properties": {
        "hs_created_by_user_id": "8675309",
        "hs_createdate": "2025-06-10T21:39:48.394Z",
        "hs_customer_email": "customer@example.com",
        "hs_has_associated_invoice": "false",
        "hs_hubspot_payments_enabled": "false",
        "hs_initial_amount": "49.99",
        "hs_initial_amount_in_portal_currency": "49.99",
        "hs_initial_amount_in_settlement_currency": "49.99",
        "hs_initiated_date": "2024-03-27T18:04:11.823Z",
        "hs_lastmodifieddate": "2025-06-10T21:39:48.394Z",
        "hs_latest_status": "processing",
        "hs_net_amount": "49.99",
        "hs_net_amount_after_refunds": "49.99",
        "hs_net_amount_in_portal_currency": "49.99",
        "hs_net_amount_in_settlement_currency": "49.99",
        "hs_number_of_associated_invoices": "0",
        "hs_object_id": "383552769679",
        "hs_object_source": "CRM_UI",
        "hs_object_source_id": "userId:959199",
        "hs_object_source_label": "CRM_UI",
        "hs_object_source_user_id": "959199",
        "hs_payment_creation_method": "OTHER",
        "hs_payment_id": "9743960263",
        "hs_presentment_to_portal_currency_dated_exchange_rate": "1",
        "hs_total_discounts_amount": "0",
        "hs_total_discounts_amount_in_portal_currency": "0",
        "hs_updated_by_user_id": "959199"
      },
      "createdAt": "2025-06-10T21:39:48.394Z",
      "updatedAt": "2025-06-10T21:39:48.394Z",
      "archived": false
    }


##

​

Retrieve payments

Depending on the information you need, there are a few ways to retrieve payments:

  * To retrieve all payments, make a `GET` request to `crm/objects/2026-03/commerce_payments`.
  * To retrieve a payment, make a `GET` request to the above URL and specify an payment ID. For example: `crm/objects/2026-03/commerce_payments/44446244097`.
  * To retrieve payments that meet a specific set of criteria, you can make a `POST` request to the search endpoint and to filter payments by property values.

The response will include a few default properties, including the create date, last modified date.


    {
      "id": "44446244097",
      "properties": {
        "hs_createdate": "2023-03-08T14:54:17.333Z",
        "hs_lastmodifieddate": "2024-03-01T22:33:09.011Z",
        "hs_object_id": "44446244097"
      },
      "createdAt": "2023-03-08T14:54:17.333Z",
      "updatedAt": "2024-03-01T22:33:09.011Z",
      "archived": false
    }


To return specific properties, include a `properties` query parameter in the request URL along with comma-separated property names. For example, making a `GET` request to the following URL would result in the response below. `crm/objects/2026-03/commerce_payments?properties=hs_customer_email,hs_latest_status`


    {
      "id": "40744976671",
      "properties": {
        "hs_createdate": "2022-09-02T15:03:40.828Z",
        "hs_customer_email": "name@emailaddress.com",
        "hs_lastmodifieddate": "2024-02-27T15:03:53.620Z",
        "hs_object_id": "40744976671",
        "hs_latest_status": "succeeded"
      },
      "createdAt": "2022-09-02T15:03:40.828Z",
      "updatedAt": "2024-02-27T15:03:53.620Z",
      "archived": false
    }


###

​

Search for payments by properties

You can use the search endpoint to retrieve payments that meet a specific set of [filter criteria](/docs/api-reference/latest/crm/search-the-crm#filter-search-results). This will be a `POST` request that includes your filter criteria in the request body. For example, to search for all refunded payments, you would make a `POST` request to `crm/objects/2026-03/commerce_payments/search` with the following request body.


    {
      "filterGroups": [
        {
          "filters": [
            {
              "propertyName": "hs_latest_status",
              "value": "refunded",
              "operator": "EQ"
            }
          ]
        }
      ],
      "properties": ["hs_latest_status", "hs_customer_email"]
    }


Note that the `filters` array specifies the search criteria, while the `properties` array specifies which properties to return.

##

​

Update payments

To update a payment, make a `PATCH` request to `/crm/objects/2026-03/commerce_payments/{paymentId}`. In the request body, include a `properties` object containing the properties that you want to update. For example, if you wanted to update a payment’s status from “processing” to “succeeded”, you could send the following request body.


    {
      "properties": {
        "hs_latest_status": "succeeded"
      }
    }


The response will include a set of default properties along with the property that you just updated.


    {
      "id": "44446244097",
      "properties": {
        "hs_createdate": "2023-03-08T14:54:17.333Z",
        "hs_lastmodifieddate": "2024-03-27T20:03:05.890Z",
        "hs_latest_status": "succeeded",
        "hs_object_id": "44446244097"
      },
      "createdAt": "2023-03-08T14:54:17.333Z",
      "updatedAt": "2024-03-27T20:03:05.890Z",
      "archived": false
    }


##

​

Delete payments

To delete a payment, make a `DELETE` request to `/crm/objects/2026-03/commerce_payments/{paymentId}`. The payment will be moved to the recycling bin and can be restored within 90 days. After 90 days, the payment will be permanently deleted.

##

​

Properties

Payment details are stored in payment properties. HubSpot provides a set of default payment properties, but you can also create your own custom properties using the [properties API](/docs/api-reference/latest/crm/properties/guide). To get all payment properties, make a `GET` request to `/crm/properties/2026-03/commerce_payments`. When managing your payment data, you can use the writeable properties in the tables below.

  * `hs_currency_code` (enumeration): The currency code for the payment. Options will include the currencies [configured for the account](https://knowledge.hubspot.com/payment-processing/configure-currencies-for-commerce-hub).
  * `hs_customer_email` (string): The buyer’s email address.
  * `hs_fees_amount` (number): The total amount HubSpot charged to process this payment.
  * `hs_initial_amount` (number): The total amount the customer was charged.
  * `hs_initiated_date` (datetime): The date the payment was initiated.
  * `hs_internal_comment` (string): An internal note/comment left by a user when creating an external payment record from an invoice.
  * `hs_latest_status` (enumeration): The most recently set payment status. Options include:
    * `processing`
    * `succeeded`
    * `failed`
    * `partially_refunded`
    * `refunded`
    * `processing_refund`
    * `disputed_won`
    * `disputed_lost`
    * `disputed_action_required`
    * `disputed_awaiting_decision`
  * `hs_payment_method_bank_or_issuer` (string): The name of the bank or card issuer.
  * `hs_payment_method_last_4` (string): The last four digits of the payment method used.
  * `hs_payment_method_type` (enumeration): Depending on your [location](https://knowledge.hubspot.com/payment-processing/configure-currencies-for-commerce-hub#enable-bank-debit-payment-methods), the payment method the customer used. Options include:
    * `card`
    * `ach`
    * `cash`
    * `check`
    * `wire_transfer`
    * `other`
    * `sepa`
    * `bacs`
    * `pads`
  * `hs_payout_date` (date time): The date a bank deposit associated with this payment was made.
  * `hs_processor_type` (enumeration): The processor used to collect the payment. Options include:
    * `hs_payments`
    * `byo_stripe`
    * `none`
    * `quickbooks`
    * `xero`
  * `hs_reference_number` (string): The reference number associated with the external payment.
  * `hs_refunds_amount` (number): The total amount refunded to the customer.
  * `hs_billing_address_city` (string): The city for the payment method that the buyer used to make a payment.
  * `hs_billing_address_country` (string): The country for the payment method that the buyer used to make a payment.
  * `hs_billing_address_line_1` (string): The street address for the payment method that the buyer used to make a payment.
  * `hs_billing_address_line_2` (string): The apartment, unit number, or building for the payment method that the buyer used to make a payment. This is an optional field.
  * `hs_billing_address_state` (string): The state for the payment method that the buyer used to make a payment.
  * `hs_billing_address_zip` (string): The zip code for the payment method that the buyer used to make a payment.
  * `hs_line_item_discounts_amount` (number): The discount amount on the line items.
  * `hs_shipping_address_city` (string): The city of the shipping address associated with the payment.
  * `hs_shipping_address_country` (string): The country of the shipping address associated with the payment.
  * `hs_shipping_address_line_1` (string): The street address of the shipping address associated with the payment.
  * `hs_shipping_address_line_2` (string): The apartment, unit number, or building of the shipping address associated with the payment.
  * `hs_shipping_address_state` (string): The state of the shipping address associated with the payment.
  * `hs_shipping_address_zip` (string): The zip code of the shipping address associated with the payment.
  * `hs_shipping_ship_to_name` (string): The person’s name associated with the payment.


###

​

Read-only properties

The properties below are reserved for Commerce Hub payment processing and cannot be set via the API.

  * `hs_digital_wallet_type` (enumeration): The type of digital wallet type used to create the payment. Options include:
    * `apple_pay`
    * `google_pay`
    * `amex_express_checkout`
    * `link`
    * `masterpass`
    * `samsung_pay`
    * `visa_checkout`
  * `hs_fees_amount_in_settlement_currency` (number): The total amount HubSpot charged to process this payment in the settlement currency.
  * `hs_line_item_discounts_amount_in_portal_currency` (number): Line item discount amount in the account’s currency.
  * `hs_max_refundable_amount_in_portal_currency` (number): The maximum amount that can be refunded in the account’s default currency.
  * `hs_net_amount_in_settlement_currency` (number): The total amount you collected after fees in the settlement currency.
  * `hs_order_discount_code` (string): The discount code used.
  * `hs_order_discount_amount` (number): The discount amount on the order.
  * `hs_order_discount_percentage` (number): The discount percentage on the order.
  * `hs_payment_id` (string): The ID of the payment.
  * `hs_payment_method` (enumeration): How the customer made a payment, derived from an external source. Options depend on the [payment methods enabled for your account](https://knowledge.hubspot.com/payment-processing/configure-currencies-for-commerce-hub?hubs_content=knowledge.hubspot.com/payment-processing/connect-your-stripe-account-as-a-payment-processor-in-hubspot&hubs_content-cta=international%20currencies).
  * `hs_payment_source_app` (enumeration): The source that created the payment. Options include:
    * `SALES_CHECKOUT`
    * `QUOTE`
    * `INVOICE`
    * `MIGRATION`
    * `SUBSCRIPTION`
  * `hs_payment_source_id` (string): The ID of the source that created the payment.
  * `hs_payment_source_name` (string): The internal name of the source that created the payment.
  * `hs_payment_source_url` (string): The URL of the source that created the payment.
  * `hs_payment_type` (enumeration): The type of payment, the line item types on the payment (`one_time_or_initial` or `recurring`).
  * `hs_platform_fee` (number): The total amount charged to facilitate this payment.
  * `hs_platform_fee_in_portal_currency` (number): the total amount charged to facilitate this payment in the account’s default currency.
  * `hs_platform_fee_in_settlement_currency` (number): The total amount charged to facilitate this payment in the settlement currency.
  * `hs_refunds_amount_in_portal_currency` (number): The amount refunded in the account’s default currency.
  * `hs_settlement_currency_code` (enumeration): The currency code that the merchant’s payments will settle in. Options will include the currencies [configured for the account](https://knowledge.hubspot.com/payment-processing/configure-currencies-for-commerce-hub).
  * `hs_total_discounts_amount` (number): The sum of all discounts on a payment collected from the buyer, including line-item and order discounts.


##

​

Associations

You can associate the payment with other HubSpot CRM objects at creation by including an `associations` array. You can also use the [associations API](/docs/api-reference/latest/crm/associations/associate-records/guide) to update payments after creation. You can associate payments with the following CRM objects:

  * [Companies](/docs/api-reference/latest/crm/objects/companies/guide): `389`
  * [Contacts](/docs/api-reference/latest/crm/objects/contacts/guide): `387`
  * [Deals](/docs/api-reference/latest/crm/objects/deals/guide): `391`
  * [Discounts](/docs/api-reference/latest/crm/objects/discounts/guide): `428`
  * [Feedback submissions](/docs/api-reference/latest/crm/objects/feedback-submissions/guide): `1170`
  * [Invoices](/docs/api-reference/latest/crm/objects/invoices/guide): `542`
  * [Line items](/docs/api-reference/latest/crm/objects/line-items/guide): `395`
  * [Orders](/docs/api-reference/latest/crm/objects/orders/guide): `524`
  * [Payment links](https://knowledge.hubspot.com/payment-links/create-and-share-a-products-payment-link): `476`
  * [Quotes](/docs/api-reference/latest/crm/objects/quotes/guide): `397`
  * [Subscriptions](/docs/api-reference/latest/crm/objects/commerce-subscriptions/guide): `393`
  * [Tickets](/docs/api-reference/latest/crm/objects/tickets/guide): `1354`

To see a list of all association types, check out the [associations API documentation](/docs/api-reference/latest/crm/associations/associate-records/guide#association-type-id-values). Or, you can retrieve each value by making a `GET` request to `/crm/associations/2026-03/commerce_payments/{toObjectType}/labels`.

**Please note:** When retrieving line items from different objects created in HubSpot, you should expect to receive different IDs. This is because line items should only be associated with one object, which HubSpot handles automatically by creating copies of line items rather than using the same line item across multiple objects.

To update the associations for an existing payment, make a `PUT` request to `/crm/objects/2026-03/commerce_payments/{paymentId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`. You can also use the [associations API](/docs/api-reference/latest/crm/associations/associate-records/guide). For example, to associate an existing payment with an existing order, you would make a PUT request to the following URL: `/crm/objects/2026-03/commerce_payments/{paymentId}/associations/order/{orderId}/523` To remove an association from an existing payment, make a `DELETE` request to the following URL: `/crm/objects/2026-03/commerce_payments/{paymentId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`.

###

​

Retrieving a payment with associated contact

To retrieve a payment and contact associated with it, make a `GET` request to: `crm/objects/2026-03/commerce_payments/{contactId}/associations/contact` This will return the IDs of the currently associated contact, along with meta information about the association type.


    {
      "results": [
        {
          "id": "301",
          "type": "commerce_payment_to_contact"
        }
      ]
    }


You can then use the returned IDs to request more information about the line items through the [contacts API](/docs/api-reference/latest/crm/objects/contacts/guide). For example, you could retrieve the contact using its ID by making a `GET` request to `crm/objects/2026-03/contacts/{contactId}`


    {
      "id": "301",
      "properties": {
        "createdate": "2022-09-27T13:13:31.004Z",
        "email": "tom.bombadil@oldforest.com",
        "firstname": "Tom",
        "hs_object_id": "301",
        "lastmodifieddate": "2023-11-07T17:14:00.841Z",
        "lastname": "Bombadil"
      },
      "createdAt": "2022-09-27T13:13:31.004Z",
      "updatedAt": "2023-11-07T17:14:00.841Z",
      "archived": false
    }


Last modified on March 31, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)