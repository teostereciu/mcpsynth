# REST API endpoints for GPG keys

*Source: https://docs.github.com/en/rest/users/gpg-keys*

---

# REST API endpoints for GPG keys
Use the REST API to manage GPG keys of authenticated users.

## About user GPG key administration
The data returned in thepublic_keyresponse field is not a GPG formatted key. When a user uploads a GPG key, it is parsed and the cryptographic public key is extracted and stored. This cryptographic key is what the endpoints in this category will return. This key is not suitable for direct use in programs such as GPG.
If a request URL does not include a{username}parameter then the response will be for the signed-in user (and you must passauthentication informationwith your request). Additional private information, such as whether a user has two-factor authentication enabled, is included when authenticated through OAuth with theuserscope.

## List GPG keys for the authenticated user
Lists the current user's GPG keys.
OAuth app tokens and personal access tokens (classic) need theread:gpg_keyscope to use this endpoint.

### Fine-grained access tokens for "List GPG keys for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "GPG keys" user permissions (read)

### Parameters for "List GPG keys for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List GPG keys for the authenticated user"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Not modified
Requires authentication
Forbidden
Resource not found

### Code samples for "List GPG keys for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/gpg_keys
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
    "id": 3,
    "name": "Octocat's GPG Key",
    "primary_key_id": 2,
    "key_id": "3262EFF25BA0D270",
    "public_key": "xsBNBFayYZ...",
    "emails": [
      {
        "email": "octocat@users.noreply.github.com",
        "verified": true
      }
    ],
    "subkeys": [
      {
        "id": 4,
        "primary_key_id": 3,
        "key_id": "4A595D4C72EE49C7",
        "public_key": "zsBNBFayYZ...",
        "emails": [],
        "can_sign": false,
        "can_encrypt_comms": true,
        "can_encrypt_storage": true,
        "can_certify": false,
        "created_at": "2016-03-24T11:31:04-06:00",
        "expires_at": "2016-03-24T11:31:04-07:00",
        "revoked": false
      }
    ],
    "can_sign": true,
    "can_encrypt_comms": false,
    "can_encrypt_storage": false,
    "can_certify": true,
    "created_at": "2016-03-24T11:31:04-06:00",
    "expires_at": "2016-03-24T11:31:04-07:00",
    "revoked": false,
    "raw_key": "string"
  }
]
```

## Create a GPG key for the authenticated user
Adds a GPG key to the authenticated user's GitHub account.
OAuth app tokens and personal access tokens (classic) need thewrite:gpg_keyscope to use this endpoint.

### Fine-grained access tokens for "Create a GPG key for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "GPG keys" user permissions (write)

### Parameters for "Create a GPG key for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
namestringA descriptive name for the new key.
armored_public_keystringRequiredA GPG key in ASCII-armored format.
[/TABLE]
A descriptive name for the new key.

```
armored_public_key
```
A GPG key in ASCII-armored format.

### HTTP response status codes for "Create a GPG key for the authenticated user"

[TABLE]
Status code | Description
201 | Created
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Not modified
Requires authentication
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Create a GPG key for the authenticated user"

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
  https://api.github.com/user/gpg_keys \
  -d '{"name":"Octocat'\''s GPG Key","armored_public_key":"-----BEGIN PGP PUBLIC KEY BLOCK-----\nVersion: GnuPG v1\n\nmQINBFnZ2ZIBEADQ2Z7Z7\n-----END PGP PUBLIC KEY BLOCK-----"}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "id": 3,
  "name": "Octocat's GPG Key",
  "primary_key_id": 2,
  "key_id": "3262EFF25BA0D270",
  "public_key": "xsBNBFayYZ...",
  "emails": [
    {
      "email": "octocat@users.noreply.github.com",
      "verified": true
    }
  ],
  "subkeys": [
    {
      "id": 4,
      "primary_key_id": 3,
      "key_id": "4A595D4C72EE49C7",
      "public_key": "zsBNBFayYZ...",
      "emails": [],
      "can_sign": false,
      "can_encrypt_comms": true,
      "can_encrypt_storage": true,
      "can_certify": false,
      "created_at": "2016-03-24T11:31:04-06:00",
      "expires_at": "2016-03-24T11:31:04-07:00",
      "revoked": false
    }
  ],
  "can_sign": true,
  "can_encrypt_comms": false,
  "can_encrypt_storage": false,
  "can_certify": true,
  "created_at": "2016-03-24T11:31:04-06:00",
  "expires_at": "2016-03-24T11:31:04-07:00",
  "revoked": false,
  "raw_key": "\"-----BEGIN PGP PUBLIC KEY BLOCK-----\\nVersion: GnuPG v2\\n\\n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\\nIts/HFYRLiFgDLmTlxo=\\n=+OzK\\n-----END PGP PUBLIC KEY BLOCK-----\""
}
```

## Get a GPG key for the authenticated user
View extended details for a single GPG key.
OAuth app tokens and personal access tokens (classic) need theread:gpg_keyscope to use this endpoint.

### Fine-grained access tokens for "Get a GPG key for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "GPG keys" user permissions (read)

### Parameters for "Get a GPG key for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
gpg_key_idintegerRequiredThe unique identifier of the GPG key.
[/TABLE]
The unique identifier of the GPG key.

### HTTP response status codes for "Get a GPG key for the authenticated user"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Not modified
Requires authentication
Forbidden
Resource not found

### Code samples for "Get a GPG key for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/gpg_keys/GPG_KEY_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 3,
  "name": "Octocat's GPG Key",
  "primary_key_id": 2,
  "key_id": "3262EFF25BA0D270",
  "public_key": "xsBNBFayYZ...",
  "emails": [
    {
      "email": "octocat@users.noreply.github.com",
      "verified": true
    }
  ],
  "subkeys": [
    {
      "id": 4,
      "primary_key_id": 3,
      "key_id": "4A595D4C72EE49C7",
      "public_key": "zsBNBFayYZ...",
      "emails": [],
      "can_sign": false,
      "can_encrypt_comms": true,
      "can_encrypt_storage": true,
      "can_certify": false,
      "created_at": "2016-03-24T11:31:04-06:00",
      "expires_at": "2016-03-24T11:31:04-07:00",
      "revoked": false
    }
  ],
  "can_sign": true,
  "can_encrypt_comms": false,
  "can_encrypt_storage": false,
  "can_certify": true,
  "created_at": "2016-03-24T11:31:04-06:00",
  "expires_at": "2016-03-24T11:31:04-07:00",
  "revoked": false,
  "raw_key": "\"-----BEGIN PGP PUBLIC KEY BLOCK-----\\nVersion: GnuPG v2\\n\\n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\\nIts/HFYRLiFgDLmTlxo=\\n=+OzK\\n-----END PGP PUBLIC KEY BLOCK-----\""
}
```

## Delete a GPG key for the authenticated user
Removes a GPG key from the authenticated user's GitHub account.
OAuth app tokens and personal access tokens (classic) need theadmin:gpg_keyscope to use this endpoint.

### Fine-grained access tokens for "Delete a GPG key for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "GPG keys" user permissions (write)

### Parameters for "Delete a GPG key for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
gpg_key_idintegerRequiredThe unique identifier of the GPG key.
[/TABLE]
The unique identifier of the GPG key.

### HTTP response status codes for "Delete a GPG key for the authenticated user"

[TABLE]
Status code | Description
204 | No Content
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
No Content
Not modified
Requires authentication
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Delete a GPG key for the authenticated user"

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
  https://api.github.com/user/gpg_keys/GPG_KEY_ID
```

#### Response

```
Status: 204
```

## List GPG keys for a user
Lists the GPG keys for a user. This information is accessible by anyone.

### Fine-grained access tokens for "List GPG keys for a user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.

### Parameters for "List GPG keys for a user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The handle for the GitHub user account.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List GPG keys for a user"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List GPG keys for a user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/users/USERNAME/gpg_keys
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
    "id": 3,
    "name": "Octocat's GPG Key",
    "primary_key_id": 2,
    "key_id": "3262EFF25BA0D270",
    "public_key": "xsBNBFayYZ...",
    "emails": [
      {
        "email": "octocat@users.noreply.github.com",
        "verified": true
      }
    ],
    "subkeys": [
      {
        "id": 4,
        "primary_key_id": 3,
        "key_id": "4A595D4C72EE49C7",
        "public_key": "zsBNBFayYZ...",
        "emails": [],
        "can_sign": false,
        "can_encrypt_comms": true,
        "can_encrypt_storage": true,
        "can_certify": false,
        "created_at": "2016-03-24T11:31:04-06:00",
        "expires_at": "2016-03-24T11:31:04-07:00",
        "revoked": false
      }
    ],
    "can_sign": true,
    "can_encrypt_comms": false,
    "can_encrypt_storage": false,
    "can_certify": true,
    "created_at": "2016-03-24T11:31:04-06:00",
    "expires_at": "2016-03-24T11:31:04-07:00",
    "revoked": false,
    "raw_key": "string"
  }
]
```