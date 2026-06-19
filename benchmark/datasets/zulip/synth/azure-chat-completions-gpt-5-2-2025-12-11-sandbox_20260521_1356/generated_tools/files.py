from typing import Any, Dict

from .client import ZulipClient


def upload_file(client: ZulipClient, file_path: str, form_field_name: str = "filename") -> Dict[str, Any]:
    url = client.base + "/user_uploads"
    try:
        with open(file_path, "rb") as f:
            files = {form_field_name: (file_path.split("/")[-1], f)}
            resp = client.session.post(url, files=files, timeout=60)
    except OSError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}

    try:
        data = resp.json()
    except ValueError:
        return {"error": f"Non-JSON response (status {resp.status_code})", "text": resp.text}

    if resp.status_code >= 400 or data.get("result") == "error":
        return {"error": data.get("msg") or f"HTTP {resp.status_code}", "data": data, "status": resp.status_code}
    return data


def get_file_temporary_url(client: ZulipClient, realm_id_str: int, filename: str) -> Dict[str, Any]:
    return client.request("GET", f"/user_uploads/{realm_id_str}/{filename}")
