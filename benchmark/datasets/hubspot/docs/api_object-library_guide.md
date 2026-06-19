# Object library

*Source: https://developers.hubspot.com/docs/api-reference/legacy/crm/objects/object-library/guide*

---

Object Library

# Object library

Learn how to check whether or not objects in the object library are activated for use in a HubSpot account.

Scope requirements

As objects are added to the [object library](https://knowledge.hubspot.com/data-management/data-model-templates) in HubSpot, you can use the object library enablement endpoints to check whether or not an object is activated for use in a HubSpot account. The endpoints can check the status of an object, but you can only [activate or deactivate an object from within HubSpot](https://knowledge.hubspot.com/data-management/data-model-templates#view-the-object-library). If an object is enabled, an app will need the corresponding object [scopes](/docs/apps/legacy-apps/authentication/oauth-quickstart-guide#list-of-available-scopes) to access and manage records for the object. Learn more about creating and managing records [using the object APIs](/docs/guides/crm/understanding-the-crm).

##

​

Retrieve enablement statuses of all objects in the object library

To check if all objects in the object library are activated in the account, make a `GET` request to `crm/v3/object-library/enablement`. Only objects which can be [activated or deactivated](https://knowledge.hubspot.com/data-management/data-model-templates#view-the-object-library) will be returned (i.e. contacts, companies, deals, and tickets will not be included). In your response, the `enablementByObjectTypeId` object will be returned with `objectTypeId` values and a value of `true` or `false` for each. If the value is `true`, the object is activated for use in the account. If the value is `false`, the object is deactivated. You can view each object’s `objectTypeId` value in [the table in this article](/docs/api-reference/legacy/crm/property-validations/guide#object-type-ids). For example, the following response shows an account where appointments and services are activated, but courses and listings are not.


    //Example response
    GET crm/v3/object-library/enablement
    {
      "enablementByObjectTypeId": {
        "0-420": false,
        "0-421": true,
        "0-162": true,
        "0-410": false
      }
    }


##

​

Retrieve an object’s enablement status

To check if a specific object is activated, make a `GET` request to `crm/v3/object-library/enablement/{objectTypeId}`. Refer to [the table in this article](/docs/api-reference/legacy/crm/property-validations/guide#object-type-ids) to find an object’s `objectTypeId`. The object’s `enablement` value will be returned as `true` or `false`. If the value is `true`, the object is activated for use in the account. If the value is `false`, the object is deactivated. For example, to check if appointments are activated in an account, make a `GET` request to `crm/v3/object-library/enablement/0-421`. If appointments are activated, the response will look like:


    //Example response
    GET crm/v3/object-library/enablement/0-421
    {
      "enablement": true
    }


Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)