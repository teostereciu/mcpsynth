# Scripting with the REST API and JavaScript

*Source: https://docs.github.com/en/rest/guides/scripting-with-the-rest-api-and-javascript*

---

# Scripting with the REST API and JavaScript
Write a script using the Octokit.js SDK to interact with the REST API.

## In this article

## About Octokit.js
If you want to write a script using JavaScript to interact with GitHub's REST API, GitHub recommends that you use the Octokit.js SDK. Octokit.js is maintained by GitHub. The SDK implements best practices and makes it easier for you to interact with the REST API via JavaScript. Octokit.js works with all modern browsers, Node.js, and Deno. For more information about Octokit.js, seethe Octokit.js README.

## Prerequisites
This guide assumes that you are familiar with JavaScript and the GitHub REST API. For more information about the REST API, seeGetting started with the REST API.
You must install and importoctokitin order to use the Octokit.js library. This guide uses import statements in accordance with ES6. For more information about different installation and import methods, seethe Octokit.js README's Usage section.

## Instantiating and authenticating
Warning
Treat your authentication credentials like a password.
To keep your credentials secure, you can store your credentials as a secret and run your script through GitHub Actions. For more information, seeUsing secrets in GitHub Actions.
You can also store your credentials as a Codespaces secret and run your script in Codespaces. For more information, seeManaging your account-specific secrets for GitHub Codespaces.
If these options are not possible, consider using another CLI service to store your credentials securely.

### Authenticating with a personal access token
If you want to use the GitHub REST API for personal use, you can create a personal access token. For more information about creating a personal access token, seeManaging your personal access tokens.
First, importOctokitfromoctokit. Then, pass your personal access token when you create an instance ofOctokit. In the following example, replaceYOUR-TOKENwith a reference to your personal access token.

```
import{Octokit}from"octokit";constoctokit =newOctokit({auth:'YOUR-TOKEN',
});
```

```
import{Octokit}from"octokit";constoctokit =newOctokit({auth:'YOUR-TOKEN',
});
```

### Authenticating with a GitHub App
If you want to use the API on behalf of an organization or another user, GitHub recommends that you use a GitHub App. If an endpoint is available to GitHub Apps, the REST reference documentation for that endpoint will indicate what type of GitHub App token is required. For more information, seeRegistering a GitHub AppandAbout authentication with a GitHub App.
Instead of importingOctokitfromoctokit, importApp. In the following example, replaceAPP_IDwith a reference to your app's ID. ReplacePRIVATE_KEYwith a reference to your app's private key. ReplaceINSTALLATION_IDwith the ID of the installation of your app that you want to authenticate on behalf of. You can find your app's ID and generate a private key on the settings page_number for your app. For more information, seeManaging private keys for GitHub Apps. You can get an installation ID with theGET /users/{username}/installation,GET /repos/{owner}/{repo}/installation, orGET /orgs/{org}/installationendpoints. For more information, seeREST API endpoints for GitHub Apps.

```
import{App}from"octokit";constapp =newApp({appId:APP_ID,privateKey:PRIVATE_KEY,
});constoctokit =awaitapp.getInstallationOctokit(INSTALLATION_ID);
```

```
import{App}from"octokit";constapp =newApp({appId:APP_ID,privateKey:PRIVATE_KEY,
});constoctokit =awaitapp.getInstallationOctokit(INSTALLATION_ID);
```

### Authenticating in GitHub Actions
If you want to use the API in a GitHub Actions workflow, GitHub recommends that you authenticate with the built-inGITHUB_TOKENinstead of creating a token. You can grant permissions to theGITHUB_TOKENwith thepermissionskey. For more information aboutGITHUB_TOKEN, seeGITHUB_TOKEN.
If your workflow needs to access resources outside of the workflow's repository, then you will not be able to useGITHUB_TOKEN. In that case, store your credentials as a secret and replaceGITHUB_TOKENin the examples below with the name of your secret. For more information about secrets, seeUsing secrets in GitHub Actions.
If you use therunkeyword to execute your JavaScript script in your GitHub Actions workflows, you can store the value ofGITHUB_TOKENas an environment variable. Your script can access the environment variable asprocess.env.VARIABLE_NAME.
For example, this workflow step storesGITHUB_TOKENin an environment variable calledTOKEN:

```
-name:Runscriptenv:TOKEN:${{secrets.GITHUB_TOKEN}}run:|
    node .github/actions-scripts/use-the-api.mjs
```

```
-name:Runscriptenv:TOKEN:${{secrets.GITHUB_TOKEN}}run:|
    node .github/actions-scripts/use-the-api.mjs
```
The script that the workflow runs usesprocess.env.TOKENto authenticate:

