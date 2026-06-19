# Identify a visitor

*Source: https://developers.hubspot.com/docs/api-reference/latest/account/settings/tracking-code/identify*

---

Tracking Code

# Identify a visitor

Identify a visitor by email address. This ties the visitor’s usertoken to their email address, allowing HubSpot to update an existing contact record or create a new one.

You should only use the `identify` method when you know the identity (i.e. the email address) of the person viewing the page. Using a placeholder email for unknown visitors will create a contact record with that placeholder email.

##

​

Usage


    var _hsq = (window._hsq = window._hsq || []);
    _hsq.push([
      "identify",
      {
        email: "visitor@example.com",
        firstname: "John",
        lastname: "Doe",
      },
    ]);


##

​

Notes

  * The `identify` function only sets the identities in the tracker
  * The identities do not get passed to HubSpot until you make a separate `trackPageView` or `trackEvent` call
  * HubSpot will validate the email address used for any process that would create or update a contact record


Last modified on April 10, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)