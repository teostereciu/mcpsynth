# terminal-api/1/post/cardreaderapdu

*Source: https://docs.adyen.com/api-explorer/terminal-api/1/post/cardreaderapdu*

---

# CardReaderAPDU Request
It contains the APDU request to send to the chip of the card, and a possible invitation message to display on the CashierInterface or the CustomerInterface.
Content of the Card Reader APDU Request message.
Class field of the APDU command (CLA). APDU request for Card Reader device request. For specific card like synchronous card, a private value should be used in accordance to ISO 7816- 4 (private range D0-FE).
Instruction field of the APDU command (INS).
Parameter 1 field of the APDU command (P1).
Parameter 2 field of the APDU command(P2).
Data field of the APDU command (Lc + Data).
Expected length of the data field of the APDU response to the command (Le).
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200Content of the Card Reader APDU Response message.
It contains the result of the requested service, APDU response sent by the chip of the card in response to the APDU request.Show moreShow lessResponseobjectResult of a message request processing.
If Result is Success,ErrorConditionis absent or not used in the processing of the message. In the other cases, theErrorConditionhas to be present and can refine the processing of the message response.AdditionalResponsegives more information about the success or the failure of the message request processing, for logging without real time involvements.Show childrenHide childrenResultstringResult of the processing of the message.
Possible values:FailurePartialSuccessErrorConditionstringCondition that has produced an error on the processing of a message request.
Returned if Result is not Success.
Possible values:AbortedBusyCancelDeviceOutInProgressInsertedCardInvalidCardLoggedOutMessageFormatNotAllowedNotFoundPaymentRestrictionRefusalUnavailableDeviceUnavailableServiceUnreachableHostWrongPINAdditionalResponsestringAdditional information related to processing status of a message request.
If present, the POI logs it for further examination.APDUDatastringData field of the APDU command (Lc + Data).CardStatusWordsstringStatus of a smartcard response to a command (SW1-SW2).

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