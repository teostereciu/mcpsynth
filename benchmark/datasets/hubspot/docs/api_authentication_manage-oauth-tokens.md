# Manage OAuth access tokens using the v3 APIs

*Source: https://developers.hubspot.com/docs/api-reference/legacy/authentication/manage-oauth-tokens*

---

Authentication

# Manage OAuth access tokens using the v3 APIs

Learn how to use the new v3 OAuth endpoints to manage access and refresh tokens to securely perform CRUD actions with HubSpot APIs.

The new v3 OAuth endpoints provide security improvements over the previous [v1 endpoints](/docs/api-reference/legacy/authentication/oauth-tokens/v1/guide), while still maintaining the same functionality to leverage OAuth 2.1 to manage access and refresh tokens. Each of the v3 endpoints require that parameters are included in the request body, which differs from how the corresponding values were included as query parameters in the v1 endpoints. This new approach ensures that sensitive data such as your app’s client ID and secret don’t inadvertently appear in server logs or other persistent logging in your app’s backend services. Before you can use these endpoints, you’ll have to [create an app](/docs/apps/developer-platform/build-apps/create-an-app). A user will then need to install it into their account to initiate OAuth access. Review the sections below on how to use the new v3 endpoints to initiate OAuth access, manage access tokens, and retrieve token metadata.

##

​

Token types

The OAuth authorization flow involves three distinct token types:

  * **Authorization code:** a temporary, single-use code that’s provided in the redirect URL as a query parameter when the user approves the installation of your app. Your app then has a short window to exchange it for an access token and a refresh token, after which the authorization code cannot be reused.
  * **Access token:** your app’s authentication credential used for every API request made on behalf of the user and the account where they installed your app. This token is provided as a _Bearer_ token in the request, and expires after 30 minutes.
  * **Refresh token:** your app’s long-term authentication credential that you can use to generate a new access token after the previous one expires.

Check out the blog post linked below for guidance on how to cache and auto-refresh access tokens:

##

​

Initiate OAuth access

After you create your app, a user can install it into their HubSpot account using the install URL located in your [app’s settings](/docs/apps/developer-platform/build-apps/manage-apps-in-hubspot), which will include the `client_id`, `redirect_uri`, and `scopes` as query parameters. You may also include `optional_scopes` and `state`, if needed. For example, the Node.js code block below demonstrates how to construct this authorization URL:


    const authorizationUrl =
      'https://app.hubspot.com/oauth/authorize' +
      `?client_id=${encodeURIComponent(CLIENT_ID)}` + // app's client ID
      `&scope=${encodeURIComponent(SCOPES)}` + // scopes being requested by the app
      `&redirect_uri=${encodeURIComponent(REDIRECT_URI)}`; // where to send the user after the consent page


After a user authorizes your app and installs it into their account, the redirect URL will be appended with a `code` query parameter, which you can use to generate an access token and a refresh token. The access token will be used to authenticate requests that your app makes, while the refresh token will be used to get a new access token when the current one expires.

##

​

Generate initial access and refresh tokens

After a user authorizes your app, the response will include a `code` value as a query parameter. Using this code, you’ll generate the initial access token and refresh token. Access tokens are short-lived (30 minutes), and you can check the `expires_in` parameter when generating an access token to determine its lifetime (in seconds). To get OAuth access and refresh tokens, make a URL-form encoded `POST` request to `/oauth/v3/token`. In the request body, you’ll specify various auth parameters, such as `client_id` and `client_secret`, along with the `code` passed back through the redirect URL. For example, your request may look similar to the following:


    curl --request POST \
      --url https://api.hubspot.com/oauth/v3/token \
      --header 'content-type: application/x-www-form-urlencoded' \
      --data client_id=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee \
      --data client_secret=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee \
      --data code=na1-aaaa-bbbb-cccc-dddd-eeeeeeeeeeee \
      --data grant_type=authorization_code \
      --data redirect_uri=http://localhost:3000/oauth-callback


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
      "refresh_token": "na1-aaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "access_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "hub_id": 1234567,
      "scopes": [
        "oauth",
        "crm.objects.contacts.write",
        "crm.objects.contacts.read"
      ],
      "expires_in": 1800
    }


