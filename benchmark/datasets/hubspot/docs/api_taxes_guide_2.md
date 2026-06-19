# CRM API | Taxes

*Source: https://developers.hubspot.com/docs/api-reference/latest/crm/objects/taxes/guide*

---

Taxes

# CRM API | Taxes

Learn how to create and associate a tax as part of the pricing details of a quote.

Scope requirements

When you’re [creating a quote in HubSpot](/docs/api-reference/latest/crm/objects/quotes/guide), you can create and associate a tax as part of the pricing details of the quote.

**Please note:** The functionality described in this article pertains to the order-level tax object you can create and apply to [invoices](/docs/api-reference/latest/crm/objects/invoices/guide) and [subscriptions](/docs/api-reference/latest/crm/objects/commerce-subscriptions/guide). This object is distinct from the tax rate object that applies separately to line items only. Learn more about tax rates in the [line items API guide](/docs/api-reference/latest/crm/objects/line-items/guide#retrieve-tax-rates).

##

​

Create a tax

Taxes are used in conjunction with [discounts](/docs/api-reference/latest/crm/objects/discounts/guide) and [fees](/docs/api-reference/latest/crm/objects/fees/guide) when determining the pricing details for a quote. Any discounts you associate with your quote will be applied first, followed by associated fees, and then any associated taxes will apply.


    {
      "properties": {
        "hs_label": "A percentage-based tax of 6.5%",
        "hs_type": "PERCENT",
        "hs_value": "6.5"
      }
    }


After you create a tax, you can use its ID to associate it with a quote. To retrieve a list of taxes you’ve created, you can make a `GET` request to `/crm/objects/2026-03/tax`.

Last modified on March 31, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)