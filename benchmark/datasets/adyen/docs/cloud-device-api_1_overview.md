# cloud-device-api/1/overview

*Source: https://docs.adyen.com/api-explorer/cloud-device-api/1/overview*

---

# Cloud device API
With the Cloud device API you can:
- Send Terminal API requests to a cloud endpoint.
You can use this communication method when it is not an option to send Terminal API requests over your local network directly to a payment terminal.
- Check the cloud connectionof a payment terminal or of a device used in a Mobile solution for in-person payments.

## Authentication
Each request to the Cloud device API must be signed with an API key that has theCloud Device APIrole.Generate your API keyin your test Customer Area and then set this key to the X-API-Key header value. For example:

```
curl
-H 'Content-Type: application/json' 
-H 'X-API-Key: ADYEN_API_KEY' 
...
```

```
curl
-H 'Content-Type: application/json' 
-H 'X-API-Key: ADYEN_API_KEY' 
...
```

## Usage with Terminal API
When usingcloud communicationsfor sending and receivingTerminal API requests, your POS system uses the internet to access the cloud and send your Terminal API request to Adyen. Adyen then forwards the request to the payment device.
The Cloud device API has different endpoints for synchronous or asynchronous cloud communications:
- If your POS system is designed to keep the connection open to wait for the response, use the endpoints ending in/sync.In the test environment the endpoint for synchronous communication ishttps://device-api-test.adyen.com/v1/merchants/{merchantAccount}/devices/{deviceId}/sync
- If your POS system is designed to close the connection so that it can initiate a new request, use the endpoints ending in/async.
You will then receive the Terminal API response asynchronously in an event notification, which is sent as a webhook to an endpoint set up by you.In the test environment the endpoint for asynchronous communication ishttps://device-api-test.adyen.com/v1/merchants/{merchantAccount}/devices/{deviceId}/async

## Going live
To access the live endpoints, you must generate a new API key with theCloud Device APIrole in your live Customer Area.
You must use the data center and live endpoint that is geographically closest to your location:
- In your Customer Area, go toDevelopers>API URLs>Select a data centerand select the closest data center.
- Switch to the live endpoint that is geographically closest to your location. See the base URLs below.

### Australia:
https://device-api-live-au.adyen.com

### East Asia:
https://device-api-live-apse.adyen.com

### Europe:
https://device-api-live.adyen.com

### United States:
https://device-api-live-us.adyen.com

## Methods