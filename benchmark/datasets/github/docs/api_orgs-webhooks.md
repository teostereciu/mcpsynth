# REST API endpoints for organization webhooks

*Source: https://docs.github.com/en/rest/orgs/webhooks*

---

# REST API endpoints for organization webhooks
Use the REST API to interact with webhooks in an organization.

## About organization webhooks
Organization webhooks allow your server to receive HTTPPOSTpayloads whenever certain events happen in an organization. For more information, seeWebhooks documentation.

## List organization webhooks
List webhooks for an organization.
The authenticated user must be an organization owner to use this endpoint.
OAuth app tokens and personal access tokens (classic) needadmin:org_hookscope. OAuth apps cannot list, view, or edit
webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Fine-grained access tokens for "List organization webhooks"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" organization permissions (read)

### Parameters for "List organization webhooks"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List organization webhooks"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "List organization webhooks"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/hooks
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
[
  {
    "id": 1,
    "url": "https://api.github.com/orgs/octocat/hooks/1",
    "ping_url": "https://api.github.com/orgs/octocat/hooks/1/pings",
    "deliveries_url": "https://api.github.com/orgs/octocat/hooks/1/deliveries",
    "name": "web",
    "events": [
      "push",
      "pull_request"
    ],
    "active": true,
    "config": {
      "url": "http://example.com",
      "content_type": "json"
    },
    "updated_at": "2011-09-06T20:39:23Z",
    "created_at": "2011-09-06T17:26:27Z",
    "type": "Organization"
  }
]
```

## Create an organization webhook
Create a hook that posts payloads in JSON format.
You must be an organization owner to use this endpoint.
OAuth app tokens and personal access tokens (classic) needadmin:org_hookscope. OAuth apps cannot list, view, or
edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Fine-grained access tokens for "Create an organization webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" organization permissions (write)

### Parameters for "Create an organization webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
namestringRequiredMust be passed as "web".
configobjectRequiredKey/value pairs to provide settings for this webhook.
Properties ofconfigName, Type, DescriptionurlstringRequiredThe URL to which the payloads will be delivered.content_typestringThe media type used to serialize the payloads. Supported values includejsonandform. The default isform.secretstringIf provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers.insecure_sslstring or numberDetermines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks.usernamestringpasswordstring | Name, Type, Description | urlstringRequiredThe URL to which the payloads will be delivered. | content_typestringThe media type used to serialize the payloads. Supported values includejsonandform. The default isform. | secretstringIf provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers. | insecure_sslstring or numberDetermines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks. | usernamestring | passwordstring
Name, Type, Description
urlstringRequiredThe URL to which the payloads will be delivered.
content_typestringThe media type used to serialize the payloads. Supported values includejsonandform. The default isform.
secretstringIf provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers.
insecure_sslstring or numberDetermines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks.
usernamestring
passwordstring
eventsarray of stringsDetermines whateventsthe hook is triggered for. Set to["*"]to receive all possible events.Default:["push"]
activebooleanDetermines if notifications are sent when the webhook is triggered. Set totrueto send notifications.Default:true
[/TABLE]
Must be passed as "web".
Key/value pairs to provide settings for this webhook.

[TABLE]
Name, Type, Description
urlstringRequiredThe URL to which the payloads will be delivered.
content_typestringThe media type used to serialize the payloads. Supported values includejsonandform. The default isform.
secretstringIf provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers.
insecure_sslstring or numberDetermines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks.
usernamestring
passwordstring
[/TABLE]
The URL to which the payloads will be delivered.

```
content_type
```
The media type used to serialize the payloads. Supported values includejsonandform. The default isform.
If provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers.

```
insecure_ssl
```
Determines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks.
Determines whateventsthe hook is triggered for. Set to["*"]to receive all possible events.
Default:["push"]
Determines if notifications are sent when the webhook is triggered. Set totrueto send notifications.
Default:true

### HTTP response status codes for "Create an organization webhook"

[TABLE]
Status code | Description
201 | Created
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Create an organization webhook"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/hooks \
  -d '{"name":"web","active":true,"events":["push","pull_request"],"config":{"url":"http://example.com/webhook","content_type":"json"}}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "id": 1,
  "url": "https://api.github.com/orgs/octocat/hooks/1",
  "ping_url": "https://api.github.com/orgs/octocat/hooks/1/pings",
  "deliveries_url": "https://api.github.com/orgs/octocat/hooks/1/deliveries",
  "name": "web",
  "events": [
    "push",
    "pull_request"
  ],
  "active": true,
  "config": {
    "url": "http://example.com",
    "content_type": "json"
  },
  "updated_at": "2011-09-06T20:39:23Z",
  "created_at": "2011-09-06T17:26:27Z",
  "type": "Organization"
}
```

