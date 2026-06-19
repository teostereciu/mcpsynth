# Quickstart for GitHub REST API

*Source: https://docs.github.com/en/rest/quickstart*

---

# Quickstart for GitHub REST API
Learn how to get started with the GitHub REST API.

## Tool navigation

## In this article

## Introduction
This article describes how to quickly get started with the GitHub REST API using GitHub CLI,curl, or JavaScript. For a more detailed guide, seeGetting started with the REST API.

## Using GitHub CLI in the command line
GitHub CLI is the easiest way to use the GitHub REST API from the command line.
1. Install GitHub CLI on macOS, Windows, or Linux. For more information, seeInstallationin the GitHub CLI repository.
2. To authenticate to GitHub, run the following command from your terminal.gh auth login
3. Select where you want to authenticate to:If you access GitHub at GitHub.com, selectGitHub.com.If you access GitHub at a different domain, selectOther, then enter your hostname (for example:octocorp.ghe.com).
4. Follow the rest of the on-screen prompts.GitHub CLI automatically stores your Git credentials for you when you choose HTTPS as your preferred protocol for Git operations and answer "yes" to the prompt asking if you would like to authenticate to Git with your GitHub credentials. This can be useful as it allows you to use Git commands likegit pushandgit pullwithout needing to set up a separate credential manager or use SSH.
5. Make a request using the GitHub CLIapisubcommand, followed by the path. Use the--methodor-Xflag to specify the method. For more information, see theGitHub CLIapidocumentation.This example makes a request to the "Get Octocat" endpoint, which uses the methodGETand the path/octocat. For the full reference documentation for this endpoint, seeREST API endpoints for meta data.gh api /octocat --method GET

```
gh auth login
```
- If you access GitHub at GitHub.com, selectGitHub.com.
- If you access GitHub at a different domain, selectOther, then enter your hostname (for example:octocorp.ghe.com).

```
gh api /octocat --method GET
```

```
gh api /octocat --method GET
```

## Using GitHub CLI in GitHub Actions
You can also use GitHub CLI in your GitHub Actions workflows. For more information, seeUsing GitHub CLI in workflows.

### Authenticating with an access token
Instead of using thegh auth logincommand, pass an access token as an environment variable calledGH_TOKEN. GitHub recommends that you use the built-inGITHUB_TOKENinstead of creating a token. If this is not possible, store your token as a secret and replaceGITHUB_TOKENin the example below with the name of your secret. For more information aboutGITHUB_TOKEN, seeUse GITHUB_TOKEN for authentication in workflows. For more information about secrets, seeUsing secrets in GitHub Actions.
The following example workflow uses theList repository issuesendpoint, and requests a list of issues in theoctocat/Spoon-Kniferepository.

```
on:workflow_dispatch:jobs:use_api:runs-on:ubuntu-latestpermissions:issues:readsteps:-env:GH_TOKEN:${{secrets.GITHUB_TOKEN}}run:|
          gh api https://api.github.com/repos/octocat/Spoon-Knife/issues
```

```
on:workflow_dispatch:jobs:use_api:runs-on:ubuntu-latestpermissions:issues:readsteps:-env:GH_TOKEN:${{secrets.GITHUB_TOKEN}}run:|
          gh api https://api.github.com/repos/octocat/Spoon-Knife/issues
```

### Authenticating with a GitHub App
If you are authenticating with a GitHub App, you can create an installation access token within your workflow:
1. Store your GitHub App's ID as a configuration variable. In the following example, replaceAPP_IDwith the name of the configuration variable. You can find your app ID on the settings page_number for your app or through the API. For more information, seeREST API endpoints for GitHub Apps. For more information about configuration variables, seeStore information in variables.
2. Generate a private key for your app. Store the contents of the resulting file as a secret. (Store the entire contents of the file, including-----BEGIN RSA PRIVATE KEY-----and-----END RSA PRIVATE KEY-----.) In the following example, replaceAPP_PEMwith the name of the secret. For more information, seeManaging private keys for GitHub Apps. For more information about secrets, seeUsing secrets in GitHub Actions.
3. Add a step to generate a token, and use that token instead ofGITHUB_TOKEN. Note that this token will expire after 60 minutes. For example:on:workflow_dispatch:jobs:track_pr:runs-on:ubuntu-lateststeps:-name:Generatetokenid:generate-tokenuses:actions/create-github-app-token@v2with:app-id:${{vars.APP_ID}}private-key:${{secrets.APP_PEM}}-name:UseAPIenv:GH_TOKEN:${{steps.generate-token.outputs.token}}run:|
          gh api https://api.github.com/repos/octocat/Spoon-Knife/issues

