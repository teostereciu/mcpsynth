# Fund/6/overview

*Source: https://docs.adyen.com/api-explorer/Fund/6/overview*

---

# Fund API
This API is used for the classic integration. If you are just starting your implementation, refer to ournew integration guideinstead.
The Fund API provides endpoints for managing the funds in the accounts on your platform. These management operations include, for example, the transfer of funds from one account to another, the payout of funds to an account holder, and the retrieval of balances in an account.
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
The Fund API supportsversioningusing a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.
For example:

```
https://cal-test.adyen.com/cal/services/Fund/v6/accountHolderBalance
```

```
https://cal-test.adyen.com/cal/services/Fund/v6/accountHolderBalance
```