# capital-webhooks/1/post/balancePlatform.grants.created

*Source: https://docs.adyen.com/api-explorer/capital-webhooks/1/post/balancePlatform.grants.created*

---

# Grant created
After a grant is created, Adyen sends this webhook with information about the grant.
Contains information about the balances of the grant.
The three-characterISO currency code.
The amount of the grant fee.
The grant amount that is paid out to the user for business financing.
The total amount of the grant that the user must repay. It is the sum of the fee amount and the principal amount.
Contains the details of the party that receives the grant.
The unique identifier of the account holder that receives the grant.
The unique identifier of the balance account where the funds are disbursed. The balance account must belong to the specified account holder.
The unique identifier of the transfer instrument where the funds are disbursed. The transfer instrument must belong to the legal entity of the specified account holder.
The unique identifier of the grant account that tracks this grant.
The unique identifier of the selected offer. Adyen uses the details of the selected offer to create a grant.
The unique identifier of the grant reference.
Contains the status of the grant.
A list of actions that need to be completed to proceed with the grant.
The code identifying the action that needs to be completed.
Indicates whether this action has been successfully completed.
The code for the status of the grant. Possible values:
- Pending
- Active
- Repaid
- WrittenOff
- Failed
- Revoked
- Requested
- Reviewing
- Approved
- Rejected
- Cancelled
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK