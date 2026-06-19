# Track a behavioral event

*Source: https://developers.hubspot.com/docs/api-reference/latest/account/settings/tracking-code/track-event*

---

Tracking Code

# Track a behavioral event

Track behavioral events in your HubSpot reports. Events can be tied to a contact record so that you can see if/when a contact triggered that event.

**Note** : Events will only be processed for accounts with **Marketing Hub Enterprise**.

##

​

Usage

###

​

Track by Event ID


    var _hsq = (window._hsq = window._hsq || []);
    _hsq.push([
      "trackEvent",
      {
        id: "000000001625",
        value: 100,
      },
    ]);


###

​

Track by Event Name


    var _hsq = (window._hsq = window._hsq || []);
    _hsq.push([
      "trackEvent",
      {
        id: "custom_event_name",
        property1: "value1",
        property2: "value2",
      },
    ]);


##

​

Event IDs vs Names

  * **Event ID** : Use numerical IDs for events created in HubSpot (Reports > Analytics Tools > Behavioral Events)
  * **Event Name** : Use string names to dynamically create new events. If an event with that name doesn’t exist, it will be created automatically


  * Events created in the HubSpot app cannot be triggered by name, only by ID
  * Events created dynamically by name can only be created **once**. If you delete an event that was created this way, a new event **will not be created** if you try to dynamically trigger an event with the same name


Last modified on April 10, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)