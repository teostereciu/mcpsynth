# transfers-api/4/overview

*Source: https://docs.adyen.com/api-explorer/transfers-api/4/overview*

---

# Raise disputes API
Disputes API for Issuing that you can use to raise disputes on transactions made with an Adyen-issued card, or to report instances of fraud. You can also add attachments as supporting information for a raised dispute, update information about the dispute, submit the dispute for a chargeback, or close the dispute.

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
-H "Content-Type: application/json" \
-U "ws@BalancePlatform.YOUR_BALANCE_PLATFORM":"YOUR_WS_PASSWORD" \
...
```

```
curl
-H "Content-Type: application/json" \
-U "ws@BalancePlatform.YOUR_BALANCE_PLATFORM":"YOUR_WS_PASSWORD" \
...
```

## Roles and permissions
To use the Disputes API, you need an additional role for your API credential. Your Adyen contact will set up the roles and permissions for you.

## Versioning
The Disputes API supportsversioningusing a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.
For example:

```
https://balanceplatform-api-test.adyen.com/btl/api/v{version}/disputes
```

```
https://balanceplatform-api-test.adyen.com/btl/api/v{version}/disputes
```

## Going live
When going live, your Adyen contact will provide your API credential for the live environment. You can then use the username and password to send requests tohttps://balanceplatform-api-live.adyen.com/btl/api/v{version}.