# Set the current page path

*Source: https://developers.hubspot.com/docs/api-reference/latest/account/settings/tracking-code/set-path*

---

Tracking Code

# Set the current page path

Set the path for tracking in single-page applications. Use before calling `trackPageView` to track the correct page.

##

​

Usage


    var _hsq = (window._hsq = window._hsq || []);
    _hsq.push(["setPath", "/about-us"]);


##

​

Single-Page Application Example


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

Notes

  * Essential for tracking page views in single-page applications
  * Always call `setPath` before `trackPageView` to ensure accurate tracking
  * The path should start with a forward slash (`/`)


Last modified on April 10, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)