# Breaking changes

*Source: https://docs.github.com/en/rest/overview/breaking-changes*

---

# Breaking changes
Learn about breaking changes that were introduced in each REST API version.

## In this article

## About breaking changes in the REST API
The GitHub REST API is versioned. The API version name is based on the date when the API version was released. For example, the API version2026-03-10was released on Tue, 10 Mar 2026.
Breaking changes are changes that can potentially break an integration. We will provide advance notice before releasing breaking changes. Breaking changes include:
- Removing an entire operation
- Removing or renaming a parameter
- Removing or renaming a response field
- Adding a new required parameter
- Making a previously optional parameter required
- Changing the type of a parameter or response field
- Removing enum values
- Adding a new validation rule to an existing parameter
- Changing authentication or authorization requirements
Any additive (non-breaking) changes will be available in all supported API versions. Additive changes are changes that should not break an integration. Additive changes include:
- Adding an operation
- Adding an optional parameter
- Adding an optional request header
- Adding a response field
- Adding a response header
- Adding enum values
When a new REST API version is released, the previous API version will be supported for at least 24 more months following the release of the new API version.
For more information about API versions, seeAPI Versions.

## Upgrading to a new API version
Before upgrading to a new REST API version, you should read the section on this page that corresponds to the new API version to understand what breaking changes are included and to learn more about how to upgrade to that API version.
When you update your integration to specify the new API version in theX-GitHub-Api-Versionheader, you'll also need to make any changes required for your integration to work with the new API version.
Once your integration is updated, test your integration to verify that it works with the new API version.

