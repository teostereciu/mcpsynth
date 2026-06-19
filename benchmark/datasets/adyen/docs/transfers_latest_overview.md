# transfers/latest/overview

*Source: https://docs.adyen.com/api-explorer/transfers/latest/overview*

---

# Transfers API
Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.
The Transfers API provides endpoints that you can use to transfer funds, whether when paying out to a transfer instrument formarketplacesorplatforms,sending funds to third partiesfor users with business bank accounts, or torequest a payout for a grant offer. The API also supports use cases forgetting transactions for business bank accountsand gettingoutstanding balancesfor one or more grants on your platform.

## Authentication
Each request to the Transfers API must be signed with an API key. Generate an API key in your Customer Area if you have aplatform setupormarketplace setup.
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

## Roles and permissions
To use the Transfers API, you need an additional role for your API credential. Transfers must also be enabled for the source balance account. Your Adyen contact will set up the roles and permissions for you.

## Versioning
The Transfers API supportsversioningusing a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.
For example:

```
https://balanceplatform-api-test.adyen.com/btl/v4/transfers
```

```
https://balanceplatform-api-test.adyen.com/btl/v4/transfers
```

## Going live
When going live, generate an API key in yourlive Customer Areaif you have an Adyen for Platforms integration orlive Balance Platform Customer Areaif you have an Adyen Issuing integration. You can then use the API key to send requests tohttps://balanceplatform-api-live.adyen.com/btl/v4.