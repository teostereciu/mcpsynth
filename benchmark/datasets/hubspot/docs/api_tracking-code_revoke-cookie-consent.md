# Revoke cookie consent

*Source: https://developers.hubspot.com/docs/api-reference/latest/account/settings/tracking-code/revoke-cookie-consent*

---

Tracking Code

# Revoke cookie consent

Remove the consent banner cookies for a visitor, such as for GDPR deletion requests.

##

​

Usage


    var _hsq = (window._hsq = window._hsq || []);
    _hsq.push(["revokeCookieConsent"]);


##

​

Use Cases

  * **GDPR Compliance** : Handle “right to be forgotten” requests
  * **Privacy Settings** : Allow users to revoke their consent
  * **Data Deletion** : Remove tracking consent as part of account deletion
  * **Privacy Reset** : Clear consent status for testing or troubleshooting


##

​

Notes

  * This function removes the consent banner cookies from the visitor’s browser
  * The visitor will see the consent banner again on their next visit
  * This does not delete historical data from HubSpot - it only affects future tracking
  * Use this in conjunction with other data deletion processes for complete GDPR compliance


Last modified on April 10, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)