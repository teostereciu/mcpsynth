# cloud-device-api/1/get/merchants/(merchantAccount)/connectedDevices

*Source: https://docs.adyen.com/api-explorer/cloud-device-api/1/get/merchants/(merchantAccount)/connectedDevices*

---

# Get a list of connected devices
Get a list of payment terminals or SDK installation IDs (in a Mobile solution) belonging to the specified merchant account that have an active cloud connection.  Thestorequery parameter limits the list of devices to those belonging to a specific store under the specified merchant account.
To make this request, your API credential must have the followingrole:
- Cloud Device API role
The store ID of the store belonging to the merchant account specified in the path.
The unique identifier of the merchant account.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200Successful operationShow moreShow lessuniqueDeviceIdsarray[string]A list of the unique IDs of the devices that have an active cloud connection.
The IDs are payment terminal IDs in the format[terminal model]-[serial number](for example, P400‑123456789), or SDK installation IDs as used in Mobile solutions.
- 401UnauthorizedShow moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 403ForbiddenShow moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200

#### 401

#### 403