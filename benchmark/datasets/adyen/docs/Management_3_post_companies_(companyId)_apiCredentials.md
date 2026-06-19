# Management/3/post/companies/(companyId)/apiCredentials

*Source: https://docs.adyen.com/api-explorer/Management/3/post/companies/(companyId)/apiCredentials*

---

# Create an API credential
Creates anAPI credentialfor the company account identified in the path. In the request, you can specify which merchant accounts the new API credential will have access to, as well as its roles and allowed origins.
The response includes several types of authentication details:
- API key: used for API request authentication.
- Client key: public key used for client-side authentication.
- Username and password: used for basic authentication.
Make sure you store the API key securely in your system. You won't be able to retrieve it later.
If your API key is lost or compromised, you need togenerate a new API key.
To make this request, your API credential must have the followingroles:
- Management API—API credentials read and write
The unique identifier of the company account.
List ofallowed originsfor the new API credential.
List of merchant accounts that the API credential has access to.
Description of the API credential.
List ofrolesfor the API credential. Only roles assigned to 'ws@Company.<CompanyName>' can be assigned to other API credentials.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow less_linksobjectReferences to resources linked to the API credential.Show childrenHide childrenallowedOriginsobjectList of allowed origins.Show childrenHide childrenhrefstringcompanyobjectCompany account that the API credential is linked to. Only present for company-level webhooks.Show childrenHide childrenhrefstringgenerateApiKeyobjectGenerates a new API key. When you generate a new one, the existing key remains valid for 24 hours.Show childrenHide childrenhrefstringgenerateClientKeyobjectGenerates a new client key, used to authenticate client-side requests. When you generate a new one, the existing key remains valid for 24 hours.Show childrenHide childrenhrefstringmerchantobjectThe merchant account that the API credential is linked to. Only present for merchant-level API credentials.Show childrenHide childrenhrefstringselfobjectLink to the resource itself.Show childrenHide childrenhrefstringactivebooleanIndicates if the API credential is enabled. Must be set totrueto use the credential in your integration.allowedIpAddressesarray[string]List of IP addresses from which your client can make requests.If the list is empty, we allow requests from any IP.
If the list is not empty and we get a request from an IP which is not on the list, you get a security error.allowedOriginsarray[object]List containing theallowed originslinked to the API credential.Show childrenHide children_linksobjectReferences to resources linked to the allowed origin.Show childrenHide childrenselfobjectLink to the resource itself.Show childrenHide childrenhrefstringdomainstringDomain of the allowed origin.idstringUnique identifier of the allowed origin.apiKeystringThe API key for the API credential that was created.associatedMerchantAccountsarray[string]List of merchant accounts that the API credential has access to.clientKeystringPublic key used forclient-side authentication. The client key is required for Drop-in and Components integrations.descriptionstringMax length:50Description of the API credential.idstringUnique identifier of the API credential.passwordstringThe password for the API credential that was created.rolesarray[string]List ofrolesfor the API credential.usernamestringThe name of theAPI credential, for examplews@Company.TestCompany.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error