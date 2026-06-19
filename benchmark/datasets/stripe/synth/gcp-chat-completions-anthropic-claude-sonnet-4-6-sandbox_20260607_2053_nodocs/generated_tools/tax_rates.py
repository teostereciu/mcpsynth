"""
Stripe Tax Rates tools.
"""
import os
import requests

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "")
BASE_URL = "https://api.stripe.com/v1"


def _auth():
    return (STRIPE_API_KEY, "")


def _handle(resp: requests.Response) -> dict:
    try:
        return resp.json()
    except Exception:
        return {"error": resp.text}


def create_tax_rate(
    display_name: str,
    percentage: float,
    inclusive: bool,
    active: bool = None,
    country: str = None,
    description: str = None,
    jurisdiction: str = None,
    state: str = None,
    tax_type: str = None,
    metadata: dict = None,
) -> dict:
    """Create a Tax Rate."""
    data = {
        "display_name": display_name,
        "percentage": percentage,
        "inclusive": str(inclusive).lower(),
    }
    if active is not None:
        data["active"] = str(active).lower()
    if country:
        data["country"] = country
    if description:
        data["description"] = description
    if jurisdiction:
        data["jurisdiction"] = jurisdiction
    if state:
        data["state"] = state
    if tax_type:
        data["tax_type"] = tax_type
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/tax_rates", data=data, auth=_auth())
    return _handle(resp)


def get_tax_rate(tax_rate_id: str) -> dict:
    """Retrieve a Tax Rate by ID."""
    resp = requests.get(f"{BASE_URL}/tax_rates/{tax_rate_id}", auth=_auth())
    return _handle(resp)


def update_tax_rate(
    tax_rate_id: str,
    active: bool = None,
    display_name: str = None,
    description: str = None,
    jurisdiction: str = None,
    metadata: dict = None,
) -> dict:
    """Update a Tax Rate."""
    data = {}
    if active is not None:
        data["active"] = str(active).lower()
    if display_name:
        data["display_name"] = display_name
    if description:
        data["description"] = description
    if jurisdiction:
        data["jurisdiction"] = jurisdiction
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(
        f"{BASE_URL}/tax_rates/{tax_rate_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def list_tax_rates(
    active: bool = None,
    inclusive: bool = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    created_gte: int = None,
    created_lte: int = None,
) -> dict:
    """List Tax Rates."""
    params = {}
    if active is not None:
        params["active"] = str(active).lower()
    if inclusive is not None:
        params["inclusive"] = str(inclusive).lower()
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
    resp = requests.get(f"{BASE_URL}/tax_rates", params=params, auth=_auth())
    return _handle(resp)
