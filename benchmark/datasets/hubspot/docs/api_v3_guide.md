# Subscriptions preferences v3

*Source: https://developers.hubspot.com/docs/api-reference/legacy/communication-preferences/v3/guide*

---

v3

# Subscriptions preferences v3

The subscription preferences endpoints allow you to manage email subscriptions details for contacts in a HubSpot portal

Scope requirements

Subscriptions types represent the legal basis to communicate with your contacts through email. Contacts can [manage their email preferences](https://knowledge.hubspot.com/marketing-email/insert-subscription-links-into-marketing-emails) so that they’re only opted into the emails they want to receive.

**Please note:** The subscription preferences API does _not_ currently support retrieving or updating [WhatsApp](https://knowledge.hubspot.com/inbox/collect-consent-for-whatsapp-conversations) subscription information for a contact.

##

​

Get contact subscription status

The contact subscription status endpoint allows users to retrieve the subscription statuses for an email address in an account. This endpoint is ideal for when you have an external preferences center or integration and need to know the subscription statuses for any given email address in your account.

* * *

##

​

Subscribe contact

The subscribe contact endpoint allows you to subscribe an email address to any given subscription type in an account, but **will not allow you to resubscribe contacts who have opted out.**

**Please note:** The new version of the subscription preferences API, v4, does provide support for resubscribing contacts who previously opted out. Learn more about the v4 API in [this article](/docs/api-reference/legacy/communication-preferences/guide).

**Example use case:** This endpoint is ideal for when you have an integration or external form that needs to opt contacts into a subscription type. **Note** : The subscribe contact endpoint should only be used to honor requests from contacts who have given you permission to subscribe them. Please [review applicable laws and regulations](https://knowledge.hubspot.com/marketing-email/set-up-email-subscription-types) before subscribing a contact.

* * *

##

​

Unsubscribe contact

The unsubscribe contact endpoint allows you to unsubscribe an email address in an account from any given subscription type. **Example use case:** This endpoint is ideal for when you have an integration or external form that needs to opt contacts out of a subscription type.

* * *

##

​

Get subscription types

The subscription info endpoint allows users to retrieve all subscription types in their account. **Example use case:** This endpoint is ideal for when you have an external preferences center, integration, or form and need to know which subscription types exist in your account so you can update the subscription statuses for your contacts accordingly.

* * *

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)