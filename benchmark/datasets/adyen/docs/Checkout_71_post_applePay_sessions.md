# Checkout/71/post/applePay/sessions

*Source: https://docs.adyen.com/api-explorer/Checkout/71/post/applePay/sessions*

---

# Get an Apple Pay session
You need to use this endpoint if you have an API-only integration with Apple Pay which uses Adyen's Apple Pay certificate.
The endpoint returns the Apple Pay session data which you need to complete theApple Pay session validation.
A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
This is the name that your shoppers will see in the Apple Pay interface.
The value returned asconfiguration.merchantNamefield from the/paymentMethodsresponse.

```
/paymentMethods
```
The domain name you provided when you added Apple Pay in your Customer Area.
This must match thewindow.location.hostnameof the web shop.
Your merchant identifier registered with Apple Pay.
Use the value of theconfiguration.merchantIdfield from the/paymentMethodsresponse.

```
/paymentMethods
```
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessdatastringBase64 encoded data you need tocomplete the Apple Pay merchant validation.

#### 200 - OK