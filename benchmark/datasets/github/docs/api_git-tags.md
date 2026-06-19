# REST API endpoints for Git tags

*Source: https://docs.github.com/en/rest/git/tags*

---

# REST API endpoints for Git tags
Use the REST API to interact with tag objects in your Git database on GitHub.

## About Git tags
A Git tag is similar to aGit reference, but the Git commit that it points to never changes. Git tags are helpful when you want to point to specific releases. These endpoints allow you to read and writetag objectsto your Git database on GitHub. The API only supportsannotated tag objects, not lightweight tags.

## Create a tag object
Note that creating a tag object does not create the reference that makes a tag in Git. If you want to create an annotated tag in Git, you have to do this call to create the tag object, and thencreatetherefs/tags/[tag]reference. If you want to create a lightweight tag, you only have tocreatethe tag reference - this call would be unnecessary.
Signature verification object
The response will include averificationobject that describes the result of verifying the commit's signature. The following fields are included in theverificationobject:

[TABLE]
Name | Type | Description
verified | boolean | Indicates whether GitHub considers the signature in this commit to be verified.
reason | string | The reason for verified value. Possible values and their meanings are enumerated in table below.
signature | string | The signature that was extracted from the commit.
payload | string | The value that was signed.
verified_at | string | The date the signature was verified by GitHub.
[/TABLE]

```
verified_at
```
These are the possible values forreasonin theverificationobject:

[TABLE]
Value | Description
expired_key | The key that made the signature is expired.
not_signing_key | The "signing" flag is not among the usage flags in the GPG key that made the signature.
gpgverify_error | There was an error communicating with the signature verification service.
gpgverify_unavailable | The signature verification service is currently unavailable.
unsigned | The object does not include a signature.
unknown_signature_type | A non-PGP signature was found in the commit.
no_user | No user was associated with thecommitteremail address in the commit.
unverified_email | Thecommitteremail address in the commit was associated with a user, but the email address is not verified on their account.
bad_email | Thecommitteremail address in the commit is not included in the identities of the PGP key that made the signature.
unknown_key | The key that made the signature has not been registered with any user's account.
malformed_signature | There was an error parsing the signature.
invalid | The signature could not be cryptographically verified using the key whose key-id was found in the signature.
valid | None of the above errors applied, so the signature is considered to be verified.
[/TABLE]

```
expired_key
```

```
not_signing_key
```

```
gpgverify_error
```

```
gpgverify_unavailable
```

```
unknown_signature_type
```

```
unverified_email
```

```
unknown_key
```

```
malformed_signature
```

### Fine-grained access tokens for "Create a tag object"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Create a tag object"

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
tagstringRequiredThe tag's name. This is typically a version (e.g., "v0.0.1").
messagestringRequiredThe tag message.
objectstringRequiredThe SHA of the git object this is tagging.
typestringRequiredThe type of the object we're tagging. Normally this is acommitbut it can also be atreeor ablob.Can be one of:commit,tree,blob
taggerobjectAn object with information about the individual creating the tag.
Properties oftaggerName, Type, DescriptionnamestringRequiredThe name of the author of the tagemailstringRequiredThe email of the author of the tagdatestringWhen this object was tagged. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ. | Name, Type, Description | namestringRequiredThe name of the author of the tag | emailstringRequiredThe email of the author of the tag | datestringWhen this object was tagged. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
Name, Type, Description
namestringRequiredThe name of the author of the tag
emailstringRequiredThe email of the author of the tag
datestringWhen this object was tagged. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
[/TABLE]
The tag's name. This is typically a version (e.g., "v0.0.1").
The tag message.
The SHA of the git object this is tagging.
The type of the object we're tagging. Normally this is acommitbut it can also be atreeor ablob.
Can be one of:commit,tree,blob
An object with information about the individual creating the tag.

[TABLE]
Name, Type, Description
namestringRequiredThe name of the author of the tag
emailstringRequiredThe email of the author of the tag
datestringWhen this object was tagged. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
[/TABLE]
The name of the author of the tag
The email of the author of the tag
When this object was tagged. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

### HTTP response status codes for "Create a tag object"

[TABLE]
Status code | Description
201 | Created
409 | Conflict
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Conflict
Validation failed, or the endpoint has been spammed.

