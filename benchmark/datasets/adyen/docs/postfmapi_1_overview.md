# postfmapi/1/overview

*Source: https://docs.adyen.com/api-explorer/postfmapi/1/overview*

---

# POS Terminal Management API (deprecated)
This API provides endpoints for managing your point-of-sale (POS) payment terminals. You can use the API to obtain information about a specific terminal, retrieve overviews of your terminals and stores, and assign terminals to a merchant account or store.
For more information, refer toClassic assign terminals.
From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate the management of your terminal fleet, use ourManagement API.

## Authentication
Each request to the Terminal Management API must be signed with an API key. For this, obtain an API Key from your Customer Area, as described inHow to get the API key. Then set this key to theX-API-Keyheader value, for example:

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: Your_API_key" \
...
```

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: Your_API_key" \
...
```
Note that when going live, you need to generate new web service user credentials to access thelive endpoints.

## Roles and permissions
To use the POS Terminal Management API, you need thePOS Terminal Management API roleadded to your API credential. Your Adyen contact will set up the roles for you.

## Versioning
Terminal Management API supportsversioningusing a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.
For example:

```
https://postfmapi-test.adyen.com/postfmapi/terminal/v1/getTerminalsUnderAccount
```

```
https://postfmapi-test.adyen.com/postfmapi/terminal/v1/getTerminalsUnderAccount
```
When using versioned endpoints, Boolean response values are returned in string format:"true"or"false".
If you omit the version from the endpoint URL, Boolean response values are returned like this:trueorfalse.

## Going live
To access the live endpoints, you need an API key from your live Customer Area.
Use this API key to make requests to:

```
https://postfmapi-live.adyen.com/postfmapi/terminal/v1
```

```
https://postfmapi-live.adyen.com/postfmapi/terminal/v1
```