## Get an organization webhook
Returns a webhook configured in an organization. To get only the webhookconfigproperties, see "Get a webhook configuration for an organization.
You must be an organization owner to use this endpoint.
OAuth app tokens and personal access tokens (classic) needadmin:org_hookscope. OAuth apps cannot list, view, or edit
webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Fine-grained access tokens for "Get an organization webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" organization permissions (read)

### Parameters for "Get an organization webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
[/TABLE]
The organization name. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

### HTTP response status codes for "Get an organization webhook"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get an organization webhook"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/hooks/HOOK_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 1,
  "url": "https://api.github.com/orgs/octocat/hooks/1",
  "ping_url": "https://api.github.com/orgs/octocat/hooks/1/pings",
  "deliveries_url": "https://api.github.com/orgs/octocat/hooks/1/deliveries",
  "name": "web",
  "events": [
    "push",
    "pull_request"
  ],
  "active": true,
  "config": {
    "url": "http://example.com",
    "content_type": "json"
  },
  "updated_at": "2011-09-06T20:39:23Z",
  "created_at": "2011-09-06T17:26:27Z",
  "type": "Organization"
}
```

## Update an organization webhook
Updates a webhook configured in an organization. When you update a webhook,
thesecretwill be overwritten. If you previously had asecretset, you must
provide the samesecretor set a newsecretor the secret will be removed. If
you are only updating individual webhookconfigproperties, use "Update a webhook
configuration for an organization".
You must be an organization owner to use this endpoint.
OAuth app tokens and personal access tokens (classic) needadmin:org_hookscope. OAuth apps cannot list, view, or edit
webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Fine-grained access tokens for "Update an organization webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" organization permissions (write)

### Parameters for "Update an organization webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
[/TABLE]
The organization name. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

[TABLE]
Name, Type, Description
configobjectKey/value pairs to provide settings for this webhook.
Properties ofconfigName, Type, DescriptionurlstringRequiredThe URL to which the payloads will be delivered.content_typestringThe media type used to serialize the payloads. Supported values includejsonandform. The default isform.secretstringIf provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers.insecure_sslstring or numberDetermines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks. | Name, Type, Description | urlstringRequiredThe URL to which the payloads will be delivered. | content_typestringThe media type used to serialize the payloads. Supported values includejsonandform. The default isform. | secretstringIf provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers. | insecure_sslstring or numberDetermines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks.
Name, Type, Description
urlstringRequiredThe URL to which the payloads will be delivered.
content_typestringThe media type used to serialize the payloads. Supported values includejsonandform. The default isform.
secretstringIf provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers.
insecure_sslstring or numberDetermines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks.
eventsarray of stringsDetermines whateventsthe hook is triggered for.Default:["push"]
activebooleanDetermines if notifications are sent when the webhook is triggered. Set totrueto send notifications.Default:true
namestring
[/TABLE]
Key/value pairs to provide settings for this webhook.

[TABLE]
Name, Type, Description
urlstringRequiredThe URL to which the payloads will be delivered.
content_typestringThe media type used to serialize the payloads. Supported values includejsonandform. The default isform.
secretstringIf provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers.
insecure_sslstring or numberDetermines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks.
[/TABLE]
The URL to which the payloads will be delivered.

```
content_type
```
The media type used to serialize the payloads. Supported values includejsonandform. The default isform.
If provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers.

```
insecure_ssl
```
Determines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks.
Determines whateventsthe hook is triggered for.
Default:["push"]
Determines if notifications are sent when the webhook is triggered. Set totrueto send notifications.
Default:true

### HTTP response status codes for "Update an organization webhook"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Update an organization webhook"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PATCH \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/hooks/HOOK_ID \
  -d '{"active":true,"events":["pull_request"]}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 1,
  "url": "https://api.github.com/orgs/octocat/hooks/1",
  "ping_url": "https://api.github.com/orgs/octocat/hooks/1/pings",
  "deliveries_url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678/deliveries",
  "name": "web",
  "events": [
    "pull_request"
  ],
  "active": true,
  "config": {
    "url": "http://example.com",
    "content_type": "json"
  },
  "updated_at": "2011-09-06T20:39:23Z",
  "created_at": "2011-09-06T17:26:27Z",
  "type": "Organization"
}
```

