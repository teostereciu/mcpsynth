# balanceplatform/2/post/scaDevices/(deviceId)/scaAssociations

*Source: https://docs.adyen.com/api-explorer/balanceplatform/2/post/scaDevices/(deviceId)/scaAssociations*

---

# Create a new SCA association for a device
Creates an association between an SCA-enabled device and an entity, such as an account holder. This action does not guarantee the association is immediately ready for use; its status may bependingApprovalif the account holder has existing devices.
The unique identifier of the SCA device that you are associating with a resource.
The list of entities to be associated.
The unique identifier of the entity.
The type of the entity that you are associating with the SCA device.
Possible values:accountHolderorpaymentInstrument.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 201 - CreatedAssociation created.Show moreShow lessscaAssociationsarray[object]List of associations created to the entities and their statuses.Show childrenHide childrenentityIdstringMin length:1Max length:100The unique identifier of the entity.entityTypestringThe type of entity you are associating the device with.Possible values:accountHolderorpaymentInstrument.scaDeviceIdstringMin length:30Max length:30The unique identifier for the SCA device.statusstringThe status of the association.Possible values:activeorpendingApproval.
- 400 - Bad RequestThe request contains invalid input and fails validation.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 404 - Not FoundDevice not found.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 201 - Created

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error