```
on:workflow_dispatch:jobs:track_pr:runs-on:ubuntu-lateststeps:-name:Generatetokenid:generate-tokenuses:actions/create-github-app-token@v2with:app-id:${{vars.APP_ID}}private-key:${{secrets.APP_PEM}}-name:UseAPIenv:GH_TOKEN:${{steps.generate-token.outputs.token}}run:|
          gh api https://api.github.com/repos/octocat/Spoon-Knife/issues
```

```
on:workflow_dispatch:jobs:track_pr:runs-on:ubuntu-lateststeps:-name:Generatetokenid:generate-tokenuses:actions/create-github-app-token@v2with:app-id:${{vars.APP_ID}}private-key:${{secrets.APP_PEM}}-name:UseAPIenv:GH_TOKEN:${{steps.generate-token.outputs.token}}run:|
          gh api https://api.github.com/repos/octocat/Spoon-Knife/issues
```

## Using Octokit.js
You can use Octokit.js to interact with the GitHub REST API in your JavaScript scripts. For more information, seeScripting with the REST API and JavaScript.
1. Create an access token. For example, create a personal access token or a GitHub App user access token. You will use this token to authenticate your request, so you should give it any scopes or permissions that are required to access that endpoint. For more information, seeAuthenticating to the REST APIorIdentifying and authorizing users for GitHub Apps.WarningTreat your access token like a password.To keep your token secure, you can store your token as a secret and run your script through GitHub Actions. For more information, see theUsing Octokit.js in GitHub Actionssection.You can also store your token as a Codespaces secret and run your script in Codespaces. For more information, seeManaging encrypted secrets for your codespaces.If these options are not possible, consider using another CLI service to store your token securely.
2. Installoctokit. For example,npm install octokit. For other ways to install or loadoctokit, seethe Octokit.js README.
3. Importoctokitin your script. For example,import { Octokit } from "octokit";. For other ways to importoctokit, seethe Octokit.js README.
4. Create an instance ofOctokitwith your token. ReplaceYOUR-TOKENwith your token.constoctokit =newOctokit({auth:'YOUR-TOKEN'});
5. Useoctokit.requestto execute your request. Send the HTTP method and path as the first argument. Specify any path, query, and body parameters in an object as the second argument. For more information about parameters, seeGetting started with the REST API.For example, in the following request the HTTP method isGET, the path is/repos/{owner}/{repo}/issues, and the parameters areowner: "octocat"andrepo: "Spoon-Knife".awaitoctokit.request("GET /repos/{owner}/{repo}/issues", {owner:"octocat",repo:"Spoon-Knife",
});

```
constoctokit =newOctokit({auth:'YOUR-TOKEN'});
```

```
constoctokit =newOctokit({auth:'YOUR-TOKEN'});
```

```
awaitoctokit.request("GET /repos/{owner}/{repo}/issues", {owner:"octocat",repo:"Spoon-Knife",
});
```

```
awaitoctokit.request("GET /repos/{owner}/{repo}/issues", {owner:"octocat",repo:"Spoon-Knife",
});
```

## Using Octokit.js in GitHub Actions
You can also execute your JavaScript scripts in your GitHub Actions workflows. For more information, seeWorkflow syntax for GitHub Actions.

### Authenticating with an access token
GitHub recommends that you use the built-inGITHUB_TOKENinstead of creating a token. If this is not possible, store your token as a secret and replaceGITHUB_TOKENin the example below with the name of your secret. For more information aboutGITHUB_TOKEN, seeUse GITHUB_TOKEN for authentication in workflows. For more information about secrets, seeUsing secrets in GitHub Actions.
The following example workflow:
1. Checks out the repository content
2. Sets up Node.js
3. Installsoctokit
4. Stores the value ofGITHUB_TOKENas an environment variable calledTOKENand runs.github/actions-scripts/use-the-api.mjs, which can access that environment variable asprocess.env.TOKEN

```
on:workflow_dispatch:jobs:use_api_via_script:runs-on:ubuntu-latestpermissions:issues:readsteps:-name:Checkoutrepocontentuses:actions/checkout@v5-name:SetupNodeuses:actions/setup-node@v4with:node-version:'16.17.0'cache:npm-name:Installdependenciesrun:npminstalloctokit-name:Runscriptrun:|
          node .github/actions-scripts/use-the-api.mjsenv:TOKEN:${{secrets.GITHUB_TOKEN}}
```

