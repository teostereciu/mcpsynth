# terminal-api/1/post/reconciliation

*Source: https://docs.adyen.com/api-explorer/terminal-api/1/post/reconciliation*

---

# Reconciliation Request
Content of the Reconciliation Request message.
It conveys Information related to the Reconciliation requested by the Sale System.
Type of Reconciliation requested by the Sale to the POI.
Possible values:
- AcquirerReconciliation
- AcquirerSynchronisation
- PreviousReconciliation
- SaleReconciliation
Identification of the Acquirer.
Could be present only if ReconciliationType is AcquirerReconciliation or AcquirerSynchronisation.
Identification of the reconciliation period between Sale and POI.
Absent if ReconciliationType is not PreviousReconciliation.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200It conveys Information related to the Reconciliation transaction processed by the POI System.
Content of the Reconciliation Response message.Show moreShow lessResponseobjectResult of a message request processing.
If Result is Success,ErrorConditionis absent or not used in the processing of the message. In the other cases, theErrorConditionhas to be present and can refine the processing of the message response.AdditionalResponsegives more information about the success or the failure of the message request processing, for logging without real time involvements.Show childrenHide childrenResultstringResult of the processing of the message.
Possible values:FailurePartialSuccessErrorConditionstringCondition that has produced an error on the processing of a message request.
Returned if Result is not Success.
Possible values:AbortedBusyCancelDeviceOutInProgressInsertedCardInvalidCardLoggedOutMessageFormatNotAllowedNotFoundPaymentRestrictionRefusalUnavailableDeviceUnavailableServiceUnreachableHostWrongPINAdditionalResponsestringAdditional information related to processing status of a message request.
If present, the POI logs it for further examination.ReconciliationTypestringType of Reconciliation requested by the Sale to the POI.
Possible values:AcquirerReconciliationAcquirerSynchronisationPreviousReconciliationSaleReconciliationPOIReconciliationIDintegerIdentification of the reconciliation period between Sale and POI.
Absent if ReconciliationType isAcquirerReconciliation.TransactionTotalsarray[object]Result of the Sale to POI Reconciliation processing.
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
- AcquirerReconciliation
- AcquirerSynchronisation
- PreviousReconciliation
- SaleReconciliation
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