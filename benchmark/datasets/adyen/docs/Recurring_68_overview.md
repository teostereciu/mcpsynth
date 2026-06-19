# Recurring/68/overview

*Source: https://docs.adyen.com/api-explorer/Recurring/68/overview*

---

# Adyen Recurring API
The Recurring API is a legacy API for managing tokens. We strongly recommend to useCheckout API recurring endpointsinstead when possible.
The Recurring API allows you to manage and remove your tokens or stored payment details. Tokens should be created with validation during a payment request.
For more information, refer to ourTokenization documentation.

## Authentication
You need anAPI credentialto authenticate to the API.
If using an API key, add anX-API-Keyheader with the API key as the value, for example:

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
Alternatively, you can use the username and password to connect to the API using basic authentication, for example:

```
curl
-U "ws@Company.YOUR_COMPANY_ACCOUNT":"YOUR_BASIC_AUTHENTICATION_PASSWORD" \
-H "Content-Type: application/json" \
...
```

```
curl
-U "ws@Company.YOUR_COMPANY_ACCOUNT":"YOUR_BASIC_AUTHENTICATION_PASSWORD" \
-H "Content-Type: application/json" \
...
```

## Versioning
Recurring API supportsversioningusing a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.
For example:

```
https://paltokenization-test.adyen.com/paltokenization/servlet/Recurring/v68/disable
```

```
https://paltokenization-test.adyen.com/paltokenization/servlet/Recurring/v68/disable
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
Recurring API is available through a Postman collection. Click the button below to create a fork, then set the environment variables atEnvironments>Adyen APIs.

## Going live
To authenticate to the live endpoints, you need anAPI credentialfrom your live Customer Area.
The live endpoint URLs contain a prefix which is unique to your company account:

```
https://{PREFIX}-paltokenization-live.adyenpayments.com/paltokenization/servlet/Recurring/v68/disable
```

```
https://{PREFIX}-paltokenization-live.adyenpayments.com/paltokenization/servlet/Recurring/v68/disable
```
Get your{PREFIX}from your live Customer Area underDevelopers>API URLs>Prefix.