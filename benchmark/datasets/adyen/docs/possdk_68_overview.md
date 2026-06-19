# possdk/68/overview

*Source: https://docs.adyen.com/api-explorer/possdk/68/overview*

---

# POS Mobile API
The POS Mobile API is used in the mutual authentication flow between an Adyen Android or iOSPOS Mobile SDKand the Adyen payments platform.
The POS Mobile SDK for Android or iOS devices enables businesses to accept in-person payments using a commercial off-the-shelf (COTS) device like a phone. For example, Tap to Pay transactions, or transactions on a mobile device in combination with a card reader.

## Authentication
Each request to the POS Mobile API must be signed with an API key.Generate your API keyin the Customer Area and then set this key to theX-API-Keyheader value.
You also need to have aclient key. The client key is part of the setup but you won't need to use it in your integration later. Therefore, you don't need to specify allowed origins, and you don't need to store the key in your system.
To access the live endpoints, you need to generate a new API key and client key in your live Customer Area.

## Versioning
The POS Mobile API handles versioning as part of the endpoint URL.
For example:

```
https://checkout-test.adyen.com/checkout/possdk/v68/sessions
```

```
https://checkout-test.adyen.com/checkout/possdk/v68/sessions
```

## Going live
To access the live endpoints, you need an API key and client key from your live Customer Area.
The live endpoint URLs contain a prefix which is unique to your company account, for example:

```
https://{PREFIX}-checkout-live.adyenpayments.com/checkout/possdk/v68/sessions
```

```
https://{PREFIX}-checkout-live.adyenpayments.com/checkout/possdk/v68/sessions
```