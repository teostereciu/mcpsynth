from typing import Any, Dict, List, Optional

from ._client import get_client


def list_organizations(
    page: Optional[int] = None,
    per_page: Optional[int] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /api/v2/organizations"""
    client = get_client()
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if per_page is not None:
        params["per_page"] = per_page
    if sort is not None:
        params["sort"] = sort
    return client.request("GET", f"{client.base_support}/organizations", params=params)  # type: ignore


def show_organization(organization_id: int) -> Dict[str, Any]:
    """GET /api/v2/organizations/{organization_id}"""
    client = get_client()
    return client.request("GET", f"{client.base_support}/organizations/{organization_id}")  # type: ignore


def show_many_organizations(ids: List[int]) -> Dict[str, Any]:
    """GET /api/v2/organizations/show_many?ids=..."""
    client = get_client()
    params = {"ids": ",".join(str(i) for i in ids)}
    return client.request("GET", f"{client.base_support}/organizations/show_many", params=params)  # type: ignore


def search_organizations(query: str) -> Dict[str, Any]:
    """GET /api/v2/organizations/search?query=..."""
    client = get_client()
    return client.request(
        "GET", f"{client.base_support}/organizations/search", params={"query": query}
    )  # type: ignore


def autocomplete_organizations(name: str) -> Dict[str, Any]:
    """GET /api/v2/organizations/autocomplete?name=..."""
    client = get_client()
    return client.request(
        "GET", f"{client.base_support}/organizations/autocomplete", params={"name": name}
    )  # type: ignore


def create_organization(organization: Dict[str, Any]) -> Dict[str, Any]:
    """POST /api/v2/organizations

    Body: {"organization": {...}}
    """
    client = get_client()
    return client.request(
        "POST", f"{client.base_support}/organizations", json={"organization": organization}
    )  # type: ignore


def update_organization(organization_id: int, organization: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /api/v2/organizations/{organization_id}

    Body: {"organization": {...}}
    """
    client = get_client()
    return client.request(
        "PUT",
        f"{client.base_support}/organizations/{organization_id}",
        json={"organization": organization},
    )  # type: ignore


def delete_organization(organization_id: int) -> Dict[str, Any]:
    """DELETE /api/v2/organizations/{organization_id}"""
    client = get_client()
    return client.request("DELETE", f"{client.base_support}/organizations/{organization_id}")  # type: ignore


def merge_organization(into_organization_id: int, from_organization_id: int) -> Dict[str, Any]:
    """POST /api/v2/organizations/{into_organization_id}/merge

    Body: {"organization_id": from_organization_id}
    """
    client = get_client()
    return client.request(
        "POST",
        f"{client.base_support}/organizations/{into_organization_id}/merge",
        json={"organization_id": from_organization_id},
    )  # type: ignore
