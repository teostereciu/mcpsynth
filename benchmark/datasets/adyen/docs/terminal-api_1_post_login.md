# terminal-api/1/post/login

*Source: https://docs.adyen.com/api-explorer/terminal-api/1/post/login*

---

# Login Request
It conveys information related to the session (period between a Login and the following Logout) to process.
Content of theLoginRequestmessage.
Date and Time. In the Login request message, the Sale System gives its date and time to the POI System. In the Login response, the POI System gives its date and time to the Sale System.
Information related to the software of the Sale System which manages the NEXO Sale to POI protocol.
Identification of the Manufacturer.
Name of the software product.
Version of the software product.
Certification code of the software which manages the Sale to POI protocol.
Information related to the software and hardware features of the Sale Terminal.
Sent in the Login Request if a Sale Terminal is involved in the login. In other messages, sent when a logical device is out of order (SaleCapabilities) or when other data have changed or were missing in the Login.
Identification of a group of transactions on a POI Terminal, having the same Sale features.
Could be used to group POI for reconciliation or other purpose defined by the Sale System. The default value is assigned by the Login Request.
Training mode.
This flag indicates to the POI that the entire session will be not used to make real transaction, but is used for test of system or operator training.
Language of the Cashier or Operator.
Default value for Device type displays.
Identification of the Cashier or Operator.
Four conditions to send it:
- The Sale System wants the POI to log it in the transaction log.
- Because of reconciliation with total on OperatorID.
- Because the POI needs it.
- Acquirer or issuer need it.
Shift number.
Same as OperatorID.
Type of token replacing the PAN of a payment card to identify the payment mean of the customer. It allows, for a merchant, to use a token for a transaction only or for a longer period.
Possible values:
- Customer
- Transaction
List of customer order open, closed or both to be sent in the response messages.
Possible values:
- Both
- Closed
- Open
Serial number of a POI Terminal.
If the login involve a POI Terminal and not the first Login to the POI System.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200It conveys Information related to the Login to process.
Content of the Login Response message.Show moreShow lessResponseobjectResult of a message request processing.
If Result is Success,ErrorConditionis absent or not used in the processing of the message. In the other cases, theErrorConditionhas to be present and can refine the processing of the message response.AdditionalResponsegives more information about the success or the failure of the message request processing, for logging without real time involvements.Show childrenHide childrenResultstringResult of the processing of the message.
Possible values:FailurePartialSuccessErrorConditionstringCondition that has produced an error on the processing of a message request.
Returned if Result is not Success.
Possible values:AbortedBusyCancelDeviceOutInProgressInsertedCardInvalidCardLoggedOutMessageFormatNotAllowedNotFoundPaymentRestrictionRefusalUnavailableDeviceUnavailableServiceUnreachableHostWrongPINAdditionalResponsestringAdditional information related to processing status of a message request.
If present, the POI logs it for further examination.POISystemDataobjectInformation related to the POI System.
Returned if the response result is Success.Show childrenHide childrenDateTimestringDate and Time. In the response, the POI System gives its date and time to the Sale System.POISoftwareobjectInformation related to the software of the POI System which manages the Sale to POI protocol. In a session allows identifying the product features of a POI System.Show childrenHide childrenManufacturerIDstringIdentification of the Manufacturer. Sent in the Login Request (Response) to identify the Sale System (POI System) manufacturer during the session.ApplicationNamestringName of the software product. Sent in the Login Request (Response) to identify the Sale System (POI System) product name during the session.SoftwareVersionstringVersion of the software product. Sent in the Login Request (Response) to identify the version of the Sale System (POI System) product software during the session.CertificationCodestringCertification code of the software which manages the Sale to POI protocol. Sent in the Login Request (Response) to get the certification code of the Sale System (POI System) product software. This code can be a software checksum or any number associated with the software.POIStatusobjectIndicate the availability of the POI Terminal components. The data element is absent if the component is not part of the POI Terminal.
State of a POI Terminal.Show childrenHide childrenGlobalStatusstringGlobal status of a POI Server or POI Terminal.
Possible values:BusyMaintenanceOKUnreachableSecurityOKFlagbooleanIndicates if the security module of the POI is working and usable.
If security module present.PEDOKFlagbooleanIndicates if the PED is working and usable.
If PED present.CardReaderOKFlagbooleanIndicates if the card readers are working and usable.
If card reader device present.PrinterStatusstringIndicates if the printer is working and usable.
Possible values:NoPaperOKOutOfOrderPaperJamPaperLowCommunicationOKFlagbooleanIndicates if the communication infrastructure is working and usable.
If communication infrastructure present.FraudPreventionFlagbooleanIndicates a suspicion of fraud by the POI System.
Could be set to True by the POI system to notify to the Sale system and the Cashier that a suspicion of fraud had been detected on the POI as an unexpected reboot of the POI.TokenRequestStatusbooleanIf token is managed by the POI, the status of the token request.

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