# capital/1/overview

*Source: https://docs.adyen.com/api-explorer/capital/1/overview*

---

# Capital API
The Capital API provides endpoints for embeddingAdyen Capitalinto your marketplace or platform. With Capital, you can offer business financing to your users as grants. When a user receives a grant, they must repay the grant amount in a specified term, in addition to paying a fee for using this service.
With these endpoints, you can:
- Get available financing offers: You can get a list of offers with fixed amounts or a range of available financing for your users. Adyen configures the financing amount, the fee, and the repayment conditions for each offer. These configurations are based on proactive risk analyses that Adyen performs on your users.
- Make requests for grants: When a user selects a financing offer, you can make a request for the grant on their behalf.
- Get information about your grant account: Your grant account tracks the information of all grants in your marketplace or platform.

## Authentication
Each request made to the Capital API must be signed with an API key. Generate an API key in your Customer Area.
To connect to the API, add anX-API-Keyheader with the API key as the value, for example:

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...
```

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...
```

## Roles and permissions
To use the Capital API, your API credential must have the following roles:
- Balance_Platform_Capital_Configuration_Role
- Balance_Platform_Capital_Grant_Initiation_Role
Reach out to your Adyen contact to set up these roles.

## Going live
When going live, generate an API key in yourlive Customer Area. You can then use the API key to send requests tohttps://balanceplatform-api-live.adyen.com/capital/v{version}.