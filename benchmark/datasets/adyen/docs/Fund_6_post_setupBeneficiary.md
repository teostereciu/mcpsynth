# Fund/6/post/setupBeneficiary

*Source: https://docs.adyen.com/api-explorer/Fund/6/post/setupBeneficiary*

---

# Designate a beneficiary account and transfer the benefactor's current balance
Defines a benefactor and a beneficiary relationship between two accounts. At the time of benefactor/beneficiary setup, the funds in the benefactor account are transferred to the beneficiary account, and any further payments to the benefactor account are automatically sent to the beneficiary account. A series of benefactor/beneficiaries may not exceed four beneficiaries and may not have a cycle in it.
The destination account code.
A value that can be supplied at the discretion of the executing user.
The benefactor account.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessinvalidFieldsarray[object]Contains field validation errors that would prevent requests from being processed.Show childrenHide childrenerrorCodeintegerThe validation error code.errorDescriptionstringA description of the validation error.fieldTypeobjectThe type of error field.Show childrenHide childrenfieldstringThe full name of the property.fieldNamestringThe type of the field.shareholderCodestringThe code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.pspReferencestringThe reference of a request. Can be used to uniquely identify the request.resultCodestringThe result code.
- 202 - AcceptedThe request has been accepted for processing, but the processing has not been completed.Show moreShow lessinvalidFieldsarray[object]Contains field validation errors that would prevent requests from being processed.Show childrenHide childrenerrorCodeintegerThe validation error code.errorDescriptionstringA description of the validation error.fieldTypeobjectThe type of error field.Show childrenHide childrenfieldstringThe full name of the property.fieldNamestringThe type of the field.shareholderCodestringThe code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.pspReferencestringThe reference of a request. Can be used to uniquely identify the request.resultCodestringThe result code.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK

#### 202 - Accepted

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error