# Management/3/post/companies/(companyId)/terminalOrders

*Source: https://docs.adyen.com/api-explorer/Management/3/post/companies/(companyId)/terminalOrders*

---

# Create an order
Creates an order for payment terminal products for the company identified in the path.
To make this request, your API credential must have the followingrole:
- Management API—Terminal ordering read and write
Requests to the Management API test endpoint do not create actual orders for test terminals. To order test terminals, you need tosubmit a sales orderin your Customer Area.
In the live environment, requests to this endpoint are subject torate limits.
The unique identifier of the company account.
The identification of the billing entity to use for the order.
When ordering products in Brazil, you do not need to include thebillingEntityIdin the request.
The merchant-defined purchase order reference.
The products included in the order.
The unique identifier of the product.
The number of installments for the specified productid.
The name of the product.
The number of items with the specified productidincluded in the order.
Type of order
The identification of the shipping location to use for the order.
The tax number of the billing entity.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessbillingEntityobjectThe details of the entity that the order is billed to.Show childrenHide childrenaddressobjectThe address details of the billing entity.Show childrenHide childrencitystringThe name of the city.companyNamestringThe name of the company.countrystringThe two-letter country code, inISO 3166-1 alpha-2format.postalCodestringThe postal code.stateOrProvincestringThe state or province as defined inISO 3166-2. For example,ONfor Ontario, Canada.Applicable for the following countries:AustraliaBrazilCanadaIndiaMexicoNew ZealandUnited StatesstreetAddressstringThe name of the street, and the house or building number.streetAddress2stringAdditional address details, if any.emailstringThe email address of the billing entity.idstringThe unique identifier of the billing entity, for use asbillingEntityIdwhen creating an order.namestringThe unique name of the billing entity.taxIdstringThe tax number of the billing entity.customerOrderReferencestringThe merchant-defined purchase order number. This will be printed on the packing list.idstringThe unique identifier of the order.itemsarray[object]The products included in the order.Show childrenHide childrenidstringThe unique identifier of the product.installmentsintegerThe number of installments for the specified productid.namestringThe name of the product.quantityintegerThe number of items with the specified productidincluded in the order.orderDatestringThe date and time that the order was placed, in UTC ISO 8601 format. For example, "2011-12-03T10:15:30Z".shippingLocationobjectThe details of the location where the order is shipped to.Show childrenHide childrenaddressobjectThe address details of the shipping location.Show childrenHide childrencitystringThe name of the city.companyNamestringThe name of the company.countrystringThe two-letter country code, inISO 3166-1 alpha-2format.postalCodestringThe postal code.stateOrProvincestringThe state or province as defined inISO 3166-2. For example,ONfor Ontario, Canada.Applicable for the following countries:AustraliaBrazilCanadaIndiaMexicoNew ZealandUnited StatesstreetAddressstringThe name of the street, and the house or building number.streetAddress2stringAdditional address details, if any.contactobjectThe contact details for the shipping location.Show childrenHide childrenemailstringThe individual's email address.firstNamestringThe individual's first name.infixstringThe infix in the individual's name, if any.lastNamestringThe individual's last name.phoneNumberstringThe individual's phone number, specified as 10-14 digits with an optional+prefix.idstringThe unique identifier of the shipping location, for use asshippingLocationIdwhen creating an order.namestringThe unique name of the shipping location.statusstringThe processing status of the order.trackingUrlstringThe URL, provided by the carrier company, where the shipment can be tracked.
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