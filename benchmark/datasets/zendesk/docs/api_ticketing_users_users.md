# Users

*Source: https://developer.zendesk.com/api-reference/ticketing/users/users/*

---

## On this page

  * [JSON format](/api-reference/ticketing/users/users/#json-format)
  * [List Users By Group](/api-reference/ticketing/users/users/#list-users-by-group)
  * [Count Users By Group](/api-reference/ticketing/users/users/#count-users-by-group)
  * [List Organization Users](/api-reference/ticketing/users/users/#list-organization-users)
  * [Count Organization Users](/api-reference/ticketing/users/users/#count-organization-users)
  * [List Users](/api-reference/ticketing/users/users/#list-users)
  * [Search Users](/api-reference/ticketing/users/users/#search-users)
  * [Autocomplete Users](/api-reference/ticketing/users/users/#autocomplete-users)
  * [Count Users](/api-reference/ticketing/users/users/#count-users)
  * [Show User](/api-reference/ticketing/users/users/#show-user)
  * [Show Many Users](/api-reference/ticketing/users/users/#show-many-users)
  * [Show User Related Information](/api-reference/ticketing/users/users/#show-user-related-information)
  * [Show Self](/api-reference/ticketing/users/users/#show-self)
  * [Create User](/api-reference/ticketing/users/users/#create-user)
  * [Create Many Users](/api-reference/ticketing/users/users/#create-many-users)
  * [Create Or Update User](/api-reference/ticketing/users/users/#create-or-update-user)
  * [Create Or Update Many Users](/api-reference/ticketing/users/users/#create-or-update-many-users)
  * [Request User Create](/api-reference/ticketing/users/users/#request-user-create)
  * [Update User](/api-reference/ticketing/users/users/#update-user)
  * [Update Many Users](/api-reference/ticketing/users/users/#update-many-users)
  * [Merge End Users](/api-reference/ticketing/users/users/#merge-end-users)
  * [Delete User](/api-reference/ticketing/users/users/#delete-user)
  * [Bulk Delete Users](/api-reference/ticketing/users/users/#bulk-delete-users)
  * [Permanently Delete User](/api-reference/ticketing/users/users/#permanently-delete-user)
  * [List Deleted Users](/api-reference/ticketing/users/users/#list-deleted-users)
  * [Count Deleted Users](/api-reference/ticketing/users/users/#count-deleted-users)
  * [Show Deleted User](/api-reference/ticketing/users/users/#show-deleted-user)
  * [Show Compliance Deletion Statuses](/api-reference/ticketing/users/users/#show-compliance-deletion-statuses)
  * [Autocomplete Users by Request Body](/api-reference/ticketing/users/users/#autocomplete-users-by-request-body)
  * [Logout many users](/api-reference/ticketing/users/users/#logout-many-users)
  * [Show Current User Settings](/api-reference/ticketing/users/users/#show-current-user-settings)
  * [Update Current User Settings](/api-reference/ticketing/users/users/#update-current-user-settings)
  * [Get Full User Entitlements](/api-reference/ticketing/users/users/#get-full-user-entitlements)


# Users

## On this page

  * [JSON format](/api-reference/ticketing/users/users/#json-format)
  * [List Users By Group](/api-reference/ticketing/users/users/#list-users-by-group)
  * [Count Users By Group](/api-reference/ticketing/users/users/#count-users-by-group)
  * [List Organization Users](/api-reference/ticketing/users/users/#list-organization-users)
  * [Count Organization Users](/api-reference/ticketing/users/users/#count-organization-users)
  * [List Users](/api-reference/ticketing/users/users/#list-users)
  * [Search Users](/api-reference/ticketing/users/users/#search-users)
  * [Autocomplete Users](/api-reference/ticketing/users/users/#autocomplete-users)
  * [Count Users](/api-reference/ticketing/users/users/#count-users)
  * [Show User](/api-reference/ticketing/users/users/#show-user)
  * [Show Many Users](/api-reference/ticketing/users/users/#show-many-users)
  * [Show User Related Information](/api-reference/ticketing/users/users/#show-user-related-information)
  * [Show Self](/api-reference/ticketing/users/users/#show-self)
  * [Create User](/api-reference/ticketing/users/users/#create-user)
  * [Create Many Users](/api-reference/ticketing/users/users/#create-many-users)
  * [Create Or Update User](/api-reference/ticketing/users/users/#create-or-update-user)
  * [Create Or Update Many Users](/api-reference/ticketing/users/users/#create-or-update-many-users)
  * [Request User Create](/api-reference/ticketing/users/users/#request-user-create)
  * [Update User](/api-reference/ticketing/users/users/#update-user)
  * [Update Many Users](/api-reference/ticketing/users/users/#update-many-users)
  * [Merge End Users](/api-reference/ticketing/users/users/#merge-end-users)
  * [Delete User](/api-reference/ticketing/users/users/#delete-user)
  * [Bulk Delete Users](/api-reference/ticketing/users/users/#bulk-delete-users)
  * [Permanently Delete User](/api-reference/ticketing/users/users/#permanently-delete-user)
  * [List Deleted Users](/api-reference/ticketing/users/users/#list-deleted-users)
  * [Count Deleted Users](/api-reference/ticketing/users/users/#count-deleted-users)
  * [Show Deleted User](/api-reference/ticketing/users/users/#show-deleted-user)
  * [Show Compliance Deletion Statuses](/api-reference/ticketing/users/users/#show-compliance-deletion-statuses)
  * [Autocomplete Users by Request Body](/api-reference/ticketing/users/users/#autocomplete-users-by-request-body)
  * [Logout many users](/api-reference/ticketing/users/users/#logout-many-users)
  * [Show Current User Settings](/api-reference/ticketing/users/users/#show-current-user-settings)
  * [Update Current User Settings](/api-reference/ticketing/users/users/#update-current-user-settings)
  * [Get Full User Entitlements](/api-reference/ticketing/users/users/#get-full-user-entitlements)


Zendesk Support has three types of users: end users (your customers), agents, and administrators.

#### End users

End users request support through tickets. End users have access to Help Center where they can view knowledge base articles and community content, access their ticket history, and submit new tickets.

#### Agents

Agents work in Zendesk Support to solve tickets. Agents can be divided into multiple groups and can also belong to multiple groups. Agents don't have access to administrative configuration in Zendesk Support such as business rules or automations, but can configure their own macros and views.

#### Administrators

Administrators have all the abilities of agents, plus administrative abilities. Accounts on the Enterprise plan and above can configure custom roles to give agents varying degrees of administrative access.

#### Listing Requested Tickets and CC'ed Tickets

Use the Tickets API to list:

  * [tickets requested by a user](/api-reference/ticketing/tickets/tickets/#list-tickets)
  * [tickets on which a user is cc'ed](/api-reference/ticketing/tickets/tickets/#list-tickets)


#### Listing Help Center Content by a User

Use the Help Center API to list:

  * [articles](/api-reference/help_center/help-center-api/articles/#list-articles) and [article comments](/api-reference/help_center/help-center-api/article_comments/#list-comments) created by a user
  * [community posts](/api-reference/help_center/help-center-api/posts/#list-posts) and [post comments](/api-reference/help_center/help-center-api/post_comments/#list-comments) created by a user


### JSON format

Users are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
active| boolean| true| false| false if the user has been deleted
agent_brand_ids| array| false| false| PUT or POST requests only. Assigns agent or agents to a brand. For more information, see Agent brand ids
alias| string| false| false| An alias displayed to end users
chat_only| boolean| true| false| Whether or not the user is a chat-only agent
created_at| string| true| false| The time the user was created
custom_role_id| integer| false| false| A custom role if the user is an agent on the Enterprise plan or above
default_group_id| integer| false| false| The id of the user's default group
details| string| false| false| Any details you want to store about the user, such as an address
email| string| false| false| The user's primary email address. *Writeable on create only. On update, a secondary email is added. See Email Address
external_id| string| false| false| A unique identifier from another system. The API treats the id as case insensitive. Example: "ian1" and "IAN1" are the same value.
iana_time_zone| string| true| false| The time zone for the user
id| integer| true| false| Automatically assigned when the user is created
last_login_at| string| true| false| Last time the user signed in to Zendesk Support or made an API request using an API token
locale| string| false| false| The user's locale. A BCP-47 compliant tag for the locale. If both "locale" and "locale_id" are present on create or update, "locale_id" is ignored and only "locale" is used.
locale_id| integer| false| false| The user's language identifier
moderator| boolean| false| false| Designates whether the user has forum moderation capabilities
name| string| false| true| The user's name
notes| string| false| false| Any notes you want to store about the user
only_private_comments| boolean| false| false| true if the user can only create private comments
organization_id| integer| false| false| The id of the user's organization. If the user has more than one [organization memberships](/api-reference/ticketing/organizations/organization_memberships/), the id of the user's default organization. If updating, see Organization ID
phone| string| false| false| The user's primary phone number. See Phone Number below
photo| object| false| false| The user's profile picture represented as an [Attachment](/api-reference/ticketing/tickets/ticket-attachments/) object
remote_photo_url| string| false| false| A URL pointing to the user's profile picture.
report_csv| boolean| true| false| This parameter is inert and has no effect. It may be deprecated in the future. Previously, this parameter determined whether a user could access a CSV report in a legacy Guide dashboard. This dashboard has been removed. See [Announcing Guide legacy reporting upgrade to Explore](https://support.zendesk.com/hc/en-us/articles/4762263171610-Announcing-Guide-legacy-reporting-upgrade-to-Explore-)
restricted_agent| boolean| true| false| If the agent has any restrictions; false for admins and unrestricted agents, true for other agents
role| string| false| false| The user's role. Possible values are "end-user", "agent", or "admin"
role_type| integer| true| false| The user's role id. 0 for a custom agent, 1 for a light agent, 2 for a chat agent, 3 for a chat agent added to the Support account as a contributor ([Chat Phase 4](https://support.zendesk.com/hc/en-us/articles/360022365373#topic_djh_1zk_4fb)), 4 for an admin, and 5 for a billing admin
shared| boolean| true| false| If the user is shared from a different Zendesk Support instance. Shared users can be added to organizations but cannot be modified through update requests. Any attempt to update a shared user results in a 403 Forbidden error. Ticket sharing accounts only
shared_agent| boolean| true| false| If the user is a shared agent from a different Zendesk Support instance. Ticket sharing accounts only
shared_phone_number| boolean| false| false| Whether the `phone` number is shared or not. See Phone Number below
signature| string| false| false| The user's signature. Only agents and admins can have signatures
suspended| boolean| false| false| If the agent is suspended. Tickets from suspended users are also suspended, and these users cannot sign in to the end user portal
tags| array| false| false| The user's tags. Only present if your account has user tagging enabled
ticket_restriction| string| false| false| Specifies which tickets the user has access to. Possible values are: "organization", "groups", "assigned", "requested", null. "groups" and "assigned" are valid only for agents. If you pass an invalid value to an end user (for example, "groups"), they will be assigned to "requested", regardless of their previous access
time_zone| string| false| false| The user's time zone. See Time Zone
two_factor_auth_enabled| boolean| true| false| If two factor authentication is enabled
updated_at| string| true| false| The time the user was last updated
url| string| true| false| The user's API url
user_fields| object| false| false| Values of custom fields in the user's profile. See User Fields
verified| boolean| false| false| Any of the user's identities is verified. See [User Identities](/api-reference/ticketing/users/user_identities)

#### Email Address

You can specify a user's primary email address when you create the user. See [Specifying email and verified attributes](/api-reference/ticketing/users/users/#specifying-email-and-verified-attributes).

To update a user's primary email address, use the [Make Identity Primary](/api-reference/ticketing/users/user_identities#make-identity-primary) endpoint.

#### Time Zone

A `time_zone` name consists of a string such as "Eastern Time (US & Canada)". For a list of valid names, click <https://support.zendesk.com/api/v2/time_zones>[](https://support.zendesk.com/api/v2/time_zones). For details, see [Time Zones](/api-reference/introduction/data-types/#time-zones).

Request body in User API:


    { "user": {   "id":   35436,   "name": "Johnny Agent",   "time_zone": "Berlin",   ... }}

#### User Fields

You can use the `user_fields` object to set the value of one or more custom fields in the user's profile. Specify [field keys](/api-reference/ticketing/users/user_fields/#json-format) as the properties to set. Example:


    "user_fields": {   "membership_level": "silver",   "membership_expires": "2019-07-23T00:00:00Z" }

For more information, see [User Fields](/api-reference/ticketing/users/user_fields/) and [Adding custom fields to users](https://support.zendesk.com/hc/en-us/articles/203662066).

#### Agent brand ids

You can give an agent access to one or more brands by including the `agent_brand_ids` property in the user object. This property is available in both single and bulk user operations. Provide an array of brand IDs to limit the agent's access and visibility to only those brands. `agent_brand_ids` is used only when setting or updating an agent's brands and does not appear on GET response bodies.

The `agent_brand_ids` field is only respected when the account's brand setting for new agents is set to "Manual". If the brand setting is not set to "Manual", any values you provide for `agent_brand_ids` will be overwritten by Zendesk according to the configured brand assignment logic in brand settings.

#### Phone Number

The phone number should comply with the E.164 international [telephone numbering plan](https://en.wikipedia.org/wiki/E.164). Example `+15551234567`. E164 numbers are international numbers with a country dial prefix, usually an area code and a subscriber number. A valid E.164 phone number must include a [country calling code](https://en.wikipedia.org/wiki/List_of_country_calling_codes).

A phone number can be one of the following types:

  * A direct line linked to a single user, which is indicated by a `shared_phone_number` attribute of false. A direct line can be used as a [user identity](/api-reference/ticketing/users/user_identities)
  * A shared number linked to multiple users, indicated by a `shared_phone_number` attribute of true. A shared number can not be used as a [user identity](/api-reference/ticketing/users/user_identities)


See [Understanding how phone numbers are linked to end-user profiles](https://support.zendesk.com/hc/en-us/articles/230553307#topic_hz3_5nm_sx) in the Support Help Center.

#### Organization ID

The `organization_id` property returns the id of the user's organization. If the user has more than one organization memberships, the id of the user's default organization is returned.

The field is writable. However, if you make a request to update the `organization_id` property, the `organization_id` of the request updates the default organization for that user and removes all other organizations currently associated with that user. Zendesk recommends using the [Organization Memberships API](/api-reference/ticketing/organizations/organization_memberships/) to add or delete organizations for a user.

#### JSON Format for End Users

When an end user makes the request, the user is returned with the following attributes:

Name| Type| Read-only| Mandatory| Comment
---|---|---|---|---
id| integer| yes| no| Automatically assigned when creating users
email| string| no| no| The primary email address of this user. If the primary email address is not [verified](https://support.zendesk.com/hc/en-us/articles/4408886752410), the secondary email address is used
name| string| no| yes| The name of the user
created_at| date| yes| no| The time the user was created
locale| string| yes| no| The locale for this user
locale_id| integer| no| no| The language identifier for this user
organization_id| integer| no| no| The id of the user's organization. If the user has more than one [organization memberships](/api-reference/ticketing/organizations/organization_memberships/), the id of the user's default organization. If updating, see Organization ID
phone| string| no| no| The primary phone number of this user. See [Phone Number](/api-reference/ticketing/users/users/#phone-number) in the Users API
shared_phone_number| boolean| yes| no| Whether the `phone` number is shared or not. See [Phone Number](/api-reference/ticketing/users/users/#phone-number) in the Users API
photo| [Attachment](/api-reference/ticketing/tickets/ticket-attachments/)| no| no| The user's profile picture represented as an [Attachment](/api-reference/ticketing/tickets/ticket-attachments/) object
role| string| no| no| The role of the user. Possible values: "end-user", "agent", "admin"
time_zone| string| no| no| The time-zone of this user
updated_at| date| yes| no| The time of the last update of the user
url| string| yes| no| The API url of this user
verified| boolean| no| no| Any of the user's identities is verified. See [User Identities](/api-reference/ticketing/users/user_identities)

Responses will vary depending on the role of the client making the request. The following example is a response for an end-user role.

#### Example


    {  "id":                    35436,  "url":                   "https://company.zendesk.com/api/v2/end_users/35436",  "name":                  "Johnny End User",  "created_at":            "2009-07-20T22:55:29Z",  "updated_at":            "2011-05-05T10:38:52Z",  "time_zone":             "Copenhagen",  "email":                 "[[email protected]](/cdn-cgi/l/email-protection)",  "phone":                 "+15551234567",  "locale":                "en-US",  "locale_id":             1,  "organization_id":       57542,  "role":                  "end-user",  "verified":              true,  "photo": {    "id":           928374,    "name":         "my_funny_profile_pic.png",    "content_url":  "https://company.zendesk.com/photos/my_funny_profile_pic.png",    "content_type": "image/png",    "size":         166144,    "thumbnails": [      {      "id":           928375,      "name":         "my_funny_profile_pic_thumb.png",      "content_url":  "https://company.zendesk.com/photos/my_funny_profile_pic_thumb.png",      "content_type": "image/png",      "size":         58298      }    ]  }}

This example is a response for an admin or agent request.

#### Example


    {  "active": true,  "alias": "Mr. Johnny",  "created_at": "2009-07-20T22:55:29Z",  "custom_role_id": 9373643,  "details": "",  "email": "[[email protected]](/cdn-cgi/l/email-protection)",  "external_id": "sai989sur98w9",  "iana_time_zone": "Pacific/Pago_Pago",  "id": 35436,  "last_login_at": "2011-05-05T10:38:52Z",  "locale": "en-US",  "locale_id": 1,  "moderator": true,  "name": "Johnny Agent",  "notes": "Johnny is a nice guy!",  "only_private_comments": false,  "organization_id": 57542,  "phone": "+15551234567",  "photo": {    "content_type": "image/png",    "content_url": "https://company.zendesk.com/photos/my_funny_profile_pic.png",    "id": 928374,    "name": "my_funny_profile_pic.png",    "size": 166144,    "thumbnails": [      {        "content_type": "image/png",        "content_url": "https://company.zendesk.com/photos/my_funny_profile_pic_thumb.png",        "id": 928375,        "name": "my_funny_profile_pic_thumb.png",        "size": 58298      }    ]  },  "restricted_agent": true,  "role": "agent",  "role_type": 0,  "shared": false,  "shared_agent": false,  "signature": "Have a nice day, Johnny",  "suspended": true,  "tags": [    "enterprise",    "other_tag"  ],  "ticket_restriction": "assigned",  "time_zone": "Copenhagen",  "updated_at": "2011-05-05T10:38:52Z",  "url": "https://company.zendesk.com/api/v2/users/35436",  "user_fields": {    "user_date": "2012-07-23T00:00:00Z",    "user_decimal": 5.1,    "user_dropdown": "option_1"  },  "verified": true}

### List Users By Group

  * `GET /api/v2/groups/{group_id}/users`


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Admins, Agents and Light Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
external_id| string| Query| false| List users by external id. External id has to be unique for each user under the same account.
permission_set| integer| Query| false| For custom roles which is available on the Enterprise plan and above. You can only filter by one role ID per request
role| string| Query| false| Filters the results by role. Possible values are "end-user", "agent", "admin", or a custom role name
role[]| string| Query| false| Filters the results by more than one role using the format `role[]={role}&role[]={role}`
group_id| integer| Path| true| The ID of the group

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/groups/{group_id}/users \   -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/groups/122/users?external_id=abc&permission_set=123&role=agent&role[]=agent"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/groups/122/users")		.newBuilder()		.addQueryParameter("external_id", "abc")		.addQueryParameter("permission_set", "123")		.addQueryParameter("role", "agent")		.addQueryParameter("role[]", "agent");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/groups/122/users',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'external_id': 'abc',    'permission_set': '123',    'role': 'agent',    'role[]': 'agent',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/groups/122/users?external_id=abc&permission_set=123&role=agent&role[]=agent"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/groups/122/users")uri.query = URI.encode_www_form("external_id": "abc", "permission_set": "123", "role": "agent", "role[]": "agent")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "users": [    {      "id": 223443,      "name": "Johnny Agent"    },    {      "id": 8678530,      "name": "James A. Rosen"    }  ]}

### Count Users By Group

  * `GET /api/v2/groups/{group_id}/users/count`


Returns an approximate count of users in the specified group. If the count exceeds 100,000, it is updated every 24 hours.

The response includes a `refreshed_at` property in a `count` object that contains a timestamp indicating when the count was last updated.

**Note** : When the count exceeds 100,000, the `refreshed_at` property may occasionally be null. This indicates that the count is being updated in the background. The `count` object's `value` property is limited to 100,000 until the update is complete.

#### Allowed For

  * Admins, Agents and Light Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
permission_set| integer| Query| false| For custom roles which is available on the Enterprise plan and above. You can only filter by one role ID per request
role| string| Query| false| Filters the results by role. Possible values are "end-user", "agent", "admin", or a custom role name
role[]| string| Query| false| Filters the results by more than one role using the format `role[]={role}&role[]={role}`
group_id| integer| Path| true| The ID of the group

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/groups/{group_id}/users/count \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/groups/122/users/count?permission_set=123&role=agent&role[]=agent"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/groups/122/users/count")		.newBuilder()		.addQueryParameter("permission_set", "123")		.addQueryParameter("role", "agent")		.addQueryParameter("role[]", "agent");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/groups/122/users/count',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'permission_set': '123',    'role': 'agent',    'role[]': 'agent',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/groups/122/users/count?permission_set=123&role=agent&role[]=agent"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/groups/122/users/count")uri.query = URI.encode_www_form("permission_set": "123", "role": "agent", "role[]": "agent")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": {    "refreshed_at": "2020-04-06T02:18:17Z",    "value": 102  }}

### List Organization Users

  * `GET /api/v2/organizations/{organization_id}/users`


Returns a list of users for a specific organization.

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Admins, Agents and Light Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
external_id| string| Query| false| List users by external id. External id has to be unique for each user under the same account.
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
permission_set| integer| Query| false| For custom roles which is available on the Enterprise plan and above. You can only filter by one role ID per request
role| string| Query| false| Filters the results by role. Possible values are "end-user", "agent", "admin", or a custom role name
role[]| string| Query| false| Filters the results by more than one role using the format `role[]={role}&role[]={role}`
sort_by| string| Query| false| The field to sort users by. Allowed values are "id", "name", "created_at", or "updated_at".
sort_order| string| Query| false| The sort order. Allowed values are "asc", or "desc".
organization_id| integer| Path| true| The ID of an organization

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/organizations/{organization_id}/users \   -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/16/users?external_id=abc&page=&per_page=50&permission_set=123&role=agent&role[]=agent&sort_by=&sort_order="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/16/users")		.newBuilder()		.addQueryParameter("external_id", "abc")		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("permission_set", "123")		.addQueryParameter("role", "agent")		.addQueryParameter("role[]", "agent")		.addQueryParameter("sort_by", "")		.addQueryParameter("sort_order", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/organizations/16/users',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'external_id': 'abc',    'page': '',    'per_page': '50',    'permission_set': '123',    'role': 'agent',    'role[]': 'agent',    'sort_by': '',    'sort_order': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/16/users?external_id=abc&page=&per_page=50&permission_set=123&role=agent&role[]=agent&sort_by=&sort_order="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/16/users")uri.query = URI.encode_www_form("external_id": "abc", "page": "", "per_page": "50", "permission_set": "123", "role": "agent", "role[]": "agent", "sort_by": "", "sort_order": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "users": [    {      "id": 223443,      "name": "Johnny Agent"    },    {      "id": 8678530,      "name": "James A. Rosen"    }  ]}

### Count Organization Users

  * `GET /api/v2/organizations/{organization_id}/users/count`


Returns an approximate count of users for a specific organization. If the count exceeds 100,000, it is updated every 24 hours.

The response includes a `refreshed_at` property in a `count` object that contains a timestamp indicating when the count was last updated.

**Note** : When the count exceeds 100,000, the `refreshed_at` property may occasionally be null. This indicates that the count is being updated in the background. The `count` object's `value` property is limited to 100,000 until the update is complete.

#### Allowed For

  * Admins, Agents and Light Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
permission_set| integer| Query| false| For custom roles which is available on the Enterprise plan and above. You can only filter by one role ID per request
role| string| Query| false| Filters the results by role. Possible values are "end-user", "agent", "admin", or a custom role name
role[]| string| Query| false| Filters the results by more than one role using the format `role[]={role}&role[]={role}`
organization_id| integer| Path| true| The ID of an organization

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/organizations/{organization_id}/users/count \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/organizations/16/users/count?permission_set=123&role=agent&role[]=agent"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/organizations/16/users/count")		.newBuilder()		.addQueryParameter("permission_set", "123")		.addQueryParameter("role", "agent")		.addQueryParameter("role[]", "agent");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/organizations/16/users/count',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'permission_set': '123',    'role': 'agent',    'role[]': 'agent',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/organizations/16/users/count?permission_set=123&role=agent&role[]=agent"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/organizations/16/users/count")uri.query = URI.encode_www_form("permission_set": "123", "role": "agent", "role[]": "agent")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": {    "refreshed_at": "2020-04-06T02:18:17Z",    "value": 102  }}

### List Users

  * `GET /api/v2/users`


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Admins, Agents and Light Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
external_id| string| Query| false| List users by external id. External id has to be unique for each user under the same account.
include| string| Query| false| Sideloads to include in the response. Accepts a comma-separated list of values. See [Sideloading](/api-reference/ticketing/users/users/#sideloading).
include_boundary_indicators| boolean| Query| false| When true, includes `has_more` indicator in the cursor pagination response meta. Only valid with cursor pagination (page[size], page[after], page[before]).
include_item_cursors| boolean| Query| false| When true, includes cursor values for each item in the cursor pagination response. Only valid with cursor pagination (page[size], page[after], page[before]).
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
permission_set| integer| Query| false| For custom roles which is available on the Enterprise plan and above. You can only filter by one role ID per request
role| string| Query| false| Filters the results by role. Possible values are "end-user", "agent", "admin", or a custom role name
role[]| string| Query| false| Filters the results by more than one role using the format `role[]={role}&role[]={role}`
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`

#### Code Samples

**cURL**


    # List Userscurl https://{subdomain}.zendesk.com/api/v2/users \   -v -u {email_address}/token:{api_token}# with role filtering# **Note**: If filtering by multiple roles in curl, make sure to include# the `-g` flag to prevent curl from interpreting the square brackets# as globbing characters. Also enclose the URL in quotes. Example:curl -g 'https://{subdomain}.zendesk.com/api/v2/users?role[]=admin&role[]=end-user' \ -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users?external_id=abc&include=roles%2Corganizations&include_boundary_indicators=&include_item_cursors=&page=&per_page=50&permission_set=123&role=agent&role[]=agent&sort=name"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users")		.newBuilder()		.addQueryParameter("external_id", "abc")		.addQueryParameter("include", "roles,organizations")		.addQueryParameter("include_boundary_indicators", "")		.addQueryParameter("include_item_cursors", "")		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("permission_set", "123")		.addQueryParameter("role", "agent")		.addQueryParameter("role[]", "agent")		.addQueryParameter("sort", "name");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'external_id': 'abc',    'include': 'roles%2Corganizations',    'include_boundary_indicators': '',    'include_item_cursors': '',    'page': '',    'per_page': '50',    'permission_set': '123',    'role': 'agent',    'role[]': 'agent',    'sort': 'name',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users?external_id=abc&include=roles%2Corganizations&include_boundary_indicators=&include_item_cursors=&page=&per_page=50&permission_set=123&role=agent&role[]=agent&sort=name"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users")uri.query = URI.encode_www_form("external_id": "abc", "include": "roles,organizations", "include_boundary_indicators": "", "include_item_cursors": "", "page": "", "per_page": "50", "permission_set": "123", "role": "agent", "role[]": "agent", "sort": "name")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "users": [    {      "id": 223443,      "name": "Johnny Agent"    },    {      "id": 8678530,      "name": "James A. Rosen"    }  ]}

### Search Users

  * `GET /api/v2/users/search`


Returns an array of users who meet the search criteria.

Returns up to 100 records per page to a maximum of 10,000 records per query. See [Using offset pagination](/api-reference/introduction/pagination/#using-offset-pagination).

#### Pagination

  * Offset pagination only


See [Using Offset Pagination](/api-reference/introduction/pagination/#using-offset-pagination).

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
external_id| string| Query| false| The `external_id` parameter does not support the search syntax. It only accepts ids.
include| string| Query| false| A comma-separated list of sideloads to include in the response.
page| integer| Query| false| Page number for offset-based pagination (non-negative integer).
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
query| string| Query| false| The `query` parameter supports the Zendesk search syntax for more advanced user searches. It can specify a partial or full value of any user property, including name, email address, notes, or phone. Example: `query="jdoe"`. See the [Search API](/api-reference/ticketing/ticket-management/search/).

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/search?query=gil \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/search?external_id=abc124&include=&page=1&per_page=50&query=jdoe"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/search")		.newBuilder()		.addQueryParameter("external_id", "abc124")		.addQueryParameter("include", "")		.addQueryParameter("page", "1")		.addQueryParameter("per_page", "50")		.addQueryParameter("query", "jdoe");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users/search',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'external_id': 'abc124',    'include': '',    'page': '1',    'per_page': '50',    'query': 'jdoe',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/search?external_id=abc124&include=&page=1&per_page=50&query=jdoe"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/search")uri.query = URI.encode_www_form("external_id": "abc124", "include": "", "page": "1", "per_page": "50", "query": "jdoe")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "users": [    {      "id": 35436,      "name": "Robert Jones",      "notes": "sigil issue"    },    {      "id": 9873843,      "name": "Terry Gilliam"    }  ]}

### Autocomplete Users

  * `GET /api/v2/users/autocomplete`


Returns an array of users whose name starts with the value specified in the `name` parameter. It only returns users with no foreign identities.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
field_id| string| Query| false| The id of a lookup relationship field. The type of field is determined by the `source` param
filter| string| Query| false| Filter to apply to autocomplete results. Accepted values: `assignable`, `requester`. Allowed values are "assignable", or "requester".
include| string| Query| false| Sideloads to include in the response. Accepts a comma-separated list of values. See [Sideloading](/api-reference/ticketing/users/users/#sideloading).
name| string| Query| false| The name to search for the user. You must specify either `name` or `phone`.
phone| string| Query| false| The phone number to search for the user. You must specify either `name` or `phone`.
source| string| Query| false| If a `field_id` is provided, this specifies the type of the field. For example, if the field is on a "zen:user", it references a field on a user

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/autocomplete?name=gil \  -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/autocomplete?field_id=&filter=&include=roles%2Corganizations&name=gil&phone=&source="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/autocomplete")		.newBuilder()		.addQueryParameter("field_id", "")		.addQueryParameter("filter", "")		.addQueryParameter("include", "roles,organizations")		.addQueryParameter("name", "gil")		.addQueryParameter("phone", "")		.addQueryParameter("source", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users/autocomplete',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'field_id': '',    'filter': '',    'include': 'roles%2Corganizations',    'name': 'gil',    'phone': '',    'source': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/autocomplete?field_id=&filter=&include=roles%2Corganizations&name=gil&phone=&source="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/autocomplete")uri.query = URI.encode_www_form("field_id": "", "filter": "", "include": "roles,organizations", "name": "gil", "phone": "", "source": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "users": [    {      "id": 35436,      "name": "Robert Jones",      "notes": "sigil issue"    },    {      "id": 9873843,      "name": "Terry Gilliam"    }  ]}

### Count Users

  * `GET /api/v2/users/count`


Returns an approximate count of users. If the count exceeds 100,000, it is updated every 24 hours.

The response includes a `refreshed_at` property in a `count` object that contains a timestamp indicating when the count was last updated.

**Note** : When the count exceeds 100,000, the `refreshed_at` property may occasionally be null. This indicates that the count is being updated in the background. The `count` object's `value` property is limited to 100,000 until the update is complete.

#### Allowed For

  * Admins, Agents and Light Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
permission_set| integer| Query| false| For custom roles which is available on the Enterprise plan and above. You can only filter by one role ID per request
role| string| Query| false| Filters the results by role. Possible values are "end-user", "agent", "admin", or a custom role name
role[]| string| Query| false| Filters the results by more than one role using the format `role[]={role}&role[]={role}`

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/count \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/count?permission_set=123&role=agent&role[]=agent"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/count")		.newBuilder()		.addQueryParameter("permission_set", "123")		.addQueryParameter("role", "agent")		.addQueryParameter("role[]", "agent");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users/count',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'permission_set': '123',    'role': 'agent',    'role[]': 'agent',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/count?permission_set=123&role=agent&role[]=agent"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/count")uri.query = URI.encode_www_form("permission_set": "123", "role": "agent", "role[]": "agent")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": {    "refreshed_at": "2020-04-06T02:18:17Z",    "value": 102  }}

### Show User

  * `GET /api/v2/users/{user_id}`


#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
include| string| Query| false| Sideloads to include in the response. Accepts a comma-separated list of values. See [Sideloading](/api-reference/ticketing/users/users/#sideloading).
user_id| integer| Path| true| The id of the user

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436?include=roles%2Corganizations"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436")		.newBuilder()		.addQueryParameter("include", "roles,organizations");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users/35436',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'include': 'roles%2Corganizations',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436?include=roles%2Corganizations"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436")uri.query = URI.encode_www_form("include": "roles,organizations")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "user": {    "id": 35436,    "name": "Johnny Agent"  }}

### Show Many Users

  * `GET /api/v2/users/show_many`


Accepts a comma-separated list of up to 100 user ids or external ids.

#### Allowed For:

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
external_ids| string| Query| false| Accepts a comma-separated list of up to 100 external ids.
ids| string| Query| false| Accepts a comma-separated list of up to 100 user ids.
include| string| Query| false| Sideloads to include in the response. Accepts a comma-separated list of values. See [Sideloading](/api-reference/ticketing/users/users/#sideloading).
include_deleted| boolean| Query| false| If true, returns inactive or deleted users.

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/show_many?ids=345678,901234 \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/show_many?external_ids=abc%2Cdef&ids=1%2C2&include=roles%2Corganizations&include_deleted="	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/show_many")		.newBuilder()		.addQueryParameter("external_ids", "abc,def")		.addQueryParameter("ids", "1,2")		.addQueryParameter("include", "roles,organizations")		.addQueryParameter("include_deleted", "");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users/show_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'external_ids': 'abc%2Cdef',    'ids': '1%2C2',    'include': 'roles%2Corganizations',    'include_deleted': '',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/show_many?external_ids=abc%2Cdef&ids=1%2C2&include=roles%2Corganizations&include_deleted="headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/show_many")uri.query = URI.encode_www_form("external_ids": "abc,def", "ids": "1,2", "include": "roles,organizations", "include_deleted": "")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "users": [    {      "id": 345678,      "name": "Johnny Appleseed"    },    {      "id": 901234,      "name": "Rupert Root"    }  ]}

### Show User Related Information

  * `GET /api/v2/users/{user_id}/related`


#### JSON Format

The JSON returned by this endpoint includes the following properties.

**Note:** Depending on the user's permissions, the count results may not match the actual number of tickets returned.

Name| Type| Comment
---|---|---
assigned_tickets| integer| Count of assigned tickets
requested_tickets| integer| Count of requested tickets
ccd_tickets| integer| Count of collaborated tickets
organization_subscriptions| integer| Count of organization subscriptions

#### Allowed For:

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/related \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436/related"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436/related")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users/35436/related',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436/related"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436/related")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "user_related": {    "assigned_tickets": 5,    "ccd_tickets": 3,    "organization_subscriptions": 1,    "requested_tickets": 10  }}

### Show Self

  * `GET /api/v2/users/me`


The endpoint returns [user information](/api-reference/ticketing/users/users/) and an `authenticity_token`.

#### Allowed For

  * Anonymous users


#### Authenticity Token

Zendesk API calls made by end users from a Zendesk help center must include `authenticity_token` in the `X-CSRF-Token` HTTP header. This helps prevent [cross-site request forgery (CSRF)](https://en.wikipedia.org/wiki/Cross-site_request_forgery) attacks.

For an example using an authenticity token, see the AJAX request in the [Upgrading from Templating API v1](https://developer.zendesk.com/documentation/help_center/help-center-templates/v1#jquery) documentation.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
include| string| Query| false| Sideloads to include in the response. Accepts a comma-separated list of values. See [Sideloading](/api-reference/ticketing/users/users/#sideloading).

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/me \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/me?include=roles%2Corganizations"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/me")		.newBuilder()		.addQueryParameter("include", "roles,organizations");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users/me',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'include': 'roles%2Corganizations',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/me?include=roles%2Corganizations"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/me")uri.query = URI.encode_www_form("include": "roles,organizations")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "user": {    "active": true,    "alias": "Mr. Johnny",    "authenticity_token": "<CORS TOKEN>",    "created_at": "2009-07-20T22:55:29Z",    "custom_role_id": 9373643,    "details": "",    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "external_id": "sai989sur98w9",    "id": 35436,    "last_login_at": "2011-05-05T10:38:52Z",    "locale": "en-US",    "locale_id": 1,    "moderator": true,    "name": "Johnny Agent",    "notes": "Johnny is a nice guy!",    "only_private_comments": false,    "organization_id": 57542,    "phone": "+15551234567",    "photo": {      "content_type": "image/png",      "content_url": "https://company.zendesk.com/photos/my_funny_profile_pic.png",      "id": 928374,      "name": "my_funny_profile_pic.png",      "size": 166144,      "thumbnails": [        {          "content_type": "image/png",          "content_url": "https://company.zendesk.com/photos/my_funny_profile_pic_thumb.png",          "id": 928375,          "name": "my_funny_profile_pic_thumb.png",          "size": 58298        }      ]    },    "restricted_agent": true,    "role": "agent",    "role_type": 0,    "shared": false,    "shared_agent": false,    "signature": "Have a nice day, Johnny",    "suspended": true,    "tags": [      "enterprise",      "other_tag"    ],    "ticket_restriction": "assigned",    "time_zone": "Copenhagen",    "updated_at": "2011-05-05T10:38:52Z",    "url": "https://company.zendesk.com/api/v2/users/35436",    "user_fields": {      "user_date": "2012-07-23T00:00:00Z",      "user_decimal": 5.1,      "user_dropdown": "option_1"    },    "verified": true  }}

### Create User

  * `POST /api/v2/users`


#### Skip verification email

If you need to create users without sending out a verification email, include a `"skip_verify_email": true` property.

#### User role

If you don't specify a `role` parameter, the new user is assigned the role of end user.

If you need to create agents with a specific role, the `role` property only accepts three possible values: "end-user", "agent", and "admin". Therefore, set `role` to "agent" as well as add a new property called `custom_role_id` and give it the actual desired role ID from your Zendesk Support account. This applies to the built-in light agent role of Zendesk Support as well.

If you set `role` to "end-user" but include a `custom_role_id` value, `role` will be set to "agent".

#### Create User with Multiple Identities

If you have a user with multiple identities, such as email addresses and X (formerly Twitter) accounts, you can also include these values at creation time by including an `identities` array where each identity in the array has a `type` and `value` property. Example: `{"type": "email", "value": "[[email protected]](/cdn-cgi/l/email-protection)"}`. This is especially useful when importing users from another system.

#### Allowed For

  * Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage team members


#### Example body


    {  "user": {    "agent_brand_ids": [      8119246973690,      8119246973691,      8119246973692    ],    "custom_role_id": 123456,    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "identities": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "twitter",        "value": "tester84"      }    ],    "name": "Roger Wilco",    "organization": {      "name": "VIP Customers"    },    "role": "agent"  }}

#### Code Samples

**cURL**


    # with rolecurl https://{subdomain}.zendesk.com/api/v2/users \  -d '{"user": {"name": "Roger Wilco", "email": "[[email protected]](/cdn-cgi/l/email-protection)", "role": "agent", "custom_role_id": 123456}, "agent_brand_ids": [1, 2, 3]}' \  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}
    # with organizationcurl https://{subdomain}.zendesk.com/api/v2/users \  -d '{"user": {"name": "Roger Wilco", "email": "[[email protected]](/cdn-cgi/l/email-protection)", "organization": {"name": "VIP Customers"}, "agent_brand_ids": [1, 2, 3]}}' \  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}
    # with identitiescurl https://{subdomain}.zendesk.com/api/v2/users \-d '{"user": {"name": "Roger Wilco", "identities": [{ "type": "email", "value": "[[email protected]](/cdn-cgi/l/email-protection)"}, {"type": "twitter", "value": "tester84" }], "agent_brand_ids": [1, 2, 3]}}' \-H "Content-Type: application/json" -X POST \-v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/users"	method := "POST"	payload := strings.NewReader(`{  "user": {    "agent_brand_ids": [      8119246973690,      8119246973691,      8119246973692    ],    "custom_role_id": 123456,    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "identities": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "twitter",        "value": "tester84"      }    ],    "name": "Roger Wilco",    "organization": {      "name": "VIP Customers"    },    "role": "agent"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"user\": {    \"agent_brand_ids\": [      8119246973690,      8119246973691,      8119246973692    ],    \"custom_role_id\": 123456,    \"email\": \"roge@example.org\",    \"identities\": [      {        \"type\": \"email\",        \"value\": \"test@user.com\"      },      {        \"type\": \"twitter\",        \"value\": \"tester84\"      }    ],    \"name\": \"Roger Wilco\",    \"organization\": {      \"name\": \"VIP Customers\"    },    \"role\": \"agent\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "user": {    "agent_brand_ids": [      8119246973690,      8119246973691,      8119246973692    ],    "custom_role_id": 123456,    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "identities": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "twitter",        "value": "tester84"      }    ],    "name": "Roger Wilco",    "organization": {      "name": "VIP Customers"    },    "role": "agent"  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/users',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users"
    payload = json.loads("""{  "user": {    "agent_brand_ids": [      8119246973690,      8119246973691,      8119246973692    ],    "custom_role_id": 123456,    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "identities": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "twitter",        "value": "tester84"      }    ],    "name": "Roger Wilco",    "organization": {      "name": "VIP Customers"    },    "role": "agent"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "user": {    "agent_brand_ids": [      8119246973690,      8119246973691,      8119246973692    ],    "custom_role_id": 123456,    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "identities": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "twitter",        "value": "tester84"      }    ],    "name": "Roger Wilco",    "organization": {      "name": "VIP Customers"    },    "role": "agent"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**201 Created**


    // Status 201 Created
    {  "user": {    "custom_role_id": 123456,    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "id": 9873843,    "name": "Roger Wilco",    "organization_id": 57542,    "role": "agent",    "role_type": 0  }}

### Create Many Users

  * `POST /api/v2/users/create_many`


Accepts an array of up to 100 user objects.

**Note** : To protect the data in your Zendesk account, bulk user imports are not enabled by default in Zendesk accounts. The account owner must contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to enable the imports. A 403 Forbidden error is returned if data imports are not enabled.

#### Allowed For

  * Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage end users or team members


#### Specifying an organization

You can assign a user to an existing organization by setting an `organization_id` property in the user object.

#### Response

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.

#### Example body


    {  "users": [    {      "agent_brand_ids": [        8119246973690,        8119246973691,        8119246973692      ],      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "name": "Roger Wilco",      "organization_id": 567812345,      "role": "agent"    },    {      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "name": "Woger Rilco",      "role": "admin"    }  ]}

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/create_many \  -d '{"users": [{"name": "Roger Wilco", "email": "[[email protected]](/cdn-cgi/l/email-protection)", "role": "agent", "agent_brand_ids": [8119246973690, 8119246973691, 8119246973692]}, {"name": "Woger Rilco", "email": "[[email protected]](/cdn-cgi/l/email-protection)", "role": "admin"}]}' \  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/users/create_many"	method := "POST"	payload := strings.NewReader(`{  "users": [    {      "agent_brand_ids": [        8119246973690,        8119246973691,        8119246973692      ],      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "name": "Roger Wilco",      "organization_id": 567812345,      "role": "agent"    },    {      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "name": "Woger Rilco",      "role": "admin"    }  ]}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/create_many")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"users\": [    {      \"agent_brand_ids\": [        8119246973690,        8119246973691,        8119246973692      ],      \"email\": \"roge@example.org\",      \"name\": \"Roger Wilco\",      \"organization_id\": 567812345,      \"role\": \"agent\"    },    {      \"email\": \"woge@example.org\",      \"name\": \"Woger Rilco\",      \"role\": \"admin\"    }  ]}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "users": [    {      "agent_brand_ids": [        8119246973690,        8119246973691,        8119246973692      ],      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "name": "Roger Wilco",      "organization_id": 567812345,      "role": "agent"    },    {      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "name": "Woger Rilco",      "role": "admin"    }  ]});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/users/create_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/create_many"
    payload = json.loads("""{  "users": [    {      "agent_brand_ids": [        8119246973690,        8119246973691,        8119246973692      ],      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "name": "Roger Wilco",      "organization_id": 567812345,      "role": "agent"    },    {      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "name": "Woger Rilco",      "role": "admin"    }  ]}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/create_many")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "users": [    {      "agent_brand_ids": [        8119246973690,        8119246973691,        8119246973692      ],      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "name": "Roger Wilco",      "organization_id": 567812345,      "role": "agent"    },    {      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "name": "Woger Rilco",      "role": "admin"    }  ]})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_status": {    "id": "82de0b044094f0c67893ac9fe64f1a99",    "message": "Completed at 2018-03-08 10:07:04 +0000",    "progress": 2,    "results": [      {        "action": "update",        "id": 244,        "status": "Updated",        "success": true      },      {        "action": "update",        "id": 245,        "status": "Updated",        "success": true      }    ],    "status": "completed",    "total": 2,    "url": "https://example.zendesk.com/api/v2/job_statuses/82de0b0467893ac9fe64f1a99"  }}

### Create Or Update User

  * `POST /api/v2/users/create_or_update`


Creates a user if the user does not already exist, or updates an existing user identified by e-mail address or external ID.

If you don't specify a role parameter, the new user is assigned the role of end user.

If you need to create users without sending out a verification email, include a `"skip_verify_email": true` property in the body.

#### External ID Case Sensitivity

When providing an external id to identify an existing user to update, the search for the user record is not case sensitive.

However, if an existing user is found, the system will update the user's external id to match the case of the external id used to find the user.

#### Response Status Code

  * If the user already exists in Zendesk, a successful request returns a 200 OK status code.
  * If the user does not exist in Zendesk and is created, the request returns a 201 Created status code.
  * In both cases, the API responds with a JSON body containing the full user object, which includes the user's id and the fully-resolved URL to the user resource.


Example response:


    {  "user": {    "id": 8929981612030,    "url": "https://{subdomain}.zendesk.com/api/v2/users/8929981612030",  ...  }}

#### Allowed For

  * Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage end users or team members


#### Example body


    {  "user": {    "agent_brand_ids": [      8119246973690,      8119246973691,      8119246973692    ],    "custom_role_id": 123456,    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "identities": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "twitter",        "value": "tester84"      }    ],    "name": "Roger Wilco",    "organization": {      "name": "VIP Customers"    },    "role": "agent"  }}

#### Limits

This endpoint has its own rate limit that is different from the account wide rate limit. When calls are made to this endpoint, this limit will be consumed and you will get a `429 Too Many Requests` response code if the allocation is exhausted.

##### Headers

API responses include usage limit information in the headers for this endpoint.


    Zendesk-RateLimit-create-update-user: total={number}; remaining={number}; resets={number}

Within this header, âTotalâ signifies the initial allocation, âRemainingâ indicates the remaining allowance for the current interval, and âResetsâ denotes the wait time in seconds before the limit refreshes. You can see the Total, and Interval values in the below table.

##### Details

The rate limit is 5 requests per minute for each unique end user profile. For example, you can make 1 call per second as long as you make five calls for one user and five calls for another user. The rate limiting mechanism behaves as described in [Usage Limits](/api-reference/introduction/rate-limits/#monitoring-your-request-activity) in the API introduction. Zendesk recommends that you obey the Retry-After header values.

Rate limit for creating or updating a single user. If you need to update many users, consider the create_or_update_many endpoint.

Rate Limits| Scopes| Interval| Sandbox| Trial| Default
---|---|---|---|---|---
Standard| Account| 1 second| 1| 1| 1
Standard| User| 1 minute| 5| 5| 5

"Default" applies to all Zendesk suite and support plans. Please refer to the [general account limits](https://developer.zendesk.com/api-reference/introduction/rate-limits) for more information.

#### Code Samples

**cURL**


    # Existing user identified by e-mail address:curl https://{subdomain}.zendesk.com/api/v2/users/create_or_update \  -d '{"user": {"name": "Roger Wilco", "email": "[[email protected]](/cdn-cgi/l/email-protection)", "agent_brand_ids": [1, 2, 3]}}' \  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}
    # Existing user identified by external ID:curl https://{subdomain}.zendesk.com/api/v2/users/create_or_update \  -d '{"user": {"external_id": "account_12345", "name": "Roger Wilco", "email": "[[email protected]](/cdn-cgi/l/email-protection)", "agent_brand_ids": [1, 2, 3]}}' \  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}
    # The user can also be added to a named organization.curl https://{subdomain}.zendesk.com/api/v2/users/create_or_update \  -d '{"user": {"name": "Roger Wilco", "email": "[[email protected]](/cdn-cgi/l/email-protection)", "organization": {"name": "VIP Customers"}, "agent_brand_ids": [8119246973690, 8119246973691, 8119246973692]}}' \  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/users/create_or_update"	method := "POST"	payload := strings.NewReader(`{  "user": {    "agent_brand_ids": [      8119246973690,      8119246973691,      8119246973692    ],    "custom_role_id": 123456,    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "identities": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "twitter",        "value": "tester84"      }    ],    "name": "Roger Wilco",    "organization": {      "name": "VIP Customers"    },    "role": "agent"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/create_or_update")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"user\": {    \"agent_brand_ids\": [      8119246973690,      8119246973691,      8119246973692    ],    \"custom_role_id\": 123456,    \"email\": \"roge@example.org\",    \"identities\": [      {        \"type\": \"email\",        \"value\": \"test@user.com\"      },      {        \"type\": \"twitter\",        \"value\": \"tester84\"      }    ],    \"name\": \"Roger Wilco\",    \"organization\": {      \"name\": \"VIP Customers\"    },    \"role\": \"agent\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "user": {    "agent_brand_ids": [      8119246973690,      8119246973691,      8119246973692    ],    "custom_role_id": 123456,    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "identities": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "twitter",        "value": "tester84"      }    ],    "name": "Roger Wilco",    "organization": {      "name": "VIP Customers"    },    "role": "agent"  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/users/create_or_update',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/create_or_update"
    payload = json.loads("""{  "user": {    "agent_brand_ids": [      8119246973690,      8119246973691,      8119246973692    ],    "custom_role_id": 123456,    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "identities": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "twitter",        "value": "tester84"      }    ],    "name": "Roger Wilco",    "organization": {      "name": "VIP Customers"    },    "role": "agent"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/create_or_update")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "user": {    "agent_brand_ids": [      8119246973690,      8119246973691,      8119246973692    ],    "custom_role_id": 123456,    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "identities": [      {        "type": "email",        "value": "[[email protected]](/cdn-cgi/l/email-protection)"      },      {        "type": "twitter",        "value": "tester84"      }    ],    "name": "Roger Wilco",    "organization": {      "name": "VIP Customers"    },    "role": "agent"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "user": {    "custom_role_id": 123456,    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "id": 9873843,    "name": "Roger Wilco",    "organization_id": 57542,    "role": "agent",    "role_type": 0  }}

**201 Created**


    // Status 201 Created
    {  "user": {    "custom_role_id": 123456,    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "id": 9873843,    "name": "Roger Wilco",    "organization_id": 57542,    "role": "agent",    "role_type": 0  }}

### Create Or Update Many Users

  * `POST /api/v2/users/create_or_update_many`


Accepts an array of up to 100 user objects. For each user, the user is created if it does not already exist, or the existing user is updated.

**Note** : To protect the data in your Zendesk account, bulk user imports are not enabled by default in Zendesk accounts. The account owner must contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to enable the imports. A 403 Forbidden error is returned if data imports are not enabled.

Each individual user object can identify an existing user by `email` or by `external_id`.

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.

#### Allowed For

  * Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage end users or team members


#### Example body


    {  "users": [    {      "agent_brand_ids": [        8119246973690,        8119246973691,        8119246973692      ],      "custom_role_id": 123456,      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "identities": [        {          "type": "email",          "value": "[[email protected]](/cdn-cgi/l/email-protection)"        },        {          "type": "twitter",          "value": "tester84"        }      ],      "name": "Roger Wilco",      "organization": {        "name": "VIP Customers"      },      "role": "agent"    },    {      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "external_id": "account_54321",      "name": "Woger Rilco",      "role": "admin"    }  ]}

#### Code Samples

**cURL**


    # Existing user identified by e-mail address:curl https://{subdomain}.zendesk.com/api/v2/users/create_or_update_many \  -d '{"users": [{"name": "Roger Wilco", "email": "[[email protected]](/cdn-cgi/l/email-protection)", "role": "agent", "agent_brand_ids": [8119246973690, 8119246973691, 8119246973692]}, {"external_id": "account_54321", "name": "Woger Rilco", "email": "[[email protected]](/cdn-cgi/l/email-protection)", "role": "admin"}]}' \  -H "Content-Type: application/json" -X POST \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/users/create_or_update_many"	method := "POST"	payload := strings.NewReader(`{  "users": [    {      "agent_brand_ids": [        8119246973690,        8119246973691,        8119246973692      ],      "custom_role_id": 123456,      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "identities": [        {          "type": "email",          "value": "[[email protected]](/cdn-cgi/l/email-protection)"        },        {          "type": "twitter",          "value": "tester84"        }      ],      "name": "Roger Wilco",      "organization": {        "name": "VIP Customers"      },      "role": "agent"    },    {      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "external_id": "account_54321",      "name": "Woger Rilco",      "role": "admin"    }  ]}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/create_or_update_many")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"users\": [    {      \"agent_brand_ids\": [        8119246973690,        8119246973691,        8119246973692      ],      \"custom_role_id\": 123456,      \"email\": \"roge@example.org\",      \"identities\": [        {          \"type\": \"email\",          \"value\": \"test@user.com\"        },        {          \"type\": \"twitter\",          \"value\": \"tester84\"        }      ],      \"name\": \"Roger Wilco\",      \"organization\": {        \"name\": \"VIP Customers\"      },      \"role\": \"agent\"    },    {      \"email\": \"woge@example.org\",      \"external_id\": \"account_54321\",      \"name\": \"Woger Rilco\",      \"role\": \"admin\"    }  ]}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "users": [    {      "agent_brand_ids": [        8119246973690,        8119246973691,        8119246973692      ],      "custom_role_id": 123456,      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "identities": [        {          "type": "email",          "value": "[[email protected]](/cdn-cgi/l/email-protection)"        },        {          "type": "twitter",          "value": "tester84"        }      ],      "name": "Roger Wilco",      "organization": {        "name": "VIP Customers"      },      "role": "agent"    },    {      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "external_id": "account_54321",      "name": "Woger Rilco",      "role": "admin"    }  ]});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/users/create_or_update_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/create_or_update_many"
    payload = json.loads("""{  "users": [    {      "agent_brand_ids": [        8119246973690,        8119246973691,        8119246973692      ],      "custom_role_id": 123456,      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "identities": [        {          "type": "email",          "value": "[[email protected]](/cdn-cgi/l/email-protection)"        },        {          "type": "twitter",          "value": "tester84"        }      ],      "name": "Roger Wilco",      "organization": {        "name": "VIP Customers"      },      "role": "agent"    },    {      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "external_id": "account_54321",      "name": "Woger Rilco",      "role": "admin"    }  ]}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/create_or_update_many")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "users": [    {      "agent_brand_ids": [        8119246973690,        8119246973691,        8119246973692      ],      "custom_role_id": 123456,      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "identities": [        {          "type": "email",          "value": "[[email protected]](/cdn-cgi/l/email-protection)"        },        {          "type": "twitter",          "value": "tester84"        }      ],      "name": "Roger Wilco",      "organization": {        "name": "VIP Customers"      },      "role": "agent"    },    {      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "external_id": "account_54321",      "name": "Woger Rilco",      "role": "admin"    }  ]})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_status": {    "id": "82de0b044094f0c67893ac9fe64f1a99",    "message": "Completed at 2018-03-08 10:07:04 +0000",    "progress": 2,    "results": [      {        "action": "update",        "id": 244,        "status": "Updated",        "success": true      },      {        "action": "update",        "id": 245,        "status": "Updated",        "success": true      }    ],    "status": "completed",    "total": 2,    "url": "https://example.zendesk.com/api/v2/job_statuses/82de0b0467893ac9fe64f1a99"  }}

### Request User Create

  * `POST /api/v2/users/request_create`


Sends the owner a reminder email to update their subscription so more agents can be created.

#### Allowed For

  * Agents


#### Example body


    {  "user": {    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "name": "Roger Wilco"  }}

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/request_create \  -d '{"user": {"name": "Roger Wilco", "email": "[[email protected]](/cdn-cgi/l/email-protection)"}}' \  -H "Content-Type: application/json" \  -X POST -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/users/request_create"	method := "POST"	payload := strings.NewReader(`{  "user": {    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "name": "Roger Wilco"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/request_create")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"user\": {    \"email\": \"roge@example.org\",    \"name\": \"Roger Wilco\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "user": {    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "name": "Roger Wilco"  }});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/users/request_create',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/request_create"
    payload = json.loads("""{  "user": {    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "name": "Roger Wilco"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/request_create")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "user": {    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "name": "Roger Wilco"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    null

### Update User

  * `PUT /api/v2/users/{user_id}`


#### Specifying email and verified attributes

  * If both `email` and `verified` attributes are provided, the provided email is added to the user as a secondary email with the `verified` property set to the specified value. The primary email remains unmodified
  * If only `email` is provided, the provided email is added to the user as a secondary email with the `verified` property set to false. The primary email remains unmodified
  * If only `verified` is provided, the `verified` property of the primary email identity is set to the given value


#### Suspending a user

You can suspend a user by setting its `suspended` attribute to true.

When a user is suspended, the user is not allowed to sign in to Help Center and all further tickets are suspended.

#### Updating a user's profile image

You can update a user's profile image by uploading a local file or by referring to an image hosted on a different website. The second option may take a few minutes to process.

#### Updating a user's phone number

If a user doesn't have a phone number and a `phone` property is provided:

  * If the phone number is unique, it is added as a [direct line](/api-reference/ticketing/users/users/#phone-number) and a [user identity](/api-reference/ticketing/users/user_identities/) is created
  * If the phone number is not unique, it is added as a [shared number](/api-reference/ticketing/users/users/#phone-number) and a user identity is not created


If a user has a shared number and a `phone` property is provided:

  * If the phone number is unique, it is added as a direct line and a user identity is created
  * If the phone number is not unique, it is added as another shared number and a user identity is not created


If the user has a direct line, and a `phone` property is provided, a user identity is created and a secondary phone number is added.

#### Rate Limit

The rate limit for updating a single, unique user is 5 requests per minute. The rate limiting mechanism behaves as described in [Usage Limits](/api-reference/ticketing/account-configuration/usage_limits/#monitoring-your-request-activity) in the API introduction. Zendesk recommends that you obey the Retry-After header values.

#### Allowed For

  * Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage end users or team members


Agents can only update end users. Administrators can update end users, agents, and administrators.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user

#### Example body


    {  "user": {    "name": "Roger Wilco II"  }}

#### Limits

This endpoint has its own rate limit that is different from the account wide rate limit. When calls are made to this endpoint, this limit will be consumed and you will get a `429 Too Many Requests` response code if the allocation is exhausted.

##### Headers

API responses include usage limit information in the headers for this endpoint.


    Zendesk-RateLimit-create-update-user: total={number}; remaining={number}; resets={number}

Within this header, âTotalâ signifies the initial allocation, âRemainingâ indicates the remaining allowance for the current interval, and âResetsâ denotes the wait time in seconds before the limit refreshes. You can see the Total, and Interval values in the below table.

##### Details

The rate limit is 5 requests per minute for each unique end user profile. For example, you can make 1 call per second as long as you make five calls for one user and five calls for another user. The rate limiting mechanism behaves as described in [Usage Limits](/api-reference/introduction/rate-limits/#monitoring-your-request-activity) in the API introduction. Zendesk recommends that you obey the Retry-After header values.

Rate limit for creating or updating a single user. If you need to update many users, consider the create_or_update_many endpoint.

Rate Limits| Scopes| Interval| Sandbox| Trial| Default
---|---|---|---|---|---
Standard| Account| 1 second| 1| 1| 1
Standard| User| 1 minute| 5| 5| 5

"Default" applies to all Zendesk suite and support plans. Please refer to the [general account limits](https://developer.zendesk.com/api-reference/introduction/rate-limits) for more information.

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id} \  -d '{"user": {"name": "Roger Wilco II"}}' \  -H "Content-Type: application/json" -X PUT \  -v -u {email_address}/token:{api_token}
    # Suspending an usercurl https://{subdomain}.zendesk.com/api/v2/users/{user_id} \  -d '{"user": {"suspended": true}}' \  -H "Content-Type: application/json" -X PUT \  -v -u {email_address}/token:{api_token}
    # Uploading a local file to usercurl https://{subdomain}.zendesk.com/api/v2/users/{user_id} \  -F "user[photo][uploaded_data]=@/path/to/profile/image.jpg" \  -v -u {email_address}/token:{api_token} -X PUT
    # Setting a remote image URL:curl https://{subdomain}.zendesk.com/api/v2/users/{user_id} \  -d '{"user": {"remote_photo_url": "http://link.to/profile/image.png"}}' \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} -X PUT

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436"	method := "PUT"	payload := strings.NewReader(`{  "user": {    "name": "Roger Wilco II"  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"user\": {    \"name\": \"Roger Wilco II\"  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "user": {    "name": "Roger Wilco II"  }});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/users/35436',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436"
    payload = json.loads("""{  "user": {    "name": "Roger Wilco II"  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "user": {    "name": "Roger Wilco II"  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "user": {    "id": 9873843,    "name": "Roger Wilco II"  }}

### Update Many Users

  * `PUT /api/v2/users/update_many`


Bulk or batch updates up to 100 users.

#### Bulk update

To make the same change to multiple users, use the following endpoint and data format:

`https://{subdomain}.zendesk.com/api/v2/users/update_many?ids=1,2,3`


    {  "user": {    "organization_id": 1  }}

#### Batch update

To make different changes to multiple users, use the following endpoint and data format:

`https://{subdomain}.zendesk.com/api/v2/users/update_many`


    {  "users": [    { "id": 10071, "name": "New Name", "organization_id": 1 },    { "id": 12307, "verified": true }  ]}

#### Allowed For

  * Agents, with restrictions


Agents can only update end users. Administrators can update end users, agents, and administrators.

#### Response

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
external_ids| string| Query| false| External Id of the users to update. Comma separated
ids| string| Query| false| Id of the users to update. Comma separated

#### Example body


    {  "user": {    "organization_id": 1  }}

#### Code Samples

**cURL**


    # Bulk updatecurl https://{subdomain}.zendesk.com/api/v2/users/update_many?ids=1,2,3 \  -d '{"user": {"organization_id": 1}}' \  -H "Content-Type: application/json" -X PUT \  -v -u {email_address}/token:{api_token}
    # Batch updatecurl https://{subdomain}.zendesk.com/api/v2/users/update_many \  -d '{"users": [{"id": 10071, "name": "New Name", "organization_id": 1}, {"external_id": "123", "verified": true}]}' \  -H "Content-Type: application/json" -X PUT \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/users/update_many?external_ids=abc%2Cdef%2Cghi&ids=1%2C2%2C3"	method := "PUT"	payload := strings.NewReader(`{  "user": {    "organization_id": 1  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/update_many")		.newBuilder()		.addQueryParameter("external_ids", "abc,def,ghi")		.addQueryParameter("ids", "1,2,3");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"user\": {    \"organization_id\": 1  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "user": {    "organization_id": 1  }});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/users/update_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'external_ids': 'abc%2Cdef%2Cghi',    'ids': '1%2C2%2C3',  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/update_many?external_ids=abc%2Cdef%2Cghi&ids=1%2C2%2C3"
    payload = json.loads("""{  "user": {    "organization_id": 1  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/update_many")uri.query = URI.encode_www_form("external_ids": "abc,def,ghi", "ids": "1,2,3")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "user": {    "organization_id": 1  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_status": {    "id": "82de0b044094f0c67893ac9fe64f1a99",    "message": "Completed at 2018-03-08 10:07:04 +0000",    "progress": 2,    "results": [      {        "action": "update",        "id": 244,        "status": "Updated",        "success": true      },      {        "action": "update",        "id": 245,        "status": "Updated",        "success": true      }    ],    "status": "completed",    "total": 2,    "url": "https://example.zendesk.com/api/v2/job_statuses/82de0b0467893ac9fe64f1a99"  }}

### Merge End Users

  * `PUT /api/v2/users/{user_id}/merge`


Merges the end user specified in the path parameter into the existing end user specified in the request body.

Any two end users can be merged with the exception of end users created by sharing agreements.

To be eligible for merging, the user in the path parameter must be a requester on 10,000 or fewer tickets. Otherwise, the merge will be blocked.

Agents, admins, and users with more than 10,000 requested tickets cannot be merged.

For more information about how user data is merged, see [Merging a user's duplicate account](https://support.zendesk.com/hc/en-us/articles/4408887695898) in Zendesk help.

#### Allowed For

  * Admins or agents with permission to edit end users


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user

#### Example body


    {  "user": {    "id": 35436  }}

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/merge \  -d '{"user": {"id": 35436}}' \  -H "Content-Type: application/json" -X PUT  \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436/merge"	method := "PUT"	payload := strings.NewReader(`{  "user": {    "id": 35436  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436/merge")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"user\": {    \"id\": 35436  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "user": {    "id": 35436  }});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/users/35436/merge',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436/merge"
    payload = json.loads("""{  "user": {    "id": 35436  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436/merge")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "user": {    "id": 35436  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "user": {    "id": 35436,    "name": "Johnny Agent"  }}

### Delete User

  * `DELETE /api/v2/users/{user_id}`


Deletes the user and associated records from the account.

**Warning** :

  * Deleted users are not recoverable.
  * Both agents and administrators can soft delete users in the agent interface in Zendesk Support. Agents with permission can delete end users, while administrators can delete all users except the account owner.


To comply with GDPR, a further step is needed. See [Permanently Delete User](/api-reference/ticketing/users/users/#permanently-delete-user).

#### Allowed For

  * Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage end users or team members


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id} \  -v -u {email_address}/token:{api_token} \  -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/users/35436',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "user": {    "active": false,    "id": 9873843,    "name": "Roger Wilco II"  }}

### Bulk Delete Users

  * `DELETE /api/v2/users/destroy_many`


Accepts a comma-separated list of up to 100 user ids.

The request takes an `ids` or an `external_ids` query parameter.

#### Allowed for

  * Admins


#### Response

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
external_ids| string| Query| false| External Id of the users to delete. Comma separated
ids| string| Query| false| Id of the users to delete. Comma separated

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/destroy_many?ids=1,2,3 \  -v -u {email_address}/token:{api_token} -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/destroy_many?external_ids=abc%2Cdef%2Cghi&ids=1%2C2%2C3"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/destroy_many")		.newBuilder()		.addQueryParameter("external_ids", "abc,def,ghi")		.addQueryParameter("ids", "1,2,3");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/users/destroy_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'external_ids': 'abc%2Cdef%2Cghi',    'ids': '1%2C2%2C3',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/destroy_many?external_ids=abc%2Cdef%2Cghi&ids=1%2C2%2C3"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/destroy_many")uri.query = URI.encode_www_form("external_ids": "abc,def,ghi", "ids": "1,2,3")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "job_status": {    "id": "82de0b044094f0c67893ac9fe64f1a99",    "message": "Completed at 2018-03-08 10:07:04 +0000",    "progress": 2,    "results": [      {        "action": "delete",        "id": 244,        "status": "Deleted",        "success": true      },      {        "action": "delete",        "id": 245,        "status": "Deleted",        "success": true      }    ],    "status": "completed",    "total": 2,    "url": "https://example.zendesk.com/api/v2/job_statuses/82de0b0467893ac9fe64f1a99"  }}

### Permanently Delete User

  * `DELETE /api/v2/deleted_users/{deleted_user_id}`


Before permanently deleting a user, you must delete the user first. See [Delete User](/api-reference/ticketing/users/users/#delete-user).

WARNING: Permanently deleting a user deletes all of their information. This information is not recoverable.

#### Permanent user deletion rate limit

You can permanently delete 700 users every 10 minutes. The rate limiting mechanism behaves as described in [Rates Limits](/api-reference/introduction/rate-limits/#monitoring-your-request-activity) in the API introduction. Zendesk recommends that you obey the Retry-After header values.

#### Allowed For

  * Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage end users or team members


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
deleted_user_id| integer| Path| true| The ID of the deleted user

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/deleted_users/{id} \  -v -u {email_address}/token:{api_token} \  -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/deleted_users/35436"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/deleted_users/35436")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/deleted_users/35436',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/deleted_users/35436"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/deleted_users/35436")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "deleted_user": {    "active": false,    "created_at": "2019-08-26T02:10:24Z",    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "id": 189304711533,    "locale": "en-US",    "locale_id": 1,    "name": "David",    "organization_id": 360000000008,    "phone": null,    "photo": null,    "role": "end-user",    "shared_phone_number": null,    "time_zone": "Eastern Time (US & Canada)",    "updated_at": "2019-08-26T02:10:27Z",    "url": "https://{subdomain}.zendesk.com/api/v2/deleted_users/189304711533"  }}

### List Deleted Users

  * `GET /api/v2/deleted_users`


Returns deleted users, including permanently deleted users.

If the results contains permanently deleted users, the users' properties that normally contain personal data, such as `email` and `phone`, are null. The `name` property is "Permanently Deleted User".

#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
page| | Query| false| Pagination parameter. Supports both traditional offset and cursor-based pagination: - Traditional: `?page=2` (integer page number) - Cursor: `?page[size]=50&page[after]=cursor` (deepObject with size, after, before) These are mutually exclusive - use one format or the other, not both.
per_page| integer| Query| false| Number of records to return per page. Note: Default and maximum values vary by endpoint. Check endpoint-specific documentation for limits.
sort| string| Query| false| Field to sort results by. Prefix with `-` for descending order. When used with cursor pagination, this determines the cursor ordering. Example: `?sort=name` or `?sort=-created_at`

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/deleted_users \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/deleted_users?page=&per_page=50&sort=name"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/deleted_users")		.newBuilder()		.addQueryParameter("page", "")		.addQueryParameter("per_page", "50")		.addQueryParameter("sort", "name");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/deleted_users',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'page': '',    'per_page': '50',    'sort': 'name',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/deleted_users?page=&per_page=50&sort=name"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/deleted_users")uri.query = URI.encode_www_form("page": "", "per_page": "50", "sort": "name")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "deleted_users": [    {      "active": false,      "created_at": "2019-08-26T02:10:24Z",      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "id": 189304711533,      "locale": "en-US",      "locale_id": 1,      "name": "David",      "organization_id": 12312312,      "phone": null,      "photo": null,      "role": "end-user",      "shared_phone_number": null,      "time_zone": "Eastern Time (US & Canada)",      "updated_at": "2019-08-26T02:10:27Z",      "url": "https://{subdomain}.zendesk.com/api/v2/deleted_users/189304711533"    },    {      "active": false,      "created_at": "2019-08-26T02:10:28Z",      "email": "[[email protected]](/cdn-cgi/l/email-protection)",      "id": 12204720593,      "locale": "en-US",      "locale_id": 1,      "name": "Linda",      "organization_id": 123123123,      "phone": null,      "photo": null,      "role": "end-user",      "shared_phone_number": null,      "time_zone": "Eastern Time (US & Canada)",      "updated_at": "2019-08-26T02:10:29Z",      "url": "https://{subdomain}.zendesk.com/api/v2/deleted_users/12204720593"    }  ]}

### Count Deleted Users

  * `GET /api/v2/deleted_users/count`


Returns an approximate count of deleted users, including permanently deleted users. If the count exceeds 100,000, it is updated every 24 hours.

The response includes a `refreshed_at` property in a `count` object that contains a timestamp indicating when the count was last updated.

**Note** : When the count exceeds 100,000, `count[refreshed_at]` may occasionally be null. This indicates that the count is being updated in the background, and `count[value]` is limited to 100,000 until the update is complete.

#### Allowed For

  * Agents


#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/deleted_users/count \-v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/deleted_users/count"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/deleted_users/count")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/deleted_users/count',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/deleted_users/count"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/deleted_users/count")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "count": {    "refreshed_at": "2020-04-06T02:18:17Z",    "value": 13  }}

### Show Deleted User

  * `GET /api/v2/deleted_users/{deleted_user_id}`


Returns users that have been deleted but not permanently yet. See Permanently Delete User.

#### Allowed For:

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
deleted_user_id| integer| Path| true| The ID of the deleted user

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/deleted_users/{deleted_user_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/deleted_users/35436"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/deleted_users/35436")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/deleted_users/35436',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/deleted_users/35436"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/deleted_users/35436")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "deleted_user": {    "active": false,    "created_at": "2019-08-26T02:10:24Z",    "email": "[[email protected]](/cdn-cgi/l/email-protection)",    "id": 189304711533,    "locale": "en-US",    "locale_id": 1,    "name": "David",    "organization_id": 360000000008,    "phone": null,    "photo": null,    "role": "end-user",    "shared_phone_number": null,    "time_zone": "Eastern Time (US & Canada)",    "updated_at": "2019-08-26T02:10:27Z",    "url": "https://{subdomain}.zendesk.com/api/v2/deleted_users/189304711533"  }}

### Show Compliance Deletion Statuses

  * `GET /api/v2/users/{user_id}/compliance_deletion_statuses`


Returns the GDPR status for each user per area of compliance. A Zendesk area of compliance is typically a product like "support/explore" but can be more fine-grained for areas within the product lines.

If the user is not in the account, the request returns a 404 status.


    Status: 404{  "error":"RecordNotFound",  "description":"Not found"}

#### Allowed For

  * Agents, with restrictions


#### Pagination

  * Cursor pagination (recommended)
  * Offset pagination


See [Pagination](/api-reference/introduction/pagination/).

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
application| string| Query| false| Area of compliance
user_id| integer| Path| true| The id of the user

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/{id}/compliance_deletion_statuses?application=chat \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436/compliance_deletion_statuses?application=chat"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436/compliance_deletion_statuses")		.newBuilder()		.addQueryParameter("application", "chat");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users/35436/compliance_deletion_statuses',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'application': 'chat',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436/compliance_deletion_statuses?application=chat"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436/compliance_deletion_statuses")uri.query = URI.encode_www_form("application": "chat")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "compliance_deletion_statuses": [    {      "account_subdomain": "accountABC",      "action": "request_deletion",      "application": "all",      "created_at": "2009-07-20T22:55:23Z",      "executer_id": 2000,      "user_id": 1    },    {      "account_subdomain": "accountABC",      "action": "started",      "application": "support",      "created_at": "2009-07-20T22:55:29Z",      "executer_id": null,      "user_id": 1    },    {      "account_subdomain": "accountABC",      "action": "complete",      "application": "support",      "created_at": "2009-07-20T22:57:02Z",      "executer_id": null,      "user_id": 1    },    {      "account_subdomain": "accountABC",      "action": "started",      "application": "chat",      "created_at": "2009-07-21T02:51:18Z",      "executer_id": null,      "user_id": 1    }  ]}

### Autocomplete Users by Request Body

  * `POST /api/v2/users/autocomplete`


Returns an array of users whose name starts with the value specified in the `name` property in the request body. It only returns users with no foreign identities.

This endpoint accepts the same parameters as the GET method but they are specified in the request body instead of the query string.

#### Allowed For

  * Agents


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
filter| string| Query| false| Filter to apply to autocomplete results. Common values: `assignable`, `requester`.
include| string| Query| false| Sideloads to include in the response. Accepts a comma-separated list of values. See [Sideloading](/api-reference/ticketing/users/users/#sideloading).
per_page| integer| Query| false| Number of results to return.

#### Example body


    {  "name": "gil"}

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/autocomplete \  -d '{"name":"gil"}' \  -H "Content-Type: application/json" \  -u {email_address}/token:{api_token} \  -X POST

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/users/autocomplete?filter=&include=roles%2Corganizations&per_page="	method := "POST"	payload := strings.NewReader(`{  "name": "gil"}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/autocomplete")		.newBuilder()		.addQueryParameter("filter", "")		.addQueryParameter("include", "roles,organizations")		.addQueryParameter("per_page", "");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"name\": \"gil\"}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "name": "gil"});
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/users/autocomplete',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'filter': '',    'include': 'roles%2Corganizations',    'per_page': '',  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/autocomplete?filter=&include=roles%2Corganizations&per_page="
    payload = json.loads("""{  "name": "gil"}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/autocomplete")uri.query = URI.encode_www_form("filter": "", "include": "roles,organizations", "per_page": "")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")request.body = %q({  "name": "gil"})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "users": [    {      "id": 35436,      "name": "Robert Jones",      "notes": "sigil issue"    },    {      "id": 9873843,      "name": "Terry Gilliam"    }  ]}

**400 Bad Request**


    // Status 400 Bad Request
    {  "description": "Invalid query syntax",  "error": "Query Error"}

**500 Internal Server Error**


    // Status 500 Internal Server Error
    {  "description": "Service temporarily unavailable",  "error": "Unavailable"}

### Logout many users

  * `POST /api/v2/users/logout_many`


Accepts a comma-separated list of up to 100 user ids.

#### Allowed For:

  * Admins


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
ids| string| Query| false| Accepts a comma-separated list of up to 100 user ids.

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/logout_many?ids=345678,901234 \  -v -u {email_address}/token:{api_token} \  -X POST

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/logout_many?ids=1%2C2"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/logout_many")		.newBuilder()		.addQueryParameter("ids", "1,2");RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/users/logout_many',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  params: {    'ids': '1%2C2',  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/logout_many?ids=1%2C2"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/logout_many")uri.query = URI.encode_www_form("ids": "1,2")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**202 Accepted**


    // Status 202 Accepted
    null

### Show Current User Settings

  * `GET /api/v2/users/me/settings`


Returns the settings for the currently authenticated user. This includes UI preferences for onboarding, tooltips, keyboard shortcuts, theme preferences, and other feature toggles.

#### Allowed For

  * Agents


#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/me/settings \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/me/settings"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/me/settings")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users/me/settings',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/me/settings"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/me/settings")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "settings": {    "admin_center": {      "has_admin_center_side_nav_open": true,      "has_seen_admin_center_dark_mode_banner": false    },    "lotus": {      "agent_workspace_theme_preference": "0",      "agent_workspace_theme_preference_for_conversation_panel": "0",      "keyboard_shortcuts_enabled": false,      "macro_shortcuts_enabled": false,      "show_onboarding_tooltips": true,      "show_reporting_video_tutorial": true,      "show_welcome_dialog": true,      "two_factor_authentication": false    }  }}

### Update Current User Settings

  * `PUT /api/v2/users/me/settings`


Updates the settings for the currently authenticated user. This includes UI preferences for onboarding, tooltips, keyboard shortcuts, theme preferences, and other feature toggles.

Settings are grouped into:

  * **Support** : Support UI preferences (onboarding, tooltips, shortcuts, theme)
  * **admin_center** : Admin Center UI preferences (navigation, onboarding)
  * **shared_views_order** : Optional array of view IDs for custom ordering


Only the specified settings will be updated. Other settings will remain unchanged.

#### Allowed For

  * Agents


#### Example body


    {  "settings": {    "admin_center": {      "has_admin_center_side_nav_open": true    },    "lotus": {      "agent_workspace_theme_preference": "1",      "keyboard_shortcuts_enabled": true,      "show_onboarding_tooltips": false    }  }}

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/me/settings \  -d '{"settings": {"lotus": {"keyboard_shortcuts_enabled": true, "agent_workspace_theme_preference": "1"}}}' \  -H "Content-Type: application/json" \  -v -u {email_address}/token:{api_token} \  -X PUT

**Go**


    import (	"fmt"	"io"	"net/http"	"strings")
    func main() {	url := "https://example.zendesk.com/api/v2/users/me/settings"	method := "PUT"	payload := strings.NewReader(`{  "settings": {    "admin_center": {      "has_admin_center_side_nav_open": true    },    "lotus": {      "agent_workspace_theme_preference": "1",      "keyboard_shortcuts_enabled": true,      "show_onboarding_tooltips": false    }  }}`)	req, err := http.NewRequest(method, url, payload)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/me/settings")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""{  \"settings\": {    \"admin_center\": {      \"has_admin_center_side_nav_open\": true    },    \"lotus\": {      \"agent_workspace_theme_preference\": \"1\",      \"keyboard_shortcuts_enabled\": true,      \"show_onboarding_tooltips\": false    }  }}""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');var data = JSON.stringify({  "settings": {    "admin_center": {      "has_admin_center_side_nav_open": true    },    "lotus": {      "agent_workspace_theme_preference": "1",      "keyboard_shortcuts_enabled": true,      "show_onboarding_tooltips": false    }  }});
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/users/me/settings',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },  data : data,};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsimport jsonfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/me/settings"
    payload = json.loads("""{  "settings": {    "admin_center": {      "has_admin_center_side_nav_open": true    },    "lotus": {      "agent_workspace_theme_preference": "1",      "keyboard_shortcuts_enabled": true,      "show_onboarding_tooltips": false    }  }}""")headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers,	json=payload)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/me/settings")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")request.body = %q({  "settings": {    "admin_center": {      "has_admin_center_side_nav_open": true    },    "lotus": {      "agent_workspace_theme_preference": "1",      "keyboard_shortcuts_enabled": true,      "show_onboarding_tooltips": false    }  }})email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "settings": {    "admin_center": {      "has_admin_center_side_nav_open": true,      "has_seen_admin_center_dark_mode_banner": false    },    "lotus": {      "agent_workspace_theme_preference": "0",      "agent_workspace_theme_preference_for_conversation_panel": "0",      "keyboard_shortcuts_enabled": false,      "macro_shortcuts_enabled": false,      "show_onboarding_tooltips": true,      "show_reporting_video_tutorial": true,      "show_welcome_dialog": true,      "two_factor_authentication": false    }  }}

**400 Bad Request**


    // Status 400 Bad Request
    {  "error": "BadRequest"}

**401 Unauthorized**


    // Status 401 Unauthorized
    {  "error": "Unauthorized"}

### Get Full User Entitlements

  * `GET /api/v2/users/{user_id}/entitlements/full`


Returns the full entitlements for all Zendesk products (Explore, Voice, Knowledge, Live Chat) for the specified user. This includes the role name and active status for each product.

An entitlement is only considered active if both of the following conditions apply: the user has access and the product is active on the account.

#### Allowed For

  * Agents


#### OAuth Scopes

Requires one of the following OAuth scopes: `users:read` or `read`

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Path| true| The id of the user

#### Code Samples

**cURL**


    curl https://{subdomain}.zendesk.com/api/v2/users/{user_id}/entitlements/full \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/users/35436/entitlements/full"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/users/35436/entitlements/full")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/users/35436/entitlements/full',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/users/35436/entitlements/full"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/users/35436/entitlements/full")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "entitlements": {    "chat": {      "is_active": true,      "name": "admin"    },    "explore": {      "is_active": true,      "name": "admin"    },    "guide": {      "is_active": true,      "name": "admin"    },    "talk": {      "is_active": true,      "name": "lead"    }  }}

**404 Not Found**


    // Status 404 Not Found
    {  "error": "RecordNotFound"}

**503 Service Unavailable**


    // Status 503 Service Unavailable
    {  "error": "ServiceUnavailable"}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)