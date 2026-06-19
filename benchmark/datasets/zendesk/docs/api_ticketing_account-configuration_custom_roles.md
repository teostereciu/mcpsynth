# Custom Agent Roles

*Source: https://developer.zendesk.com/api-reference/ticketing/account-configuration/custom_roles/*

---

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/custom_roles/#json-format)
  * [List Custom Roles](/api-reference/ticketing/account-configuration/custom_roles/#list-custom-roles)
  * [Show Custom Role](/api-reference/ticketing/account-configuration/custom_roles/#show-custom-role)
  * [Create Custom Role](/api-reference/ticketing/account-configuration/custom_roles/#create-custom-role)
  * [Update Custom Role](/api-reference/ticketing/account-configuration/custom_roles/#update-custom-role)
  * [Delete Custom Role](/api-reference/ticketing/account-configuration/custom_roles/#delete-custom-role)


# Custom Agent Roles

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/custom_roles/#json-format)
  * [List Custom Roles](/api-reference/ticketing/account-configuration/custom_roles/#list-custom-roles)
  * [Show Custom Role](/api-reference/ticketing/account-configuration/custom_roles/#show-custom-role)
  * [Create Custom Role](/api-reference/ticketing/account-configuration/custom_roles/#create-custom-role)
  * [Update Custom Role](/api-reference/ticketing/account-configuration/custom_roles/#update-custom-role)
  * [Delete Custom Role](/api-reference/ticketing/account-configuration/custom_roles/#delete-custom-role)


Zendesk Support accounts on the Enterprise plan or above can provide more granular access to their agents by defining custom agent roles. For more information, see [Creating custom roles and assigning agents](https://support.zendesk.com/hc/en-us/articles/203662026) in the Support Help Center.

### JSON format

Custom Agent Roles are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
configuration| object| false| false| Configuration settings for the role. See Configuration
created_at| string| true| false| The time the record was created
description| string| false| false| A description of the role
id| integer| true| false| Automatically assigned on creation
name| string| false| true| Name of the custom role
role_type| integer| true| true| The user's role. 0 stands for a custom agent, 1 for a light agent, 2 for a chat agent, 3 for a contributor, 4 for an admin and 5 for a billing admin. See [Understanding standard agent roles in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4409155971354-Understanding-standard-agent-roles-in-Zendesk-Support) in Zendesk help
team_member_count| integer| true| false| The number of team members assigned to this role
updated_at| string| true| false| The time the record was last updated

#### Configuration

The `configuration` object has the following properties, which are all optional.

Name| Type| Read-only| Comment
---|---|---|---
assign_tickets_to_any_brand| boolean| no| Whether or not the agent can assign tickets to any brand and list all brands associated with an account sorted by name
assign_tickets_to_any_group| boolean| no| Whether or not the agent can assign tickets to any group
chat_access| boolean| yes| Whether or not the agent has access to Chat
custom_objects| object| no| A list of custom object keys mapped to JSON objects that define the agent's permissions (scopes) for each object. Allowed values: "read", "update", "delete", "create". The "read" permission is required if any other scopes are specified. Example: { "shipment": { "scopes": ["read", "update"] } }
end_user_list_access| string| no| Whether or not the agent can view lists of user profiles. Allowed values: "full", "none"
end_user_profile_access| string| no| What the agent can do with end-user profiles. Allowed values: "edit", "edit-within-org", "full", "readonly"
explore_access| string| no| Allowed values: "edit", "full", "none", "readonly"
explore_reports| object| no| See explore_reports
export_views| boolean| no| Whether or not the agent can export views
forum_access_restricted_content| boolean| no|
group_access| boolean| yes| Whether or not the agent can add or modify groups
light_agent| boolean| yes|
macro_access| string| no| What the agent can do with macros. Allowed values: "full", "manage-group", "manage-personal", "readonly"
manage_approval_requests| boolean| no| Whether or not the agent can create and manage approval requests
manage_automations| boolean| no| Whether or not the agent can create and manage automations
manage_business_rules| boolean| no| Whether or not the agent can create and manage schedules and view rules analysis
manage_contextual_workspaces| boolean| no| Whether or not the agent can view, add, and edit contextual workspaces
manage_dynamic_content| boolean| no| Whether or not the agent can access dynamic content
manage_extensions_and_channels| boolean| no| Whether or not the agent can manage channels and extensions
manage_facebook| boolean| no| Whether or not the agent can manage facebook pages
manage_group_memberships| boolean| no| Whether or not the agent can create and manage group memberships
manage_groups| boolean| no| Whether or not the agent can create and modify groups
manage_organization_fields| boolean| no| Whether or not the agent can create and manage organization fields
manage_organizations| boolean| no| Whether or not the agent can create and modify organizations
manage_roles| string| no| Whether or not the agent can create and manage custom roles with the exception of the role they're currently assigned. Doesn't allow agents to update role assignments for other agents. Allowed values: "all-except-self", "none"
manage_skills| boolean| no| Whether or not the agent can create and manage skills
manage_slas| boolean| no| Whether or not the agent can create and manage SLAs
manage_suspended_tickets| boolean| no| Whether or not the agent can manage suspended tickets
manage_team_members| string| no| Whether or not the agent can manage team members. Allows agents to update role assignments for other agents. Allowed values: "all-with-self-restriction", "readonly", "none"
manage_ticket_fields| boolean| no| Whether or not the agent can create and manage ticket fields
manage_ticket_forms| boolean| no| Whether or not the agent can create and manage ticket forms
manage_triggers| boolean| no| Whether or not the agent can create and manage triggers
manage_user_fields| boolean| no| Whether or not the agent can create and manage user fields
moderate_forums| boolean| yes|
organization_editing| boolean| no| Whether or not the agent can add or modify organizations
organization_notes_editing| boolean| yes| Whether or not the agent can add or modify organization notes
report_access| string| no| What the agent can do with reports. Allowed values: "full", "none", "readonly"
side_conversation_create| boolean| no| Whether or not the agent can contribute to side conversations
ticket_access| string| no| What kind of tickets the agent can access. Allowed values: "all", "assigned-only", "within-groups", "within-groups-and-public-groups", "within-organization". Agents must have "all" access to create or edit end users from the Agent Workspace. However, the ability to create or edit end users through the API is determined by the user's role, not by ticket_access.
ticket_comment_access| string| no| What type of comments the agent can make. Allowed values: "public", "none"
ticket_deletion| boolean| no| Whether or not the agent can delete tickets
ticket_editing| boolean| no| Whether or not the agent can edit ticket properties
ticket_merge| boolean| no| Whether or not the agent can merge tickets
ticket_redaction| boolean| no| Whether or not the agent can redact content from tickets. Only applicable to tickets permitted by ticket_access
ticket_tag_editing| boolean| no| Whether or not the agent can edit ticket tags
twitter_search_access| boolean| no|
user_view_access| string| no| What the agent can do with customer lists. Allowed values: "full", "manage-group", "manage-personal", "none", "readonly"
view_access| string| no| What the agent can do with views. Allowed values: "full", "manage-group", "manage-personal", "playonly", "readonly"
view_deleted_tickets| boolean| no| Whether or not the agent can view deleted tickets
view_filter_tickets| boolean| no| Whether or not the agent can view and apply filters to tickets
voice_access| boolean| no| Whether or not the agent can answer and place calls to end users
voice_dashboard_access| boolean| no| Whether or not the agent can view details about calls on the Talk dashboard

#### Explore reports

Legacy version consists of two properties: `ticket_access` and `ticket_access_selected_groups`. Allowed values for `ticket access`: "all", "within-groups", "selected-groups". When `ticket_access` is set to "selected-groups", the `ticket_access_selected_groups` property is used to specify a list of selected group ids that the agent can view tickets from. Example: `{"ticket_access": "selected-groups", "ticket_access_selected_groups": ["1260803907490"]}`.

New version consists of three properties: `groups_ticket_access`, `brands_ticket_access`, `ticket_access_selected_groups` and `ticket_access_selected_brands`. Allowed values for `groups ticket access`: "all", "within-groups", "selected-groups". When `groups_ticket_access` is set to "selected-groups", the `ticket_access_selected_groups` property is used to specify a list of selected group ids that the agent can view tickets from. Allowed values for `brands ticket access`: "all", "within-brands", "selected-brands". When `brands_ticket_access` is set to "selected-brands", the `ticket_access_selected_brands` property is used to specify a list of selected brand ids that the agent can view tickets from. Example: `{ "groups_ticket_access": "selected-groups", "brands_ticket_access": "selected-brands", "ticket_access_selected_groups": ["1260803907490"], "ticket_access_selected_brands": ["19873786"] }`

#### Example


    {  "id":           35436,  "name":         "Partner",  "description":  "Can only make private comments on assigned tickets",  "created_at":   "2012-02-20T22:55:29Z",  "updated_at":   "2012-02-20T22:55:29Z",  "configuration": {    "assign_tickets_to_any_brand":     false,    "assign_tickets_to_any_group":     false,    "chat_access":                     true,    "custom_objects": {      "shipment": {        "scopes": ["read", "update", "delete", "create"]      },      "product": {        "scopes": ["read"]      }    },    "end_user_profile_access":         "readonly",    "explore_access":                  "edit",    "export_views":                     true,    "forum_access":                    "readonly",    "forum_access_restricted_content": false,    "light_agent":                     false,    "macro_access":                    "full",    "manage_approval_requests":        true,    "manage_automations":              true,    "manage_business_rules":           true,    "manage_contextual_workspaces":    false,    "manage_dynamic_content":          false,    "manage_extensions_and_channels":  true,    "manage_facebook":                 false,    "manage_group_memberships":        false,    "manage_groups":                   false,    "manage_organization_fields":      false,    "manage_organizations":            false,    "manage_roles":                    "none",    "manage_skills":                   false,    "manage_slas":                     false,    "manage_suspended_tickets":        false,    "manage_team_members":             "none",    "manage_ticket_fields":            false,    "manage_ticket_forms":             false,    "manage_triggers":                 true,    "manage_user_fields":              false,    "organization_editing":            false,    "organization_notes_editing":      false,    "report_access":                   "none",    "side_conversation_create":        true,    "ticket_access":                   "within-groups",    "ticket_comment_access":           "none",    "ticket_deletion":                 false,    "ticket_redaction":                true,    "view_deleted_tickets":            false,    "ticket_editing":                  true,    "ticket_merge":                    false,    "ticket_tag_editing":              true,    "twitter_search_access":           true,    "view_access":                     "full",    "view_filter_tickets":             false,    "voice_access":                    true,    "voice_dashboard_access":          false  }}

### List Custom Roles

  * `GET /api/v2/custom_roles`


#### Availability

  * Accounts on the Enterprise plan or above


#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/custom_roles \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/custom_roles"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/custom_roles")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/custom_roles',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/custom_roles"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/custom_roles")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "custom_roles": [    {      "configuration": {        "assign_tickets_to_any_group": false,        "chat_access": true,        "end_user_list_access": "full",        "end_user_profile_access": "readonly",        "explore_access": "edit",        "export_views": false,        "forum_access": "readonly",        "forum_access_restricted_content": false,        "group_access": true,        "light_agent": false,        "macro_access": "full",        "manage_business_rules": true,        "manage_contextual_workspaces": false,        "manage_dynamic_content": false,        "manage_extensions_and_channels": true,        "manage_facebook": false,        "manage_organization_fields": false,        "manage_ticket_fields": false,        "manage_ticket_forms": false,        "manage_user_fields": false,        "moderate_forums": false,        "organization_editing": false,        "organization_notes_editing": false,        "report_access": "none",        "side_conversation_create": true,        "ticket_access": "within-groups",        "ticket_comment_access": "none",        "ticket_deletion": false,        "ticket_editing": true,        "ticket_merge": false,        "ticket_tag_editing": true,        "twitter_search_access": true,        "user_view_access": "readonly",        "view_access": "full",        "view_deleted_tickets": false,        "voice_access": true,        "voice_dashboard_access": false      },      "created_at": "2012-03-12T16:32:22Z",      "description": "Advisors manage the workflow and configure the help desk. They create or manage automations, macros, triggers, views, and SLA targets. They also set up channels and extensions. Advisors don't solve tickets, they can only make private comments.",      "id": 16,      "name": "Advisor",      "role_type": 0,      "team_member_count": 10,      "updated_at": "2012-03-12T16:32:22Z"    },    {      "configuration": {        "assign_tickets_to_any_group": false,        "chat_access": true,        "end_user_list_access": "full",        "end_user_profile_access": "readonly",        "explore_access": "edit",        "export_views": true,        "forum_access": "readonly",        "forum_access_restricted_content": false,        "group_access": true,        "light_agent": false,        "macro_access": "full",        "manage_business_rules": true,        "manage_contextual_workspaces": false,        "manage_dynamic_content": false,        "manage_extensions_and_channels": true,        "manage_facebook": false,        "manage_organization_fields": false,        "manage_ticket_fields": false,        "manage_ticket_forms": false,        "manage_user_fields": false,        "moderate_forums": false,        "organization_editing": false,        "organization_notes_editing": false,        "report_access": "none",        "side_conversation_create": true,        "ticket_access": "within-groups",        "ticket_comment_access": "none",        "ticket_deletion": false,        "ticket_editing": true,        "ticket_merge": false,        "ticket_tag_editing": true,        "twitter_search_access": true,        "user_view_access": "readonly",        "view_access": "full",        "view_deleted_tickets": false,        "voice_access": true,        "voice_dashboard_access": false      },      "created_at": "2011-07-20T04:31:29Z",      "description": "A Staff agent's primary role is to solve tickets. They can edit tickets within their groups, view reports, and add or edit personal views and macros.",      "id": 6,      "name": "Staff",      "role_type": 0,      "team_member_count": 10,      "updated_at": "2012-02-02T10:32:59Z"    }  ]}

### Show Custom Role

  * `GET /api/v2/custom_roles/{custom_role_id}`


#### Availability

  * Accounts on the Enterprise plan or above


#### Allowed for

  * Administrators
  * Agents with the `manage_roles` permission


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
custom_role_id| integer| Path| true| The ID of the custom agent role

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/custom_roles/{custom_role_id} \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/custom_roles/10127"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/custom_roles/10127")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/custom_roles/10127',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/custom_roles/10127"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/custom_roles/10127")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "custom_role": {    "configuration": {      "assign_tickets_to_any_group": false,      "chat_access": true,      "end_user_list_access": "full",      "end_user_profile_access": "readonly",      "explore_access": "edit",      "forum_access": "readonly",      "forum_access_restricted_content": false,      "group_access": true,      "light_agent": false,      "macro_access": "full",      "manage_business_rules": true,      "manage_contextual_workspaces": false,      "manage_dynamic_content": false,      "manage_extensions_and_channels": true,      "manage_facebook": false,      "manage_organization_fields": false,      "manage_ticket_fields": false,      "manage_ticket_forms": false,      "manage_user_fields": false,      "moderate_forums": false,      "organization_editing": false,      "organization_notes_editing": false,      "report_access": "none",      "side_conversation_create": true,      "ticket_access": "within-groups",      "ticket_comment_access": "none",      "ticket_deletion": false,      "ticket_editing": true,      "ticket_merge": false,      "ticket_tag_editing": true,      "twitter_search_access": true,      "user_view_access": "readonly",      "view_access": "full",      "view_deleted_tickets": false,      "voice_access": true,      "voice_dashboard_access": false    },    "created_at": "2012-03-12T16:32:22Z",    "description": "sample description",    "id": 10127,    "name": "sample role",    "role_type": 0,    "team_member_count": 10,    "updated_at": "2012-03-12T16:32:22Z"  }}

### Create Custom Role

  * `POST /api/v2/custom_roles`


#### Availability

  * Accounts on the Enterprise plan or above


#### Allowed for

  * Administrators
  * Agents with the `manage_roles` permission


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/custom_roles \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/custom_roles"	method := "POST"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/custom_roles")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("POST", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'POST',  url: 'https://example.zendesk.com/api/v2/custom_roles',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/custom_roles"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"POST",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/custom_roles")request = Net::HTTP::Post.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "custom_role": {    "configuration": {      "assign_tickets_to_any_group": false,      "chat_access": true,      "end_user_list_access": "full",      "end_user_profile_access": "readonly",      "explore_access": "edit",      "forum_access": "readonly",      "forum_access_restricted_content": false,      "group_access": true,      "light_agent": false,      "macro_access": "full",      "manage_business_rules": true,      "manage_contextual_workspaces": false,      "manage_dynamic_content": false,      "manage_extensions_and_channels": true,      "manage_facebook": false,      "manage_organization_fields": false,      "manage_ticket_fields": false,      "manage_ticket_forms": false,      "manage_user_fields": false,      "moderate_forums": false,      "organization_editing": false,      "organization_notes_editing": false,      "report_access": "none",      "side_conversation_create": true,      "ticket_access": "within-groups",      "ticket_comment_access": "none",      "ticket_deletion": false,      "ticket_editing": true,      "ticket_merge": false,      "ticket_tag_editing": true,      "twitter_search_access": true,      "user_view_access": "readonly",      "view_access": "full",      "view_deleted_tickets": false,      "voice_access": true,      "voice_dashboard_access": false    },    "created_at": "2012-03-12T16:32:22Z",    "description": "sample description",    "id": 10127,    "name": "sample role",    "role_type": 0,    "team_member_count": 10,    "updated_at": "2012-03-12T16:32:22Z"  }}

### Update Custom Role

  * `PUT /api/v2/custom_roles/{custom_role_id}`


#### Availability

  * Accounts on the Enterprise plan or above


#### Allowed for

  * Administrators


Agents with the `manage_roles` permission

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
custom_role_id| integer| Path| true| The ID of the custom agent role

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/custom_roles/{custom_role_id} \  -v -u {email_address}/token:{api_token} \  -H "Content-Type: application/json" \  -X PUT \  -d '{ "custom_role": {    "name": "updated sample role",    "description": "sample description",    "configuration": {      "chat_access": true,      "user_view_access": "readonly"    }  }}'

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/custom_roles/10127"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/custom_roles/10127")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/custom_roles/10127',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/custom_roles/10127"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/custom_roles/10127")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "custom_role": {    "configuration": {      "assign_tickets_to_any_group": false,      "chat_access": true,      "end_user_list_access": "full",      "end_user_profile_access": "readonly",      "explore_access": "edit",      "forum_access": "readonly",      "forum_access_restricted_content": false,      "group_access": true,      "light_agent": false,      "macro_access": "full",      "manage_business_rules": true,      "manage_contextual_workspaces": false,      "manage_dynamic_content": false,      "manage_extensions_and_channels": true,      "manage_facebook": false,      "manage_organization_fields": false,      "manage_ticket_fields": false,      "manage_ticket_forms": false,      "manage_user_fields": false,      "moderate_forums": false,      "organization_editing": false,      "organization_notes_editing": false,      "report_access": "none",      "side_conversation_create": true,      "ticket_access": "within-groups",      "ticket_comment_access": "none",      "ticket_deletion": false,      "ticket_editing": true,      "ticket_merge": false,      "ticket_tag_editing": true,      "twitter_search_access": true,      "user_view_access": "readonly",      "view_access": "full",      "view_deleted_tickets": false,      "voice_access": true,      "voice_dashboard_access": false    },    "created_at": "2012-03-12T16:32:22Z",    "description": "sample description",    "id": 10127,    "name": "sample role",    "role_type": 0,    "team_member_count": 10,    "updated_at": "2012-03-12T16:32:22Z"  }}

### Delete Custom Role

  * `DELETE /api/v2/custom_roles/{custom_role_id}`


#### Availability

  * Accounts on the Enterprise plan or above


#### Allowed for

  * Administrators
  * Agents with the `manage_roles` permission


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
custom_role_id| integer| Path| true| The ID of the custom agent role

#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/custom_roles/{custom_role_id} \  -v -u {email_address}/token:{api_token} \  -X DELETE

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/custom_roles/10127"	method := "DELETE"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/custom_roles/10127")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("DELETE", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'DELETE',  url: 'https://example.zendesk.com/api/v2/custom_roles/10127',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/custom_roles/10127"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"DELETE",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/custom_roles/10127")request = Net::HTTP::Delete.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**204 No Content**


    // Status 204 No Content
    null

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)