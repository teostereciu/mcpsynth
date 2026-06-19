# Getting started with the REST API

*Source: https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api*

---

# Getting started with the REST API
Learn how to use the GitHub REST API.

## Tool navigation

## In this article

## Introduction
This article describes how to use the GitHub REST API with GitHub CLI,curl, or JavaScript. For a quickstart guide, seeQuickstart for GitHub REST API.

## About requests to the REST API
This section describes the elements that make up an API request:
- HTTP method
- Path
- Headers
- Media types
- Authentication
- Parameters
Every request to the REST API includes an HTTP method and a path. Depending on the REST API endpoint, you might also need to specify request headers, authentication information, query parameters, or body parameters.
The REST API reference documentation describes the HTTP method, path, and parameters for every endpoint. It also displays example requests and responses for each endpoint. For more information, see theREST reference documentation.

### HTTP method
The HTTP method of an endpoint defines the type of action it performs on a given resource. Some common HTTP methods areGET,POST,DELETE, andPATCH. The REST API reference documentation provides the HTTP method for every endpoint.
For example, the HTTP method for the"List repository issues" endpointisGET."
Where possible, the GitHub REST API strives to use an appropriate HTTP method for each action.
- GET: Used for retrieving resources.
- POST: Used for creating resources.
- PATCH: Used for updating properties of resources.
- PUT: Used for replacing resources or collections of resources.
- DELETE: Used for deleting resources.

### Path
Each endpoint has a path. The REST API reference documentation gives the path for every endpoint. For example, the path for the"List repository issues" endpointis/repos/{owner}/{repo}/issues.
The curly brackets{}in a path denote path parameters that you need to specify. Path parameters modify the endpoint path and are required in your request. For example, the path parameters for the"List repository issues" endpointare{owner}and{repo}. To use this path in your API request, replace{repo}with the name of the repository where you would like to request a list of issues, and replace{owner}with the name of the account that owns the repository.

### Headers
Headers provide extra information about the request and the desired response. Following are some examples of headers that you can use in your requests to the GitHub REST API. For an example of a request that uses headers, seeMaking a request.

#### Accept
Most GitHub REST API endpoints specify that you should pass anAcceptheader with a value ofapplication/vnd.github+json. The value of theAcceptheader is a media type. For more information about media types, seeMedia types.

#### X-GitHub-Api-Version

```
X-GitHub-Api-Version
```
You should use this header to specify a version of the REST API to use for your request. For more information, seeAPI Versions.

#### User-Agent
All API requests must include a validUser-Agentheader. TheUser-Agentheader identifies the user or application that is making the request.
By default, GitHub CLI sends a validUser-Agentheader. However, GitHub recommends using your GitHub username, or the name of your application, for theUser-Agentheader value. This allows GitHub to contact you if there are problems.
By default,curlsends a validUser-Agentheader. However GitHub recommends using your GitHub username, or the name of your application, for theUser-Agentheader value. This allows GitHub to contact you if there are problems.
If you use the Octokit.js SDK, the SDK will send a validUser-Agentheader for you. However, GitHub recommends using your GitHub username, or the name of your application, for theUser-Agentheader value. This allows GitHub to contact you if there are problems.
The following is an exampleUser-Agentfor an app namedAwesome-Octocat-App:

```
User-Agent: Awesome-Octocat-App
```

```
User-Agent: Awesome-Octocat-App
```
Requests with noUser-Agentheader will be rejected. If you provide an invalidUser-Agentheader, you will receive a403 Forbiddenresponse.

### Media types
You can specify one or more media types by adding them to theAcceptheader of your request. For more information about theAcceptheader, seeAccept.
Media types specify the format of the data you want to consume from the API. Media types are specific to resources, allowing them to change independently and support formats that other resources don't. The documentation for each GitHub REST API endpoint will describe the media types that it supports. For more information, see theGitHub REST API documentation.
The most common media types supported by the GitHub REST API areapplication/vnd.github+jsonandapplication/json.
There are custom media types that you can use with some endpoints. For example, the REST API to managecommitsandpull requestssupport the media typesdiff,patch, andsha. The media typesfull,raw,text, orhtmlare used by some other endpoints.
All custom media types for GitHub look like this:application/vnd.github.PARAM+json, wherePARAMis the name of the media type. For example, to specify therawmedia type, you would useapplication/vnd.github.raw+json.
For an example of a request that uses media types, seeMaking a request.

