# Permissions required for GitHub Apps

*Source: https://docs.github.com/en/rest/overview/permissions-required-for-github-apps*

---

# Permissions required for GitHub Apps
For each permission granted to a GitHub App, these are the REST API endpoints that the app can use.

## In this article

## About GitHub App permissions
GitHub Apps are created with a set of permissions. Permissions define what resources the GitHub App can access via the API. For more information, seeChoosing permissions for a GitHub App.
To help you choose the correct permissions, you will receive theX-Accepted-GitHub-Permissionsheader in the REST API response. The header will tell you what permissions are required in order to access the endpoint. For more information, seeTroubleshooting the REST API.
These permissions are required to access private resources. Some endpoints can also be used to access public resources without these permissions. To see whether an endpoint can access public resources without a permission, see the documentation for that endpoint.
Some endpoints require more than one permission. Other endpoints work with any one permission from a set of permissions. In these cases, the "Additional permissions" column will include a checkmark. For full details about the permissions that are required to use the endpoint, see the documentation for that endpoint.

## Enterprise permissions for "Enterprise teams"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/enterprises/{enterprise}/teams | write | UATIAT | 
POST/enterprises/{enterprise}/teams/{enterprise-team}/memberships/add | write | UATIAT | 
POST/enterprises/{enterprise}/teams/{enterprise-team}/memberships/remove | write | UATIAT | 
PUT/enterprises/{enterprise}/teams/{enterprise-team}/memberships/{username} | write | UATIAT | 
DELETE/enterprises/{enterprise}/teams/{enterprise-team}/memberships/{username} | write | UATIAT | 
POST/enterprises/{enterprise}/teams/{enterprise-team}/organizations/add | write | UATIAT | 
POST/enterprises/{enterprise}/teams/{enterprise-team}/organizations/remove | write | UATIAT | 
PUT/enterprises/{enterprise}/teams/{enterprise-team}/organizations/{org} | write | UATIAT | 
DELETE/enterprises/{enterprise}/teams/{enterprise-team}/organizations/{org} | write | UATIAT | 
PATCH/enterprises/{enterprise}/teams/{team_slug} | write | UATIAT | 
DELETE/enterprises/{enterprise}/teams/{team_slug} | write | UATIAT | 
GET/enterprises/{enterprise}/teams | read | UATIAT | 
GET/enterprises/{enterprise}/teams/{enterprise-team}/memberships | read | UATIAT | 
GET/enterprises/{enterprise}/teams/{enterprise-team}/memberships/{username} | read | UATIAT | 
GET/enterprises/{enterprise}/teams/{enterprise-team}/organizations | read | UATIAT | 
GET/enterprises/{enterprise}/teams/{enterprise-team}/organizations/{org} | read | UATIAT | 
GET/enterprises/{enterprise}/teams/{team_slug} | read | UATIAT | 
[/TABLE]

## Organization permissions for "API Insights"

[TABLE]
Endpoint | Access | Token types | Additional permissions
GET/orgs/{org}/insights/api/route-stats/{actor_type}/{actor_id} | read | UATIAT | 
GET/orgs/{org}/insights/api/subject-stats | read | UATIAT | 
GET/orgs/{org}/insights/api/summary-stats | read | UATIAT | 
GET/orgs/{org}/insights/api/summary-stats/users/{user_id} | read | UATIAT | 
GET/orgs/{org}/insights/api/summary-stats/{actor_type}/{actor_id} | read | UATIAT | 
GET/orgs/{org}/insights/api/time-stats | read | UATIAT | 
GET/orgs/{org}/insights/api/time-stats/users/{user_id} | read | UATIAT | 
GET/orgs/{org}/insights/api/time-stats/{actor_type}/{actor_id} | read | UATIAT | 
GET/orgs/{org}/insights/api/user-stats/{user_id} | read | UATIAT | 
[/TABLE]

## Organization permissions for "Administration"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/organizations/{org}/actions/cache/retention-limit | write | UATIAT | 
PUT/organizations/{org}/actions/cache/storage-limit | write | UATIAT | 
PATCH/organizations/{org}/dependabot/repository-access | write | UATIAT | 
PUT/organizations/{org}/dependabot/repository-access/default-level | write | UATIAT | 
PATCH/organizations/{org}/settings/billing/budgets/{budget_id} | write | UATIAT | 
DELETE/organizations/{org}/settings/billing/budgets/{budget_id} | write | UATIAT | 
PATCH/orgs/{org} | write | UATIAT | 
DELETE/orgs/{org} | write | UATIAT | 
POST/orgs/{org}/actions/hosted-runners | write | UATIAT | 
PATCH/orgs/{org}/actions/hosted-runners/{hosted_runner_id} | write | UATIAT | 
DELETE/orgs/{org}/actions/hosted-runners/{hosted_runner_id} | write | UATIAT | 
POST/orgs/{org}/actions/oidc/customization/properties/repo | write | UATIAT | 
DELETE/orgs/{org}/actions/oidc/customization/properties/repo/{custom_property_name} | write | UATIAT | 
PUT/orgs/{org}/actions/oidc/customization/sub | write | UATIAT | 
PUT/orgs/{org}/actions/permissions | write | UATIAT | 
PUT/orgs/{org}/actions/permissions/artifact-and-log-retention | write | UATIAT | 
PUT/orgs/{org}/actions/permissions/fork-pr-contributor-approval | write | UATIAT | 
PUT/orgs/{org}/actions/permissions/fork-pr-workflows-private-repos | write | UATIAT | 
PUT/orgs/{org}/actions/permissions/repositories | write | UATIAT | 
PUT/orgs/{org}/actions/permissions/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/actions/permissions/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/orgs/{org}/actions/permissions/selected-actions | write | UATIAT | 
PUT/orgs/{org}/actions/permissions/self-hosted-runners | write | UATIAT | 
PUT/orgs/{org}/actions/permissions/self-hosted-runners/repositories | write | UATIAT | 
PUT/orgs/{org}/actions/permissions/self-hosted-runners/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/actions/permissions/self-hosted-runners/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/orgs/{org}/actions/permissions/workflow | write | UATIAT | 
POST/orgs/{org}/code-security/configurations | write | UATIAT | 
DELETE/orgs/{org}/code-security/configurations/detach | write | UATIAT | 
PATCH/orgs/{org}/code-security/configurations/{configuration_id} | write | UATIAT | 
DELETE/orgs/{org}/code-security/configurations/{configuration_id} | write | UATIAT | 
POST/orgs/{org}/code-security/configurations/{configuration_id}/attach | write | UATIAT | 
PUT/orgs/{org}/code-security/configurations/{configuration_id}/defaults | write | UATIAT | 
POST/orgs/{org}/copilot/billing/selected_teams | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/copilot/billing/selected_teams | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/orgs/{org}/copilot/billing/selected_users | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/copilot/billing/selected_users | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/orgs/{org}/interaction-limits | write | UATIAT | 
DELETE/orgs/{org}/interaction-limits | write | UATIAT | 
GET/orgs/{org}/rulesets | write | UATIAT | 
POST/orgs/{org}/rulesets | write | UATIAT | 
GET/orgs/{org}/rulesets/rule-suites | write | UATIAT | 
GET/orgs/{org}/rulesets/rule-suites/{rule_suite_id} | write | UATIAT | 
GET/orgs/{org}/rulesets/{ruleset_id} | write | UATIAT | 
PUT/orgs/{org}/rulesets/{ruleset_id} | write | UATIAT | 
DELETE/orgs/{org}/rulesets/{ruleset_id} | write | UATIAT | 
GET/orgs/{org}/rulesets/{ruleset_id}/history | write | UATIAT | 
GET/orgs/{org}/rulesets/{ruleset_id}/history/{version_id} | write | UATIAT | 
PATCH/orgs/{org}/secret-scanning/pattern-configurations | write | UATIAT | 
PUT/orgs/{org}/security-managers/teams/{team_slug} | write | UATIAT | 
DELETE/orgs/{org}/security-managers/teams/{team_slug} | write | UATIAT | 
PUT/orgs/{org}/settings/immutable-releases | write | UATIAT | 
PUT/orgs/{org}/settings/immutable-releases/repositories | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/orgs/{org}/settings/immutable-releases/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/settings/immutable-releases/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/orgs/{org}/{security_product}/{enablement} | write | UATIAT | 
GET/organizations/{org}/actions/cache/retention-limit | read | UATIAT | 
GET/organizations/{org}/actions/cache/storage-limit | read | UATIAT | 
GET/organizations/{org}/dependabot/repository-access | read | UATIAT | 
GET/organizations/{org}/settings/billing/budgets | read | UATIAT | 
GET/organizations/{org}/settings/billing/budgets/{budget_id} | read | UATIAT | 
GET/organizations/{org}/settings/billing/premium_request/usage | read | UATIAT | 
GET/organizations/{org}/settings/billing/usage | read | UATIAT | 
GET/organizations/{org}/settings/billing/usage/summary | read | UATIAT | 
GET/orgs/{org}/actions/cache/usage | read | UATIAT | 
GET/orgs/{org}/actions/cache/usage-by-repository | read | UATIAT | 
GET/orgs/{org}/actions/hosted-runners | read | UATIAT | 
GET/orgs/{org}/actions/hosted-runners/images/github-owned | read | UATIAT | 
GET/orgs/{org}/actions/hosted-runners/images/partner | read | UATIAT | 
GET/orgs/{org}/actions/hosted-runners/limits | read | UATIAT | 
GET/orgs/{org}/actions/hosted-runners/machine-sizes | read | UATIAT | 
GET/orgs/{org}/actions/hosted-runners/platforms | read | UATIAT | 
GET/orgs/{org}/actions/hosted-runners/{hosted_runner_id} | read | UATIAT | 
GET/orgs/{org}/actions/oidc/customization/properties/repo | read | UATIAT | 
GET/orgs/{org}/actions/oidc/customization/sub | read | UATIAT | 
GET/orgs/{org}/actions/permissions | read | UATIAT | 
GET/orgs/{org}/actions/permissions/artifact-and-log-retention | read | UATIAT | 
GET/orgs/{org}/actions/permissions/fork-pr-contributor-approval | read | UATIAT | 
GET/orgs/{org}/actions/permissions/fork-pr-workflows-private-repos | read | UATIAT | 
GET/orgs/{org}/actions/permissions/repositories | read | UATIAT | 
GET/orgs/{org}/actions/permissions/selected-actions | read | UATIAT | 
GET/orgs/{org}/actions/permissions/self-hosted-runners | read | UATIAT | 
GET/orgs/{org}/actions/permissions/self-hosted-runners/repositories | read | UATIAT | 
GET/orgs/{org}/actions/permissions/workflow | read | UATIAT | 
GET/orgs/{org}/code-security/configurations | read | UATIAT | 
GET/orgs/{org}/code-security/configurations/defaults | read | UATIAT | 
GET/orgs/{org}/code-security/configurations/{configuration_id} | read | UATIAT | 
GET/orgs/{org}/code-security/configurations/{configuration_id}/repositories | read | UATIAT | 
GET/orgs/{org}/copilot/billing | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/copilot/billing/seats | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/copilot/metrics | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/installations | read | UATIAT | 
GET/orgs/{org}/interaction-limits | read | UATIAT | 
GET/orgs/{org}/members/{username}/copilot | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/secret-scanning/pattern-configurations | read | UATIAT | 
GET/orgs/{org}/security-managers | read | UATIAT | 
GET/orgs/{org}/settings/immutable-releases | read | UATIAT | 
GET/orgs/{org}/settings/immutable-releases/repositories | read | UATIAT | 
GET/orgs/{org}/team/{team_slug}/copilot/metrics | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## Organization permissions for "Blocking users"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/orgs/{org}/blocks/{username} | write | UATIAT | 
DELETE/orgs/{org}/blocks/{username} | write | UATIAT | 
GET/orgs/{org}/blocks | read | UATIAT | 
GET/orgs/{org}/blocks/{username} | read | UATIAT | 
[/TABLE]

