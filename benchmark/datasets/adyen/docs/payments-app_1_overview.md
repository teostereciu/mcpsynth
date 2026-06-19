# payments-app/1/overview

*Source: https://docs.adyen.com/api-explorer/payments-app/1/overview*

---

# Payments App API
Board and manage the Adyen Payments App on your Android mobile devices.

## Authentication
Each request to the Payments App API must be signed with an API key.Generate your API keyin the Customer Area and then set this key to theX-API-Keyheader value.

## Versioning
Payments App API handles versioning as part of the endpoint URL. For example, to send a request to this version of the/merchants/{merchantId}/generatePaymentsAppBoardingTokenendpoint, use:

```
https://management-test.adyen.com/v1/merchants/{merchantId}/generatePaymentsAppBoardingToken
```

```
https://management-test.adyen.com/v1/merchants/{merchantId}/generatePaymentsAppBoardingToken
```

## Going live
To access the live endpoints, you need an API key from your live Customer Area. Use this API key to make requests to:

```
https://management-live.adyen.com/v{version}
```

```
https://management-live.adyen.com/v{version}
```