### Authentication
Many endpoints require authentication or return additional information if you are authenticated. Additionally, you can make more requests per hour when you are authenticated.
To authenticate your request, you will need to provide an authentication token with the required scopes or permissions. There a few different ways to get a token: You can create a personal access token, generate a token with a GitHub App, or use the built-inGITHUB_TOKENin a GitHub Actions workflow. For more information, seeAuthenticating to the REST API.
For an example of a request that uses an authentication token, seeMaking a request.
Note
If you don't want to create a token, you can use GitHub CLI. GitHub CLI will take care of authentication for you, and help keep your account secure. For more information, see theGitHub CLI version of this page.
Warning
Treat your access token the same way you would treat your passwords or other sensitive credentials. For more information, seeKeeping your API credentials secure.
Although some REST API endpoints are accessible without authentication, GitHub CLI requires you to authenticate before you can use theapisubcommand to make an API request. Use theauth loginsubcommand to authenticate to GitHub. For more information, seeMaking a request.
To authenticate your request, you will need to provide an authentication token with the required scopes or permissions. There a few different ways to get a token: You can create a personal access token, generate a token with a GitHub App, or use the built-inGITHUB_TOKENin a GitHub Actions workflow. For more information, seeAuthenticating to the REST API.
For an example of a request that uses an authentication token, seeMaking a request.
Warning
Treat your access token the same way you would treat your passwords or other sensitive credentials. For more information, seeKeeping your API credentials secure.

### Parameters
Many API methods require or allow you to send additional information in parameters in your request. There are a few different types of parameters: Path parameters, body parameters, and query parameters.

#### Path parameters
Path parameters modify the endpoint path. These parameters are required in your request. For more information, seePath.

#### Body parameters
Body parameters allow you to pass additional data to the API. These parameters can be optional or required, depending on the endpoint. For example, a body parameter may allow you to specify an issue title when creating a new issue, or specify certain settings when enabling or disabling a feature. The documentation for each GitHub REST API endpoint will describe the body parameters that it supports. For more information, see theGitHub REST API documentation.
For example, the"Create an issue" endpointrequires that you specify a title for the new issue in your request. It also allows you to optionally specify other information, such as text to put in the issue body, users to assign to the new issue, or labels to apply to the new issue. For an example of a request that uses body parameters, seeMaking a request.
You must authenticate your request to pass body parameters. For more information, seeAuthentication.

#### Query parameters
Query parameters allow you to control what data is returned for a request. These parameters are usually optional. The documentation for each GitHub REST API endpoint will describe any query parameters that it supports. For more information, see theGitHub REST API documentation.
For example, the"List public events" endpointreturns thirty issues by default. You can use theper_pagequery parameter to return two issues instead of 30. You can use thepagequery parameter to fetch only the first page of results. For an example of a request that uses query parameters, seeMaking a request.

## Making a request
This section demonstrates how to make an authenticated request to the GitHub REST API using GitHub CLI.

### 1. Setup
Install GitHub CLI on macOS, Windows, or Linux. For more information, seeInstallationin the GitHub CLI repository.

### 2. Authenticate
1. To authenticate to GitHub, run the following command from your terminal.gh auth loginYou can use the--scopesoption to specify what scopes you want. If you want to authenticate with a token that you created, you can use the--with-tokenoption. For more information, see theGitHub CLIauth logindocumentation.
2. Select where you want to authenticate to:If you access GitHub at GitHub.com, selectGitHub.com.If you access GitHub at a different domain, selectOther, then enter your hostname (for example:octocorp.ghe.com).
3. Follow the rest of the on-screen prompts.GitHub CLI automatically stores your Git credentials for you when you choose HTTPS as your preferred protocol for Git operations and answer "yes" to the prompt asking if you would like to authenticate to Git with your GitHub credentials. This can be useful as it allows you to use Git commands likegit pushandgit pullwithout needing to set up a separate credential manager or use SSH.

```
gh auth login
```
- If you access GitHub at GitHub.com, selectGitHub.com.
- If you access GitHub at a different domain, selectOther, then enter your hostname (for example:octocorp.ghe.com).

### 3. Choose an endpoint for your request
1. Choose an endpoint to make a request to. You can explore GitHub'sREST API documentationto discover endpoints that you can use to interact with GitHub.
2. Identify the HTTP method and path of the endpoint. You will send these with your request. For more information, seeHTTP methodandPath.For example, the"Create an issue" endpointuses the HTTP methodPOSTand the path/repos/{owner}/{repo}/issues.
3. Identify any required path parameters. Required path parameters appear in curly brackets{}in the path of the endpoint. Replace each parameter placeholder with the desired value. For more information, seePath.For example, the"Create an issue" endpointuses the path/repos/{owner}/{repo}/issues, and the path parameters are{owner}and{repo}. To use this path in your API request, replace{repo}with the name of the repository where you would like to create a new issue, and replace{owner}with the name of the account that owns the repository.

