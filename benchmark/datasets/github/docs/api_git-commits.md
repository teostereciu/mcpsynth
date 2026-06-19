# REST API endpoints for Git commits

*Source: https://docs.github.com/en/rest/git/commits*

---

# REST API endpoints for Git commits
Use the REST API to interact with commit objects in your Git database on GitHub.

## About Git commits
A Git commit is a snapshot of the hierarchy (Git tree) and the contents of the files (Git blob) in a Git repository. These endpoints allow you to read and writecommit objectsto your Git database on GitHub.

## Create a commit
Creates a new Gitcommit object.
Signature verification object
The response will include averificationobject that describes the result of verifying the commit's signature. The following fields are included in theverificationobject:

[TABLE]
Name | Type | Description
verified | boolean | Indicates whether GitHub considers the signature in this commit to be verified.
reason | string | The reason for verified value. Possible values and their meanings are enumerated in the table below.
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

### Fine-grained access tokens for "Create a commit"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Create a commit"

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
messagestringRequiredThe commit message
treestringRequiredThe SHA of the tree object this commit points to
parentsarray of stringsThe full SHAs of the commits that were the parents of this commit. If omitted or empty, the commit will be written as a root commit. For a single parent, an array of one SHA should be provided; for a merge commit, an array of more than one should be provided.
authorobjectInformation about the author of the commit. By default, theauthorwill be the authenticated user and the current date. See theauthorandcommitterobject below for details.
Properties ofauthorName, Type, DescriptionnamestringRequiredThe name of the author (or committer) of the commitemailstringRequiredThe email of the author (or committer) of the commitdatestringIndicates when this commit was authored (or committed). This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ. | Name, Type, Description | namestringRequiredThe name of the author (or committer) of the commit | emailstringRequiredThe email of the author (or committer) of the commit | datestringIndicates when this commit was authored (or committed). This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
Name, Type, Description
namestringRequiredThe name of the author (or committer) of the commit
emailstringRequiredThe email of the author (or committer) of the commit
datestringIndicates when this commit was authored (or committed). This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
committerobjectInformation about the person who is making the commit. By default,committerwill use the information set inauthor. See theauthorandcommitterobject below for details.
Properties ofcommitterName, Type, DescriptionnamestringThe name of the author (or committer) of the commitemailstringThe email of the author (or committer) of the commitdatestringIndicates when this commit was authored (or committed). This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ. | Name, Type, Description | namestringThe name of the author (or committer) of the commit | emailstringThe email of the author (or committer) of the commit | datestringIndicates when this commit was authored (or committed). This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
Name, Type, Description
namestringThe name of the author (or committer) of the commit
emailstringThe email of the author (or committer) of the commit
datestringIndicates when this commit was authored (or committed). This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
signaturestringThePGP signatureof the commit. GitHub adds the signature to thegpgsigheader of the created commit. For a commit signature to be verifiable by Git or GitHub, it must be an ASCII-armored detached PGP signature over the string commit as it would be written to the object database. To pass asignatureparameter, you need to first manually create a valid PGP signature, which can be complicated. You may find it easier touse the command lineto create signed commits.
[/TABLE]
The commit message
The SHA of the tree object this commit points to
The full SHAs of the commits that were the parents of this commit. If omitted or empty, the commit will be written as a root commit. For a single parent, an array of one SHA should be provided; for a merge commit, an array of more than one should be provided.
Information about the author of the commit. By default, theauthorwill be the authenticated user and the current date. See theauthorandcommitterobject below for details.

[TABLE]
Name, Type, Description
namestringRequiredThe name of the author (or committer) of the commit
emailstringRequiredThe email of the author (or committer) of the commit
datestringIndicates when this commit was authored (or committed). This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
[/TABLE]
The name of the author (or committer) of the commit
The email of the author (or committer) of the commit
Indicates when this commit was authored (or committed). This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
Information about the person who is making the commit. By default,committerwill use the information set inauthor. See theauthorandcommitterobject below for details.

[TABLE]
Name, Type, Description
namestringThe name of the author (or committer) of the commit
emailstringThe email of the author (or committer) of the commit
datestringIndicates when this commit was authored (or committed). This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
[/TABLE]
The name of the author (or committer) of the commit
The email of the author (or committer) of the commit
Indicates when this commit was authored (or committed). This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
ThePGP signatureof the commit. GitHub adds the signature to thegpgsigheader of the created commit. For a commit signature to be verifiable by Git or GitHub, it must be an ASCII-armored detached PGP signature over the string commit as it would be written to the object database. To pass asignatureparameter, you need to first manually create a valid PGP signature, which can be complicated. You may find it easier touse the command lineto create signed commits.

### HTTP response status codes for "Create a commit"

[TABLE]
Status code | Description
201 | Created
404 | Resource not found
409 | Conflict
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Resource not found
Conflict
Validation failed, or the endpoint has been spammed.