```
on:workflow_dispatch:jobs:use_api_via_script:runs-on:ubuntu-latestpermissions:issues:readsteps:-name:Checkoutrepocontentuses:actions/checkout@v5-name:SetupNodeuses:actions/setup-node@v4with:node-version:'16.17.0'cache:npm-name:Installdependenciesrun:npminstalloctokit-name:Runscriptrun:|
          node .github/actions-scripts/use-the-api.mjsenv:TOKEN:${{secrets.GITHUB_TOKEN}}
```
The following is an example JavaScript script with the file path.github/actions-scripts/use-the-api.mjs.

```
import{Octokit}from"octokit"constoctokit =newOctokit({auth: process.env.TOKEN});try{constresult =awaitoctokit.request("GET /repos/{owner}/{repo}/issues", {owner:"octocat",repo:"Spoon-Knife",
    });consttitleAndAuthor = result.data.map(issue=>{title: issue.title,authorID: issue.user.id})console.log(titleAndAuthor)

}catch(error) {console.log(`Error! Status:${error.status}. Message:${error.response.data.message}`)
}
```

```
import{Octokit}from"octokit"constoctokit =newOctokit({auth: process.env.TOKEN});try{constresult =awaitoctokit.request("GET /repos/{owner}/{repo}/issues", {owner:"octocat",repo:"Spoon-Knife",
    });consttitleAndAuthor = result.data.map(issue=>{title: issue.title,authorID: issue.user.id})console.log(titleAndAuthor)

}catch(error) {console.log(`Error! Status:${error.status}. Message:${error.response.data.message}`)
}
```

### Authenticating with a GitHub App
If you are authenticating with a GitHub App, you can create an installation access token within your workflow:
1. Store your GitHub App's ID as a configuration variable. In the following example, replaceAPP_IDwith the name of the configuration variable. You can find your app ID on the settings page_number for your app or through the App API. For more information, seeREST API endpoints for GitHub Apps. For more information about configuration variables, seeStore information in variables.
2. Generate a private key for your app. Store the contents of the resulting file as a secret. (Store the entire contents of the file, including-----BEGIN RSA PRIVATE KEY-----and-----END RSA PRIVATE KEY-----.) In the following example, replaceAPP_PEMwith the name of the secret. For more information, seeManaging private keys for GitHub Apps. For more information about secrets, seeUsing secrets in GitHub Actions.
3. Add a step to generate a token, and use that token instead ofGITHUB_TOKEN. Note that this token will expire after 60 minutes. For example:on:workflow_dispatch:jobs:use_api_via_script:runs-on:ubuntu-lateststeps:-name:Checkoutrepocontentuses:actions/checkout@v5-name:SetupNodeuses:actions/setup-node@v4with:node-version:'16.17.0'cache:npm-name:Installdependenciesrun:npminstalloctokit-name:Generatetokenid:generate-tokenuses:actions/create-github-app-token@v2with:app-id:${{vars.APP_ID}}private-key:${{secrets.APP_PEM}}-name:Runscriptrun:|
          node .github/actions-scripts/use-the-api.mjsenv:TOKEN:${{steps.generate-token.outputs.token}}

```
on:workflow_dispatch:jobs:use_api_via_script:runs-on:ubuntu-lateststeps:-name:Checkoutrepocontentuses:actions/checkout@v5-name:SetupNodeuses:actions/setup-node@v4with:node-version:'16.17.0'cache:npm-name:Installdependenciesrun:npminstalloctokit-name:Generatetokenid:generate-tokenuses:actions/create-github-app-token@v2with:app-id:${{vars.APP_ID}}private-key:${{secrets.APP_PEM}}-name:Runscriptrun:|
          node .github/actions-scripts/use-the-api.mjsenv:TOKEN:${{steps.generate-token.outputs.token}}
```

## Usingcurlin the command line
Note
If you want to make API requests from the command line, GitHub recommends that you use GitHub CLI, which simplifies authentication and requests. For more information about getting started with the REST API using GitHub CLI, see the GitHub CLI version of this article.
1. Installcurlif it isn't already installed on your machine. To check ifcurlis installed, executecurl --versionin the command line. If the output provides information about the version ofcurl, that meanscurlis installed. If you get a message similar tocommand not found: curl, you need to download and installcurl. For more information, seethe curl project download page_number.
2. Create an access token. For example, create a personal access token or a GitHub App user access token. You will use this token to authenticate your request, so you should give it any scopes or permissions that are required to access the endpoint. For more information, seeAuthenticating to the REST API.WarningTreat your access token like a password.To keep your token secure, you can store your token as a Codespaces secret and use the command line through Codespaces. For more information, seeManaging encrypted secrets for your codespaces.You can also use GitHub CLI instead ofcurl. GitHub CLI will take care of authentication for you. For more information, see the GitHub CLI version of this page_number.If these options are not possible, consider using another CLI service to store your token securely.
3. Use thecurlcommand to make your request. Pass your token in anAuthorizationheader. ReplaceYOUR-TOKENwith your token.curl --request GET \
--url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer YOUR-TOKEN"NoteIn most cases, you can useAuthorization: BearerorAuthorization: tokento pass a token. However, if you are passing a JSON web token (JWT), you must useAuthorization: Bearer.

