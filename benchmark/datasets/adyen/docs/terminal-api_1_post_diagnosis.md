# terminal-api/1/post/diagnosis

*Source: https://docs.adyen.com/api-explorer/terminal-api/1/post/diagnosis*

---

# Diagnosis Request
It conveys Information related to the target POI for which the diagnosis is requested.
Content of the Diagnosis Request message.
Identification of a POI System or a POI Terminal for the Sale to POI protocol.
MessageHeader.POIID.
Indicates if Host Diagnosis are required.
Identification of the Acquirer.
Present if requesting the diagnosis of these hosts only.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200It conveys the result of the requested diagnosis and a possible message to display on a logical device.
Content of the Diagnosis Response message.Show moreShow lessResponseobjectResult of a message request processing.
If Result is Success,ErrorConditionis absent or not used in the processing of the message. In the other cases, theErrorConditionhas to be present and can refine the processing of the message response.AdditionalResponsegives more information about the success or the failure of the message request processing, for logging without real time involvements.Show childrenHide childrenResultstringResult of the processing of the message.
Possible values:FailurePartialSuccessErrorConditionstringCondition that has produced an error on the processing of a message request.
Returned if Result is not Success.
Possible values:AbortedBusyCancelDeviceOutInProgressInsertedCardInvalidCardLoggedOutMessageFormatNotAllowedNotFoundPaymentRestrictionRefusalUnavailableDeviceUnavailableServiceUnreachableHostWrongPINAdditionalResponsestringAdditional information related to processing status of a message request.
If present, the POI logs it for further examination.POIStatusobjectIndicate the availability of the POI Terminal components. The data element is absent if the component is not part of the POI Terminal.
State of a POI Terminal.Show childrenHide childrenGlobalStatusstringGlobal status of a POI Server or POI Terminal.
Possible values:BusyMaintenanceOKUnreachableSecurityOKFlagbooleanIndicates if the security module of the POI is working and usable.
If security module present.PEDOKFlagbooleanIndicates if the PED is working and usable.
If PED present.CardReaderOKFlagbooleanIndicates if the card readers are working and usable.
If card reader device present.PrinterStatusstringIndicates if the printer is working and usable.
Possible values:NoPaperOKOutOfOrderPaperJamPaperLowCommunicationOKFlagbooleanIndicates if the communication infrastructure is working and usable.
If communication infrastructure present.FraudPreventionFlagbooleanIndicates a suspicion of fraud by the POI System.
Could be set to True by the POI system to notify to the Sale system and the Cashier that a suspicion of fraud had been detected on the POI as an unexpected reboot of the POI.HostStatusarray[object]State of a Host.Show childrenHide childrenAcquirerIDintegerIdentification of the Acquirer.IsReachableFlagbooleanIndicate if a Host is reachable.

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
- Busy
- Maintenance
- OK
- Unreachable
- NoPaper
- OK
- OutOfOrder
- PaperJam
- PaperLow