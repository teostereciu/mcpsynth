# legalentity/4/overview

*Source: https://docs.adyen.com/api-explorer/legalentity/4/overview*

---

# Legal Entity Management API
The Legal Entity Management API enables you to manage legal entities that contain information required for verification.

## Authentication
Each request to the Legal Entity Management API must be signed with an API key. Generate an API key in your Customer Area if you have aplatform setupormarketplace setup.
If you have an Adyen Issuing integration,generate an API keyin your Balance Platform Customer Area.
To connect to the API, add anX-API-Keyheader with the API key as the value. For example:

```
curl
-H "X-API-Key: YOUR_API_KEY" \
-H "Content-Type: application/json" \
...
```

```
curl
-H "X-API-Key: YOUR_API_KEY" \
-H "Content-Type: application/json" \
...
```

## Versioning
The Legal Entity Management API supportsversioningusing a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.
For example:

```
https://kyc-test.adyen.com/lem/v4/legalEntities
```

```
https://kyc-test.adyen.com/lem/v4/legalEntities
```

## Rate limits
We enforce rate limits on Legal Entity Management API endpoints. When the number of requests you send exceeds a threshold within a time frame, additional requests are blocked until the time frame ends. Current limits:
- Live environments: 700 requests per 5 seconds.
- Test environments: 200 requests per 5 seconds.
- Failed requests are subject to a limit of 5 failures per 10 seconds.

## Going live
When going live, generate an API key in yourlive Customer Areaif you have an Adyen for Platforms integration orlive Balance Platform Customer Areaif you have an Adyen Issuing integration.You can then use the API key to send requests tohttps://kyc-live.adyen.com/lem/v4.