## Version 2026-03-10
- Remove deprecatedrateproperty from rate limit endpointTherateproperty has been deprecated since 2021 and duplicates information
available in theresources.coreproperty. To migrate, update your integration
to read rate limit information fromresources.coreinstead ofrate.Seehttps://docs.github.com/rest/rate-limitfor updated documentation.Affected endpointsGET /rate_limit
- Remove deprecatedpermissionproperty from request when a team is createdAffected endpointsPOST /orgs/{org}/teams
- Updates the "Get repository content" API, so that, when listing the contents of a directory, submodules have thetype"submodule" instead of thetype"file"Affected endpointsGET /repos/{owner}/{repo}/contents/{path}
- Change Content-Type of SARIF responseWhen trying to receive the SARIF upload by setting theAcceptheader toapplication/sarif+jsonthe responseContent-Typewould incorrectly be set toapplication/json+sarif.
This change corrects this so the responseContent-Typein this case becomesapplication/sarif+json.For more information, see "Get a code scanning analysis for a repository" in the REST API documentation.
- Remove deprecateduse_squash_pr_title_as_defaultproperty from repo settings endpointsThis property has been replaced bysquash_merge_commit_title.Affected endpointsDELETE /repos/{owner}/{repo}/issues/{issue_number}/assigneesDELETE /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by/{issue_id}DELETE /repos/{owner}/{repo}/issues/{issue_number}/sub_issueDELETE /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewersGET /eventsGET /installation/repositoriesGET /issuesGET /networks/{owner}/{repo}/eventsGET /orgs/{org}/actions/permissions/repositoriesGET /orgs/{org}/actions/permissions/self-hosted-runners/repositoriesGET /orgs/{org}/eventsGET /orgs/{org}/issuesGET /orgs/{org}/migrationsGET /orgs/{org}/migrations/{migration_id}GET /repos/{owner}/{repo}GET /repos/{owner}/{repo}/commits/{commit_sha}/pullsGET /repos/{owner}/{repo}/eventsGET /repos/{owner}/{repo}/issuesGET /repos/{owner}/{repo}/issues/eventsGET /repos/{owner}/{repo}/issues/events/{event_id}GET /repos/{owner}/{repo}/issues/{issue_number}GET /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_byGET /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blockingGET /repos/{owner}/{repo}/issues/{issue_number}/parentGET /repos/{owner}/{repo}/issues/{issue_number}/sub_issuesGET /repos/{owner}/{repo}/issues/{issue_number}/timelineGET /repos/{owner}/{repo}/pullsGET /repos/{owner}/{repo}/pulls/{pull_number}GET /search/issuesGET /teams/{team_id}/repos/{owner}/{repo}GET /user/installations/{installation_id}/repositoriesGET /user/issuesGET /user/migrationsGET /user/migrations/{migration_id}GET /user/reposGET /user/starredGET /users/{username}/eventsGET /users/{username}/events/orgs/{org}GET /users/{username}/events/publicGET /users/{username}/received_eventsGET /users/{username}/received_events/publicGET /users/{username}/starredPATCH /repos/{owner}/{repo}PATCH /repos/{owner}/{repo}/issues/{issue_number}PATCH /repos/{owner}/{repo}/issues/{issue_number}/sub_issues/priorityPATCH /repos/{owner}/{repo}/pulls/{pull_number}POST /app/installations/{installation_id}/access_tokensPOST /enterprises/{enterprise}/actions/runners/registration-tokenPOST /enterprises/{enterprise}/actions/runners/remove-tokenPOST /orgs/{org}/actions/runners/registration-tokenPOST /orgs/{org}/actions/runners/remove-tokenPOST /orgs/{org}/migrationsPOST /orgs/{org}/projectsV2/{project_number}/draftsPOST /orgs/{org}/projectsV2/{project_number}/itemsPOST /orgs/{org}/reposPOST /repos/{owner}/{repo}/actions/runners/registration-tokenPOST /repos/{owner}/{repo}/actions/runners/remove-tokenPOST /repos/{owner}/{repo}/forksPOST /repos/{owner}/{repo}/issuesPOST /repos/{owner}/{repo}/issues/{issue_number}/assigneesPOST /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_byPOST /repos/{owner}/{repo}/issues/{issue_number}/sub_issuesPOST /repos/{owner}/{repo}/pullsPOST /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewersPOST /repos/{owner}/{repo}/security-advisories/{ghsa_id}/forksPOST /repos/{template_owner}/{template_repo}/generatePOST /user/codespaces/{codespace_name}/publishPOST /user/migrationsPOST /user/reposPOST /user/{user_id}/projectsV2/{project_number}/draftsPOST /users/{username}/projectsV2/{project_number}/items
- Removeauthorizations_urlfrom the API root (GET /)The OAuth Authorization API has beendeprecated since 2020.Affected endpointsGET /
- Deprecate support for thebetamedia typeThis media type was officially deprecated in 2014. However, there are still remnants
of its use that modify response payloads. The following response properties are
deprecated as a result:emailsresponse as a flat array of strings instead of email objectspull_requestresponse property withnulldefault valuesuserresponse property, replaced byownermaster_branchresponse property, replaced bydefault_branchAffected endpointsDELETE /repos/{owner}/{repo}/issues/{issue_number}/assigneesDELETE /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by/{issue_id}DELETE /repos/{owner}/{repo}/issues/{issue_number}/sub_issueDELETE /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewersGET /eventsGET /gistsGET /gists/publicGET /gists/starredGET /installation/repositoriesGET /issuesGET /networks/{owner}/{repo}/eventsGET /orgs/{org}/actions/permissions/repositoriesGET /orgs/{org}/actions/permissions/self-hosted-runners/repositoriesGET /orgs/{org}/eventsGET /orgs/{org}/issuesGET /orgs/{org}/migrationsGET /orgs/{org}/migrations/{migration_id}GET /repos/{owner}/{repo}GET /repos/{owner}/{repo}/commits/{commit_sha}/pullsGET /repos/{owner}/{repo}/eventsGET /repos/{owner}/{repo}/issuesGET /repos/{owner}/{repo}/issues/eventsGET /repos/{owner}/{repo}/issues/events/{event_id}GET /repos/{owner}/{repo}/issues/{issue_number}GET /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_byGET /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blockingGET /repos/{owner}/{repo}/issues/{issue_number}/parentGET /repos/{owner}/{repo}/issues/{issue_number}/sub_issuesGET /repos/{owner}/{repo}/issues/{issue_number}/timelineGET /repos/{owner}/{repo}/pullsGET /repos/{owner}/{repo}/pulls/{pull_number}GET /search/issuesGET /teams/{team_id}/repos/{owner}/{repo}GET /user/installations/{installation_id}/repositoriesGET /user/issuesGET /user/migrationsGET /user/migrations/{migration_id}GET /user/reposGET /user/starredGET /users/{username}/eventsGET /users/{username}/events/orgs/{org}GET /users/{username}/events/publicGET /users/{username}/gistsGET /users/{username}/received_eventsGET /users/{username}/received_events/publicGET /users/{username}/starredPATCH /repos/{owner}/{repo}PATCH /repos/{owner}/{repo}/issues/{issue_number}PATCH /repos/{owner}/{repo}/issues/{issue_number}/sub_issues/priorityPATCH /repos/{owner}/{repo}/pulls/{pull_number}POST /app/installations/{installation_id}/access_tokensPOST /enterprises/{enterprise}/actions/runners/registration-tokenPOST /enterprises/{enterprise}/actions/runners/remove-tokenPOST /gists/{gist_id}/forksPOST /orgs/{org}/actions/runners/registration-tokenPOST /orgs/{org}/actions/runners/remove-tokenPOST /orgs/{org}/migrationsPOST /orgs/{org}/projectsV2/{project_number}/draftsPOST /orgs/{org}/projectsV2/{project_number}/itemsPOST /orgs/{org}/reposPOST /repos/{owner}/{repo}/actions/runners/registration-tokenPOST /repos/{owner}/{repo}/actions/runners/remove-tokenPOST /repos/{owner}/{repo}/forksPOST /repos/{owner}/{repo}/issuesPOST /repos/{owner}/{repo}/issues/{issue_number}/assigneesPOST /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_byPOST /repos/{owner}/{repo}/issues/{issue_number}/sub_issuesPOST /repos/{owner}/{repo}/pullsPOST /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewersPOST /repos/{owner}/{repo}/security-advisories/{ghsa_id}/forksPOST /repos/{template_owner}/{template_repo}/generatePOST /user/codespaces/{codespace_name}/publishPOST /user/migrationsPOST /user/reposPOST /user/{user_id}/projectsV2/{project_number}/draftsPOST /users/{username}/projectsV2/{project_number}/items
- This changeset removes the underspecified fieldshistoryandforksfrom the base-gist objectThese properties were unintentionally added when we converted JSON schemas to OpenAPI. The
properties appear in resources such as "gist revisions" and "update gist" but should not
be implemented in the base gist object.Affected endpointsGET /gistsGET /gists/publicGET /gists/starredGET /gists/{gist_id}GET /gists/{gist_id}/forksGET /gists/{gist_id}/{sha}GET /users/{username}/gistsPATCH /gists/{gist_id}POST /gistsPOST /gists/{gist_id}/forks
- Change success status code from204to202for deleting an installationThe installation deletion is being moved to the backgroundAffected endpointsDELETE /app/installations/{installation_id}
- Removesecret_scanning_push_protection_custom_link_enabledfrom the organization request and responseAffected endpointsGET /orgs/{org}PATCH /orgs/{org}
- Removejavascriptandtypescriptvalues from thelanguagesenum in code scanning default setup responses, in favor ofjavascript-typescriptJavaScript and TypeScript are analyzed together by CodeQL, so having separate enum values was misleading and inconsistent with how the analysis actually works. This breaking change removes the individual "javascript" and "typescript" values in favor of the combined "javascript-typescript" value that accurately represents the unified analysis.For more information, see "Get a code scanning default setup configuration" in the REST API documentation and the relatedcodeql-actionCHANGELOG.Affected endpointsGET /repos/{owner}/{repo}/code-scanning/default-setup
- Remove deprecatedhas_downloadsproperty from Repository responsehas_downloadshas been deprecated for 10+ yearsAffected endpointsDELETE /repos/{owner}/{repo}/issues/{issue_number}/assigneesDELETE /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by/{issue_id}DELETE /repos/{owner}/{repo}/issues/{issue_number}/sub_issueDELETE /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewersGET /eventsGET /installation/repositoriesGET /issuesGET /networks/{owner}/{repo}/eventsGET /notificationsGET /notifications/threads/{thread_id}GET /orgs/{org}/actions/permissions/repositoriesGET /orgs/{org}/actions/permissions/self-hosted-runners/repositoriesGET /orgs/{org}/actions/runner-groups/{runner_group_id}/repositoriesGET /orgs/{org}/actions/secrets/{secret_name}/repositoriesGET /orgs/{org}/actions/variables/{name}/repositoriesGET /orgs/{org}/codespacesGET /orgs/{org}/codespaces/secrets/{secret_name}/repositoriesGET /orgs/{org}/dependabot/secrets/{secret_name}/repositoriesGET /orgs/{org}/docker/conflictsGET /orgs/{org}/eventsGET /orgs/{org}/issuesGET /orgs/{org}/members/{username}/codespacesGET /orgs/{org}/migrationsGET /orgs/{org}/migrations/{migration_id}GET /orgs/{org}/migrations/{migration_id}/repositoriesGET /orgs/{org}/packagesGET /orgs/{org}/packages/{package_type}/{package_name}GET /orgs/{org}/personal-access-token-requests/{pat_request_id}/repositoriesGET /orgs/{org}/personal-access-tokens/{pat_id}/repositoriesGET /orgs/{org}/reposGET /orgs/{org}/settings/immutable-releases/repositoriesGET /orgs/{org}/teams/{team_slug}/reposGET /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}GET /repos/{owner}/{repo}GET /repos/{owner}/{repo}/actions/runsGET /repos/{owner}/{repo}/actions/runs/{run_id}GET /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}/runsGET /repos/{owner}/{repo}/check-suites/{check_suite_id}GET /repos/{owner}/{repo}/codespacesGET /repos/{owner}/{repo}/commits/{commit_sha}/pullsGET /repos/{owner}/{repo}/commits/{ref}/check-suitesGET /repos/{owner}/{repo}/commits/{ref}/statusGET /repos/{owner}/{repo}/eventsGET /repos/{owner}/{repo}/forksGET /repos/{owner}/{repo}/invitationsGET /repos/{owner}/{repo}/issuesGET /repos/{owner}/{repo}/issues/eventsGET /repos/{owner}/{repo}/issues/events/{event_id}GET /repos/{owner}/{repo}/issues/{issue_number}GET /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_byGET /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blockingGET /repos/{owner}/{repo}/issues/{issue_number}/parentGET /repos/{owner}/{repo}/issues/{issue_number}/sub_issuesGET /repos/{owner}/{repo}/issues/{issue_number}/timelineGET /repos/{owner}/{repo}/notificationsGET /repos/{owner}/{repo}/pullsGET /repos/{owner}/{repo}/pulls/{pull_number}GET /repositoriesGET /search/codeGET /search/commitsGET /search/issuesGET /teams/{team_id}/reposGET /teams/{team_id}/repos/{owner}/{repo}GET /user/codespacesGET /user/codespaces/secrets/{secret_name}/repositoriesGET /user/codespaces/{codespace_name}GET /user/docker/conflictsGET /user/installations/{installation_id}/repositoriesGET /user/issuesGET /user/migrationsGET /user/migrations/{migration_id}GET /user/migrations/{migration_id}/repositoriesGET /user/packagesGET /user/packages/{package_type}/{package_name}GET /user/reposGET /user/repository_invitationsGET /user/starredGET /user/subscriptionsGET /users/{username}/docker/conflictsGET /users/{username}/eventsGET /users/{username}/events/orgs/{org}GET /users/{username}/events/publicGET /users/{username}/packagesGET /users/{username}/packages/{package_type}/{package_name}GET /users/{username}/received_eventsGET /users/{username}/received_events/publicGET /users/{username}/reposGET /users/{username}/starredGET /users/{username}/subscriptionsPATCH /repos/{owner}/{repo}PATCH /repos/{owner}/{repo}/check-suites/preferencesPATCH /repos/{owner}/{repo}/invitations/{invitation_id}PATCH /repos/{owner}/{repo}/issues/{issue_number}PATCH /repos/{owner}/{repo}/issues/{issue_number}/sub_issues/priorityPATCH /repos/{owner}/{repo}/pulls/{pull_number}PATCH /user/codespaces/{codespace_name}POST /app/installations/{installation_id}/access_tokensPOST /enterprises/{enterprise}/actions/runners/registration-tokenPOST /enterprises/{enterprise}/actions/runners/remove-tokenPOST /orgs/{org}/actions/runners/registration-tokenPOST /orgs/{org}/actions/runners/remove-tokenPOST /orgs/{org}/members/{username}/codespaces/{codespace_name}/stopPOST /orgs/{org}/migrationsPOST /orgs/{org}/projectsV2/{project_number}/draftsPOST /orgs/{org}/projectsV2/{project_number}/itemsPOST /orgs/{org}/reposPOST /repos/{owner}/{repo}/actions/runners/registration-tokenPOST /repos/{owner}/{repo}/actions/runners/remove-tokenPOST /repos/{owner}/{repo}/check-suitesPOST /repos/{owner}/{repo}/codespacesPOST /repos/{owner}/{repo}/forksPOST /repos/{owner}/{repo}/issuesPOST /repos/{owner}/{repo}/issues/{issue_number}/assigneesPOST /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_byPOST /repos/{owner}/{repo}/issues/{issue_number}/sub_issuesPOST /repos/{owner}/{repo}/pullsPOST /repos/{owner}/{repo}/pulls/{pull_number}/codespacesPOST /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewersPOST /repos/{owner}/{repo}/security-advisories/{ghsa_id}/forksPOST /repos/{owner}/{repo}/transferPOST /repos/{template_owner}/{template_repo}/generatePOST /user/codespacesPOST /user/codespaces/{codespace_name}/publishPOST /user/codespaces/{codespace_name}/startPOST /user/codespaces/{codespace_name}/stopPOST /user/migrationsPOST /user/reposPOST /user/{user_id}/projectsV2/{project_number}/draftsPOST /users/{username}/projectsV2/{project_number}/itemsPUT /repos/{owner}/{repo}/collaborators/{username}
- Change create repository response from422to451when blocked by trade controlsRepository creation requests where the creator or owner is subject to trade control regulations
now return451 Unavailable For Legal Reasonsinstead of422 Unprocessable Entity.Affected endpointsPOST /orgs/{org}/reposPOST /user/repos
- Change delete organization response from403to451when blocked by trade controlsOrganization deletion requests blocked by trade controls now return451 Unavailable For Legal Reasonsinstead of403 Forbidden.Affected endpointsDELETE /orgs/{org}
- Change remove organization member response from403to451when blocked by trade controlsRequests to remove a member from a trade-controlled organization now return451 Unavailable For Legal Reasonsinstead of403 Forbidden.Affected endpointsDELETE /orgs/{org}/members/{username}
- Change update organization membership response from403to451when blocked by trade controlsMembership update requests for trade-controlled organizations now return451 Unavailable For Legal Reasonsinstead of403 Forbidden.Affected endpointsPUT /orgs/{org}/memberships/{username}
- Change accept repository invitation response from403to451when blocked by trade controlsRepository invitation acceptance blocked by trade controls now returns451 Unavailable For Legal Reasonsinstead of403 Forbidden.Affected endpointsPATCH /user/repository_invitations/{invitation_id}
- Remove deprecatedhub_urlproperty from API root responseAffected endpointsGET /
- Deprecatecvssproperty in favor ofcvss_severitiesfor advisory APIsThecvss_severitiesproperty will supplant the existingcvssproperty and containcvss_v3andcvss_v4properties if they exist on the advisory.Affected endpointsGET /advisoriesGET /advisories/{ghsa_id}GET /enterprises/{enterprise}/dependabot/alertsGET /orgs/{org}/dependabot/alertsGET /orgs/{org}/security-advisoriesGET /repos/{owner}/{repo}/dependabot/alertsGET /repos/{owner}/{repo}/dependabot/alerts/{alert_number}GET /repos/{owner}/{repo}/security-advisoriesGET /repos/{owner}/{repo}/security-advisories/{ghsa_id}PATCH /repos/{owner}/{repo}/dependabot/alerts/{alert_number}PATCH /repos/{owner}/{repo}/security-advisories/{ghsa_id}POST /repos/{owner}/{repo}/security-advisoriesPOST /repos/{owner}/{repo}/security-advisories/reports
- Remove repository detail fields from migration resource responsesAffected endpointsGET /orgs/{org}/migrationsGET /orgs/{org}/migrations/{migration_id}GET /orgs/{org}/migrations/{migration_id}/repositoriesGET /user/migrationsGET /user/migrations/{migration_id}GET /user/migrations/{migration_id}/repositoriesPOST /orgs/{org}/migrationsPOST /user/migrations
- Remove deprecated/hubendpoint
- Removemerge_commit_shafield from pull request responsesThemerge_commit_shaproperty is removed from pull request payloads across all endpoints that return pull request objects.Affected endpointsDELETE /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewersGET /eventsGET /networks/{owner}/{repo}/eventsGET /orgs/{org}/eventsGET /repos/{owner}/{repo}/commits/{commit_sha}/pullsGET /repos/{owner}/{repo}/eventsGET /repos/{owner}/{repo}/pullsGET /repos/{owner}/{repo}/pulls/{pull_number}GET /users/{username}/eventsGET /users/{username}/events/orgs/{org}GET /users/{username}/events/publicGET /users/{username}/received_eventsGET /users/{username}/received_events/publicPATCH /repos/{owner}/{repo}/pulls/{pull_number}POST /orgs/{org}/projectsV2/{project_number}/draftsPOST /orgs/{org}/projectsV2/{project_number}/itemsPOST /repos/{owner}/{repo}/pullsPOST /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewersPOST /user/{user_id}/projectsV2/{project_number}/draftsPOST /users/{username}/projectsV2/{project_number}/items
- Change workflow dispatch response from204to200with workflow run detailsRemoves thereturn_run_detailsparameter. The endpoint now always returns200with the workflow run details in the response body.Affected endpointsPOST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches
- Remove deprecated singular "assignee" field from Issue and Pull Request endpointsThe singularassigneefield has been marked as "closing down" for years and
duplicates information available in theassigneesarray. To migrate, update
your integration to:Use theassigneesarray parameter instead of the singularassigneeparameter when creating or updating Issues.Read assignee information from theassigneesarray instead of the singularassigneeproperty in Issue and Pull Request responses.Seehttps://docs.github.com/rest/issues/issuesfor updated documentation.Affected endpointsDELETE /repos/{owner}/{repo}/issues/{issue_number}/assigneesDELETE /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by/{issue_id}DELETE /repos/{owner}/{repo}/issues/{issue_number}/sub_issueDELETE /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewersGET /eventsGET /issuesGET /networks/{owner}/{repo}/eventsGET /orgs/{org}/eventsGET /orgs/{org}/issuesGET /repos/{owner}/{repo}/commits/{commit_sha}/pullsGET /repos/{owner}/{repo}/eventsGET /repos/{owner}/{repo}/issuesGET /repos/{owner}/{repo}/issues/eventsGET /repos/{owner}/{repo}/issues/events/{event_id}GET /repos/{owner}/{repo}/issues/{issue_number}GET /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_byGET /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blockingGET /repos/{owner}/{repo}/issues/{issue_number}/parentGET /repos/{owner}/{repo}/issues/{issue_number}/sub_issuesGET /repos/{owner}/{repo}/issues/{issue_number}/timelineGET /repos/{owner}/{repo}/pullsGET /repos/{owner}/{repo}/pulls/{pull_number}GET /search/issuesGET /user/issuesGET /users/{username}/eventsGET /users/{username}/events/orgs/{org}GET /users/{username}/events/publicGET /users/{username}/received_eventsGET /users/{username}/received_events/publicPATCH /repos/{owner}/{repo}/issues/{issue_number}PATCH /repos/{owner}/{repo}/issues/{issue_number}/sub_issues/priorityPATCH /repos/{owner}/{repo}/pulls/{pull_number}POST /orgs/{org}/projectsV2/{project_number}/draftsPOST /orgs/{org}/projectsV2/{project_number}/itemsPOST /repos/{owner}/{repo}/issuesPOST /repos/{owner}/{repo}/issues/{issue_number}/assigneesPOST /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_byPOST /repos/{owner}/{repo}/issues/{issue_number}/sub_issuesPOST /repos/{owner}/{repo}/pullsPOST /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewersPOST /user/{user_id}/projectsV2/{project_number}/draftsPOST /users/{username}/projectsV2/{project_number}/items
- Changeselected_repository_idsparameter to only accept integers for Dependabot org secretsAffected endpointsPUT /orgs/{org}/dependabot/secrets/{secret_name}
- Remove thebundleproperty from attestation list responsesThebundlefield is removed from repo, org, and user attestation list and bulk-list responses. Usebundle_urlto retrieve the attestation bundle.Affected endpointsGET /orgs/{org}/attestations/{subject_digest}GET /repos/{owner}/{repo}/attestations/{subject_digest}GET /users/{username}/attestations/{subject_digest}POST /orgs/{org}/attestations/bulk-listPOST /users/{username}/attestations/bulk-list
- GET /rate_limit
- POST /orgs/{org}/teams
- GET /repos/{owner}/{repo}/contents/{path}

