# Consent banner API

*Source: https://developers.hubspot.com/docs/api-reference/latest/account/settings/consent-banner/consent-banner-api*

---

Consent banner

# Consent banner API

The consent banner enables you to enable/disable different analytics scripts based on user preferences.

Super admins and users with [permission to edit website settings](https://knowledge.hubspot.com/user-management/hubspot-user-permissions-guide#marketing) can customize visitor cookie tracking and consent banners to comply with EU cookie laws and the [General Data Protection Regulation (GDPR)](https://www.hubspot.com/data-privacy/gdpr). A cookie consent banner allows visitors to opt in or opt out of being tracked in your HubSpot account with cookies. Learn more about how to customize the cookie tracking settings and cookie consent banner on the [HubSpot Knowledge Base](https://knowledge.hubspot.com/privacy-and-consent/set-up-a-consent-banner-with-the-new-editor). In this article, learn how to programmatically manage the cookies added to a visitor’s browser through the cookie consent banner. This feature works for all HubSpot pages as well as any external pages with your [HubSpot tracking code](https://knowledge.hubspot.com/reports/install-the-hubspot-tracking-code) installed, which will expose an `_hsp` object on your website that you can use to call functions to control consent and cookie settings for visitors. You can also learn how to use a third-party cookie consent banner to distribute consent, disable the consent collection, and manage features within HubSpot.

##

​

Impact of rejected cookies on HubSpot analytics

If a visitor rejects non-essential cookies (e.g., tracking and analytics cookies), the HubSpot tracking code can still load and execute, but it won’t set cookies to store unique identifiers for tracking individual behavior across sessions. This will impact the following behavior in HubSpot reporting and attribution tools:

  * **Aggregated page views:** HubSpot will still register page views for analytics purposes in an aggregated and anonymized manner. The data in the [web traffic analytics tool](https://knowledge.hubspot.com/reports/analyze-your-site-traffic-with-the-traffic-analytics-tool) in HubSpot will still reflect page views and session counts, but won’t associate these visits with individual visitors or existing contacts in your CRM.
  * **Anonymized traffic:** a visitor’s session will be treated as anonymous, and personally identifiable data (e.g., IP addresses or behavior across sessions) will _not_ be tracked.


##

​

Remove cookies

`_hsp.push(['revokeCookieConsent']);` Remove the cookies created by the HubSpot tracking code that are included in the consent banner under GDPR, include the HubSpot cookies related to tracking the visitor. As a result of the cookies being removed, the visitor would see the [cookie consent banner](https://knowledge.hubspot.com/privacy-and-consent/customize-your-cookie-tracking-settings-and-consent-banner) on their next page load, as they would appear as a new visitor. This function _does not_ remove cookies placed by non-HubSpot banners. You can find the specific list of cookies that will be removed on [HubSpot’s Knowledge Base](https://knowledge.hubspot.com/privacy-and-consent/what-cookies-does-hubspot-set-in-a-visitor-s-browser#consent-banner-cookies). If cookie blocking is turned on, this function will revoke consent so any third-party cookies will not be updated or dropped during future visits to the website. The code block below provides an example of defining an event handler to remove cookies when the user clicks an element (like a button) with an `id` of `removeCookies`:


    /*
    Example code to remove the consent banner cookies
    when a visitor clicks an element with the 'removeCookies' id.
    */

    var _hsp = (window._hsp = window._hsp || []);
    document.getElementById("removeCookies").onclick = function () {
      _hsp.push(["revokeCookieConsent"]);
    };


##

​

Place do not track cookie

`_hsq.push(['doNotTrack']);` Places the `__hs_do_not_track` cookie in the visitors browser, which will prevent the HubSpot tracking code from sending any information for the visitor. You can remove the cookie by calling the function again and including the `{track: true}` argument: `_hsq.push(['doNotTrack', {track: true}]);`

This function prevents all information from being collected by the tracking code, including anonymized traffic and custom event data.

The code block below provides an example of defining an event handler to remove cookies when the user clicks an element (like a button) with an `id` of `removeCookies`:


    document.getElementById("doNotTrack").onclick = function () {
      _hsq.push(["doNotTrack"]);
    };


##

​

Get privacy consent status

`_hsp.push(['addPrivacyConsentListener', callbackFunction]);` Get the privacy consent status of the current visitor. There are 3 categories of consent that can be used to provide more granular control to the user. These each have their own keys within the `consent.categories` object:

  * `consent.categories.analytics`
  * `consent.categories.advertisement`
  * `consent.categories.functionality`

The provided `callbackFunction` will be called, depending on the state of the page:

  * If the banner is _not_ enabled, or if the visitor has previously seen the banner and clicked accept or decline:
    * the _callbackFunction_ will be called immediately if the banner code is already loaded.
    * the _callbackFunction_ will be called after the tracking code loads if the function is pushed to `_hsp` before the tracking code loads.
  * If the banner is enabled, the callback function will be called when the visitor clicks on the accept or decline button.

The code block below demonstrates how to log the various category consent statuses of the current visitor to the console.


    var _hsp = (window._hsp = window._hsp || []);

    // analytics
    _hsp.push([
      "addPrivacyConsentListener",
      function (consent) {
        console.log(consent.categories.analytics);
      },
    ]);

    // advertisement
    _hsp.push([
      "addPrivacyConsentListener",
      function (consent) {
        console.log(consent.categories.advertisement);
      },
    ]);

    // functionality
    _hsp.push([
      "addPrivacyConsentListener",
      function (consent) {
        console.log(consent.categories.functionality);
      },
    ]);

    // or it can all be done in one call
    _hsp.push([
      "addPrivacyConsentListener",
      function (consent) {
        console.log(`analytics: ${consent.categories.analytics}`);
        console.log(`advertisement: ${consent.categories.advertisement}`);
        console.log(`functionality: ${consent.categories.functionality}`);
      },
    ]);


##

​

Cookies not by category

This is provided for backward compatibility with older scripts. For all new websites you should use the cookies by category method, giving more granular control over cookie activation.

`_hsp.push(['addPrivacyConsentListener', callbackFunction]);` Allows you to get the _true_ or _false_ privacy consent status of the current visitor. The _callbackFunction_ will be called, depending on the state of the page:

  * If the banner is _not_ enabled, or if the visitor has previously seen the banner and clicked accept or decline:
    * the _callbackFunction_ will be called immediately if the banner code is already loaded.
    * the _callbackFunction_ will be called after the tracking code loads if the function is pushed to **hsp** before the tracking code loads.
  * If the banner is enabled, the callback function will be called when the visitor clicks on the accept or decline button.

The code block below demonstrates how to log the consent status of the current visitor to the console.


    var _hsp = (window._hsp = window._hsp || []);
    _hsp.push([
      "addPrivacyConsentListener",
      function (consent) {
        if (consent.allowed) {
          console.log("something");
        }
      },
    ]);


The `callbackFunction` accepts a `consent` object as its only argument. The `consent` object has a single `allowed` property that will be `true` if:

  * The [cookie consent banner](https://knowledge.hubspot.com/privacy-and-consent/customize-your-cookie-tracking-settings-and-consent-banner) is not enabled, or is enabled in notify-only mode.
  * The visitor clicks accept on the banner when opt-in mode is enabled.
  * The visitor has previously clicked accept on the banner when opt-in mode is enabled.

The property will be `false` if the consent banner is enabled in opt-in mode and the visitor clicks or has previously clicked the decline button.

##

​

​​Enable website visitors to manage their consent

Call the `showBanner` function to resurface the banner, enabling website visitors to make changes to their consent preferences. For example:


    ​​var _hsp = window._hsp = window._hsp || [];
    ​​_hsp.push(['showBanner']);


The behavior of`showBanner` varies by policy and is only available for _Opt-In_ and _Cookie-By-Category_ policies. For _Opt-in_ policies, calling `showBanner` will cause the banner to reappear, as shown in the video below: For Cookies-By-Category policies, calling `showBanner` will cause the modal for selecting each category to reappear, as shown in the video below:

##

​

UI Examples

This functionality can be made available to visitors in the form of buttons/links on your website that they can use to re-open the banner and edit their preferences. The following are examples with code.

###

​

Button

A button, often placed in the website footer.


    <button
      type="button"
      id="hs_show_banner_button"
      onClick="(function(){
            var _hsp = window._hsp = window._hsp || [];
            _hsp.push(['showBanner']);
          })()"
    >
      Cookie Settings
    </button>


    #hs_show_banner_button {
      display: inline-block;
      text-align: center;
      height: 50px;
      background-color: #425b76;
      border: 1px solid #425b76;
      border-radius: 3px;
      padding: 10px 16px;
      text-decoration: none;
      color: #fff;
      font-family: inherit;
      font-size: inherit;
      font-weight: normal;
      line-height: inherit;
      text-shadow: none;
    }


###

​

Fixed position button

A button with fixed positioning on the bottom of the screen. This kind of button has the advantage of being readily available and easy to find, while being somewhat obtrusive UX.


    <button
      id="hs-hud-cookie-settings"
      onClick="(function(){
          var _hsp = window._hsp = window._hsp || [];
          _hsp.push(['showBanner']);
        })()"
    >
      Cookie Settings
    </button>


    button#hs-hud-cookie-settings {
      position: fixed !important;
      bottom: 0px;
      right: 10px;
      color: white;
      background-color: #425b76;
      padding: 5px;
      border-top-right-radius: 5px;
      border-top-left-radius: 5px;
      border-width: 0;
      appearance: none;
    }


