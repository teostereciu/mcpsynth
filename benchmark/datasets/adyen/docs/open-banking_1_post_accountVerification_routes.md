# open-banking/1/post/accountVerification/routes

*Source: https://docs.adyen.com/api-explorer/open-banking/1/post/accountVerification/routes*

---

# Create routes for account verification
Create a list of routes for verifying bank accounts of third-party individuals. Successful connections generate a unique code used for requesting bank reports and verifying identity.
The location where the third-party individual's bank account is registered. Adyen uses this information to determine an available open banking provider, and to configure the open banking flow for that respective location.
The language to use in the open banking flow UI, specified by a combination of a two-letterISO 639-1language code and anISO 3166-1 alpha-2country code.
This information is used to configure the open banking flow with the same language for a consistent user experience.
Default value:en-US
The URL where Adyen redirects the third-party individual after they complete the open banking flow.
A value that helps you identify the request in callback handling. You can generate this value on a per-session basis to protect the callback against Cross-Site Request Forgery (CSRF) attacks. This value  must be composed of characters that can be successfully URL-encoded.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessroutesarray[object]This array lists available open banking redirection links, each with its associated provider metadata.Show childrenHide childrenlinkstringMin length:1The redirection link. You can use this link to redirect the user to the open banking flow when the user selects it.providerobjectMetadata about the selected provider, including the name and company logo. You can use this information to inform the user about the provider they will be redirected to when they select the link.Show childrenHide childrenlogoURLstringMin length:1The URL of the organization's or brand's logo. This URL typically points to an image file (e.g., .png, .jpg, .svg) that can be displayed to visually represent the entity.namestringMin length:1The official or commonly used name of the organization, brand, or entity.
- 400 - Bad RequestThe request is malformed or is not in the expected format.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 401 - UnauthorizedThe API credential used in the request is invalid or does not have the right permissions.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 429 - Too Many RequestsRequest rate limit exceeded.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 500 - Internal Service ErrorAn unrecoverable error occurred while trying to perform the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 422 - Unprocessable Entity

#### 429 - Too Many Requests

#### 500 - Internal Service Error