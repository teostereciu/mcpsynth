# Invoices

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/objects/invoices/guide*

---

Invoices

# Invoices

Use the invoices API to create, manage, retrieve, and delete the invoices used for billing your customers.

Scope requirements

Use the invoices API to create, update, fetch, and delete [invoices](https://knowledge.hubspot.com/invoices/create-invoices). Once configured, an invoice can be shared with a buyer at a specified URL. Users can also [create and manage invoices in HubSpot](https://knowledge.hubspot.com/invoices/create-invoices#manage-invoices) to add details, update associations, and more. If you’ve set up either [HubSpot payments](https://knowledge.hubspot.com/payment-processing/set-up-payments) or [Stripe payment processing](https://knowledge.hubspot.com/payment-processing/connect-your-stripe-account-as-a-payment-processor-in-hubspot), you can configure an invoice to be payable through this API. For example, use this API to create a new invoice or fetch all currently open invoices.

##

​

Create invoices

The invoice creation process can be broken up into the following steps:

  1. **Create an invoice:** create a draft invoice and set the currency.
  2. **Configure the invoice:** add associations to CRM records, such as a contact and line items to the invoice, properties, and configure payment settings.
  3. **Move the invoice status to open:** move the invoice status from `draft` to `open`.
  4. **Share the invoice:** share the invoice with the buyer.

To create an invoice, you’ll first configure its basic details by making a `POST` request to `/crm/objects/2026-03/invoices`. In the post body, include a `properties` object to store basic invoice information.

  * The only property required for creating a draft invoice is `hs_currency`, which accepts a string value of a currency code (e.g., `USD`).
  * You can modify a drafted invoice’s properties any time by updating the invoice.
  * The invoice will inherit other property values when you later associate a contact with it, such as contact and company details, which will be required before you can set the invoice to the _Open_ state. Learn more about updating properties and adding associations.


Depending on your preferred workflow, you can instead create a draft invoice with associations through one POST request, rather than making two separate requests.


    {
      "properties": {
        "hs_currency": "USD"
      }
    }


The response will include an `id`, which you’ll use to continue configuring the invoice. You can update invoice properties at any time by making a `PATCH` request to `/crm/objects/2026-03/invoices/{invoiceId}`.

###

​

Invoice configuration

To move the invoice to the `open` status so that it can be shared and paid, you’ll need to set a few required properties and associate it with other CRM records, such as line items and a contact. If you’ve set up [HubSpot payments](https://knowledge.hubspot.com/payment-processing/set-up-payments) or [Stripe payment processing](https://knowledge.hubspot.com/payment-processing/connect-your-stripe-account-as-a-payment-processor-in-hubspot), you can also configure the invoice’s payment settings.

####

​

Update invoice properties

To update an invoice’s properties, make a `PATCH` request to `/crm/objects/2026-03/invoices/{invoiceId}`. In the request body, include a properties object with fields for the properties you want to update.


    {
      "properties": {
        "hs_currency": "USD",
        "hs_invoice_date": "2025-12-05T17:29:08.788Z",
        "hs_due_date": "2026-01-05T17:29:08.000Z",
        "hs_tax_id": "US EIN 12-3456789"
      }
    }


Property| Description|
---|---|---
`hs_currency`| String| Currency of the invoice (e.g., `USD`).
`hs_invoice_date`| Datetime| Date of the invoice. Can be formatted as ISO 8601 or UNIX timestamp in milliseconds. If no value is provided, this property will be set automatically to the current datetime.
`hs_due_date`| Datetime| Due date of the invoice. Can be formatted as ISO 8601 or UNIX timestamp in milliseconds. If no value is provided, this property will be set automatically to the current datetime.
`hs_tax_id`| String| The account tax ID listed on the invoice, which includes a tax ID type and a tax ID number. If the account has a configured [default tax ID for invoices](https://knowledge.hubspot.com/invoices/set-up-the-hubspot-invoices-tool#customization), this property will be set automatically if not provided.

####

​

Add associations

To associate other CRM records with the invoice, make a `PUT` request to `/crm/objects/2026-03/invoices/{fromObjectId}/associations/default/{toObjectType}/{toObjectId}`. The table below show which CRM record associations are required to move the invoice to the Open state, and which are optional. [View a full list of the objects can be associated with invoices](/docs/api-reference/latest/crm/associations/associate-records/guide#invoice-to-object).

**Please note:** A _Draft_ invoice can be created without any associations.

Object type| Required| Description
---|---|---
[Line items](/docs/api-reference/latest/crm/objects/line-items/guide)| Yes| The goods and/or services being sold through the invoice. You can create line items from [products in your product library](/docs/api-reference/latest/crm/objects/products/guide) or create custom standalone line items.
[Contact](/docs/api-reference/latest/crm/objects/contacts/guide)| Yes| Specific buyers that you’re addressing in the invoice.
[Company](/docs/api-reference/latest/crm/objects/companies/guide)| No| A specific company that you’re addressing in the invoice.
[Discounts](/docs/api-reference/latest/crm/objects/discounts/guide), [fees](/docs/api-reference/latest/crm/objects/fees/guide), and [taxes](/docs/api-reference/latest/crm/objects/taxes/guide)| No| Any discounts, fees, and taxes to be applied at checkout. When determining the total invoice amount, HubSpot first applies discounts, followed by fees, then taxes. You can use the `hs_sort_order` field to reorder objects of the same type. Can be set to fixed values or percentages by setting `hs_type` to either `FIXED` or `PERCENT`.

To make each association, you’ll first need to retrieve the ID of each object you want to associate. To retrieve each ID, you’ll make a `GET` request to the relevant object endpoint, which follows the same pattern across each CRM object.


    #GET request for line items
    curl --request GET \
      --url 'https://api.hubapi.com/crm/objects/2026-03/line_items?archived=false' \
      --header 'authorization: Bearer YOUR_ACCESS_TOKEN'

    #GET request for contacts
    curl --request GET \
      --url 'https://api.hubapi.com/crm/objects/2026-03/contacts?archived=false' \
      --header 'authorization: Bearer YOUR_ACCESS_TOKEN'

    #GET request for companies
    curl --request GET \
      --url 'https://api.hubapi.com/crm/objects/2026-03/companies?archived=false' \
      --header 'authorization: Bearer YOUR_ACCESS_TOKEN'

    #GET request for discounts
    curl --request GET \
      --url 'https://api.hubapi.com/crm/objects/2026-03/discounts?archived=false' \
      --header 'authorization: Bearer YOUR_ACCESS_TOKEN'

    #GET request for fees
    curl --request GET \
      --url 'https://api.hubapi.com/crm/objects/2026-03/fees?archived=false' \
      --header 'authorization: Bearer YOUR_ACCESS_TOKEN'

    #GET request for taxes
    curl --request GET \
      --url 'https://api.hubapi.com/crm/objects/2026-03/taxes?archived=false' \
      --header 'authorization: Bearer YOUR_ACCESS_TOKEN'


Each successful call will return a `200` response with details for each fetched object type. You’ll use the value in the `id` field to set associations in the next step.


    {
      "results": [
        {
          "id": "54486102441",
          "properties": {
            "hs_createdate": "2024-03-18T07:34:29.586Z",
            "hs_lastmodifieddate": "2024-03-18T07:34:29.586Z",
            "hs_object_id": "54486102441",
            "hs_type": "PERCENT",
            "hs_value": "20.0000"
          },
          "createdAt": "2024-03-18T07:34:29.586Z",
          "updatedAt": "2024-03-18T07:34:29.586Z",
          "archived": false
        }
      ]
    }


####

​

Make an invoice non-billable

A non-billable invoice won’t render, meaning an invoice document won’t be created, and other invoice functionalities, such as validation, email, and notifications, will not be included. This could be useful if you want to track invoice data in HubSpot, but manage or bill the invoices outside of HubSpot. To make an invoice non-billable, create an invoice, making a `POST` request to `/crm/objects/2026-03/invoices` and include the `hs_invoice_billable` property.


    {
      "properties": {
        "hs_currency": "USD",
        "hs_invoice_billable": "false"
      }
    }


####

​

Configure payment settings

**Please note:**

  * Recording payments manually is not possible via the API but is [possible in the platform](https://knowledge.hubspot.com/invoices/create-invoices#manage-finalized-invoices).
  * The HubSpot account must have either [HubSpot payments](https://knowledge.hubspot.com/payment-processing/set-up-payments) or [Stripe payment processing](https://knowledge.hubspot.com/payment-processing/connect-your-stripe-account-as-a-payment-processor-in-hubspot) set up before using this capability.


If your account is set up to collect digital payments using HubSpot payments or Stripe payment processing, and the currency of the invoice is set to a [currency that is valid for transacting](https://knowledge.hubspot.com/payment-processing/configure-currencies-for-commerce-hub#available-currencies), the invoice will automatically be configured to collect payments. In addition, other properties will automatically be set based on the account [payment settings](https://knowledge.hubspot.com/payment-processing/configure-your-buyer-checkout-experience#set-the-default-payment-method-and-shipping-information). The properties below can be amended if required. This is not an exhaustive list. To get a list of all available properties, make a `GET` request to `/crm/objects/2026-03/invoices`.

Parameter| Type| Description
---|---|---
`hs_allowed_payment_methods`| Enumeration| The payment methods to be used. For example, `credit_or_debit_card`, `ach`.

  * [Accepted payment methods when using HubSpot payments](https://knowledge.hubspot.com/payment-processing/set-up-payments).
  * [Accepted payment methods when using Stripe as a payment processor](https://knowledge.hubspot.com/payment-processing/connect-your-stripe-account-as-a-payment-processor-in-hubspot#configure-currencies-and-payment-methods).

If no value is provided, this property will be set automatically based on the account [payment settings](https://knowledge.hubspot.com/payment-processing/configure-your-buyer-checkout-experience#set-the-default-payment-method-and-shipping-information).[](https://knowledge.hubspot.com/payment-processing/configure-your-buyer-checkout-experience#set-the-default-payment-method-and-shipping-information)
`hs_invoice_payment_collection_method`| Enumeration| Set to `manual` if you want the invoice to have digital payment capability. Set to `none` if you don’t want digital payment capability. If no value is provided, this property will be set automatically based on the account [payment settings](https://knowledge.hubspot.com/payment-processing/configure-your-buyer-checkout-experience#set-the-default-payment-method-and-shipping-information).[](https://knowledge.hubspot.com/payment-processing/configure-your-buyer-checkout-experience#set-the-default-payment-method-and-shipping-information)
`hs_collect_address_types`| Boolean| The types of addresses that are collected while paying the invoice. Value can be `billing_address` and/or `shipping_address`.
`hs_recipient_shipping_address`| String| The shipping address of the recipient.
`hs_recipient_shipping_city`| String| The shipping city of the recipient.
`hs_recipient_shipping_state`| String| The shipping state or region of the recipient.
`hs_recipient_shipping_zip`| String| The shipping postal or zip code of the recipient.

###

​

Add taxes to an invoice

You can add taxes to an invoice in two different ways depending on your use case:

  * Add taxes to individual line items by setting the `hs_tax_rate_group_id` property when you create an invoice. You’ll first need to [set up tax rates](https://knowledge.hubspot.com/payments/create-and-use-discount-codes#add-a-tax-rate-to-the-tax-library) in your account before associating them with line items. You’ll need to authorize the `tax_rates.read` scope for your app to fetch tax rates and the `crm.objects.line_items.write` scope to update or create a line item.
  * Use the [tax object](/docs/api-reference/latest/crm/objects/taxes/guide) to add taxes to the entire invoice, applying taxes to the total amount of the invoice.


####

​

Add taxes to line items

To associate a tax rate with a line item of an invoice, first make a `GET` request to `/tax-rates/v1/tax-rates` to fetch all tax rates. The resulting response will resemble the following:


    {
      "results": [
        {
          "name": "state-sales-tax",
          "percentageRate": 1,
          "label": "State sales tax 2025",
          "active": true,
          "id": "15970230",
          "createdAt": "2025-02-25T21:57:20.703Z",
          "updatedAt": "2025-02-25T21:57:20.703Z"
        }
      ],
      "paging": {
        "next": {
          "after": "MTU5NzAyMzA%3D",
          "link": "https://api.hubspot.com/tax-rates/v1/tax-rates?after=MTU5NzAyMzA%3D"
        }
      }
    }


You can then use the `id` of one of your tax rates as the `hs_tax_rate_group_id` when creating or updating a line item. Learn more about setting up tax rates in the [line items API guide](/docs/api-reference/latest/crm/objects/line-items/guide#create-a-line-item).

####

​

Add taxes to the entire invoice order

Rather than apply an existing tax rate to individual line items, you can instead apply a tax to the [entire invoice order](https://knowledge.hubspot.com/products/edit-products-and-terms-in-the-line-items-editor#add-discounts-fees-and-taxes-to-an-invoice). An invoice-level tax has a 1:1 relationship with the invoice, meaning the tax must be unique to the invoice. However, an invoice can include multiple taxes. To add taxes to an entire invoice order:

  * [Create a tax](/docs/api-reference/latest/crm/objects/taxes/create-tax).
  * Create an invoice.
  * Use the [associations API to associate the invoice to the tax](/docs/api-reference/latest/crm/associations/associate-records/guide#invoice-to-object).


###

​

Move the invoice to the Open status

An invoice can be set to one of four statuses, as set by the `hs_invoice_status` property:

Status| Description
---|---
`draft`| The invoice is being edited and is not yet ready to be sent.
`open`| The invoice has all of the details needed to be sent to the buyer, and is payable.
`paid`| The buyer has paid the invoice.
`voided`| The invoice has been voided.

When creating an invoice, you may want to set its status to `draft` until it’s ready to be sent to the buyer. Once all of the required properties and associations are added to the invoice, you can update its status to `open`, meaning the invoice can be shared and is payable. To move the invoice to the `open` status, make a `PATCH` request to `/crm/objects/2026-03/invoices` and set the `hs_invoice_status` property to `open`.

**Please note:** To move an invoice to the _Open_ status (open invoice that is payable), one contact and at least one line item must be associated.


    {
      "properties": {
        "hs_invoice_status": "open"
      }
    }


##

​

Retrieve invoices

Depending on the information you need, there are a few ways to retrieve invoices:

  * To retrieve all invoices, make a `GET` request to `crm/objects/2026-03/invoices`.
  * To retrieve a specific invoice, make a `GET` request to the above URL and specify an invoice ID. For example: `crm/objects/2026-03/invoices/44446244097`.
  * To retrieve invoices that meet a specific set of criteria, you can make a `POST` request to the search endpoint and include filters in the request body. See an example of using the search endpoint below.

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


For reference, review the list of common properties below. To view all available invoice properties, make a `GET` request to `crm/properties/2026-03/invoices`. Learn more about using the [properties API](/docs/api-reference/latest/crm/properties/guide).

###

​

Search for invoices by properties

You can use the search [endpoint](/docs/api-reference/latest/crm/search-the-crm) to retrieve invoices that meet a specific set of [filter criteria](/docs/api-reference/latest/crm/search-the-crm#filter-search-results). This will be a `POST` request that includes your filter criteria in the request body. For example, to search for all open invoices, you would make a `POST` request to `crm/objects/2026-03/invoices/search` with the following request body:


    {
      "filterGroups": [
        {
          "filters": [
            {
              "propertyName": "hs_invoice_status",
              "value": "open",
              "operator": "EQ"
            }
          ]
        }
      ],
      "properties": ["hs_invoice_status", "hs_due_date"]
    }


Note that the `filters` array specifies the search criteria, while the `properties` array specifies which properties to return.

####

​

Retrieve associations

To retrieve association information for an invoice,make a `GET` request to the following URL: `crm/objects/2026-03/invoice/{`hs_object_id}`/associations/{associatedObjectName}` Associated objects can include [contacts](/docs/api-reference/latest/crm/objects/contacts/guide), [companies](/docs/api-reference/latest/crm/objects/companies/guide), [deals](/docs/api-reference/latest/crm/objects/deals/guide), [line items](/docs/api-reference/latest/crm/objects/line-items/guide), [discounts](/docs/api-reference/latest/crm/objects/discounts/guide), **[fees](/docs/api-reference/latest/crm/objects/fees/guide)** , and **[taxes](/docs/api-reference/latest/crm/objects/taxes/guide)**. For example, to retrieve an invoice and the line items associated with it, make a `GET` request to: `crm/objects/2026-03/invoice/{invoiceId}/associations/line_items` This will return the IDs of the currently associated line items, along with meta information about the association type.


    {
      "results": [
        {
          "id": "1526712436",
          "type": "invoice_to_line_item"
        },
        {
          "id": "1526712437",
          "type": "invoice_to_line_item"
        }
      ]
    }


You can then use the returned IDs to request more information about the line items through the [line items API](/docs/api-reference/latest/crm/objects/line-items/guide). For example, you could batch retrieve line items by ID by making a `POST` request to the following URL with the request body below: `crm/objects/2026-03/line_items/batch/read`


    {
      "inputs": [
        {
          "id": "1526712436"
        },
        {
          "id": "1526712437"
        }
      ],
      "properties": ["name", "amount"]
    }


The response would be formatted as follows:


    {
      "status": "COMPLETE",
      "results": [
        {
          "id": "1359205183",
          "properties": {
            "amount": "123.00",
            "createdate": "2023-04-26T14:52:35.885Z",
            "hs_lastmodifieddate": "2023-04-26T14:52:35.885Z",
            "hs_object_id": "1359205183",
            "name": "itemname"
          },
          "createdAt": "2023-04-26T14:52:35.885Z",
          "updatedAt": "2023-04-26T14:52:35.885Z",
          "archived": false
        }
      ],
      "startedAt": "2024-03-11T20:09:44.151Z",
      "completedAt": "2024-03-11T20:09:44.195Z"
    }


**Please note:** Line items belong to one single parent object. For example, if retrieving line items from an invoice, the line item IDs will be different to those on a deal, or a quote.

##

​

Delete invoices

You can delete invoices with a `hs_invoice_status` of `draft` and `open` (if [enabled in your account settings](https://knowledge.hubspot.com/invoices/set-up-the-hubspot-invoices-tool#turn-on-the-ability-to-delete-unpaid-invoices)).

  * To [delete one invoice](/docs/api-reference/latest/crm/objects/invoices/batch/delete-invoices) by ID, make a `DELETE` request to `/crm/objects/2026-03/invoices/{invoiceId}`.
  * To [delete a batch](/docs/api-reference/latest/crm/objects/invoices/batch/delete-invoices) of invoices by ID, make a `POST` request to `/crm/objects/2026-03/invoices/batch/archive` with the invoice IDs specified in the request body:


    {
      "inputs": [
        {
          "id": "1234567"
        },
        {
          "id": "8675309"
        }
      ]
    }


##

​

Reference

###

​

Common properties

Below is a list of properties commonly used. This is not an exhaustive list. To get a list of all available properties, make a `GET` request to `/crm/objects/2026-03/invoices`.

Parameter| Type| Description
---|---|---
`hs_currency`| String| Currency of the invoice.
`hs_invoice_date`| Datetime| Date of the invoice. Can be formatted as ISO 8601 or UNIX timestamp in milliseconds. If no value is provided, this property will be set automatically to the current datetime.
`hs_due_date`| Datetime| Due date of the invoice. Can be formatted as ISO 8601 or UNIX timestamp in milliseconds. If no value is provided, this property will be set automatically to the current datetime.
`hs_purchase_order_number`| String| Add an associated PO number.
`hs_comments`| String| Add comments to the invoice for the buyer to see.
`hs_tax_id`| String| The account tax ID listed on the invoice, which includes a tax ID type and a tax ID number (e.g., `US EIN 12-3456789`). If the account has a configured [default tax ID for invoices](https://knowledge.hubspot.com/invoices/set-up-the-hubspot-invoices-tool#customization), this property will be set automatically if not provided.
`hs_allowed_payment_methods`| Enumeration| The payment methods to be used. For example, `credit_or_debit_card`, `ach`.

  * [Accepted payment methods when using HubSpot payments](https://knowledge.hubspot.com/payment-processing/set-up-payments).
  * [Accepted payment methods when using Stripe as a payment processor](https://knowledge.hubspot.com/payment-processing/connect-your-stripe-account-as-a-payment-processor-in-hubspot#configure-currencies-and-payment-methods).

If no value is provided, this property will set automatically based on the account [payment settings](https://knowledge.hubspot.com/payment-processing/configure-your-buyer-checkout-experience#set-the-default-payment-method-and-shipping-information).[](https://knowledge.hubspot.com/payment-processing/configure-your-buyer-checkout-experience#set-the-default-payment-method-and-shipping-information)
`hs_invoice_payment_collection_method`| Enumeration| Set to `manual` if you want the invoice to have digital payment capability. Set to `none` if you don’t want digital payment capability. If no value is provided, this property will be set automatically based on the account [payment settings](https://knowledge.hubspot.com/payment-processing/configure-your-buyer-checkout-experience#set-the-default-payment-method-and-shipping-information).[](https://knowledge.hubspot.com/payment-processing/configure-your-buyer-checkout-experience#set-the-default-payment-method-and-shipping-information)
`hs_allow_partial_payments`| Boolean| Allow your customer to pay less than the balance due.
`hs_collect_address_types`| Boolean| The types of addresses that are collected while paying the invoice. Value can be `billing_address` and/or `shipping_address`.
`hs_recipient_shipping_address`| String| The shipping address of the recipient. This address is used as the billing address.
`hs_recipient_shipping_address2`| String| The second line of the shipping address of the recipient. This address is used as the billing address.
`hs_recipient_shipping_city`| String| The shipping city of the recipient.
`hs_recipient_shipping_state`| String| The shipping state or region of the recipient.
`hs_recipient_shipping_zip`| String| The shipping postal or zip code of the recipient. This postal or zip code is used as the billing postal or zip code.
`hs_recipient_shipping_country`| String| The shipping country of the recipient.
`hs_recipient_company_address`| String| The address of the recipient’s company.
`hs_recipient_company_address2`| String| The second line of the address of the recipient’s company.
`hs_recipient_company_city`| String| The city of the recipient’s company.
`hs_recipient_company_state`| String| The state or region of the recipient’s company.
`hs_recipient_company_zip`| String| The postal or zip code of the recipient’s company.
`hs_custom_fields`| Enumeration| The custom fields that have been added to the invoice. [Learn more about the configuration of this setting](https://knowledge.hubspot.com/invoices/set-up-the-hubspot-invoices-tool#add-or-remove-custom-fields).
`hs_invoice_link`| String| The URL of the invoice.
`hs_language`| String| Language of the invoice.


`hs_locale`| String| Locale of the invoice.
`hs_pdf_download_link`| String| PDF download link.
`hs_invoice_billable`| Boolean| Whether the invoice is billable or not.

###

​

Create a draft with associations (single request)

The following request body will create a new draft invoice with an association to a contact. `POST` `/crm/objects/2026-03/invoices/batch/create`


    {
      "inputs": [
        {
          "properties": {
            "hs_currency": "USD",
            "hs_invoice_date": "1729859279",
            "hs_due_date": "1732537679"
          },
          "associations": [
            {
              "to": {
                "id": "2171512734"
              },
              "types": [
                {
                  "associationCategory": "HUBSPOT_DEFINED",
                  "associationTypeId": 177
                }
              ]
            }
          ]
        }
      ]
    }


Parameter| Type| Description
---|---|---
`hs_currency`| String| Currency of the invoice.
`hs_invoice_date`| Datetime| Date of the invoice. Can be formatted as ISO 8601 or UNIX timestamp in milliseconds. If no value is provided, this property will be set automatically to the current datetime.
`hs_due_date`| Datetime| Due date of the invoice. Can be formatted as ISO 8601 or UNIX timestamp in milliseconds. If no value is provided, this property will be set automatically to the current datetime.
`associations`| Array| The invoice’s associated records. To set each association, include a separate object in the associations array with the following fields:

  * to: the ID of the record to associate with the invoice.
  * associationCategory: the [_type of association_](/docs/api-reference/latest/crm/associations/associate-records/guide#retrieve-association-types). Can be HUBSPOT_DEFINED or USER_DEFINED.
  * associationTypeId: the ID of the type of association being made:
    * 177: invoice to contact

[Learn more about association type IDs](/docs/api-reference/latest/crm/associations/associate-records/guide#association-type-id-values).

Last modified on March 31, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)