# Checkout/71/overview

*Source: https://docs.adyen.com/api-explorer/Checkout/71/overview*

---

# Adyen Checkout API
Adyen Checkout API provides a simple and flexible way to initiate and authorise online payments. You can use the same integration for payments made with cards (including 3D Secure), mobile wallets, and local payment methods (for example, iDEAL and Sofort).
This API reference provides information on available endpoints and how to interact with them. To learn more about the API, visitonline payments documentation.

## Authentication
Each request to Checkout API must be signed with an API key. For this,get your API keyfrom your Customer Area, and set this key to theX-API-Keyheader value, for example:

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...
```

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...
```

## Versioning
Checkout API supportsversioningusing a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.
For example:

```
https://checkout-test.adyen.com/v71/payments
```

```
https://checkout-test.adyen.com/v71/payments
```

## Server-side API libraries
We provide open-sourceserver-side API librariesin several languages:
- PHP
- Java
- Node.js
- .NET
- Go
- Python
- Ruby
- Apex (beta)
See ourintegration examplesfor example uses of the libraries.

## Developer resources
Checkout API is available through a Postman collection. Click the button below to create a fork, then set the environment variables atEnvironments>Adyen APIs.

## Going live
To access the live endpoints, you need an API key from your live Customer Area.
The live endpoint URLs contain a prefix which is unique to your company account, for example:

```
https://{PREFIX}-checkout-live.adyenpayments.com/checkout/v71/payments
```

```
https://{PREFIX}-checkout-live.adyenpayments.com/checkout/v71/payments
```
Get your{PREFIX}from your live Customer Area underDevelopers>API URLs>Prefix.
When preparing to do live transactions with Checkout API, follow thego-live checklistto make sure you've got all the required configuration in place.

## Release notes
Have a look at therelease notesto find out what changed in this version!