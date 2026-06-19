# postfmapi/1/post/assignTerminals

*Source: https://docs.adyen.com/api-explorer/postfmapi/1/post/assignTerminals*

---

# Assign terminals
Use POST/terminals/{terminalId}/reassign.
Assigns one or more payment terminals to a merchant account or a store. You can also use this endpoint to reassign terminals between merchant accounts or stores, and to unassign a terminal and return it to company inventory.
From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate the management of your terminal fleet, use ourManagement API.
Your company account. To return terminals to the company inventory, specify only this parameter and theterminals.
Name of the merchant account. Specify this parameter to assign terminals to this merchant account or to a store under this merchant account.
Boolean that indicates if you are assigning the terminals to the merchant inventory. Do not use when assigning terminals to a store. Required when assigning the terminal to a merchant account.
- Set this totrueto assign the terminals to the merchant inventory. This also means that the terminals cannot be boarded.
- Set this tofalseto assign the terminals to the merchant account as in-store terminals. This makes the terminals ready to be boarded and to process payments through the specified merchant account.
The store code of the store that you want to assign the terminals to.
Array containing a list of terminal IDs that you want to assign or reassign to the merchant account or store, or that you want to return to the company inventory.
For example,["V400m-324689776","P400Plus-329127412"].
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessresultsobjectArray that returns a list of the terminals, and for each terminal the result of assigning it to an account or store.The results can be:Done: The terminal has been assigned.AssignmentScheduled: The terminal will be assigned asynschronously.RemoveConfigScheduled: The terminal was previously assigned and boarded. Wait for the terminal to synchronize with the Adyen platform. For more information, refer toReassigning boarded terminals.Error: There was an error when assigning the terminal.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- Done: The terminal has been assigned.
- AssignmentScheduled: The terminal will be assigned asynschronously.
- RemoveConfigScheduled: The terminal was previously assigned and boarded. Wait for the terminal to synchronize with the Adyen platform. For more information, refer toReassigning boarded terminals.
- Error: There was an error when assigning the terminal.

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error