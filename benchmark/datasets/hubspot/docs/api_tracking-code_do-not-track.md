# Enable do not track

*Source: https://developers.hubspot.com/docs/api-reference/latest/account/settings/tracking-code/do-not-track*

---

Tracking Code

# Enable do not track

Prevent tracking by placing a cookie in the visitor’s browser.

Prevent all tracking by the HubSpot tracking code by placing a do not track cookie in the visitor’s browser.

##

​

Usage


    var _hsq = (window._hsq = window._hsq || []);
    _hsq.push(["doNotTrack"]);


##

​

What this does

  * Places a “do not track” cookie in the visitor’s browser
  * Prevents the HubSpot tracking code from collecting any analytics data
  * Stops page view tracking, event tracking, and visitor identification
  * Honors the visitor’s privacy preferences


##

​

Use Cases

  * **Privacy Compliance** : Respect visitor’s do-not-track preferences
  * **Opt-out Mechanism** : Provide a way for visitors to disable tracking
  * **Employee Exclusion** : Prevent internal traffic from being tracked
  * **Testing Environment** : Disable tracking during development/testing


##

​

Notes

  * This is a permanent setting until the cookie is manually removed
  * The cookie persists across browser sessions
  * This affects all HubSpot tracking functionality
  * To re-enable tracking, the visitor would need to clear their cookies or you would need to provide a mechanism to remove the do-not-track cookie


Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)