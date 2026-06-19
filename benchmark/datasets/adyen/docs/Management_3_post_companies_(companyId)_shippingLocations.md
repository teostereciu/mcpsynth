# Management/3/post/companies/(companyId)/shippingLocations

*Source: https://docs.adyen.com/api-explorer/Management/3/post/companies/(companyId)/shippingLocations*

---

# Create a shipping location
Creates a shipping location for the company identified in the path. A shipping location defines an address where orders can be delivered.
To make this request, your API credential must have the followingrole:
- Management API—Terminal ordering read and write
In the live environment, requests to this endpoint are subject torate limits.
The unique identifier of the company account.
The address details of the shipping location.
The name of the city.
The name of the company.
The two-letter country code, inISO 3166-1 alpha-2format.
The postal code.
The state or province as defined inISO 3166-2. For example,ONfor Ontario, Canada.
Applicable for the following countries:
- Australia
- Brazil
- Canada
- India
- Mexico
- New Zealand
- United States
The name of the street, and the house or building number.
Additional address details, if any.
The contact details for the shipping location.
The individual's email address.
The individual's first name.
The infix in the individual's name, if any.
The individual's last name.
The individual's phone number, specified as 10-14 digits with an optional+prefix.
The unique identifier of the shipping location, for use asshippingLocationIdwhen creating an order.
The unique name of the shipping location.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessaddressobjectThe address details of the shipping location.Show childrenHide childrencitystringThe name of the city.companyNamestringThe name of the company.countrystringThe two-letter country code, inISO 3166-1 alpha-2format.postalCodestringThe postal code.stateOrProvincestringThe state or province as defined inISO 3166-2. For example,ONfor Ontario, Canada.Applicable for the following countries:AustraliaBrazilCanadaIndiaMexicoNew ZealandUnited StatesstreetAddressstringThe name of the street, and the house or building number.streetAddress2stringAdditional address details, if any.contactobjectThe contact details for the shipping location.Show childrenHide childrenemailstringThe individual's email address.firstNamestringThe individual's first name.infixstringThe infix in the individual's name, if any.lastNamestringThe individual's last name.phoneNumberstringThe individual's phone number, specified as 10-14 digits with an optional+prefix.idstringThe unique identifier of the shipping location, for use asshippingLocationIdwhen creating an order.namestringThe unique name of the shipping location.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - OK
- Australia
- Brazil
- Canada
- India
- Mexico
- New Zealand
- United States

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error