# Brands API

*Source: https://developers.hubspot.com/docs/api-reference/legacy/account/brands/guide*

---

Brands

# Brands API

HubSpot’s brands API endpoint provides information about brands tied to a user.

Scope requirements

The following endpoint provides information about [brands](https://knowledge.hubspot.com/branding/manage-your-brands-with-hubspot-brands) tied to a user. This may also include information about [logos](https://knowledge.hubspot.com/branding/edit-your-logo-favicon-and-brand-colors).

**Please note:** The API described in this article references business units, which is the former name for [brands](https://knowledge.hubspot.com/branding/manage-your-brands-with-hubspot-brands). This change does _not_ impact this API. When making requests to the endpoint listed below, the URL path should still include `/business-units/v3/business-units/`, as the endpoint path itself has not changed.

This API currently only supports retrieving brand data and does _not_ support associating assets with a brand, nor creating a new brand.

##

​

Get brands tied to a user

To get the brands that a user has access to, you can make a `GET` request to `/business-units/v3/business-units/user/{userId}` The following is an example of what the response body would include:


    {
      "logoMetadata": {
        "logoAltText": "logo sample text",
        "resizedUrl": "sillystring",
        "logoUrl": "examplelogourl.com"
      },
      "name": "sample business unit name",
      "id": "101"
    }


For more information on how to use the brands API, check out the [reference documentation](/docs/api-reference/legacy/account/brands/get-brands).

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)