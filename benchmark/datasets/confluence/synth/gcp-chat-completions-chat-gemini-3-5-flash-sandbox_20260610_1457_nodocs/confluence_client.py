import os
import requests
from requests.auth import HTTPBasicAuth
from typing import Any, Dict, Optional, Union

class ConfluenceClient:
    def __init__(self):
        self.base_url = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
        self.email = os.environ.get("JIRA_EMAIL", "")
        self.api_token = os.environ.get("JIRA_API_TOKEN", "")
        self.default_space_key = os.environ.get("CONFLUENCE_SPACE_KEY", "")

        if not self.base_url:
            raise ValueError("CONFLUENCE_BASE_URL environment variable is required.")
        if not self.email or not self.api_token:
            raise ValueError("JIRA_EMAIL and JIRA_API_TOKEN environment variables are required.")

        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(self.email, self.api_token)
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

    def request(self, method: str, path: str, **kwargs) -> Dict[str, Any]:
        """
        Make an HTTP request to the Confluence API.
        path should start with /rest/api/ or /api/v2/
        """
        url = f"{self.base_url}{path}"
        try:
            response = self.session.request(method, url, **kwargs)
            if response.status_code == 204:
                return {"success": True}
            
            try:
                data = response.json()
            except ValueError:
                data = {"text": response.text}

            if not response.ok:
                error_msg = data.get("message") or data.get("error") or response.reason
                return {
                    "error": f"HTTP {response.status_code}: {error_msg}",
                    "status_code": response.status_code,
                    "details": data
                }
            return data
        except Exception as e:
            return {"error": f"Request failed: {str(e)}"}

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self.request("GET", path, params=params)

    def post(self, path: str, json_data: Optional[Any] = None, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        kwargs = {}
        if json_data is not None:
            kwargs["json"] = json_data
        if headers is not None:
            kwargs["headers"] = headers
        return self.request("POST", path, **kwargs)

    def put(self, path: str, json_data: Optional[Any] = None) -> Dict[str, Any]:
        return self.request("PUT", path, json=json_data)

    def delete(self, path: str) -> Dict[str, Any]:
        return self.request("DELETE", path)

    def resolve_space_id(self, space_key: str) -> Union[str, Dict[str, Any]]:
        """
        Resolve a space key (e.g. 'SYNTH') to a space ID.
        Returns the space ID string, or an error dict if not found.
        """
        if not space_key:
            return {"error": "Space key is required"}
        
        # Try v2 spaces endpoint with keys filter
        res = self.get("/api/v2/spaces", params={"keys": space_key})
        if "error" in res:
            return res
        
        results = res.get("results", [])
        if not results:
            # Fallback to v1 space endpoint
            res_v1 = self.get(f"/rest/api/space/{space_key}")
            if "error" in res_v1:
                return {"error": f"Space with key '{space_key}' not found."}
            # v1 space object doesn't have numeric ID in the same place, but let's see if we can get it
            # Actually, v1 space response has an 'id' field in some versions, or we can use the key.
            # Let's check if v1 returns id.
            space_id = res_v1.get("id")
            if space_id:
                return str(space_id)
            return {"error": f"Could not resolve space key '{space_key}' to an ID."}
        
        return str(results[0]["id"])

    def resolve_space_key(self, space_id: str) -> Union[str, Dict[str, Any]]:
        """
        Resolve a space ID to a space key.
        """
        res = self.get(f"/api/v2/spaces/{space_id}")
        if "error" in res:
            return res
        return res.get("key", "")
