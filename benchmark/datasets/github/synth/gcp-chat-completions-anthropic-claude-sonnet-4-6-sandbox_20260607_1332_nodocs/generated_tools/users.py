"""MCP tools for GitHub Users and Organizations."""
from mcp.server.fastmcp import FastMCP
from .client import gh_get, gh_post, gh_patch, gh_delete, gh_put

def register(mcp: FastMCP):

    # --- Authenticated User ---

    @mcp.tool()
    def get_authenticated_user() -> dict | list:
        """Get the authenticated user's profile."""
        return gh_get("/user")

    @mcp.tool()
    def update_authenticated_user(
        name: str = "",
        email: str = "",
        blog: str = "",
        company: str = "",
        location: str = "",
        hireable: bool | None = None,
        bio: str = "",
        twitter_username: str = "",
    ) -> dict | list:
        """Update the authenticated user's profile."""
        payload: dict = {}
        if name:
            payload["name"] = name
        if email:
            payload["email"] = email
        if blog:
            payload["blog"] = blog
        if company:
            payload["company"] = company
        if location:
            payload["location"] = location
        if hireable is not None:
            payload["hireable"] = hireable
        if bio:
            payload["bio"] = bio
        if twitter_username:
            payload["twitter_username"] = twitter_username
        return gh_patch("/user", json=payload)

    @mcp.tool()
    def get_user(username: str) -> dict | list:
        """Get a public user profile by username."""
        return gh_get(f"/users/{username}")

    @mcp.tool()
    def list_users(since: int = 0, per_page: int = 30) -> dict | list:
        """List all public users."""
        return gh_get("/users", params={"since": since, "per_page": per_page})

    # --- Followers ---

    @mcp.tool()
    def list_followers(username: str = "", per_page: int = 30, page: int = 1) -> dict | list:
        """List followers of a user. Leave username empty for authenticated user."""
        params = {"per_page": per_page, "page": page}
        if username:
            return gh_get(f"/users/{username}/followers", params=params)
        return gh_get("/user/followers", params=params)

    @mcp.tool()
    def list_following(username: str = "", per_page: int = 30, page: int = 1) -> dict | list:
        """List users a user is following. Leave username empty for authenticated user."""
        params = {"per_page": per_page, "page": page}
        if username:
            return gh_get(f"/users/{username}/following", params=params)
        return gh_get("/user/following", params=params)

    @mcp.tool()
    def follow_user(username: str) -> dict | list:
        """Follow a user."""
        return gh_put(f"/user/following/{username}")

    @mcp.tool()
    def unfollow_user(username: str) -> dict | list:
        """Unfollow a user."""
        return gh_delete(f"/user/following/{username}")

    @mcp.tool()
    def check_following_user(username: str) -> dict | list:
        """Check if the authenticated user follows a user."""
        return gh_get(f"/user/following/{username}")

    # --- Emails ---

    @mcp.tool()
    def list_emails() -> dict | list:
        """List email addresses for the authenticated user."""
        return gh_get("/user/emails")

    @mcp.tool()
    def add_emails(emails: list[str]) -> dict | list:
        """Add email addresses for the authenticated user."""
        return gh_post("/user/emails", json={"emails": emails})

    @mcp.tool()
    def delete_emails(emails: list[str]) -> dict | list:
        """Delete email addresses for the authenticated user."""
        return gh_delete("/user/emails", json={"emails": emails})

    # --- SSH Keys ---

    @mcp.tool()
    def list_ssh_keys(username: str = "", per_page: int = 30, page: int = 1) -> dict | list:
        """List SSH keys for a user. Leave username empty for authenticated user."""
        params = {"per_page": per_page, "page": page}
        if username:
            return gh_get(f"/users/{username}/keys", params=params)
        return gh_get("/user/keys", params=params)

    @mcp.tool()
    def get_ssh_key(key_id: int) -> dict | list:
        """Get an SSH key for the authenticated user."""
        return gh_get(f"/user/keys/{key_id}")

    @mcp.tool()
    def create_ssh_key(title: str, key: str) -> dict | list:
        """Add an SSH key for the authenticated user."""
        return gh_post("/user/keys", json={"title": title, "key": key})

    @mcp.tool()
    def delete_ssh_key(key_id: int) -> dict | list:
        """Delete an SSH key for the authenticated user."""
        return gh_delete(f"/user/keys/{key_id}")

    # --- GPG Keys ---

    @mcp.tool()
    def list_gpg_keys(per_page: int = 30, page: int = 1) -> dict | list:
        """List GPG keys for the authenticated user."""
        return gh_get("/user/gpg_keys", params={"per_page": per_page, "page": page})

    @mcp.tool()
    def create_gpg_key(armored_public_key: str, name: str = "") -> dict | list:
        """Add a GPG key for the authenticated user."""
        payload: dict = {"armored_public_key": armored_public_key}
        if name:
            payload["name"] = name
        return gh_post("/user/gpg_keys", json=payload)

    @mcp.tool()
    def delete_gpg_key(gpg_key_id: int) -> dict | list:
        """Delete a GPG key for the authenticated user."""
        return gh_delete(f"/user/gpg_keys/{gpg_key_id}")

    # --- Starred Repos ---

    @mcp.tool()
    def list_starred_repos(username: str = "", per_page: int = 30, page: int = 1) -> dict | list:
        """List repositories starred by a user."""
        params = {"per_page": per_page, "page": page}
        if username:
            return gh_get(f"/users/{username}/starred", params=params)
        return gh_get("/user/starred", params=params)

    @mcp.tool()
    def star_repo(owner: str, repo: str) -> dict | list:
        """Star a repository."""
        return gh_put(f"/user/starred/{owner}/{repo}")

    @mcp.tool()
    def unstar_repo(owner: str, repo: str) -> dict | list:
        """Unstar a repository."""
        return gh_delete(f"/user/starred/{owner}/{repo}")

    @mcp.tool()
    def check_repo_starred(owner: str, repo: str) -> dict | list:
        """Check if the authenticated user has starred a repository."""
        return gh_get(f"/user/starred/{owner}/{repo}")

    # --- Organizations ---

    @mcp.tool()
    def get_org(org: str) -> dict | list:
        """Get an organization's public profile."""
        return gh_get(f"/orgs/{org}")

    @mcp.tool()
    def update_org(
        org: str,
        billing_email: str = "",
        company: str = "",
        email: str = "",
        location: str = "",
        name: str = "",
        description: str = "",
        has_organization_projects: bool | None = None,
        has_repository_projects: bool | None = None,
        default_repository_permission: str = "",
        members_can_create_repositories: bool | None = None,
    ) -> dict | list:
        """Update an organization."""
        payload: dict = {}
        for k, v in [("billing_email", billing_email), ("company", company), ("email", email),
                     ("location", location), ("name", name), ("description", description),
                     ("default_repository_permission", default_repository_permission)]:
            if v:
                payload[k] = v
        if has_organization_projects is not None:
            payload["has_organization_projects"] = has_organization_projects
        if has_repository_projects is not None:
            payload["has_repository_projects"] = has_repository_projects
        if members_can_create_repositories is not None:
            payload["members_can_create_repositories"] = members_can_create_repositories
        return gh_patch(f"/orgs/{org}", json=payload)

    @mcp.tool()
    def list_org_members(
        org: str, filter: str = "all", role: str = "all", per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List members of an organization."""
        return gh_get(f"/orgs/{org}/members",
                      params={"filter": filter, "role": role, "per_page": per_page, "page": page})

    @mcp.tool()
    def remove_org_member(org: str, username: str) -> dict | list:
        """Remove a member from an organization."""
        return gh_delete(f"/orgs/{org}/members/{username}")

    @mcp.tool()
    def list_user_orgs(username: str = "", per_page: int = 30, page: int = 1) -> dict | list:
        """List organizations for a user. Leave username empty for authenticated user."""
        params = {"per_page": per_page, "page": page}
        if username:
            return gh_get(f"/users/{username}/orgs", params=params)
        return gh_get("/user/orgs", params=params)

    @mcp.tool()
    def list_org_invitations(org: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List pending invitations for an organization."""
        return gh_get(f"/orgs/{org}/invitations", params={"per_page": per_page, "page": page})

    @mcp.tool()
    def create_org_invitation(
        org: str,
        invitee_id: int | None = None,
        email: str = "",
        role: str = "direct_member",
        team_ids: list[int] | None = None,
    ) -> dict | list:
        """Create an invitation to an organization."""
        payload: dict = {"role": role}
        if invitee_id is not None:
            payload["invitee_id"] = invitee_id
        if email:
            payload["email"] = email
        if team_ids:
            payload["team_ids"] = team_ids
        return gh_post(f"/orgs/{org}/invitations", json=payload)

    @mcp.tool()
    def cancel_org_invitation(org: str, invitation_id: int) -> dict | list:
        """Cancel an organization invitation."""
        return gh_delete(f"/orgs/{org}/invitations/{invitation_id}")

    # --- Teams ---

    @mcp.tool()
    def list_org_teams(org: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List teams in an organization."""
        return gh_get(f"/orgs/{org}/teams", params={"per_page": per_page, "page": page})

    @mcp.tool()
    def get_team_by_slug(org: str, team_slug: str) -> dict | list:
        """Get a team by slug."""
        return gh_get(f"/orgs/{org}/teams/{team_slug}")

    @mcp.tool()
    def create_team(
        org: str,
        name: str,
        description: str = "",
        privacy: str = "secret",
        permission: str = "pull",
        parent_team_id: int | None = None,
    ) -> dict | list:
        """Create a team in an organization. privacy: secret|closed."""
        payload: dict = {"name": name, "privacy": privacy, "permission": permission}
        if description:
            payload["description"] = description
        if parent_team_id is not None:
            payload["parent_team_id"] = parent_team_id
        return gh_post(f"/orgs/{org}/teams", json=payload)

    @mcp.tool()
    def update_team(
        org: str,
        team_slug: str,
        name: str = "",
        description: str = "",
        privacy: str = "",
        permission: str = "",
    ) -> dict | list:
        """Update a team."""
        payload: dict = {}
        if name:
            payload["name"] = name
        if description:
            payload["description"] = description
        if privacy:
            payload["privacy"] = privacy
        if permission:
            payload["permission"] = permission
        return gh_patch(f"/orgs/{org}/teams/{team_slug}", json=payload)

    @mcp.tool()
    def delete_team(org: str, team_slug: str) -> dict | list:
        """Delete a team."""
        return gh_delete(f"/orgs/{org}/teams/{team_slug}")

    @mcp.tool()
    def list_team_members(org: str, team_slug: str, role: str = "all", per_page: int = 30, page: int = 1) -> dict | list:
        """List members of a team."""
        return gh_get(f"/orgs/{org}/teams/{team_slug}/members",
                      params={"role": role, "per_page": per_page, "page": page})

    @mcp.tool()
    def add_team_member(org: str, team_slug: str, username: str, role: str = "member") -> dict | list:
        """Add or update a team member. role: member|maintainer."""
        return gh_put(f"/orgs/{org}/teams/{team_slug}/memberships/{username}", json={"role": role})

    @mcp.tool()
    def remove_team_member(org: str, team_slug: str, username: str) -> dict | list:
        """Remove a member from a team."""
        return gh_delete(f"/orgs/{org}/teams/{team_slug}/memberships/{username}")

    @mcp.tool()
    def list_team_repos(org: str, team_slug: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List repositories for a team."""
        return gh_get(f"/orgs/{org}/teams/{team_slug}/repos",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def add_team_repo(org: str, team_slug: str, owner: str, repo: str, permission: str = "push") -> dict | list:
        """Add or update a repository for a team."""
        return gh_put(f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}", json={"permission": permission})

    @mcp.tool()
    def remove_team_repo(org: str, team_slug: str, owner: str, repo: str) -> dict | list:
        """Remove a repository from a team."""
        return gh_delete(f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}")