### Code samples for "Create a tag object"

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
  https://api.github.com/repos/OWNER/REPO/git/tags \
  -d '{"tag":"v0.0.1","message":"initial version","object":"c3d0be41ecbe669545ee3e94d31ed9a4bc91ee3c","type":"commit","tagger":{"name":"Monalisa Octocat","email":"octocat@github.com","date":"2011-06-17T14:53:35-07:00"}}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "node_id": "MDM6VGFnOTQwYmQzMzYyNDhlZmFlMGY5ZWU1YmM3YjJkNWM5ODU4ODdiMTZhYw==",
  "tag": "v0.0.1",
  "sha": "940bd336248efae0f9ee5bc7b2d5c985887b16ac",
  "url": "https://api.github.com/repos/octocat/Hello-World/git/tags/940bd336248efae0f9ee5bc7b2d5c985887b16ac",
  "message": "initial version",
  "tagger": {
    "name": "Monalisa Octocat",
    "email": "octocat@github.com",
    "date": "2014-11-07T22:01:45Z"
  },
  "object": {
    "type": "commit",
    "sha": "c3d0be41ecbe669545ee3e94d31ed9a4bc91ee3c",
    "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/c3d0be41ecbe669545ee3e94d31ed9a4bc91ee3c"
  },
  "verification": {
    "verified": false,
    "reason": "unsigned",
    "signature": null,
    "payload": null,
    "verified_at": null
  }
}
```

## Get a tag
Signature verification object
The response will include averificationobject that describes the result of verifying the commit's signature. The following fields are included in theverificationobject:

[TABLE]
Name | Type | Description
verified | boolean | Indicates whether GitHub considers the signature in this commit to be verified.
reason | string | The reason for verified value. Possible values and their meanings are enumerated in table below.
signature | string | The signature that was extracted from the commit.
payload | string | The value that was signed.
verified_at | string | The date the signature was verified by GitHub.
[/TABLE]

```
verified_at
```
These are the possible values forreasonin theverificationobject:

[TABLE]
Value | Description
expired_key | The key that made the signature is expired.
not_signing_key | The "signing" flag is not among the usage flags in the GPG key that made the signature.
gpgverify_error | There was an error communicating with the signature verification service.
gpgverify_unavailable | The signature verification service is currently unavailable.
unsigned | The object does not include a signature.
unknown_signature_type | A non-PGP signature was found in the commit.
no_user | No user was associated with thecommitteremail address in the commit.
unverified_email | Thecommitteremail address in the commit was associated with a user, but the email address is not verified on their account.
bad_email | Thecommitteremail address in the commit is not included in the identities of the PGP key that made the signature.
unknown_key | The key that made the signature has not been registered with any user's account.
malformed_signature | There was an error parsing the signature.
invalid | The signature could not be cryptographically verified using the key whose key-id was found in the signature.
valid | None of the above errors applied, so the signature is considered to be verified.
[/TABLE]

```
expired_key
```

```
not_signing_key
```

```
gpgverify_error
```

```
gpgverify_unavailable
```

```
unknown_signature_type
```

```
unverified_email
```

```
unknown_key
```

```
malformed_signature
```

### Fine-grained access tokens for "Get a tag"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a tag"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
tag_shastringRequired
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Get a tag"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
409 | Conflict
[/TABLE]
OK
Resource not found
Conflict

### Code samples for "Get a tag"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/git/tags/TAG_SHA
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "node_id": "MDM6VGFnOTQwYmQzMzYyNDhlZmFlMGY5ZWU1YmM3YjJkNWM5ODU4ODdiMTZhYw==",
  "tag": "v0.0.1",
  "sha": "940bd336248efae0f9ee5bc7b2d5c985887b16ac",
  "url": "https://api.github.com/repos/octocat/Hello-World/git/tags/940bd336248efae0f9ee5bc7b2d5c985887b16ac",
  "message": "initial version",
  "tagger": {
    "name": "Monalisa Octocat",
    "email": "octocat@github.com",
    "date": "2014-11-07T22:01:45Z"
  },
  "object": {
    "type": "commit",
    "sha": "c3d0be41ecbe669545ee3e94d31ed9a4bc91ee3c",
    "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/c3d0be41ecbe669545ee3e94d31ed9a4bc91ee3c"
  },
  "verification": {
    "verified": false,
    "reason": "unsigned",
    "signature": null,
    "payload": null,
    "verified_at": null
  }
}
```