### 4. Make a request with GitHub CLI
Use the GitHub CLIapisubcommand to make your API request. For more information, see theGitHub CLIapidocumentation.
In your request, specify the following options and values:
- --methodfollowed by the HTTP method and the path of the endpoint. For more information, seeHTTP methodandPath.
- --header:Accept:Pass the media type in anAcceptheader. To pass multiple media types in anAcceptheader, separate the media types with a comma:Accept: application/vnd.github+json,application/vnd.github.diff. For more information, seeAcceptandMedia types.X-GitHub-Api-Version:Pass the API version in aX-GitHub-Api-Versionheader. For more information, seeX-GitHub-Api-Version.
- -for-Ffollowed by any body parameters or query parameters inkey=valueformat. Use the-Foption to pass a parameter that is a number, Boolean, or null. Use the-foption to pass string parameters.Some endpoints use query parameters that are arrays. To send an array in the query string, use the query parameter once per array item, and append[]after the query parameter name. For example, to provide an array of two repository IDs, use-f repository_ids[]=REPOSITORY_A_ID -f repository_ids[]=REPOSITORY_B_ID.If you do not need to specify any body parameters or query parameters in your request, omit this option. For more information, seeBody parametersandQuery parameters. For examples, seeExample request using body parametersandExample request using query parameters.
- Accept:Pass the media type in anAcceptheader. To pass multiple media types in anAcceptheader, separate the media types with a comma:Accept: application/vnd.github+json,application/vnd.github.diff. For more information, seeAcceptandMedia types.
- X-GitHub-Api-Version:Pass the API version in aX-GitHub-Api-Versionheader. For more information, seeX-GitHub-Api-Version.

```
X-GitHub-Api-Version
```

```
X-GitHub-Api-Version
```

#### Example request
The following example request uses the"Get Octocat" endpointto return the octocat as ASCII art.

```
gh api --method GET /octocat \
--header 'Accept: application/vnd.github+json' \
--header "X-GitHub-Api-Version: 2022-11-28"
```

```
gh api --method GET /octocat \
--header 'Accept: application/vnd.github+json' \
--header "X-GitHub-Api-Version: 2022-11-28"
```

#### Example request using query parameters
The"List public events" endpointreturns thirty issues by default. The following example uses theper_pagequery parameter to return two issues instead of 30, and thepagequery parameter to fetch only the first page of results.

```
gh api --method GET /events -F per_page=2 -F page=1
--header 'Accept: application/vnd.github+json' \
```

```
gh api --method GET /events -F per_page=2 -F page=1
--header 'Accept: application/vnd.github+json' \
```

#### Example request using body parameters
The following example uses the"Create an issue" endpointto create a new issue in the octocat/Spoon-Knife repository. In the response, find thehtml_urlof your issue, and navigate to your issue in the browser.

```
gh api --method POST /repos/octocat/Spoon-Knife/issues \
--header "Accept: application/vnd.github+json" \
--header "X-GitHub-Api-Version: 2022-11-28" \
-f title='Created with the REST API' \
-f body='This is a test issue created by the REST API' \
```

```
gh api --method POST /repos/octocat/Spoon-Knife/issues \
--header "Accept: application/vnd.github+json" \
--header "X-GitHub-Api-Version: 2022-11-28" \
-f title='Created with the REST API' \
-f body='This is a test issue created by the REST API' \
```
This section demonstrates how to make an authenticated request to the GitHub REST API usingcurl.

### 1. Setup
You must havecurlinstalled on your machine. To check ifcurlis already installed, runcurl --versionon the command line.
- If the output provides information about the version ofcurl, that meanscurlis installed.
- If you get a message similar tocommand not found: curl, that meanscurlis not installed. Download and installcurl. For more information, seethe curl download page.

### 2. Choose an endpoint for your request
1. Choose an endpoint to make a request to. You can explore GitHub'sREST API documentationto discover endpoints that you can use to interact with GitHub.
2. Identify the HTTP method and path of the endpoint. You will send these with your request. For more information, seeHTTP methodandPath.For example, the"Create an issue" endpointuses the HTTP methodPOSTand the path/repos/{owner}/{repo}/issues.
3. Identify any required path parameters. Required path parameters appear in curly brackets{}in the path of the endpoint. Replace each parameter placeholder with the desired value. For more information, seePath.For example, the"Create an issue" endpointuses the path/repos/{owner}/{repo}/issues, and the path parameters are{owner}and{repo}. To use this path in your API request, replace{repo}with the name of the repository where you would like to create a new issue, and replace{owner}with the name of the account that owns the repository.

### 3. Create authentication credentials
Create an access token to authenticate your request. You can save your token and use it for multiple requests. Give the token any scopes or permissions that are required to access the endpoint. You will send this token in anAuthorizationheader with your request. For more information, seeAuthentication.