## Delete an organization webhook
Delete a webhook for an organization.
The authenticated user must be an organization owner to use this endpoint.
OAuth app tokens and personal access tokens (classic) needadmin:org_hookscope. OAuth apps cannot list, view, or edit
webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Fine-grained access tokens for "Delete an organization webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" organization permissions (write)

### Parameters for "Delete an organization webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
[/TABLE]
The organization name. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

### HTTP response status codes for "Delete an organization webhook"

[TABLE]
Status code | Description
204 | No Content
404 | Resource not found
[/TABLE]
No Content
Resource not found

### Code samples for "Delete an organization webhook"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X DELETE \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/hooks/HOOK_ID
```

#### Response

```
Status: 204
```

## Get a webhook configuration for an organization
Returns the webhook configuration for an organization. To get more information about the webhook, including theactivestate andevents, use "Get an organization webhook."
You must be an organization owner to use this endpoint.
OAuth app tokens and personal access tokens (classic) needadmin:org_hookscope. OAuth apps cannot list, view, or edit
webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Fine-grained access tokens for "Get a webhook configuration for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" organization permissions (read)

### Parameters for "Get a webhook configuration for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
[/TABLE]
The organization name. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

### HTTP response status codes for "Get a webhook configuration for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a webhook configuration for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/hooks/HOOK_ID/config
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "content_type": "json",
  "insecure_ssl": "0",
  "secret": "********",
  "url": "https://example.com/webhook"
}
```

## Update a webhook configuration for an organization
Updates the webhook configuration for an organization. To update more information about the webhook, including theactivestate andevents, use "Update an organization webhook."
You must be an organization owner to use this endpoint.
OAuth app tokens and personal access tokens (classic) needadmin:org_hookscope. OAuth apps cannot list, view, or edit
webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Fine-grained access tokens for "Update a webhook configuration for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" organization permissions (write)

### Parameters for "Update a webhook configuration for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
[/TABLE]
The organization name. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

[TABLE]
Name, Type, Description
urlstringThe URL to which the payloads will be delivered.
content_typestringThe media type used to serialize the payloads. Supported values includejsonandform. The default isform.
secretstringIf provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers.
insecure_sslstring or numberDetermines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks.
[/TABLE]
The URL to which the payloads will be delivered.

```
content_type
```
The media type used to serialize the payloads. Supported values includejsonandform. The default isform.
If provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers.

```
insecure_ssl
```
Determines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks.

### HTTP response status codes for "Update a webhook configuration for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Update a webhook configuration for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PATCH \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/hooks/HOOK_ID/config \
  -d '{"url":"http://example.com/webhook","content_type":"json","insecure_ssl":"0","secret":"********"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "content_type": "json",
  "insecure_ssl": "0",
  "secret": "********",
  "url": "https://example.com/webhook"
}
```

## List deliveries for an organization webhook
Returns a list of webhook deliveries for a webhook configured in an organization.
You must be an organization owner to use this endpoint.
OAuth app tokens and personal access tokens (classic) needadmin:org_hookscope. OAuth apps cannot list, view, or edit
webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Fine-grained access tokens for "List deliveries for an organization webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" organization permissions (read)

### Parameters for "List deliveries for an organization webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
[/TABLE]
The organization name. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
cursorstringUsed for pagination: the starting delivery from which the page of deliveries is fetched. Refer to thelinkheader for the next and previous page cursors.
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
Used for pagination: the starting delivery from which the page of deliveries is fetched. Refer to thelinkheader for the next and previous page cursors.

### HTTP response status codes for "List deliveries for an organization webhook"

[TABLE]
Status code | Description
200 | OK
400 | Bad Request
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Bad Request
Validation failed, or the endpoint has been spammed.

### Code samples for "List deliveries for an organization webhook"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/hooks/HOOK_ID/deliveries
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
[
  {
    "id": 12345678,
    "guid": "0b989ba4-242f-11e5-81e1-c7b6966d2516",
    "delivered_at": "2019-06-03T00:57:16Z",
    "redelivery": false,
    "duration": 0.27,
    "status": "OK",
    "status_code": 200,
    "event": "issues",
    "action": "opened",
    "installation_id": 123,
    "repository_id": 456,
    "throttled_at": "2019-06-03T00:57:16Z"
  },
  {
    "id": 123456789,
    "guid": "0b989ba4-242f-11e5-81e1-c7b6966d2516",
    "delivered_at": "2019-06-04T00:57:16Z",
    "redelivery": true,
    "duration": 0.28,
    "status": "OK",
    "status_code": 200,
    "event": "issues",
    "action": "opened",
    "installation_id": 123,
    "repository_id": 456,
    "throttled_at": null
  }
]
```

