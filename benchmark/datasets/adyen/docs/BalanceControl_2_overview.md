# BalanceControl/2/overview

*Source: https://docs.adyen.com/api-explorer/BalanceControl/2/overview*

---

# Balance Control API
The Balance Control API allows you to view and manage the balances in your company and merchant accounts.

## Authentication
We recommend that you use an API key to connect to the Balance Control API. You cangenerate an API keyin your Customer Area.

### Header format
To connect to the Balance Control API, add anX-API-Keyheader with the API key as the value. For example:

```
curl
-H 'Content-Type: application/json' \
-H 'X-API-Key: ADYEN_API_KEY' \
...
```

```
curl
-H 'Content-Type: application/json' \
-H 'X-API-Key: ADYEN_API_KEY' \
...
```

## Versioning
The Balance Control API handles versioning as part of the endpoint URL. For example, to send a request to version 2 of the/balanceOverview/companies/{companyId}/balancesendpoint, use:
https://balance-control-test.adyen.com/balance-control/api/v2/balanceOverview/companies/{companyId}/balances

## Going live
When going live, generate an API key in yourlive Customer Area. You can then use the API key to send requests tohttps://balance-control-live.adyen.com/api/v2.