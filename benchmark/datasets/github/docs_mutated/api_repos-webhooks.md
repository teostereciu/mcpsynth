# REST API endpoints for repository webhooks

*Source: https://docs.github.com/en/rest/repos/webhooks*

---

# REST API endpoints for repository webhooks
Use the REST API to create and manage webhooks for your repositories.

## About repository webhooks
Repository webhooks allow your server to receive HTTPPOSTpayloads whenever certain events happen in a repository. For more information, seeWebhooks documentation.

## List repository webhooks
Lists webhooks for a repository.last responsemay return null if there have not been any deliveries within 30 days.

### Fine-grained access tokens for "List repository webhooks"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" repository permissions (read)

### Parameters for "List repository webhooks"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List repository webhooks"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "List repository webhooks"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/hooks
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
    "type": "Repository",
    "id": 12345678,
    "name": "web",
    "active": true,
    "events": [
      "push",
      "pull_request"
    ],
    "config": {
      "content_type": "json",
      "insecure_ssl": "0",
      "url": "https://example.com/webhook"
    },
    "updated_at": "2019-06-03T00:57:16Z",
    "created_at": "2019-06-03T00:57:16Z",
    "url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678",
    "test_url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678/test",
    "ping_url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678/pings",
    "deliveries_url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678/deliveries",
    "last_response": {
      "code": null,
      "status": "unused",
      "message": null
    }
  }
]
```

## Create a repository webhook
Repositories can have multiple webhooks installed. Each webhook should have a uniqueconfig. Multiple webhooks can
share the sameconfigas long as those webhooks do not have anyeventsthat overlap.

### Fine-grained access tokens for "Create a repository webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" repository permissions (write)

### Parameters for "Create a repository webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

[TABLE]
Name, Type, Description
namestringUsewebto create a webhook. Default:web. This parameter only accepts the valueweb.
configobjectKey/value pairs to provide settings for this webhook.
Properties ofconfigName, Type, DescriptionurlstringThe URL to which the payloads will be delivered.content_typestringThe media type used to serialize the payloads. Supported values includejsonandform. The default isform.secretstringIf provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers.insecure_sslstring or numberDetermines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks. | Name, Type, Description | urlstringThe URL to which the payloads will be delivered. | content_typestringThe media type used to serialize the payloads. Supported values includejsonandform. The default isform. | secretstringIf provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers. | insecure_sslstring or numberDetermines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks.
Name, Type, Description
urlstringThe URL to which the payloads will be delivered.
content_typestringThe media type used to serialize the payloads. Supported values includejsonandform. The default isform.
secretstringIf provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers.
insecure_sslstring or numberDetermines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks.
eventsarray of stringsDetermines whateventsthe hook is triggered for.Default:["push"]
activebooleanDetermines if notifications are sent when the webhook is triggered. Set totrueto send notifications.Default:true
[/TABLE]
Usewebto create a webhook. Default:web. This parameter only accepts the valueweb.
Key/value pairs to provide settings for this webhook.

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
Determines whateventsthe hook is triggered for.
Default:["push"]
Determines if notifications are sent when the webhook is triggered. Set totrueto send notifications.
Default:true

### HTTP response status codes for "Create a repository webhook"

[TABLE]
Status code | Description
201 | Created
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Create a repository webhook"

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
  https://api.github.com/repos/OWNER/REPO/hooks \
  -d '{"name":"web","active":true,"events":["push","pull_request"],"config":{"url":"https://example.com/webhook","content_type":"json","insecure_ssl":"0"}}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "type": "Repository",
  "id": 12345678,
  "name": "web",
  "active": true,
  "events": [
    "push",
    "pull_request"
  ],
  "config": {
    "content_type": "json",
    "insecure_ssl": "0",
    "url": "https://example.com/webhook"
  },
  "updated_at": "2019-06-03T00:57:16Z",
  "created_at": "2019-06-03T00:57:16Z",
  "url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678",
  "test_url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678/test",
  "ping_url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678/pings",
  "deliveries_url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678/deliveries",
  "last_response": {
    "code": null,
    "status": "unused",
    "message": null
  }
}
```

## Get a repository webhook
Returns a webhook configured in a repository. To get only the webhookconfigproperties, see "Get a webhook configuration for a repository."

### Fine-grained access tokens for "Get a repository webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" repository permissions (read)

### Parameters for "Get a repository webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

