# REST API endpoints for repository contents

*Source: https://docs.github.com/en/rest/repos/contents*

---

# REST API endpoints for repository contents
Use the REST API to create, modify, and delete Base64 encoded content in a repository.

## Get repository content
Gets the contents of a file or directory in a repository. Specify the file path or directory with thepathparameter. If you omit thepathparameter, you will receive the contents of the repository's root directory.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github.raw+json: Returns the raw file contents for files and symlinks.
- application/vnd.github.html+json: Returns the file contents in HTML. Markup languages are rendered to HTML using GitHub's open-sourceMarkup library.
- application/vnd.github.object+json: Returns the contents in a consistent object format regardless of the content type. For example, instead of an array of objects for a directory, the response will be an object with anentriesattribute containing the array of objects.

```
application/vnd.github.raw+json
```

```
application/vnd.github.html+json
```

```
application/vnd.github.object+json
```
If the content is a directory: The response will be an array of objects, one object for each item in the directory.
If the content is a symlink and the symlink's target is a normal file in the repository, then the API responds with the content of the file. Otherwise, the API responds with an object describing the symlink itself.
If the content is a submodule, thesubmodule_git_urlfield identifies the location of the submodule repository, and theshaidentifies a specific commit within the submodule repository. Git uses the given URL when cloning the submodule repository, and checks out the submodule at that specific commit. If the submodule repository is not hosted on github.com, the Git URLs (git_urland_links["git"]) and the github.com URLs (html_urland_links["html"]) will have null values.
Notes:
- To get a repository's contents recursively, you canrecursively get the tree.
- This API has an upper limit of 1,000 files for a directory. If you need to retrieve
more files, use theGit Trees API.
- Download URLs expire and are meant to be used just once. To ensure the download URL does not expire, please use the contents API to obtain a fresh download URL for each download.
- If the requested file's size is:1 MB or smaller: All features of this endpoint are supported.Between 1-100 MB: Only theraworobjectcustom media types are supported. Both will work as normal, except that when using theobjectmedia type, thecontentfield will be an empty
string and theencodingfield will be"none". To get the contents of these larger files, use therawmedia type.Greater than 100 MB: This endpoint is not supported.
- 1 MB or smaller: All features of this endpoint are supported.
- Between 1-100 MB: Only theraworobjectcustom media types are supported. Both will work as normal, except that when using theobjectmedia type, thecontentfield will be an empty
string and theencodingfield will be"none". To get the contents of these larger files, use therawmedia type.
- Greater than 100 MB: This endpoint is not supported.

### Fine-grained access tokens for "Get repository content"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get repository content"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
pathstringRequiredpath parameter
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
path parameter

[TABLE]
Name, Type, Description
refstringThe name of the commit/branch/tag. Default: the repository’s default branch.
[/TABLE]
The name of the commit/branch/tag. Default: the repository’s default branch.

### HTTP response status codes for "Get repository content"

[TABLE]
Status code | Description
200 | OK
302 | Found
304 | Not modified
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Found
Not modified
Forbidden
Resource not found

