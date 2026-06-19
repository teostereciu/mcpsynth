# legalentity/4/get/documents/(id)

*Source: https://docs.adyen.com/api-explorer/legalentity/4/get/documents/(id)*

---

# Get a document
Returns a document.
Requests to this endpoint are subject to rate limits:
- Live environments: 700 requests per 5 seconds.
- Test environments: 200 requests per 5 seconds.
- Failed requests are subject to a limit of 5 failures per 10 seconds.
Do not load document content while fetching the document.
The unique identifier of the document.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessattachmentobjectDeprecated in version 1Use theattachmentsarray instead.Object that contains the document.Show childrenHide childrencontentstringThe document in Base64-encoded string format.contentTypestringDeprecated in version 1The file format.Possible values:application/pdf,image/jpg,image/jpeg,image/png.filenamestringDeprecated in version 1The name of the file including the file extension.pageNamestringThe name of the file including the file extension.pageTypestringSpecifies which side of the ID card is uploaded.If thetypeisdriversLicenseoridentityCard, you must set this tofrontorbackand include both sides in the same API request.For any other types, when this is omitted, we infer the page number based on the order of attachments.attachmentsarray[object]Array that contains the document. The array supports multiple attachments for uploading different sides or pages of a document.Show childrenHide childrencontentstringThe document in Base64-encoded string format.contentTypestringDeprecated in version 1The file format.Possible values:application/pdf,image/jpg,image/jpeg,image/png.filenamestringDeprecated in version 1The name of the file including the file extension.pageNamestringThe name of the file including the file extension.pageTypestringSpecifies which side of the ID card is uploaded.If thetypeisdriversLicenseoridentityCard, you must set this tofrontorbackand include both sides in the same API request.For any other types, when this is omitted, we infer the page number based on the order of attachments.creationDatestringThe creation date of the document.descriptionstringYour description for the document.expiryDatestringDeprecated in version 1The expiry date of the document, in YYYY-MM-DD format.fileNamestringThe filename of the document.idstringThe unique identifier of the document.issuerCountrystringDeprecated in version 1The two-characterISO 3166-1 alpha-2country code where the document was issued. For example,US.issuerStatestringDeprecated in version 1The state or province where the document was issued (AU only).modificationDatestringThe modification date of the document.numberstringThe number in the document.ownerobjectContains information about the resource that owns the document.Show childrenHide childrenidstringUnique identifier of the resource that owns the document. FortypelegalEntity, this value is the unique identifier of thelegal entity. FortypebankAccount, this value is the unique identifier of thetransfer instrument.typestringType of resource that owns the document.Possible values:legalEntity,bankAccount.typestringType of document, used when providing an ID number or uploading a document. The possible values depend on the legal entity type.Fororganization, thetypevalues can beproofOfAddress,registrationDocument,vatDocument,proofOfOrganizationTaxInfo,proofOfOwnership,proofOfIndustry,proofOfSignatory,proofOfDirector, orproofOfFundingOrWealthSource.Forindividual, thetypevalues can beidentityCard,driversLicense,passport,liveSelfie,proofOfNationalIdNumber,proofOfResidency,proofOfIndustry,proofOfIndividualTaxId,proofOfFundingOrWealthSourceorproofOfRelationship.ForsoleProprietorship, thetypevalues can beconstitutionalDocument,proofOfAddress, orproofOfIndustry.Fortrust, thetypevalue isconstitutionalDocument.ForunincorporatedPartnership, thetypevalue isconstitutionalDocument.UsebankStatementto upload documents for atransfer instrument.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- If thetypeisdriversLicenseoridentityCard, you must set this tofrontorbackand include both sides in the same API request.
- For any other types, when this is omitted, we infer the page number based on the order of attachments.
- If thetypeisdriversLicenseoridentityCard, you must set this tofrontorbackand include both sides in the same API request.
- For any other types, when this is omitted, we infer the page number based on the order of attachments.
- Fororganization, thetypevalues can beproofOfAddress,registrationDocument,vatDocument,proofOfOrganizationTaxInfo,proofOfOwnership,proofOfIndustry,proofOfSignatory,proofOfDirector, orproofOfFundingOrWealthSource.
- Forindividual, thetypevalues can beidentityCard,driversLicense,passport,liveSelfie,proofOfNationalIdNumber,proofOfResidency,proofOfIndustry,proofOfIndividualTaxId,proofOfFundingOrWealthSourceorproofOfRelationship.
- ForsoleProprietorship, thetypevalues can beconstitutionalDocument,proofOfAddress, orproofOfIndustry.
- Fortrust, thetypevalue isconstitutionalDocument.
- ForunincorporatedPartnership, thetypevalue isconstitutionalDocument.
- UsebankStatementto upload documents for atransfer instrument.

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error