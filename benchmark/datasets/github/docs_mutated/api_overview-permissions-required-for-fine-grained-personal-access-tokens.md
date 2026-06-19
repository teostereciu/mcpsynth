# Permissions required for fine-grained personal access tokens

*Source: https://docs.github.com/en/rest/overview/permissions-required-for-fine-grained-personal-access-tokens*

---

# Permissions required for fine-grained personal access tokens
For each permission granted to a fine-grained personal access token, these are the REST API endpoints that the app can use.

## In this article

## About permissions required for fine-grained personal access token
When you create a fine-grained personal access token, you grant it a set of permissions. Permissions define what resources the GitHub App can access via the API. For more information, seeManaging your personal access tokens.
To help you choose the correct permissions, you will receive theX-Accepted-GitHub-Permissionsheader in the REST API response. The header will tell you what permissions are required in order to access the endpoint. For more information, seeTroubleshooting the REST API.
These permissions are required to access private resources. Some endpoints can also be used to access public resources without these permissions. To see whether an endpoint can access public resources without a permission, see the documentation for that endpoint.
Some endpoints require more than one permission. Other endpoints work with any one permission from a set of permissions. In these cases, the "Additional permissions" column will include a checkmark. For full details about the permissions that are required to use the endpoint, see the documentation for that endpoint.

## Organization permissions for "API Insights"

[TABLE]
Endpoint | Access | Additional permissions
GET/orgs/{org}/insights/api/route-stats/{actor_type}/{actor_id} | read | 
GET/orgs/{org}/insights/api/subject-stats | read | 
GET/orgs/{org}/insights/api/summary-stats | read | 
GET/orgs/{org}/insights/api/summary-stats/users/{user_id} | read | 
GET/orgs/{org}/insights/api/summary-stats/{actor_type}/{actor_id} | read | 
GET/orgs/{org}/insights/api/time-stats | read | 
GET/orgs/{org}/insights/api/time-stats/users/{user_id} | read | 
GET/orgs/{org}/insights/api/time-stats/{actor_type}/{actor_id} | read | 
GET/orgs/{org}/insights/api/user-stats/{user_id} | read | 
[/TABLE]

## Organization permissions for "Administration"

[TABLE]
Endpoint | Access | Additional permissions
PUT/organizations/{org}/actions/cache/retention-limit | write | 
PUT/organizations/{org}/actions/cache/storage-limit | write | 
PATCH/organizations/{org}/dependabot/repository-access | write | 
PUT/organizations/{org}/dependabot/repository-access/default-level | write | 
PATCH/organizations/{org}/settings/billing/budgets/{budget_id} | write | 
DELETE/organizations/{org}/settings/billing/budgets/{budget_id} | write | 
PATCH/orgs/{org} | write | 
DELETE/orgs/{org} | write | 
POST/orgs/{org}/actions/hosted-runners | write | 
PATCH/orgs/{org}/actions/hosted-runners/{hosted_runner_id} | write | 
DELETE/orgs/{org}/actions/hosted-runners/{hosted_runner_id} | write | 
POST/orgs/{org}/actions/oidc/customization/properties/repo | write | 
DELETE/orgs/{org}/actions/oidc/customization/properties/repo/{custom_property_name} | write | 
PUT/orgs/{org}/actions/oidc/customization/sub | write | 
PUT/orgs/{org}/actions/permissions | write | 
PUT/orgs/{org}/actions/permissions/artifact-and-log-retention | write | 
PUT/orgs/{org}/actions/permissions/fork-pr-contributor-approval | write | 
PUT/orgs/{org}/actions/permissions/fork-pr-workflows-private-repos | write | 
PUT/orgs/{org}/actions/permissions/repositories | write | 
PUT/orgs/{org}/actions/permissions/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/actions/permissions/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/orgs/{org}/actions/permissions/selected-actions | write | 
PUT/orgs/{org}/actions/permissions/self-hosted-runners | write | 
PUT/orgs/{org}/actions/permissions/self-hosted-runners/repositories | write | 
PUT/orgs/{org}/actions/permissions/self-hosted-runners/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/actions/permissions/self-hosted-runners/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/orgs/{org}/actions/permissions/workflow | write | 
POST/orgs/{org}/code-security/configurations | write | 
DELETE/orgs/{org}/code-security/configurations/detach | write | 
PATCH/orgs/{org}/code-security/configurations/{configuration_id} | write | 
DELETE/orgs/{org}/code-security/configurations/{configuration_id} | write | 
POST/orgs/{org}/code-security/configurations/{configuration_id}/attach | write | 
PUT/orgs/{org}/code-security/configurations/{configuration_id}/defaults | write | 
POST/orgs/{org}/copilot/billing/selected_teams | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/copilot/billing/selected_teams | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/orgs/{org}/copilot/billing/selected_users | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/copilot/billing/selected_users | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/orgs/{org}/interaction-limits | write | 
DELETE/orgs/{org}/interaction-limits | write | 
GET/orgs/{org}/rulesets | write | 
POST/orgs/{org}/rulesets | write | 
GET/orgs/{org}/rulesets/rule-suites | write | 
GET/orgs/{org}/rulesets/rule-suites/{rule_suite_id} | write | 
GET/orgs/{org}/rulesets/{ruleset_id} | write | 
PUT/orgs/{org}/rulesets/{ruleset_id} | write | 
DELETE/orgs/{org}/rulesets/{ruleset_id} | write | 
GET/orgs/{org}/rulesets/{ruleset_id}/history | write | 
GET/orgs/{org}/rulesets/{ruleset_id}/history/{version_id} | write | 
PATCH/orgs/{org}/secret-scanning/pattern-configurations | write | 
PUT/orgs/{org}/security-managers/teams/{team_slug} | write | 
DELETE/orgs/{org}/security-managers/teams/{team_slug} | write | 
PUT/orgs/{org}/settings/immutable-releases | write | 
PUT/orgs/{org}/settings/immutable-releases/repositories | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/orgs/{org}/settings/immutable-releases/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/settings/immutable-releases/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/orgs/{org}/{security_product}/{enablement} | write | 
GET/organizations/{org}/actions/cache/retention-limit | read | 
GET/organizations/{org}/actions/cache/storage-limit | read | 
GET/organizations/{org}/dependabot/repository-access | read | 
GET/organizations/{org}/settings/billing/budgets | read | 
GET/organizations/{org}/settings/billing/budgets/{budget_id} | read | 
GET/organizations/{org}/settings/billing/premium_request/usage | read | 
GET/organizations/{org}/settings/billing/usage | read | 
GET/organizations/{org}/settings/billing/usage/summary | read | 
GET/orgs/{org}/actions/cache/usage | read | 
GET/orgs/{org}/actions/cache/usage-by-repository | read | 
GET/orgs/{org}/actions/hosted-runners | read | 
GET/orgs/{org}/actions/hosted-runners/images/github-owned | read | 
GET/orgs/{org}/actions/hosted-runners/images/partner | read | 
GET/orgs/{org}/actions/hosted-runners/limits | read | 
GET/orgs/{org}/actions/hosted-runners/machine-sizes | read | 
GET/orgs/{org}/actions/hosted-runners/platforms | read | 
GET/orgs/{org}/actions/hosted-runners/{hosted_runner_id} | read | 
GET/orgs/{org}/actions/oidc/customization/properties/repo | read | 
GET/orgs/{org}/actions/oidc/customization/sub | read | 
GET/orgs/{org}/actions/permissions | read | 
GET/orgs/{org}/actions/permissions/artifact-and-log-retention | read | 
GET/orgs/{org}/actions/permissions/fork-pr-contributor-approval | read | 
GET/orgs/{org}/actions/permissions/fork-pr-workflows-private-repos | read | 
GET/orgs/{org}/actions/permissions/repositories | read | 
GET/orgs/{org}/actions/permissions/selected-actions | read | 
GET/orgs/{org}/actions/permissions/self-hosted-runners | read | 
GET/orgs/{org}/actions/permissions/self-hosted-runners/repositories | read | 
GET/orgs/{org}/actions/permissions/workflow | read | 
GET/orgs/{org}/code-security/configurations | read | 
GET/orgs/{org}/code-security/configurations/defaults | read | 
GET/orgs/{org}/code-security/configurations/{configuration_id} | read | 
GET/orgs/{org}/code-security/configurations/{configuration_id}/repositories | read | 
GET/orgs/{org}/copilot/billing | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/copilot/billing/seats | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/copilot/metrics | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/installations | read | 
GET/orgs/{org}/interaction-limits | read | 
GET/orgs/{org}/members/{username}/copilot | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/secret-scanning/pattern-configurations | read | 
GET/orgs/{org}/security-managers | read | 
GET/orgs/{org}/settings/immutable-releases | read | 
GET/orgs/{org}/settings/immutable-releases/repositories | read | 
GET/orgs/{org}/team/{team_slug}/copilot/metrics | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## Organization permissions for "Blocking users"

