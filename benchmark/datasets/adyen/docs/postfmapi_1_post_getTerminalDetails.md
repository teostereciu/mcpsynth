# postfmapi/1/post/getTerminalDetails

*Source: https://docs.adyen.com/api-explorer/postfmapi/1/post/getTerminalDetails*

---

# Get the details of a terminal
Use GET/terminals. For the details of a store, use GET/stores/{storeId}.
Returns the details of a payment terminal, including where the terminal is assigned to. The response returns the same details that are provided in the terminal list in your Customer Area and in the Terminal Fleet report.
From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate the management of your terminal fleet, use ourManagement API.
The unique terminal ID in the format[Device model]-[Serial number].
For example,V400m-324689776.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessbluetoothIpstringThe Bluetooth IP address of the terminal.bluetoothMacstringThe Bluetooth MAC address of the terminal.companyAccountstringThe company account that the terminal is associated with. If this is the only account level shown in the response, the terminal is assigned to the inventory of the company account.countrystringThe country where the terminal is used.deviceModelstringThe model name of the terminal.dhcpEnabledbooleanIndicates whether assigning IP addresses through a DHCP server is enabled on the terminal.displayLabelstringThe label shown on the status bar of the display. This label (if any) is specified in your Customer Area.ethernetIpstringThe terminal's IP address in your Ethernet network.ethernetMacstringThe terminal's MAC address in your Ethernet network.firmwareVersionstringThe software release currently in use on the terminal.iccidstringThe integrated circuit card identifier (ICCID) of the SIM card in the terminal.lastActivityDateTimestringDate and time of the last activity on the terminal. Not included when the last activity was more than 14 days ago.lastTransactionDateTimestringDate and time of the last transaction on the terminal. Not included when the last transaction was more than 14 days ago.linkNegotiationstringThe Ethernet link negotiation that the terminal uses:auto: Auto-negotiation100full: 100 Mbps full duplexmerchantAccountstringThe merchant account that the terminal is associated with. If the response doesn't contain astorethe terminal is assigned to this merchant account.merchantInventorybooleanBoolean that indicates if the terminal is assigned to the merchant inventory. This is returned when the terminal is assigned to a merchant account.Iftrue, this indicates that the terminal is in the merchant inventory. This also means that the terminal cannot be boarded.Iffalse, this indicates that the terminal is assigned to the merchant account as an in-store terminal. This means that the terminal is ready to be boarded, or is already boarded.permanentTerminalIdstringThe permanent terminal ID.serialNumberstringThe serial number of the terminal.simStatusstringOn a terminal that supports 3G or 4G connectivity, indicates the status of the SIM card in the terminal: ACTIVE or INVENTORY.storestringThe store code of the store that the terminal is assigned to.storeDetailsobjectThe store that the terminal is assigned to.Show childrenHide childrenaddressobjectThe address of the store.Show childrenHide childrencitystringcountryCodestringpostalCodestringstateOrProvincestringstreetAddressstringstreetAddress2stringdescriptionstringThe description of the store.inStoreTerminalsarray[string]The list of terminals assigned to the store.merchantAccountCodestringThe code of the merchant account.statusstringThe status of the store:PreActive: the store has been created, but not yet activated.Active: the store has been activated. This means you can process payments for this store.Inactive: the store is currently not active.InactiveWithModifications: the store is currently not active, but payment modifications such as refunds are possible.Closed: the store has been closed.storestringThe code of the store.terminalstringThe unique terminal ID.terminalStatusstringThe status of the terminal:OnlineToday,OnlineLast1Day,OnlineLast2Daysetcetera toOnlineLast7Days: Indicates when in the past week the terminal was last online.SwitchedOff: Indicates it was more than a week ago that the terminal was last online.ReAssignToInventoryPending,ReAssignToStorePending,ReAssignToMerchantInventoryPending: Indicates the terminal is scheduled to be reassigned.wifiIpstringThe terminal's IP address in your Wi-Fi network.wifiMacstringThe terminal's MAC address in your Wi-Fi network.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- auto: Auto-negotiation
- 100full: 100 Mbps full duplex
- Iftrue, this indicates that the terminal is in the merchant inventory. This also means that the terminal cannot be boarded.
- Iffalse, this indicates that the terminal is assigned to the merchant account as an in-store terminal. This means that the terminal is ready to be boarded, or is already boarded.
- PreActive: the store has been created, but not yet activated.
- Active: the store has been activated. This means you can process payments for this store.
- Inactive: the store is currently not active.
- InactiveWithModifications: the store is currently not active, but payment modifications such as refunds are possible.
- Closed: the store has been closed.
- OnlineToday,OnlineLast1Day,OnlineLast2Daysetcetera toOnlineLast7Days: Indicates when in the past week the terminal was last online.
- SwitchedOff: Indicates it was more than a week ago that the terminal was last online.
- ReAssignToInventoryPending,ReAssignToStorePending,ReAssignToMerchantInventoryPending: Indicates the terminal is scheduled to be reassigned.

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error