```
import{Octokit}from"octokit";constoctokit =newOctokit({auth: process.env.TOKEN,
});
```

```
import{Octokit}from"octokit";constoctokit =newOctokit({auth: process.env.TOKEN,
});
```

### Instantiating without authentication
You can use the REST API without authentication, although you will have a lower rate limit and will not be able to use some endpoints. To create an instance ofOctokitwithout authenticating, do not pass theauthargument.

```
import{Octokit}from"octokit";constoctokit =newOctokit({ });
```

```
import{Octokit}from"octokit";constoctokit =newOctokit({ });
```

## Making requests
Octokit supports multiple ways of making requests. You can use therequestmethod to make requests if you know the HTTP verb and path for the endpoint. You can use therestmethod if you want to take advantage of autocompletion in your IDE and typing. For paginated endpoints, you can use thepaginatemethod to request multiple pages of data.

### Using therequestmethod to make requests
To use therequestmethod to make requests, pass the HTTP method and path as the first argument. Pass any body, query, or path parameters in an object as the second argument. For example, to make aGETrequest to/repos/{owner}/{repo}/issuesand pass theowner,repo, andper_pageparameters:

```
awaitoctokit.request("GET /repos/{owner}/{repo}/issues", {owner:"github",repo:"docs",page_limit:2});
```

```
awaitoctokit.request("GET /repos/{owner}/{repo}/issues", {owner:"github",repo:"docs",page_limit:2});
```
Therequestmethod automatically passes theAccept: application/vnd.github+jsonheader. To pass additional headers or a differentAcceptheader, add aheadersproperty to the object that is passed as a second argument. The value of theheadersproperty is an object with the header names as keys and header values as values. For example, to send acontent-typeheader with a value oftext/plainand ax-github-api-versionheader with a value of2026-03-10:

```
awaitoctokit.request("POST /markdown/raw", {text:"Hello **world**",headers: {"content-type":"text/plain","x-github-api-version":"2026-03-10",
  },
});
```

```
awaitoctokit.request("POST /markdown/raw", {text:"Hello **world**",headers: {"content-type":"text/plain","x-github-api-version":"2026-03-10",
  },
});
```

### Usingrestendpoint methods to make requests
Every REST API endpoint has an associatedrestendpoint method in Octokit. These methods generally autocomplete in your IDE for convenience. You can pass any parameters as an object to the method.

```
awaitoctokit.rest.issues.listForRepo({owner:"github",repo:"docs",page_limit:2});
```

```
awaitoctokit.rest.issues.listForRepo({owner:"github",repo:"docs",page_limit:2});
```
Additionally, if you are using a typed language such as TypeScript, you can import types to use with these methods. For more information, seethe TypeScript section in the plugin-rest-endpoint-methods.js README.

### Making paginated requests
If the endpoint is paginated and you want to fetch more than one page_number of results, you can use thepaginatemethod.paginatewill fetch the next page_number of results until it reaches the last page_number and then return all of the results as a single array. A few endpoints return paginated results as array in an object, as opposed to returning the paginated results as an array.paginatealways returns an array of items even if the raw result was an object.
For example, the following example gets all of the issues from thegithub/docsrepository. Although it requests 100 issues at a time, the function won't return until the last page_number of data is reached.

```
constissueData =awaitoctokit.paginate("GET /repos/{owner}/{repo}/issues", {owner:"github",repo:"docs",page_limit:100,headers: {"x-github-api-version":"2026-03-10",
  },
});
```

```
constissueData =awaitoctokit.paginate("GET /repos/{owner}/{repo}/issues", {owner:"github",repo:"docs",page_limit:100,headers: {"x-github-api-version":"2026-03-10",
  },
});
```
Thepaginatemethod accepts an optional map function, which you can use to collect only the data that you want from the response. This reduces memory usage by your script. The map function can take a second argument,done, which you can call to end the pagination before the last page_number is reached. This lets you fetch a subset of pages. For example, the following example continues to fetch results until an issue that includes "test" in the title is returned. For the pages of data that were returned, only the issue title and author are stored.

```
constissueData =awaitoctokit.paginate("GET /repos/{owner}/{repo}/issues", {owner:"github",repo:"docs",page_limit:100,headers: {"x-github-api-version":"2026-03-10",
  },
},(response, done) =>response.data.map((issue) =>{if(issue.title.includes("test")) {done()
    }return({title: issue.title,author: issue.user.login})
  })
);
```

