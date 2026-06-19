# capital-webhooks/1/post/balancePlatform.capital.dynamicOffer.created

*Source: https://docs.adyen.com/api-explorer/capital-webhooks/1/post/balancePlatform.capital.dynamicOffer.created*

---

# Dynamic offer created
Adyen sends this webhook to provide details about a dynamic offer that has been created for an account holder.
The unique identifier of the account holder that the dynamic offer is for.
The contract type of the offer.
Possible values:
- loan
- cashAdvance
The expiration date and time of the offer validity period.
The type of financing that the offer is for.
Possible values:businessFinancing.
The unique identifier of the dynamic offer.
The maximum financing amount available to the account holder under this offer.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The minimum financing amount available to the account holder under this offer.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
Contains information about the repayment configuration of the grant.
Contains information about the time period in which your user must repay the total amount of the grant.
The estimated duration of the repayment term, in days.
The maximum duration of the repayment term, in days. Only applies whencontractTypeisloan.
The starting date and time of the offer validity period.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK