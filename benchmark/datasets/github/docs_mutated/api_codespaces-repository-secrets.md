# REST API endpoints for Codespaces repository secrets

*Source: https://docs.github.com/en/rest/codespaces/repository-secrets*

---

# REST API endpoints for Codespaces repository secrets
Use the REST API to manage secrets for repositories that the user has access to in a codespace.

## Who can use this feature?
Users with write access to a repository can manage Codespaces repository secrets.

## About Codespaces repository secrets
You can create, list, and delete secrets (such as access tokens for cloud services) for repositories that the user has access to. These secrets are made available to the codespace at runtime. For more information, seeManaging your account-specific secrets for GitHub Codespaces.

## List repository secrets
Lists all development environment secrets available in a repository without revealing their encrypted
values.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "List repository secrets"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces secrets" repository permissions (write)

### Parameters for "List repository secrets"

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

### HTTP response status codes for "List repository secrets"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List repository secrets"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/codespaces/secrets
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 2,
  "secrets": [
    {
      "name": "GH_TOKEN",
      "created_at": "2019-08-10T14:59:22Z",
      "updated_at": "2020-01-10T14:59:22Z",
      "visibility": "all"
    },
    {
      "name": "GIST_ID",
      "created_at": "2020-01-10T10:59:22Z",
      "updated_at": "2020-01-11T11:59:22Z",
      "visibility": "all"
    }
  ]
}
```

## Get a repository public key
Gets your public key, which you need to encrypt secrets. You need to
encrypt a secret before you can create or update secrets.
If the repository is private, OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get a repository public key"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces secrets" repository permissions (write)

### Parameters for "Get a repository public key"

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

### HTTP response status codes for "Get a repository public key"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a repository public key"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/codespaces/secrets/public-key
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "key_id": "012345678912345678",
  "key": "2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvv1234"
}
```

## Get a repository secret
Gets a single repository development environment secret without revealing its encrypted value.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get a repository secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces secrets" repository permissions (write)

### Parameters for "Get a repository secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
secret_namestringRequiredThe name of the secret.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
secret_name
```
The name of the secret.

### HTTP response status codes for "Get a repository secret"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a repository secret"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/codespaces/secrets/SECRET_NAME
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "name": "GH_TOKEN",
  "created_at": "2019-08-10T14:59:22Z",
  "updated_at": "2020-01-10T14:59:22Z",
  "visibility": "all"
}
```

## Create or update a repository secret
Creates or updates a repository development environment secret with an encrypted value. Encrypt your secret usingLibSodium. For more information, see "Encrypting secrets for the REST API."
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint. The associated user must be a repository admin.

### Fine-grained access tokens for "Create or update a repository secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces secrets" repository permissions (write)

### Parameters for "Create or update a repository secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
secret_namestringRequiredThe name of the secret.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
secret_name
```
The name of the secret.

[TABLE]
Name, Type, Description
encrypted_valuestringValue for your secret, encrypted withLibSodiumusing the public key retrieved from theGet a repository public keyendpoint.
key_idstringID of the key you used to encrypt the secret.
[/TABLE]

```
encrypted_value
```
Value for your secret, encrypted withLibSodiumusing the public key retrieved from theGet a repository public keyendpoint.
ID of the key you used to encrypt the secret.

### HTTP response status codes for "Create or update a repository secret"

[TABLE]
Status code | Description
201 | Response when creating a secret
204 | Response when updating a secret
[/TABLE]
Response when creating a secret
Response when updating a secret

### Code samples for "Create or update a repository secret"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/codespaces/secrets/SECRET_NAME \
  -d '{"encrypted_value":"c2VjcmV0","key_id":"012345678912345678"}'
```

#### Response when creating a secret
- Example response
- Response schema

```
Status: 201
```

## Delete a repository secret
Deletes a development environment secret in a repository using the secret name.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint. The associated user must be a repository admin.

### Fine-grained access tokens for "Delete a repository secret"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces secrets" repository permissions (write)

### Parameters for "Delete a repository secret"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
secret_namestringRequiredThe name of the secret.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
secret_name
```
The name of the secret.

### HTTP response status codes for "Delete a repository secret"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete a repository secret"

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
  https://api.github.com/repos/OWNER/REPO/codespaces/secrets/SECRET_NAME
```

#### Response

```
Status: 204
```