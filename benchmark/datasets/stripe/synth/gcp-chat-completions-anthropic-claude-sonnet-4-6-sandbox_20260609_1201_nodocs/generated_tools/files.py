"""
Stripe Files & File Links tools.
Endpoints covered:
  GET    /v1/files/{id}
  GET    /v1/files
  POST   /v1/file_links
  GET    /v1/file_links/{id}
  POST   /v1/file_links/{id}
  GET    /v1/file_links
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def get_file(file_id: str) -> dict:
        """Retrieve a File by ID."""
        return stripe_request("GET", f"/v1/files/{file_id}")

    @mcp.tool()
    def list_files(
        purpose: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        created_gte: int = None,
        created_lte: int = None,
    ) -> dict:
        """
        List Files.
        purpose: account_requirement | additional_verification | business_icon |
                 business_logo | customer_signature | dispute_evidence | document_provider_identity_document |
                 finance_report_run | identity_document | pci_document | sigma_scheduled_query | tax_document_user_upload
        """
        params = {}
        if purpose:
            params["purpose"] = purpose
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        if created_gte is not None:
            params["created[gte]"] = created_gte
        if created_lte is not None:
            params["created[lte]"] = created_lte
        return stripe_request("GET", "/v1/files", params=params)

    @mcp.tool()
    def create_file_link(
        file: str,
        expires_at: int = None,
        metadata: dict = None,
    ) -> dict:
        """Create a File Link to make a File publicly accessible."""
        data = {"file": file}
        if expires_at is not None:
            data["expires_at"] = expires_at
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/file_links", data=data)

    @mcp.tool()
    def get_file_link(file_link_id: str) -> dict:
        """Retrieve a File Link by ID."""
        return stripe_request("GET", f"/v1/file_links/{file_link_id}")

    @mcp.tool()
    def update_file_link(
        file_link_id: str,
        expires_at: int = None,
        metadata: dict = None,
    ) -> dict:
        """Update a File Link's expiry or metadata. Set expires_at=0 to remove expiry."""
        data = {}
        if expires_at is not None:
            data["expires_at"] = expires_at if expires_at != 0 else "now"
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/file_links/{file_link_id}", data=data)

    @mcp.tool()
    def list_file_links(
        file: str = None,
        expired: bool = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List File Links."""
        params = {}
        if file:
            params["file"] = file
        if expired is not None:
            params["expired"] = str(expired).lower()
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return stripe_request("GET", "/v1/file_links", params=params)
