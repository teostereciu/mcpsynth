# Management/3/overview

*Source: https://docs.adyen.com/api-explorer/Management/3/overview*

---

# Management API
Configure and manage your Adyen company and merchant accounts, stores, and payment terminals.

## Authentication
Each request to the Management API must be signed with an API key.Generate your API keyin the Customer Area and then set this key to theX-API-Keyheader value.
To access the live endpoints, you need to generate a new API key in your live Customer Area.

## Versioning
Management API handles versioning as part of the endpoint URL. For example, to send a request to this version of the/companies/{companyId}/webhooksendpoint, use:

```
https://management-test.adyen.com/v3/companies/{companyId}/webhooks
```

```
https://management-test.adyen.com/v3/companies/{companyId}/webhooks
```

## Going live
To access the live endpoints, you need an API key from your live Customer Area. Use this API key to make requests to:

```
https://management-live.adyen.com/v3
```

```
https://management-live.adyen.com/v3
```

## Release notes
Have a look at therelease notesto find out what changed in this version!