[TABLE]
Endpoint | Access | Additional permissions
PUT/orgs/{org}/blocks/{username} | write | 
DELETE/orgs/{org}/blocks/{username} | write | 
GET/orgs/{org}/blocks | read | 
GET/orgs/{org}/blocks/{username} | read | 
[/TABLE]

## Organization permissions for "Campaigns"

[TABLE]
Endpoint | Access | Additional permissions
POST/orgs/{org}/campaigns | write | 
PATCH/orgs/{org}/campaigns/{campaign_number} | write | 
DELETE/orgs/{org}/campaigns/{campaign_number} | write | 
GET/orgs/{org}/campaigns | read | 
GET/orgs/{org}/campaigns/{campaign_number} | read | 
[/TABLE]

## Organization permissions for "Copilot agent settings"

[TABLE]
Endpoint | Access | Additional permissions
PUT/orgs/{org}/copilot/coding-agent/permissions | write | 
PUT/orgs/{org}/copilot/coding-agent/permissions/repositories | write | 
PUT/orgs/{org}/copilot/coding-agent/permissions/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/copilot/coding-agent/permissions/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/copilot/coding-agent/permissions | read | 
GET/orgs/{org}/copilot/coding-agent/permissions/repositories | read | 
[/TABLE]

## Organization permissions for "Copilot content exclusion"

[TABLE]
Endpoint | Access | Additional permissions
PUT/orgs/{org}/copilot/content_exclusion | write | 
GET/orgs/{org}/copilot/content_exclusion | read | 
[/TABLE]

## Organization permissions for "Custom organization roles"

[TABLE]
Endpoint | Access | Additional permissions
GET/orgs/{org}/organization-roles | read | 
GET/orgs/{org}/organization-roles/{role_id} | read | 
[/TABLE]

## Organization permissions for "Custom properties"

[TABLE]
Endpoint | Access | Additional permissions
PATCH/orgs/{org}/properties/schema | admin | 
PUT/orgs/{org}/properties/schema/{custom_property_name} | admin | 
DELETE/orgs/{org}/properties/schema/{custom_property_name} | admin | 
PATCH/orgs/{org}/properties/values | write | 
GET/orgs/{org}/properties/schema | read | 
GET/orgs/{org}/properties/schema/{custom_property_name} | read | 
GET/orgs/{org}/properties/values | read | 
[/TABLE]

## Organization permissions for "Events"

[TABLE]
Endpoint | Access | Additional permissions
GET/users/{username}/events/orgs/{org} | read | 
[/TABLE]

## Organization permissions for "GitHub Copilot Business"

[TABLE]
Endpoint | Access | Additional permissions
POST/orgs/{org}/copilot/billing/selected_teams | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/copilot/billing/selected_teams | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/orgs/{org}/copilot/billing/selected_users | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/copilot/billing/selected_users | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/copilot/billing | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/copilot/billing/seats | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/copilot/metrics | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/members/{username}/copilot | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/team/{team_slug}/copilot/metrics | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## Organization permissions for "Hosted runner custom images"

[TABLE]
Endpoint | Access | Additional permissions
DELETE/orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id} | write | 
DELETE/orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id}/versions/{version} | write | 
GET/orgs/{org}/actions/hosted-runners/images/custom | read | 
GET/orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id} | read | 
GET/orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id}/versions | read | 
GET/orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id}/versions/{version} | read | 
[/TABLE]

## Organization permissions for "Issue Fields"

[TABLE]
Endpoint | Access | Additional permissions
POST/orgs/{org}/issue-fields | write | 
PATCH/orgs/{org}/issue-fields/{issue_field_id} | write | 
DELETE/orgs/{org}/issue-fields/{issue_field_id} | write | 
GET/orgs/{org}/issue-fields | read | 
[/TABLE]

## Organization permissions for "Issue Types"

[TABLE]
Endpoint | Access | Additional permissions
POST/orgs/{org}/issue-types | write | 
PUT/orgs/{org}/issue-types/{issue_type_id} | write | 
DELETE/orgs/{org}/issue-types/{issue_type_id} | write | 
GET/orgs/{org}/issue-types | read | 
[/TABLE]

## Organization permissions for "Members"

[TABLE]
Endpoint | Access | Additional permissions
POST/orgs/{org}/invitations | write | 
DELETE/orgs/{org}/invitations/{invitation_id} | write | 
DELETE/orgs/{org}/members/{username} | write | 
PUT/orgs/{org}/memberships/{username} | write | 
DELETE/orgs/{org}/memberships/{username} | write | 
DELETE/orgs/{org}/organization-roles/teams/{team_slug} | write | 
PUT/orgs/{org}/organization-roles/teams/{team_slug}/{role_id} | write | 
DELETE/orgs/{org}/organization-roles/teams/{team_slug}/{role_id} | write | 
DELETE/orgs/{org}/organization-roles/users/{username} | write | 
PUT/orgs/{org}/organization-roles/users/{username}/{role_id} | write | 
DELETE/orgs/{org}/organization-roles/users/{username}/{role_id} | write | 
PUT/orgs/{org}/outside_collaborators/{username} | write | 
DELETE/orgs/{org}/outside_collaborators/{username} | write | 
PUT/orgs/{org}/public_members/{username} | write | 
DELETE/orgs/{org}/public_members/{username} | write | 
POST/orgs/{org}/teams | write | 
PATCH/orgs/{org}/teams/{team_slug} | write | 
DELETE/orgs/{org}/teams/{team_slug} | write | 
PUT/orgs/{org}/teams/{team_slug}/memberships/{username} | write | 
DELETE/orgs/{org}/teams/{team_slug}/memberships/{username} | write | 
PATCH/teams/{team_id} | write | 
DELETE/teams/{team_id} | write | 
PUT/teams/{team_id}/members/{username} | write | 
DELETE/teams/{team_id}/members/{username} | write | 
PUT/teams/{team_id}/memberships/{username} | write | 
DELETE/teams/{team_id}/memberships/{username} | write | 
PATCH/user/memberships/orgs/{org} | write | 
GET/orgs/{org}/failed_invitations | read | 
GET/orgs/{org}/invitations | read | 
GET/orgs/{org}/invitations/{invitation_id}/teams | read | 
GET/orgs/{org}/members | read | 
GET/orgs/{org}/members/{username} | read | 
GET/orgs/{org}/memberships/{username} | read | 
GET/orgs/{org}/organization-roles/{role_id}/teams | read | 
GET/orgs/{org}/organization-roles/{role_id}/users | read | 
GET/orgs/{org}/outside_collaborators | read | 
GET/orgs/{org}/public_members | read | 
GET/orgs/{org}/public_members/{username} | read | 
GET/orgs/{org}/teams | read | 
GET/orgs/{org}/teams/{team_slug} | read | 
GET/orgs/{org}/teams/{team_slug}/invitations | read | 
GET/orgs/{org}/teams/{team_slug}/members | read | 
GET/orgs/{org}/teams/{team_slug}/memberships/{username} | read | 
GET/orgs/{org}/teams/{team_slug}/repos | read | 
GET/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/teams/{team_slug}/teams | read | 
GET/teams/{team_id} | read | 
GET/teams/{team_id}/invitations | read | 
GET/teams/{team_id}/members | read | 
GET/teams/{team_id}/members/{username} | read | 
GET/teams/{team_id}/memberships/{username} | read | 
GET/teams/{team_id}/repos | read | 
GET/teams/{team_id}/repos/{owner}/{repo} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/teams/{team_id}/repos/{owner}/{repo} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/teams/{team_id}/repos/{owner}/{repo} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/teams/{team_id}/teams | read | 
GET/user/memberships/orgs/{org} | read | 
[/TABLE]