### Code samples for "Get repository content"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github.object" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/contents/PATH
```

#### Response if content is a file
- Example response
- Response schema

```
Status: 200
```

```
{
  "type": "file",
  "encoding": "base64",
  "size": 5362,
  "name": "README.md",
  "path": "README.md",
  "content": "IyBZb2dhIEJvmsgaW4gcHJvZ3Jlc3MhIEZlZWwgdAoKOndhcm5pbmc6IFdvc\\nZnJlZSBmUgdG8gY0byBjaGVjayBvdXQgdGhlIGFwcCwgYnV0IGJlIHN1c29t\\nZSBiYWNrIG9uY2UgaXQgaXMgY29tcGxldGUuCgpBIHdlYiBhcHAgdGhhdCBs\\nZWFkcyB5b3UgdGhyb3VnaCBhIHlvZ2Egc2Vzc2lvbi4KCltXb3Jrb3V0IG5v\\ndyFdKGh0dHBzOi8vc2tlZHdhcmRzODguZ2l0aHViLmlvL3lvZ2EvKQoKPGlt\\nZyBzcmM9InNyYy9pbWFnZXMvbWFza2FibGVfaWNvbl81MTIucG5nIiBhbHQ9\\nImJvdCBsaWZ0aW5nIHdlaWdodHMiIHdpZHRoPSIxMDAiLz4KCkRvIHlvdSBo\\nYXZlIGZlZWRiYWNrIG9yIGlkZWFzIGZvciBpbXByb3ZlbWVudD8gW09wZW4g\\nYW4gaXNzdWVdKGh0dHBzOi8vZ2l0aHViLmNvbS9za2Vkd2FyZHM4OC95b2dh\\nL2lzc3Vlcy9uZXcpLgoKV2FudCBtb3JlIGdhbWVzPyBWaXNpdCBbQ25TIEdh\\nbWVzXShodHRwczovL3NrZWR3YXJkczg4LmdpdGh1Yi5pby9wb3J0Zm9saW8v\\nKS4KCiMjIERldmVsb3BtZW50CgpUbyBhZGQgYSBuZXcgcG9zZSwgYWRkIGFu\\nIGVudHJ5IHRvIHRoZSByZWxldmFudCBmaWxlIGluIGBzcmMvYXNhbmFzYC4K\\nClRvIGJ1aWxkLCBydW4gYG5wbSBydW4gYnVpbGRgLgoKVG8gcnVuIGxvY2Fs\\nbHkgd2l0aCBsaXZlIHJlbG9hZGluZyBhbmQgbm8gc2VydmljZSB3b3JrZXIs\\nIHJ1biBgbnBtIHJ1biBkZXZgLiAoSWYgYSBzZXJ2aWNlIHdvcmtlciB3YXMg\\ncHJldmlvdXNseSByZWdpc3RlcmVkLCB5b3UgY2FuIHVucmVnaXN0ZXIgaXQg\\naW4gY2hyb21lIGRldmVsb3BlciB0b29sczogYEFwcGxpY2F0aW9uYCA+IGBT\\nZXJ2aWNlIHdvcmtlcnNgID4gYFVucmVnaXN0ZXJgLikKClRvIHJ1biBsb2Nh\\nbGx5IGFuZCByZWdpc3RlciB0aGUgc2VydmljZSB3b3JrZXIsIHJ1biBgbnBt\\nIHN0YXJ0YC4KClRvIGRlcGxveSwgcHVzaCB0byBgbWFpbmAgb3IgbWFudWFs\\nbHkgdHJpZ2dlciB0aGUgYC5naXRodWIvd29ya2Zsb3dzL2RlcGxveS55bWxg\\nIHdvcmtmbG93Lgo=\\n",
  "sha": "3d21ec53a331a6f037a91c368710b99387d012c1",
  "url": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
  "git_url": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
  "html_url": "https://github.com/octokit/octokit.rb/blob/master/README.md",
  "download_url": "https://raw.githubusercontent.com/octokit/octokit.rb/master/README.md",
  "_links": {
    "git": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
    "self": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
    "html": "https://github.com/octokit/octokit.rb/blob/master/README.md"
  }
}
```

## Create or update file contents
Creates a new file or replaces an existing file in a repository.
Note
If you use this endpoint and the "Delete a file" endpoint in parallel, the concurrent requests will conflict and you will receive errors. You must use these endpoints serially instead.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint. Theworkflowscope is also required in order to modify files in the.github/workflowsdirectory.

### Fine-grained access tokens for "Create or update file contents"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Contents" repository permissions (write)
- "Contents" repository permissions (write)and"Workflows" repository permissions (write)

### Parameters for "Create or update file contents"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
pathstringRequiredpath parameter
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
path parameter

[TABLE]
Name, Type, Description
messagestringRequiredThe commit message.
contentstringRequiredThe new file content, using Base64 encoding.
shastringRequired if you are updating a file. The blob SHA of the file being replaced.
branchstringThe branch name. Default: the repository’s default branch.
committerobjectThe person that committed the file. Default: the authenticated user.
Properties ofcommitterName, Type, DescriptionnamestringRequiredThe name of the author or committer of the commit. You'll receive a422status code ifnameis omitted.emailstringRequiredThe email of the author or committer of the commit. You'll receive a422status code ifemailis omitted.datestring | Name, Type, Description | namestringRequiredThe name of the author or committer of the commit. You'll receive a422status code ifnameis omitted. | emailstringRequiredThe email of the author or committer of the commit. You'll receive a422status code ifemailis omitted. | datestring
Name, Type, Description
namestringRequiredThe name of the author or committer of the commit. You'll receive a422status code ifnameis omitted.
emailstringRequiredThe email of the author or committer of the commit. You'll receive a422status code ifemailis omitted.
datestring
authorobjectThe author of the file. Default: Thecommitteror the authenticated user if you omitcommitter.
Properties ofauthorName, Type, DescriptionnamestringRequiredThe name of the author or committer of the commit. You'll receive a422status code ifnameis omitted.emailstringRequiredThe email of the author or committer of the commit. You'll receive a422status code ifemailis omitted.datestring | Name, Type, Description | namestringRequiredThe name of the author or committer of the commit. You'll receive a422status code ifnameis omitted. | emailstringRequiredThe email of the author or committer of the commit. You'll receive a422status code ifemailis omitted. | datestring
Name, Type, Description
namestringRequiredThe name of the author or committer of the commit. You'll receive a422status code ifnameis omitted.
emailstringRequiredThe email of the author or committer of the commit. You'll receive a422status code ifemailis omitted.
datestring
[/TABLE]
The commit message.
The new file content, using Base64 encoding.
Required if you are updating a file. The blob SHA of the file being replaced.
The branch name. Default: the repository’s default branch.
The person that committed the file. Default: the authenticated user.

[TABLE]
Name, Type, Description
namestringRequiredThe name of the author or committer of the commit. You'll receive a422status code ifnameis omitted.
emailstringRequiredThe email of the author or committer of the commit. You'll receive a422status code ifemailis omitted.
datestring
[/TABLE]
The name of the author or committer of the commit. You'll receive a422status code ifnameis omitted.
The email of the author or committer of the commit. You'll receive a422status code ifemailis omitted.
The author of the file. Default: Thecommitteror the authenticated user if you omitcommitter.

[TABLE]
Name, Type, Description
namestringRequiredThe name of the author or committer of the commit. You'll receive a422status code ifnameis omitted.
emailstringRequiredThe email of the author or committer of the commit. You'll receive a422status code ifemailis omitted.
datestring
[/TABLE]
The name of the author or committer of the commit. You'll receive a422status code ifnameis omitted.
The email of the author or committer of the commit. You'll receive a422status code ifemailis omitted.

### HTTP response status codes for "Create or update file contents"

[TABLE]
Status code | Description
200 | OK
201 | Created
404 | Resource not found
409 | Conflict
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Created
Resource not found
Conflict
Validation failed, or the endpoint has been spammed.

### Code samples for "Create or update file contents"

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
  https://api.github.com/repos/OWNER/REPO/contents/PATH \
  -d '{"message":"my commit message","committer":{"name":"Monalisa Octocat","email":"octocat@github.com"},"content":"bXkgbmV3IGZpbGUgY29udGVudHM="}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "content": {
    "name": "hello.txt",
    "path": "notes/hello.txt",
    "sha": "95b966ae1c166bd92f8ae7d1c313e738c731dfc3",
    "size": 9,
    "url": "https://api.github.com/repos/octocat/Hello-World/contents/notes/hello.txt",
    "html_url": "https://github.com/octocat/Hello-World/blob/master/notes/hello.txt",
    "git_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs/95b966ae1c166bd92f8ae7d1c313e738c731dfc3",
    "download_url": "https://raw.githubusercontent.com/octocat/HelloWorld/master/notes/hello.txt",
    "type": "file",
    "_links": {
      "self": "https://api.github.com/repos/octocat/Hello-World/contents/notes/hello.txt",
      "git": "https://api.github.com/repos/octocat/Hello-World/git/blobs/95b966ae1c166bd92f8ae7d1c313e738c731dfc3",
      "html": "https://github.com/octocat/Hello-World/blob/master/notes/hello.txt"
    }
  },
  "commit": {
    "sha": "7638417db6d59f3c431d3e1f261cc637155684cd",
    "node_id": "MDY6Q29tbWl0NzYzODQxN2RiNmQ1OWYzYzQzMWQzZTFmMjYxY2M2MzcxNTU2ODRjZA==",
    "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/7638417db6d59f3c431d3e1f261cc637155684cd",
    "html_url": "https://github.com/octocat/Hello-World/git/commit/7638417db6d59f3c431d3e1f261cc637155684cd",
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
      "url": "https://api.github.com/repos/octocat/Hello-World/git/trees/691272480426f78a0138979dd3ce63b77f706feb",
      "sha": "691272480426f78a0138979dd3ce63b77f706feb"
    },
    "parents": [
      {
        "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/1acc419d4d6a9ce985db7be48c6349a0475975b5",
        "html_url": "https://github.com/octocat/Hello-World/git/commit/1acc419d4d6a9ce985db7be48c6349a0475975b5",
        "sha": "1acc419d4d6a9ce985db7be48c6349a0475975b5"
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
}
```