##

​

Refresh an access token

Using a refresh token, you can generate a new access token by making a URL-form encoded `POST` request to `/oauth/v3/token`. In the request body, you’ll specify the `grant_type`, `client_id`, `client_secret`, and `refresh_token`.


    curl --request POST \
      --url https://api.hubspot.com/oauth/v3/token \
      --header 'content-type: application/x-www-form-urlencoded' \
      --data client_id=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee \
      --data client_secret=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee \
      --data refresh_token=na1-aaaa-bbbb-cccc-dddd-eeeeeeeeeeee \
      --data grant_type=refresh_token


Parameter| Type| Description
---|---|---
`grant_type`| String| Must be `refresh_token` for the request to generate new access tokens from the refresh token.
`refresh_token`| String| The refresh token value.
`client_id`| String| The app’s client ID.
`client_secret`| String| The app’s client secret.

##

​

Retrieve access token metadata

To get information about an OAuth access token, including the user that the token was created for and their corresponding Hub ID, make a `POST` request to `/oauth/v3/token/introspect`, providing the following form URL-encoded properties in the request body:

Property| Type| Description
---|---|---
`client_id`| String| The app’s client ID.
`client_secret`| String| The app’s client secret.
`token_type_hint`| String| The type of token you’re querying, which can be either `access_token` or `refresh_token`.
`refresh_token`| String| If you specified `refresh_token` as the `token_type_hint`, then provide the `refresh_token` as an additional property in your request.
`access_token`| String| If you specified `access_token` as the `token_type_hint`, then provide the `access_token` as an additional property in your request.

For example, if you wanted to query for details about the `refresh_token` of `na1-aaaa-bbbb-cccc-dddd-eeeeeeeeeeee`, your form URL-encoded request body would include:


    {
      "client_id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "client_secret": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "token_type_hint": "refresh_token",
      "refresh_token": "na1-aaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
    }


You’ll receive a response containing information about the user’s access token and their HubSpot account. The code blocks below provide example responses when querying for both `access_token` and `refresh_token` grant types.

##

  * Access token metadata

  * Refresh token metadata


      {
        "active": true,
        "token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "hub_id": 1234567,
        "user_id": 222222,
        "client_id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        "app_id": 1234444,
        "user": "jdoe@hubspot.com",
        "hub_domain": "example.com",
        "scopes": [
          "oauth",
          "crm.objects.contacts.read",
          "crm.objects.contacts.write"
        ],
        "signed_access_token": {
          "expiresAt": 1769213087721,
          "scopes": "xxxxxxxxxxxxxxxxxxxxxxxx",
          "hubId": 1234567,
          "userId": 222222,
          "appId": 1234444,
          "signature": "xxxxxxxxxxxxxxxxxxxxxxxx",
          "scopeToScopeGroupPks": "xxxxxxxxxxxxxxxxxxxxxxxx",
          "newSignature": "xxxxxxxxxxxxxxxxxxxxxxxx",
          "hublet": "na1",
          "trialScopes": "",
          "trialScopeToScopeGroupPks": "",
          "isUserLevel": false,
          "isPrivateDistribution": true
        },
        "expires_in": 1789,
        "is_private_distribution": true,
        "token_use": "access_token",
        "token_type": "Bearer"
      }


      {
        "active": true,
        "token": "na1-aaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        "hub_id": 1234567,
        "user_id": 222222,
        "client_id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        "app_id": 1234444,
        "user": "jdoe@hubspot.com",
        "hub_domain": "example.com",
        "scopes": [
          "crm.objects.contacts.write",
          "oauth",
          "crm.objects.contacts.read"
        ],
        "token_use": "refresh_token",
        "token_type": "Bearer"
      }


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


This response fully conforms to [RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749) of the OAuth 2.0 standard, which many OAuth libraries and tools expect. Note that the HubSpot-specific `status` and `message` fields that were included in previous versions of the OAuth token API endpoints are still available for backwards compatibility.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)