# foreignexchange/1/post/rates/calculate

*Source: https://docs.adyen.com/api-explorer/foreignexchange/1/post/rates/calculate*

---

# Calculate amount in a different currency
Returns the calculated amounts and rates required to convert the currency of a transaction.
An array of objects, where each object defines a currency and value for which you want to perform an exchange calculation.
The operation performed on the source amount. Possible values:
- buy
- sell
An object specifying the currency and value for which you want to perform an exchange calculation.
The three-characterISO currency code.
The amount of the transaction, inminor units.
The currency to which you want to convert the source amount.
The type of transaction. Possible values:
- splitPayment: for payments
- splitRefund: for refunds
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200Successful operationShow moreShow lessexchangeCalculationsarray[object]An array of objects, where each object returns a currency and value for which you performed an exchange calculation. You can use the calculated amounts in your payment requests.Show childrenHide childrenappliedExchangeRatenumberThe exchange rate to convert the source currency to the target currency. This includes Adyen's markup.exchangeSidestringThe operation performed on the source amount. Possible values:buysellsourceAmountobjectThe currency of the amount you converted (the source amount).Show childrenHide childrencurrencystringThe three-characterISO currency code.valueintegerThe amount of the transaction, inminor units.targetAmountobjectAn object specifying the currency and value to which you want to convert the source amount (the target amount).Show childrenHide childrencurrencystringThe three-characterISO currency code.valueintegerThe amount of the transaction, inminor units.typestringThe type of transaction. Possible values:splitPayment: for paymentssplitRefund: for refunds
- 401UnauthorizedShow moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 403ForbiddenShow moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200
- buy
- sell
- splitPayment: for payments
- splitRefund: for refunds

#### 401

#### 403

#### 422 - Unprocessable Entity