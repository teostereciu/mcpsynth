# Manage OAuth access tokens using the v1 APIs

*Source: https://developers.hubspot.com/docs/api-reference/legacy/authentication/oauth-tokens/v1/guide*

---

v1

# Manage OAuth access tokens using the v1 APIs

Get OAuth access and refresh tokens using the older v1 API endpoints.

Use the OAuth tokens API to generate and manage tokens needed for authorizing your app and its API requests. For example, you’ll need to use this API to fetch the initial access and refresh tokens during the app installation process. You’ll then use it to continue generating new tokens when the old ones expire. Before you can use these endpoints, you’ll need to first [create an app](/docs/apps/developer-platform/build-apps/create-an-app). A user will then need to install it into their account to initiate OAuth access.

A newer version of the OAuth API is available, which offers security improvements over the endpoints covered in this guide. Learn more about using the new [v3 OAuth API](/docs/api-reference/legacy/authentication/manage-oauth-tokens).

##

​

Initiating OAuth access

After you create your app, a user can install it into their HubSpot account using the install URL located in your app’s settings, which will include the `client_id`, `redirect_uri`, and `scopes` as query parameters. You may also include `optional_scopes` and `state`, if needed. After a user authorizes your app and installs it into their account, the redirect URL will be appended with a `code` value, which you can use to generate an access token and a refresh token. The access token will be used to authenticate requests that your app makes, while the refresh token will be used to get a new access token when the current one expires.

##

​

Generate initial access and refresh tokens

To get OAuth access and refresh tokens, make a URL-form encoded `POST` request to `/oauth/v1/token`. In the request body, you’ll specify various auth parameters, such as `client_id` and `client_secret`, along with the `code` passed back through the redirect URL. After a user authorizes your app, the redirect URL will be appended with a `code` value. Using this code, you’ll generate the initial access token and refresh token. Access tokens are short-lived, and you can check the `expires_in` parameter when generating an access token to determine its lifetime (in seconds). For example, your request may look similar to the following:


    curl --request POST \
      --url https://api.hubapi.com/oauth/v1/token \
      --header 'content-type: application/x-www-form-urlencoded' \
      --data 'grant_type=authorization_code&code=bcf33c57-dd7a-c7eb-4179-9241-e01bd&redirect_uri=https://www.domain.com/redirect&client_id=7933b042-0952-4e7d-a327dab-3dc&client_secret=7a572d8a-69bf-44c6-9a34-416aad3ad5'


Parameter| Type| Description
---|---|---
`grant_type`| String| Must be `authorization_code` for the request to generate initial access and refresh tokens.
`code`| String| The `code` returned in the redirect URL after the user installs the app.
`redirect_uri`| String| The app’s set redirect URL.
`client_id`| String| The app’s client ID.
`client_secret`| String| The app’s client secret.

In the response, you’ll receive the access token along with the refresh token, which you can use to refresh the access token. The `expires_in` field specifies how long the access token will last (in seconds).


    {
      "token_type": "bearer",
      "refresh_token": "1e8fbfb1-8e96-4826-8b8d-c8af73715",
      "access_token": "CIrToaiiMhIHAAEAQAAAARiO1ooBIOP0sgEokuLtAEaOaTFnToZ3VjUbtl46MAAAAEAAAAAgAAAAAAAAAAAACAAAAAAAOABAAAAAAAAAAAAAAAQAkIUVrptEzQ4hQHP89Eoahkq-p7dVIAWgBgAA",
      "expires_in": 1800
    }


##

​

Refresh an access token

Using a refresh token, you can generate a new access token by making a URL-form encoded `POST` request to `/oauth/v1/token`. In the request body, you’ll specify the `grant_type`, `client_id`, `client_secret`, and `refresh_token`.


    curl --request POST \
      --url https://api.hubapi.com/oauth/v1/token \
      --header 'content-type: application/x-www-form-urlencoded' \
      --data 'grant_type=refresh_token&refresh_token=1e8fbfb1-8e96-4826-8b8d-c8af73715&client_id=7933b042-0952-4e7d-a327dab-3dc&client_secret=7a572d8a-69bf-44c6-9a34-416aad3ad5'


Parameter| Type| Description
---|---|---
`grant_type`| String| Must be `refresh_token` for the request to generate new access tokens from the refresh token.
`refresh_token`| String| The refresh token value.
`client_id`| String| The app’s client ID.
`client_secret`| String| The app’s client secret.

##

​

Retrieve access token metadata

To get information about an OAuth access token, including the user that the token was created for and their corresponding Hub ID, make a `GET` request to `/oauth/v1/access-tokens/{token}`. You’ll receive a response containing information about the user’s access token and their HubSpot account.


    {
      "token": "CNaKSIHAAEAQAAAARiO1ooBIOP0sgEokuLtATIU5m7Kzmjj0ihJJuKFq1TcIiHCqwE6MAAAAEEAAAAAAAAAAgAIUfmerBenQwc07ZHXy6atYNNW8XCVKA25hMVIAWgBgAA",
      "user": "user@domain.com",
      "hub_domain": "meowmix.com",
      "scopes": ["oauth", "crm.objects.contacts.read", "crm.objects.contacts.write"],
      "signed_access_token": {
        "expiresAt": 1727190403926,
        "scopes": "AAEAAAAQ==",
        "hubId": 1234567,
        "userId": 293199,
        "appId": 111111,
        "signature": "5m7ihJJuKFq1TcIiHCqwE=",
        "scopeToScopeGroupPks": "AAAAQAAAAAAAAAACAAAAAAAAAAAAAIAAAAAAA4AEAAAAAAAAAAAAAABAC",
        "newSignature": "fme07ZHXy6atYNNW8XCU=",
        "hublet": "na1",
        "trialScopes": "",
        "trialScopeToScopeGroupPks": "",
        "isUserLevel": false
      },
      "hub_id": 1234567,
      "app_id": 111111,
      "expires_in": 1754,
      "user_id": 293199,
      "token_type": "access"
    }


**Please note:** HubSpot access tokens are expected to fluctuate in size over time, as updates will be made to the token’s encoded information. It’s recommended to allow for tokens to be up to 512 characters to account for any changes.

##

​

Delete a refresh token

If a user uninstalls your app, you can delete the refresh token by making a `DELETE` request to `/oauth/v1/refresh-tokens/{token}`. This will only delete the refresh token. Access tokens generated with the refresh token will not be deleted. Additionally, this will not uninstall the application from HubSpot accounts or inhibit data syncing between the app and account.

##

​

Error handling

When querying for access or refresh tokens, if an OAuth error occurs, the response will resemble the following:


    {
      "error": "invalid_grant",
      "error_description": "refresh token is invalid, expired or revoked",
      "status": "BAD_REFRESH_TOKEN",
      "message": "refresh token is invalid, expired or revoked"
    }


This response fully conforms to RFC 6749 of the OAuth 2.0 standard, which many OAuth libraries and tools expect. Note that the HubSpot-specific `status` and `message` fields that were included in previous versions of the OAuth token API endpoints are still available for backwards compatibility.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)