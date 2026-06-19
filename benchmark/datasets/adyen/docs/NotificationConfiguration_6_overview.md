# NotificationConfiguration/6/overview

*Source: https://docs.adyen.com/api-explorer/NotificationConfiguration/6/overview*

---

# Notification Configuration API
This API is used for the classic integration. If you are just starting your implementation, refer to ournew integration guideinstead.
The Notification Configuration API provides endpoints for setting up and testing notifications that inform you of events on your platform, for example when a verification check or a payout has been completed.
For more information, refer to ourdocumentation.

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
The Notification Configuration API supportsversioningusing a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.
For example:

```
https://cal-test.adyen.com/cal/services/Notification/v6/createNotificationConfiguration
```

```
https://cal-test.adyen.com/cal/services/Notification/v6/createNotificationConfiguration
```