## Delete a file
Deletes a file in a repository.
You can provide an additionalcommitterparameter, which is an object containing information about the committer. Or, you can provide anauthorparameter, which is an object containing information about the author.
Theauthorsection is optional and is filled in with thecommitterinformation if omitted. If thecommitterinformation is omitted, the authenticated user's information is used.
You must provide values for bothnameandemail, whether you choose to useauthororcommitter. Otherwise, you'll receive a422status code.
Note
If you use this endpoint and the "Create or update file contents" endpoint in parallel, the concurrent requests will conflict and you will receive errors. You must use these endpoints serially instead.

### Fine-grained access tokens for "Delete a file"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Contents" repository permissions (write)
- "Contents" repository permissions (write)and"Workflows" repository permissions (write)

### Parameters for "Delete a file"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
pathstringRequiredpath parameter
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
path parameter

[TABLE]
Name, Type, Description
messagestringRequiredThe commit message.
shastringRequiredThe blob SHA of the file being deleted.
branchstringThe branch name. Default: the repository’s default branch
committerobjectobject containing information about the committer.
Properties ofcommitterName, Type, DescriptionnamestringThe name of the author (or committer) of the commitemailstringThe email of the author (or committer) of the commit | Name, Type, Description | namestringThe name of the author (or committer) of the commit | emailstringThe email of the author (or committer) of the commit
Name, Type, Description
namestringThe name of the author (or committer) of the commit
emailstringThe email of the author (or committer) of the commit
authorobjectobject containing information about the author.
Properties ofauthorName, Type, DescriptionnamestringThe name of the author (or committer) of the commitemailstringThe email of the author (or committer) of the commit | Name, Type, Description | namestringThe name of the author (or committer) of the commit | emailstringThe email of the author (or committer) of the commit
Name, Type, Description
namestringThe name of the author (or committer) of the commit
emailstringThe email of the author (or committer) of the commit
[/TABLE]
The commit message.
The blob SHA of the file being deleted.
The branch name. Default: the repository’s default branch
object containing information about the committer.

