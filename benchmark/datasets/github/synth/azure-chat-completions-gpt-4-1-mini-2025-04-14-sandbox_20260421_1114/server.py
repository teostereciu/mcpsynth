import os
from fastmcp import FastMCP

from generated_tools import issues, pulls, repos, releases, actions_workflows, search, branches


class GitHubMCPServer(FastMCP):
    def list_tools(self):
        return [
            'issues.list_issues_assigned_to_authenticated_user',
            'issues.get_issue',
            'issues.create_issue',
            'issues.update_issue',
            'issues.lock_issue',
            'issues.unlock_issue',
            'pulls.list_pull_requests',
            'pulls.get_pull_request',
            'pulls.create_pull_request',
            'pulls.update_pull_request',
            'pulls.merge_pull_request',
            'repos.list_org_repos',
            'repos.create_org_repo',
            'releases.list_releases',
            'releases.create_release',
            'releases.generate_release_notes',
            'releases.get_latest_release',
            'releases.get_release_by_tag',
            'releases.get_release',
            'releases.update_release',
            'releases.delete_release',
            'actions_workflows.list_workflows',
            'actions_workflows.get_workflow',
            'actions_workflows.disable_workflow',
            'actions_workflows.create_workflow_dispatch_event',
            'actions_workflows.enable_workflow',
            'actions_workflows.get_workflow_usage',
            'search.search_code',
            'search.search_commits',
            'search.search_issues_and_pull_requests',
            'search.search_labels',
            'search.search_repositories',
            'search.search_topics',
            'search.search_users',
            'branches.get_branch_protection',
            'branches.update_branch_protection',
            'branches.delete_branch_protection',
        ]


if __name__ == '__main__':
    server = GitHubMCPServer()
    server.serve_forever()
