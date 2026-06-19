# Payment/68/overview

*Source: https://docs.adyen.com/api-explorer/Payment/68/overview*

---

# Adyen Payment API
A set of API endpoints that allow you to initiate, settle, and modify payments on the Adyen payments platform. You can use the API to accept card payments (including One-Click and 3D Secure), bank transfers, ewallets, and many other payment methods.
To learn more about the API, visitClassic integration.

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
Payments API supportsversioningusing a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.
For example:

```
https://pal-test.adyen.com/pal/servlet/Payment/v68/authorise
```

```
https://pal-test.adyen.com/pal/servlet/Payment/v68/authorise
```

## Going live
To authenticate to the live endpoints, you need anAPI credentialfrom your live Customer Area.
The live endpoint URLs contain a prefix which is unique to your company account:

```
https://{PREFIX}-pal-live.adyenpayments.com/pal/servlet/Payment/v68/authorise
```

```
https://{PREFIX}-pal-live.adyenpayments.com/pal/servlet/Payment/v68/authorise
```
Get your{PREFIX}from your live Customer Area underDevelopers>API URLs>Prefix.