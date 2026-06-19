# Remote Authentications

*Source: https://developer.zendesk.com/api-reference/ticketing/account-configuration/remote_authentications/*

---

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/remote_authentications/#json-format)
  * [List Remote Authentications](/api-reference/ticketing/account-configuration/remote_authentications/#list-remote-authentications)


# Remote Authentications

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/remote_authentications/#json-format)
  * [List Remote Authentications](/api-reference/ticketing/account-configuration/remote_authentications/#list-remote-authentications)


Remote authentications are enterprise single sign-on (SSO) options that let team members and end users authenticate through an external identity provider.

The API supports OAuth tokens scoped for "security:read". See [Scopes](/api-reference/ticketing/oauth/oauth_tokens/#scopes).

### JSON format

Remote Authentications are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
agent| boolean| false| true| If true, the method is used for the team member remote authentication
agent_primary| boolean| false| true| If team members for sign-in are redirected to a remote authentication, this is the default method shown to a team member
auth_flow| string| false| false| Authentication mode. Allowed values are "PKCE", or "authorization_code".
auth_mode| integer| false| true| The numeric representation of remote authentication type. Allowed values are '\x02', '\x03', or '\x04'.
auth_mode_name| string| true| false| The string representation of remote authentication type. Allowed values are "saml", "jwt", or "oidc".
auth_url| string| false| false| For the "oidc" auth mode only. The authorization endpoint to use for the request
auto_discovery| boolean| false| false| For the "oidc" auth mode only. When turned on, Zendesk will automatically extract the configuration details from the OIDC Configuration Document. Only the Issuer URL and Authentication Mode need to be provided
can_display_button_to_end_users| boolean| false| true| If users can choose how they sign in, this remote authentication method appears as an option when it's active
can_display_button_to_team_members| boolean| false| true| If team members can choose how they sign in, this remote authentication method appears as an option when it's active
client_id| string| false| false| For the "oidc" auth mode only.
end_user| boolean| false| true| If true, the method is used for the end-user remote authentication
end_user_primary| boolean| false| true| If end users for sign-in are redirected to a remote authentication, this is the default method shown to an end user
fingerprint| string| false| false| For the "saml" auth mode only. The SHA-256 certificate fingerprint.
id| integer| true| false| Uniquely identifies a remote authentication. Automatically assigned on creation
ip_ranges| string| false| false| Requests from these IP ranges will always be routed via remote authentication. Requests from IP addresses outside these ranges will be routed to the normal sign-in form. When this is blank, all requests are routed through remote authentication. An IP range is in the format n.n.n.n, where n is a number or an asterisk (*) wild card. Multiple IP ranges are separated with spaces
is_active| boolean| true| false| If true, the method is enabled for end users or team members
issuer_url| string| false| false| For the "oidc" auth mode only. This is the URL that is used as the logical identifier for your provider's connection
jwks_url| string| false| false| For the "oidc" auth mode only. This is the URL that returns the provider's JSON Web Key Set
label| string| false| false| The sign-in button label
masked_client_secret| string| false| false| For the "oidc" auth mode only.
masked_secret| string| false| false| For the "jwt" auth mode only. The token is a shared secret between you and Zendesk. It must never be publicized
name| string| false| true| The name of the remote configuration. It's good to use something recognizable like the identity provider's name
priority| integer| false| false|
remote_login_url| string| false| true| The URL that Zendesk invokes to redirect users to the identity provider
remote_logout_url| string| false| true| The URL that Zendesk uses to redirect users after they sign out
scope| string| false| false| For the "oidc" auth mode only. These are the user details your account can access, like name and email address. Supported scopes within the OIDC standard include `openid`, `profile`, `email`, `address`, and `phone`. It must contain at least `openid` and `email`. Scopes are separated with spaces
token_url| string| false| false| For the "oidc" auth mode only. Your account uses this URL to request access tokens for users
update_external_ids| boolean| false| false| For the "jwt" auth mode only. When enabled, the external id of the user being signed in can be updated. This only happens when a user with the external id is not found, but the user's email address is found. The external id is unique for an account. Users without an external id will have one added if it is present in the authentication request
user_info_url| string| false| false| For the "oidc" auth mode only. This the URL that returns Claims about the authenticated user

#### Enterprise SSO options

There are three enterprise SSO options available in Zendesk:

Name| `auth_mode`| `auth_mode_name`| Description
---|---|---|---
Secure Assertion Markup Language (SAML)| `2`| `saml`| SAML is supported by many identity provider services, such as Okta, OneLogin, Active Directory, and LDAP
JSON Web Token (JWT)| `3`| `jwt`| Credentials and user information is sent in JSON format encrypted using a Zendesk Shared Secret
OpenID Connect (OIDC)| `4`| `oidc`| Built on the OAuth 2.0 framework, OIDC uses ID tokens to verify the identity of users based on the authentication performed by an authorization server

#### Example


    {  "agent": false,  "agent_primary": false,  "auth_mode": 3,  "auth_mode_name": "jwt",  "can_display_button_to_end_users": false,  "can_display_button_to_team_members": false,  "end_user": true,  "end_user_primary": false,  "id": 7949169175677,  "ip_ranges": null,  "is_active": true,  "label": "",  "masked_secret": "SRT2hj******************************************",  "name": "Testing JWT",  "priority": 1,  "remote_login_url": "https://example.com/sso/login",  "remote_logout_url": "https://example.zendesk.com/sso/logout",  "update_external_ids": false}

### List Remote Authentications

  * `GET /api/v2/remote_authentications`


#### Allowed For

  * Admins


#### Code Samples

**cURL**


    # List Remote Authenticationscurl https://{subdomain}.zendesk.com/api/v2/remote_authentications \   -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/remote_authentications"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/remote_authentications")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/remote_authentications',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/remote_authentications"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/remote_authentications")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "remote_authentications": [    {      "agent": false,      "agent_primary": false,      "auth_mode": 3,      "auth_mode_name": "jwt",      "can_display_button_to_end_users": false,      "can_display_button_to_team_members": false,      "end_user": true,      "end_user_primary": false,      "id": 1234,      "ip_ranges": null,      "is_active": true,      "label": "MyJWT",      "masked_secret": "16egqn******************************************",      "name": "JWT Provider",      "priority": 1,      "remote_login_url": "https://example.com/jwt/login",      "remote_logout_url": "https://example.zendesk.com/jwt/logout",      "update_external_ids": false    },    {      "agent": false,      "agent_primary": false,      "auth_mode": 2,      "auth_mode_name": "saml",      "can_display_button_to_end_users": false,      "can_display_button_to_team_members": false,      "end_user": false,      "end_user_primary": false,      "fingerprint": "asdfghasdfgasdfgasdfgasdfgasdfgasdfgasdfg",      "id": 5678,      "ip_ranges": null,      "is_active": false,      "label": "MySAML",      "name": "SAML Provider",      "priority": 2,      "remote_login_url": "https://example.com/saml/login",      "remote_logout_url": "https://example.zendesk.com/saml/logout"    },    {      "agent": false,      "agent_primary": false,      "auth_flow": "PKCE",      "auth_mode": 4,      "auth_mode_name": "oidc",      "auth_url": "https://example.com/auth",      "auto_discovery": false,      "can_display_button_to_end_users": true,      "can_display_button_to_team_members": true,      "client_id": "abcdef",      "end_user": false,      "end_user_primary": false,      "id": 9012,      "ip_ranges": null,      "is_active": false,      "issuer_url": "https://example.com/issuer",      "jwks_url": "https://example.com/jwks",      "label": "MyOIDC",      "masked_client_secret": "SRT2hj******************************************",      "name": "OIDC",      "priority": 1,      "remote_login_url": "",      "remote_logout_url": "",      "scope": "openid email",      "token_url": "https://example.com/token",      "user_info_url": "https://example.com/user"    }  ]}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)