```
use_squash_pr_title_as_default
```
- DELETE /repos/{owner}/{repo}/issues/{issue_number}/assignees
- DELETE /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by/{issue_id}
- DELETE /repos/{owner}/{repo}/issues/{issue_number}/sub_issue
- DELETE /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers
- GET /events
- GET /installation/repositories
- GET /issues
- GET /networks/{owner}/{repo}/events
- GET /orgs/{org}/actions/permissions/repositories
- GET /orgs/{org}/actions/permissions/self-hosted-runners/repositories
- GET /orgs/{org}/events
- GET /orgs/{org}/issues
- GET /orgs/{org}/migrations
- GET /orgs/{org}/migrations/{migration_id}
- GET /repos/{owner}/{repo}
- GET /repos/{owner}/{repo}/commits/{commit_sha}/pulls
- GET /repos/{owner}/{repo}/events
- GET /repos/{owner}/{repo}/issues
- GET /repos/{owner}/{repo}/issues/events
- GET /repos/{owner}/{repo}/issues/events/{event_id}
- GET /repos/{owner}/{repo}/issues/{issue_number}
- GET /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by
- GET /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocking
- GET /repos/{owner}/{repo}/issues/{issue_number}/parent
- GET /repos/{owner}/{repo}/issues/{issue_number}/sub_issues
- GET /repos/{owner}/{repo}/issues/{issue_number}/timeline
- GET /repos/{owner}/{repo}/pulls
- GET /repos/{owner}/{repo}/pulls/{pull_number}
- GET /search/issues
- GET /teams/{team_id}/repos/{owner}/{repo}
- GET /user/installations/{installation_id}/repositories
- GET /user/issues
- GET /user/migrations
- GET /user/migrations/{migration_id}
- GET /user/repos
- GET /user/starred
- GET /users/{username}/events
- GET /users/{username}/events/orgs/{org}
- GET /users/{username}/events/public
- GET /users/{username}/received_events
- GET /users/{username}/received_events/public
- GET /users/{username}/starred
- PATCH /repos/{owner}/{repo}
- PATCH /repos/{owner}/{repo}/issues/{issue_number}
- PATCH /repos/{owner}/{repo}/issues/{issue_number}/sub_issues/priority
- PATCH /repos/{owner}/{repo}/pulls/{pull_number}
- POST /app/installations/{installation_id}/access_tokens
- POST /enterprises/{enterprise}/actions/runners/registration-token
- POST /enterprises/{enterprise}/actions/runners/remove-token
- POST /orgs/{org}/actions/runners/registration-token
- POST /orgs/{org}/actions/runners/remove-token
- POST /orgs/{org}/migrations
- POST /orgs/{org}/projectsV2/{project_number}/drafts
- POST /orgs/{org}/projectsV2/{project_number}/items
- POST /orgs/{org}/repos
- POST /repos/{owner}/{repo}/actions/runners/registration-token
- POST /repos/{owner}/{repo}/actions/runners/remove-token
- POST /repos/{owner}/{repo}/forks
- POST /repos/{owner}/{repo}/issues
- POST /repos/{owner}/{repo}/issues/{issue_number}/assignees
- POST /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by
- POST /repos/{owner}/{repo}/issues/{issue_number}/sub_issues
- POST /repos/{owner}/{repo}/pulls
- POST /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers
- POST /repos/{owner}/{repo}/security-advisories/{ghsa_id}/forks
- POST /repos/{template_owner}/{template_repo}/generate
- POST /user/codespaces/{codespace_name}/publish
- POST /user/migrations
- POST /user/repos
- POST /user/{user_id}/projectsV2/{project_number}/drafts
- POST /users/{username}/projectsV2/{project_number}/items

