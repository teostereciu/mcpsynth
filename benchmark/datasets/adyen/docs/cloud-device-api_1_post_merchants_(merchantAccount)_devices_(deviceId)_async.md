# cloud-device-api/1/post/merchants/(merchantAccount)/devices/(deviceId)/async

*Source: https://docs.adyen.com/api-explorer/cloud-device-api/1/post/merchants/(merchantAccount)/devices/(deviceId)/async*

---

# Send a Terminal API request and receive an asynchronous response
Sends a Terminal API request and receives the response asynchronously.
The request body is a JSON object containing a Terminal API request. For the structure, see the various request types underTerminal API.
A HTTP status code of200 OKis returned when the payment device is online and our backend has sent the request. The actual Terminal API response is returned as an event notification webhook to your event notification endpoint. SeeReceiving an asynchronous result.
To make this request, your API credential must have the followingrole:
- Cloud Device API role
The unique identifier of the payment device that you send this request to. Must be the same as thePOIIDin theMessageHeaderof the Terminal API request.
In an integration with payment terminals, use the terminal ID in the format[terminal model]-[serial number], for example,P400‑123456789. In a Mobile solution, use the installation ID of the SDK.
The unique identifier of the merchant account.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.

#### 200 - OK