```
constissueData =awaitoctokit.paginate("GET /repos/{owner}/{repo}/issues", {owner:"github",repo:"docs",page_limit:100,headers: {"x-github-api-version":"2026-03-10",
  },
},(response, done) =>response.data.map((issue) =>{if(issue.title.includes("test")) {done()
    }return({title: issue.title,author: issue.user.login})
  })
);
```
Instead of fetching all of the results at once, you can useoctokit.paginate.iterator()to iterate through a single page_number at a time. For example, the following example fetches one page_number of results at a time and processes each object from the page_number before fetching the next page_number. Once an issue that includes "test" in the title is reached, the script stops the iteration and returns the issue title and issue author of each object that was processed. The iterator is the most memory efficient method for fetching paginated data.

```
constiterator = octokit.paginate.iterator("GET /repos/{owner}/{repo}/issues", {owner:"github",repo:"docs",page_limit:100,headers: {"x-github-api-version":"2026-03-10",
  },
});letissueData = []letbreakLoop =falseforawait(const{data}ofiterator) {if(breakLoop)breakfor(constissueofdata) {if(issue.title.includes("test")) {
      breakLoop =truebreak}else{
      issueData = [...issueData, {title: issue.title,author: issue.user.login}];
    }
  }
}
```

```
constiterator = octokit.paginate.iterator("GET /repos/{owner}/{repo}/issues", {owner:"github",repo:"docs",page_limit:100,headers: {"x-github-api-version":"2026-03-10",
  },
});letissueData = []letbreakLoop =falseforawait(const{data}ofiterator) {if(breakLoop)breakfor(constissueofdata) {if(issue.title.includes("test")) {
      breakLoop =truebreak}else{
      issueData = [...issueData, {title: issue.title,author: issue.user.login}];
    }
  }
}
```
You can use thepaginatemethod with therestendpoint methods as well. Pass therestendpoint method as the first argument. Pass any parameters as the second argument.

```
constiterator = octokit.paginate.iterator(octokit.rest.issues.listForRepo, {owner:"github",repo:"docs",page_limit:100,headers: {"x-github-api-version":"2026-03-10",
  },
});
```

```
constiterator = octokit.paginate.iterator(octokit.rest.issues.listForRepo, {owner:"github",repo:"docs",page_limit:100,headers: {"x-github-api-version":"2026-03-10",
  },
});
```
For more information about pagination, seeUsing pagination in the REST API.

## Catching errors

### Catching all errors
Sometimes, the GitHub REST API will return an error. For example, you will get an error if your access token is expired or if you omitted a required parameter. Octokit.js automatically retries the request when it gets an error other than400 Bad Request,401 Unauthorized,403 Forbidden,404 Not Found, and422 Unprocessable Entity. If an API error occurs even after retries, Octokit.js throws an error that includes the HTTP status code of the response (response.status) and the response headers (response.headers). You should handle these errors in your code. For example, you can use a try/catch block to catch errors:

```
letfilesChanged = []try{constiterator = octokit.paginate.iterator("GET /repos/{owner}/{repo}/pulls/{pull_number}/files", {owner:"github",repo:"docs",pull_number:22809,page_limit:100,headers: {"x-github-api-version":"2026-03-10",
    },
  });forawait(const{data}ofiterator) {
    filesChanged = [...filesChanged, ...data.map(fileData=>fileData.filename)];
  }
}catch(error) {if(error.response) {console.error(`Error! Status:${error.response.status}. Message:${error.response.data.message}`)
  }console.error(error)
}
```

```
letfilesChanged = []try{constiterator = octokit.paginate.iterator("GET /repos/{owner}/{repo}/pulls/{pull_number}/files", {owner:"github",repo:"docs",pull_number:22809,page_limit:100,headers: {"x-github-api-version":"2026-03-10",
    },
  });forawait(const{data}ofiterator) {
    filesChanged = [...filesChanged, ...data.map(fileData=>fileData.filename)];
  }
}catch(error) {if(error.response) {console.error(`Error! Status:${error.response.status}. Message:${error.response.data.message}`)
  }console.error(error)
}
```

### Handling intended error codes
Sometimes, GitHub uses a 4xx status code to indicate a non-error response. If the endpoint you are using does this, you can add additional handling for specific errors. For example, theGET /user/starred/{owner}/{repo}endpoint will return a404if the repository is not starred. The following example uses the404response to indicate that the repository was not starred; all other errors codes are treated as errors.

