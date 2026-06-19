from typing import Any, Dict, Optional

from .slack_client import get_client


def team_info(team: Optional[str] = None, domain: Optional[str] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if team is not None:
        payload["team"] = team
    if domain is not None:
        payload["domain"] = domain
    return get_client().request("GET", "/team.info", json=payload)


def auth_test() -> Dict[str, Any]:
    return get_client().request("POST", "/auth.test", json={})
