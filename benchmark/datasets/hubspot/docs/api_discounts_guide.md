# CRM API | Discounts

*Source: https://developers.hubspot.com/docs/api-reference/legacy/crm/objects/discounts/guide*

---

Discounts

# CRM API | Discounts

Learn how to create and associate a discount as part of the pricing details of a quote.

Scope requirements

When you’re [creating a quote in HubSpot](/docs/api-reference/legacy/crm/objects/quotes/guide), you can create and associate a discount as part of the pricing details of the quote.

##

​

Create a discount

Discounts are used in conjunction with [fees](/docs/api-reference/legacy/crm/objects/fees/guide) and [taxes](/docs/api-reference/legacy/crm/objects/taxes/guide) when determining the pricing details for a quote. Any discounts you associate with your quote will be applied first, followed by associated fees, and then any associated taxes will apply.


    {
      "properties": {
        "hs_label": "A fixed, one-time discount",
        "hs_duration": "ONCE",
        "hs_type": "PERCENT",
        "hs_value": "50",
        "hs_sort_order": "2"
      }
    }


After you create a discount, you can use its ID to associate it with a quote. To retrieve a list of discounts you’ve created, you can make a `GET` request to `/crm/v3/objects/discount`.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)