### 4. Make acurlrequest
Use thecurlcommand to make your request. For more information, seethe curl documentation.
Specify the following options and values in your request:
- --requestor-Xfollowed by the HTTP method as the value. For more information, seeHTTP method.
- --urlfollowed by the full path as the value. The full path is a URL that includes the base URL for the GitHub REST API (https://api.github.com) and the path of the endpoint, like this:https://api.github.com/PATH. ReplacePATHwith the path of the endpoint. For more information, seePath.To use query parameters, add a?to the end of the path, then append your query parameter name and value in the formparameter_name=value. Separate multiple query parameters with&. If you need to send an array in the query string, use the query parameter once per array item, and append[]after the query parameter name. For example, to provide an array of two repository IDs, use?repository_ids[]=REPOSITORY_A_ID&repository_ids[]=REPOSITORY_B_ID. For more information, seeQuery parameters. For an example, seeExample request using query parameters.
- --headeror-H:Accept:Pass the media type in anAcceptheader. To pass multiple media types in anAcceptheader, separate the media types with a comma, for example:Accept: application/vnd.github+json,application/vnd.github.diff. For more information, seeAcceptandMedia types.X-GitHub-Api-Version:Pass the API version in aX-GitHub-Api-Versionheader. For more information, seeX-GitHub-Api-Version.Authorization:Pass your authentication token in anAuthorizationheader. Note that in most cases you can useAuthorization: BearerorAuthorization: tokento pass a token. However, if you are passing a JSON web token (JWT), you must useAuthorization: Bearer. For more information, seeAuthentication. For an example of a request that uses anAuthorizationheader, seeExample request using body parameters.
- --dataor-dfollowed by any body parameters within a JSON object. If you do not need to specify any body parameters in your request, omit this option. For more information, seeBody parameters. For an example, seeExample request using body parameters.
- Accept:Pass the media type in anAcceptheader. To pass multiple media types in anAcceptheader, separate the media types with a comma, for example:Accept: application/vnd.github+json,application/vnd.github.diff. For more information, seeAcceptandMedia types.
- X-GitHub-Api-Version:Pass the API version in aX-GitHub-Api-Versionheader. For more information, seeX-GitHub-Api-Version.
- Authorization:Pass your authentication token in anAuthorizationheader. Note that in most cases you can useAuthorization: BearerorAuthorization: tokento pass a token. However, if you are passing a JSON web token (JWT), you must useAuthorization: Bearer. For more information, seeAuthentication. For an example of a request that uses anAuthorizationheader, seeExample request using body parameters.

```
X-GitHub-Api-Version
```

```
X-GitHub-Api-Version
```

```
Authorization
```

#### Example request
The following example request uses the"Get Octocat" endpointto return the octocat as ASCII art.

```
curl --request GET \
--url "https://api.github.com/octocat" \
--header "Accept: application/vnd.github+json" \
--header "X-GitHub-Api-Version: 2022-11-28"
```

```
curl --request GET \
--url "https://api.github.com/octocat" \
--header "Accept: application/vnd.github+json" \
--header "X-GitHub-Api-Version: 2022-11-28"
```

#### Example request using query parameters
The"List public events" endpointreturns thirty issues by default. The following example uses theper_pagequery parameter to return two issues instead of 30, and thepagequery parameter to fetch only the first page of results.

```
curl --request GET \
--url "https://api.github.com/events?per_page=2&page=1" \
--header "Accept: application/vnd.github+json" \
--header "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/events
```

```
curl --request GET \
--url "https://api.github.com/events?per_page=2&page=1" \
--header "Accept: application/vnd.github+json" \
--header "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/events
```

#### Example request using body parameters
The following example uses theCreate an issueendpoint to create a new issue in the octocat/Spoon-Knife repository. ReplaceYOUR-TOKENwith the authentication token you created in a previous step.
Note
If you are using a fine-grained personal access token, you must replaceoctocat/Spoon-Knifewith a repository that you own or that is owned by an organization that you are a member of. Your token must have access to that repository and have read and write permissions for repository issues. For more information, seeManaging your personal access tokens.

```
curl \
--request POST \
--url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
--header "Accept: application/vnd.github+json" \
--header "X-GitHub-Api-Version: 2022-11-28" \
--header "Authorization: Bearer YOUR-TOKEN" \
--data '{
  "title": "Created with the REST API",
  "body": "This is a test issue created by the REST API"
}'
```

```
curl \
--request POST \
--url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
--header "Accept: application/vnd.github+json" \
--header "X-GitHub-Api-Version: 2022-11-28" \
--header "Authorization: Bearer YOUR-TOKEN" \
--data '{
  "title": "Created with the REST API",
  "body": "This is a test issue created by the REST API"
}'
```
This section demonstrates how to make a request to the GitHub REST API using JavaScript andOctokit.js. For a more detailed guide, seeScripting with the REST API and JavaScript.

### 1. Setup
You must installoctokitto use the Octokit.js library shown in the following examples.
- Installoctokit. For example,npm install octokit. For other ways to install or loadoctokit, seethe Octokit.js README.

### 2. Choose an endpoint for your request
1. Choose an endpoint to make a request to. You can explore GitHub'sREST API documentationto discover endpoints that you can use to interact with GitHub.
2. Identify the HTTP method and path of the endpoint. You will send these with your request. For more information, seeHTTP methodandPath.For example, the"Create an issue" endpointuses the HTTP methodPOSTand the path/repos/{owner}/{repo}/issues.
3. Identify any required path parameters. Required path parameters appear in curly brackets{}in the path of the endpoint. Replace each parameter placeholder with the desired value. For more information, seePath.For example, the"Create an issue" endpointuses the path/repos/{owner}/{repo}/issues, and the path parameters are{owner}and{repo}. To use this path in your API request, replace{repo}with the name of the repository where you would like to create a new issue, and replace{owner}with the name of the account that owns the repository.

### 3. Create an access token
Create an access token to authenticate your request. You can save your token and use it for multiple requests. Give the token any scopes or permissions that are required to access the endpoint. You will send this token in anAuthorizationheader with your request. For more information, seeAuthentication.

### 4. Make a request with Octokit.js
1. Importoctokitin your script. For example,import { Octokit } from "octokit";. For other ways to importoctokit, seethe Octokit.js README.
2. Create an instance ofOctokitwith your token. ReplaceYOUR-TOKENwith your token.constoctokit =newOctokit({auth:'YOUR-TOKEN'});
3. Useoctokit.requestto execute your request.Send the HTTP method and path as the first argument to therequestmethod. For more information, seeHTTP methodandPath.Specify all path, query, and body parameters in an object as the second argument to therequestmethod. For more information, seeParameters.In the following example request, the HTTP method isPOST, the path is/repos/{owner}/{repo}/issues, the path parameters areowner: "octocat"andrepo: "Spoon-Knife", and the body parameters aretitle: "Created with the REST API"andbody: "This is a test issue created by the REST API".NoteIf you are using a fine-grained personal access token, you must replaceoctocat/Spoon-Knifewith a repository that you own or that is owned by an organization that you are a member of. Your token must have access to that repository and have read and write permissions for repository issues. For more information, seeManaging your personal access tokens.awaitoctokit.request("POST /repos/{owner}/{repo}/issues", {owner:"octocat",repo:"Spoon-Knife",title:"Created with the REST API",body:"This is a test issue created by the REST API",
});Therequestmethod automatically passes theAccept: application/vnd.github+jsonheader. To pass additional headers or a differentAcceptheader, add aheadersproperty to the object that is passed as a second argument. The value of theheadersproperty is an object with the header names as keys and header values as values.For example, the following code will send acontent-typeheader with a value oftext/plainand aX-GitHub-Api-Versionheader with a value of2026-03-10.awaitoctokit.request("GET /octocat", {headers: {"content-type":"text/plain","X-GitHub-Api-Version":"2026-03-10",
  },
});

```
constoctokit =newOctokit({auth:'YOUR-TOKEN'});
```

```
constoctokit =newOctokit({auth:'YOUR-TOKEN'});
```
- Send the HTTP method and path as the first argument to therequestmethod. For more information, seeHTTP methodandPath.
- Specify all path, query, and body parameters in an object as the second argument to therequestmethod. For more information, seeParameters.

```
awaitoctokit.request("POST /repos/{owner}/{repo}/issues", {owner:"octocat",repo:"Spoon-Knife",title:"Created with the REST API",body:"This is a test issue created by the REST API",
});
```

```
awaitoctokit.request("POST /repos/{owner}/{repo}/issues", {owner:"octocat",repo:"Spoon-Knife",title:"Created with the REST API",body:"This is a test issue created by the REST API",
});
```

```
awaitoctokit.request("GET /octocat", {headers: {"content-type":"text/plain","X-GitHub-Api-Version":"2026-03-10",
  },
});
```

```
awaitoctokit.request("GET /octocat", {headers: {"content-type":"text/plain","X-GitHub-Api-Version":"2026-03-10",
  },
});
```

## Using the response
After you make a request, the API will return the response status code, response headers, and potentially a response body.

### About the response code and headers
Every request will return an HTTP status code that indicates the success of the response. For more information about response codes, seethe MDN HTTP response status code documentation.
Additionally, the response will include headers that give more details about the response. Headers that start withX-orx-are custom to GitHub. For example, thex-ratelimit-remainingandx-ratelimit-resetheaders tell you how many requests you can make in a time period.
To view the status code and headers, use the--includeor--ioption when you send your request.
For example, this request gets a list of issues in the octocat/Spoon-Knife repository:

```
gh api \
--header 'Accept: application/vnd.github+json' \
--method GET /repos/octocat/Spoon-Knife/issues \
-F per_page=2 --include
```

```
gh api \
--header 'Accept: application/vnd.github+json' \
--method GET /repos/octocat/Spoon-Knife/issues \
-F per_page=2 --include
```
And it returns a response code and headers that look something like this:

```
HTTP/2.0 200 OK
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: ETag, Link, Location, Retry-After, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, X-GitHub-SSO, X-GitHub-Request-Id, Deprecation, Sunset
Cache-Control: private, max-age=60, s-maxage=60
Content-Security-Policy: default-src 'none'
Content-Type: application/json; charset=utf-8
Date: Thu, 04 Aug 2022 19:56:41 GMT
Etag: W/"a63dfbcfdb73621e9d2e89551edcf9856731ced534bd7f1e114a5da1f5f73418"
Link: <https://api.github.com/repositories/1300192/issues?per_page=1&page=2>; rel="next", <https://api.github.com/repositories/1300192/issues?per_page=1&page=14817>; rel="last"
Referrer-Policy: origin-when-cross-origin, strict-origin-when-cross-origin
Server: GitHub.com
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
Vary: Accept, Authorization, Cookie, Accept-Encoding, Accept, X-Requested-With
X-Accepted-Oauth-Scopes: repo
X-Content-Type-Options: nosniff
X-Frame-Options: deny
X-Github-Api-Version-Selected: 2022-08-09
X-Github-Media-Type: github.v3; format=json
X-Github-Request-Id: 1C73:26D4:E2E500:1EF78F4:62EC2479
X-Oauth-Client-Id: 178c6fc778ccc68e1d6a
X-Oauth-Scopes: gist, read:org, repo, workflow
X-Ratelimit-Limit: 15000
X-Ratelimit-Remaining: 14996
X-Ratelimit-Reset: 1659645499
X-Ratelimit-Resource: core
X-Ratelimit-Used: 4
X-Xss-Protection: 0
```

```
HTTP/2.0 200 OK
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: ETag, Link, Location, Retry-After, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, X-GitHub-SSO, X-GitHub-Request-Id, Deprecation, Sunset
Cache-Control: private, max-age=60, s-maxage=60
Content-Security-Policy: default-src 'none'
Content-Type: application/json; charset=utf-8
Date: Thu, 04 Aug 2022 19:56:41 GMT
Etag: W/"a63dfbcfdb73621e9d2e89551edcf9856731ced534bd7f1e114a5da1f5f73418"
Link: <https://api.github.com/repositories/1300192/issues?per_page=1&page=2>; rel="next", <https://api.github.com/repositories/1300192/issues?per_page=1&page=14817>; rel="last"
Referrer-Policy: origin-when-cross-origin, strict-origin-when-cross-origin
Server: GitHub.com
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
Vary: Accept, Authorization, Cookie, Accept-Encoding, Accept, X-Requested-With
X-Accepted-Oauth-Scopes: repo
X-Content-Type-Options: nosniff
X-Frame-Options: deny
X-Github-Api-Version-Selected: 2022-08-09
X-Github-Media-Type: github.v3; format=json
X-Github-Request-Id: 1C73:26D4:E2E500:1EF78F4:62EC2479
X-Oauth-Client-Id: 178c6fc778ccc68e1d6a
X-Oauth-Scopes: gist, read:org, repo, workflow
X-Ratelimit-Limit: 15000
X-Ratelimit-Remaining: 14996
X-Ratelimit-Reset: 1659645499
X-Ratelimit-Resource: core
X-Ratelimit-Used: 4
X-Xss-Protection: 0
```
In this example, the response code is200, which indicates a successful request.
When you make a request with Octokit.js, therequestmethod returns a promise. If the request was successful, the promise resolves to an object that includes the HTTP status code of the response (status) and the response headers (headers). If an error occurs, the promise resolves to an object that includes the HTTP status code of the response (status) and the response headers (response.headers).
You can use atry/catchblock to catch an error if it occurs. For example, if the request in the following script is successful, the script will log the status code and the value of thex-ratelimit-remainingheader. If the request was not successful, the script will log the status code, the value of thex-ratelimit-remainingheader, and the error message.
In the following example, replaceREPO-OWNERwith the name of the account that owns the repository, andREPO-NAMEwith the name of the repository.

```
try{constresult =awaitoctokit.request("GET /repos/{owner}/{repo}/issues", {owner:"REPO-OWNER",repo:"REPO-NAME",per_page:2,
  });console.log(`Success! Status:${result.status}. Rate limit remaining:${result.headers["x-ratelimit-remaining"]}`)

}catch(error) {console.log(`Error! Status:${error.status}. Rate limit remaining:${error.headers["x-ratelimit-remaining"]}. Message:${error.response.data.message}`)
}
```

```
try{constresult =awaitoctokit.request("GET /repos/{owner}/{repo}/issues", {owner:"REPO-OWNER",repo:"REPO-NAME",per_page:2,
  });console.log(`Success! Status:${result.status}. Rate limit remaining:${result.headers["x-ratelimit-remaining"]}`)

}catch(error) {console.log(`Error! Status:${error.status}. Rate limit remaining:${error.headers["x-ratelimit-remaining"]}. Message:${error.response.data.message}`)
}
```
To view the status code and headers, use the--includeor--ioption when you send your request.
For example, this request gets a list of issues in the octocat/Spoon-Knife repository:

```
curl --request GET \
--url "https://api.github.com/repos/octocat/Spoon-Knife/issues?per_page=2" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer YOUR-TOKEN" \
--include
```

```
curl --request GET \
--url "https://api.github.com/repos/octocat/Spoon-Knife/issues?per_page=2" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer YOUR-TOKEN" \
--include
```
And it returns a response code and headers that look something like this:

```
HTTP/2 200
server: GitHub.com
date: Thu, 04 Aug 2022 20:07:51 GMT
content-type: application/json; charset=utf-8
cache-control: public, max-age=60, s-maxage=60
vary: Accept, Accept-Encoding, Accept, X-Requested-With
etag: W/"7fceb7e8c958d3ec4d02524b042578dcc7b282192e6c939070f4a70390962e18"
x-github-media-type: github.v3; format=json
link: <https://api.github.com/repositories/1300192/issues?per_page=2&sort=updated&direction=asc&page=2>; rel="next", <https://api.github.com/repositories/1300192/issues?per_page=2&sort=updated&direction=asc&page=7409>; rel="last"
access-control-expose-headers: ETag, Link, Location, Retry-After, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, X-GitHub-SSO, X-GitHub-Request-Id, Deprecation, Sunset
access-control-allow-origin: *
strict-transport-security: max-age=31536000; includeSubdomains; preload
x-frame-options: deny
x-content-type-options: nosniff
x-xss-protection: 0
referrer-policy: origin-when-cross-origin, strict-origin-when-cross-origin
content-security-policy: default-src 'none'
x-ratelimit-limit: 15000
x-ratelimit-remaining: 14996
x-ratelimit-reset: 1659645535
x-ratelimit-resource: core
x-ratelimit-used: 4
accept-ranges: bytes
content-length: 4936
x-github-request-id: 14E0:4BC6:F1B8BA:208E317:62EC2715
```

```
HTTP/2 200
server: GitHub.com
date: Thu, 04 Aug 2022 20:07:51 GMT
content-type: application/json; charset=utf-8
cache-control: public, max-age=60, s-maxage=60
vary: Accept, Accept-Encoding, Accept, X-Requested-With
etag: W/"7fceb7e8c958d3ec4d02524b042578dcc7b282192e6c939070f4a70390962e18"
x-github-media-type: github.v3; format=json
link: <https://api.github.com/repositories/1300192/issues?per_page=2&sort=updated&direction=asc&page=2>; rel="next", <https://api.github.com/repositories/1300192/issues?per_page=2&sort=updated&direction=asc&page=7409>; rel="last"
access-control-expose-headers: ETag, Link, Location, Retry-After, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, X-GitHub-SSO, X-GitHub-Request-Id, Deprecation, Sunset
access-control-allow-origin: *
strict-transport-security: max-age=31536000; includeSubdomains; preload
x-frame-options: deny
x-content-type-options: nosniff
x-xss-protection: 0
referrer-policy: origin-when-cross-origin, strict-origin-when-cross-origin
content-security-policy: default-src 'none'
x-ratelimit-limit: 15000
x-ratelimit-remaining: 14996
x-ratelimit-reset: 1659645535
x-ratelimit-resource: core
x-ratelimit-used: 4
accept-ranges: bytes
content-length: 4936
x-github-request-id: 14E0:4BC6:F1B8BA:208E317:62EC2715
```
In this example, the response code is200, which indicates a successful request.

### About the response body
Many endpoints will return a response body. Unless otherwise specified, the response body is in JSON format. Blank fields are included asnullinstead of being omitted. All timestamps return in UTC time, ISO 8601 format:YYYY-MM-DDTHH:MM:SSZ.
Unlike the GraphQL API where you specify what information you want, the REST API typically returns more information than you need. If desired, you can parse the response to pull out specific pieces of information.
For example, you can use>to redirect the response to a file. In the following example, replaceREPO-OWNERwith the name of the account that owns the repository, andREPO-NAMEwith the name of the repository.

```
gh api \
--header 'Accept: application/vnd.github+json' \
--method GET /repos/REPO-OWNER/REPO-NAME/issues \
-F per_page=2 > data.json
```

```
gh api \
--header 'Accept: application/vnd.github+json' \
--method GET /repos/REPO-OWNER/REPO-NAME/issues \
-F per_page=2 > data.json
```
Then you can use jq to get the title and author ID of each issue:

```
jq '.[] | {title: .title, authorID: .user.id}' data.json
```

```
jq '.[] | {title: .title, authorID: .user.id}' data.json
```
The previous two commands return something like:

```
{"title":"Update index.html","authorID":10701255}{"title":"Edit index file","authorID":53709285}
```

```
{"title":"Update index.html","authorID":10701255}{"title":"Edit index file","authorID":53709285}
```
For more information about jq, seethe jq documentation.
For example, you can get the title and author ID of each issue. In the following example, replaceREPO-OWNERwith the name of the account that owns the repository, andREPO-NAMEwith the name of the repository.

```
try{constresult =awaitoctokit.request("GET /repos/{owner}/{repo}/issues", {owner:"REPO-OWNER",repo:"REPO-NAME",per_page:2,
  });consttitleAndAuthor = result.data.map(issue=>{title: issue.title,authorID: issue.user.id})console.log(titleAndAuthor)

}catch(error) {console.log(`Error! Status:${error.status}. Message:${error.response.data.message}`)
}
```

```
try{constresult =awaitoctokit.request("GET /repos/{owner}/{repo}/issues", {owner:"REPO-OWNER",repo:"REPO-NAME",per_page:2,
  });consttitleAndAuthor = result.data.map(issue=>{title: issue.title,authorID: issue.user.id})console.log(titleAndAuthor)

}catch(error) {console.log(`Error! Status:${error.status}. Message:${error.response.data.message}`)
}
```
For example, you can use>to redirect the response to a file. In the following example, replaceREPO-OWNERwith the name of the account that owns the repository, andREPO-NAMEwith the name of the repository.

```
curl --request GET \
--url "https://api.github.com/repos/REPO-OWNER/REPO-NAME/issues?per_page=2" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer YOUR-TOKEN" > data.json
```

```
curl --request GET \
--url "https://api.github.com/repos/REPO-OWNER/REPO-NAME/issues?per_page=2" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer YOUR-TOKEN" > data.json
```
Then you can use jq to get the title and author ID of each issue:

```
jq '.[] | {title: .title, authorID: .user.id}' data.json
```

```
jq '.[] | {title: .title, authorID: .user.id}' data.json
```
The previous two commands return something like:

```
{"title":"Update index.html","authorID":10701255}{"title":"Edit index file","authorID":53709285}
```

```
{"title":"Update index.html","authorID":10701255}{"title":"Edit index file","authorID":53709285}
```
For more information about jq, seethe jq documentation.

#### Detailed versus summary representations
A response can include all attributes for a resource or only a subset of attributes, depending on whether you fetch an individual resource or a list of resources.
- When you fetch anindividual resource, like a specific repository, the response will typically include all attributes for that resource. This is the "detailed" representation of the resource.
- When you fetch alist of resources, like a list of multiple repositories, the response will only include a subset of the attributes for each resource. This is the "summary" representation of the resource.
Note that authorization sometimes influences the amount of detail included in a representation.
The reason for this is because some attributes are computationally expensive for the API to provide, so GitHub excludes those attributes from the summary representation. To obtain those attributes, you can fetch the detailed representation.
The documentation provides an example response for each API method. The example response illustrates all attributes that are returned by that method.

#### Hypermedia
All resources may have one or more*_urlproperties linking to other resources. These are meant to provide explicit URLs so that proper API clients don't need to construct URLs on their own. It is highly recommended that API clients use these. Doing so will make future upgrades of the API easier for developers. All URLs are expected to be properRFC 6570URI templates.
You can then expand these templates using something like theuri_templategem:

```
>>tmpl =URITemplate.new('/notifications{?since,all,participating}')>>tmpl.expand
=>"/notifications">>tmpl.expandall:1=>"/notifications?all=1">>tmpl.expandall:1,participating:1=>"/notifications?all=1&participating=1"
```

```
>>tmpl =URITemplate.new('/notifications{?since,all,participating}')>>tmpl.expand
=>"/notifications">>tmpl.expandall:1=>"/notifications?all=1">>tmpl.expandall:1,participating:1=>"/notifications?all=1&participating=1"
```

## Next steps
This article demonstrated how to list and create issues in a repository. For more practice, try to comment on an issue, edit the title of an issue, or close an issue. For more information, see the"Create an issue comment" endpointand the"Update an issue" endpoint.
For more information about other endpoints that you can use, see theREST reference documentation.