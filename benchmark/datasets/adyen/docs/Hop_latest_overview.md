# Hop/latest/overview

*Source: https://docs.adyen.com/api-explorer/Hop/latest/overview*

---

# Hosted onboarding API
This API is used for the classic integration. If you are just starting your implementation, refer to ournew integration guideinstead.
The Hosted onboarding API provides endpoints that you can use to generate links to Adyen-hosted pages, such as anonboarding pageor aPCI compliance questionnaire. You can provide these links to your account holders so that they can complete their onboarding.

## Authentication
Your Adyen contact will provide your API credential and an API key. To connect to the API, add anX-API-Keyheader with the API key as the value, for example:

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
Alternatively, you can use the username and password to connect to the API using basic authentication. For example:

```
curl
-U "ws@MarketPlace.YOUR_PLATFORM_ACCOUNT":"YOUR_WS_PASSWORD" \
-H "Content-Type: application/json" \
...
```

```
curl
-U "ws@MarketPlace.YOUR_PLATFORM_ACCOUNT":"YOUR_WS_PASSWORD" \
-H "Content-Type: application/json" \
...
```
When going live, you need to generate new web service user credentials to access thelive endpoints.

## Versioning
The Hosted onboarding API supportsversioningusing a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.
For example:

```
https://cal-test.adyen.com/cal/services/Hop/v6/getOnboardingUrl
```

```
https://cal-test.adyen.com/cal/services/Hop/v6/getOnboardingUrl
```