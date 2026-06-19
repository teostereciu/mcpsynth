from typing import Any, Dict, Optional

from .slack_client import SlackWebAPIClient, _clean_dict


def auth_test(client: Optional[SlackWebAPIClient] = None) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    return client.post("auth.test", {})
