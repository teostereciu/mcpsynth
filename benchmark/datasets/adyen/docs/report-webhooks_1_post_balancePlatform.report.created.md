# report-webhooks/1/post/balancePlatform.report.created

*Source: https://docs.adyen.com/api-explorer/report-webhooks/1/post/balancePlatform.report.created*

---

# Report generated
Adyen sends this webhook after a report is generated and ready to be downloaded. The webhook contains the URL at which the report can be downloaded.
Before you download reports, ask your Adyen contact for your report credentials. You must use your the credentials to authenticate your GET request.
Contains event details.
The account holder related to the report.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The balance account related to the report.
The description of the resource.
The unique identifier of the resource.
The reference for the resource.
The unique identifier of the balance platform.
The date and time when the event was triggered, in ISO 8601 extended format. For example,2025-03-19T10:15:30+01:00.
The URL at which you can download the report. To download, you must authenticate your GET request with yourAPI credentials.
The filename of the report.
The ID of the resource.
The type of report. Possible values:
- balanceplatform_accounting_interactive_report
- balanceplatform_accounting_report
- balanceplatform_balance_report
- balanceplatform_fee_report
- balanceplatform_payment_instrument_report
- balanceplatform_payout_report
- balanceplatform_statement_report
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
Type of webhook.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK