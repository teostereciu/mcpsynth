# HubSpot tracking code API

*Source: https://developers.hubspot.com/docs/api-reference/latest/account/settings/tracking-code/overview*

---

Tracking Code

# HubSpot tracking code API

The HubSpot tracking code allows you to identify visitors, track events, and track page views.

The details for events on this page are only for legacy custom events. For the new [custom events](https://knowledge.hubspot.com/analytics-tools/create-codeless-custom-behavioral-events), please see the [updated documentation](/docs/api-reference/latest/account/settings/tracking-code/overview).

In addition to tracking page views, the HubSpot tracking code allows you to identify visitors, track events, and manually track page views (without reloading the page). The Tracking Code API allows you to dynamically create events and track event data in HubSpot. Function calls are pushed into the `_hsq` array:


    var _hsq = (window._hsq = window._hsq || []);
    _hsq.push(["method", "arg1"]);


Anything already in the `_hsq` array is processed when the tracking code is loaded, so you can push an `identify` call to the array before the code loads to have the identity information pushed with the initial `trackPageView` call.

Note: `trackPageView` is automatically called when the tracking code loads, so you should not push any `trackPageView` calls to `_hsq` before the page loads.

##

​

How do identities work?

The HubSpot analytics tool identifies unique records using two pieces of data, the `usertoken` (stored in the visitors browser in the `hubspotutk` cookie) and the email address. When the HubSpot tracking code tracks an action (such as a page view) for a visitor, it automatically associates that action with the `usertoken`. When you use the Tracking Code API to identify a visitor by email address, the analytics system will tie that email to the `usertoken`, allowing HubSpot to update an existing contact record or create a new one. HubSpot will [validate the email address](https://developers.hubspot.com/docs/faq/how-does-hubspot-validate-email-addresses) used for any process that would create or update a contact record. Analytics data (page views, original source, etc.) associated with the `usertoken` will show up on the contact record. With this in mind, you should only use the `identify` method when you know the identity (i.e. the email address) of the person viewing the page. Using a placeholder email for unknown visitors will create a contact record with that placeholder email, and the visitor’s `usertoken` cookie will be associated with that record, meaning that all unknown visitors would be associated with that single placeholder contact. Keep in mind that the `identify` function only sets the identities in the tracker. The identities do not get passed to HubSpot until you make a separate `trackPageView` or `trackEvent` call. Please note that the HTTP API cannot be used to associate analytics data with a contact record, though you can still use the `email=` parameter in the URL to associate the event with the contact with that email address (or create a new contact if the email address does not belong to an existing record).

##

​

Tracking events

**Note** : Events will only be processed for accounts with **Marketing Hub Enterprise**.

The `trackEvent` function is used to track [behavioral events](https://knowledge.hubspot.com/reports/analyze-and-manage-your-events-with-the-events-analytics-tool) in your HubSpot reports. Events are used to track that some action occurred, and can be tied to a contact record so that you can see if/when a contact triggered that event. While you can set up simple events in HubSpot, you can use the Events API to track more complicated processes on your website or track events that occur offline.

##

​

Event IDs and names

Events can be triggered using a numerical ID or a string name. If you’re creating events in HubSpot (Reports > Analytics Tools > Behavioral Events), they’ll automatically be assigned a numerical ID, which will be used to trigger that specific event. You can get the ID out of the URL when viewing the event in HubSpot. See [this page](http://knowledge.hubspot.com/articles/KCS_Article/Reports/How-do-I-create-Events-in-HubSpot) for more details about creating events. You can also trigger an event using a string name for the event. If you use a name, and there is not an existing event that already has that name, a new event with that name will be dynamically created. If an event with that name was already dynamically, then the new event will count towards that existing one. This allows you to keep dynamically creating new events without doing manual work in HubSpot.

Notes:

  * Events created in the HubSpot app cannot be triggered by name, only by ID.
  * Events created dynamically by name can only be created **once**. If you delete an event that was created this way, a new event **will not be created** if you try to dynamically trigger an event with the same name.


##

​

Tracking in single-page applications

The HubSpot tracking code will automatically record a page view when the code is first loaded, but you can also manually track page views in a single-page application without reloading the tracking code. You can use the `setPath` and `trackPageView` functions to update and track the current page:


    <!-- Set up the path for the initial page view -->
    <script>
      var _hsq = window._hsq = window._hsq || [];
      _hsq.push(['setPath', '/home']);
    </script>

    <!-- Load the HubSpot tracking code -->
    <!-- Start of HubSpot Embed Code -->
      <script type="text/javascript" id="hs-script-loader" async defer src="//js.hs-scripts.com/{hubId}.js"></script>
    <!-- End of HubSpot Embed Code -->

    <!-- Tracking subsequent page views -->
    <script>
      var _hsq = window._hsq = window._hsq || [];
      _hsq.push(['setPath', '/about-us']);
      _hsq.push(['trackPageView']);
    </script>


##

​

Available Methods

The following methods are available in the Tracking Code API:

  * [`identify`](/docs/api-reference/latest/account/settings/tracking-code/identify) \- Identify a visitor by email
  * [`trackEvent`](/docs/api-reference/latest/account/settings/tracking-code/track-event) \- Track behavioral events
  * [`trackPageView`](/docs/api-reference/latest/account/settings/tracking-code/track-page-view) \- Track page views
  * [`setPath`](/docs/api-reference/latest/account/settings/tracking-code/set-path) \- Set path for single-page applications
  * [`addPrivacyConsentListener`](/docs/api-reference/latest/account/settings/tracking-code/add-privacy-consent-listener) \- Check consent status
  * [`revokeCookieConsent`](/docs/api-reference/latest/account/settings/tracking-code/revoke-cookie-consent) \- Remove consent cookies
  * [`doNotTrack`](/docs/api-reference/latest/account/settings/tracking-code/do-not-track) \- Prevent all tracking


Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)