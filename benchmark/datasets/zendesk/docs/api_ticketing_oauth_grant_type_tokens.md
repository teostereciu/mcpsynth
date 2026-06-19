# OAuth Tokens for Grant Types

*Source: https://developer.zendesk.com/api-reference/ticketing/oauth/grant_type_tokens/*

---

## On this page

  * [Authorization code grant type](/api-reference/ticketing/oauth/grant_type_tokens/#authorization-code-grant-type)
  * [Refresh token grant type](/api-reference/ticketing/oauth/grant_type_tokens/#refresh-token-grant-type)
  * [Client credentials grant type](/api-reference/ticketing/oauth/grant_type_tokens/#client-credentials-grant-type)
  * [JSON format](/api-reference/ticketing/oauth/grant_type_tokens/#json-format)
  * [Create Token for Grant Type](/api-reference/ticketing/oauth/grant_type_tokens/#create-token-for-grant-type)


# OAuth Tokens for Grant Types

## On this page

  * [Authorization code grant type](/api-reference/ticketing/oauth/grant_type_tokens/#authorization-code-grant-type)
  * [Refresh token grant type](/api-reference/ticketing/oauth/grant_type_tokens/#refresh-token-grant-type)
  * [Client credentials grant type](/api-reference/ticketing/oauth/grant_type_tokens/#client-credentials-grant-type)
  * [JSON format](/api-reference/ticketing/oauth/grant_type_tokens/#json-format)
  * [Create Token for Grant Type](/api-reference/ticketing/oauth/grant_type_tokens/#create-token-for-grant-type)


This API includes the Create Token for Grant Type endpoint which allows you to obtain access tokens for both the authorization code and the refresh token grant types.

For more information, see [Authorization code grant flow](https://support.zendesk.com/hc/en-us/articles/4408845965210#topic_jkc_dcm_dcc) and [Refresh token grant flow](https://support.zendesk.com/hc/en-us/articles/4408845965210) in Zendesk help.

If you're not working with grant types, use the [Create Token](/api-reference/ticketing/oauth/oauth_tokens#create-token) endpoint in the OAuth Tokens API. The two APIs don't share the same path, JSON format, or request parameters. However, both APIs return access tokens that can be used to [authenticate API requests](/api-reference/ticketing/introduction/#oauth-access-token).

### Authorization code grant type

The authorization code grant flow enables an application to obtain an access token on behalf of a user after the user successfully authenticates and grants permission. To initiate this flow, redirect the user to the authorization server's authorization endpoint, where they log in and authorize the application. After successful authorization, the server redirects the user back to the specified redirect URI with an `authorization_code`. The application then exchanges this authorization code for an access token by sending a request to the `/oauth/tokens` endpoint, including the `authorization_code`, `client_id`, and, if using PKCE, the `code_verifier`. This access token allows the application to access protected resources on behalf of the user. When using PKCE, the initial authorization request must also include the `code_challenge` and `code_challenge_method` parameters.

### Refresh token grant type

The refresh token grant type allows for refreshing an access token that has either expired or is about to expire. To generate a new OAuth access token, pass a `refresh_token` parameter to the `/oauth/tokens` endpoint using `grant_type: refresh_token`. This process returns a new access token and refresh token while invalidating the previous access and refresh tokens. Refresh tokens will be issued for all new OAuth token requests, but existing OAuth tokens cannot be refreshed.

The `authorization_code` and `refresh_token` grant types accept the `expires_in` and `refresh_token_expires_in` parameters in requests to the `/oauth/tokens` endpoint, allowing clients to set expiration times.

There is no default `expires_in` value to preserve current access token behavior. However, you can specify an `expires_in` value through the API when creating a token to set an expiration. The `refresh_token_expires_in` has a default value of 30 days, but can be adjusted through the API.

**Note** : The `refresh_token` flow does not impact Zendesk Integration Services (ZIS) flows. No mandatory token expirations are enforced that could disrupt ZIS functionality. Although you can set `expires_in` for testing in non-ZIS OAuth use cases, ZIS does not currently support or require this.

### Client credentials grant type

The OAuth client credentials grant type is intended only for confidential clients and enables creating an OAuth token using just the clientâs secret. To use this flow, send a request to the `/oauth/tokens` endpoint with `grant_type: client_credentials` and a valid `client_secret` parameter to generate a new access token. Unlike other authorization flows, this grant type does not return a refresh token and does not require user authorization. The tokenâs user will be the one associated with the client. You can optionally include an `expires_in` value to set the tokenâs expiration time in seconds. For security reasons, public clients are not allowed to use this grant type.

### JSON format

OAuth Tokens for Grant Types are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
access_token| string| true| false| The access token
expires_in| integer| false| false| Number of seconds the access token is valid. Must be more than 300 seconds (5 minutes) and less than 172,800 seconds (2 days), or less than `refresh_token_expires_in`, whichever is the smallest. Defaults to null
refresh_token| string| true| false| The refresh token
refresh_token_expires_in| integer| false| false| Number of seconds the refresh token is valid. Must be more than 604,800 seconds (7 days) or `expires_in` (if given), and less than 7,776,000 seconds (90 days). Defaults to 2,592,000 seconds (30 days)
scope| string| true| false| The valid scopes for this token. See Scope below
token_type| string| true| false| Type of the access token, for example "bearer"

#### Example


    {  "access_token": "gErypPlm4dOVgGRvA1ZzMH5MQ3nLo8bo",  "expires_in": 86400,  "refresh_token": "af3t24tfj34h43s...",  "refresh_token_expires_in": 604800,  "scope": "read",  "token_type": "bearer"}

### Create Token for Grant Type

  * `POST /oauth/tokens`


Returns an OAuth access token in exchange for an [authorization code](https://support.zendesk.com/hc/en-us/articles/203663836#topic_pvr_ncl_1l) valid for 120 seconds.

Using a Zendesk username and password to gain an OAuth access token (password grant type flow) has been deprecated and is highly discouraged.

An access token can be revoked. Use the [OAuth Tokens API](/api-reference/ticketing/oauth/oauth_tokens) to list, show, or revoke tokens.

#### Request parameters

The POST request takes the following parameters, which must be formatted as JSON:

Name| Description
---|---
grant_type| "authorization_code", "refresh_token", or "client_credentials"
code| Authorization grant flow only. The authorization code you received from Zendesk after the user granted access. See [Handle the user's authorization decision](https://support.zendesk.com/hc/en-us/articles/203663836#topic_tfc_cdl_1l) in Help Center
client_id| The **Unique Identifier** specified in an OAuth client in the Support admin interface (**Apps and integrations** > **APIs** > **OAuth clients**). See [Registering your application with Zendesk](https://support.zendesk.com/hc/en-us/articles/203663836#topic_s21_lfs_qk)
client_secret| The **Secret** specified in an OAuth client in the Support admin interface (**Apps and integrations** > **APIs** > **OAuth clients**). See [Registering your application with Zendesk](https://support.zendesk.com/hc/en-us/articles/203663836#topic_s21_lfs_qk)
redirect_uri| Authorization grant flow only. The redirect URL you specified when you sent the user to the Zendesk authorization page. For ID purposes only. See [Send the user to the Zendesk authorization page](https://support.zendesk.com/hc/en-us/articles/203663836#topic_qk3_d3s_qk)
scope| Valid scope for this token. A string of space-separated values. See Scope below
expires_in| Number of seconds the access token is valid. Must be more than 300 seconds (5 minutes) and less than 172,800 seconds (2 days), or less than `refresh_token_expires_in`, whichever is the smallest. Defaults to null
refresh_token_expires_in| Number of seconds the refresh token is valid. Must be more than 604,800 seconds (7 days) or `expires_in` (if given), and less than 7,776,000 seconds (90 days). Defaults to 2,592,000 seconds (30 days)
refresh_token| The refresh token

**Example Node.js authorization code grant flow**


    const tokenResponse = await axios.post(  `https://${ZENDESK_SUBDOMAIN}.zendesk.com/oauth/tokens`,  {    grant_type: "authorization_code",    code: req.query.code,    client_id: ZENDESK_CLIENT_ID,    redirect_uri: REDIRECT_URI_PKCE,    scope: "read write",    code_verifier: CODE_VERIFIER,    expires_in: 86400,    refresh_token_expires_in: 604800,  },  { headers: { "Content-Type": "application/json" } });

**Example Node.js refresh token grant flow**


    const tokenResponse = await axios.post(  `https://${ZENDESK_SUBDOMAIN}.zendesk.com/oauth/tokens`,  {    grant_type: "refresh_token",    refresh_token: refresh_token,    client_id: ZENDESK_CLIENT_ID,    client_secret: ZENDESK_CLIENT_SECRET,    scopes: "tickets:write",    expires_in: 86400,    refresh_token_expires_in: 604800,  },  { headers: { "Content-Type": "application/json" } });

#### Scope

You must specify a scope to control the app's access to Zendesk resources. The "read" scope gives access to GET endpoints. It includes permission to sideload related resources. The "write" scope gives access to POST, PUT, and DELETE endpoints for creating, updating, and deleting resources.

**Note** : Don't confuse the **scope** parameter (singular) with the **scopes** parameter (plural) for non-grant-type tokens described in [OAuth Tokens](/api-reference/ticketing/oauth/oauth_tokens).

The "impersonate" scope allows a Zendesk admin to make requests on behalf of end users. See [Making API requests on behalf of end users](/documentation/ticketing/using-the-zendesk-api/making-api-requests-on-behalf-of-end-users/).

**Broad scopes**

The following parameter gives read access to all resources:

`"scope": "read"`

The following parameter gives read and write access to all resources:

`"scope": "read write"`

**Resource-specific scopes**

You can fine-tune the scope of the following resources:

  * [tickets](/api-reference/ticketing/tickets/tickets/)
  * [users](/api-reference/ticketing/users/users/)
  * [audit logs (read only)](/api-reference/ticketing/account-configuration/audit_logs/)
  * [organizations](/api-reference/ticketing/organizations/organizations/)
  * [help center resources](/api-reference/help_center/help-center-api/introduction/)
  * [apps](/api-reference/apps/introduction/)
  * [triggers](/api-reference/ticketing/business-rules/triggers/)
  * [automations](/api-reference/ticketing/business-rules/automations/)
  * [targets](/api-reference/ticketing/targets/targets/)
  * [webhooks](/api-reference/webhooks/introduction/)


The syntax is as follows:

`"scope": "resource:scope"`

For example, the following parameter restricts the scope to only reading tickets:

`"scope": "tickets:read"`

To give read and write access to a resource, specify both scopes:

`"scope": "users:read users:write"`

To give write access only to one resource, such as organizations, and read access to everything else:

`"scope": "organizations:write read"`

**Restrictions and limitations**

A "Forbidden" error can occur either because the token is missing required scopes for an endpoint, or because the requested scopes were provided in an invalid format.

  * The resources defined in the scope must align with the resources accessed by the API endpoint. If the token lacks the required scope for an endpoint, the request will fail with a "Forbidden" error.

  * The endpoint can return an access token even if you specify an invalid scope such as `"scope": ["read", "write"]`. Any request you make with the token will return a "Forbidden" error.


#### Tokens for Implicit Grant Type

The implicit grant flow has been deprecated. It's considered insecure and its use is highly discouraged.

#### Code Samples

**curl**

Authorization code grant


    curl https://{subdomain}.zendesk.com/oauth/tokens \  -H "Content-Type: application/json" \  -d '{"grant_type": "authorization_code", "code": "7xqwtlf3rrdj8uyeb1yf",    "client_id": "acme_rockets", "client_secret": "77f9931747b63f720f9fbc6",    "redirect_uri": "https://www.example.com/app/grant_decision",    "scope": "organizations:write read" }' \  -X POST

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://support.zendesk.com/oauth/tokens"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://support.zendesk.com/oauth/tokens")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://support.zendesk.com/oauth/tokens',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://support.zendesk.com/oauth/tokens"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://support.zendesk.com/oauth/tokens")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "access_token": "gErypPlm4dOVgGRvA1ZzMH5MQ3nLo8bo",  "scope": "organizations:write read",  "token_type": "bearer"}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)