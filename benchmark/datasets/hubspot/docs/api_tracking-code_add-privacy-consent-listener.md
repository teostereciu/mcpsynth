# Add privacy consent listener

*Source: https://developers.hubspot.com/docs/api-reference/latest/account/settings/tracking-code/add-privacy-consent-listener*

---

Tracking Code

# Add privacy consent listener

Check the consent status of the visitor when using the [consent banner](/docs/api-reference/latest/account/settings/consent-banner/consent-banner-api).

##

​

Usage


    var _hsq = (window._hsq = window._hsq || []);
    _hsq.push([
      "addPrivacyConsentListener",
      function (consent) {
        // Handle consent status
        if (consent.allowed) {
          console.log("Consent granted");
          // Enable additional tracking or analytics
        } else {
          console.log("Consent denied");
          // Disable additional tracking
        }
      },
    ]);


##

​

Parameters

The callback function receives a consent object with information about the visitor’s consent status:

  * `allowed` (boolean): Whether the visitor has granted consent
  * Additional properties may be available depending on the consent banner configuration


##

​

Use Cases

  * Conditionally enable third-party analytics based on consent
  * Show/hide certain features that require tracking
  * Customize user experience based on privacy preferences
  * Comply with GDPR and other privacy regulations


Last modified on April 10, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)