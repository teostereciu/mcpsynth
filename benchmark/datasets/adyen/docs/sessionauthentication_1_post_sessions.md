# sessionauthentication/1/post/sessions

*Source: https://docs.adyen.com/api-explorer/sessionauthentication/1/post/sessions*

---

# Create a session token
Creates a session token that is required to integratecomponents.
The response contains encrypted session data. The front end then uses the session data to make the required server-side calls for the component.
To create a token, you must meet specific requirements. These requirements vary depending on the type of component. For more information, see the documentation forOnboardingandPlatform Experiencecomponents.
The URL where the component will appear. In your live environment, you must protect the URL with an SSL certificate and ensure that it starts withhttps://.
An object that contains a description of the allowed resources and roles for the requested session.
An object containing the type and the unique identifier of the user of the component.
ForOnboarding components, this is the ID of the legal entity that has a contractual relationship with your platform. For sole proprietorships, use the ID of the legal entity of the individual owner.
ForPlatform Experience components, this is the ID of the account holder that is associated with the balance account shown in the component.
The resource type.
Possible values:accountHolder,legalEntity.
You must also include the corresponding unique identifier of the resource. For example, the account holder ID.
The name of the role required to use the component.
The type of component.
ForOnboarding components, set this toonboarding.
ForPlatform Experience components, set this toplatform.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200Successful operationShow moreShow lessidstringThe unique identifier of the session.tokenstringThe session token created.
- 400Bad requestShow moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 401UnauthorizedShow moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.
- 403ForbiddenShow moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringUnique business error code.instancestringA URI that identifies the specific occurrence of the problem if applicable.invalidFieldsarray[object]Array of fields with validation errors when applicable.Show childrenHide childrennamestringThe field that has an invalid value.valuestringThe invalid value.messagestringDescription of the validation error.requestIdstringThe unique reference for the request.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the validation error type. It points to human-readable documentation for the problem type.

#### 200

#### 400

#### 401

#### 403