```
authorizations_url
```
- GET /
- emailsresponse as a flat array of strings instead of email objects
- pull_requestresponse property withnulldefault values
- userresponse property, replaced byowner
- master_branchresponse property, replaced bydefault_branch
- DELETE /repos/{owner}/{repo}/issues/{issue_number}/assignees
- DELETE /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by/{issue_id}
- DELETE /repos/{owner}/{repo}/issues/{issue_number}/sub_issue
- DELETE /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers
- GET /events
- GET /gists
- GET /gists/public
- GET /gists/starred
- GET /installation/repositories
- GET /issues
- GET /networks/{owner}/{repo}/events
- GET /orgs/{org}/actions/permissions/repositories
- GET /orgs/{org}/actions/permissions/self-hosted-runners/repositories
- GET /orgs/{org}/events
- GET /orgs/{org}/issues
- GET /orgs/{org}/migrations
- GET /orgs/{org}/migrations/{migration_id}
- GET /repos/{owner}/{repo}
- GET /repos/{owner}/{repo}/commits/{commit_sha}/pulls
- GET /repos/{owner}/{repo}/events
- GET /repos/{owner}/{repo}/issues
- GET /repos/{owner}/{repo}/issues/events
- GET /repos/{owner}/{repo}/issues/events/{event_id}
- GET /repos/{owner}/{repo}/issues/{issue_number}
- GET /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by
- GET /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocking
- GET /repos/{owner}/{repo}/issues/{issue_number}/parent
- GET /repos/{owner}/{repo}/issues/{issue_number}/sub_issues
- GET /repos/{owner}/{repo}/issues/{issue_number}/timeline
- GET /repos/{owner}/{repo}/pulls
- GET /repos/{owner}/{repo}/pulls/{pull_number}
- GET /search/issues
- GET /teams/{team_id}/repos/{owner}/{repo}
- GET /user/installations/{installation_id}/repositories
- GET /user/issues
- GET /user/migrations
- GET /user/migrations/{migration_id}
- GET /user/repos
- GET /user/starred
- GET /users/{username}/events
- GET /users/{username}/events/orgs/{org}
- GET /users/{username}/events/public
- GET /users/{username}/gists
- GET /users/{username}/received_events
- GET /users/{username}/received_events/public
- GET /users/{username}/starred
- PATCH /repos/{owner}/{repo}
- PATCH /repos/{owner}/{repo}/issues/{issue_number}
- PATCH /repos/{owner}/{repo}/issues/{issue_number}/sub_issues/priority
- PATCH /repos/{owner}/{repo}/pulls/{pull_number}
- POST /app/installations/{installation_id}/access_tokens
- POST /enterprises/{enterprise}/actions/runners/registration-token
- POST /enterprises/{enterprise}/actions/runners/remove-token
- POST /gists/{gist_id}/forks
- POST /orgs/{org}/actions/runners/registration-token
- POST /orgs/{org}/actions/runners/remove-token
- POST /orgs/{org}/migrations
- POST /orgs/{org}/projectsV2/{project_number}/drafts
- POST /orgs/{org}/projectsV2/{project_number}/items
- POST /orgs/{org}/repos
- POST /repos/{owner}/{repo}/actions/runners/registration-token
- POST /repos/{owner}/{repo}/actions/runners/remove-token
- POST /repos/{owner}/{repo}/forks
- POST /repos/{owner}/{repo}/issues
- POST /repos/{owner}/{repo}/issues/{issue_number}/assignees
- POST /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by
- POST /repos/{owner}/{repo}/issues/{issue_number}/sub_issues
- POST /repos/{owner}/{repo}/pulls
- POST /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers
- POST /repos/{owner}/{repo}/security-advisories/{ghsa_id}/forks
- POST /repos/{template_owner}/{template_repo}/generate
- POST /user/codespaces/{codespace_name}/publish
- POST /user/migrations
- POST /user/repos
- POST /user/{user_id}/projectsV2/{project_number}/drafts
- POST /users/{username}/projectsV2/{project_number}/items
- GET /gists
- GET /gists/public
- GET /gists/starred
- GET /gists/{gist_id}
- GET /gists/{gist_id}/forks
- GET /gists/{gist_id}/{sha}
- GET /users/{username}/gists
- PATCH /gists/{gist_id}
- POST /gists
- POST /gists/{gist_id}/forks
- DELETE /app/installations/{installation_id}