## Organization permissions for "Network configurations"

[TABLE]
Endpoint | Access | Additional permissions
POST/orgs/{org}/settings/network-configurations | write | 
PATCH/orgs/{org}/settings/network-configurations/{network_configuration_id} | write | 
DELETE/orgs/{org}/settings/network-configurations/{network_configuration_id} | write | 
GET/orgs/{org}/settings/network-configurations | read | 
GET/orgs/{org}/settings/network-configurations/{network_configuration_id} | read | 
GET/orgs/{org}/settings/network-settings/{network_settings_id} | read | 
[/TABLE]

## Organization permissions for "Organization codespaces secrets"

[TABLE]
Endpoint | Access | Additional permissions
PUT/orgs/{org}/codespaces/secrets/{secret_name} | write | 
DELETE/orgs/{org}/codespaces/secrets/{secret_name} | write | 
PUT/orgs/{org}/codespaces/secrets/{secret_name}/repositories | write | 
PUT/orgs/{org}/codespaces/secrets/{secret_name}/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/codespaces/secrets/{secret_name}/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/codespaces/secrets | read | 
GET/orgs/{org}/codespaces/secrets/public-key | read | 
GET/orgs/{org}/codespaces/secrets/{secret_name} | read | 
GET/orgs/{org}/codespaces/secrets/{secret_name}/repositories | read | 
[/TABLE]

## Organization permissions for "Organization codespaces settings"

[TABLE]
Endpoint | Access | Additional permissions
PUT/orgs/{org}/codespaces/access | write | 
POST/orgs/{org}/codespaces/access/selected_users | write | 
DELETE/orgs/{org}/codespaces/access/selected_users | write | 
[/TABLE]

## Organization permissions for "Organization codespaces"

[TABLE]
Endpoint | Access | Additional permissions
DELETE/orgs/{org}/members/{username}/codespaces/{codespace_name} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/orgs/{org}/members/{username}/codespaces/{codespace_name}/stop | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/codespaces | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/members/{username}/codespaces | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## Organization permissions for "Organization dependabot secrets"

[TABLE]
Endpoint | Access | Additional permissions
PUT/orgs/{org}/dependabot/secrets/{secret_name} | write | 
DELETE/orgs/{org}/dependabot/secrets/{secret_name} | write | 
PUT/orgs/{org}/dependabot/secrets/{secret_name}/repositories | write | 
PUT/orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/dependabot/secrets | read | 
GET/orgs/{org}/dependabot/secrets/public-key | read | 
GET/orgs/{org}/dependabot/secrets/{secret_name} | read | 
GET/orgs/{org}/dependabot/secrets/{secret_name}/repositories | read | 
[/TABLE]

## Organization permissions for "Organization private registries"

[TABLE]
Endpoint | Access | Additional permissions
POST/orgs/{org}/private-registries | write | 
PATCH/orgs/{org}/private-registries/{secret_name} | write | 
DELETE/orgs/{org}/private-registries/{secret_name} | write | 
GET/orgs/{org}/private-registries | read | 
GET/orgs/{org}/private-registries/public-key | read | 
GET/orgs/{org}/private-registries/{secret_name} | read | 
[/TABLE]

## Organization permissions for "Projects"

[TABLE]
Endpoint | Access | Additional permissions
POST/orgs/{org}/projectsV2/{project_number}/drafts | write | 
POST/orgs/{org}/projectsV2/{project_number}/fields | write | 
POST/orgs/{org}/projectsV2/{project_number}/items | write | 
PATCH/orgs/{org}/projectsV2/{project_number}/items/{item_id} | write | 
DELETE/orgs/{org}/projectsV2/{project_number}/items/{item_id} | write | 
POST/orgs/{org}/projectsV2/{project_number}/views | write | 
GET/orgs/{org}/projectsV2 | read | 
GET/orgs/{org}/projectsV2/{project_number} | read | 
GET/orgs/{org}/projectsV2/{project_number}/fields | read | 
GET/orgs/{org}/projectsV2/{project_number}/fields/{field_id} | read | 
GET/orgs/{org}/projectsV2/{project_number}/items | read | 
GET/orgs/{org}/projectsV2/{project_number}/items/{item_id} | read | 
GET/orgs/{org}/projectsV2/{project_number}/views/{view_number}/items | read | 
[/TABLE]

## Organization permissions for "Secrets"

[TABLE]
Endpoint | Access | Additional permissions
PUT/orgs/{org}/actions/secrets/{secret_name} | write | 
DELETE/orgs/{org}/actions/secrets/{secret_name} | write | 
PUT/orgs/{org}/actions/secrets/{secret_name}/repositories | write | 
PUT/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/actions/secrets | read | 
GET/orgs/{org}/actions/secrets/public-key | read | 
GET/orgs/{org}/actions/secrets/{secret_name} | read | 
GET/orgs/{org}/actions/secrets/{secret_name}/repositories | read | 
[/TABLE]

## Organization permissions for "Self-hosted runners"

[TABLE]
Endpoint | Access | Additional permissions
POST/orgs/{org}/actions/runner-groups | write | 
PATCH/orgs/{org}/actions/runner-groups/{runner_group_id} | write | 
DELETE/orgs/{org}/actions/runner-groups/{runner_group_id} | write | 
PUT/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories | write | 
PUT/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/orgs/{org}/actions/runner-groups/{runner_group_id}/runners | write | 
PUT/orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id} | write | 
DELETE/orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id} | write | 
POST/orgs/{org}/actions/runners/generate-jitconfig | write | 
POST/orgs/{org}/actions/runners/registration-token | write | 
POST/orgs/{org}/actions/runners/remove-token | write | 
DELETE/orgs/{org}/actions/runners/{runner_id} | write | 
POST/orgs/{org}/actions/runners/{runner_id}/label_filters | write | 
PUT/orgs/{org}/actions/runners/{runner_id}/label_filters | write | 
DELETE/orgs/{org}/actions/runners/{runner_id}/label_filters | write | 
DELETE/orgs/{org}/actions/runners/{runner_id}/label_filters/{name} | write | 
GET/orgs/{org}/actions/runner-groups | read | 
GET/orgs/{org}/actions/runner-groups/{runner_group_id} | read | 
GET/orgs/{org}/actions/runner-groups/{runner_group_id}/hosted-runners | read | 
GET/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories | read | 
GET/orgs/{org}/actions/runner-groups/{runner_group_id}/runners | read | 
GET/orgs/{org}/actions/runners | read | 
GET/orgs/{org}/actions/runners/downloads | read | 
GET/orgs/{org}/actions/runners/{runner_id} | read | 
GET/orgs/{org}/actions/runners/{runner_id}/label_filters | read | 
[/TABLE]

## Organization permissions for "Variables"

[TABLE]
Endpoint | Access | Additional permissions
POST/orgs/{org}/actions/variables | write | 
PATCH/orgs/{org}/actions/variables/{name} | write | 
DELETE/orgs/{org}/actions/variables/{name} | write | 
PUT/orgs/{org}/actions/variables/{name}/repositories | write | 
PUT/orgs/{org}/actions/variables/{name}/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/actions/variables/{name}/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/actions/variables | read | 
GET/orgs/{org}/actions/variables/{name} | read | 
GET/orgs/{org}/actions/variables/{name}/repositories | read | 
[/TABLE]

## Organization permissions for "Webhooks"