## Organization permissions for "Campaigns"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/campaigns | write | UATIAT | 
PATCH/orgs/{org}/campaigns/{campaign_number} | write | UATIAT | 
DELETE/orgs/{org}/campaigns/{campaign_number} | write | UATIAT | 
GET/orgs/{org}/campaigns | read | UATIAT | 
GET/orgs/{org}/campaigns/{campaign_number} | read | UATIAT | 
[/TABLE]

## Organization permissions for "Copilot agent settings"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/orgs/{org}/copilot/coding-agent/permissions | write | UATIAT | 
PUT/orgs/{org}/copilot/coding-agent/permissions/repositories | write | UATIAT | 
PUT/orgs/{org}/copilot/coding-agent/permissions/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/copilot/coding-agent/permissions/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/copilot/coding-agent/permissions | read | UATIAT | 
GET/orgs/{org}/copilot/coding-agent/permissions/repositories | read | UATIAT | 
[/TABLE]

## Organization permissions for "Copilot content exclusion"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/orgs/{org}/copilot/content_exclusion | write | UATIAT | 
GET/orgs/{org}/copilot/content_exclusion | read | UATIAT | 
[/TABLE]

## Organization permissions for "Custom organization roles"

[TABLE]
Endpoint | Access | Token types | Additional permissions
GET/orgs/{org}/organization-roles | read | UATIAT | 
GET/orgs/{org}/organization-roles/{role_id} | read | UATIAT | 
[/TABLE]

## Organization permissions for "Custom properties"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PATCH/orgs/{org}/properties/schema | admin | UATIAT | 
PUT/orgs/{org}/properties/schema/{custom_property_name} | admin | UATIAT | 
DELETE/orgs/{org}/properties/schema/{custom_property_name} | admin | UATIAT | 
PATCH/orgs/{org}/properties/values | write | UATIAT | 
GET/orgs/{org}/properties/schema | read | UATIAT | 
GET/orgs/{org}/properties/schema/{custom_property_name} | read | UATIAT | 
GET/orgs/{org}/properties/values | read | UATIAT | 
[/TABLE]

## Organization permissions for "Events"

[TABLE]
Endpoint | Access | Token types | Additional permissions
GET/users/{username}/events/orgs/{org} | read | UAT | 
[/TABLE]

## Organization permissions for "GitHub Copilot Business"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/copilot/billing/selected_teams | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/copilot/billing/selected_teams | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/orgs/{org}/copilot/billing/selected_users | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/copilot/billing/selected_users | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/copilot/billing | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/copilot/billing/seats | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/copilot/metrics | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/members/{username}/copilot | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/team/{team_slug}/copilot/metrics | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## Organization permissions for "Hosted runner custom images"

[TABLE]
Endpoint | Access | Token types | Additional permissions
DELETE/orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id} | write | UATIAT | 
DELETE/orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id}/versions/{version} | write | UATIAT | 
GET/orgs/{org}/actions/hosted-runners/images/custom | read | UATIAT | 
GET/orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id} | read | UATIAT | 
GET/orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id}/versions | read | UATIAT | 
GET/orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id}/versions/{version} | read | UATIAT | 
[/TABLE]

## Organization permissions for "Issue Fields"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/issue-fields | write | UATIAT | 
PATCH/orgs/{org}/issue-fields/{issue_field_id} | write | UATIAT | 
DELETE/orgs/{org}/issue-fields/{issue_field_id} | write | UATIAT | 
GET/orgs/{org}/issue-fields | read | UATIAT | 
[/TABLE]

## Organization permissions for "Issue Types"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/issue-types | write | UATIAT | 
PUT/orgs/{org}/issue-types/{issue_type_id} | write | UATIAT | 
DELETE/orgs/{org}/issue-types/{issue_type_id} | write | UATIAT | 
GET/orgs/{org}/issue-types | read | UATIAT | 
[/TABLE]