### Code samples for "Create a commit"

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
  https://api.github.com/repos/OWNER/REPO/git/commits \
  -d '{"message":"my commit message","author":{"name":"Mona Octocat","email":"octocat@github.com","date":"2008-07-09T16:13:30+12:00"},"parents":["7d1b31e74ee336d15cbd21741bc88a537ed063a0"],"tree":"827efc6d56897b048c772eb4087f854f46256132","signature":"-----BEGIN PGP SIGNATURE-----\n\niQIzBAABAQAdFiEESn/54jMNIrGSE6Tp6cQjvhfv7nAFAlnT71cACgkQ6cQjvhfv\n7nCWwA//XVqBKWO0zF+bZl6pggvky3Oc2j1pNFuRWZ29LXpNuD5WUGXGG209B0hI\nDkmcGk19ZKUTnEUJV2Xd0R7AW01S/YSub7OYcgBkI7qUE13FVHN5ln1KvH2all2n\n2+JCV1HcJLEoTjqIFZSSu/sMdhkLQ9/NsmMAzpf/iIM0nQOyU4YRex9eD1bYj6nA\nOQPIDdAuaTQj1gFPHYLzM4zJnCqGdRlg0sOM/zC5apBNzIwlgREatOYQSCfCKV7k\nnrU34X8b9BzQaUx48Qa+Dmfn5KQ8dl27RNeWAqlkuWyv3pUauH9UeYW+KyuJeMkU\n+NyHgAsWFaCFl23kCHThbLStMZOYEnGagrd0hnm1TPS4GJkV4wfYMwnI4KuSlHKB\njHl3Js9vNzEUQipQJbgCgTiWvRJoK3ENwBTMVkKHaqT4x9U4Jk/XZB6Q8MA09ezJ\n3QgiTjTAGcum9E9QiJqMYdWQPWkaBIRRz5cET6HPB48YNXAAUsfmuYsGrnVLYbG+\nUpC6I97VybYHTy2O9XSGoaLeMI9CsFn38ycAxxbWagk5mhclNTP5mezIq6wKSwmr\nX11FW3n1J23fWZn5HJMBsRnUCgzqzX3871IqLYHqRJ/bpZ4h20RhTyPj5c/z7QXp\neSakNQMfbbMcljkha+ZMuVQX1K9aRlVqbmv3ZMWh+OijLYVU2bc=\n=5Io4\n-----END PGP SIGNATURE-----\n"}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "sha": "7638417db6d59f3c431d3e1f261cc637155684cd",
  "node_id": "MDY6Q29tbWl0NzYzODQxN2RiNmQ1OWYzYzQzMWQzZTFmMjYxY2M2MzcxNTU2ODRjZA==",
  "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/7638417db6d59f3c431d3e1f261cc637155684cd",
  "author": {
    "date": "2014-11-07T22:01:45Z",
    "name": "Monalisa Octocat",
    "email": "octocat@github.com"
  },
  "committer": {
    "date": "2014-11-07T22:01:45Z",
    "name": "Monalisa Octocat",
    "email": "octocat@github.com"
  },
  "message": "my commit message",
  "tree": {
    "url": "https://api.github.com/repos/octocat/Hello-World/git/trees/827efc6d56897b048c772eb4087f854f46256132",
    "sha": "827efc6d56897b048c772eb4087f854f46256132"
  },
  "parents": [
    {
      "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/7d1b31e74ee336d15cbd21741bc88a537ed063a0",
      "sha": "7d1b31e74ee336d15cbd21741bc88a537ed063a0",
      "html_url": "https://github.com/octocat/Hello-World/commit/7d1b31e74ee336d15cbd21741bc88a537ed063a0"
    }
  ],
  "verification": {
    "verified": false,
    "reason": "unsigned",
    "signature": null,
    "payload": null,
    "verified_at": null
  },
  "html_url": "https://github.com/octocat/Hello-World/commit/7638417db6d59f3c431d3e1f261cc637155684cd"
}
```

## Get a commit object
Gets a Gitcommit object.
To get the contents of a commit, see "Get a commit."
Signature verification object
The response will include averificationobject that describes the result of verifying the commit's signature. The following fields are included in theverificationobject:

[TABLE]
Name | Type | Description
verified | boolean | Indicates whether GitHub considers the signature in this commit to be verified.
reason | string | The reason for verified value. Possible values and their meanings are enumerated in the table below.
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

### Fine-grained access tokens for "Get a commit object"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a commit object"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
commit_shastringRequiredThe SHA of the commit.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The SHA of the commit.

### HTTP response status codes for "Get a commit object"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
409 | Conflict
[/TABLE]
OK
Resource not found
Conflict

### Code samples for "Get a commit object"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/git/commits/COMMIT_SHA
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "sha": "7638417db6d59f3c431d3e1f261cc637155684cd",
  "node_id": "MDY6Q29tbWl0NmRjYjA5YjViNTc4NzVmMzM0ZjYxYWViZWQ2OTVlMmU0MTkzZGI1ZQ==",
  "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/7638417db6d59f3c431d3e1f261cc637155684cd",
  "html_url": "https://github.com/octocat/Hello-World/commit/7638417db6d59f3c431d3e1f261cc637155684cd",
  "author": {
    "date": "2014-11-07T22:01:45Z",
    "name": "Monalisa Octocat",
    "email": "octocat@github.com"
  },
  "committer": {
    "date": "2014-11-07T22:01:45Z",
    "name": "Monalisa Octocat",
    "email": "octocat@github.com"
  },
  "message": "added readme, because im a good github citizen",
  "tree": {
    "url": "https://api.github.com/repos/octocat/Hello-World/git/trees/691272480426f78a0138979dd3ce63b77f706feb",
    "sha": "691272480426f78a0138979dd3ce63b77f706feb"
  },
  "parents": [
    {
      "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/1acc419d4d6a9ce985db7be48c6349a0475975b5",
      "sha": "1acc419d4d6a9ce985db7be48c6349a0475975b5",
      "html_url": "https://github.com/octocat/Hello-World/commit/7638417db6d59f3c431d3e1f261cc637155684cd"
    }
  ],
  "verification": {
    "verified": false,
    "reason": "unsigned",
    "signature": null,
    "payload": null,
    "verified_at": null
  }
}
```