# terminal-api/1/post/gettotals

*Source: https://docs.adyen.com/api-explorer/terminal-api/1/post/gettotals*

---

# GetTotals Request
It conveys information from the Sale System related to the scope and the format of the totals to be computed by the POI System.
Content of the Get Totals Request message.
Indicates the hierarchical structure of the reconciliation result of the Sale to POI reconciliation.
Required to present totals per value of element included in this cluster (POI Terminal, Sale Terminal, Cashier, Shift, TotalsGroupID).
Possible values:
- OperatorID
- POIID
- SaleID
- ShiftNumber
- TotalsGroupID
Filter to compute the totals.
Used for the Get Totals, to request totals for a (or a combination of) particular value of the POI Terminal, Sale Terminal, Cashier, Shift, or TotalsGroupID.
Identification of a POI System or a POI Terminal for the Sale to POI protocol.
Identification of a Sale System or a Sale Terminal for the Sale to POI protocol.
Identification of the Cashier or Operator.
Shift number.
Sent if totals in the response have to be computed only for this particular value of TotalsGroupID.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200Content of the Reconciliation Response message.
It conveys Information related to the Reconciliation transaction processed by the POI System.Show moreShow lessResponseobjectResult of a message request processing.
If Result is Success,ErrorConditionis absent or not used in the processing of the message. In the other cases, theErrorConditionhas to be present and can refine the processing of the message response.AdditionalResponsegives more information about the success or the failure of the message request processing, for logging without real time involvements.Show childrenHide childrenResultstringResult of the processing of the message.
Possible values:FailurePartialSuccessErrorConditionstringCondition that has produced an error on the processing of a message request.
Returned if Result is not Success.
Possible values:AbortedBusyCancelDeviceOutInProgressInsertedCardInvalidCardLoggedOutMessageFormatNotAllowedNotFoundPaymentRestrictionRefusalUnavailableDeviceUnavailableServiceUnreachableHostWrongPINAdditionalResponsestringAdditional information related to processing status of a message request.
If present, the POI logs it for further examination.POIReconciliationIDintegerIdentification of the reconciliation period between Sale and POI.TransactionTotalsarray[object]Result of the Sale to POI Reconciliation processing.
IfResponse.Resultis Success.Show childrenHide childrenPaymentInstrumentTypestringType of payment instrument.
Possible values:CardCashCheckMobileStoredValueAcquirerIDintegerIdentification of the Acquirer.HostReconciliationIDstringIdentifier of a reconciliation period with a payment or loyalty host.CardBrandstringType of payment or loyalty card.
If configured to present totals per card brand, and Response.Result is Success.POIIDstringIdentification of a POI System or a POI Terminal for the Sale to POI protocol.
Sent if requested in the message request.SaleIDstringIdentification of a Sale System or a Sale Terminal for the Sale to POI protocol.
Sent if requested in the message request.OperatorIDstringIdentification of the Cashier or Operator.
Sent if requested in the message request.ShiftNumberstringShift number.
Sent if requested in the message request.TotalsGroupIDstringIdentification of a group of transaction on a POI Terminal, having the same Sale features.
Sent if requested in the message request.PaymentCurrencystringCurrency of a monetary amount.PaymentTotalsarray[object]Totals of the payment transaction during the reconciliation period.
If bothTransactionCountandTransactionAmountare not equal to zero.Show childrenHide childrenTransactionTypestringType of transaction for which totals are grouped.
Debit, Credit, ReverseDebit, ReverseCredit, OneTimeReservation, CompletedDeffered, FirstReservation, UpdateReservation, CompletedReservation, CashAdvance.
Possible values:AwardCashAdvanceCompletedDefferedCompletedReservationCreditDebitDeclinedFailedFirstReservationIssuerInstalmentOneTimeReservationRebateRedemptionReverseAwardReverseCreditReverseDebitReverseRebateReverseRedemptionUpdateReservationTransactionCountintegerNumber of processed transaction during the period.TransactionAmountnumberMaximum:99999999.999999Sum of amount of processed transaction during the period.

#### 200
- Failure
- Partial
- Success
- Aborted
- Busy
- Cancel
- DeviceOut
- InProgress
- InsertedCard
- InvalidCard
- LoggedOut
- MessageFormat
- NotAllowed
- NotFound
- PaymentRestriction
- Refusal
- UnavailableDevice
- UnavailableService
- UnreachableHost
- WrongPIN
- Card
- Cash
- Check
- Mobile
- StoredValue
- Award
- CashAdvance
- CompletedDeffered
- CompletedReservation
- Credit
- Debit
- Declined
- Failed
- FirstReservation
- IssuerInstalment
- OneTimeReservation
- Rebate
- Redemption
- ReverseAward
- ReverseCredit
- ReverseDebit
- ReverseRebate
- ReverseRedemption
- UpdateReservation