# Checkout/71/get/sessions/(sessionId)

*Source: https://docs.adyen.com/api-explorer/Checkout/71/get/sessions/(sessionId)*

---

# Get the result of a payment session
Returns the status of the payment session with thesessionIdandsessionResultspecified in the path.
ThesessionResultvalue from the Drop-in or Component.
A unique identifier of the session.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some fields are included only if you enable them. To enable these fields in your Customer Area, go toDevelopers>Additional data.Select additionalDataResponseAdditionalData3DSecureResponseAdditionalDataBillingAddressResponseAdditionalDataCardResponseAdditionalDataCommonResponseAdditionalDataDomesticErrorResponseAdditionalDataInstallmentsResponseAdditionalDataNetworkTokensResponseAdditionalDataOpiResponseAdditionalDataSepaResponseAdditionalDataSwishidstringA unique identifier of the session.paymentsarray[object]A list of all authorised payments done for this session.Show childrenHide childrenamountobjectAuthorised amount in the transaction.Show childrenHide childrencurrencystringMin length:3Max length:3The three-characterISO currency codeof the amount.valueintegerThe numeric value of the amount, inminor units.paymentMethodobjectOnly returned forresultCode:Authorised.
Details about the payment method used in the transaction.Show childrenHide childrenbrandstringThe card brand that the shopper used to pay. Only returned ifpaymentMethod.typeisscheme.typestringThepaymentMethod.typevalue used in the request.pspReferencestringAdyen's 16-character reference associated with the transaction/request. This value is globally unique. Use this reference when you communicate with us about this request.resultCodestringThe result of the payment. For more information, seeResult codes.Possible values:Authorised– The payment was successfully authorised. This state serves as an indicator to proceed with the delivery of goods and services. This is a final state.Received– Indicates the payment request was successfully received by Adyen, and will be processed. This is the initial state for all payments.Pending– The payment order was successfully received but the final status of the payment is not available yet. This is common for payment methods with an asynchronous flow.referencestringThe unique reference that you provided in the original/sessionsrequest. This identifies the payment and is used in all communication with you about the payment status.statusstringThe status of the session. The status included in the response doesn't get updated. Don't make the request again to check for payment status updates.Possible values:completed: the shopper completed the payment, and the payment was authorized.paymentPending: the shopper is in the process of making the payment. This applies to payment methods with an asynchronous flow, like voucher payments where the shopper completes the payment in a physical shop.refused: the session has been refused, because of too many refused payment attempts. The shopper can no longer complete the payment with this session.canceled: the shopper canceled the payment.expired: the session expired. The shopper can no longer complete the payment with this session. By default, the session expires one hour after it is created.

#### 200 - OK
- Authorised– The payment was successfully authorised. This state serves as an indicator to proceed with the delivery of goods and services. This is a final state.
- Received– Indicates the payment request was successfully received by Adyen, and will be processed. This is the initial state for all payments.
- Pending– The payment order was successfully received but the final status of the payment is not available yet. This is common for payment methods with an asynchronous flow.
- completed: the shopper completed the payment, and the payment was authorized.
- paymentPending: the shopper is in the process of making the payment. This applies to payment methods with an asynchronous flow, like voucher payments where the shopper completes the payment in a physical shop.
- refused: the session has been refused, because of too many refused payment attempts. The shopper can no longer complete the payment with this session.
- canceled: the shopper canceled the payment.
- expired: the session expired. The shopper can no longer complete the payment with this session. By default, the session expires one hour after it is created.