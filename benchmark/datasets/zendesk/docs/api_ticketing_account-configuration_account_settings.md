# Account Settings

*Source: https://developer.zendesk.com/api-reference/ticketing/account-configuration/account_settings/*

---

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/account_settings/#json-format)
  * [Show Settings](/api-reference/ticketing/account-configuration/account_settings/#show-settings)
  * [Update Account Settings](/api-reference/ticketing/account-configuration/account_settings/#update-account-settings)


# Account Settings

## On this page

  * [JSON format](/api-reference/ticketing/account-configuration/account_settings/#json-format)
  * [Show Settings](/api-reference/ticketing/account-configuration/account_settings/#show-settings)
  * [Update Account Settings](/api-reference/ticketing/account-configuration/account_settings/#update-account-settings)


Account settings are settings specific to your Zendesk account which affect how your account behaves. Some settings are read-only, but others can be updated through the API.

### JSON format

Account Settings are represented as JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Description
---|---|---|---|---
active_features| object| false| false| The active features for an account. See Active Features
agents| object| false| false| Configuration for the agent workspace. See Agents
api| object| false| false| API configuration options. See API
apps| object| false| false| Apps configuration options. See Apps
billing| object| false| false| Billing configuration options. See Billing
branding| object| false| false| Branding settings. See Branding
brands| object| false| false| Brand settings. See Brands
cdn| object| false| false| CDN settings
chat| object| false| false| Zendesk Chat settings. See Chat
cross_sell| object| false| false| Cross Sell settings
device_metadata| object| false| false| End user device settings. See Device Metadata
email| object| false| false| Email settings
google_apps| object| false| false| Google Apps configuration. See G Suite
groups| object| false| false| Group configuration
knowledge| object| false| false| Account's knowledge management and search capabilities. See Knowledge
limits| object| false| false| Account limits configuration. See Limits
localization| object| false| false| Internationalization configuration settings. See Localization
lotus| object| false| false| Support UI settings. See Lotus
messaging_inactivity| object| false| false| Auto-release capacity settings. See Messaging inactivity
metrics| object| false| false| Account metrics settings. See Metrics
onboarding| object| false| false| Onboarding settings
routing| object| false| false| Configuration for routing. See Routing
rule| object| false| false| Rules settings for triggers, macros, views, and automations. See Rules
side_conversations| object| false| false| Side conversations settings
statistics| object| false| false| Account statistics settings. See Statistics
ticket_form| object| false| false| Ticket form settings. See Ticket Form
tickets| object| false| false| Ticket settings. See Tickets
twitter| object| false| false| X (formerly Twitter) settings. See X
user| object| false| false| User settings. See Users
voice| object| false| false| Zendesk Talk settings. See Voice

You can access the following data describing the settings of an account. You can update the settings marked as not read-only.

#### Branding

Name| Type| Read-only| Comment
---|---|---|---
header_color| string| no| HEX of the header color
page_background_color| string| no| HEX of the page background color
tab_background_color| string| no| HEX of tab background color
text_color| string| no| HEX of the text color, usually matched to contrast well with `header_color`
header_logo_url| string| yes| The URL for the custom header logo
favicon_url| string| yes| The URL for the custom favicon

#### Apps

Name| Type| Read-only| Comment
---|---|---|---
use| boolean| yes| The account can use apps
create_private| boolean| yes| The account can create private apps

#### Tickets

Name| Type| Read-only| Comment
---|---|---|---
comments_public_by_default| boolean| no| Comments from agents are public by default
is_first_comment_private_enabled| boolean| no| Allow first comment on tickets to be private
list_newest_comments_first| boolean| no| When viewing a ticket, show the newest comments and events first
collaboration| boolean| yes| CCs may be added to a ticket
private_attachments| boolean| no| Users must sign in to access attachments
email_attachments| boolean| no| Attachments should be sent as real attachments when under the size limit
agent_collision| boolean| yes| Clients should provide an indicator when a ticket is being viewed by ther agent
list_empty_views| boolean| no| Clients should display views with no matching tickets in menus
maximum_personal_views_to_list| number| yes| Maximum number of personal views clients should display in menus
tagging| boolean| no| Tickets may be tagged
markdown_ticket_comments| boolean| no| Whether agent comments should be processed with Markdown
emoji_autocompletion| boolean| no| Whether agent comments should allow for Emoji rendering
agent_ticket_deletion| boolean| no| Whether agents can delete tickets
assign_default_organization| boolean| yes| Whether a ticket is assigned to the requester's default organization in multi-organization mode
agent_invitation_enabled| boolean| no| Whether agent invitation should be allowed for tickets
chat_sla_enablement| boolean| no| Whether the proper SLA behavior should be applied to chat tickets
modern_ticket_reassignment| boolean| no| If true, turns on modern ticket reassignment for solved tickets
show_modern_ticket_reassignment| boolean| no| If true, shows UI components for modern ticket reassignment for solved tickets
default_solved_ticket_reassignment_strategy| string| no| Default solved ticket reassignment strategy

#### Agents

Name| Type| Read-only| Comment
---|---|---|---
agent_workspace| boolean| no| Toggles the Agent Workspace experience
aw_self_serve_migration_enabled| boolean| yes| Toggles the AW Self-serve migration control setting

#### Chat

Name| Type| Read-only| Comment
---|---|---|---
enabled| boolean| yes| Chat is enabled
maximum_requests| number| yes| The maximum number of chat requests an agent may handle at one time
welcome_message| string| yes| The message automatically sent to end-users when they begin chatting with agent

#### Messaging inactivity

Name| Type| Read-only| Comment
---|---|---|---
enabled| boolean| no| Auto-release capacity is enabled
timeout| number| no| Auto-release capacity timeout in minutes
ticket_status_id| number| no| Ticket status ID
end_session| boolean| no| Whether messaging session should end with the final reminder
reminders| array| no| Array of reminders
default_localized_messages| object| yes| Localized default reminder messages in the account language

#### Reminders

Name| Type| Read-only| Comment
---|---|---|---
message| string| no| Mandatory message for each reminder
timeout| number| no| Reminder timeout in seconds, available and mandatory for the 2nd and 3rd reminders, if configured
ticket_status_id| number| no| Ticket status id, available and mandatory for the 2nd and 3rd reminders, if configured. The field can be null to indicate no status change
tags| array| no| Array of strings, tags added to ticket with each reminder. Can be empty

#### X (formerly Twitter)

Name| Type| Read-only| Comment
---|---|---|---
shorten_url| string| yes| Possible values: 'always', 'optional', 'never'

#### G Suite

Name| Type| Read-only| Comment
---|---|---|---
has_google_apps| boolean| yes|
has_google_apps_admin| boolean| no| Account has at least one G Suite admin

#### Voice

Name| Type| Read-only| Comment
---|---|---|---
enabled| boolean| yes| Voice is enabled
maintenance| boolean| yes|
logging| boolean| yes|
outbound_enabled| boolean| yes|
agent_confirmation_when_forwarding| boolean| yes|
agent_wrap_up_after_calls| boolean| yes|
maximum_queue_size| number| yes|
maximum_queue_wait_time| number| yes|
only_during_business_hours| boolean| yes|
recordings_public| boolean| yes|
uk_mobile_forwarding| boolean| yes|

#### Users

Name| Type| Read-only| Comment
---|---|---|---
tagging| boolean| no| Users may be tagged
time_zone_selection| boolean| yes| Whether user can view time zone for profile
language_selection| boolean| yes| Whether to display language drop down for a user
agent_created_welcome_emails| boolean| no| Whether a user created by an agent receives a welcome email
end_user_phone_number_validation| boolean| no| Whether a user's phone number is validated
have_gravatars_enabled| boolean| no| Whether user gravatars are displayed in the UI

#### Brands

Name| Type| Read-only| Comment
---|---|---|---
default_brand_id| number| no| The id of the brand that is assigned to tickets by default
require_brand_on_new_tickets| boolean| no| Require agents to select a brand before saving tickets
end_user_across_brand_requests| boolean| no| When enabled, allows end users to access their own ticket requests in all of the help centers of a given account, regardless of the brand the ticket was originally created in

#### Statistics

Name| Type| Read-only| Comment
---|---|---|---
forum| boolean| yes| Allow users to view forum statistics
search| boolean| yes| Allow users to view search statistics

#### Billing

Name| Type| Read-only| Comment
---|---|---|---
backend| string| yes| Backend Billing system either 'internal' or 'zuora'

#### Active Features

Name| Type| Read-only| Comment
---|---|---|---
on_hold_status| boolean| yes| Account can use status hold
user_tagging| boolean| no| Enable user tags
ticket_tagging| boolean| no| Allow tagging tickets
topic_suggestion| boolean| yes| Allow topic suggestions in tickets
voice| boolean| yes| Voice support
facebook_login| boolean| yes|
google_login| boolean| yes|
twitter_login| boolean| yes|
forum_analytics| boolean| yes| Forum and search analytics
business_hours| boolean| no|
agent_forwarding| boolean| yes|
chat| boolean| yes|
chat_about_my_ticket| boolean| yes|
customer_satisfaction| boolean| no|
satisfaction_prediction| boolean| no|
csat_reason_code| boolean| yes|
markdown| boolean| yes| Markdown in ticket comments
bcc_archiving| boolean| yes| Account has a bcc_archive_address set
allow_ccs| boolean| yes| Allow CCs on tickets
explore| boolean| yes| Has account plan setting 'explore'
good_data_and_explore| boolean| yes| Has account plan setting 'good_data_and_explore'
explore_on_support_pro_plan| boolean| yes| Allowed to show explore role controls
sandbox| boolean| yes| Account has a sandbox
suspended_ticket_notification| boolean| yes|
twitter| boolean| yes| Account monitors at least one X (formerly Twitter) handle
facebook| boolean| yes| Account is actively linked to at least one Facebook page
feedback_tabs| boolean| yes| Feedback tab has been configured before
dynamic_contents| boolean| yes| Account has at least one dynamic content
light_agents| boolean| yes| Account has at least one light agent
is_abusive| boolean| yes| Account exceeded trial limits
rich_content_in_email| boolean| yes| Account supports incoming HTML email
fallback_composer| boolean| yes| Fallback composer for Asian languages
custom_objects_activated| boolean| no| Account has custom objects feature activated
organization_access_enabled| boolean| no| Displays the [Organizations page](https://support.zendesk.com/hc/en-us/articles/4408821417114)

#### API

Name| Type| Read-only| Comment
---|---|---|---
accepted_api_agreement| boolean| no| Account has accepted the API agreement
api_password_access_end_users| boolean| no| Allow end users to use the API with a username and password
api_token_access| boolean| no| Allow the account to use the API with API tokens

#### Ticket Form

Name| Type| Read-only| Comment
---|---|---|---
ticket_forms_instructions| string| no|

#### Lotus

Name| Type| Read-only| Comment
---|---|---|---
prefer_lotus| boolean| yes| Prefers the current version of Zendesk Support rather than Zendesk Classic

#### Rules

Name| Type| Read-only| Comment
---|---|---|---
macro_most_used| boolean| no| Display the most-used macros in the `Apply macro` list. Defaults to true
macro_order| string| no| Default macro display order. Possible values are 'alphabetical' or 'position'
skill_based_filtered_views| object| no| Array of view ids
enable_macro_suggestions| boolean| no| Display up to three of the suggested macros in the `Apply macro` list. Defaults to false

#### Limits

Name| Type| Read-only| Comment
---|---|---|---
attachment_size| number| yes| The maximum ticket attachment file size (in bytes)

#### Metrics

Name| Type| Read-only| Comment
---|---|---|---
account_size| string| yes| An account size category computed from the number of billable agents

#### Localization

Name| Type| Read-only| Comment
---|---|---|---
locale_ids| array| no| Array of locale IDs enabled for the account. See [Locales](/api-reference/ticketing/account-configuration/locales/) for possible values
time_zone| string| no| The time zone for the account
iana_time_zone| string| yes| The IANA (Internet Assigned Numbers Authority) time zone designation for the account
default_locale_identifier| string| no| The default locale for the account
uses_12_hour_clock| boolean| no| Toggles what time format is used for the account

#### Routing

Name| Type| Read-only| Comment
---|---|---|---
enabled| boolean| no| Toggles auto-routing functionality
autorouting_tag| string| no| Items tagged with this value will be auto-routed
max_email_capacity| number| no| Max number of email tickets that can be auto-assigned
max_messaging_capacity| number| no| Max number of messaging tickets that can be auto-assigned
reassignment_messaging_enabled| boolean| no| Whether the account is enabled with reassignment in messaging channel
reassignment_messaging_timeout| number| no| The amount of time before the chat is assigned to another agent
reassignment_talk_timeout| number| no| The amount of time before the call is assigned to another agent

#### Email

Name| Type| Read-only| Comment
---|---|---|---
accept_wildcard_emails| boolean| no| Allows users to create tickets sent to any variation of the support address's local-part (the text before the @ symbol). [Learn more](https://support.zendesk.com/hc/en-us/articles/5318946039578)
custom_dkim_domain| boolean| no| Uses your support address domain as the DKIM domain for outbound email deliveries. Two CNAME records must be configured for this to work
email_status| boolean| yes| Displays email status and delivery failures in the Zendesk Agent Workspace. [Learn more](https://support.zendesk.com/hc/en-us/articles/7917145637530)
email_sender_authentication| boolean| no| Authenticates inbound emails with SPF, DKIM, and DMARC alignment rules. When emails fail SPF and DKIM, they might be suspended or rejected by Zendesk
email_sender_authentication_profile| string| no| Controls the strictness of how inbound emails are validated and handled based on SPF, DKIM, and other authentication factors, with levels from flagging to suspending suspicious traffic. Defaults to `default`
email_template_photos| boolean| no| Shows user profile photos in emails. When enabled, the email notification will include the agent and end-user profile picture next to their comment text
email_template_selection| boolean| no| When enabled, admins can select email templates
gmail_actions| boolean| no| Enables Gmail Go-to Actions. It allows agents and end users to take quick actions directly from their Gmail inbox without opening the email
html_mail_template| string| no| The HTML template for outbound emails. Edit this template to customize the look & feel of the email notification
mail_delimiter| string| no| The text to be used as the mail delimiter. Defaults to `{{txt.email.delimiter}}`
modern_email_template| boolean| no| When enabled, the modern HTML template for outbound emails is used
no_mail_delimiter| boolean| no| When enabled, email recipients who reply to an email won't see the mail delimiter text separating the reply and the previous comments, resulting in an email that looks more personal and less machine-automated
personalized_replies| boolean| no| Enables personalized email replies by including agents' names (or aliases) in the outgoing email sender's address
rich_content_in_emails| boolean| no| Allows rich content in inbound emails, resulting in tickets and comments with HTML formatting and inline images. Disable it if you prefer to see plain text messages
send_gmail_messages_via_gmail| boolean| no| Sends emails via Gmail servers for authenticated addresses using the Gmail Connector API. Disable it if you see rate-limit warnings from either Gmail or Zendesk
text_mail_template| string| no| The plain-text template for outbound emails. Edit this template to customize the text and layout of the email notification

#### Device metadata

Name| Type| Read-only| Comment
---|---|---|---
enabled| boolean| no| If true, displays the device metadata
hide_ip| boolean| no| If true, hides the unique number assigned to the device currently being used. This may not reflect the end user's originating IP address
hide_location| boolean| no| If true, hides the city and country associated with the device IP address

#### Knowledge

Name| Type| Read-only| Comment
---|---|---|---
default_search_filters_brands| string| no| Specifies the default brand filters applied when searching knowledge base content
default_search_filters_categories| string| no| The default category filters applied during knowledge searches. An empty string means no category filters are set
default_search_filters_external_content_sources| string| no| Lists default external content sources to filter by in knowledge searches. An empty string means no external sources are filtered
default_search_filters_locales| string| no| Local or language filters applied
search_articles| boolean| no| If true, searching for help center articles is enabled
search_community_posts| boolean| no| If true, searching in community form posts is enabled
search_external_content| boolean| no| If true, searching external content sources outside the help center and community is enabled
require_article_templates| boolean| no| If true, mandates the use of predefined templates when creating new knowledge articles
generative_answers| boolean| no| If true, AI-powered generative answers are enabled to assist agents with suggested responses

#### Example


    {  "active_features": {    "agent_forwarding": false,    "allow_ccs": true,    "allow_email_template_customization": true,    "automatic_answers": false,    "bcc_archiving": false,    "benchmark_opt_out": false,    "business_hours": false,    "chat": false,    "chat_about_my_ticket": false,    "csat_reason_code": false,    "custom_dkim_domain": true,    "customer_context_as_default": false,    "customer_satisfaction": false,    "dynamic_contents": false,    "explore": true,    "explore_on_support_ent_plan": false,    "explore_on_support_pro_plan": false,    "facebook": false,    "facebook_login": false,    "fallback_composer": false,    "forum_analytics": true,    "good_data_and_explore": false,    "google_login": false,    "is_abusive": false,    "light_agents": false,    "markdown": false,    "on_hold_status": false,    "organization_access_enabled": true,    "rich_content_in_emails": true,    "sandbox": false,    "satisfaction_prediction": false,    "suspended_ticket_notification": false,    "ticket_forms": true,    "ticket_tagging": true,    "topic_suggestion": false,    "twitter": true,    "twitter_login": false,    "user_org_fields": true,    "user_tagging": true,    "voice": true  },  "agents": {    "agent_home": false,    "agent_workspace": false,    "aw_self_serve_migration_enabled": true,    "focus_mode": false,    "idle_timeout_enabled": false,    "unified_agent_statuses": false  },  "api": {    "accepted_api_agreement": true,    "api_password_access_end_users": true,    "api_token_access": "true"  },  "apps": {    "create_private": true,    "create_public": false,    "use": true  },  "billing": {    "backend": "zuora"  },  "branding": {    "favicon_url": null,    "header_color": "78A300",    "header_logo_url": null,    "page_background_color": "333333",    "tab_background_color": "7FA239",    "text_color": "FFFFFF"  },  "brands": {    "default_brand_id": 1873,    "end_user_across_brand_requests": false,    "require_brand_on_new_tickets": false  },  "cdn": {    "cdn_provider": "default",    "fallback_cdn_provider": "secondary",    "hosts": [      {        "name": "default",        "url": "https://static.zdassets.com"      },      {        "name": "secondary",        "url": "https://static-fallback.zdassets.com"      }    ]  },  "chat": {    "available": true,    "enabled": false,    "integrated": true,    "maximum_request_count": 1,    "welcome_message": "Hi there. How can I help today?"  },  "cross_sell": {    "show_chat_tooltip": true,    "xsell_source": null  },  "device_metadata": {    "enabled": true,    "hide_ip": true,    "hide_location": true  },  "email": {    "accept_wildcard_emails": false,    "custom_dkim_domain": false,    "email_sender_authentication": true,    "email_sender_authentication_profile": "enhanced",    "email_status": true,    "email_template_photos": true,    "email_template_selection": false,    "gmail_actions": true,    "html_mail_template": "<!DOCTYPE html>\r\n<html dir=\"auto\" {{lang}}>\r\n<head>\r\n  <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\r\n  <style type=\"text/css\">\r\n    table td {\r\n      border-collapse: collapse;\r\n    }\r\n    {{styles}}\r\n  </style>\r\n</head>\r\n<body {{attributes}} style=\"width: 100%!important; margin: 0; padding: 0;\">\r\n  <div style=\"font-family: 'system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','Arial','sans-serif'; font-size: 14px; line-height: 1.5; color:#444444;\">\r\n    <div style=\"color: #b5b5b5;\">{{delimiter}}</div>\r\n    {{content}}\r\n  </div><br/>\r\n  <div style=\"font-family: 'system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','Arial','sans-serif'; font-size: 12px; line-height: 1.5; color: #49545c; margin: 10px 0 14px 0; padding-top: 10px;\">\r\n    {{footer}} {{footer_link}}\r\n  </div><br/>\r\n  {{quoted_content}}\r\n</body>\r\n</html>\r\n",    "mail_delimiter": "{{txt.email.delimiter}}",    "modern_email_template": true,    "no_mail_delimiter": true,    "personalized_replies": true,    "rich_content_in_emails": true,    "send_gmail_messages_via_gmail": true,    "text_mail_template": "{{content}}\r\n\r\n{{footer}}\r\n\r\n{{quoted_content}}"  },  "google_apps": {    "has_google_apps": false,    "has_google_apps_admin": false  },  "groups": {    "check_group_name_uniqueness": true  },  "knowledge": {    "default_search_filters_brands": "_TICKET",    "default_search_filters_categories": "",    "default_search_filters_external_content_sources": "",    "default_search_filters_locales": "_TICKET",    "default_search_filters_sections": "",    "generative_answers": true,    "require_article_templates": false,    "search_articles": true,    "search_community_posts": true,    "search_external_content": true  },  "limits": {    "attachment_size": 52428800  },  "localization": {    "locale_ids": [      1042    ]  },  "lotus": {    "pod_id": 999,    "prefer_lotus": true,    "reporting": true  },  "messaging_inactivity": {    "default_localized_messages": {      "pre_solved_message_1": "Waiting on your response. If we don't hear from you within a few minutes, this ticket will be marked as solved.",      "pre_solved_message_2": "This ticket will be marked as solved soon. We hope to hear from you.",      "solved_message": "As we haven't heard from you in a while, we'll be marking this ticket as solved."    },    "enabled": true,    "reminders": [      {        "message": "Waiting on your response. If we don't hear from you within a few minutes, this ticket will be marked as solved."      },      {        "message": "This ticket will be marked as solved soon. We hope to hear from you.",        "ticket_status_id": null,        "timeout": 300      },      {        "message": "As we haven't heard from you in a while, we'll be marking this ticket as solved.",        "ticket_status_id": 8678123367037,        "timeout": 60      }    ],    "ticket_status_id": 8001424138749,    "timeout": 5  },  "metrics": {    "account_size": "100-399"  },  "onboarding": {    "checklist_onboarding_version": 2,    "onboarding_segments": null,    "product_sign_up": null  },  "routing": {    "autorouting_tag": "",    "enabled": false,    "max_email_capacity": 0,    "max_messaging_capacity": 0,    "reassignment_messaging_enabled": true,    "reassignment_messaging_timeout": 30,    "reassignment_talk_timeout": 30  },  "rule": {    "macro_most_used": true,    "macro_order": "alphabetical",    "skill_based_filtered_views": [],    "using_skill_based_routing": false  },  "side_conversations": {    "email_channel": false,    "msteams_channel": false,    "show_in_context_panel": false,    "slack_channel": false,    "tickets_channel": false  },  "statistics": {    "forum": true,    "rule_usage": true,    "search": true  },  "ticket_form": {    "raw_ticket_forms_instructions": "Please choose your issue below",    "ticket_forms_instructions": "Please choose your issue below"  },  "tickets": {    "accepted_new_collaboration_tos": false,    "agent_collision": true,    "agent_invitation_enabled": true,    "agent_ticket_deletion": false,    "allow_group_reset": true,    "assign_default_organization": true,    "assign_tickets_upon_solve": true,    "auto_translation_enabled": false,    "auto_updated_ccs_followers_rules": false,    "chat_sla_enablement": false,    "collaboration": true,    "comments_public_by_default": true,    "default_solved_ticket_reassignment_strategy": "legacy",    "default_to_draft_mode": false,    "email_attachments": false,    "emoji_autocompletion": true,    "follower_and_email_cc_collaborations": false,    "has_color_text": true,    "is_first_comment_private_enabled": true,    "light_agent_email_ccs_allowed": false,    "list_empty_views": true,    "list_newest_comments_first": true,    "markdown_ticket_comments": false,    "maximum_personal_views_to_list": 8,    "modern_ticket_reassignment": false,    "private_attachments": false,    "rich_text_comments": true,    "show_modern_ticket_reassignment": false,    "status_hold": false,    "tagging": true,    "using_skill_based_routing": false  },  "twitter": {    "shorten_url": "optional"  },  "user": {    "agent_created_welcome_emails": true,    "end_user_phone_number_validation": false,    "have_gravatars_enabled": true,    "language_selection": true,    "multiple_organizations": false,    "tagging": true,    "time_zone_selection": true  },  "voice": {    "agent_confirmation_when_forwarding": true,    "agent_wrap_up_after_calls": true,    "enabled": true,    "logging": true,    "maximum_queue_size": 5,    "maximum_queue_wait_time": 1,    "only_during_business_hours": false,    "outbound_enabled": true,    "recordings_public": true,    "uk_mobile_forwarding": true  }}

### Show Settings

  * `GET /api/v2/account/settings`


Shows the settings that are available for the account.

#### Allowed For

  * Agents


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/account/settings \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/account/settings"	method := "GET"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/account/settings")		.newBuilder();String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("GET", null)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'GET',  url: 'https://example.zendesk.com/api/v2/account/settings',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/account/settings"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"GET",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/account/settings")request = Net::HTTP::Get.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "settings": {    "active_features": {      "agent_forwarding": false,      "allow_ccs": true,      "allow_email_template_customization": true,      "automatic_answers": false,      "bcc_archiving": false,      "benchmark_opt_out": false,      "business_hours": false,      "chat": false,      "chat_about_my_ticket": false,      "csat_reason_code": false,      "custom_dkim_domain": true,      "customer_context_as_default": false,      "customer_satisfaction": false,      "dynamic_contents": false,      "explore": true,      "explore_on_support_ent_plan": false,      "explore_on_support_pro_plan": false,      "facebook": false,      "facebook_login": false,      "fallback_composer": false,      "forum_analytics": true,      "good_data_and_explore": false,      "google_login": false,      "is_abusive": false,      "light_agents": false,      "markdown": false,      "on_hold_status": false,      "organization_access_enabled": true,      "rich_content_in_emails": true,      "sandbox": false,      "satisfaction_prediction": false,      "suspended_ticket_notification": false,      "ticket_forms": true,      "ticket_tagging": true,      "topic_suggestion": false,      "twitter": true,      "twitter_login": false,      "user_org_fields": true,      "user_tagging": true,      "voice": true    },    "agents": {      "agent_home": false,      "agent_workspace": false,      "aw_self_serve_migration_enabled": true,      "focus_mode": false,      "idle_timeout_enabled": false,      "unified_agent_statuses": false    },    "api": {      "accepted_api_agreement": true,      "api_password_access_end_users": true,      "api_token_access": "true"    },    "apps": {      "create_private": true,      "create_public": false,      "use": true    },    "billing": {      "backend": "zuora"    },    "branding": {      "favicon_url": null,      "header_color": "78A300",      "header_logo_url": null,      "page_background_color": "333333",      "tab_background_color": "7FA239",      "text_color": "FFFFFF"    },    "brands": {      "default_brand_id": 1873,      "end_user_across_brand_requests": false,      "require_brand_on_new_tickets": false    },    "cdn": {      "cdn_provider": "default",      "fallback_cdn_provider": "secondary",      "hosts": [        {          "name": "default",          "url": "https://static.zdassets.com"        },        {          "name": "secondary",          "url": "https://static-fallback.zdassets.com"        }      ]    },    "chat": {      "available": true,      "enabled": false,      "integrated": true,      "maximum_request_count": 1,      "welcome_message": "Hi there. How can I help today?"    },    "cross_sell": {      "show_chat_tooltip": true,      "xsell_source": null    },    "email": {      "accept_wildcard_emails": false,      "custom_dkim_domain": false,      "email_sender_authentication": true,      "email_sender_authentication_profile": "enhanced",      "email_status": true,      "email_template_photos": true,      "email_template_selection": false,      "gmail_actions": true,      "html_mail_template": "<!DOCTYPE html>\r\n<html dir=\"auto\" {{lang}}>\r\n<head>\r\n  <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\r\n  <style type=\"text/css\">\r\n    table td {\r\n      border-collapse: collapse;\r\n    }\r\n    {{styles}}\r\n  </style>\r\n</head>\r\n<body {{attributes}} style=\"width: 100%!important; margin: 0; padding: 0;\">\r\n  <div style=\"font-family: 'system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','Arial','sans-serif'; font-size: 14px; line-height: 1.5; color:#444444;\">\r\n    <div style=\"color: #b5b5b5;\">{{delimiter}}</div>\r\n    {{content}}\r\n  </div><br/>\r\n  <div style=\"font-family: 'system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','Arial','sans-serif'; font-size: 12px; line-height: 1.5; color: #49545c; margin: 10px 0 14px 0; padding-top: 10px;\">\r\n    {{footer}} {{footer_link}}\r\n  </div><br/>\r\n  {{quoted_content}}\r\n</body>\r\n</html>\r\n",      "mail_delimiter": "{{txt.email.delimiter}}",      "modern_email_template": true,      "multi_recipient_email_tickets": true,      "no_mail_delimiter": true,      "personalized_replies": true,      "rich_content_in_emails": true,      "send_gmail_messages_via_gmail": true,      "text_mail_template": "{{content}}\r\n\r\n{{footer}}\r\n\r\n{{quoted_content}}"    },    "google_apps": {      "has_google_apps": false,      "has_google_apps_admin": false    },    "groups": {      "check_group_name_uniqueness": true    },    "limits": {      "attachment_size": 52428800    },    "localization": {      "locale_ids": [        1042      ]    },    "lotus": {      "pod_id": 999,      "prefer_lotus": true,      "reporting": true    },    "messaging_inactivity": {      "default_localized_messages": {        "pre_solved_message_1": "Waiting on your response. If we don't hear from you within a few minutes, this ticket will be marked as solved.",        "pre_solved_message_2": "This ticket will be marked as solved soon. We hope to hear from you.",        "solved_message": "As we haven't heard from you in a while, we'll be marking this ticket as solved."      },      "enabled": true,      "reminders": [        {          "message": "Waiting on your response. If we don't hear from you within a few minutes, this ticket will be marked as solved."        },        {          "message": "This ticket will be marked as solved soon. We hope to hear from you.",          "ticket_status_id": null,          "timeout": 300        },        {          "message": "As we haven't heard from you in a while, we'll be marking this ticket as solved.",          "ticket_status_id": 8678123367037,          "timeout": 60        }      ],      "ticket_status_id": 8001424138749,      "timeout": 5    },    "metrics": {      "account_size": "100-399"    },    "onboarding": {      "checklist_onboarding_version": 2,      "onboarding_segments": null,      "product_sign_up": null    },    "routing": {      "autorouting_tag": "",      "enabled": false,      "max_email_capacity": 0,      "max_messaging_capacity": 0    },    "rule": {      "macro_most_used": true,      "macro_order": "alphabetical",      "skill_based_filtered_views": [],      "using_skill_based_routing": false    },    "side_conversations": {      "email_channel": false,      "msteams_channel": false,      "show_in_context_panel": false,      "slack_channel": false,      "tickets_channel": false    },    "statistics": {      "forum": true,      "rule_usage": true,      "search": true    },    "ticket_form": {      "raw_ticket_forms_instructions": "Please choose your issue below",      "ticket_forms_instructions": "Please choose your issue below"    },    "tickets": {      "accepted_new_collaboration_tos": false,      "agent_collision": true,      "agent_invitation_enabled": true,      "agent_ticket_deletion": false,      "allow_group_reset": true,      "assign_default_organization": true,      "assign_tickets_upon_solve": true,      "auto_translation_enabled": false,      "auto_updated_ccs_followers_rules": false,      "chat_sla_enablement": false,      "collaboration": true,      "comments_public_by_default": true,      "default_solved_ticket_reassignment_strategy": "legacy",      "default_to_draft_mode": false,      "email_attachments": false,      "emoji_autocompletion": true,      "follower_and_email_cc_collaborations": false,      "has_color_text": true,      "is_first_comment_private_enabled": true,      "light_agent_email_ccs_allowed": false,      "list_empty_views": true,      "list_newest_comments_first": true,      "markdown_ticket_comments": false,      "maximum_personal_views_to_list": 8,      "modern_ticket_reassignment": false,      "private_attachments": false,      "rich_text_comments": true,      "show_modern_ticket_reassignment": false,      "status_hold": false,      "tagging": true,      "using_skill_based_routing": false    },    "twitter": {      "shorten_url": "optional"    },    "user": {      "agent_created_welcome_emails": true,      "end_user_phone_number_validation": false,      "have_gravatars_enabled": true,      "language_selection": true,      "multiple_organizations": false,      "tagging": true,      "time_zone_selection": true    },    "voice": {      "agent_confirmation_when_forwarding": true,      "agent_wrap_up_after_calls": true,      "enabled": true,      "logging": true,      "maximum_queue_size": 5,      "maximum_queue_wait_time": 1,      "only_during_business_hours": false,      "outbound_enabled": true,      "recordings_public": true,      "uk_mobile_forwarding": true    }  }}

### Update Account Settings

  * `PUT /api/v2/account/settings`


Updates settings for the account. See JSON Format above for the settings you can update.

#### Allowed For

  * Admins


#### Code Samples

**curl**


    curl https://{subdomain}.zendesk.com/api/v2/account/settings \  -H "Content-Type: application/json" -X PUT \  -d '{ "settings": { "active_features": { "customer_satisfaction": false }}}' \  -v -u {email_address}/token:{api_token}

**Go**


    import (	"fmt"	"io"	"net/http")
    func main() {	url := "https://example.zendesk.com/api/v2/account/settings"	method := "PUT"	req, err := http.NewRequest(method, url, nil)
    	if err != nil {		fmt.Println(err)		return	}	req.Header.Add("Content-Type", "application/json")	req.Header.Add("Authorization", "Basic <auth-value>") // Base64 encoded "{email_address}/token:{api_token}"
    	client := &http.Client {}	res, err := client.Do(req)	if err != nil {		fmt.Println(err)		return	}	defer res.Body.Close()
    	body, err := io.ReadAll(res.Body)	if err != nil {		fmt.Println(err)		return	}	fmt.Println(string(body))}

**Java**


    import com.squareup.okhttp.*;OkHttpClient client = new OkHttpClient();HttpUrl.Builder urlBuilder = HttpUrl.parse("https://example.zendesk.com/api/v2/account/settings")		.newBuilder();RequestBody body = RequestBody.create(MediaType.parse("application/json"),		"""""");String userCredentials = "your_email_address" + "/token:" + "your_api_token";String basicAuth = "Basic " + java.util.Base64.getEncoder().encodeToString(userCredentials.getBytes());
    Request request = new Request.Builder()		.url(urlBuilder.build())		.method("PUT", body)		.addHeader("Content-Type", "application/json")		.addHeader("Authorization", basicAuth)		.build();Response response = client.newCall(request).execute();

**Nodejs**


    var axios = require('axios');
    var config = {  method: 'PUT',  url: 'https://example.zendesk.com/api/v2/account/settings',  headers: {	'Content-Type': 'application/json',	'Authorization': 'Basic <auth-value>', // Base64 encoded "{email_address}/token:{api_token}"  },};
    axios(config).then(function (response) {  console.log(JSON.stringify(response.data));}).catch(function (error) {  console.log(error);});

**Python**


    import requestsfrom requests.auth import HTTPBasicAuth
    url = "https://example.zendesk.com/api/v2/account/settings"headers = {	"Content-Type": "application/json",}email_address = 'your_email_address'api_token = 'your_api_token'# Use basic authenticationauth = HTTPBasicAuth(f'{email_address}/token', api_token)
    response = requests.request(	"PUT",	url,	auth=auth,	headers=headers)
    print(response.text)

**Ruby**


    require "net/http"require "base64"uri = URI("https://example.zendesk.com/api/v2/account/settings")request = Net::HTTP::Put.new(uri, "Content-Type": "application/json")email = "your_email_address"api_token = "your_api_token"credentials = "#{email}/token:#{api_token}"encoded_credentials = Base64.strict_encode64(credentials)request["Authorization"] = "Basic #{encoded_credentials}"response = Net::HTTP.start uri.hostname, uri.port, use_ssl: true do |http|	http.request(request)end

#### Example response(s)

**200 OK**


    // Status 200 OK
    {  "settings": {    "active_features": {      "agent_forwarding": false,      "allow_ccs": true,      "allow_email_template_customization": true,      "automatic_answers": false,      "bcc_archiving": false,      "benchmark_opt_out": false,      "business_hours": false,      "chat": false,      "chat_about_my_ticket": false,      "csat_reason_code": false,      "custom_dkim_domain": true,      "customer_context_as_default": false,      "customer_satisfaction": false,      "dynamic_contents": false,      "explore": true,      "explore_on_support_ent_plan": false,      "explore_on_support_pro_plan": false,      "facebook": false,      "facebook_login": false,      "fallback_composer": false,      "forum_analytics": true,      "good_data_and_explore": false,      "google_login": false,      "is_abusive": false,      "light_agents": false,      "markdown": false,      "on_hold_status": false,      "organization_access_enabled": true,      "rich_content_in_emails": true,      "sandbox": false,      "satisfaction_prediction": false,      "suspended_ticket_notification": false,      "ticket_forms": true,      "ticket_tagging": true,      "topic_suggestion": false,      "twitter": true,      "twitter_login": false,      "user_org_fields": true,      "user_tagging": true,      "voice": true    },    "agents": {      "agent_home": false,      "agent_workspace": false,      "aw_self_serve_migration_enabled": true,      "focus_mode": false,      "idle_timeout_enabled": false,      "unified_agent_statuses": false    },    "api": {      "accepted_api_agreement": true,      "api_password_access_end_users": true,      "api_token_access": "true"    },    "apps": {      "create_private": true,      "create_public": false,      "use": true    },    "billing": {      "backend": "zuora"    },    "branding": {      "favicon_url": null,      "header_color": "78A300",      "header_logo_url": null,      "page_background_color": "333333",      "tab_background_color": "7FA239",      "text_color": "FFFFFF"    },    "brands": {      "default_brand_id": 1873,      "end_user_across_brand_requests": false,      "require_brand_on_new_tickets": false    },    "cdn": {      "cdn_provider": "default",      "fallback_cdn_provider": "secondary",      "hosts": [        {          "name": "default",          "url": "https://static.zdassets.com"        },        {          "name": "secondary",          "url": "https://static-fallback.zdassets.com"        }      ]    },    "chat": {      "available": true,      "enabled": false,      "integrated": true,      "maximum_request_count": 1,      "welcome_message": "Hi there. How can I help today?"    },    "cross_sell": {      "show_chat_tooltip": true,      "xsell_source": null    },    "email": {      "accept_wildcard_emails": false,      "custom_dkim_domain": false,      "email_sender_authentication": true,      "email_sender_authentication_profile": "enhanced",      "email_status": true,      "email_template_photos": true,      "email_template_selection": false,      "gmail_actions": true,      "html_mail_template": "<!DOCTYPE html>\r\n<html dir=\"auto\" {{lang}}>\r\n<head>\r\n  <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\r\n  <style type=\"text/css\">\r\n    table td {\r\n      border-collapse: collapse;\r\n    }\r\n    {{styles}}\r\n  </style>\r\n</head>\r\n<body {{attributes}} style=\"width: 100%!important; margin: 0; padding: 0;\">\r\n  <div style=\"font-family: 'system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','Arial','sans-serif'; font-size: 14px; line-height: 1.5; color:#444444;\">\r\n    <div style=\"color: #b5b5b5;\">{{delimiter}}</div>\r\n    {{content}}\r\n  </div><br/>\r\n  <div style=\"font-family: 'system-ui','-apple-system','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','Arial','sans-serif'; font-size: 12px; line-height: 1.5; color: #49545c; margin: 10px 0 14px 0; padding-top: 10px;\">\r\n    {{footer}} {{footer_link}}\r\n  </div><br/>\r\n  {{quoted_content}}\r\n</body>\r\n</html>\r\n",      "mail_delimiter": "{{txt.email.delimiter}}",      "modern_email_template": true,      "multi_recipient_email_tickets": true,      "no_mail_delimiter": true,      "personalized_replies": true,      "rich_content_in_emails": true,      "send_gmail_messages_via_gmail": true,      "text_mail_template": "{{content}}\r\n\r\n{{footer}}\r\n\r\n{{quoted_content}}"    },    "google_apps": {      "has_google_apps": false,      "has_google_apps_admin": false    },    "groups": {      "check_group_name_uniqueness": true    },    "limits": {      "attachment_size": 52428800    },    "localization": {      "locale_ids": [        1042      ]    },    "lotus": {      "pod_id": 999,      "prefer_lotus": true,      "reporting": true    },    "messaging_inactivity": {      "default_localized_messages": {        "pre_solved_message_1": "Waiting on your response. If we don't hear from you within a few minutes, this ticket will be marked as solved.",        "pre_solved_message_2": "This ticket will be marked as solved soon. We hope to hear from you.",        "solved_message": "As we haven't heard from you in a while, we'll be marking this ticket as solved."      },      "enabled": true,      "reminders": [        {          "message": "Waiting on your response. If we don't hear from you within a few minutes, this ticket will be marked as solved."        },        {          "message": "This ticket will be marked as solved soon. We hope to hear from you.",          "ticket_status_id": null,          "timeout": 300        },        {          "message": "As we haven't heard from you in a while, we'll be marking this ticket as solved.",          "ticket_status_id": 8678123367037,          "timeout": 60        }      ],      "ticket_status_id": 8001424138749,      "timeout": 5    },    "metrics": {      "account_size": "100-399"    },    "onboarding": {      "checklist_onboarding_version": 2,      "onboarding_segments": null,      "product_sign_up": null    },    "routing": {      "autorouting_tag": "",      "enabled": false,      "max_email_capacity": 0,      "max_messaging_capacity": 0    },    "rule": {      "macro_most_used": true,      "macro_order": "alphabetical",      "skill_based_filtered_views": [],      "using_skill_based_routing": false    },    "side_conversations": {      "email_channel": false,      "msteams_channel": false,      "show_in_context_panel": false,      "slack_channel": false,      "tickets_channel": false    },    "statistics": {      "forum": true,      "rule_usage": true,      "search": true    },    "ticket_form": {      "raw_ticket_forms_instructions": "Please choose your issue below",      "ticket_forms_instructions": "Please choose your issue below"    },    "tickets": {      "accepted_new_collaboration_tos": false,      "agent_collision": true,      "agent_invitation_enabled": true,      "agent_ticket_deletion": false,      "allow_group_reset": true,      "assign_default_organization": true,      "assign_tickets_upon_solve": true,      "auto_translation_enabled": false,      "auto_updated_ccs_followers_rules": false,      "chat_sla_enablement": false,      "collaboration": true,      "comments_public_by_default": true,      "default_solved_ticket_reassignment_strategy": "legacy",      "default_to_draft_mode": false,      "email_attachments": false,      "emoji_autocompletion": true,      "follower_and_email_cc_collaborations": false,      "has_color_text": true,      "is_first_comment_private_enabled": true,      "light_agent_email_ccs_allowed": false,      "list_empty_views": true,      "list_newest_comments_first": true,      "markdown_ticket_comments": false,      "maximum_personal_views_to_list": 8,      "modern_ticket_reassignment": false,      "private_attachments": false,      "rich_text_comments": true,      "show_modern_ticket_reassignment": false,      "status_hold": false,      "tagging": true,      "using_skill_based_routing": false    },    "twitter": {      "shorten_url": "optional"    },    "user": {      "agent_created_welcome_emails": true,      "end_user_phone_number_validation": false,      "have_gravatars_enabled": true,      "language_selection": true,      "multiple_organizations": false,      "tagging": true,      "time_zone_selection": true    },    "voice": {      "agent_confirmation_when_forwarding": true,      "agent_wrap_up_after_calls": true,      "enabled": true,      "logging": true,      "maximum_queue_size": 5,      "maximum_queue_wait_time": 1,      "only_during_business_hours": false,      "outbound_enabled": true,      "recordings_public": true,      "uk_mobile_forwarding": true    }  }}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)