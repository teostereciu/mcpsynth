# terminal-api/1/post/input

*Source: https://docs.adyen.com/api-explorer/terminal-api/1/post/input*

---

# Input Request
Content of theInputRequestmessage. It conveys the data to display and how to process it. In addition to the display on the Input Device, it might contain an operation (theDisplayOutputelement) per Display Device type.
Information to display and how to process it.
Contains a complete display operation for a Display or an Input Device type. For the Input Devices, Diagnosis andEnableService,ResponseRequiredFlag, andMinimumDisplayTimeshall be absent.
Indicates if the message response is required.
Number of seconds the message has to be displayed.
Logical device located on a Sale Terminal or a POI Terminal, in terms of class of information to output (display, print, or store), or input (keyboard) for the Cashier or the Customer.
Possible values:
- CashierDisplay
- CashierInput
- CustomerDisplay
- CustomerInput
Qualification of the information to sent to an output logical device, to display or print to the Cashier or the Customer. Allows the manager of the device, Sale or POI Terminal, to send the information to a particular physical device or to present the information accordingly.
Possible values:
- CustomerAssistance
- Display
- Document
- Error
- Input
- POIReplication
- Receipt
- Sound
- Status
- Voucher
Content to display or print.
This is a sequence of elements if they have different formats.
Format of the content to display or print. Display or print device function.
Possible values:
- BarCode
- MessageRef
- Text
- XHTML
Reference of a predefined message to display or print.
It conveys information related to the predefined message.
Identification of a predefined message to display or print.
Identification of a language.
Content of text message to display or print.
Mandatory, ifOutputFormatis Text, not allowed otherwise. One instance ofOutputTextper shared format.
Content of text message to display, print or play.
Character height of the text string to display or print. Absence of this data element means the characters have normal height.
Row where the text string has to be displayed or printed.
Column where the text string has to be displayed or printed.
Character width of the text string to display or print. Absence of this data element means the characters have normal width.
Possible values:
- DoubleWidth
- SingleWidth
Character height of the text string to display or print. Absence of this data element means the characters have normal height.
Possible values:
- DoubleHeight
- HalfHeight
- SingleHeight
Typographic style of the sequence of characters to display or print. Absence of this data element means the characters have normal style.
Possible values:
- Bold
- Italic
- Normal
- Underline
Alignment of the text string on the display line or print line. Absence of this data element means the characters have normal alignment.
Possible values:
- Centred
- Justified
- Left
- Right
Indicates if the text is at the end of a line. Allows the display or the print of a new line and a carry-over return characters after the formatted text.
XHTML document body containing the message to display or print.
Mandatory ifOutputFormatis XHTML, not allowed otherwise.
Barcode content to display or print.
Mandatory ifOutputFormatis Barcode, not allowed otherwise.
Value with a Barcode coding. The barcode value to display or print.
An entry of the menu to present to the Cashier. It conveys the message text and parameters of the menu entry. This output data could be only provided for an input command, in order to choose an entryof the menu.
Characteristics related to the selection of a menu entry.
Possible values:
- NonSelectable
- NonSelectableSubMenu
- Selectable
- SubMenu
Selection of a menu entry to be displayed. In Input request message, it allows selection of one or several menu entries before any user action.
Format of the content to display or print. Display or print device function.
Possible values:
- BarCode
- MessageRef
- Text
- XHTML
Reference of a predefined message to display or print.
It conveys information related to the predefined message.
Identification of a predefined message to display or print.
Identification of a language.
Content of text message to display or print. It conveys Information related to the content of the text message and its format. All the data elements related to the format of the text to display or print are parameters valid for the whole Text content.
Content of text message to display, print or play.
Character height of the text string to display or print. Absence of this data element means the characters have normal height.
Row where the text string has to be displayed or printed.
Column where the text string has to be displayed or printed.
Character width of the text string to display or print. Absence of this data element means the characters have normal width.
Possible values:
- DoubleWidth
- SingleWidth
Character height of the text string to display or print. Absence of this data element means the characters have normal height.
Possible values:
- DoubleHeight
- HalfHeight
- SingleHeight
Typographic style of the sequence of characters to display or print. Absence of this data element means the characters have normal style.
Possible values:
- Bold
- Italic
- Normal
- Underline
Alignment of the text string on the display line or print line. Absence of this data element means the characters have normal alignment.
Possible values:
- Centred
- Justified
- Left
- Right
Indicates if the text is at the end of a line. Allows the display or the print of a new line and a carry-over return characters after the formatted text.
XHTML document body containing the message to display or print.
Vendor-specific signature of the text message to display or print.
If protection has to be provided to the vendor on the text to display or print.
Information related to an Input request. It conveys the target input logical device, the type of input command, and possible minimum and maximum length of the input. In addition, if the requestor might require to receive an Event Notification if a card is inserted in a card reader, with theNotifyCardInputFlag.
Logical device located on a Sale Terminal or a POI Terminal, regarding the class of information to output (display, print or store), or input (keyboard) for the Cashier or the Customer.
Possible values:
- CashierDisplay
- CashierInput
- CustomerDisplay
- CustomerInput
Qualification of the information to send to an output logical device, to display or print to the Cashier or the Customer.
Possible values:
- CustomerAssistance
- Display
- Document
- Error
- Input
- POIReplication
- Receipt
- Sound
- Status
- Voucher
Type of requested input. Can be:GetConfirmation,TextString,DigitString,DecimalStringorGetMenuEntry.
Possible values:
- DecimalString
- DigitString
- GetAnyKey
- GetConfirmation
- GetFunctionKey
- GetMenuEntry
- Password
- SiteManager
- TextString
Request Notification of the card entered in the POI card reader.
Maximum input time in seconds. Limits the time to answer to an Input request message.
Indicates whether to request an Immediate response to the message without waiting for the completion of the command.
Minimum length of an entered string, or minimum number of entries that can be selected in a menu.
Maximum length of an entered string, or maximum number of entries that can be selected in a menu.
Maximum input length of the decimal part (without decimal point).
Indicates that the user must confirm the entered characters, when the maximum allowed length is reached. During the processing of an Input commandTextString,DigitStringorDecimalStringwithMaxLengthorMaxDecimalLengthpresent in the request.
Default string value for an input command. On theTextString,DigitStringandDecimalStringinput commands: default string displayed on the input field before entering the string. InGetConfirmationinput command:Yfor yes,Nfor no.
String mask to get information requiring a specific format. For the processing of an Input commandTextString,DigitStringorDecimalString. Some information as date or plate number required to be entered with a certain format.
Indicates if the entered character has to be displayed from the right to the left of the display field.
Indicates to mask the characters entered by the user (i.e. replacing in the display of the input, the entered character by a standard character as *).
Indicates, when the user press a key, if a beep has to be generated (value True).
Indicates, when the user presses the Correct function key in an input entry, if all the entered characters are removed (value True) or only the last entered character if any (value False).
Indicates if the Cancel function key has to be deactivated (value True).
Indicates if the Correct function key has to be deactivated (value True). During the processing of an Input commandGetConfirmation,SiteManager, orGetMenuEntry.
Indicates if the Valid function key has to be deactivated (value True). During the processing of an Input commandGetConfirmation,SiteManager, orGetMenuEntry.
If it has the value True, it indicates that the Back function key (respectively Home function key) may be used to go back to the immediate upper level of the menu. If it has the value False, it indicates that the current menu level has no parent menu.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200It conveys the result of the input or the result of the outputs, parallel to the message request, except if response not required and absent.
Content of the Input Response message.Show moreShow lessOutputResultobjectIn the message response, it contains the result of the output, if required in the message request.
Information related to the result the output (display, print, input).Show childrenHide childrenDevicestringLogical device located on a Sale Terminal or a POI Terminal, in term of class of information to output (display, print or store), or input (keyboard) for the Cashier or the Customer.
Copy.
Possible values:CashierDisplayCashierInputCustomerDisplayCustomerInputInfoQualifystringQualification of the information to sent to an output logical device, to display or print to the Cashier or the Customer.
Copy.
Possible values:CustomerAssistanceDisplayDocumentErrorInputPOIReplicationReceiptSoundStatusVoucherResponseobjectResult of a message request processing.
If Result is Success,ErrorConditionis absent or not used in the processing of the message. In the other cases, theErrorConditionhas to be present and can refine the processing of the message response.AdditionalResponsegives more information about the success or the failure of the message request processing, for logging without real time involvements.Show childrenHide childrenResultstringResult of the processing of the message.
Possible values:FailurePartialSuccessErrorConditionstringCondition that has produced an error on the processing of a message request.
Returned if Result is not Success.
Possible values:AbortedBusyCancelDeviceOutInProgressInsertedCardInvalidCardLoggedOutMessageFormatNotAllowedNotFoundPaymentRestrictionRefusalUnavailableDeviceUnavailableServiceUnreachableHostWrongPINAdditionalResponsestringAdditional information related to processing status of a message request.
If present, the POI logs it for further examination.InputResultobjectContains the result and the content of the input.Show childrenHide childrenDevicestringLogical device located on a Sale Terminal or a POI Terminal, in terms of class of information to output (display, print or store), or input (keyboard) for the Cashier or the Customer.
Possible values:CashierDisplayCashierInputCustomerDisplayCustomerInputInfoQualifystringQualification of the information to send to an output logical device, to display or print to the Cashier or the Customer.
Possible values:CustomerAssistanceDisplayDocumentErrorInputPOIReplicationReceiptSoundStatusVoucherResponseobjectResult of a message request processing.
If Result is Success,ErrorConditionis absent or not used in the processing of the message. In the other cases, theErrorConditionhas to be present and can refine the processing of the message response.AdditionalResponsegives more information about the success or the failure of the message request processing, for logging without real time involvements.Show childrenHide childrenResultstringResult of the processing of the message.
Possible values:FailurePartialSuccessErrorConditionstringCondition that has produced an error on the processing of a message request.
Returned if Result is not Success.
Possible values:AbortedBusyCancelDeviceOutInProgressInsertedCardInvalidCardLoggedOutMessageFormatNotAllowedNotFoundPaymentRestrictionRefusalUnavailableDeviceUnavailableServiceUnreachableHostWrongPINAdditionalResponsestringAdditional information related to processing status of a message request.
If present, the POI logs it for further examination.InputobjectData entered by the user, related to the input command.Show childrenHide childrenInputCommandstringType of requested input. Can be:GetConfirmation,TextString,DigitString,DecimalStringorGetMenuEntry.
Possible values:DecimalStringDigitStringGetAnyKeyGetConfirmationGetFunctionKeyGetMenuEntryPasswordSiteManagerTextStringConfirmedFlagbooleanIndicates te response of the user from theGetConfirmationinput command.FunctionKeyintegerThe number of the function key which is typed by the Customer on the POI or the Cashier on the Sale Terminal.TextInputstringThe text typed by the Customer on the POI or by the Cashier on the Sale Terminal.DigitInputintegerThe digits typed by the Customer on the POI or by the Cashier on the Sale Terminal.PasswordstringThe text password typed by the Customer on the POI or by the Cashier on the Sale Terminal.MenuEntryNumberarray[integer]The index of the menu item (from 1 to n) which is selected by the Cashier on the Sale Terminal. The value -1 indicates that the immediate upper level of the menu is requested. The value 0 indicates that the root of the menu is requested.

#### 200
- CashierDisplay
- CashierInput
- CustomerDisplay
- CustomerInput
- CustomerAssistance
- Display
- Document
- Error
- Input
- POIReplication
- Receipt
- Sound
- Status
- Voucher
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
- CashierDisplay
- CashierInput
- CustomerDisplay
- CustomerInput
- CustomerAssistance
- Display
- Document
- Error
- Input
- POIReplication
- Receipt
- Sound
- Status
- Voucher
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
- DecimalString
- DigitString
- GetAnyKey
- GetConfirmation
- GetFunctionKey
- GetMenuEntry
- Password
- SiteManager
- TextString