[TABLE]
Endpoint | Access | Additional permissions
POST/orgs/{org}/hooks | write | 
PATCH/orgs/{org}/hooks/{hook_id} | write | 
DELETE/orgs/{org}/hooks/{hook_id} | write | 
PATCH/orgs/{org}/hooks/{hook_id}/config | write | 
POST/orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}/attempts | write | 
POST/orgs/{org}/hooks/{hook_id}/pings | write | 
GET/orgs/{org}/hooks | read | 
GET/orgs/{org}/hooks/{hook_id} | read | 
GET/orgs/{org}/hooks/{hook_id}/config | read | 
GET/orgs/{org}/hooks/{hook_id}/deliveries | read | 
GET/orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id} | read | 
[/TABLE]

## Repository permissions for "Actions"

[TABLE]
Endpoint | Access | Additional permissions
DELETE/repos/{owner}/{repo}/actions/artifacts/{artifact_id} | write | 
DELETE/repos/{owner}/{repo}/actions/caches | write | 
DELETE/repos/{owner}/{repo}/actions/caches/{cache_id} | write | 
POST/repos/{owner}/{repo}/actions/jobs/{job_id}/rerun | write | 
PUT/repos/{owner}/{repo}/actions/oidc/customization/sub | write | 
DELETE/repos/{owner}/{repo}/actions/runs/{run_id} | write | 
POST/repos/{owner}/{repo}/actions/runs/{run_id}/approve | write | 
POST/repos/{owner}/{repo}/actions/runs/{run_id}/cancel | write | 
POST/repos/{owner}/{repo}/actions/runs/{run_id}/force-cancel | write | 
DELETE/repos/{owner}/{repo}/actions/runs/{run_id}/logs | write | 
POST/repos/{owner}/{repo}/actions/runs/{run_id}/rerun | write | 
POST/repos/{owner}/{repo}/actions/runs/{run_id}/rerun-failed-jobs | write | 
PUT/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable | write | 
POST/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches | write | 
PUT/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable | write | 
GET/repos/{owner}/{repo}/actions/artifacts | read | 
GET/repos/{owner}/{repo}/actions/artifacts/{artifact_id} | read | 
GET/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format} | read | 
GET/repos/{owner}/{repo}/actions/cache/storage-limit | read | 
GET/repos/{owner}/{repo}/actions/cache/usage | read | 
GET/repos/{owner}/{repo}/actions/caches | read | 
GET/repos/{owner}/{repo}/actions/jobs/{job_id} | read | 
GET/repos/{owner}/{repo}/actions/jobs/{job_id}/logs | read | 
GET/repos/{owner}/{repo}/actions/oidc/customization/sub | read | 
GET/repos/{owner}/{repo}/actions/runs | read | 
GET/repos/{owner}/{repo}/actions/runs/{run_id} | read | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/approvals | read | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts | read | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number} | read | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs | read | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/logs | read | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/jobs | read | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/logs | read | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments | read | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/timing | read | 
GET/repos/{owner}/{repo}/actions/workflows | read | 
GET/repos/{owner}/{repo}/actions/workflows/{workflow_id} | read | 
GET/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs | read | 
GET/repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing | read | 
GET/repos/{owner}/{repo}/environments | read | 
GET/repos/{owner}/{repo}/environments/{environment_name} | read | 
GET/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies | read | 
GET/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id} | read | 
GET/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules | read | 
GET/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/{protection_rule_id} | read | 
[/TABLE]

## Repository permissions for "Administration"

[TABLE]
Endpoint | Access | Additional permissions
POST/orgs/{org}/repos | write | 
PUT/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo} | write | 
DELETE/repos/{owner}/{repo} | write | 
PUT/repos/{owner}/{repo}/actions/cache/retention-limit | write | 
PUT/repos/{owner}/{repo}/actions/cache/storage-limit | write | 
PUT/repos/{owner}/{repo}/actions/permissions | write | 
PUT/repos/{owner}/{repo}/actions/permissions/access | write | 
PUT/repos/{owner}/{repo}/actions/permissions/artifact-and-log-retention | write | 
PUT/repos/{owner}/{repo}/actions/permissions/fork-pr-contributor-approval | write | 
PUT/repos/{owner}/{repo}/actions/permissions/fork-pr-workflows-private-repos | write | 
PUT/repos/{owner}/{repo}/actions/permissions/selected-actions | write | 
PUT/repos/{owner}/{repo}/actions/permissions/workflow | write | 
POST/repos/{owner}/{repo}/actions/runners/generate-jitconfig | write | 
POST/repos/{owner}/{repo}/actions/runners/registration-token | write | 
POST/repos/{owner}/{repo}/actions/runners/remove-token | write | 
DELETE/repos/{owner}/{repo}/actions/runners/{runner_id} | write | 
POST/repos/{owner}/{repo}/actions/runners/{runner_id}/label_filters | write | 
PUT/repos/{owner}/{repo}/actions/runners/{runner_id}/label_filters | write | 
DELETE/repos/{owner}/{repo}/actions/runners/{runner_id}/label_filters | write | 
DELETE/repos/{owner}/{repo}/actions/runners/{runner_id}/label_filters/{name} | write | 
POST/repos/{owner}/{repo}/autolinks | write | 
DELETE/repos/{owner}/{repo}/autolinks/{autolink_id} | write | 
PUT/repos/{owner}/{repo}/automated-security-fixes | write | 
DELETE/repos/{owner}/{repo}/automated-security-fixes | write | 
PUT/repos/{owner}/{repo}/branches/{branch}/protection | write | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection | write | 
POST/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins | write | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins | write | 
PATCH/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews | write | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews | write | 
POST/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures | write | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures | write | 
PATCH/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks | write | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks | write | 
POST/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | write | 
PUT/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | write | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | write | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/restrictions | write | 
POST/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | write | 
PUT/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | write | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | write | 
POST/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | write | 
PUT/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | write | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | write | 
POST/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | write | 
PUT/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | write | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | write | 
PATCH/repos/{owner}/{repo}/code-scanning/default-setup | write | 
PUT/repos/{owner}/{repo}/collaborators/{username} | write | 
DELETE/repos/{owner}/{repo}/collaborators/{username} | write | 
PUT/repos/{owner}/{repo}/environments/{environment_name} | write | 
DELETE/repos/{owner}/{repo}/environments/{environment_name} | write | 
POST/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies | write | 
PUT/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id} | write | 
DELETE/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id} | write | 
POST/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules | write | 
DELETE/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/{protection_rule_id} | write | 
POST/repos/{owner}/{repo}/forks | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/immutable-releases | write | 
DELETE/repos/{owner}/{repo}/immutable-releases | write | 
PUT/repos/{owner}/{repo}/interaction-limits | write | 
DELETE/repos/{owner}/{repo}/interaction-limits | write | 
PATCH/repos/{owner}/{repo}/invitations/{invitation_id} | write | 
DELETE/repos/{owner}/{repo}/invitations/{invitation_id} | write | 
POST/repos/{owner}/{repo}/keys | write | 
DELETE/repos/{owner}/{repo}/keys/{key_id} | write | 
POST/repos/{owner}/{repo}/pages | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/pages | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/pages | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/pages/health | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/private-vulnerability-reporting | write | 
DELETE/repos/{owner}/{repo}/private-vulnerability-reporting | write | 
POST/repos/{owner}/{repo}/rulesets | write | 
PUT/repos/{owner}/{repo}/rulesets/{ruleset_id} | write | 
DELETE/repos/{owner}/{repo}/rulesets/{ruleset_id} | write | 
GET/repos/{owner}/{repo}/rulesets/{ruleset_id}/history | write | 
GET/repos/{owner}/{repo}/rulesets/{ruleset_id}/history/{version_id} | write | 
POST/repos/{owner}/{repo}/security-advisories/{ghsa_id}/forks | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/topics | write | 
PUT/repos/{owner}/{repo}/vulnerability-alerts | write | 
DELETE/repos/{owner}/{repo}/vulnerability-alerts | write | 
POST/repos/{template_owner}/{template_repo}/generate | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/teams/{team_id}/repos/{owner}/{repo} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/teams/{team_id}/repos/{owner}/{repo} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/user/repos | write | 
DELETE/user/repository_invitations/{invitation_id} | write | 
GET/repos/{owner}/{repo}/actions/cache/retention-limit | read | 
GET/repos/{owner}/{repo}/actions/permissions | read | 
GET/repos/{owner}/{repo}/actions/permissions/access | read | 
GET/repos/{owner}/{repo}/actions/permissions/artifact-and-log-retention | read | 
GET/repos/{owner}/{repo}/actions/permissions/fork-pr-contributor-approval | read | 
GET/repos/{owner}/{repo}/actions/permissions/fork-pr-workflows-private-repos | read | 
GET/repos/{owner}/{repo}/actions/permissions/selected-actions | read | 
GET/repos/{owner}/{repo}/actions/permissions/workflow | read | 
GET/repos/{owner}/{repo}/actions/runners | read | 
GET/repos/{owner}/{repo}/actions/runners/downloads | read | 
GET/repos/{owner}/{repo}/actions/runners/{runner_id} | read | 
GET/repos/{owner}/{repo}/actions/runners/{runner_id}/label_filters | read | 
GET/repos/{owner}/{repo}/autolinks | read | 
GET/repos/{owner}/{repo}/autolinks/{autolink_id} | read | 
GET/repos/{owner}/{repo}/automated-security-fixes | read | 
GET/repos/{owner}/{repo}/branches/{branch}/protection | read | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins | read | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews | read | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures | read | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks | read | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | read | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/restrictions | read | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | read | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | read | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | read | 
GET/repos/{owner}/{repo}/code-scanning/default-setup | read | 
GET/repos/{owner}/{repo}/code-security-configuration | read | 
GET/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/apps | read | 
GET/repos/{owner}/{repo}/immutable-releases | read | 
GET/repos/{owner}/{repo}/interaction-limits | read | 
GET/repos/{owner}/{repo}/invitations | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/keys | read | 
GET/repos/{owner}/{repo}/keys/{key_id} | read | 
GET/repos/{owner}/{repo}/rulesets/rule-suites | read | 
GET/repos/{owner}/{repo}/rulesets/rule-suites/{rule_suite_id} | read | 
GET/repos/{owner}/{repo}/teams | read | 
GET/repos/{owner}/{repo}/traffic/clones | read | 
GET/repos/{owner}/{repo}/traffic/popular/paths | read | 
GET/repos/{owner}/{repo}/traffic/popular/referrers | read | 
GET/repos/{owner}/{repo}/traffic/views | read | 
GET/repos/{owner}/{repo}/vulnerability-alerts | read | 
GET/user/repository_invitations | read | 
[/TABLE]