## Organization permissions for "Members"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/invitations | write | UATIAT | 
DELETE/orgs/{org}/invitations/{invitation_id} | write | UATIAT | 
DELETE/orgs/{org}/members/{username} | write | UATIAT | 
PUT/orgs/{org}/memberships/{username} | write | UATIAT | 
DELETE/orgs/{org}/memberships/{username} | write | UATIAT | 
DELETE/orgs/{org}/organization-roles/teams/{team_slug} | write | UATIAT | 
PUT/orgs/{org}/organization-roles/teams/{team_slug}/{role_id} | write | UATIAT | 
DELETE/orgs/{org}/organization-roles/teams/{team_slug}/{role_id} | write | UATIAT | 
DELETE/orgs/{org}/organization-roles/users/{username} | write | UATIAT | 
PUT/orgs/{org}/organization-roles/users/{username}/{role_id} | write | UATIAT | 
DELETE/orgs/{org}/organization-roles/users/{username}/{role_id} | write | UATIAT | 
PUT/orgs/{org}/outside_collaborators/{username} | write | UATIAT | 
DELETE/orgs/{org}/outside_collaborators/{username} | write | UATIAT | 
PUT/orgs/{org}/public_members/{username} | write | UAT | 
DELETE/orgs/{org}/public_members/{username} | write | UAT | 
POST/orgs/{org}/teams | write | UATIAT | 
PATCH/orgs/{org}/teams/{team_slug} | write | UATIAT | 
DELETE/orgs/{org}/teams/{team_slug} | write | UATIAT | 
PUT/orgs/{org}/teams/{team_slug}/memberships/{username} | write | UATIAT | 
DELETE/orgs/{org}/teams/{team_slug}/memberships/{username} | write | UATIAT | 
PATCH/teams/{team_id} | write | UATIAT | 
DELETE/teams/{team_id} | write | UATIAT | 
PUT/teams/{team_id}/members/{username} | write | UATIAT | 
DELETE/teams/{team_id}/members/{username} | write | UATIAT | 
PUT/teams/{team_id}/memberships/{username} | write | UATIAT | 
DELETE/teams/{team_id}/memberships/{username} | write | UATIAT | 
PATCH/user/memberships/orgs/{org} | write | UAT | 
GET/orgs/{org}/failed_invitations | read | UATIAT | 
GET/orgs/{org}/invitations | read | UATIAT | 
GET/orgs/{org}/invitations/{invitation_id}/teams | read | UATIAT | 
GET/orgs/{org}/members | read | UATIAT | 
GET/orgs/{org}/members/{username} | read | UATIAT | 
GET/orgs/{org}/memberships/{username} | read | UATIAT | 
GET/orgs/{org}/organization-roles/{role_id}/teams | read | UATIAT | 
GET/orgs/{org}/organization-roles/{role_id}/users | read | UATIAT | 
GET/orgs/{org}/outside_collaborators | read | UATIAT | 
GET/orgs/{org}/public_members | read | UATIAT | 
GET/orgs/{org}/public_members/{username} | read | UATIAT | 
GET/orgs/{org}/teams | read | UATIAT | 
GET/orgs/{org}/teams/{team_slug} | read | UATIAT | 
GET/orgs/{org}/teams/{team_slug}/invitations | read | UATIAT | 
GET/orgs/{org}/teams/{team_slug}/members | read | UATIAT | 
GET/orgs/{org}/teams/{team_slug}/memberships/{username} | read | UATIAT | 
GET/orgs/{org}/teams/{team_slug}/repos | read | UATIAT | 
GET/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/teams/{team_slug}/teams | read | UATIAT | 
GET/teams/{team_id} | read | UATIAT | 
GET/teams/{team_id}/invitations | read | UATIAT | 
GET/teams/{team_id}/members | read | UATIAT | 
GET/teams/{team_id}/members/{username} | read | UATIAT | 
GET/teams/{team_id}/memberships/{username} | read | UATIAT | 
GET/teams/{team_id}/repos | read | UATIAT | 
GET/teams/{team_id}/repos/{owner}/{repo} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/teams/{team_id}/repos/{owner}/{repo} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/teams/{team_id}/repos/{owner}/{repo} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/teams/{team_id}/teams | read | UATIAT | 
GET/user/memberships/orgs/{org} | read | UAT | 
[/TABLE]

## Organization permissions for "Network configurations"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/settings/network-configurations | write | UATIAT | 
PATCH/orgs/{org}/settings/network-configurations/{network_configuration_id} | write | UATIAT | 
DELETE/orgs/{org}/settings/network-configurations/{network_configuration_id} | write | UATIAT | 
GET/orgs/{org}/settings/network-configurations | read | UATIAT | 
GET/orgs/{org}/settings/network-configurations/{network_configuration_id} | read | UATIAT | 
GET/orgs/{org}/settings/network-settings/{network_settings_id} | read | UATIAT | 
[/TABLE]

## Organization permissions for "Organization codespaces secrets"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/orgs/{org}/codespaces/secrets/{secret_name} | write | UATIAT | 
DELETE/orgs/{org}/codespaces/secrets/{secret_name} | write | UATIAT | 
PUT/orgs/{org}/codespaces/secrets/{secret_name}/repositories | write | UATIAT | 
PUT/orgs/{org}/codespaces/secrets/{secret_name}/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/codespaces/secrets/{secret_name}/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/codespaces/secrets | read | UATIAT | 
GET/orgs/{org}/codespaces/secrets/public-key | read | UATIAT | 
GET/orgs/{org}/codespaces/secrets/{secret_name} | read | UATIAT | 
GET/orgs/{org}/codespaces/secrets/{secret_name}/repositories | read | UATIAT | 
[/TABLE]

## Organization permissions for "Organization codespaces settings"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/orgs/{org}/codespaces/access | write | UATIAT | 
POST/orgs/{org}/codespaces/access/selected_users | write | UATIAT | 
DELETE/orgs/{org}/codespaces/access/selected_users | write | UATIAT | 
[/TABLE]

## Organization permissions for "Organization codespaces"

[TABLE]
Endpoint | Access | Token types | Additional permissions
DELETE/orgs/{org}/members/{username}/codespaces/{codespace_name} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/orgs/{org}/members/{username}/codespaces/{codespace_name}/stop | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/codespaces | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/members/{username}/codespaces | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## Organization permissions for "Organization dependabot secrets"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/orgs/{org}/dependabot/secrets/{secret_name} | write | UATIAT | 
DELETE/orgs/{org}/dependabot/secrets/{secret_name} | write | UATIAT | 
PUT/orgs/{org}/dependabot/secrets/{secret_name}/repositories | write | UATIAT | 
PUT/orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/dependabot/secrets | read | UATIAT | 
GET/orgs/{org}/dependabot/secrets/public-key | read | UATIAT | 
GET/orgs/{org}/dependabot/secrets/{secret_name} | read | UATIAT | 
GET/orgs/{org}/dependabot/secrets/{secret_name}/repositories | read | UATIAT | 
[/TABLE]

## Organization permissions for "Organization private registries"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/private-registries | write | UATIAT | 
PATCH/orgs/{org}/private-registries/{secret_name} | write | UATIAT | 
DELETE/orgs/{org}/private-registries/{secret_name} | write | UATIAT | 
GET/orgs/{org}/private-registries | read | UATIAT | 
GET/orgs/{org}/private-registries/public-key | read | UATIAT | 
GET/orgs/{org}/private-registries/{secret_name} | read | UATIAT | 
[/TABLE]

## Organization permissions for "Personal access token requests"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/personal-access-token-requests | write | UATIAT | 
POST/orgs/{org}/personal-access-token-requests/{pat_request_id} | write | UATIAT | 
GET/orgs/{org}/personal-access-token-requests | read | UATIAT | 
GET/orgs/{org}/personal-access-token-requests/{pat_request_id}/repositories | read | UATIAT | 
[/TABLE]

## Organization permissions for "Personal access tokens"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/personal-access-tokens | write | UATIAT | 
POST/orgs/{org}/personal-access-tokens/{pat_id} | write | UATIAT | 
GET/orgs/{org}/personal-access-tokens | read | UATIAT | 
GET/orgs/{org}/personal-access-tokens/{pat_id}/repositories | read | UATIAT | 
[/TABLE]

## Organization permissions for "Projects"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/projectsV2/{project_number}/drafts | write | UATIAT | 
POST/orgs/{org}/projectsV2/{project_number}/fields | write | UATIAT | 
POST/orgs/{org}/projectsV2/{project_number}/items | write | UATIAT | 
PATCH/orgs/{org}/projectsV2/{project_number}/items/{item_id} | write | UATIAT | 
DELETE/orgs/{org}/projectsV2/{project_number}/items/{item_id} | write | UATIAT | 
POST/orgs/{org}/projectsV2/{project_number}/views | write | UATIAT | 
GET/orgs/{org}/projectsV2 | read | UATIAT | 
GET/orgs/{org}/projectsV2/{project_number} | read | UATIAT | 
GET/orgs/{org}/projectsV2/{project_number}/fields | read | UATIAT | 
GET/orgs/{org}/projectsV2/{project_number}/fields/{field_id} | read | UATIAT | 
GET/orgs/{org}/projectsV2/{project_number}/items | read | UATIAT | 
GET/orgs/{org}/projectsV2/{project_number}/items/{item_id} | read | UATIAT | 
GET/orgs/{org}/projectsV2/{project_number}/views/{view_number}/items | read | UATIAT | 
[/TABLE]

## Organization permissions for "Secrets"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/orgs/{org}/actions/secrets/{secret_name} | write | UATIAT | 
DELETE/orgs/{org}/actions/secrets/{secret_name} | write | UATIAT | 
PUT/orgs/{org}/actions/secrets/{secret_name}/repositories | write | UATIAT | 
PUT/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/actions/secrets | read | UATIAT | 
GET/orgs/{org}/actions/secrets/public-key | read | UATIAT | 
GET/orgs/{org}/actions/secrets/{secret_name} | read | UATIAT | 
GET/orgs/{org}/actions/secrets/{secret_name}/repositories | read | UATIAT | 
[/TABLE]

