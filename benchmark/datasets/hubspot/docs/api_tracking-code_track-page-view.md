# Track a page view

*Source: https://developers.hubspot.com/docs/api-reference/latest/account/settings/tracking-code/track-page-view*

---

Tracking Code

# Track a page view

Manually track a page view. This is automatically called when the tracking code loads, but can be used for single-page applications.

`trackPageView` is automatically called when the tracking code loads, so you should not push any `trackPageView` calls to `_hsq` before the page loads.

##

​

Usage

###

​

Basic Page View


    var _hsq = (window._hsq = window._hsq || []);
    _hsq.push(["trackPageView"]);


###

​

For Single-Page Applications


    var _hsq = (window._hsq = window._hsq || []);
    // First set the path
    _hsq.push(["setPath", "/about-us"]);
    // Then track the page view
    _hsq.push(["trackPageView"]);


##

​

Notes

  * Use this method when you need to track page views without reloading the page
  * Commonly used in single-page applications (SPAs)
  * Use with `setPath` to track the correct page path in SPAs


Last modified on April 10, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)