# Security Settings

*Source: https://developer.zendesk.com/api-reference/ticketing/account-configuration/security_settings/*

---

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/security_settings/#json-format)
  * [Show Security Settings](/api-reference/ticketing/account-configuration/security_settings/#show-security-settings)


# Security Settings

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/security_settings/#json-format)
  * [Show Security Settings](/api-reference/ticketing/account-configuration/security_settings/#show-security-settings)


Security settings describe how team members and end users access a Zendesk account and ensure all private information is protected.

The API supports OAuth tokens scoped for "security:read". See [Scopes](/api-reference/ticketing/oauth/oauth_tokens/#scopes).

### JSON format

Security Settings are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
admins_can_set_user_passwords| boolean| false| false| If administrators are allowed to set passwords for users. When disabled, administrators can only reset passwords
agent_session_timeout| integer| false| false| The period of inactivity in minutes, before a team member is automatically signed out
assumable| boolean| false| false| If account assumption is enabled
assumable_account_type| boolean| false| false| Indicates if an account is always assumable, based on account type (e.g. always true for a trial account)
assumption_duration| string| false| false| Describes how long the account can be assumed. Allowed values are "off", "day", "week", "month", "year", or "always".
assumption_expiration| string| false| false| The time when assumption option expires
authentication| object| false| false| Describes how users authenticate. See Authentication
csp_blocking_enabled| boolean| false| false| If Content Security Policy blocking is enabled
email_agent_when_sensitive_fields_changed| boolean| false| false| If a notification is sent on password change for admins, agents and end users
end_user_session_timeout| integer| false| false| The period of inactivity in minutes, before an end user is automatically signed out
ip| object| false| false| Describes IP addresses restrictions. See IP Restrictions
maximum_session_duration| integer| false| false| The maximum session duration, which is the maximum amount of time in minutes a team member can stay signed in. The session will expire after this duration or the inactivity timeout
maximum_session_duration_enabled| boolean| false| false| If maximum session duration for team members is enabled
mobile_app_access| boolean| false| false| If admins and agents can use the Zendesk Support mobile app
mobile_app_session_timeout| integer| false| false| The period of inactivity in minutes, before a mobile app user gets signed out
two_factor_last_update| string| false| false| The time when the two-factor authentication setting was last updated

#### Authentication

Name| Type| Description
---|---|---
agent| object| Describes authentication for a team member. See User Role Authentication
end_user| object| Describes authentication for a end user. See User Role Authentication

#### Example


    {  "authentication": {    "agent": {      "security_policy_id": 100,      "security_policy_name": "low",      "google_login": false,      "office_365_login": false,      "zendesk_login": true,      "remote_login": false,      "enforce_sso": false,      "remote_bypass": 2,      "password": {        "password_history_length": null,        "password_length": 5,        "password_complexity": 0,        "password_in_mixed_case": false,        "failed_attempts_allowed": 10,        "max_sequence": null,        "disallow_local_part_from_email": false,        "password_duration": null      },      "sso_auto_redirect": false,      "primary_external_auth": null,      "office_365_enforce_tid": false,      "office_365_allowed_tids": ""    },    "end_user": {      "security_policy_id": 100,      "security_policy_name": "low",      "office_365_login": false,      "zendesk_login": true,      "remote_login": false,      "facebook_login": false,      "enforce_sso": false,      "sso_auto_redirect": false,      "primary_external_auth": null    }  }}

#### User Role Authentication

Name| Type| Nullable| Description
---|---|---|---
security_policy_id| integer| | The ID of the password security policy. See Security Policies
security_policy_name| string| | The name of the password security policy. See Security Policies
google_login| boolean| | If true, Google SSO is enabled
office_365_login| boolean| | If true, Microsoft SSO is enabled
zendesk_login| boolean| | If true, users can sign in with an email and password
remote_login| boolean| | If true, users can sign in using enterprise SSO
enforce_sso| boolean| | If true, email and password logins are disabled; users can sign in using SSO methods
sso_auto_redirect| boolean| | If true, for more than one SSO method active, user goes to primary SSO; if false, user can select any active authentication method
primary_external_auth| string| yes| Defines the primary SSO when "sso_auto_redirect" is true. Possible values are: "google", "facebook", "office_365" and "remote"
two_factor_enforce| boolean| | If true, requires users to use 2FA when signing in

##### For Team Mebers

Name| Type| Description
---|---|---
password| object| Defines custome security level properties. See Custom Security Policy
office_365_enforce_tid| boolean|
office_365_allowed_tids| string| Allowed tenant IDs from the Microsoft Entra ID portal. Multiple tenant IDs are separated with spaces
remote_bypass| integer| If the selected SSO service is interrupted, it says who can still access the account by requesting a one-time access link. Possible values are: 1 --- the account owner only; 2 --- all admins
remote_bypass_name| string| If the selected SSO service is interrupted, it says who can still access the account by requesting a one-time access link. Possible values are: "owner" --- the account owner only; "admins" --- all admins

##### For End Users

Name| Type| Description
---|---|---
facebook_login| boolean| If true, Facebook SSO is enabled

#### Security Policies

Many organizations require complex passwords as part of their security policies. Security levels differ by the following password requirements:

  * number of previous passwords to reject
  * minimum length
  * if must include numbers and special characters
  * if must include letters in mixed case
  * password expiration
  * number of failed attempts until lockout
  * max number of consecutive letters or numbers
  * if password can resemble an email


Zendesk strongly suggests setting the Recommended password security level. The Low, Medium and High password security levels have lower security requirements. The "Custom" security level is available only for team members. For more information, see [About password security levels](https://support.zendesk.com/hc/en-us/articles/4408822149018-Setting-the-password-security-level#topic_j41_j4r_2j) in Zendesk help.

Name| `security_policy_id`| `security_policy_name`
---|---|---
Low| 100| `low`
Medium| 200| `medium`
High| 300| `high`
Recommended| 350| `recommended`
Custom| 400| `custom`

#### Custom Security Policy

Name| Type| Nullable| Description
---|---|---|---
password_history_length| integer| yes| Number of previous passwords to reject. When unset, it means there is no limit
password_length| integer| | Minimum password length
password_complexity| integer| | If password must include numbers and special characters. Possible values are: 0 --- No; 1 --- Numbers only; 2 --- Numbers and special characters
password_in_mixed_case| boolean| | If password must include letters in mixed case
failed_attempts_allowed| integer| | Number of failed login attempts until lockout
max_sequence| integer| yes| Max number of consecutive letters or numbers in a password. When unset, it means there is no limit
disallow_local_part_from_email| boolean| | If passwords can resemble emails
password_duration| integer| yes| How long a password lasts before expiring (in days). When unset, it means passwords do not expire

#### IP Restrictions

If Zendesk authentication is enabled, the access to Zendesk Support can be restricted to users within a specific range of IP addresses. This means that users connecting from these IP addresses are the only users allowed to sign in to Support.

Name| Type| Nullable| Description
---|---|---|---
ip_ranges| string| yes| Space separated IP addresses or IP ranges.
ip_restriction_enabled| boolean| | If true, IP restrictions are enabled
enable_agent_ip_restrictions| boolean| | If true, IP restrictions are applied only to agents, allowing customers, even form outside the allowed IP ranges, to access Zendesk

#### Example


    {  "ip": {    "ip_ranges": "127.0.0.1 127.0.0.2",    "ip_restriction_enabled": true,    "enable_agent_ip_restrictions": false  }}

### Show Security Settings

  * `GET /api/v2/security_settings`


#### Allowed For

  * Admins


#### Code Samples

**cURL**


    # Show Security Settingscurl https://{subdomain}.zendesk.com/api/v2/security_settings \   -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/security_settings"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/security_settings")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/security_settings',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/security_settings"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/security_settings")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "security_settings": {    "admins_can_set_user_passwords": false,    "agent_session_timeout": 480,    "assumable": true,    "assumable_account_type": false,    "assumption_duration": "day",    "assumption_expiration": "2025-10-10T12:12:12Z",    "authentication": {      "agent": {        "enforce_sso": false,        "google_login": false,        "office_365_allowed_tids": "",        "office_365_enforce_tid": false,        "office_365_login": false,        "password": {          "disallow_local_part_from_email": false,          "failed_attempts_allowed": 10,          "is_available": true,          "max_sequence": null,          "password_complexity": 0,          "password_duration": 0,          "password_history_length": 0,          "password_in_mixed_case": false,          "password_length": 5        },        "primary_external_auth": null,        "remote_bypass": 2,        "remote_bypass_name": "admins",        "remote_login": false,        "security_policy_id": 350,        "security_policy_name": "recommended",        "sso_auto_redirect": false,        "zendesk_login": true      },      "end_user": {        "enforce_sso": false,        "facebook_login": false,        "google_login": false,        "office_365_login": false,        "primary_external_auth": null,        "remote_login": false,        "security_policy_id": 350,        "security_policy_name": "recommended",        "sso_auto_redirect": false,        "twitter_login": false,        "zendesk_login": true      }    },    "csp_blocking_enabled": true,    "email_agent_when_sensitive_fields_changed": true,    "end_user_session_timeout": 480,    "ip": {      "enable_agent_ip_restrictions": false,      "ip_ranges": "127.0.0.1 127.0.0.2",      "ip_restriction_enabled": true    },    "maximum_session_duration": 720,    "maximum_session_duration_enabled": true,    "mobile_app_access": true,    "mobile_app_session_timeout": 300,    "two_factor_last_update": "2025-09-08T18:12:19Z"  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)