"""
Zulip MCP Tools — Realm / Organisation domain
Covers: realm info, settings, emoji, linkifiers, filters, profile fields, invitations
"""
import os, requests
from mcp.server.fastmcp import FastMCP


def _client():
    email   = os.environ["ZULIP_EMAIL"]
    api_key = os.environ["ZULIP_API_KEY"]
    site    = os.environ["ZULIP_SITE"].rstrip("/")
    base    = f"{site}/api/v1"
    return base, (email, api_key)


def register_realm_tools(mcp: FastMCP):

    @mcp.tool()
    def get_realm_info() -> dict:
        """Get basic information about the Zulip organisation (realm)."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/realm", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_server_settings() -> dict:
        """Get server-level settings (no authentication required)."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/server_settings", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_realm_emoji() -> dict:
        """List all custom emoji defined in the organisation."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/realm/emoji", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def upload_realm_emoji(emoji_name: str, file_path: str) -> dict:
        """Upload a new custom emoji for the organisation.

        Args:
            emoji_name: The name for the new emoji (alphanumeric and hyphens).
            file_path: Path to the image file (PNG, JPG, or GIF).
        """
        base, auth = _client()
        try:
            with open(file_path, "rb") as fh:
                r = requests.post(
                    f"{base}/realm/emoji/{emoji_name}",
                    files={"f": fh},
                    auth=auth,
                )
            return r.json()
        except FileNotFoundError:
            return {"error": f"File not found: {file_path}"}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_realm_emoji(emoji_name: str) -> dict:
        """Delete a custom emoji from the organisation.

        Args:
            emoji_name: The name of the emoji to delete.
        """
        base, auth = _client()
        try:
            r = requests.delete(f"{base}/realm/emoji/{emoji_name}", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_realm_linkifiers() -> dict:
        """List all linkifier (URL pattern) rules for the organisation."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/realm/linkifiers", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def add_realm_linkifier(pattern: str, url_template: str) -> dict:
        """Add a new linkifier rule to the organisation.

        Args:
            pattern: A Python regular expression to match in messages.
            url_template: The URL template to expand matches into
                          (use %(name)s for named groups).
        """
        base, auth = _client()
        try:
            r = requests.post(
                f"{base}/realm/linkifiers",
                data={"pattern": pattern, "url_template": url_template},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_realm_linkifier(
        filter_id: int, pattern: str, url_template: str
    ) -> dict:
        """Update an existing linkifier rule.

        Args:
            filter_id: The numeric ID of the linkifier to update.
            pattern: New regex pattern.
            url_template: New URL template.
        """
        base, auth = _client()
        try:
            r = requests.patch(
                f"{base}/realm/linkifiers/{filter_id}",
                data={"pattern": pattern, "url_template": url_template},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_realm_linkifier(filter_id: int) -> dict:
        """Delete a linkifier rule from the organisation.

        Args:
            filter_id: The numeric ID of the linkifier to delete.
        """
        base, auth = _client()
        try:
            r = requests.delete(f"{base}/realm/linkifiers/{filter_id}", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_realm_profile_fields() -> dict:
        """List all custom profile fields defined in the organisation."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/realm/profile_fields", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def create_realm_profile_field(
        name: str,
        field_type: int,
        hint: str = "",
        field_data: str = "",
    ) -> dict:
        """Create a new custom profile field for the organisation.

        Args:
            name: Display name of the field.
            field_type: Integer type — 1=short text, 2=long text, 3=list of options,
                        4=date, 5=link, 6=person, 7=pronouns.
            hint: Optional hint text shown below the field.
            field_data: JSON string with field-specific data (e.g. options for type 3).
        """
        base, auth = _client()
        payload: dict = {"name": name, "field_type": field_type}
        if hint:
            payload["hint"] = hint
        if field_data:
            payload["field_data"] = field_data
        try:
            r = requests.post(f"{base}/realm/profile_fields", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_realm_profile_field(field_id: int) -> dict:
        """Delete a custom profile field from the organisation.

        Args:
            field_id: The numeric ID of the profile field to delete.
        """
        base, auth = _client()
        try:
            r = requests.delete(f"{base}/realm/profile_fields/{field_id}", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_realm_filters() -> dict:
        """List all code-playground filters for the organisation."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/realm/playgrounds", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def add_realm_playground(
        name: str,
        pygments_language: str,
        url_template: str,
    ) -> dict:
        """Add a code playground to the organisation.

        Args:
            name: Display name for the playground.
            pygments_language: The Pygments language identifier (e.g. 'Python').
            url_template: URL template for the playground (use %(code)s for the code).
        """
        base, auth = _client()
        payload = {
            "name": name,
            "pygments_language": pygments_language,
            "url_template": url_template,
        }
        try:
            r = requests.post(f"{base}/realm/playgrounds", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_realm_playground(playground_id: int) -> dict:
        """Delete a code playground from the organisation.

        Args:
            playground_id: The numeric ID of the playground to delete.
        """
        base, auth = _client()
        try:
            r = requests.delete(
                f"{base}/realm/playgrounds/{playground_id}", auth=auth
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def send_realm_invitation(
        emails: str,
        invite_expires_in_minutes: int = 10080,
        invite_as: int = 400,
        stream_ids: str = "[]",
    ) -> dict:
        """Send email invitations to join the organisation.

        Args:
            emails: Comma-separated list of email addresses to invite.
            invite_expires_in_minutes: Expiry time in minutes (default 7 days = 10080).
            invite_as: Role for invited users — 400=member (default), 600=guest.
            stream_ids: JSON list of stream IDs to auto-subscribe invitees to.
        """
        base, auth = _client()
        payload = {
            "invitee_emails": emails,
            "invite_expires_in_minutes": invite_expires_in_minutes,
            "invite_as": invite_as,
            "stream_ids": stream_ids,
        }
        try:
            r = requests.post(f"{base}/invites", data=payload, auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_invitations() -> dict:
        """List all pending invitations for the organisation (admin only)."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/invites", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def revoke_invitation(invite_id: int) -> dict:
        """Revoke a pending email invitation.

        Args:
            invite_id: The numeric ID of the invitation to revoke.
        """
        base, auth = _client()
        try:
            r = requests.delete(f"{base}/invites/{invite_id}", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_realm_export() -> dict:
        """List all data exports for the organisation (admin only)."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/export/realm", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def create_realm_export() -> dict:
        """Initiate a new data export for the organisation (admin only)."""
        base, auth = _client()
        try:
            r = requests.post(f"{base}/export/realm", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}
