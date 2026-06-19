# possdk/68/post/sessions

*Source: https://docs.adyen.com/api-explorer/possdk/68/post/sessions*

---

# Create a communication session
Establishes a secure communications session between the POS Mobile SDK and the Adyen payments platform, through mutual authentication.
The request sends a setup token that identifies the SDK and the device. The response returns a session token that the SDK can use to authenticate responses received from the Adyen payments platform.
This request applies tomobile in-persontransactions. You cannot use this request to create online payments sessions.
The unique identifier of your merchant account.
The setup token provided by the POS Mobile SDK.
- When using the Android POS Mobile SDK, obtain the token through theAuthenticationService.authenticate(setupToken)callback ofAuthenticationService.
- When using the iOS POS Mobile SDK, obtain the token through thePaymentServiceDelegate.register(with:)callback ofPaymentServiceDelegate.
The unique identifier of the store that you want to process transactions for.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 201 - CreatedThe request has been fulfilled and has resulted in one or more new resources being created.Show moreShow lessidstringThe unique identifier of the session.installationIdstringThe unique identifier of the SDK installation. If you create theTerminal APItransaction request on your backend, use this as thePOIIDin theMessageHeaderof the request.merchantAccountstringThe unique identifier of your merchant account.sdkDatastringThe data that the SDK uses to authenticate responses from the Adyen payments platform. Pass this value to your POS app.storestringThe unique identifier of the store that you want to process transactions for.

#### 201 - Created