```
try{awaitoctokit.request("GET /user/starred/{owner}/{repo}", {owner:"github",repo:"docs",headers: {"x-github-api-version":"2026-03-10",
    },
  });console.log(`The repository is starred by me`);

}catch(error) {if(error.status===404) {console.log(`The repository is not starred by me`);
  }else{console.error(`An error occurred while checking if the repository is starred:${error?.response?.data?.message}`);
  }
}
```

```
try{awaitoctokit.request("GET /user/starred/{owner}/{repo}", {owner:"github",repo:"docs",headers: {"x-github-api-version":"2026-03-10",
    },
  });console.log(`The repository is starred by me`);

}catch(error) {if(error.status===404) {console.log(`The repository is not starred by me`);
  }else{console.error(`An error occurred while checking if the repository is starred:${error?.response?.data?.message}`);
  }
}
```

### Handling rate limit errors
If you receive a rate limit error, you may want to retry your request after waiting. When you are rate limited, GitHub responds with a403 Forbiddenerror and thex-ratelimit-remainingresponse header value will be"0". The response headers will include ax-ratelimit-resetheader, which tells you the time at which the current rate limit window resets, in UTC epoch seconds. You can retry your request after the time specified byx-ratelimit-reset.

```
asyncfunctionrequestRetry(route, parameters) {try{constresponse =awaitoctokit.request(route, parameters);returnresponse
  }catch(error) {if(error.response&& error.status===403&& error.response.headers['x-ratelimit-remaining'] ==='0') {constresetTimeEpochSeconds = error.response.headers['x-ratelimit-reset'];constcurrentTimeEpochSeconds =Math.floor(Date.now() /1000);constsecondsToWait = resetTimeEpochSeconds - currentTimeEpochSeconds;console.log(`You have exceeded your rate limit. Retrying in${secondsToWait}seconds.`);setTimeout(requestRetry, secondsToWait *1000, route, parameters);
    }else{console.error(error);
    }
  }
}constresponse =awaitrequestRetry("GET /repos/{owner}/{repo}/issues", {owner:"github",repo:"docs",page_limit:2})
```

```
asyncfunctionrequestRetry(route, parameters) {try{constresponse =awaitoctokit.request(route, parameters);returnresponse
  }catch(error) {if(error.response&& error.status===403&& error.response.headers['x-ratelimit-remaining'] ==='0') {constresetTimeEpochSeconds = error.response.headers['x-ratelimit-reset'];constcurrentTimeEpochSeconds =Math.floor(Date.now() /1000);constsecondsToWait = resetTimeEpochSeconds - currentTimeEpochSeconds;console.log(`You have exceeded your rate limit. Retrying in${secondsToWait}seconds.`);setTimeout(requestRetry, secondsToWait *1000, route, parameters);
    }else{console.error(error);
    }
  }
}constresponse =awaitrequestRetry("GET /repos/{owner}/{repo}/issues", {owner:"github",repo:"docs",page_limit:2})
```

## Using the response
Therequestmethod returns a promise that resolves to an object if the request was successful. The object properties aredata(the response body returned by the endpoint),status(the HTTP response code),url(the URL of the request), andheaders(an object containing the response headers). Unless otherwise specified, the response body is in JSON format. Some endpoints do not return a response body; in those cases, thedataproperty is omitted.

```
constresponse =awaitoctokit.request("GET /repos/{owner}/{repo}/issues/{issue_number}", {owner:"github",repo:"docs",issue_number:11901,headers: {"x-github-api-version":"2026-03-10",
  },
});console.log(`The status of the response is:${response.status}`)console.log(`The request URL was:${response.url}`)console.log(`The x-ratelimit-remaining response header is:${response.headers["x-ratelimit-remaining"]}`)console.log(`The issue title is:${response.data.title}`)
```

```
constresponse =awaitoctokit.request("GET /repos/{owner}/{repo}/issues/{issue_number}", {owner:"github",repo:"docs",issue_number:11901,headers: {"x-github-api-version":"2026-03-10",
  },
});console.log(`The status of the response is:${response.status}`)console.log(`The request URL was:${response.url}`)console.log(`The x-ratelimit-remaining response header is:${response.headers["x-ratelimit-remaining"]}`)console.log(`The issue title is:${response.data.title}`)
```
Similarly, thepaginatemethod returns a promise. If the request was successful, the promise resolves to an array of data returned by the endpoint. Unlike therequestmethod, thepaginatemethod does not return the status code, URL, or headers.

```
constdata =awaitoctokit.paginate("GET /repos/{owner}/{repo}/issues", {owner:"github",repo:"docs",page_limit:100,headers: {"x-github-api-version":"2026-03-10",
  },
});console.log(`${data.length}issues were returned`)console.log(`The title of the first issue is:${data[0].title}`)
```

