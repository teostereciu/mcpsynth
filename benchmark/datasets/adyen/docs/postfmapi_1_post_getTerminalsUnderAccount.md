# postfmapi/1/post/getTerminalsUnderAccount

*Source: https://docs.adyen.com/api-explorer/postfmapi/1/post/getTerminalsUnderAccount*

---

# Get the list of terminals
Use GET/terminals.
Returns a list of payment terminals associated with a company account, merchant account, or store. The response shows whether the terminals are in the inventory, or in-store (ready for boarding or already boarded).
From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate the management of your terminal fleet, use ourManagement API.
Your company account. If you only specify this parameter, the response includes all terminals at all account levels.
The merchant account. This is required if you are retrieving the terminals assigned to a store.If you don't specify astorethe response includes the terminals assigned to the specified merchant account and the terminals assigned to the stores under this merchant account.
The store code of the store. With this parameter, the response only includes the terminals assigned to the specified store.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lesscompanyAccountstringYour company account.inventoryTerminalsarray[string]Array that returns a list of all terminals that are in the inventory of the company account.merchantAccountsarray[object]Array that returns a list of all merchant accounts belonging to the company account.Show childrenHide childreninStoreTerminalsarray[string]List of terminals assigned to this merchant account as in-store terminals. This means that the terminal is ready to be boarded, or is already boarded.inventoryTerminalsarray[string]List of terminals assigned to the inventory of this merchant account.merchantAccountstringThe merchant account.storesarray[object]Array of stores under this merchant account.Show childrenHide childrenaddressobjectThe address of the store.Show childrenHide childrencitystringcountryCodestringpostalCodestringstateOrProvincestringstreetAddressstringstreetAddress2stringdescriptionstringThe description of the store.inStoreTerminalsarray[string]The list of terminals assigned to the store.merchantAccountCodestringThe code of the merchant account.statusstringThe status of the store:PreActive: the store has been created, but not yet activated.Active: the store has been activated. This means you can process payments for this store.Inactive: the store is currently not active.InactiveWithModifications: the store is currently not active, but payment modifications such as refunds are possible.Closed: the store has been closed.storestringThe code of the store.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- PreActive: the store has been created, but not yet activated.
- Active: the store has been activated. This means you can process payments for this store.
- Inactive: the store is currently not active.
- InactiveWithModifications: the store is currently not active, but payment modifications such as refunds are possible.
- Closed: the store has been closed.

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error