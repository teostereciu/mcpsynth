# terminal-api/1/overview

*Source: https://docs.adyen.com/api-explorer/terminal-api/1/overview*

---

# Adyen Terminal API
The AdyenTerminal APIlets you make payments, issue refunds, collect shopper information, and perform other shopper-device interactions using a payment terminal supplied by Adyen. The Terminal API is also used for transactions inAdyen Mobile solutions.

## API structure
The architecture of Terminal API is determined by thenexo Sale to POI Protocol Specifications.
A Terminal API request is a JSON message consisting of aSaleToPOIRequestobject with:
- MessageHeader: identifies the type of transaction, the terminal or Mobile SDK instance being used, and unique transaction identifiers.
- Request body: content depending on the type of transaction or operation, for example, aPaymentRequest.

```
MessageHeader
```
A Terminal API response is a JSON message consisting of aSaletoPOIResponsewith:
- MessageHeader: echoes the values provided in the request, except forMessageType, which is alwaysResponse.
- Response body: content depending on the type of transaction or operation, for example, aPaymentResponse.

```
MessageHeader
```

## Sending and receiving
In an integration with Ayden payment terminals, you can send and receive Terminal API messages in the following ways:
- Local communications: using your local network, your POS system sends the request directly to the IP address of the terminal, and receives the result synchronously.
- Cloud communications: using the internet to access the cloud, your POS system sends the request to an Adyen endpoint, and Adyen forwards the request to the terminal. Your POS system either keeps the connection open and receives the response synchronously, or closes the connection and receives the response asynchronously in an event notification.

## Using local communications
To learn how to set up and protect local communications, refer toBuilding a local integration.

## Endpoints for cloud communications
If your POS system is cloud-based, you POST your Terminal API requests to aCloud device APIendpoint, using path and query parameters to identify the device that you want to send the request to.
- If your POS system is designed to keep the connection open to wait for the response, use the endpoints ending in/sync.
- If your POS system is designed to close the connection so that it can initiate a new request, use the endpoints ending in/async.

### Test endpoints
- https://device-api-test.adyen.com/v1/merchants/{merchantAccount}/devices/{deviceId}/sync
- https://device-api-test.adyen.com/v1/merchants/{merchantAccount}/devices/{deviceId}/async

### Live endpoints
The live endpoints differ per region. In addition to using a regional endpoint, you must select the geographically closest data center in your live Customer Area.
Australia
- https://device-api-live-au.adyen.com/v1/merchants/{merchantId}/devices/{deviceId}/sync
- https://device-api-live-au.adyen.com/v1/merchants/{merchantId}/devices/{deviceId}/async
East Asia
- https://device-api-live-apse.adyen.com/v1/merchants/{merchantId}/devices/{deviceId}/sync
- https://device-api-live-apse.adyen.com/v1/merchants/{merchantId}/devices/{deviceId}/async
Europe
- https://device-api-live.adyen.com/v1/merchants/{merchantId}/devices/{deviceId}/sync
- https://device-api-live.adyen.com/v1/merchants/{merchantId}/devices/{deviceId}/async
United States
- https://device-api-live-us.adyen.com/v1/merchants/{merchantId}/devices/{deviceId}/sync
- https://device-api-live-us.adyen.com/v1/merchants/{merchantId}/devices/{deviceId}/async

### Old endpoints
If you currently use endpoints with a base URL that includesterminal-api, we strongly recommend migrating to Cloud device API endpoints, for the following reasons:
- When using Cloud device API, the API logs in the Customer Area include the Terminal API requests and responses.
- Cloud device API endpoints offer technical advantages such as versioning and better routing.
- Future enhancements and features will be based on Cloud device API.
There will be no future development on the old endpoints, but we continue to support them.
Old test endpoints:
- https://terminal-api-test.adyen.com/syncandhttps://terminal-api-test.adyen.com/async
Old live endpoints Australia:
- https://terminal-api-live-au.adyen.com/syncandhttps://terminal-api-live-au.adyen.com/async
Old live endpoints East Asia:
- https://terminal-api-live-apse.adyen.com/syncandhttps://terminal-api-live-apse.adyen.com/async
Old live endpoints Europe:
- https://terminal-api-live.adyen.com/syncandhttps://terminal-api-live.adyen.com/async
Old live endpoints United States:
- https://terminal-api-live-us.adyen.com/syncandhttps://terminal-api-live-us.adyen.com/async

## Authentication for cloud communications
Each request to aCloud device APIendpoint must be signed with an API key that has theCloud Device API role.Generate your API Keyin the Customer Area and set this key to theX-API-Keyheader value of the Cloud device API request.
When going live, generate a new API key in the live Customer Area.

## Available Terminal API requests