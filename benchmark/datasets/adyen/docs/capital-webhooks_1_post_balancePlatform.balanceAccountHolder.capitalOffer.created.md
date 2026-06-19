# capital-webhooks/1/post/balancePlatform.balanceAccountHolder.capitalOffer.created

*Source: https://docs.adyen.com/api-explorer/capital-webhooks/1/post/balancePlatform.balanceAccountHolder.capitalOffer.created*

---

# Static offer created
Adyen sends this webhook to provide details about a static offer that has been created for an account holder.
The unique identifier of the account holder to which the grant is offered.
The amount that would be paid out to the user for business financing.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The contract type of the offer.
Possible values:
- loan
- cashAdvance
The expiration date and time of the offer validity period.
Contains information about the fee that your user would pay for the grant.
Contains the amount of the offer fee.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
Annual Percentage Rate (APR) of the offer. The percentage is expressed inbasis points.
The unique identifier of the offer.
Contains information about the repayment configuration of the grant.
The percentage of your user's incoming net volume that is deducted for repaying the grant. The percentage expressed inbasis points.
Contains information about the time period in which your user must repay the total amount of the grant.
The estimated duration of the repayment term, in days.
The maximum duration of the repayment term, in days. Only applies whencontractTypeisloan.
Contains the minimum threshold amount that your user must repay every 30-day period.
The minimum threshold amount that your user must repay on every 30-day period.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The starting date and time of the offer validity period.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK