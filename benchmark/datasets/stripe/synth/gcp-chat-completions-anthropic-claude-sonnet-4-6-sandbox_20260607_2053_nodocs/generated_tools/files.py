"""
Stripe Files and File Links tools.
"""
import os
import requests

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "")
BASE_URL = "https://api.stripe.com/v1"
FILES_URL = "https://files.stripe.com/v1"


def _auth():
    return (STRIPE_API_KEY, "")


def _handle(resp: requests.Response) -> dict:
    try:
        return resp.json()
    except Exception:
        return {"error": resp.text}


def upload_file(file_path: str, purpose: str) -> dict:
    """
    Upload a File to Stripe.
    purpose: 'dispute_evidence', 'identity_document', 'tax_document_user_upload', etc.
    file_path: local path to the file to upload.
    """
    try:
        with open(file_path, "rb") as f:
            resp = requests.post(
                f"{FILES_URL}/files",
                data={"purpose": purpose},
                files={"file": f},
                auth=_auth(),
            )
        return _handle(resp)
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}


def get_file(file_id: str) -> dict:
    """Retrieve a File by ID."""
    resp = requests.get(f"{BASE_URL}/files/{file_id}", auth=_auth())
    return _handle(resp)


def list_files(
    purpose: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    created_gte: int = None,
    created_lte: int = None,
) -> dict:
    """List Files."""
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
    resp = requests.get(f"{BASE_URL}/files", params=params, auth=_auth())
    return _handle(resp)


def create_file_link(
    file: str,
    expires_at: int = None,
    metadata: dict = None,
) -> dict:
    """Create a File Link for a File."""
    data = {"file": file}
    if expires_at is not None:
        data["expires_at"] = expires_at
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/file_links", data=data, auth=_auth())
    return _handle(resp)


def get_file_link(file_link_id: str) -> dict:
    """Retrieve a File Link by ID."""
    resp = requests.get(f"{BASE_URL}/file_links/{file_link_id}", auth=_auth())
    return _handle(resp)


def update_file_link(
    file_link_id: str,
    expires_at: int = None,
    metadata: dict = None,
) -> dict:
    """Update a File Link."""
    data = {}
    if expires_at is not None:
        data["expires_at"] = expires_at
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(
        f"{BASE_URL}/file_links/{file_link_id}", data=data, auth=_auth()
    )
    return _handle(resp)


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
    resp = requests.get(f"{BASE_URL}/file_links", params=params, auth=_auth())
    return _handle(resp)