## Repository permissions for "Artifact metadata"

[TABLE]
Endpoint | Access | Additional permissions
POST/orgs/{org}/artifacts/metadata/deployment-record | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/orgs/{org}/artifacts/metadata/deployment-record/cluster/{cluster} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/orgs/{org}/artifacts/metadata/storage-record | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/artifacts/{subject_digest}/metadata/deployment-records | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/artifacts/{subject_digest}/metadata/storage-records | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## Repository permissions for "Attestations"

[TABLE]
Endpoint | Access | Additional permissions
POST/orgs/{org}/attestations/delete-request | write | 
DELETE/orgs/{org}/attestations/digest/{subject_digest} | write | 
DELETE/orgs/{org}/attestations/{attestation_id} | write | 
POST/repos/{owner}/{repo}/attestations | write | 
POST/users/{username}/attestations/delete-request | write | 
DELETE/users/{username}/attestations/digest/{subject_digest} | write | 
DELETE/users/{username}/attestations/{attestation_id} | write | 
GET/orgs/{org}/attestations/repositories | read | 
GET/repos/{owner}/{repo}/attestations/{subject_digest} | read | 
[/TABLE]

## Repository permissions for "Code scanning alerts"

[TABLE]
Endpoint | Access | Additional permissions
PATCH/repos/{owner}/{repo}/code-scanning/alerts/{alert_number} | write | 
POST/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix | write | 
DELETE/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id} | write | 
POST/repos/{owner}/{repo}/code-scanning/sarifs | write | 
GET/orgs/{org}/code-scanning/alerts | read | 
GET/repos/{owner}/{repo}/code-scanning/alerts | read | 
GET/repos/{owner}/{repo}/code-scanning/alerts/{alert_number} | read | 
GET/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix | read | 
GET/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances | read | 
GET/repos/{owner}/{repo}/code-scanning/analyses | read | 
GET/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id} | read | 
GET/repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id} | read | 
[/TABLE]

## Repository permissions for "Codespaces lifecycle admin"

[TABLE]
Endpoint | Access | Additional permissions
POST/orgs/{org}/members/{username}/codespaces/{codespace_name}/stop | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/user/codespaces/{codespace_name}/exports | write | 
POST/user/codespaces/{codespace_name}/start | write | 
POST/user/codespaces/{codespace_name}/stop | write | 
GET/user/codespaces/{codespace_name}/exports/{export_id} | read | 
[/TABLE]

## Repository permissions for "Codespaces metadata"

[TABLE]
Endpoint | Access | Additional permissions
GET/repos/{owner}/{repo}/codespaces/devcontainers | read | 
GET/repos/{owner}/{repo}/codespaces/machines | read | 
GET/user/codespaces/{codespace_name}/machines | read | 
[/TABLE]

## Repository permissions for "Codespaces secrets"

[TABLE]
Endpoint | Access | Additional permissions
GET/repos/{owner}/{repo}/codespaces/secrets | write | 
GET/repos/{owner}/{repo}/codespaces/secrets/public-key | write | 
GET/repos/{owner}/{repo}/codespaces/secrets/{secret_name} | write | 
PUT/repos/{owner}/{repo}/codespaces/secrets/{secret_name} | write | 
DELETE/repos/{owner}/{repo}/codespaces/secrets/{secret_name} | write | 
[/TABLE]

## Repository permissions for "Codespaces"

[TABLE]
Endpoint | Access | Additional permissions
DELETE/orgs/{org}/members/{username}/codespaces/{codespace_name} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/codespaces | write | 
GET/repos/{owner}/{repo}/codespaces/new | write | 
GET/repos/{owner}/{repo}/codespaces/permissions_check | write | 
POST/repos/{owner}/{repo}/pulls/{pull_number}/codespaces | write | 
POST/user/codespaces | write | 
PATCH/user/codespaces/{codespace_name} | write | 
DELETE/user/codespaces/{codespace_name} | write | 
POST/user/codespaces/{codespace_name}/publish | write | 
GET/orgs/{org}/codespaces | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/members/{username}/codespaces | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/codespaces | read | 
GET/user/codespaces | read | 
GET/user/codespaces/{codespace_name} | read | 
[/TABLE]

## Repository permissions for "Commit statuses"

[TABLE]
Endpoint | Access | Additional permissions
POST/repos/{owner}/{repo}/statuses/{commit_sha} | write | 
GET/repos/{owner}/{repo}/commits/{ref}/status | read | 
GET/repos/{owner}/{repo}/commits/{ref}/statuses | read | 
[/TABLE]

## Repository permissions for "Contents"

