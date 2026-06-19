# Payout/latest/overview

*Source: https://docs.adyen.com/api-explorer/Payout/latest/overview*

---

# Adyen Payout API
ThePayout API is deprecatedand no longer supports new integrations. Do one of the following:
- If you are building a new integration, use theTransfers APIinstead.
- If you are already using the Payout API, reach out to your Adyen contact to learn how to migrate to the Transfers API.
With the Transfers API, you can:
- Handle multiple payout use cases with a single API.
- Use new payout functionalities, such as instant payouts to bank accounts.
- Receive webhooks with more details and defined transfer states.
For more information about the payout features of the Transfers API, see ourPayoutsdocumentation.
A set of API endpoints that allow you to store payout details, confirm, or decline a payout.
For more information, refer toOnline payouts.

## Authentication
To use the Payout API, you need to havetwo API credentials: one for storing payout details and submitting payouts, and another one for confirming or declining payouts. If you don't have the required API credentials, contact ourSupport Team.
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
Alternatively, you can use the username and password to connect to the API usingbasic authentication.
The following example shows how to authenticate your request with basic authentication when submitting a payout:

```
curl
-U "storePayout@Company.YOUR_COMPANY_ACCOUNT":"YOUR_BASIC_AUTHENTICATION_PASSWORD" \
-H "Content-Type: application/json" \
...
```

```
curl
-U "storePayout@Company.YOUR_COMPANY_ACCOUNT":"YOUR_BASIC_AUTHENTICATION_PASSWORD" \
-H "Content-Type: application/json" \
...
```

## Versioning
Payments API supportsversioningusing a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.
For example:

```
https://pal-test.adyen.com/pal/servlet/Payout/v68/payout
```

```
https://pal-test.adyen.com/pal/servlet/Payout/v68/payout
```

## Going live
To authenticate to the live endpoints, you needAPI credentialsfrom your live Customer Area.
The live endpoint URLs contain a prefix which is unique to your company account:

```
https://{PREFIX}-pal-live.adyenpayments.com/pal/servlet/Payout/v68/payout
```

```
https://{PREFIX}-pal-live.adyenpayments.com/pal/servlet/Payout/v68/payout
```
Get your{PREFIX}from your live Customer Area underDevelopers>API URLs>Prefix.