```
secret_scanning_push_protection_custom_link_enabled
```
- GET /orgs/{org}
- PATCH /orgs/{org}

```
javascript-typescript
```

```
codeql-action
```
- GET /repos/{owner}/{repo}/code-scanning/default-setup

```
has_downloads
```
- DELETE /repos/{owner}/{repo}/issues/{issue_number}/assignees
- DELETE /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by/{issue_id}
- DELETE /repos/{owner}/{repo}/issues/{issue_number}/sub_issue
- DELETE /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers
- GET /events
- GET /installation/repositories
- GET /issues
- GET /networks/{owner}/{repo}/events
- GET /notifications
- GET /notifications/threads/{thread_id}
- GET /orgs/{org}/actions/permissions/repositories
- GET /orgs/{org}/actions/permissions/self-hosted-runners/repositories
- GET /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories
- GET /orgs/{org}/actions/secrets/{secret_name}/repositories
- GET /orgs/{org}/actions/variables/{name}/repositories
- GET /orgs/{org}/codespaces
- GET /orgs/{org}/codespaces/secrets/{secret_name}/repositories
- GET /orgs/{org}/dependabot/secrets/{secret_name}/repositories
- GET /orgs/{org}/docker/conflicts
- GET /orgs/{org}/events
- GET /orgs/{org}/issues
- GET /orgs/{org}/members/{username}/codespaces
- GET /orgs/{org}/migrations
- GET /orgs/{org}/migrations/{migration_id}
- GET /orgs/{org}/migrations/{migration_id}/repositories
- GET /orgs/{org}/packages
- GET /orgs/{org}/packages/{package_type}/{package_name}
- GET /orgs/{org}/personal-access-token-requests/{pat_request_id}/repositories
- GET /orgs/{org}/personal-access-tokens/{pat_id}/repositories
- GET /orgs/{org}/repos
- GET /orgs/{org}/settings/immutable-releases/repositories
- GET /orgs/{org}/teams/{team_slug}/repos
- GET /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}
- GET /repos/{owner}/{repo}
- GET /repos/{owner}/{repo}/actions/runs
- GET /repos/{owner}/{repo}/actions/runs/{run_id}
- GET /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}
- GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs
- GET /repos/{owner}/{repo}/check-suites/{check_suite_id}
- GET /repos/{owner}/{repo}/codespaces
- GET /repos/{owner}/{repo}/commits/{commit_sha}/pulls
- GET /repos/{owner}/{repo}/commits/{ref}/check-suites
- GET /repos/{owner}/{repo}/commits/{ref}/status
- GET /repos/{owner}/{repo}/events
- GET /repos/{owner}/{repo}/forks
- GET /repos/{owner}/{repo}/invitations
- GET /repos/{owner}/{repo}/issues
- GET /repos/{owner}/{repo}/issues/events
- GET /repos/{owner}/{repo}/issues/events/{event_id}
- GET /repos/{owner}/{repo}/issues/{issue_number}
- GET /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by
- GET /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocking
- GET /repos/{owner}/{repo}/issues/{issue_number}/parent
- GET /repos/{owner}/{repo}/issues/{issue_number}/sub_issues
- GET /repos/{owner}/{repo}/issues/{issue_number}/timeline
- GET /repos/{owner}/{repo}/notifications
- GET /repos/{owner}/{repo}/pulls
- GET /repos/{owner}/{repo}/pulls/{pull_number}
- GET /repositories
- GET /search/code
- GET /search/commits
- GET /search/issues
- GET /teams/{team_id}/repos
- GET /teams/{team_id}/repos/{owner}/{repo}
- GET /user/codespaces
- GET /user/codespaces/secrets/{secret_name}/repositories
- GET /user/codespaces/{codespace_name}
- GET /user/docker/conflicts
- GET /user/installations/{installation_id}/repositories
- GET /user/issues
- GET /user/migrations
- GET /user/migrations/{migration_id}
- GET /user/migrations/{migration_id}/repositories
- GET /user/packages
- GET /user/packages/{package_type}/{package_name}
- GET /user/repos
- GET /user/repository_invitations
- GET /user/starred
- GET /user/subscriptions
- GET /users/{username}/docker/conflicts
- GET /users/{username}/events
- GET /users/{username}/events/orgs/{org}
- GET /users/{username}/events/public
- GET /users/{username}/packages
- GET /users/{username}/packages/{package_type}/{package_name}
- GET /users/{username}/received_events
- GET /users/{username}/received_events/public
- GET /users/{username}/repos
- GET /users/{username}/starred
- GET /users/{username}/subscriptions
- PATCH /repos/{owner}/{repo}
- PATCH /repos/{owner}/{repo}/check-suites/preferences
- PATCH /repos/{owner}/{repo}/invitations/{invitation_id}
- PATCH /repos/{owner}/{repo}/issues/{issue_number}
- PATCH /repos/{owner}/{repo}/issues/{issue_number}/sub_issues/priority
- PATCH /repos/{owner}/{repo}/pulls/{pull_number}
- PATCH /user/codespaces/{codespace_name}
- POST /app/installations/{installation_id}/access_tokens
- POST /enterprises/{enterprise}/actions/runners/registration-token
- POST /enterprises/{enterprise}/actions/runners/remove-token
- POST /orgs/{org}/actions/runners/registration-token
- POST /orgs/{org}/actions/runners/remove-token
- POST /orgs/{org}/members/{username}/codespaces/{codespace_name}/stop
- POST /orgs/{org}/migrations
- POST /orgs/{org}/projectsV2/{project_number}/drafts
- POST /orgs/{org}/projectsV2/{project_number}/items
- POST /orgs/{org}/repos
- POST /repos/{owner}/{repo}/actions/runners/registration-token
- POST /repos/{owner}/{repo}/actions/runners/remove-token
- POST /repos/{owner}/{repo}/check-suites
- POST /repos/{owner}/{repo}/codespaces
- POST /repos/{owner}/{repo}/forks
- POST /repos/{owner}/{repo}/issues
- POST /repos/{owner}/{repo}/issues/{issue_number}/assignees
- POST /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by
- POST /repos/{owner}/{repo}/issues/{issue_number}/sub_issues
- POST /repos/{owner}/{repo}/pulls
- POST /repos/{owner}/{repo}/pulls/{pull_number}/codespaces
- POST /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers
- POST /repos/{owner}/{repo}/security-advisories/{ghsa_id}/forks
- POST /repos/{owner}/{repo}/transfer
- POST /repos/{template_owner}/{template_repo}/generate
- POST /user/codespaces
- POST /user/codespaces/{codespace_name}/publish
- POST /user/codespaces/{codespace_name}/start
- POST /user/codespaces/{codespace_name}/stop
- POST /user/migrations
- POST /user/repos
- POST /user/{user_id}/projectsV2/{project_number}/drafts
- POST /users/{username}/projectsV2/{project_number}/items
- PUT /repos/{owner}/{repo}/collaborators/{username}
- POST /orgs/{org}/repos
- POST /user/repos
- DELETE /orgs/{org}
- DELETE /orgs/{org}/members/{username}
- PUT /orgs/{org}/memberships/{username}
- PATCH /user/repository_invitations/{invitation_id}
- GET /

