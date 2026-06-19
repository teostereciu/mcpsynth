# Disputes/30/overview

*Source: https://docs.adyen.com/api-explorer/Disputes/30/overview*

---

# Disputes API
You can use theDisputes APIto automate the dispute handling process so that you can respond to disputes and chargebacks as soon as they are initiated. The Disputes API lets you retrieve defense reasons, supply and delete defense documents, and accept or defend disputes.

## Authentication
Each request to the Disputes API must be signed with an API key. For this, obtain an API Key from your Customer Area, as described inHow to get the API key. Then set this key to theX-API-Keyheader value, for example:

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: Your_API_key" \
...
```

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: Your_API_key" \
...
```
Note that when going live, you need to generate new web service user credentials to access thelive endpoints.

## Versioning
Disputes API supportsversioningusing a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.
For example:

```
https://ca-test.adyen.com/ca/services/DisputeService/v30/defendDispute
```

```
https://ca-test.adyen.com/ca/services/DisputeService/v30/defendDispute
```