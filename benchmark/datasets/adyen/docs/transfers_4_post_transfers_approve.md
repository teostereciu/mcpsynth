# transfers/4/post/transfers/approve

*Source: https://docs.adyen.com/api-explorer/transfers/4/post/transfers/approve*

---

# Approve initiated transfers
Initiates the approval of a list of transfers that triggered an additionalreview. Adyen sends the outcome of the approval request through webhooks.
To use this endpoint:
- Your API credential must have theTransferService Approverole.
- The account holder must have the requiredcapabilities.
Reach out to your Adyen contact to set up these permissions.
Header for authenticating through SCA
A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
Contains the unique identifiers of the transfers that you want to approve.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - No ContentLook at the actual response code for the status of the request.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.routingDetailsarray[object]Detailed explanation of each attempt to route the transfer with the priorities from the request.Show childrenHide childrendetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.prioritystringThe priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers withcategorybank.Possible values:regular: For normal, low-value transactions.fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.instant: For instant funds transfers within the United States and inSEPA locations.crossBorder: For high-value transfers to a recipient in a different country.internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).titlestringA short, human-readable summary of the problem type.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.routingDetailsarray[object]Detailed explanation of each attempt to route the transfer with the priorities from the request.Show childrenHide childrendetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.prioritystringThe priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers withcategorybank.Possible values:regular: For normal, low-value transactions.fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.instant: For instant funds transfers within the United States and inSEPA locations.crossBorder: For high-value transfers to a recipient in a different country.internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).titlestringA short, human-readable summary of the problem type.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.routingDetailsarray[object]Detailed explanation of each attempt to route the transfer with the priorities from the request.Show childrenHide childrendetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.prioritystringThe priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers withcategorybank.Possible values:regular: For normal, low-value transactions.fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.instant: For instant funds transfers within the United States and inSEPA locations.crossBorder: For high-value transfers to a recipient in a different country.internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).titlestringA short, human-readable summary of the problem type.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - No Content

#### 401 - Unauthorized

#### 403 - Forbidden
- regular: For normal, low-value transactions.
- fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.
- wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.
- instant: For instant funds transfers within the United States and inSEPA locations.
- crossBorder: For high-value transfers to a recipient in a different country.
- internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).

#### 422 - Unprocessable Entity
- regular: For normal, low-value transactions.
- fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.
- wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.
- instant: For instant funds transfers within the United States and inSEPA locations.
- crossBorder: For high-value transfers to a recipient in a different country.
- internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).

#### 500 - Internal Server Error
- regular: For normal, low-value transactions.
- fast: A faster way to transfer funds, but the fees are higher. Recommended for high-priority, low-value transactions.
- wire: The fastest way to transfer funds, but this has the highest fees. Recommended for high-priority, high-value transactions.
- instant: For instant funds transfers within the United States and inSEPA locations.
- crossBorder: For high-value transfers to a recipient in a different country.
- internal: For transfers to an Adyen-issued business bank account (by bank account number/IBAN).