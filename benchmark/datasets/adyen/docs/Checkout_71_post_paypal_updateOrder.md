# Checkout/71/post/paypal/updateOrder

*Source: https://docs.adyen.com/api-explorer/Checkout/71/post/paypal/updateOrder*

---

# Updates the order for PayPal Express Checkout
Updates the order for PayPal Express Checkout. This can be used to update the PayPal lightbox with an updated amount and delivery methods based on the delivery address.
A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
The updated final payment amount. This amount is the item total plus the shipping costs of the selecteddeliveryMethod.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The list of new delivery methods and the cost of each.
The cost of this delivery method.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The name of the delivery method as shown to the shopper.
The reference of the delivery method.
If you display the PayPal lightbox with delivery methods, set totruefor the delivery method that is selected. Only one delivery method can be selected at a time.
The type of the delivery method.
ThepaymentDatafrom the client side. This value changes every time you make a/paypal/updateOrderrequest.
The originalpspReferencefrom the/paymentsresponse.
The originalsessionIdfrom the/sessionsresponse.
Total tax amount from the order.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lesspaymentDatastringThe updated paymentData.statusstringThe status of the request. This indicates whether the order was successfully updated with PayPal.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error