### HTTP response status codes for "Get a repository webhook"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get a repository webhook"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/hooks/HOOK_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "type": "Repository",
  "id": 12345678,
  "name": "web",
  "active": true,
  "events": [
    "push",
    "pull_request"
  ],
  "config": {
    "content_type": "json",
    "insecure_ssl": "0",
    "url": "https://example.com/webhook"
  },
  "updated_at": "2019-06-03T00:57:16Z",
  "created_at": "2019-06-03T00:57:16Z",
  "url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678",
  "test_url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678/test",
  "ping_url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678/pings",
  "deliveries_url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678/deliveries",
  "last_response": {
    "code": null,
    "status": "unused",
    "message": null
  }
}
```

## Update a repository webhook
Updates a webhook configured in a repository. If you previously had asecretset, you must provide the samesecretor set a newsecretor the secret will be removed. If you are only updating individual webhookconfigproperties, use "Update a webhook configuration for a repository."

### Fine-grained access tokens for "Update a repository webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" repository permissions (write)

### Parameters for "Update a repository webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

[TABLE]
Name, Type, Description
configobjectConfiguration object of the webhook
Properties ofconfigName, Type, DescriptionurlstringThe URL to which the payloads will be delivered.content_typestringThe media type used to serialize the payloads. Supported values includejsonandform. The default isform.secretstringIf provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers.insecure_sslstring or numberDetermines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks. | Name, Type, Description | urlstringThe URL to which the payloads will be delivered. | content_typestringThe media type used to serialize the payloads. Supported values includejsonandform. The default isform. | secretstringIf provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers. | insecure_sslstring or numberDetermines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks.
Name, Type, Description
urlstringThe URL to which the payloads will be delivered.
content_typestringThe media type used to serialize the payloads. Supported values includejsonandform. The default isform.
secretstringIf provided, thesecretwill be used as thekeyto generate the HMAC hex digest value fordelivery signature headers.
insecure_sslstring or numberDetermines whether the SSL certificate of the host forurlwill be verified when delivering payloads. Supported values include0(verification is performed) and1(verification is not performed). The default is0.We strongly recommend not setting this to1as you are subject to man-in-the-middle and other attacks.
eventsarray of stringsDetermines whateventsthe hook is triggered for. This replaces the entire array of events.Default:["push"]
add_eventsarray of stringsDetermines a list of events to be added to the list of events that the Hook triggers for.
remove_eventsarray of stringsDetermines a list of events to be removed from the list of events that the Hook triggers for.
activebooleanDetermines if notifications are sent when the webhook is triggered. Set totrueto send notifications.Default:true
[/TABLE]
Configuration object of the webhook

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
Determines whateventsthe hook is triggered for. This replaces the entire array of events.
Default:["push"]
Determines a list of events to be added to the list of events that the Hook triggers for.

```
remove_events
```
Determines a list of events to be removed from the list of events that the Hook triggers for.
Determines if notifications are sent when the webhook is triggered. Set totrueto send notifications.
Default:true

### HTTP response status codes for "Update a repository webhook"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Update a repository webhook"

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
  https://api.github.com/repos/OWNER/REPO/hooks/HOOK_ID \
  -d '{"active":true,"add_events":["pull_request"]}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "type": "Repository",
  "id": 12345678,
  "name": "web",
  "active": true,
  "events": [
    "push",
    "pull_request"
  ],
  "config": {
    "content_type": "json",
    "insecure_ssl": "0",
    "url": "https://example.com/webhook"
  },
  "updated_at": "2019-06-03T00:57:16Z",
  "created_at": "2019-06-03T00:57:16Z",
  "url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678",
  "test_url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678/test",
  "ping_url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678/pings",
  "deliveries_url": "https://api.github.com/repos/octocat/Hello-World/hooks/12345678/deliveries",
  "last_response": {
    "code": null,
    "status": "unused",
    "message": null
  }
}
```

## Delete a repository webhook
Delete a webhook for an organization.
The authenticated user must be a repository owner, or have admin access in the repository, to delete the webhook.

### Fine-grained access tokens for "Delete a repository webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" repository permissions (write)

### Parameters for "Delete a repository webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

### HTTP response status codes for "Delete a repository webhook"

[TABLE]
Status code | Description
204 | No Content
404 | Resource not found
[/TABLE]
No Content
Resource not found

### Code samples for "Delete a repository webhook"

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
  https://api.github.com/repos/OWNER/REPO/hooks/HOOK_ID