[TABLE]
Endpoint | Access | Additional permissions
POST/orgs/{org}/artifacts/metadata/deployment-record | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/orgs/{org}/artifacts/metadata/deployment-record/cluster/{cluster} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/orgs/{org}/artifacts/metadata/storage-record | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/branches/{branch}/rename | write | 
POST/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix/commits | write | 
DELETE/repos/{owner}/{repo}/code-scanning/codeql/databases/{language} | write | 
POST/repos/{owner}/{repo}/code-scanning/codeql/variant-analyses | write | 
PATCH/repos/{owner}/{repo}/comments/{comment_id} | write | 
DELETE/repos/{owner}/{repo}/comments/{comment_id} | write | 
POST/repos/{owner}/{repo}/comments/{comment_id}/reactions | write | 
DELETE/repos/{owner}/{repo}/comments/{comment_id}/reactions/{reaction_id} | write | 
PUT/repos/{owner}/{repo}/contents/{path} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/contents/{path} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/contents/{path} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/contents/{path} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/dependency-graph/snapshots | write | 
POST/repos/{owner}/{repo}/dispatches | write | 
POST/repos/{owner}/{repo}/git/blobs | write | 
POST/repos/{owner}/{repo}/git/commits | write | 
POST/repos/{owner}/{repo}/git/refs | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/git/refs | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/git/refs/{ref} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/git/refs/{ref} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/git/refs/{ref} | write | 
POST/repos/{owner}/{repo}/git/tags | write | 
POST/repos/{owner}/{repo}/git/trees | write | 
PUT/repos/{owner}/{repo}/import | write | 
PATCH/repos/{owner}/{repo}/import | write | 
DELETE/repos/{owner}/{repo}/import | write | 
PATCH/repos/{owner}/{repo}/import/authors/{author_id} | write | 
PATCH/repos/{owner}/{repo}/import/lfs | write | 
POST/repos/{owner}/{repo}/merge-upstream | write | 
POST/repos/{owner}/{repo}/merges | write | 
PUT/repos/{owner}/{repo}/pulls/{pull_number}/merge | write | 
POST/repos/{owner}/{repo}/releases | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/releases | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/releases/assets/{asset_id} | write | 
DELETE/repos/{owner}/{repo}/releases/assets/{asset_id} | write | 
POST/repos/{owner}/{repo}/releases/generate-notes | write | 
PATCH/repos/{owner}/{repo}/releases/{release_id} | write | 
DELETE/repos/{owner}/{repo}/releases/{release_id} | write | 
POST/repos/{owner}/{repo}/secret-scanning/push-protection-bypasses | write | 
POST/markdown | read | 
GET/orgs/{org}/artifacts/{subject_digest}/metadata/deployment-records | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/artifacts/{subject_digest}/metadata/storage-records | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/activity | read | 
GET/repos/{owner}/{repo}/branches | read | 
GET/repos/{owner}/{repo}/branches/{branch} | read | 
GET/repos/{owner}/{repo}/code-scanning/codeql/databases | read | 
GET/repos/{owner}/{repo}/code-scanning/codeql/databases/{language} | read | 
GET/repos/{owner}/{repo}/code-scanning/codeql/variant-analyses/{codeql_variant_analysis_id} | read | 
GET/repos/{owner}/{repo}/code-scanning/codeql/variant-analyses/{codeql_variant_analysis_id}/repos/{repo_owner}/{repo_name} | read | 
GET/repos/{owner}/{repo}/codeowners/errors | read | 
GET/repos/{owner}/{repo}/commits | read | 
GET/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head | read | 
POST/repos/{owner}/{repo}/commits/{commit_sha}/comments | read | 
GET/repos/{owner}/{repo}/commits/{ref} | read | 
GET/repos/{owner}/{repo}/community/profile | read | 
GET/repos/{owner}/{repo}/compare/{basehead} | read | 
GET/repos/{owner}/{repo}/contents/{path} | read | 
GET/repos/{owner}/{repo}/dependency-graph/compare/{basehead} | read | 
GET/repos/{owner}/{repo}/dependency-graph/sbom | read | 
POST/repos/{owner}/{repo}/forks | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/git/blobs/{file_sha} | read | 
GET/repos/{owner}/{repo}/git/commits/{commit_sha} | read | 
GET/repos/{owner}/{repo}/git/matching-refs/{ref} | read | 
GET/repos/{owner}/{repo}/git/ref/{ref} | read | 
GET/repos/{owner}/{repo}/git/tags/{tag_sha} | read | 
GET/repos/{owner}/{repo}/git/trees/{tree_sha} | read | 
GET/repos/{owner}/{repo}/import | read | 
GET/repos/{owner}/{repo}/import/authors | read | 
GET/repos/{owner}/{repo}/import/large_files | read | 
GET/repos/{owner}/{repo}/pulls/{pull_number} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/readme | read | 
GET/repos/{owner}/{repo}/readme/{dir} | read | 
GET/repos/{owner}/{repo}/releases | read | 
GET/repos/{owner}/{repo}/releases/assets/{asset_id} | read | 
GET/repos/{owner}/{repo}/releases/latest | read | 
GET/repos/{owner}/{repo}/releases/tags/{tag} | read | 
GET/repos/{owner}/{repo}/releases/{release_id} | read | 
GET/repos/{owner}/{repo}/releases/{release_id}/assets | read | 
GET/repos/{owner}/{repo}/tarball/{ref} | read | 
GET/repos/{owner}/{repo}/zipball/{ref} | read | 
POST/repos/{template_owner}/{template_repo}/generate | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## Repository permissions for "Custom properties"

[TABLE]
Endpoint | Access | Additional permissions
PATCH/repos/{owner}/{repo}/properties/values | write | 
[/TABLE]

## Repository permissions for "Dependabot alerts"

[TABLE]
Endpoint | Access | Additional permissions
PATCH/repos/{owner}/{repo}/dependabot/alerts/{alert_number} | write | 
GET/orgs/{org}/dependabot/alerts | read | 
GET/repos/{owner}/{repo}/dependabot/alerts | read | 
GET/repos/{owner}/{repo}/dependabot/alerts/{alert_number} | read | 
[/TABLE]

## Repository permissions for "Dependabot secrets"

[TABLE]
Endpoint | Access | Additional permissions
PUT/repos/{owner}/{repo}/dependabot/secrets/{secret_name} | write | 
DELETE/repos/{owner}/{repo}/dependabot/secrets/{secret_name} | write | 
GET/repos/{owner}/{repo}/dependabot/secrets | read | 
GET/repos/{owner}/{repo}/dependabot/secrets/public-key | read | 
GET/repos/{owner}/{repo}/dependabot/secrets/{secret_name} | read | 
[/TABLE]

## Repository permissions for "Deployments"

[TABLE]
Endpoint | Access | Additional permissions
POST/repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments | write | 
POST/repos/{owner}/{repo}/deployments | write | 
DELETE/repos/{owner}/{repo}/deployments/{deployment_id} | write | 
POST/repos/{owner}/{repo}/deployments/{deployment_id}/statuses | write | 
GET/repos/{owner}/{repo}/deployments | read | 
GET/repos/{owner}/{repo}/deployments/{deployment_id} | read | 
GET/repos/{owner}/{repo}/deployments/{deployment_id}/statuses | read | 
GET/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id} | read | 
[/TABLE]

## Repository permissions for "Environments"

[TABLE]
Endpoint | Access | Additional permissions
PUT/repos/{owner}/{repo}/environments/{environment_name}/secrets/{secret_name} | write | 
DELETE/repos/{owner}/{repo}/environments/{environment_name}/secrets/{secret_name} | write | 
POST/repos/{owner}/{repo}/environments/{environment_name}/variables | write | 
PATCH/repos/{owner}/{repo}/environments/{environment_name}/variables/{name} | write | 
DELETE/repos/{owner}/{repo}/environments/{environment_name}/variables/{name} | write | 
GET/repos/{owner}/{repo}/environments/{environment_name}/secrets | read | 
GET/repos/{owner}/{repo}/environments/{environment_name}/secrets/public-key | read | 
GET/repos/{owner}/{repo}/environments/{environment_name}/secrets/{secret_name} | read | 
GET/repos/{owner}/{repo}/environments/{environment_name}/variables | read | 
GET/repos/{owner}/{repo}/environments/{environment_name}/variables/{name} | read | 
[/TABLE]

## Repository permissions for "Issues"