```
cvss_severities
```
- GET /advisories
- GET /advisories/{ghsa_id}
- GET /enterprises/{enterprise}/dependabot/alerts
- GET /orgs/{org}/dependabot/alerts
- GET /orgs/{org}/security-advisories
- GET /repos/{owner}/{repo}/dependabot/alerts
- GET /repos/{owner}/{repo}/dependabot/alerts/{alert_number}
- GET /repos/{owner}/{repo}/security-advisories
- GET /repos/{owner}/{repo}/security-advisories/{ghsa_id}
- PATCH /repos/{owner}/{repo}/dependabot/alerts/{alert_number}
- PATCH /repos/{owner}/{repo}/security-advisories/{ghsa_id}
- POST /repos/{owner}/{repo}/security-advisories
- POST /repos/{owner}/{repo}/security-advisories/reports
- GET /orgs/{org}/migrations
- GET /orgs/{org}/migrations/{migration_id}
- GET /orgs/{org}/migrations/{migration_id}/repositories
- GET /user/migrations
- GET /user/migrations/{migration_id}
- GET /user/migrations/{migration_id}/repositories
- POST /orgs/{org}/migrations
- POST /user/migrations

```
merge_commit_sha
```
- DELETE /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers
- GET /events
- GET /networks/{owner}/{repo}/events
- GET /orgs/{org}/events
- GET /repos/{owner}/{repo}/commits/{commit_sha}/pulls
- GET /repos/{owner}/{repo}/events
- GET /repos/{owner}/{repo}/pulls
- GET /repos/{owner}/{repo}/pulls/{pull_number}
- GET /users/{username}/events
- GET /users/{username}/events/orgs/{org}
- GET /users/{username}/events/public
- GET /users/{username}/received_events
- GET /users/{username}/received_events/public
- PATCH /repos/{owner}/{repo}/pulls/{pull_number}
- POST /orgs/{org}/projectsV2/{project_number}/drafts
- POST /orgs/{org}/projectsV2/{project_number}/items
- POST /repos/{owner}/{repo}/pulls
- POST /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers
- POST /user/{user_id}/projectsV2/{project_number}/drafts
- POST /users/{username}/projectsV2/{project_number}/items
- POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches
- Use theassigneesarray parameter instead of the singularassigneeparameter when creating or updating Issues.
- Read assignee information from theassigneesarray instead of the singularassigneeproperty in Issue and Pull Request responses.
- DELETE /repos/{owner}/{repo}/issues/{issue_number}/assignees
- DELETE /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by/{issue_id}
- DELETE /repos/{owner}/{repo}/issues/{issue_number}/sub_issue
- DELETE /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers
- GET /events
- GET /issues
- GET /networks/{owner}/{repo}/events
- GET /orgs/{org}/events
- GET /orgs/{org}/issues
- GET /repos/{owner}/{repo}/commits/{commit_sha}/pulls
- GET /repos/{owner}/{repo}/events
- GET /repos/{owner}/{repo}/issues
- GET /repos/{owner}/{repo}/issues/events
- GET /repos/{owner}/{repo}/issues/events/{event_id}
- GET /repos/{owner}/{repo}/issues/{issue_number}
- GET /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by
- GET /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocking
- GET /repos/{owner}/{repo}/issues/{issue_number}/parent
- GET /repos/{owner}/{repo}/issues/{issue_number}/sub_issues
- GET /repos/{owner}/{repo}/issues/{issue_number}/timeline
- GET /repos/{owner}/{repo}/pulls
- GET /repos/{owner}/{repo}/pulls/{pull_number}
- GET /search/issues
- GET /user/issues
- GET /users/{username}/events
- GET /users/{username}/events/orgs/{org}
- GET /users/{username}/events/public
- GET /users/{username}/received_events
- GET /users/{username}/received_events/public
- PATCH /repos/{owner}/{repo}/issues/{issue_number}
- PATCH /repos/{owner}/{repo}/issues/{issue_number}/sub_issues/priority
- PATCH /repos/{owner}/{repo}/pulls/{pull_number}
- POST /orgs/{org}/projectsV2/{project_number}/drafts
- POST /orgs/{org}/projectsV2/{project_number}/items
- POST /repos/{owner}/{repo}/issues
- POST /repos/{owner}/{repo}/issues/{issue_number}/assignees
- POST /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by
- POST /repos/{owner}/{repo}/issues/{issue_number}/sub_issues
- POST /repos/{owner}/{repo}/pulls
- POST /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers
- POST /user/{user_id}/projectsV2/{project_number}/drafts
- POST /users/{username}/projectsV2/{project_number}/items

```
selected_repository_ids
```
- PUT /orgs/{org}/dependabot/secrets/{secret_name}
- GET /orgs/{org}/attestations/{subject_digest}
- GET /repos/{owner}/{repo}/attestations/{subject_digest}
- GET /users/{username}/attestations/{subject_digest}
- POST /orgs/{org}/attestations/bulk-list
- POST /users/{username}/attestations/bulk-list

## Version 2022-11-28
Version2022-11-28is the first version of the GitHub Free, Pro & Team REST API after date-based versioning was introduced. This version does not include any breaking changes.