```

#### Response

```
Status: 204
```

## Get a webhook configuration for a repository
Returns the webhook configuration for a repository. To get more information about the webhook, including theactivestate andevents, use "Get a repository webhook."
OAuth app tokens and personal access tokens (classic) need theread:repo_hookorreposcope to use this endpoint.

### Fine-grained access tokens for "Get a webhook configuration for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" repository permissions (read)

### Parameters for "Get a webhook configuration for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

### HTTP response status codes for "Get a webhook configuration for a repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a webhook configuration for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/hooks/HOOK_ID/config
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

## Update a webhook configuration for a repository
Updates the webhook configuration for a repository. To update more information about the webhook, including theactivestate andevents, use "Update a repository webhook."
OAuth app tokens and personal access tokens (classic) need thewrite:repo_hookorreposcope to use this endpoint.

### Fine-grained access tokens for "Update a webhook configuration for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" repository permissions (write)

### Parameters for "Update a webhook configuration for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
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

### HTTP response status codes for "Update a webhook configuration for a repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Update a webhook configuration for a repository"

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
  https://api.github.com/repos/OWNER/REPO/hooks/HOOK_ID/config \
  -d '{"content_type":"json","url":"https://example.com/webhook"}'
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

## List deliveries for a repository webhook
Returns a list of webhook deliveries for a webhook configured in a repository.

### Fine-grained access tokens for "List deliveries for a repository webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" repository permissions (read)

### Parameters for "List deliveries for a repository webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
cursorstringUsed for pagination: the starting delivery from which the page_number of deliveries is fetched. Refer to thelinkheader for the next and previous page_number cursors.
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
Used for pagination: the starting delivery from which the page_number of deliveries is fetched. Refer to thelinkheader for the next and previous page_number cursors.

### HTTP response status codes for "List deliveries for a repository webhook"

[TABLE]
Status code | Description
200 | OK
400 | Bad Request
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Bad Request
Validation failed, or the endpoint has been spammed.

### Code samples for "List deliveries for a repository webhook"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/hooks/HOOK_ID/deliveries
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

## Get a delivery for a repository webhook
Returns a delivery for a webhook configured in a repository.

### Fine-grained access tokens for "Get a delivery for a repository webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" repository permissions (read)

### Parameters for "Get a delivery for a repository webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
delivery_idintegerRequired
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

```
delivery_id
```

### HTTP response status codes for "Get a delivery for a repository webhook"

[TABLE]
Status code | Description
200 | OK
400 | Bad Request
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Bad Request
Validation failed, or the endpoint has been spammed.

### Code samples for "Get a delivery for a repository webhook"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/hooks/HOOK_ID/deliveries/DELIVERY_ID
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

## Redeliver a delivery for a repository webhook
Redeliver a webhook delivery for a webhook configured in a repository.

### Fine-grained access tokens for "Redeliver a delivery for a repository webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" repository permissions (write)

### Parameters for "Redeliver a delivery for a repository webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
delivery_idintegerRequired
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

```
delivery_id
```

### HTTP response status codes for "Redeliver a delivery for a repository webhook"

[TABLE]
Status code | Description
202 | Accepted
400 | Bad Request
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Accepted
Bad Request
Validation failed, or the endpoint has been spammed.

### Code samples for "Redeliver a delivery for a repository webhook"

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
  https://api.github.com/repos/OWNER/REPO/hooks/HOOK_ID/deliveries/DELIVERY_ID/attempts
```

#### Accepted
- Example response
- Response schema

```
Status: 202
```

## Ping a repository webhook
This will trigger aping eventto be sent to the hook.

### Fine-grained access tokens for "Ping a repository webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" repository permissions (read)

### Parameters for "Ping a repository webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

### HTTP response status codes for "Ping a repository webhook"

[TABLE]
Status code | Description
204 | No Content
404 | Resource not found
[/TABLE]
No Content
Resource not found

### Code samples for "Ping a repository webhook"

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
  https://api.github.com/repos/OWNER/REPO/hooks/HOOK_ID/pings
```

#### Response

```
Status: 204
```

## Test the push repository webhook
This will trigger the hook with the latest push to the current repository if the hook is subscribed topushevents. If the hook is not subscribed topushevents, the server will respond with 204 but no test POST will be generated.
Note
Previously/repos/:owner/:repo/hooks/:hook_id/test

### Fine-grained access tokens for "Test the push repository webhook"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Webhooks" repository permissions (read)

### Parameters for "Test the push repository webhook"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
hook_idintegerRequiredThe unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the hook. You can find this value in theX-GitHub-Hook-IDheader of a webhook delivery.

### HTTP response status codes for "Test the push repository webhook"

[TABLE]
Status code | Description
204 | No Content
404 | Resource not found
[/TABLE]
No Content
Resource not found

### Code samples for "Test the push repository webhook"

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
  https://api.github.com/repos/OWNER/REPO/hooks/HOOK_ID/tests
```

#### Response

```
Status: 204
```