[TABLE]
Endpoint | Access | Additional permissions
POST/repos/{owner}/{repo}/issues | write | 
PATCH/repos/{owner}/{repo}/issues/comments/{comment_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/comments/{comment_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/issues/comments/{comment_id}/pin | write | 
DELETE/repos/{owner}/{repo}/issues/comments/{comment_id}/pin | write | 
POST/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions | write | 
DELETE/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id} | write | 
PATCH/repos/{owner}/{repo}/issues/{issue_number} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/issues/{issue_number}/assignees | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/{issue_number}/assignees | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/issues/{issue_number}/comments | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by | write | 
DELETE/repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by/{issue_id} | write | 
POST/repos/{owner}/{repo}/issues/{issue_number}/label_filters | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/issues/{issue_number}/label_filters | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/{issue_number}/label_filters | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/{issue_number}/label_filters/{name} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/issues/{issue_number}/lock | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/{issue_number}/lock | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/issues/{issue_number}/reactions | write | 
DELETE/repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id} | write | 
DELETE/repos/{owner}/{repo}/issues/{issue_number}/sub_issue | write | 
POST/repos/{owner}/{repo}/issues/{issue_number}/sub_issues | write | 
PATCH/repos/{owner}/{repo}/issues/{issue_number}/sub_issues/priority | write | 
POST/repos/{owner}/{repo}/label_filters | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/label_filters/{name} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/label_filters/{name} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/milestones | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/milestones/{milestone_number} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/milestones/{milestone_number} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repositories/{repository_id}/issues/{issue_number}/issue-field-values | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repositories/{repository_id}/issues/{issue_number}/issue-field-values | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repositories/{repository_id}/issues/{issue_number}/issue-field-values/{issue_field_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/assignees | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/assignees/{assignee} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues | read | 
GET/repos/{owner}/{repo}/issues/comments | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/comments/{comment_id} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions | read | 
GET/repos/{owner}/{repo}/issues/events | read | 
GET/repos/{owner}/{repo}/issues/events/{event_id} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number} | read | 
GET/repos/{owner}/{repo}/issues/{issue_number}/assignees/{assignee} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/comments | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by | read | 
GET/repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocking | read | 
GET/repos/{owner}/{repo}/issues/{issue_number}/events | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/issue-field-values | read | 
GET/repos/{owner}/{repo}/issues/{issue_number}/label_filters | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/parent | read | 
GET/repos/{owner}/{repo}/issues/{issue_number}/reactions | read | 
GET/repos/{owner}/{repo}/issues/{issue_number}/sub_issues | read | 
GET/repos/{owner}/{repo}/issues/{issue_number}/timeline | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/label_filters | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/label_filters/{name} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/milestones | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/milestones/{milestone_number} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/milestones/{milestone_number}/label_filters | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## Repository permissions for "Metadata"

[TABLE]
Endpoint | Access | Additional permissions
GET/orgs/{org}/repos | read | 
GET/repos/{owner}/{repo} | read | 
GET/repos/{owner}/{repo}/collaborators | read | 
GET/repos/{owner}/{repo}/collaborators/{username} | read | 
GET/repos/{owner}/{repo}/collaborators/{username}/permission | read | 
GET/repos/{owner}/{repo}/comments | read | 
GET/repos/{owner}/{repo}/comments/{comment_id} | read | 
GET/repos/{owner}/{repo}/comments/{comment_id}/reactions | read | 
GET/repos/{owner}/{repo}/commits/{commit_sha}/comments | read | 
GET/repos/{owner}/{repo}/contributors | read | 
GET/repos/{owner}/{repo}/events | read | 
GET/repos/{owner}/{repo}/forks | read | 
GET/repos/{owner}/{repo}/languages | read | 
GET/repos/{owner}/{repo}/license | read | 
GET/repos/{owner}/{repo}/private-vulnerability-reporting | read | 
GET/repos/{owner}/{repo}/properties/values | read | 
GET/repos/{owner}/{repo}/rules/branches/{branch} | read | 
GET/repos/{owner}/{repo}/rulesets | read | 
GET/repos/{owner}/{repo}/rulesets/{ruleset_id} | read | 
GET/repos/{owner}/{repo}/stargazers | read | 
GET/repos/{owner}/{repo}/stats/code_frequency | read | 
GET/repos/{owner}/{repo}/stats/commit_activity | read | 
GET/repos/{owner}/{repo}/stats/contributors | read | 
GET/repos/{owner}/{repo}/stats/participation | read | 
GET/repos/{owner}/{repo}/stats/punch_card | read | 
GET/repos/{owner}/{repo}/subscribers | read | 
GET/repos/{owner}/{repo}/tags | read | 
GET/repos/{owner}/{repo}/topics | read | 
GET/repositories | read | 
GET/search/label_filters | read | 
GET/user/repos | read | 
GET/users/{username}/repos | read | 
[/TABLE]

## Repository permissions for "Pages"

[TABLE]
Endpoint | Access | Additional permissions
POST/repos/{owner}/{repo}/pages | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/pages | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/pages | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/pages/builds | write | 
POST/repos/{owner}/{repo}/pages/deployments | write | 
POST/repos/{owner}/{repo}/pages/deployments/{pages_deployment_id}/cancel | write | 
GET/repos/{owner}/{repo}/pages/health | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/pages | read | 
GET/repos/{owner}/{repo}/pages/builds | read | 
GET/repos/{owner}/{repo}/pages/builds/latest | read | 
GET/repos/{owner}/{repo}/pages/builds/{build_id} | read | 
GET/repos/{owner}/{repo}/pages/deployments/{pages_deployment_id} | read | 
[/TABLE]

## Repository permissions for "Pull requests"

[TABLE]
Endpoint | Access | Additional permissions
PATCH/repos/{owner}/{repo}/issues/comments/{comment_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/comments/{comment_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/issues/{issue_number} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/issues/{issue_number}/assignees | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/{issue_number}/assignees | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/issues/{issue_number}/comments | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/issues/{issue_number}/label_filters | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/issues/{issue_number}/label_filters | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/{issue_number}/label_filters | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/{issue_number}/label_filters/{name} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/issues/{issue_number}/lock | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/{issue_number}/lock | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/label_filters | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/label_filters/{name} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/label_filters/{name} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/milestones | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/milestones/{milestone_number} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/milestones/{milestone_number} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/pulls | write | 
PATCH/repos/{owner}/{repo}/pulls/comments/{comment_id} | write | 
DELETE/repos/{owner}/{repo}/pulls/comments/{comment_id} | write | 
POST/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions | write | 
DELETE/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id} | write | 
PATCH/repos/{owner}/{repo}/pulls/{pull_number} | write | 
POST/repos/{owner}/{repo}/pulls/{pull_number}/comments | write | 
POST/repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies | write | 
POST/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers | write | 
DELETE/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers | write | 
POST/repos/{owner}/{repo}/pulls/{pull_number}/reviews | write | 
PUT/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id} | write | 
DELETE/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id} | write | 
PUT/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals | write | 
POST/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events | write | 
PUT/repos/{owner}/{repo}/pulls/{pull_number}/update-branch | write | 
POST/repositories/{repository_id}/issues/{issue_number}/issue-field-values | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repositories/{repository_id}/issues/{issue_number}/issue-field-values | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repositories/{repository_id}/issues/{issue_number}/issue-field-values/{issue_field_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/assignees | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/assignees/{assignee} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/commits/{commit_sha}/pulls | read | 
GET/repos/{owner}/{repo}/issues/comments | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/comments/{comment_id} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/events/{event_id} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/assignees/{assignee} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/comments | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/events | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/label_filters | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/timeline | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/label_filters | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/label_filters/{name} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/milestones | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/milestones/{milestone_number} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/milestones/{milestone_number}/label_filters | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/pulls | read | 
GET/repos/{owner}/{repo}/pulls/comments | read | 
GET/repos/{owner}/{repo}/pulls/comments/{comment_id} | read | 
GET/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions | read | 
GET/repos/{owner}/{repo}/pulls/{pull_number} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/pulls/{pull_number}/comments | read | 
GET/repos/{owner}/{repo}/pulls/{pull_number}/commits | read | 
GET/repos/{owner}/{repo}/pulls/{pull_number}/files | read | 
GET/repos/{owner}/{repo}/pulls/{pull_number}/merge | read | 
GET/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers | read | 
GET/repos/{owner}/{repo}/pulls/{pull_number}/reviews | read | 
GET/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id} | read | 
GET/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments | read | 
[/TABLE]

