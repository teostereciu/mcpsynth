from typing import Any, Dict, Optional

from .slack_client import SlackWebAPIClient, _clean_dict


def team_info(
    team: Optional[str] = None,
    domain: Optional[str] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    params = _clean_dict({"team": team, "domain": domain})
    return client.get("team.info", params)
