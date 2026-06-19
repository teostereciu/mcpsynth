# foreignexchange/1/overview

*Source: https://docs.adyen.com/api-explorer/foreignexchange/1/overview*

---

# Foreign Exchange API
The Foreign Exchange API allows you to manage and convert the currencies that are enabled for your integration.

## Authentication
We recommend that you use an API key to connect to the Foreign Exchange API. You can generate an API key in your Customer Area. If you have an Adyen Issuing integration, generate an API key in your Balance Platform Customer Area.

### Credential format
- For therates/calculateendpoint: Generate an API key for the credential with the formatws@BalancePlatform.[YourBalancePlatform].

### Header format
To connect to the Foreign Exchange API, add anX-API-Keyheader with the API key as the value, for example:

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
The Foreign Exchange API supportsversioningusing a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.
For example:
https://balanceplatform-api-test.adyen.com/fx/v1/rates/calculate

## Going live
When going live, generate an API key in yourlive Customer Area. If you have an Adyen Issuing integration,generate an API keyin yourlive Balance Platform Customer Area. You can then use the API key to send requests tohttps://balanceplatform-api-test.adyen.com/fx/v1.