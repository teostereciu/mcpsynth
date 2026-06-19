# Account/6/post/getUploadedDocuments

*Source: https://docs.adyen.com/api-explorer/Account/6/post/getUploadedDocuments*

---

# Get documents
Returns documents that were previously uploaded for an account holder. Adyen uses the documents during theverification process.
The code of the Account Holder for which to retrieve the documents.
The code of the Bank Account for which to retrieve the documents.
The code of the Shareholder for which to retrieve the documents.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessdocumentDetailsarray[object]A list of the documents and their details.Show childrenHide childrenaccountHolderCodestringThe code of account holder, to which the document applies.bankAccountUUIDstringThe Adyen-generatedbankAccountUUIDto which the document must be linked. Refer toBank account checkfor details on when a document should be submitted.Required if thedocumentTypeisBANK_STATEMENT, where a document is being submitted in order to verify a bank account.descriptionstringDescription of the document.documentTypestringThe type of the document. Refer toVerification checksfor details on when each document type should be submitted and for the accepted file formats.Permitted values:BANK_STATEMENT: A file containing a bank statement or other document proving ownership of a specific bank account.COMPANY_REGISTRATION_SCREENING(Supported from v5 and later): A file containing a company registration document.CONSTITUTIONAL_DOCUMENT: A file containing information about the account holder's legal arrangement.PASSPORT: A file containing the identity page(s) of a passport.ID_CARD_FRONT: A file containing only the front of the ID card. In order for a document to be usable, both theID_CARD_FRONTandID_CARD_BACKmust be submitted.ID_CARD_BACK: A file containing only the back of the ID card. In order for a document to be usable, both theID_CARD_FRONTandID_CARD_BACKmust be submitted.DRIVING_LICENCE_FRONT: A file containing only the front of the driving licence. In order for a document to be usable, both theDRIVING_LICENCE_FRONTandDRIVING_LICENCE_BACKmust be submitted.DRIVING_LICENCE_BACK: A file containing only the back of the driving licence. In order for a document to be usable, both theDRIVING_LICENCE_FRONTandDRIVING_LICENCE_FRONTmust be submitted.filenamestringFilename of the document.legalArrangementCodestringThe Adyen-generatedlegalArrangementCodeto which the document must be linked.legalArrangementEntityCodestringThe Adyen-generatedlegalArrangementEntityCodeto which the document must be linked.shareholderCodestringThe Adyen-generatedshareholderCodeto which the document must be linked. Refer toVerification checksfor details on when a document should be submitted.Required if the account holder has alegalEntityof typeBusinessand thedocumentTypeis eitherPASSPORT,ID_CARD_FRONT,ID_CARD_BACK,DRIVING_LICENCE_FRONT, orDRIVING_LICENCE_BACK.signatoryCodestringThe Adyen-generatedsignatoryCodeto which the document must be linked.invalidFieldsarray[object]Contains field validation errors that would prevent requests from being processed.Show childrenHide childrenerrorCodeintegerThe validation error code.errorDescriptionstringA description of the validation error.fieldTypeobjectThe type of error field.Show childrenHide childrenfieldstringThe full name of the property.fieldNamestringThe type of the field.shareholderCodestringThe code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.pspReferencestringThe reference of a request. Can be used to uniquely identify the request.resultCodestringThe result code.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK

```
bankAccountUUID
```
- BANK_STATEMENT: A file containing a bank statement or other document proving ownership of a specific bank account.
- COMPANY_REGISTRATION_SCREENING(Supported from v5 and later): A file containing a company registration document.
- CONSTITUTIONAL_DOCUMENT: A file containing information about the account holder's legal arrangement.
- PASSPORT: A file containing the identity page(s) of a passport.
- ID_CARD_FRONT: A file containing only the front of the ID card. In order for a document to be usable, both theID_CARD_FRONTandID_CARD_BACKmust be submitted.
- ID_CARD_BACK: A file containing only the back of the ID card. In order for a document to be usable, both theID_CARD_FRONTandID_CARD_BACKmust be submitted.
- DRIVING_LICENCE_FRONT: A file containing only the front of the driving licence. In order for a document to be usable, both theDRIVING_LICENCE_FRONTandDRIVING_LICENCE_BACKmust be submitted.
- DRIVING_LICENCE_BACK: A file containing only the back of the driving licence. In order for a document to be usable, both theDRIVING_LICENCE_FRONTandDRIVING_LICENCE_FRONTmust be submitted.

```
legalArrangementCode
```

```
legalArrangementEntityCode
```

```
shareholderCode
```

```
signatoryCode
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error