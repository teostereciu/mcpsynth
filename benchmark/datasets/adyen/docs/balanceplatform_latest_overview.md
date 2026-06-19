# balanceplatform/latest/overview

*Source: https://docs.adyen.com/api-explorer/balanceplatform/latest/overview*

---

# Configuration API
The Configuration API allows you to manage your balance platform where you can create account holders, balance accounts, cards, and business accounts.

## Authentication
Each request to the Configuration API must be signed with an API key. Generate an API key in your Customer Area if you have aplatform setupormarketplace setup.
If you have an Adyen Issuing integration,generate an API keyin your Balance Platform Customer Area.
To connect to the API, add anX-API-Keyheader with the API key as the value, for example:

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
The Configuration API supportsversioningusing a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.
For example:

```
https://balanceplatform-api-test.adyen.com/bcl/v2/accountHolders
```

```
https://balanceplatform-api-test.adyen.com/bcl/v2/accountHolders
```

## Going live
When going live, generate an API key in yourlive Customer Areaif you have an Adyen for Platforms integration orlive Balance Platform Customer Areaif you have an Adyen Issuing integration.You can then use the API key to send requests tohttps://balanceplatform-api-live.adyen.com/bcl/v2.