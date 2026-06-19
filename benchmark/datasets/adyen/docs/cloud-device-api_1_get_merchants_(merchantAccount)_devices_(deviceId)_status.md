# cloud-device-api/1/get/merchants/(merchantAccount)/devices/(deviceId)/status

*Source: https://docs.adyen.com/api-explorer/cloud-device-api/1/get/merchants/(merchantAccount)/devices/(deviceId)/status*

---

# Get the connection status of a device
Check if the specified payment terminal or SDK installation ID (in an IPP Mobile solution) has an active cloud connection.
To make this request, your API credential must have the followingrole:
- Cloud Device API role
The unique identifier of the device.
For a payment terminal, use the terminal ID in the format[terminal model]-[serial number], for example,P400‑123456789.
In a Mobile solution, use the installation ID of the SDK.
The unique identifier of the merchant account.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200Successful operationShow moreShow lessdeviceIdstringThe unique identification of the device.
This can be a payment terminal ID in the format[terminal model]-[serial number](for example, P400‑123456789), or an SDK installation ID as used in Mobile solutions.statusstringIndicates if the device has an active cloud connection. Possible values:ONLINEOFFLINE
- 401UnauthorizedShow moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 403ForbiddenShow moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200
- ONLINE
- OFFLINE

#### 401

#### 403