###

​

Link

A link or highlighted text.


    <a
      id="hs-cookie-settings-link"
      onClick="(function(){
          var _hsp = window._hsp = window._hsp || [];
          _hsp.push(['showBanner']);
        })()"
    >
      Cookie Settings
    </a>


    #hs-cookie-settings-link {
      cursor: pointer;
    }


##

​

Block third party cookies manually

The HubSpot Consent Banner supports manual handling of third party tracking technologies and cookies. It’s recommended to use manual handling if you have a complicated website and/or a dedicated web developer. If auto-blocking does not work for your site, manual blocking is also a good option. Manual blocking is implemented through the consent banner listener API, as described in the sections below. This API is used to prevent tracking technologies from running until they have consent.

###

​

General usage

If you want to install a tracking script onto your website to display targeted ads to visitors. You could use something like the below: `<script src=”https://my.advertisement.script.com/ads”></script>` When this script is pasted into the head HTML of a page on a website it would run anytime someone visits that page, regardless of their consent status. Visitors will have cookies placed on their browser without consent. To prevent the script from running without consent, you can use the privacy consent listener API to install the script when the visitor has consented to its cookies. Consent listeners are functions that run whenever the visitor submits their consent. To use this functionality, a consent listener needs to be created that adds the script to the page if the visitor has consented to advertisement cookies.


    <script>
     var _hsp = window._hsp = window._hsp || [];
    _hsp.push(['addPrivacyConsentListener', (consent) => {
    if (consent.categories.advertisement) {
    const script = document.createElement('script');
            	script.src = "https://my.advertisement.script.com/ads";
            	document.head.appendChild(script)
    }
    }])
    </script>


