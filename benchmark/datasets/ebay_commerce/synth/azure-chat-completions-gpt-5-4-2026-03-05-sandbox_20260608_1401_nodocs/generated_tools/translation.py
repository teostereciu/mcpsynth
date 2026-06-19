from typing import Any, Dict

from .common import client


def translate(body: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/commerce/translation/v1_beta/translate", "app", json_body=body)
