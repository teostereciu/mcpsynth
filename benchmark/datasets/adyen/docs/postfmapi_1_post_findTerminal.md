# postfmapi/1/post/findTerminal

*Source: https://docs.adyen.com/api-explorer/postfmapi/1/post/findTerminal*

---

# Get the account or store of a terminal
Use GET/terminals, specifying the unique terminal ID as a query parameter.
Returns the company account, merchant account, or store that a payment terminal is assigned to.
From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate the management of your terminal fleet, use ourManagement API.
The unique terminal ID in the format[Device model]-[Serial number].
For example,V400m-324689776.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lesscompanyAccountstringThe company account that the terminal is associated with. If this is the only account level shown in the response, the terminal is assigned to the inventory of the company account.merchantAccountstringThe merchant account that the terminal is associated with. If the response doesn't contain astorethe terminal is assigned to this merchant account.merchantInventorybooleanBoolean that indicates if the terminal is assigned to the merchant inventory. This is returned when the terminal is assigned to a merchant account.Iftrue, this indicates that the terminal is in the merchant inventory. This also means that the terminal cannot be boarded.Iffalse, this indicates that the terminal is assigned to the merchant account as an in-store terminal. This means that the terminal is ready to be boarded, or is already boarded.storestringThe store code of the store that the terminal is assigned to.terminalstringThe unique terminal ID.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- Iftrue, this indicates that the terminal is in the merchant inventory. This also means that the terminal cannot be boarded.
- Iffalse, this indicates that the terminal is assigned to the merchant account as an in-store terminal. This means that the terminal is ready to be boarded, or is already boarded.

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error