This script will register the consent listener with the banner. When consent to cookies is submitted, the consent listener will run, adding HubSpot’s third party ads script to the page.

###

​

Example: Google Tag

[Google Tag or gtag.js](https://developers.google.com/tag-platform/gtagjs) can be used to add Google Analytics. For example:


    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){window.dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'GA_TRACKING_ID');
    </script>


To load Google Analytics when analytics consent has been given, the gtag script needs to be added when consent is given:


    <!-- Google tag (gtag.js) -->
    <script>
         var _hsp = window._hsp = window._hsp || [];
        _hsp.push(['addPrivacyConsentListener', (consent) => {
        if (consent.categories.analytics) {
            const script = document.createElement('script');
              script.src = "https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID";
              script.async = 'true'
              document.head.appendChild(script)
          }
        }])
    </script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'GA_TRACKING_ID');
    </script>


###

​

Example: HotJar

[HotJar](https://help.hotjar.com/hc/en-us/articles/115009336727-How-to-Install-Your-Hotjar-Tracking-Code#manually) is another example of analytics tracking. For example:


    <!-- Hotjar Tracking Code -->
    <script>
        (function(h,o,t,j,a,r){
            h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
            h._hjSettings={hjid:HOT_JAR_ID,hjsv:6};
            a=o.getElementsByTagName('head')[0];
            r=o.createElement('script');r.async=1;
            r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
            a.appendChild(r);
        })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
    </script>


To ensure Hotjar runs when analytics consent is given, the consent listener can be added.


    <!-- Hotjar Tracking Code -->
    <script>
    var _hsp = window._hsp = window._hsp || [];
    _hsp.push(['addPrivacyConsentListener', (consent) => {
    	if (consent.categories.analytics){
    (function(h,o,t,j,a,r){
            		h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
            		h._hjSettings={hjid:HOT_JAR_ID,hjsv:6};
            		a=o.getElementsByTagName('head')[0];
            		r=o.createElement('script');r.async=1;
            		r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
            		a.appendChild(r);
        		})(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
    }

    }])
    </script>


##

​

Third-party cookie consent

In the section below, learn how to use a third party cookie consent banner to:

  * Distribute consent
  * Disable the consent collection
  * Manage features within HubSpot


###

​

Disable the HubSpot consent banner

To disable rendering of the HubSpot consent banner, include the code below in a script near the top of your page’s head html. This will also disable any consent management.

This flag must be set before the consent banner is loaded.


    window.disableHubSpotCookieBanner = true;


###

​

Set consent state of the HubSpot consent banner

Set the consent value for all HubSpot, third party, or custom products integrated with the HubSpot consent banner. This function takes an object specifying the consent state of the visitor, saves that value as the current consent state, and distributes that consent to all scripts with attached consent listeners. This value isn’t saved in consent cookies managed by the consent banner. Preserving consent state across sessions falls to the caller of this function. The function accepts a consent object with the following fields:

Field name| Type| Description
---|---|---
`analytics`| Boolean| Grants consent to use cookies to gather analytics data from the website visitor.
`advertisement`| Boolean| Grants consent to use cookies to help serve personalized ads to the visitor.
`functionality`| Boolean| Grants consent to use cookies for required functionality for your website to function (e.g., authentication).

The example code block below initializes all consent values to `true`.


    window._hsp = window._hsp || [];
    window._hsp.push([
      "setHubSpotConsent",
      {
        analytics: true,
        advertisement: true,
        functionality: true,
      },
    ]);


**Example: Using a third-party consent banner to control HubSpot cookies** The following code snippet and script provide an example of how to send a custom event whenever consent state changes. Note that the functionality that you want to implement for your specific use case may vary from the example code below. Consult any third-party documentation (e.g., Google’s introduction to user consent management) for more information on how to tailor behavior to your website’s needs.


    CustomEvent("thirdPartyConsentEvent", {
      detail: {
        analytics: true,
        advertisement: true,
        functionality: true,
      },
    });


The following script should be placed at the top of the head html of the page.


    <script>
      // disable the hubspot consent banner window.disableHubSpotCookieBanner = true // listen for the third party consent
      event and send consent to HubSpot window._hsp = window._hsp || []; document.addEventListener("thirdPartyConsentEvent",
      (e) =>{" "}
      {window._hsp.push([
        "setHubSpotConsent",
        {
          analytics: e.detail.analytics,
          advertisement: e.detail.advertisement,
          functionality: e.detail.functionality,
        },
      ])}
      )
    </script>;


Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)