```
constdata =awaitoctokit.paginate("GET /repos/{owner}/{repo}/issues", {owner:"github",repo:"docs",page_limit:100,headers: {"x-github-api-version":"2026-03-10",
  },
});console.log(`${data.length}issues were returned`)console.log(`The title of the first issue is:${data[0].title}`)
```

## Example script
Here is a full example script that uses Octokit.js. The script importsOctokitand creates a new instance ofOctokit. If you wanted to authenticate with a GitHub App instead of a personal access token, you would import and instantiateAppinstead ofOctokit. For more information, seeAuthenticating with a GitHub App.
ThegetChangedFilesfunction gets all of the files changed for a pull request. ThecommentIfDataFilesChangedfunction calls thegetChangedFilesfunction. If any of the files that the pull request changed include/data/in the file path, then the function will comment on the pull request.

```
import{Octokit}from"octokit";constoctokit =newOctokit({auth:'YOUR-TOKEN',
});asyncfunctiongetChangedFiles({owner, repo, pullNumber}) {letfilesChanged = []try{constiterator = octokit.paginate.iterator("GET /repos/{owner}/{repo}/pulls/{pull_number}/files", {owner: owner,repo: repo,pull_number: pullNumber,page_limit:100,headers: {"x-github-api-version":"2026-03-10",
      },
    });forawait(const{data}ofiterator) {
      filesChanged = [...filesChanged, ...data.map(fileData=>fileData.filename)];
    }
  }catch(error) {if(error.response) {console.error(`Error! Status:${error.response.status}. Message:${error.response.data.message}`)
    }console.error(error)
  }returnfilesChanged
}asyncfunctioncommentIfDataFilesChanged({owner, repo, pullNumber}) {constchangedFiles =awaitgetChangedFiles({owner, repo, pullNumber});constfilePathRegex =newRegExp(/\/data\//,"i");if(!changedFiles.some(fileName=>filePathRegex.test(fileName))) {return;
  }try{const{data: comment} =awaitoctokit.request("POST /repos/{owner}/{repo}/issues/{issue_number}/comments", {owner: owner,repo: repo,issue_number: pullNumber,body:`It looks like you changed a data file. These files are auto-generated. \n\nYou must revert any changes to data files before your pull request will be reviewed.`,headers: {"x-github-api-version":"2026-03-10",
      },
    });returncomment.html_url;
  }catch(error) {if(error.response) {console.error(`Error! Status:${error.response.status}. Message:${error.response.data.message}`)
    }console.error(error)
  }
}awaitcommentIfDataFilesChanged({owner:"github",repo:"docs",pullNumber:191});
```

```
import{Octokit}from"octokit";constoctokit =newOctokit({auth:'YOUR-TOKEN',
});asyncfunctiongetChangedFiles({owner, repo, pullNumber}) {letfilesChanged = []try{constiterator = octokit.paginate.iterator("GET /repos/{owner}/{repo}/pulls/{pull_number}/files", {owner: owner,repo: repo,pull_number: pullNumber,page_limit:100,headers: {"x-github-api-version":"2026-03-10",
      },
    });forawait(const{data}ofiterator) {
      filesChanged = [...filesChanged, ...data.map(fileData=>fileData.filename)];
    }
  }catch(error) {if(error.response) {console.error(`Error! Status:${error.response.status}. Message:${error.response.data.message}`)
    }console.error(error)
  }returnfilesChanged
}asyncfunctioncommentIfDataFilesChanged({owner, repo, pullNumber}) {constchangedFiles =awaitgetChangedFiles({owner, repo, pullNumber});constfilePathRegex =newRegExp(/\/data\//,"i");if(!changedFiles.some(fileName=>filePathRegex.test(fileName))) {return;
  }try{const{data: comment} =awaitoctokit.request("POST /repos/{owner}/{repo}/issues/{issue_number}/comments", {owner: owner,repo: repo,issue_number: pullNumber,body:`It looks like you changed a data file. These files are auto-generated. \n\nYou must revert any changes to data files before your pull request will be reviewed.`,headers: {"x-github-api-version":"2026-03-10",
      },
    });returncomment.html_url;
  }catch(error) {if(error.response) {console.error(`Error! Status:${error.response.status}. Message:${error.response.data.message}`)
    }console.error(error)
  }
}awaitcommentIfDataFilesChanged({owner:"github",repo:"docs",pullNumber:191});
```

## Next steps
- To learn more about Octokit.js seethe Octokit.js documentation.
- For some real life examples, look at how GitHub Docs uses Octokit.js bysearching the GitHub Docs repository.