[TABLE]
Name, Type, Description
namestringThe name of the author (or committer) of the commit
emailstringThe email of the author (or committer) of the commit
[/TABLE]
The name of the author (or committer) of the commit
The email of the author (or committer) of the commit
object containing information about the author.

[TABLE]
Name, Type, Description
namestringThe name of the author (or committer) of the commit
emailstringThe email of the author (or committer) of the commit
[/TABLE]
The name of the author (or committer) of the commit
The email of the author (or committer) of the commit

### HTTP response status codes for "Delete a file"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
409 | Conflict
422 | Validation failed, or the endpoint has been spammed.
503 | Service unavailable
[/TABLE]
OK
Resource not found
Conflict
Validation failed, or the endpoint has been spammed.
Service unavailable

### Code samples for "Delete a file"

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
  https://api.github.com/repos/OWNER/REPO/contents/PATH \
  -d '{"message":"my commit message","committer":{"name":"Monalisa Octocat","email":"octocat@github.com"},"sha":"329688480d39049927147c162b9d2deaf885005f"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "content": null,
  "commit": {
    "sha": "7638417db6d59f3c431d3e1f261cc637155684cd",
    "node_id": "MDY6Q29tbWl0NzYzODQxN2RiNmQ1OWYzYzQzMWQzZTFmMjYxY2M2MzcxNTU2ODRjZA==",
    "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/7638417db6d59f3c431d3e1f261cc637155684cd",
    "html_url": "https://github.com/octocat/Hello-World/git/commit/7638417db6d59f3c431d3e1f261cc637155684cd",
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
      "url": "https://api.github.com/repos/octocat/Hello-World/git/trees/691272480426f78a0138979dd3ce63b77f706feb",
      "sha": "691272480426f78a0138979dd3ce63b77f706feb"
    },
    "parents": [
      {
        "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/1acc419d4d6a9ce985db7be48c6349a0475975b5",
        "html_url": "https://github.com/octocat/Hello-World/git/commit/1acc419d4d6a9ce985db7be48c6349a0475975b5",
        "sha": "1acc419d4d6a9ce985db7be48c6349a0475975b5"
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
}
```

## Get a repository README
Gets the preferred README for a repository.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github.raw+json: Returns the raw file contents. This is the default if you do not specify a media type.
- application/vnd.github.html+json: Returns the README in HTML. Markup languages are rendered to HTML using GitHub's open-sourceMarkup library.

```
application/vnd.github.raw+json
```

```
application/vnd.github.html+json
```

### Fine-grained access tokens for "Get a repository README"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a repository README"

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
refstringThe name of the commit/branch/tag. Default: the repository’s default branch.
[/TABLE]
The name of the commit/branch/tag. Default: the repository’s default branch.

### HTTP response status codes for "Get a repository README"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Not modified
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Get a repository README"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/readme
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "type": "file",
  "encoding": "base64",
  "size": 5362,
  "name": "README.md",
  "path": "README.md",
  "content": "encoded content ...",
  "sha": "3d21ec53a331a6f037a91c368710b99387d012c1",
  "url": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
  "git_url": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
  "html_url": "https://github.com/octokit/octokit.rb/blob/master/README.md",
  "download_url": "https://raw.githubusercontent.com/octokit/octokit.rb/master/README.md",
  "_links": {
    "git": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
    "self": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
    "html": "https://github.com/octokit/octokit.rb/blob/master/README.md"
  }
}
```

## Get a repository README for a directory
Gets the README from a repository directory.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/vnd.github.raw+json: Returns the raw file contents. This is the default if you do not specify a media type.
- application/vnd.github.html+json: Returns the README in HTML. Markup languages are rendered to HTML using GitHub's open-sourceMarkup library.

```
application/vnd.github.raw+json
```

```
application/vnd.github.html+json
```

### Fine-grained access tokens for "Get a repository README for a directory"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a repository README for a directory"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
dirstringRequiredThe alternate path to look for a README file
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The alternate path to look for a README file

[TABLE]
Name, Type, Description
refstringThe name of the commit/branch/tag. Default: the repository’s default branch.
[/TABLE]
The name of the commit/branch/tag. Default: the repository’s default branch.

### HTTP response status codes for "Get a repository README for a directory"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Get a repository README for a directory"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/readme/DIR
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "type": "file",
  "encoding": "base64",
  "size": 5362,
  "name": "README.md",
  "path": "README.md",
  "content": "encoded content ...",
  "sha": "3d21ec53a331a6f037a91c368710b99387d012c1",
  "url": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
  "git_url": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
  "html_url": "https://github.com/octokit/octokit.rb/blob/master/README.md",
  "download_url": "https://raw.githubusercontent.com/octokit/octokit.rb/master/README.md",
  "_links": {
    "git": "https://api.github.com/repos/octokit/octokit.rb/git/blobs/3d21ec53a331a6f037a91c368710b99387d012c1",
    "self": "https://api.github.com/repos/octokit/octokit.rb/contents/README.md",
    "html": "https://github.com/octokit/octokit.rb/blob/master/README.md"
  }
}
```

## Download a repository archive (tar)
Gets a redirect URL to download a tar archive for a repository. If you omit:ref, the repository’s default branch (usuallymain) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use
theLocationheader to make a secondGETrequest.
Note
For private repositories, these links are temporary and expire after five minutes.

### Fine-grained access tokens for "Download a repository archive (tar)"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Download a repository archive (tar)"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
refstringRequired
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Download a repository archive (tar)"

[TABLE]
Status code | Description
302 | Found
[/TABLE]
Found

### Code samples for "Download a repository archive (tar)"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/tarball/REF
```

#### Response

```
Status: 302
```

## Download a repository archive (zip)
Gets a redirect URL to download a zip archive for a repository. If you omit:ref, the repository’s default branch (usuallymain) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use
theLocationheader to make a secondGETrequest.
Note
For private repositories, these links are temporary and expire after five minutes. If the repository is empty, you will receive a 404 when you follow the redirect.

### Fine-grained access tokens for "Download a repository archive (zip)"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Download a repository archive (zip)"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
refstringRequired
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Download a repository archive (zip)"

[TABLE]
Status code | Description
302 | Found
[/TABLE]
Found

### Code samples for "Download a repository archive (zip)"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/zipball/REF
```

#### Response

```
Status: 302
```