## Organization permissions for "Self-hosted runners"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/actions/runner-groups | write | UATIAT | 
PATCH/orgs/{org}/actions/runner-groups/{runner_group_id} | write | UATIAT | 
DELETE/orgs/{org}/actions/runner-groups/{runner_group_id} | write | UATIAT | 
PUT/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories | write | UATIAT | 
PUT/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/orgs/{org}/actions/runner-groups/{runner_group_id}/runners | write | UATIAT | 
PUT/orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id} | write | UATIAT | 
DELETE/orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id} | write | UATIAT | 
POST/orgs/{org}/actions/runners/generate-jitconfig | write | UATIAT | 
POST/orgs/{org}/actions/runners/registration-token | write | UATIAT | 
POST/orgs/{org}/actions/runners/remove-token | write | UATIAT | 
DELETE/orgs/{org}/actions/runners/{runner_id} | write | UATIAT | 
POST/orgs/{org}/actions/runners/{runner_id}/labels | write | UATIAT | 
PUT/orgs/{org}/actions/runners/{runner_id}/labels | write | UATIAT | 
DELETE/orgs/{org}/actions/runners/{runner_id}/labels | write | UATIAT | 
DELETE/orgs/{org}/actions/runners/{runner_id}/labels/{name} | write | UATIAT | 
GET/orgs/{org}/actions/runner-groups | read | UATIAT | 
GET/orgs/{org}/actions/runner-groups/{runner_group_id} | read | UATIAT | 
GET/orgs/{org}/actions/runner-groups/{runner_group_id}/hosted-runners | read | UATIAT | 
GET/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories | read | UATIAT | 
GET/orgs/{org}/actions/runner-groups/{runner_group_id}/runners | read | UATIAT | 
GET/orgs/{org}/actions/runners | read | UATIAT | 
GET/orgs/{org}/actions/runners/downloads | read | UATIAT | 
GET/orgs/{org}/actions/runners/{runner_id} | read | UATIAT | 
GET/orgs/{org}/actions/runners/{runner_id}/labels | read | UATIAT | 
[/TABLE]

## Organization permissions for "Variables"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/actions/variables | write | UATIAT | 
PATCH/orgs/{org}/actions/variables/{name} | write | UATIAT | 
DELETE/orgs/{org}/actions/variables/{name} | write | UATIAT | 
PUT/orgs/{org}/actions/variables/{name}/repositories | write | UATIAT | 
PUT/orgs/{org}/actions/variables/{name}/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/actions/variables/{name}/repositories/{repository_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/actions/variables | read | UATIAT | 
GET/orgs/{org}/actions/variables/{name} | read | UATIAT | 
GET/orgs/{org}/actions/variables/{name}/repositories | read | UATIAT | 
[/TABLE]

## Organization permissions for "Webhooks"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/hooks | write | UATIAT | 
PATCH/orgs/{org}/hooks/{hook_id} | write | UATIAT | 
DELETE/orgs/{org}/hooks/{hook_id} | write | UATIAT | 
PATCH/orgs/{org}/hooks/{hook_id}/config | write | UATIAT | 
POST/orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}/attempts | write | UATIAT | 
POST/orgs/{org}/hooks/{hook_id}/pings | write | UATIAT | 
GET/orgs/{org}/hooks | read | UATIAT | 
GET/orgs/{org}/hooks/{hook_id} | read | UATIAT | 
GET/orgs/{org}/hooks/{hook_id}/config | read | UATIAT | 
GET/orgs/{org}/hooks/{hook_id}/deliveries | read | UATIAT | 
GET/orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id} | read | UATIAT | 
[/TABLE]

## Repository permissions for "Actions"

