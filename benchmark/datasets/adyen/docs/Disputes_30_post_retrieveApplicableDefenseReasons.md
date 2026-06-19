# Disputes/30/post/retrieveApplicableDefenseReasons

*Source: https://docs.adyen.com/api-explorer/Disputes/30/post/retrieveApplicableDefenseReasons*

---

# Get applicable defense reasons
Returns a list of all applicable defense reasons to defend a specific dispute.
The PSP reference assigned to the dispute.
The merchant account identifier, for which you want to process the dispute transaction.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessdefenseReasonsarray[object]The defense reasons that can be used to defend the dispute.Show childrenHide childrendefenseDocumentTypesarray[object]Array of defense document types for a specific defense reason. Indicates the document types that you can submit to the schemes to defend this dispute, and whether they are required.Show childrenHide childrenavailablebooleanWhentrue, you've successfully uploaded this type of defense document. Whenfalse, you haven't uploaded this defense document type.defenseDocumentTypeCodestringThe document type code of the defense document.requirementLevelstringIndicates to what extent the defense document is required in the defense process.Possible values:Required: You must supply the document.OneOrMore: You must supply at least one of the documents with this label.Optional: You can choose to supply the document.AlternativeRequired: You must supply a generic defense document. To enable this functionality, contact our Support Team. When enabled, you can supply a generic defense document for all schemes.defenseReasonCodestringThe defense reason code that was selected to defend this dispute.satisfiedbooleanIndicates if sufficient defense material has been supplied.disputeServiceResultobjectThe result of the dispute service.Show childrenHide childrenerrorMessagestringThe general error message.successbooleanIndicates whether the request succeeded.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- Required: You must supply the document.
- OneOrMore: You must supply at least one of the documents with this label.
- Optional: You can choose to supply the document.
- AlternativeRequired: You must supply a generic defense document. To enable this functionality, contact our Support Team. When enabled, you can supply a generic defense document for all schemes.

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error