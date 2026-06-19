# balanceplatform/2/get/accountHolders/(id)/taxFormSummary

*Source: https://docs.adyen.com/api-explorer/balanceplatform/2/get/accountHolders/(id)/taxFormSummary*

---

# Get summary of tax forms for an account holder
Returns a summary of all tax forms for an account holder.
The type of tax form you want a summary for. Accepted values areUS1099kandUS1099nec.
The unique identifier of the account holder.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessdataarray[object]A list of tax form summaries, where each summary consists of the legal entity and the tax years in which the legal entity has a tax form.Show childrenHide childrenlegalEntityIdstringThe unique identifier of the legal entity.taxYearsarray[integer]The tax years for which the legal entity has a tax form.

#### 200 - OK