```
curl --request GET \
--url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer YOUR-TOKEN"
```

```
curl --request GET \
--url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
--header "Accept: application/vnd.github+json" \
--header "Authorization: Bearer YOUR-TOKEN"
```

## Usingcurlcommands in GitHub Actions
You can also usecurlcommands in your GitHub Actions workflows.

### Authenticating with an access token
GitHub recommends that you use the built-inGITHUB_TOKENinstead of creating a token. If this is not possible, store your token as a secret and replaceGITHUB_TOKENin the example below with the name of your secret. For more information aboutGITHUB_TOKEN, seeUse GITHUB_TOKEN for authentication in workflows. For more information about secrets, seeUsing secrets in GitHub Actions.

```
on:workflow_dispatch:jobs:use_api:runs-on:ubuntu-latestpermissions:issues:readsteps:-env:GH_TOKEN:${{secrets.GITHUB_TOKEN}}run:|
          curl --request GET \
          --url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
          --header "Accept: application/vnd.github+json" \
          --header "Authorization: Bearer $GH_TOKEN"
```

```
on:workflow_dispatch:jobs:use_api:runs-on:ubuntu-latestpermissions:issues:readsteps:-env:GH_TOKEN:${{secrets.GITHUB_TOKEN}}run:|
          curl --request GET \
          --url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
          --header "Accept: application/vnd.github+json" \
          --header "Authorization: Bearer $GH_TOKEN"
```

### Authenticating with a GitHub App
If you are authenticating with a GitHub App, you can create an installation access token within your workflow:
1. Store your GitHub App's ID as a configuration variable. In the following example, replaceAPP_IDwith the name of the configuration variable. You can find your app ID on the settings page_number for your app or through the App API. For more information, seeREST API endpoints for GitHub Apps. For more information about configuration variables, seeStore information in variables.
2. Generate a private key for your app. Store the contents of the resulting file as a secret. (Store the entire contents of the file, including-----BEGIN RSA PRIVATE KEY-----and-----END RSA PRIVATE KEY-----.) In the following example, replaceAPP_PEMwith the name of the secret. For more information, seeManaging private keys for GitHub Apps. For more information about storing secrets, seeUsing secrets in GitHub Actions.
3. Add a step to generate a token, and use that token instead ofGITHUB_TOKEN. Note that this token will expire after 60 minutes. For example:on:workflow_dispatch:jobs:use_api:runs-on:ubuntu-lateststeps:-name:Generatetokenid:generate-tokenuses:actions/create-github-app-token@v2with:app-id:${{vars.APP_ID}}private-key:${{secrets.APP_PEM}}-name:UseAPIenv:GH_TOKEN:${{steps.generate-token.outputs.token}}run:|
          curl --request GET \
          --url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
          --header "Accept: application/vnd.github+json" \
          --header "Authorization: Bearer $GH_TOKEN"

```
on:workflow_dispatch:jobs:use_api:runs-on:ubuntu-lateststeps:-name:Generatetokenid:generate-tokenuses:actions/create-github-app-token@v2with:app-id:${{vars.APP_ID}}private-key:${{secrets.APP_PEM}}-name:UseAPIenv:GH_TOKEN:${{steps.generate-token.outputs.token}}run:|
          curl --request GET \
          --url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
          --header "Accept: application/vnd.github+json" \
          --header "Authorization: Bearer $GH_TOKEN"
```

```
on:workflow_dispatch:jobs:use_api:runs-on:ubuntu-lateststeps:-name:Generatetokenid:generate-tokenuses:actions/create-github-app-token@v2with:app-id:${{vars.APP_ID}}private-key:${{secrets.APP_PEM}}-name:UseAPIenv:GH_TOKEN:${{steps.generate-token.outputs.token}}run:|
          curl --request GET \
          --url "https://api.github.com/repos/octocat/Spoon-Knife/issues" \
          --header "Accept: application/vnd.github+json" \
          --header "Authorization: Bearer $GH_TOKEN"
```

## Next steps
For a more detailed guide, seeGetting started with the REST API.