## Repository permissions for "Repository security advisories"

[TABLE]
Endpoint | Access | Additional permissions
GET/orgs/{org}/security-advisories | write | 
POST/repos/{owner}/{repo}/security-advisories | write | 
POST/repos/{owner}/{repo}/security-advisories/reports | write | 
PATCH/repos/{owner}/{repo}/security-advisories/{ghsa_id} | write | 
POST/repos/{owner}/{repo}/security-advisories/{ghsa_id}/cve | write | 
GET/repos/{owner}/{repo}/security-advisories | read | 
GET/repos/{owner}/{repo}/security-advisories/{ghsa_id} | read | 
POST/repos/{owner}/{repo}/security-advisories/{ghsa_id}/forks | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## Repository permissions for "Secret scanning alerts"

[TABLE]
Endpoint | Access | Additional permissions
PATCH/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number} | write | 
GET/orgs/{org}/secret-scanning/alerts | read | 
GET/repos/{owner}/{repo}/secret-scanning/alerts | read | 
GET/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number} | read | 
GET/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations | read | 
GET/repos/{owner}/{repo}/secret-scanning/scan-history | read | 
[/TABLE]

## Repository permissions for "Secrets"

[TABLE]
Endpoint | Access | Additional permissions
PUT/repos/{owner}/{repo}/actions/secrets/{secret_name} | write | 
DELETE/repos/{owner}/{repo}/actions/secrets/{secret_name} | write | 
GET/repos/{owner}/{repo}/actions/organization-secrets | read | 
GET/repos/{owner}/{repo}/actions/secrets | read | 
GET/repos/{owner}/{repo}/actions/secrets/public-key | read | 
GET/repos/{owner}/{repo}/actions/secrets/{secret_name} | read | 
[/TABLE]

## Repository permissions for "Variables"

[TABLE]
Endpoint | Access | Additional permissions
POST/repos/{owner}/{repo}/actions/variables | write | 
PATCH/repos/{owner}/{repo}/actions/variables/{name} | write | 
DELETE/repos/{owner}/{repo}/actions/variables/{name} | write | 
GET/repos/{owner}/{repo}/actions/organization-variables | read | 
GET/repos/{owner}/{repo}/actions/variables | read | 
GET/repos/{owner}/{repo}/actions/variables/{name} | read | 
[/TABLE]

## Repository permissions for "Webhooks"

[TABLE]
Endpoint | Access | Additional permissions
POST/repos/{owner}/{repo}/hooks | write | 
PATCH/repos/{owner}/{repo}/hooks/{hook_id} | write | 
DELETE/repos/{owner}/{repo}/hooks/{hook_id} | write | 
PATCH/repos/{owner}/{repo}/hooks/{hook_id}/config | write | 
POST/repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}/attempts | write | 
GET/repos/{owner}/{repo}/hooks | read | 
GET/repos/{owner}/{repo}/hooks/{hook_id} | read | 
GET/repos/{owner}/{repo}/hooks/{hook_id}/config | read | 
GET/repos/{owner}/{repo}/hooks/{hook_id}/deliveries | read | 
GET/repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id} | read | 
POST/repos/{owner}/{repo}/hooks/{hook_id}/pings | read | 
POST/repos/{owner}/{repo}/hooks/{hook_id}/tests | read | 
[/TABLE]

## Repository permissions for "Workflows"

[TABLE]
Endpoint | Access | Additional permissions
PUT/repos/{owner}/{repo}/contents/{path} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/contents/{path} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/git/refs | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/git/refs/{ref} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/releases | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## User permissions for "Block another user"

[TABLE]
Endpoint | Access | Additional permissions
PUT/user/blocks/{username} | write | 
DELETE/user/blocks/{username} | write | 
GET/user/blocks | read | 
GET/user/blocks/{username} | read | 
[/TABLE]

## User permissions for "Codespaces user secrets"

[TABLE]
Endpoint | Access | Additional permissions
PUT/user/codespaces/secrets/{secret_name} | write | 
DELETE/user/codespaces/secrets/{secret_name} | write | 
PUT/user/codespaces/secrets/{secret_name}/repositories | write | 
PUT/user/codespaces/secrets/{secret_name}/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/user/codespaces/secrets/{secret_name}/repositories/{repository_id} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/user/codespaces/secrets | read | 
GET/user/codespaces/secrets/public-key | read | 
GET/user/codespaces/secrets/{secret_name} | read | 
GET/user/codespaces/secrets/{secret_name}/repositories | read | 
[/TABLE]

## User permissions for "Email addresses"

[TABLE]
Endpoint | Access | Additional permissions
PATCH/user/email/visibility | write | 
POST/user/emails | write | 
DELETE/user/emails | write | 
GET/user/emails | read | 
GET/user/public_emails | read | 
[/TABLE]

## User permissions for "Followers"

[TABLE]
Endpoint | Access | Additional permissions
PUT/user/following/{username} | write | 
DELETE/user/following/{username} | write | 
GET/user/followers | read | 
GET/user/following | read | 
GET/user/following/{username} | read | 
[/TABLE]

## User permissions for "GPG keys"

[TABLE]
Endpoint | Access | Additional permissions
POST/user/gpg_keys | write | 
DELETE/user/gpg_keys/{gpg_key_id} | write | 
GET/user/gpg_keys | read | 
GET/user/gpg_keys/{gpg_key_id} | read | 
[/TABLE]

## User permissions for "Gists"

[TABLE]
Endpoint | Access | Additional permissions
POST/gists | write | 
PATCH/gists/{gist_id} | write | 
DELETE/gists/{gist_id} | write | 
POST/gists/{gist_id}/comments | write | 
PATCH/gists/{gist_id}/comments/{comment_id} | write | 
DELETE/gists/{gist_id}/comments/{comment_id} | write | 
POST/gists/{gist_id}/forks | write | 
PUT/gists/{gist_id}/star | write | 
DELETE/gists/{gist_id}/star | write | 
[/TABLE]

## User permissions for "Git SSH keys"

[TABLE]
Endpoint | Access | Additional permissions
POST/user/keys | write | 
DELETE/user/keys/{key_id} | write | 
GET/user/keys | read | 
GET/user/keys/{key_id} | read | 
GET/users/{username}/keys | read | 
[/TABLE]

## User permissions for "Interaction limits"

[TABLE]
Endpoint | Access | Additional permissions
PUT/user/interaction-limits | write | 
DELETE/user/interaction-limits | write | 
GET/user/interaction-limits | read | 
[/TABLE]

## User permissions for "Plan"

[TABLE]
Endpoint | Access | Additional permissions
GET/users/{username}/settings/billing/premium_request/usage | read | 
GET/users/{username}/settings/billing/usage | read | 
GET/users/{username}/settings/billing/usage/summary | read | 
[/TABLE]

## User permissions for "Private repository invitations"

[TABLE]
Endpoint | Access | Additional permissions
GET/repos/{owner}/{repo}/invitations | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## User permissions for "Profile"

[TABLE]
Endpoint | Access | Additional permissions
PATCH/user | write | 
POST/user/social_accounts | write | 
DELETE/user/social_accounts | write | 
[/TABLE]

## User permissions for "SSH signing keys"

[TABLE]
Endpoint | Access | Additional permissions
POST/user/ssh_signing_keys | write | 
DELETE/user/ssh_signing_keys/{ssh_signing_key_id} | write | 
GET/user/ssh_signing_keys | read | 
GET/user/ssh_signing_keys/{ssh_signing_key_id} | read | 
[/TABLE]

## User permissions for "Starring"

[TABLE]
Endpoint | Access | Additional permissions
PUT/user/starred/{owner}/{repo} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/user/starred/{owner}/{repo} | write | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/user/starred | read | 
GET/user/starred/{owner}/{repo} | read | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/users/{username}/starred | read | 
[/TABLE]

## User permissions for "Watching"

[TABLE]
Endpoint | Access | Additional permissions
GET/user/subscriptions | read | 
GET/users/{username}/subscriptions | read | 
[/TABLE]