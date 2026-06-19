from typing import Any, Dict, List
from .common import get_base_url, get_token, request_json


def create_document(document_type: str, languages: List[str]) -> Dict[str, Any]:
    token = get_token("refresh_token").get("access_token")
    if not token:
        return {"error": "unable to obtain user token"}
    body = {"documentType": document_type, "languages": languages}
    return request_json("POST", f"{get_base_url(True)}/commerce/media/v1_beta/document", token, json_body=body, headers={"Content-Type": "application/json"})
