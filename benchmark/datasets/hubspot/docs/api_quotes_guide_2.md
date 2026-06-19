# Create CPQ quotes

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/objects/quotes/guide*

---

Quotes

# Create CPQ quotes

CPQ quotes are built on an updated quotes system that uses the same API endpoints, but is more streamlined and built with AI in mind.

Supported products

Scope requirements

CPQ (Configure, Price, Quote) quotes represent HubSpot’s new AI-powered quoting system, offering enhanced functionality over legacy quotes. While CPQ quotes and [legacy quotes](/docs/api-reference/legacy/crm/objects/quotes/guide) use the same API endpoints, there are important differences in how you create and manage them. If you’ve set up either [HubSpot payments](https://knowledge.hubspot.com/payment-processing/set-up-payments) or [Stripe payment processing](https://knowledge.hubspot.com/payment-processing/connect-your-stripe-account-as-a-payment-processor-in-hubspot), you can configure a quote to be payable through this API. Learn more about [payable quotes](/docs/api-reference/latest/crm/objects/quotes/guide#enable-payments).

CPQ quotes can be built for accounts with a _**Commerce Hub**_ _Professional_ or _Enterprise_ subscription. Other accounts created before September 3rd, 2025 may have access to legacy quotes:

  * **Users in a Free account:** access to legacy quotes if one or more quotes were created in the 6 months prior to Sept. 3rd, 2025.
  * **Users in a _Sales Hub_ account:** continue to have access to legacy quotes after Sept. 3rd, 2025.

If the account has access to legacy quotes and you’re assigned a _**Commerce Hub**_ seat, you’ll no longer be able to create new legacy quotes via the UI, but you can still view and edit existing legacy quotes. To go back to the legacy experience, you’ll need to change your seat to a core or view-only seat.

##

​

Changes for CPQ quotes

Below is an overview of the changes for creating CPQ quotes versus legacy quotes. Properties:

  * When creating a CPQ quote, you must set `hs_template_type` to `CPQ_QUOTE` at the time of creation. This automatically sets the quote to use a CPQ template. Learn more about CPQ quote templates.
  * While many of the existing legacy quote properties are supported for configuring CPQ quotes, there’s a new set of CPQ-specific properties, which replaces some legacy properties.

Associations:

  * A CPQ quote must include line item, contact, and deal associations. For quotes that require signatures, you’ll also need to associate a signing contact.
  * Currently, one-time discounts, taxes, fees, and payment schedules are not supported for CPQ quotes. You can still set discounts and tax rates on individual line items.
  * If you want to associate a specific quote template with a quote, you can only do so at the time of creation. The quote template’s, properties, content, and associations will be added to the quote as supplemental information, with properties set on the quote overriding the quote template’s settings.

Learn more about quote associations. Quote states:

  * A CPQ quote created via the API will automatically be set to `DRAFT`. Other states such as `PENDING_APPROVAL`,`APPROVED`, and `REJECTED` are primarily managed via the UI and approval workflows.
  * The state will automatically be updated to `ACCEPTED` when the buyer accepts the quote.


If you’re a partner (a user that is assigned a Partner Seat) in an account that has both legacy and CPQ quotes:

  * When creating a quote in the UI, you can select either the legacy builder or CPQ builder.
  * You can manage both legacy and CPQ [approval workflows](https://knowledge.hubspot.com/quotes/set-up-quote-approvals) in the accounts _Approvals_ settings.


##

​

Create a CPQ quote

To create a quote, make a `POST` request to `/crm/objects/2026-03/quotes`. In the request body, you’ll specify the quote’s properties and associations with other CRM objects as needed. At a minimum, a CPQ quote must include the following properties:

  * `hs_title`
  * `hs_expiration_date`
  * `hs_template_type` (must be set to `CPQ_QUOTE`)


    {
      "properties": {
        "hs_title": "My CPQ quote",
        "hs_expiration_date": "2026-09-30",
        "hs_template_type": "CPQ_QUOTE"
      }
    }


Parameter| Type| Description
---|---|---
`hs_title`| String| The title of the quote.
`hs_expiration_date`| String| The date that the quote expires.
`hs_template_type`| Enumeration| Specifies the type of quote template to use. For CPQ quotes, use `CPQ_QUOTE`.

Within the `properties` object, you can include properties for configuring the acceptance method (e.g., e-signature) and enabling payments, as shown below.

###

​

Enable e-signatures

By default, a CPQ quote will be configured for manual printing and signing. Use the `hs_acceptance_method` property to customize the quote’s signature requirements.


    {
      "properties": {
        "hs_title": "My custom quote",
        "hs_expiration_date": "2026-09-30",
        "hs_template_type": "CPQ_QUOTE",
        "hs_acceptance_method": "clickwrap"
      }
    }


`hs_acceptance_method` can be set to one of the following:

  * `clickwrap`: renders a button on the quote to allow the buyer to accept by clicking (no signature).


  * `esignature`: renders a button on the quote that triggers an e-signature flow. This option requires at least one buyer contact to be associated with the quote as a signer. You can add one or more countersigners via the HubSpot UI to capture seller signatures.


  * `print_and_sign` (default): renders fields intended for printing and signing. This option requires at least one buyer contact to be associated with the quote as a signer. You can add one or more countersigners via the HubSpot UI to capture seller signatures.


**Please note:** A quote with e-sign enabled can’t be published if the account has exceeded its [monthly e-signature limit](https://knowledge.hubspot.com/quotes/use-e-signatures-with-quotes#monitor-e-signature-usage).

###

​

Enable payments

If you’ve set up [HubSpot payments](https://knowledge.hubspot.com/payment-processing/set-up-payments) or [Stripe payment processing](https://knowledge.hubspot.com/payment-processing/connect-your-stripe-account-as-a-payment-processor-in-hubspot), the quote will automatically be configured to be payable through your connected payment processor. Payment details are configured by a set of default properties, which you can update as needed.


    {
      "properties": {
        "hs_title": "Quote with CC payment",
        "hs_expiration_date": "2026-09-30",
        "hs_template_type": "CPQ_QUOTE",
        "hs_acceptance_method": "clickwrap",
        "hs_billing_enabled": true,
        "hs_payment_enabled": true,
        "hs_payment_type": "HUBSPOT",
        "hs_allowed_payment_methods":"CREDIT_OR_DEBIT_CARD",
        "hs_collect_billing_address": true
      }
    }


Parameter| Type| Description
---|---|---
`hs_payment_enabled`| Boolean| By default, this will be set to `true` with a connected payment processor, which enables the quote to collect payment using either HubSpot payments or Stripe payment processing.
`hs_billing_enabled`| Boolean| By default, this will be set to `true` with a connected payment processor, which enables HubSpot to automatically create invoices and subscriptions for the transaction. When set to `true`, `hs_payment_enabled` must also be `true`. This property is only available for CPQ quotes.
`hs_payment_type`| Enumeration| Determines which payment processor to use. Automatically set by HubSpot based on the account’s payment processor. Value can be either `HUBSPOT` or `BYO_STRIPE`.
`hs_payment_status`| Enumeration| The status of payment collection, if you’ve enabled payments. Upon publishing with payments enabled, this property will be set to `PENDING`. Once the buyer submits payment through the quote, the status will automatically update accordingly. Learn more about [enabling payments](/docs/api-reference/latest/crm/objects/quotes/guide#enable-payments).
`hs_allowed_payment_methods`| Enumeration| The payment methods to be used. By default, this will be set to the payment methods configured for the account. Can be one of: `ACH`, `CREDIT_OR_DEBIT_CARD`, `SEPA`, `BACS`, `PADS`.
`hs_collect_billing_address`| Boolean| When set to `true`, allows the buyer to enter their billing address during checkout.
`hs_collect_shipping_address`| Boolean| When set to `true`, allows the buyer to enter their shipping address during checkout.

##

​

Quote associations

In order for a CPQ quote to be published and shared externally, the quote must include line item, contact, and deal associations. For quotes that require signatures, you’ll also need to associate a signing contact. You can set these associations either when creating the quote or by updating it via the associations API. By default, setting a quote’s `hs_template_type` to `CPQ_QUOTE` will automatically create the quote using the default CPQ quote template. However, you can specify a different template at the time of creation if needed. The quote template’s properties, content, and associations will be added to the quote as supplemental information, with properties set on the quote overriding the quote template’s settings. Learn more about setting associations when creating a quote. Below are the associations available for CPQ quotes.

Object type| Type ID| Description
---|---|---
[Line items](/docs/api-reference/latest/crm/objects/line-items/guide) | `67`| The goods and/or services being sold through the quote. You can create line items from [products in your product library](/docs/api-reference/latest/crm/objects/products/guide) or create custom standalone line items. **Please note:** line items associated with a quote should be distinct from the line items associated with other objects, such as deals. Reusing line items across objects can lead to unexpected behavior.
[Deal](/docs/api-reference/latest/crm/objects/deals/guide) | `64`| The deal record for tracking revenue and sales lifecycle. A quote inherits values from the associated deal, including the owner and currency. Each quote can be associated with one deal.
[Contact](/docs/api-reference/latest/crm/objects/contacts/guide) | `69`| Specific buyers that you’re addressing in the quote.
[Contact (signer)](/docs/api-reference/latest/crm/objects/contacts/guide)| `702`| Specifies the contact whose signature is required on the quote. This association is required if the quote requires a signature.
[Company](/docs/api-reference/latest/crm/objects/companies/guide)| `71`| A specific company that you’re addressing in the quote. Each quote can be associated with one company.
Quote template| `286`| The template that renders the quote. This association can only be set at the time of creation. The quote template’s properties, content, and associations will be added to the quote as supplemental information, with properties set on the quote overriding the quote template’s settings.

###

​

Set associations when creating a quote

To set associations when creating a quote, include the `associations` array in the request body. For each CRM object you’re associating with the quote, you’ll include an object with association details, such as the ID of the CRM record and the ID of the association type. For example, the request body below would create a CPQ quote that’s associated with a contact, a deal, and a line item. A list of association type IDs for the available CRM object associations is provided in the table below the code sample.


    {
      "properties": {
        "hs_title": "My CPQ quote",
        "hs_expiration_date": "2026-09-30",
        "hs_template_type": "CPQ_QUOTE"
      },
      "associations": [
        {
          "to": {
            "id": 123456789
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 69
            }
          ]
        },
        {
          "to": {
            "id": 28973222148
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 64
            }
          ]
        },
        {
          "to": {
            "id": 24417508135
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 67
            }
          ]
        }
      ]
    }


###

​

Associating after creation

To configure associations for an existing quote, make a `POST` request to the following [associations API](/docs/api-reference/latest/crm/associations/associate-records/guide#associate-records) endpoint for each association: `/crm/objects/2026-03/quote/{quoteId}/associations/default/{toObjectType}/{toObjectId}`

Parameter| Description
---|---
`quoteId`| The ID of the quote.
`toObjectType`| The type of CRM object to associate with the quote (e.g., `contact`).
`toObjectId`| The ID of the CRM record to associate with.

For example, the following request would associate a quote that has an ID of `1234567` with a contact that has an ID of `8675309`: `/crm/objects/2026-03/quote/1234567/associations/default/contact/8675309`

**Please note:** you can only associate a quote template with a quote at the time of creation.

##

​

Quote templates

Templates for CPQ quotes can be [created and customized in the HubSpot UI](https://knowledge.hubspot.com/quotes/set-up-quotes#customize-quotes-with-branding-and-templates). When creating a CPQ quote via the API, you can specify a quote template to use by associating it with the quote at the time of creation. The quote template’s properties, content, and associations will be added to the quote as supplemental information, with properties set on the quote overriding the quote template’s settings. There are multiple ways to retrieve the ID of a CPQ quote template:

  * Retrieve via the quote template editor in HubSpot
  * Retrieve all quote templates via the API
  * Search for CPQ quote templates via the API


###

​

Retrieve an ID from the quote template editor

To find the ID of a quote template in HubSpot, navigate to the [quote template editor](https://knowledge.hubspot.com/quotes/customize-quotes-with-branding-and-templates?hubs_content=knowledge.hubspot.com/cpq/getting-started-with-hubspot-cpq&hubs_content-cta=create-and-edit-quote-templates#create-templates), then copy the second number in the URL (the number that is _not_ your HubID):

###

​

Retrieve all quote templates via the API

To retrieve all quote templates from an account, make a `GET` request to `/crm/objects/2026-03/quote_templates?properties=hs_type`.

The `properties=hs_type` query parameter adds the `hs_type` property of each template to the response. Templates compatible with CPQ quotes will have a `hs_type` property value of `cpq_template`.

**Example response:**


    {
      "results": [
        {
          "id": "46470285449",
          "properties": {
            "hs_createdate": "2023-06-12T16:26:34.968Z",
            "hs_lastmodifieddate": "2023-06-12T16:26:34.968Z",
            "hs_object_id": "46470285449",
            "hs_type": "cpq_template"
          },
          "createdAt": "2023-06-12T16:26:34.968Z",
          "updatedAt": "2023-06-12T16:26:34.968Z",
          "archived": false,
          "url": "https://app.hubspot.com/contacts/123456/record/0-64/46470285449"
        }
      ]
    }


###

​

Search for CPQ quote templates via the API

To retrieve only the quote templates that are compatible with CPQ quotes, make a `POST` request to `/crm/objects/2026-03/quote_templates/search`. In the request body, include a filter for the `hs_type` property with a value of `cpq_template`, as shown below.

  * Request body

  * Response


    {
      "filterGroups": [
        {
          "filters": [
            {
              "propertyName": "hs_type",
              "operator": "CONTAINS_TOKEN",
              "value": "cpq_template"
            }
          ]
        }
      ]
    }


    {
      "total": 1,
      "results": [
        {
          "id": "46470285449",
          "properties": {
            "hs_createdate": "2023-06-12T16:26:34.968Z",
            "hs_lastmodifieddate": "2023-06-12T16:26:34.968Z",
            "hs_object_id": "46470285449",
            "hs_type": "cpq_template"
          },
          "createdAt": "2023-06-12T16:26:34.968Z",
          "updatedAt": "2023-06-12T16:26:34.968Z",
          "archived": false,
          "url": "https://app.hubspot.com/contacts/123456/record/0-64/46470285449"
        }
      ]
    }


###

​

Editing template source code

Using the [quote template editor](https://knowledge.hubspot.com/quotes/customize-quotes-with-branding-and-templates#create-templates) in HubSpot, you can edit the source code of rich text template sections, such as the _Acceptance_ section. This gives you the ability to add custom code to the template.

**Please note:** using HubL in rich text areas is not recommended, as HubL code will not render or populate data until the quote is published. While editing the template or quote, the HubL output will not be visible.

To edit the source code of a quote template:

  * In your HubSpot account, click the **Settings** icon.
  * In the left sidebar menu, navigate to **Objects** > **Quotes**.
  * Click the **Quote templates** tab.
  * Click the **name** of the template that you want to edit.
  * In the editor, click into a rich text section, such as the _Cover letter_ , _Executive summary_ , or _Acceptance_ section. Then, in the top bar, click **Advanced** > **Source code**.


  * Add your custom code, then click **Save changes**.


##

​

Quote properties

Below is a list of available default quote properties, including properties that can only be used with CPQ quotes. To fetch all available quote properties from a given account, make a `GET` request to `crm/properties/2026-03/quotes`. Learn more about the [properties API](/docs/api-reference/latest/crm/properties/guide).

The following legacy quote properties are not supported in CPQ quotes:

  * `hs_esign_enabled` (replaced by `hs_acceptance_method`)
  * `hs_show_signature_box` (replaced by `hs_acceptance_method`)
  * `hs_proposal_*` (e.g., `hs_proposal_domain`)


###

​

CPQ properties

The properties below can be used exclusively with CPQ quotes.

Property| Type| Description
---|---|---
`hs_acceptance_method`| Enumeration| The acceptance method of the quote. Can be one of:

  * `clickwrap`: click to accept
  * `esignature`: enables e-sign
  * `print_and_sign`: for manual signatures


`hs_billing_enabled`| Boolean| Set to `true` to enable automatic invoice and subscription creation.
`hs_clickwrap_accepted_by`| String| The name or identifier of the individual who accepted the quote via clickwrap (i.e., without providing a handwritten or electronic signature).
`hs_collection_process`| Enumeration| Set to `AUTO_PAYMENTS` to charge invoices using the customer’s payment method automatically on each billing date.
`hs_contract_effective_start_date`| Date| Contract effective start date.
`hs_contract_effective_start_date_type`| Enumeration| How the effective start date of a contract is determined. Can be one of:

  * `ON_AGREEMENT`: the contract becomes effective on the date both parties agree, with signing being optional to indicate acceptance.
  * `CUSTOM`: allows for specifying a fixed custom start date for the contract.
  * `DELAYED_BY_DAYS`: the effective start date is delayed by a set number of days post-agreement.
  * `DELAYED_BY_MONTHS`: the effective start date is delayed by a set number of months post-agreement.


`hs_contract_effective_start_delayed_by_days`| Number| The number of days that the contract’s effective start date is delayed by.
`hs_contract_effective_start_delayed_by_months`| Number| The number of months that the contract’s effective start date is delayed by.
`hs_cover_letter`| String| The cover letter presented on the quote.
`hs_net_payment_terms`| Number| The period in days in which a buyer must make a full payment.

###

​

Properties set by quote state

Updating the quote’s state will update the following properties:

Property| Type| Description
---|---|---
`hs_quote_amount`| Number| The total amount due for the quote. This can be either total contract value or the amount due at checkout depending on the account’s [default quote value setting](https://knowledge.hubspot.com/quotes/set-up-quotes#set-the-default-quote-value).
`hs_domain`| String| Domain this quote should be served from. By default, this will be set to the domain that’s configured as the primary quotes domain. Learn more about [setting up quotes](https://knowledge.hubspot.com/quotes/set-up-quotes#configure-general-quote-settings).
`hs_slug`| String| The URL path that the quote will be served from.
`hs_quote_total_preference`| Enumeration| The line item property that will be used to calculate `hs_quote_amount`.
`hs_timezone`| String| The time zone for displaying dates on the quote.
`hs_locale`| String| The locale for displaying this quote publicly.
`hs_quote_number`| String| Reference number shown on quote document.
`hs_language`| String| The language for displaying this quote publicly.
`hs_currency`| String| Currency code for the quote.

Additionally, the properties below will be calculated when the quote is published.

Property| Type| Description
---|---|---
`hs_pdf_download_link`| String| Populated with a URL of a PDF for the quote.
`hs_locked`| Boolean| Set to `true`. To modify any properties after you’ve published a quote, you must first update the `hs_status` of the quote back to `DRAFT`, `PENDING_APPROVAL`, or `REJECTED`.
`hs_quote_link`| String| The quote’s publicly accessible URL. This is a read-only property and cannot be set through the API after publishing.
`hs_esign_num_signers_required`| Number| If you’ve enabled e-signatures, displays the number of signatures required.
`hs_payment_status`| Enumeration| The status of payment collection, if you’ve enabled payments. Upon publishing with payments enabled, this property will be set to `PENDING`. Once the buyer submits payment through the quote, the status will automatically update accordingly. Learn more about [enabling payments](/docs/api-reference/latest/crm/objects/quotes/guide#enable-payments).

Last modified on March 31, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)