[TABLE]
Endpoint | Access | Token types | Additional permissions
DELETE/repos/{owner}/{repo}/actions/artifacts/{artifact_id} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/actions/caches | write | UATIAT | 
DELETE/repos/{owner}/{repo}/actions/caches/{cache_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/actions/jobs/{job_id}/rerun | write | UATIAT | 
PUT/repos/{owner}/{repo}/actions/oidc/customization/sub | write | UATIAT | 
DELETE/repos/{owner}/{repo}/actions/runs/{run_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/actions/runs/{run_id}/approve | write | UATIAT | 
POST/repos/{owner}/{repo}/actions/runs/{run_id}/cancel | write | UATIAT | 
POST/repos/{owner}/{repo}/actions/runs/{run_id}/force-cancel | write | UATIAT | 
DELETE/repos/{owner}/{repo}/actions/runs/{run_id}/logs | write | UATIAT | 
POST/repos/{owner}/{repo}/actions/runs/{run_id}/rerun | write | UATIAT | 
POST/repos/{owner}/{repo}/actions/runs/{run_id}/rerun-failed-jobs | write | UATIAT | 
PUT/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable | write | UATIAT | 
POST/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches | write | UATIAT | 
PUT/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable | write | UATIAT | 
GET/repos/{owner}/{repo}/actions/artifacts | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/artifacts/{artifact_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format} | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/cache/storage-limit | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/cache/usage | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/caches | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/jobs/{job_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/jobs/{job_id}/logs | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/oidc/customization/sub | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/runs | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/runs/{run_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/approvals | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number} | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/logs | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/jobs | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/logs | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/runs/{run_id}/timing | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/workflows | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/workflows/{workflow_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing | read | UATIAT | 
GET/repos/{owner}/{repo}/environments | read | UATIAT | 
GET/repos/{owner}/{repo}/environments/{environment_name} | read | UATIAT | 
GET/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies | read | UATIAT | 
GET/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules | read | UATIAT | 
GET/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/{protection_rule_id} | read | UATIAT | 
[/TABLE]

## Repository permissions for "Administration"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/repos | write | UATIAT | 
PUT/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo} | write | UATIAT | 
DELETE/repos/{owner}/{repo} | write | UATIAT | 
PUT/repos/{owner}/{repo}/actions/cache/retention-limit | write | UATIAT | 
PUT/repos/{owner}/{repo}/actions/cache/storage-limit | write | UATIAT | 
PUT/repos/{owner}/{repo}/actions/permissions | write | UATIAT | 
PUT/repos/{owner}/{repo}/actions/permissions/access | write | UATIAT | 
PUT/repos/{owner}/{repo}/actions/permissions/artifact-and-log-retention | write | UATIAT | 
PUT/repos/{owner}/{repo}/actions/permissions/fork-pr-contributor-approval | write | UATIAT | 
PUT/repos/{owner}/{repo}/actions/permissions/fork-pr-workflows-private-repos | write | UATIAT | 
PUT/repos/{owner}/{repo}/actions/permissions/selected-actions | write | UATIAT | 
PUT/repos/{owner}/{repo}/actions/permissions/workflow | write | UATIAT | 
POST/repos/{owner}/{repo}/actions/runners/generate-jitconfig | write | UATIAT | 
POST/repos/{owner}/{repo}/actions/runners/registration-token | write | UATIAT | 
POST/repos/{owner}/{repo}/actions/runners/remove-token | write | UATIAT | 
DELETE/repos/{owner}/{repo}/actions/runners/{runner_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/actions/runners/{runner_id}/labels | write | UATIAT | 
PUT/repos/{owner}/{repo}/actions/runners/{runner_id}/labels | write | UATIAT | 
DELETE/repos/{owner}/{repo}/actions/runners/{runner_id}/labels | write | UATIAT | 
DELETE/repos/{owner}/{repo}/actions/runners/{runner_id}/labels/{name} | write | UATIAT | 
POST/repos/{owner}/{repo}/autolinks | write | UATIAT | 
DELETE/repos/{owner}/{repo}/autolinks/{autolink_id} | write | UATIAT | 
PUT/repos/{owner}/{repo}/automated-security-fixes | write | UATIAT | 
DELETE/repos/{owner}/{repo}/automated-security-fixes | write | UATIAT | 
PUT/repos/{owner}/{repo}/branches/{branch}/protection | write | UATIAT | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection | write | UATIAT | 
POST/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins | write | UATIAT | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins | write | UATIAT | 
PATCH/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews | write | UATIAT | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews | write | UATIAT | 
POST/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures | write | UATIAT | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures | write | UATIAT | 
PATCH/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks | write | UATIAT | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks | write | UATIAT | 
POST/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | write | UATIAT | 
PUT/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | write | UATIAT | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | write | UATIAT | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/restrictions | write | UATIAT | 
POST/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | write | UATIAT | 
PUT/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | write | UATIAT | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | write | UATIAT | 
POST/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | write | UATIAT | 
PUT/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | write | UATIAT | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | write | UATIAT | 
POST/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | write | UATIAT | 
PUT/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | write | UATIAT | 
DELETE/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | write | UATIAT | 
PATCH/repos/{owner}/{repo}/code-scanning/default-setup | write | UATIAT | 
PUT/repos/{owner}/{repo}/collaborators/{username} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/collaborators/{username} | write | UATIAT | 
PUT/repos/{owner}/{repo}/environments/{environment_name} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/environments/{environment_name} | write | UATIAT | 
POST/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies | write | UATIAT | 
PUT/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules | write | UATIAT | 
DELETE/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/{protection_rule_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/forks | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/immutable-releases | write | UATIAT | 
DELETE/repos/{owner}/{repo}/immutable-releases | write | UATIAT | 
PUT/repos/{owner}/{repo}/interaction-limits | write | UATIAT | 
DELETE/repos/{owner}/{repo}/interaction-limits | write | UATIAT | 
PATCH/repos/{owner}/{repo}/invitations/{invitation_id} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/invitations/{invitation_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/keys | write | UATIAT | 
DELETE/repos/{owner}/{repo}/keys/{key_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/pages | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/pages | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/pages | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/pages/health | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/private-vulnerability-reporting | write | UATIAT | 
DELETE/repos/{owner}/{repo}/private-vulnerability-reporting | write | UATIAT | 
POST/repos/{owner}/{repo}/rulesets | write | UATIAT | 
PUT/repos/{owner}/{repo}/rulesets/{ruleset_id} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/rulesets/{ruleset_id} | write | UATIAT | 
GET/repos/{owner}/{repo}/rulesets/{ruleset_id}/history | write | UATIAT | 
GET/repos/{owner}/{repo}/rulesets/{ruleset_id}/history/{version_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/security-advisories/{ghsa_id}/forks | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/topics | write | UATIAT | 
POST/repos/{owner}/{repo}/transfer | write | UAT | 
PUT/repos/{owner}/{repo}/vulnerability-alerts | write | UATIAT | 
DELETE/repos/{owner}/{repo}/vulnerability-alerts | write | UATIAT | 
POST/repos/{template_owner}/{template_repo}/generate | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/teams/{team_id}/repos/{owner}/{repo} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/teams/{team_id}/repos/{owner}/{repo} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/user/repos | write | UAT | 
PATCH/user/repository_invitations/{invitation_id} | write | UAT | 
DELETE/user/repository_invitations/{invitation_id} | write | UAT | 
GET/repos/{owner}/{repo}/actions/cache/retention-limit | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/permissions | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/permissions/access | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/permissions/artifact-and-log-retention | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/permissions/fork-pr-contributor-approval | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/permissions/fork-pr-workflows-private-repos | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/permissions/selected-actions | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/permissions/workflow | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/runners | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/runners/downloads | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/runners/{runner_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/runners/{runner_id}/labels | read | UATIAT | 
GET/repos/{owner}/{repo}/autolinks | read | UATIAT | 
GET/repos/{owner}/{repo}/autolinks/{autolink_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/automated-security-fixes | read | UATIAT | 
GET/repos/{owner}/{repo}/branches/{branch}/protection | read | UATIAT | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins | read | UATIAT | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews | read | UATIAT | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures | read | UATIAT | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks | read | UATIAT | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | read | UATIAT | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/restrictions | read | UATIAT | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | read | UATIAT | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | read | UATIAT | 
GET/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | read | UATIAT | 
GET/repos/{owner}/{repo}/code-scanning/default-setup | read | UATIAT | 
GET/repos/{owner}/{repo}/code-security-configuration | read | UATIAT | 
GET/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/apps | read | UATIAT | 
GET/repos/{owner}/{repo}/immutable-releases | read | UATIAT | 
GET/repos/{owner}/{repo}/interaction-limits | read | UATIAT | 
GET/repos/{owner}/{repo}/invitations | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/keys | read | UATIAT | 
GET/repos/{owner}/{repo}/keys/{key_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/rulesets/rule-suites | read | UATIAT | 
GET/repos/{owner}/{repo}/rulesets/rule-suites/{rule_suite_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/teams | read | UATIAT | 
GET/repos/{owner}/{repo}/traffic/clones | read | UATIAT | 
GET/repos/{owner}/{repo}/traffic/popular/paths | read | UATIAT | 
GET/repos/{owner}/{repo}/traffic/popular/referrers | read | UATIAT | 
GET/repos/{owner}/{repo}/traffic/views | read | UATIAT | 
GET/repos/{owner}/{repo}/vulnerability-alerts | read | UATIAT | 
GET/user/repository_invitations | read | UAT | 
[/TABLE]

## Repository permissions for "Artifact metadata"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/artifacts/metadata/deployment-record | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/orgs/{org}/artifacts/metadata/deployment-record/cluster/{cluster} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/orgs/{org}/artifacts/metadata/storage-record | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/artifacts/{subject_digest}/metadata/deployment-records | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/artifacts/{subject_digest}/metadata/storage-records | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## Repository permissions for "Attestations"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/attestations/delete-request | write | UATIAT | 
DELETE/orgs/{org}/attestations/digest/{subject_digest} | write | UATIAT | 
DELETE/orgs/{org}/attestations/{attestation_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/attestations | write | UATIAT | 
POST/users/{username}/attestations/delete-request | write | UATIAT | 
DELETE/users/{username}/attestations/digest/{subject_digest} | write | UATIAT | 
DELETE/users/{username}/attestations/{attestation_id} | write | UATIAT | 
GET/orgs/{org}/attestations/repositories | read | UATIAT | 
GET/repos/{owner}/{repo}/attestations/{subject_digest} | read | UATIAT | 
[/TABLE]

## Repository permissions for "Checks"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/repos/{owner}/{repo}/check-runs | write | UATIAT | 
PATCH/repos/{owner}/{repo}/check-runs/{check_run_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/check-runs/{check_run_id}/rerequest | write | UATIAT | 
POST/repos/{owner}/{repo}/check-suites | write | UATIAT | 
PATCH/repos/{owner}/{repo}/check-suites/preferences | write | UATIAT | 
POST/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest | write | UATIAT | 
GET/repos/{owner}/{repo}/check-runs/{check_run_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations | read | UATIAT | 
GET/repos/{owner}/{repo}/check-suites/{check_suite_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs | read | UATIAT | 
GET/repos/{owner}/{repo}/commits/{ref}/check-runs | read | UATIAT | 
GET/repos/{owner}/{repo}/commits/{ref}/check-suites | read | UATIAT | 
[/TABLE]

## Repository permissions for "Code scanning alerts"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PATCH/repos/{owner}/{repo}/code-scanning/alerts/{alert_number} | write | UATIAT | 
POST/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix | write | UATIAT | 
DELETE/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/code-scanning/sarifs | write | UATIAT | 
GET/orgs/{org}/code-scanning/alerts | read | UATIAT | 
GET/repos/{owner}/{repo}/code-scanning/alerts | read | UATIAT | 
GET/repos/{owner}/{repo}/code-scanning/alerts/{alert_number} | read | UATIAT | 
GET/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix | read | UATIAT | 
GET/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances | read | UATIAT | 
GET/repos/{owner}/{repo}/code-scanning/analyses | read | UATIAT | 
GET/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id} | read | UATIAT | 
[/TABLE]

## Repository permissions for "Codespaces lifecycle admin"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/members/{username}/codespaces/{codespace_name}/stop | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/user/codespaces/{codespace_name}/exports | write | UAT | 
POST/user/codespaces/{codespace_name}/start | write | UAT | 
POST/user/codespaces/{codespace_name}/stop | write | UAT | 
GET/user/codespaces/{codespace_name}/exports/{export_id} | read | UAT | 
[/TABLE]

## Repository permissions for "Codespaces metadata"

[TABLE]
Endpoint | Access | Token types | Additional permissions
GET/repos/{owner}/{repo}/codespaces/devcontainers | read | UATIAT | 
GET/repos/{owner}/{repo}/codespaces/machines | read | UATIAT | 
GET/user/codespaces/{codespace_name}/machines | read | UAT | 
[/TABLE]

## Repository permissions for "Codespaces secrets"

[TABLE]
Endpoint | Access | Token types | Additional permissions
GET/repos/{owner}/{repo}/codespaces/secrets | write | UATIAT | 
GET/repos/{owner}/{repo}/codespaces/secrets/public-key | write | UATIAT | 
GET/repos/{owner}/{repo}/codespaces/secrets/{secret_name} | write | UATIAT | 
PUT/repos/{owner}/{repo}/codespaces/secrets/{secret_name} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/codespaces/secrets/{secret_name} | write | UATIAT | 
[/TABLE]

## Repository permissions for "Codespaces"

[TABLE]
Endpoint | Access | Token types | Additional permissions
DELETE/orgs/{org}/members/{username}/codespaces/{codespace_name} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/codespaces | write | UAT | 
GET/repos/{owner}/{repo}/codespaces/new | write | UAT | 
GET/repos/{owner}/{repo}/codespaces/permissions_check | write | UAT | 
POST/repos/{owner}/{repo}/pulls/{pull_number}/codespaces | write | UAT | 
POST/user/codespaces | write | UAT | 
PATCH/user/codespaces/{codespace_name} | write | UAT | 
DELETE/user/codespaces/{codespace_name} | write | UAT | 
POST/user/codespaces/{codespace_name}/publish | write | UAT | 
GET/orgs/{org}/codespaces | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/members/{username}/codespaces | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/codespaces | read | UAT | 
GET/user/codespaces | read | UAT | 
GET/user/codespaces/{codespace_name} | read | UAT | 
[/TABLE]

## Repository permissions for "Commit statuses"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/repos/{owner}/{repo}/statuses/{sha} | write | UATIAT | 
GET/repos/{owner}/{repo}/commits/{ref}/status | read | UATIAT | 
GET/repos/{owner}/{repo}/commits/{ref}/statuses | read | UATIAT | 
[/TABLE]

## Repository permissions for "Contents"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/orgs/{org}/artifacts/metadata/deployment-record | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/orgs/{org}/artifacts/metadata/deployment-record/cluster/{cluster} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/orgs/{org}/artifacts/metadata/storage-record | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/branches/{branch}/rename | write | UATIAT | 
POST/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix/commits | write | UATIAT | 
DELETE/repos/{owner}/{repo}/code-scanning/codeql/databases/{language} | write | UATIAT | 
POST/repos/{owner}/{repo}/code-scanning/codeql/variant-analyses | write | UATIAT | 
PATCH/repos/{owner}/{repo}/comments/{comment_id} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/comments/{comment_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/comments/{comment_id}/reactions | write | UATIAT | 
DELETE/repos/{owner}/{repo}/comments/{comment_id}/reactions/{reaction_id} | write | UATIAT | 
PUT/repos/{owner}/{repo}/contents/{path} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/contents/{path} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/contents/{path} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/contents/{path} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/dependency-graph/snapshots | write | UATIAT | 
POST/repos/{owner}/{repo}/dispatches | write | UATIAT | 
POST/repos/{owner}/{repo}/git/blobs | write | UATIAT | 
POST/repos/{owner}/{repo}/git/commits | write | UATIAT | 
POST/repos/{owner}/{repo}/git/refs | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/git/refs | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/git/refs/{ref} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/git/refs/{ref} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/git/refs/{ref} | write | UATIAT | 
POST/repos/{owner}/{repo}/git/tags | write | UATIAT | 
POST/repos/{owner}/{repo}/git/trees | write | UATIAT | 
PUT/repos/{owner}/{repo}/import | write | UAT | 
PATCH/repos/{owner}/{repo}/import | write | UAT | 
DELETE/repos/{owner}/{repo}/import | write | UAT | 
PATCH/repos/{owner}/{repo}/import/authors/{author_id} | write | UAT | 
PATCH/repos/{owner}/{repo}/import/lfs | write | UAT | 
POST/repos/{owner}/{repo}/merge-upstream | write | UATIAT | 
POST/repos/{owner}/{repo}/merges | write | UATIAT | 
PUT/repos/{owner}/{repo}/pulls/{pull_number}/merge | write | UATIAT | 
POST/repos/{owner}/{repo}/releases | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/releases | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/releases/assets/{asset_id} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/releases/assets/{asset_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/releases/generate-notes | write | UATIAT | 
PATCH/repos/{owner}/{repo}/releases/{release_id} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/releases/{release_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/secret-scanning/push-protection-bypasses | write | UAT | 
POST/markdown | read | UATIAT | 
GET/orgs/{org}/artifacts/{subject_digest}/metadata/deployment-records | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/orgs/{org}/artifacts/{subject_digest}/metadata/storage-records | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/activity | read | UATIAT | 
GET/repos/{owner}/{repo}/branches | read | UATIAT | 
GET/repos/{owner}/{repo}/branches/{branch} | read | UATIAT | 
GET/repos/{owner}/{repo}/code-scanning/codeql/databases | read | UATIAT | 
GET/repos/{owner}/{repo}/code-scanning/codeql/databases/{language} | read | UATIAT | 
GET/repos/{owner}/{repo}/code-scanning/codeql/variant-analyses/{codeql_variant_analysis_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/code-scanning/codeql/variant-analyses/{codeql_variant_analysis_id}/repos/{repo_owner}/{repo_name} | read | UATIAT | 
GET/repos/{owner}/{repo}/codeowners/errors | read | UATIAT | 
GET/repos/{owner}/{repo}/commits | read | UATIAT | 
GET/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head | read | UATIAT | 
POST/repos/{owner}/{repo}/commits/{commit_sha}/comments | read | UATIAT | 
GET/repos/{owner}/{repo}/commits/{ref} | read | UATIAT | 
GET/repos/{owner}/{repo}/community/profile | read | UATIAT | 
GET/repos/{owner}/{repo}/compare/{basehead} | read | UATIAT | 
GET/repos/{owner}/{repo}/contents/{path} | read | UATIAT | 
GET/repos/{owner}/{repo}/dependency-graph/compare/{basehead} | read | UATIAT | 
GET/repos/{owner}/{repo}/dependency-graph/sbom | read | UATIAT | 
POST/repos/{owner}/{repo}/forks | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/git/blobs/{file_sha} | read | UATIAT | 
GET/repos/{owner}/{repo}/git/commits/{commit_sha} | read | UATIAT | 
GET/repos/{owner}/{repo}/git/matching-refs/{ref} | read | UATIAT | 
GET/repos/{owner}/{repo}/git/ref/{ref} | read | UATIAT | 
GET/repos/{owner}/{repo}/git/tags/{tag_sha} | read | UATIAT | 
GET/repos/{owner}/{repo}/git/trees/{tree_sha} | read | UATIAT | 
GET/repos/{owner}/{repo}/import | read | UAT | 
GET/repos/{owner}/{repo}/import/authors | read | UAT | 
GET/repos/{owner}/{repo}/import/large_files | read | UAT | 
GET/repos/{owner}/{repo}/pulls/{pull_number} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/readme | read | UATIAT | 
GET/repos/{owner}/{repo}/readme/{dir} | read | UATIAT | 
GET/repos/{owner}/{repo}/releases | read | UATIAT | 
GET/repos/{owner}/{repo}/releases/assets/{asset_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/releases/latest | read | UATIAT | 
GET/repos/{owner}/{repo}/releases/tags/{tag} | read | UATIAT | 
GET/repos/{owner}/{repo}/releases/{release_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/releases/{release_id}/assets | read | UATIAT | 
GET/repos/{owner}/{repo}/tarball/{ref} | read | UATIAT | 
GET/repos/{owner}/{repo}/zipball/{ref} | read | UATIAT | 
POST/repos/{template_owner}/{template_repo}/generate | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## Repository permissions for "Custom properties"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PATCH/repos/{owner}/{repo}/properties/values | write | UATIAT | 
[/TABLE]

## Repository permissions for "Dependabot alerts"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PATCH/repos/{owner}/{repo}/dependabot/alerts/{alert_number} | write | UATIAT | 
GET/orgs/{org}/dependabot/alerts | read | UATIAT | 
GET/repos/{owner}/{repo}/dependabot/alerts | read | UATIAT | 
GET/repos/{owner}/{repo}/dependabot/alerts/{alert_number} | read | UATIAT | 
[/TABLE]

## Repository permissions for "Dependabot secrets"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/repos/{owner}/{repo}/dependabot/secrets/{secret_name} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/dependabot/secrets/{secret_name} | write | UATIAT | 
GET/repos/{owner}/{repo}/dependabot/secrets | read | UATIAT | 
GET/repos/{owner}/{repo}/dependabot/secrets/public-key | read | UATIAT | 
GET/repos/{owner}/{repo}/dependabot/secrets/{secret_name} | read | UATIAT | 
[/TABLE]

## Repository permissions for "Deployments"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/repos/{owner}/{repo}/actions/runs/{run_id}/deployment_protection_rule | write | IAT | 
POST/repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments | write | UATIAT | 
POST/repos/{owner}/{repo}/deployments | write | UATIAT | 
DELETE/repos/{owner}/{repo}/deployments/{deployment_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/deployments/{deployment_id}/statuses | write | UATIAT | 
GET/repos/{owner}/{repo}/deployments | read | UATIAT | 
GET/repos/{owner}/{repo}/deployments/{deployment_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/deployments/{deployment_id}/statuses | read | UATIAT | 
GET/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id} | read | UATIAT | 
[/TABLE]

## Repository permissions for "Environments"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/repos/{owner}/{repo}/environments/{environment_name}/secrets/{secret_name} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/environments/{environment_name}/secrets/{secret_name} | write | UATIAT | 
POST/repos/{owner}/{repo}/environments/{environment_name}/variables | write | UATIAT | 
PATCH/repos/{owner}/{repo}/environments/{environment_name}/variables/{name} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/environments/{environment_name}/variables/{name} | write | UATIAT | 
GET/repos/{owner}/{repo}/environments/{environment_name}/secrets | read | UATIAT | 
GET/repos/{owner}/{repo}/environments/{environment_name}/secrets/public-key | read | UATIAT | 
GET/repos/{owner}/{repo}/environments/{environment_name}/secrets/{secret_name} | read | UATIAT | 
GET/repos/{owner}/{repo}/environments/{environment_name}/variables | read | UATIAT | 
GET/repos/{owner}/{repo}/environments/{environment_name}/variables/{name} | read | UATIAT | 
[/TABLE]

## Repository permissions for "Issues"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/repos/{owner}/{repo}/issues | write | UATIAT | 
PATCH/repos/{owner}/{repo}/issues/comments/{comment_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/comments/{comment_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/issues/comments/{comment_id}/pin | write | UATIAT | 
DELETE/repos/{owner}/{repo}/issues/comments/{comment_id}/pin | write | UATIAT | 
POST/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions | write | UATIAT | 
DELETE/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id} | write | UATIAT | 
PATCH/repos/{owner}/{repo}/issues/{issue_number} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/issues/{issue_number}/assignees | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/{issue_number}/assignees | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/issues/{issue_number}/comments | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by | write | UATIAT | 
DELETE/repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by/{issue_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/issues/{issue_number}/labels | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/issues/{issue_number}/labels | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/{issue_number}/labels | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/{issue_number}/labels/{name} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/issues/{issue_number}/lock | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/{issue_number}/lock | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/issues/{issue_number}/reactions | write | UATIAT | 
DELETE/repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/issues/{issue_number}/sub_issue | write | UATIAT | 
POST/repos/{owner}/{repo}/issues/{issue_number}/sub_issues | write | UATIAT | 
PATCH/repos/{owner}/{repo}/issues/{issue_number}/sub_issues/priority | write | UATIAT | 
POST/repos/{owner}/{repo}/labels | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/labels/{name} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/labels/{name} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/milestones | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/milestones/{milestone_number} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/milestones/{milestone_number} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repositories/{repository_id}/issues/{issue_number}/issue-field-values | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repositories/{repository_id}/issues/{issue_number}/issue-field-values | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repositories/{repository_id}/issues/{issue_number}/issue-field-values/{issue_field_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/assignees | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/assignees/{assignee} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues | read | UATIAT | 
GET/repos/{owner}/{repo}/issues/comments | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/comments/{comment_id} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions | read | UATIAT | 
GET/repos/{owner}/{repo}/issues/events | read | UATIAT | 
GET/repos/{owner}/{repo}/issues/events/{event_id} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number} | read | UATIAT | 
GET/repos/{owner}/{repo}/issues/{issue_number}/assignees/{assignee} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/comments | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by | read | UATIAT | 
GET/repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocking | read | UATIAT | 
GET/repos/{owner}/{repo}/issues/{issue_number}/events | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/issue-field-values | read | UATIAT | 
GET/repos/{owner}/{repo}/issues/{issue_number}/labels | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/parent | read | UATIAT | 
GET/repos/{owner}/{repo}/issues/{issue_number}/reactions | read | UATIAT | 
GET/repos/{owner}/{repo}/issues/{issue_number}/sub_issues | read | UATIAT | 
GET/repos/{owner}/{repo}/issues/{issue_number}/timeline | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/labels | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/labels/{name} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/milestones | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/milestones/{milestone_number} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/milestones/{milestone_number}/labels | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## Repository permissions for "Metadata"

[TABLE]
Endpoint | Access | Token types | Additional permissions
GET/orgs/{org}/repos | read | UATIAT | 
GET/repos/{owner}/{repo} | read | UATIAT | 
GET/repos/{owner}/{repo}/collaborators | read | UATIAT | 
GET/repos/{owner}/{repo}/collaborators/{username} | read | UATIAT | 
GET/repos/{owner}/{repo}/collaborators/{username}/permission | read | UATIAT | 
GET/repos/{owner}/{repo}/comments | read | UATIAT | 
GET/repos/{owner}/{repo}/comments/{comment_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/comments/{comment_id}/reactions | read | UATIAT | 
GET/repos/{owner}/{repo}/commits/{commit_sha}/comments | read | UATIAT | 
GET/repos/{owner}/{repo}/contributors | read | UATIAT | 
GET/repos/{owner}/{repo}/events | read | UATIAT | 
GET/repos/{owner}/{repo}/forks | read | UATIAT | 
GET/repos/{owner}/{repo}/languages | read | UATIAT | 
GET/repos/{owner}/{repo}/license | read | UATIAT | 
GET/repos/{owner}/{repo}/private-vulnerability-reporting | read | UATIAT | 
GET/repos/{owner}/{repo}/properties/values | read | UATIAT | 
GET/repos/{owner}/{repo}/rules/branches/{branch} | read | UATIAT | 
GET/repos/{owner}/{repo}/rulesets | read | UATIAT | 
GET/repos/{owner}/{repo}/rulesets/{ruleset_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/stargazers | read | UATIAT | 
GET/repos/{owner}/{repo}/stats/code_frequency | read | UATIAT | 
GET/repos/{owner}/{repo}/stats/commit_activity | read | UATIAT | 
GET/repos/{owner}/{repo}/stats/contributors | read | UATIAT | 
GET/repos/{owner}/{repo}/stats/participation | read | UATIAT | 
GET/repos/{owner}/{repo}/stats/punch_card | read | UATIAT | 
GET/repos/{owner}/{repo}/subscribers | read | UATIAT | 
GET/repos/{owner}/{repo}/tags | read | UATIAT | 
GET/repos/{owner}/{repo}/topics | read | UATIAT | 
GET/repositories | read | UATIAT | 
GET/search/labels | read | UATIAT | 
GET/user/installations/{installation_id}/repositories | read | UAT | 
GET/user/repos | read | UAT | 
GET/users/{username}/repos | read | UATIAT | 
[/TABLE]

## Repository permissions for "Pages"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/repos/{owner}/{repo}/pages | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/pages | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/pages | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/pages/builds | write | UATIAT | 
POST/repos/{owner}/{repo}/pages/deployments | write | UATIAT | 
POST/repos/{owner}/{repo}/pages/deployments/{pages_deployment_id}/cancel | write | UATIAT | 
GET/repos/{owner}/{repo}/pages/health | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/pages | read | UATIAT | 
GET/repos/{owner}/{repo}/pages/builds | read | UATIAT | 
GET/repos/{owner}/{repo}/pages/builds/latest | read | UATIAT | 
GET/repos/{owner}/{repo}/pages/builds/{build_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/pages/deployments/{pages_deployment_id} | read | UATIAT | 
[/TABLE]

## Repository permissions for "Pull requests"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PATCH/repos/{owner}/{repo}/issues/comments/{comment_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/comments/{comment_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/issues/{issue_number} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/issues/{issue_number}/assignees | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/{issue_number}/assignees | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/issues/{issue_number}/comments | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/issues/{issue_number}/labels | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/issues/{issue_number}/labels | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/{issue_number}/labels | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/{issue_number}/labels/{name} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repos/{owner}/{repo}/issues/{issue_number}/lock | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/issues/{issue_number}/lock | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/labels | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/labels/{name} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/labels/{name} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/milestones | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/milestones/{milestone_number} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/milestones/{milestone_number} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/pulls | write | UATIAT | 
PATCH/repos/{owner}/{repo}/pulls/comments/{comment_id} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/pulls/comments/{comment_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions | write | UATIAT | 
DELETE/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id} | write | UATIAT | 
PATCH/repos/{owner}/{repo}/pulls/{pull_number} | write | UATIAT | 
POST/repos/{owner}/{repo}/pulls/{pull_number}/comments | write | UATIAT | 
POST/repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies | write | UATIAT | 
POST/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers | write | UATIAT | 
DELETE/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers | write | UATIAT | 
POST/repos/{owner}/{repo}/pulls/{pull_number}/reviews | write | UATIAT | 
PUT/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id} | write | UATIAT | 
PUT/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals | write | UATIAT | 
POST/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events | write | UATIAT | 
PUT/repos/{owner}/{repo}/pulls/{pull_number}/update-branch | write | UATIAT | 
POST/repositories/{repository_id}/issues/{issue_number}/issue-field-values | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PUT/repositories/{repository_id}/issues/{issue_number}/issue-field-values | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repositories/{repository_id}/issues/{issue_number}/issue-field-values/{issue_field_id} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/assignees | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/assignees/{assignee} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/commits/{commit_sha}/pulls | read | UATIAT | 
GET/repos/{owner}/{repo}/issues/comments | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/comments/{comment_id} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/events/{event_id} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/assignees/{assignee} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/comments | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/events | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/labels | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/issues/{issue_number}/timeline | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/labels | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/labels/{name} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/milestones | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/milestones/{milestone_number} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/milestones/{milestone_number}/labels | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/pulls | read | UATIAT | 
GET/repos/{owner}/{repo}/pulls/comments | read | UATIAT | 
GET/repos/{owner}/{repo}/pulls/comments/{comment_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions | read | UATIAT | 
GET/repos/{owner}/{repo}/pulls/{pull_number} | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/repos/{owner}/{repo}/pulls/{pull_number}/comments | read | UATIAT | 
GET/repos/{owner}/{repo}/pulls/{pull_number}/commits | read | UATIAT | 
GET/repos/{owner}/{repo}/pulls/{pull_number}/files | read | UATIAT | 
GET/repos/{owner}/{repo}/pulls/{pull_number}/merge | read | UATIAT | 
GET/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers | read | UATIAT | 
GET/repos/{owner}/{repo}/pulls/{pull_number}/reviews | read | UATIAT | 
GET/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments | read | UATIAT | 
[/TABLE]

## Repository permissions for "Repository security advisories"

[TABLE]
Endpoint | Access | Token types | Additional permissions
GET/orgs/{org}/security-advisories | write | UATIAT | 
POST/repos/{owner}/{repo}/security-advisories | write | UATIAT | 
POST/repos/{owner}/{repo}/security-advisories/reports | write | UATIAT | 
PATCH/repos/{owner}/{repo}/security-advisories/{ghsa_id} | write | UATIAT | 
POST/repos/{owner}/{repo}/security-advisories/{ghsa_id}/cve | write | UATIAT | 
GET/repos/{owner}/{repo}/security-advisories | read | UATIAT | 
GET/repos/{owner}/{repo}/security-advisories/{ghsa_id} | read | UATIAT | 
POST/repos/{owner}/{repo}/security-advisories/{ghsa_id}/forks | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## Repository permissions for "Secret scanning alerts"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PATCH/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number} | write | UATIAT | 
GET/orgs/{org}/secret-scanning/alerts | read | UATIAT | 
GET/repos/{owner}/{repo}/secret-scanning/alerts | read | UATIAT | 
GET/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number} | read | UATIAT | 
GET/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations | read | UATIAT | 
GET/repos/{owner}/{repo}/secret-scanning/scan-history | read | UATIAT | 
[/TABLE]

## Repository permissions for "Secrets"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/repos/{owner}/{repo}/actions/secrets/{secret_name} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/actions/secrets/{secret_name} | write | UATIAT | 
GET/repos/{owner}/{repo}/actions/organization-secrets | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/secrets | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/secrets/public-key | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/secrets/{secret_name} | read | UATIAT | 
[/TABLE]

## Repository permissions for "Variables"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/repos/{owner}/{repo}/actions/variables | write | UATIAT | 
PATCH/repos/{owner}/{repo}/actions/variables/{name} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/actions/variables/{name} | write | UATIAT | 
GET/repos/{owner}/{repo}/actions/organization-variables | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/variables | read | UATIAT | 
GET/repos/{owner}/{repo}/actions/variables/{name} | read | UATIAT | 
[/TABLE]

## Repository permissions for "Webhooks"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/repos/{owner}/{repo}/hooks | write | UATIAT | 
PATCH/repos/{owner}/{repo}/hooks/{hook_id} | write | UATIAT | 
DELETE/repos/{owner}/{repo}/hooks/{hook_id} | write | UATIAT | 
PATCH/repos/{owner}/{repo}/hooks/{hook_id}/config | write | UATIAT | 
POST/repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}/attempts | write | UATIAT | 
GET/repos/{owner}/{repo}/hooks | read | UATIAT | 
GET/repos/{owner}/{repo}/hooks/{hook_id} | read | UATIAT | 
GET/repos/{owner}/{repo}/hooks/{hook_id}/config | read | UATIAT | 
GET/repos/{owner}/{repo}/hooks/{hook_id}/deliveries | read | UATIAT | 
GET/repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id} | read | UATIAT | 
POST/repos/{owner}/{repo}/hooks/{hook_id}/pings | read | UATIAT | 
POST/repos/{owner}/{repo}/hooks/{hook_id}/tests | read | UATIAT | 
[/TABLE]

## Repository permissions for "Workflows"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/repos/{owner}/{repo}/contents/{path} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/repos/{owner}/{repo}/contents/{path} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/git/refs | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
PATCH/repos/{owner}/{repo}/git/refs/{ref} | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
POST/repos/{owner}/{repo}/releases | write | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## User permissions for "Block another user"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/user/blocks/{username} | write | UAT | 
DELETE/user/blocks/{username} | write | UAT | 
GET/user/blocks | read | UAT | 
GET/user/blocks/{username} | read | UAT | 
[/TABLE]

## User permissions for "Codespaces user secrets"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/user/codespaces/secrets/{secret_name} | write | UAT | 
DELETE/user/codespaces/secrets/{secret_name} | write | UAT | 
PUT/user/codespaces/secrets/{secret_name}/repositories | write | UAT | 
PUT/user/codespaces/secrets/{secret_name}/repositories/{repository_id} | write | UAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/user/codespaces/secrets/{secret_name}/repositories/{repository_id} | write | UAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/user/codespaces/secrets | read | UAT | 
GET/user/codespaces/secrets/public-key | read | UAT | 
GET/user/codespaces/secrets/{secret_name} | read | UAT | 
GET/user/codespaces/secrets/{secret_name}/repositories | read | UAT | 
[/TABLE]

## User permissions for "Email addresses"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PATCH/user/email/visibility | write | UAT | 
POST/user/emails | write | UAT | 
DELETE/user/emails | write | UAT | 
GET/user/emails | read | UAT | 
GET/user/public_emails | read | UAT | 
[/TABLE]

## User permissions for "Followers"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/user/following/{username} | write | UAT | 
DELETE/user/following/{username} | write | UAT | 
GET/user/followers | read | UAT | 
GET/user/following | read | UAT | 
GET/user/following/{username} | read | UAT | 
[/TABLE]

## User permissions for "GPG keys"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/user/gpg_keys | write | UAT | 
DELETE/user/gpg_keys/{gpg_key_id} | write | UAT | 
GET/user/gpg_keys | read | UAT | 
GET/user/gpg_keys/{gpg_key_id} | read | UAT | 
[/TABLE]

## User permissions for "Gists"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/gists | write | UAT | 
PATCH/gists/{gist_id} | write | UAT | 
DELETE/gists/{gist_id} | write | UAT | 
POST/gists/{gist_id}/comments | write | UAT | 
PATCH/gists/{gist_id}/comments/{comment_id} | write | UAT | 
DELETE/gists/{gist_id}/comments/{comment_id} | write | UAT | 
POST/gists/{gist_id}/forks | write | UAT | 
PUT/gists/{gist_id}/star | write | UAT | 
DELETE/gists/{gist_id}/star | write | UAT | 
[/TABLE]

## User permissions for "Git SSH keys"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/user/keys | write | UAT | 
DELETE/user/keys/{key_id} | write | UAT | 
GET/user/keys | read | UAT | 
GET/user/keys/{key_id} | read | UAT | 
GET/users/{username}/keys | read | UATIAT | 
[/TABLE]

## User permissions for "Interaction limits"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/user/interaction-limits | write | UAT | 
DELETE/user/interaction-limits | write | UAT | 
GET/user/interaction-limits | read | UAT | 
[/TABLE]

## User permissions for "Plan"

[TABLE]
Endpoint | Access | Token types | Additional permissions
GET/users/{username}/settings/billing/premium_request/usage | read | UAT | 
GET/users/{username}/settings/billing/usage | read | UAT | 
GET/users/{username}/settings/billing/usage/summary | read | UAT | 
[/TABLE]

## User permissions for "Private repository invitations"

[TABLE]
Endpoint | Access | Token types | Additional permissions
GET/repos/{owner}/{repo}/invitations | read | UATIAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
[/TABLE]

## User permissions for "Profile"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PATCH/user | write | UAT | 
POST/user/social_accounts | write | UAT | 
DELETE/user/social_accounts | write | UAT | 
[/TABLE]

## User permissions for "SSH signing keys"

[TABLE]
Endpoint | Access | Token types | Additional permissions
POST/user/ssh_signing_keys | write | UAT | 
DELETE/user/ssh_signing_keys/{ssh_signing_key_id} | write | UAT | 
GET/user/ssh_signing_keys | read | UAT | 
GET/user/ssh_signing_keys/{ssh_signing_key_id} | read | UAT | 
[/TABLE]

## User permissions for "Starring"

[TABLE]
Endpoint | Access | Token types | Additional permissions
PUT/user/starred/{owner}/{repo} | write | UAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
DELETE/user/starred/{owner}/{repo} | write | UAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/user/starred | read | UAT | 
GET/user/starred/{owner}/{repo} | read | UAT | Multiple permissions are required, or a different permission may be used. For more information about the permissions, see the documentation for this endpoint.
GET/users/{username}/starred | read | UATIAT | 
[/TABLE]

## User permissions for "Watching"

[TABLE]
Endpoint | Access | Token types | Additional permissions
GET/user/subscriptions | read | UAT | 
GET/users/{username}/subscriptions | read | UATIAT | 
[/TABLE]