## Get a webhook delivery for an organization webhook
Returns a delivery for a webhook configured in an organization.
You must be an organization owner to use this endpoint.
OAuth app tokens and personal access tokens (classic) needadmin:org_hookscope. OAuth apps cannot list, view, or edit
webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Fine-grained access tokens for "Get a webhook delivery for an organization webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" organization permissions (read)

### Parameters for "Get a webhook delivery for an organization webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
delivery_idintegerRequired
[/TABLE]
The organization name. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

```
delivery_id
```

### HTTP response status codes for "Get a webhook delivery for an organization webhook"

[TABLE]
Status code | Description
200 | OK
400 | Bad Request
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Bad Request
Validation failed, or the endpoint has been spammed.

### Code samples for "Get a webhook delivery for an organization webhook"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/hooks/HOOK_ID/deliveries/DELIVERY_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 12345678,
  "guid": "0b989ba4-242f-11e5-81e1-c7b6966d2516",
  "delivered_at": "2019-06-03T00:57:16Z",
  "redelivery": false,
  "duration": 0.27,
  "status": "OK",
  "status_code": 200,
  "event": "issues",
  "action": "opened",
  "installation_id": 123,
  "repository_id": 456,
  "url": "https://www.example.com",
  "throttled_at": "2019-06-03T00:57:16Z",
  "request": {
    "headers": {
      "X-GitHub-Delivery": "0b989ba4-242f-11e5-81e1-c7b6966d2516",
      "X-Hub-Signature-256": "sha256=6dcb09b5b57875f334f61aebed695e2e4193db5e",
      "Accept": "*/*",
      "X-GitHub-Hook-ID": "42",
      "User-Agent": "GitHub-Hookshot/b8c71d8",
      "X-GitHub-Event": "issues",
      "X-GitHub-Hook-Installation-Target-ID": "123",
      "X-GitHub-Hook-Installation-Target-Type": "repository",
      "content-type": "application/json",
      "X-Hub-Signature": "sha1=a84d88e7554fc1fa21bcbc4efae3c782a70d2b9d"
    },
    "payload": {
      "action": "opened",
      "issue": {
        "body": "foo"
      },
      "repository": {
        "id": 123
      }
    }
  },
  "response": {
    "headers": {
      "Content-Type": "text/html;charset=utf-8"
    },
    "payload": "ok"
  }
}
```

## Redeliver a delivery for an organization webhook
Redeliver a delivery for a webhook configured in an organization.
You must be an organization owner to use this endpoint.
OAuth app tokens and personal access tokens (classic) needadmin:org_hookscope. OAuth apps cannot list, view, or edit
webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Fine-grained access tokens for "Redeliver a delivery for an organization webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" organization permissions (write)

### Parameters for "Redeliver a delivery for an organization webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
delivery_idintegerRequired
[/TABLE]
The organization name. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

```
delivery_id
```

### HTTP response status codes for "Redeliver a delivery for an organization webhook"

[TABLE]
Status code | Description
202 | Accepted
400 | Bad Request
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Accepted
Bad Request
Validation failed, or the endpoint has been spammed.

### Code samples for "Redeliver a delivery for an organization webhook"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/hooks/HOOK_ID/deliveries/DELIVERY_ID/attempts
```

#### Accepted
- Example response
- Response schema

```
Status: 202
```

## Ping an organization webhook
This will trigger aping eventto be sent to the hook.
You must be an organization owner to use this endpoint.
OAuth app tokens and personal access tokens (classic) needadmin:org_hookscope. OAuth apps cannot list, view, or edit
webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Fine-grained access tokens for "Ping an organization webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" organization permissions (write)

### Parameters for "Ping an organization webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
[/TABLE]
The organization name. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

### HTTP response status codes for "Ping an organization webhook"

[TABLE]
Status code | Description
204 | No Content
404 | Resource not found
[/TABLE]
No Content
Resource not found

### Code samples for "Ping an organization webhook"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/hooks/HOOK_ID/pings
```

#### Response

```
Status: 204
```