import os
import requests
from typing import Any, Dict, Optional

class ConfluenceClient:
    def __init__(self):
        self.base_url = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
        self.space_key = os.environ.get("CONFLUENCE_SPACE_KEY", "")
        self.email = os.environ.get("JIRA_EMAIL", "")
        self.api_token = os.environ.get("JIRA_API_TOKEN", "")
        
        if not self.base_url or not self.email or not self.api_token:
            raise ValueError("Missing required environment variables: CONFLUENCE_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN")

    def request(self, method: str, path: str, params: Optional[Dict] = None, json_data: Optional[Dict] = None, data: Any = None, headers: Optional[Dict] = None) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        auth = (self.email, self.api_token)
        
        req_headers = {"Accept": "application/json"}
        if json_data is not None:
            req_headers["Content-Type"] = "application/json"
        if headers:
            req_headers.update(headers)
            
        try:
            response = requests.request(
                method=method,
                url=url,
                auth=auth,
                params=params,
                json=json_data,
                data=data,
                headers=req_headers
            )
            
            if response.status_code == 204:
                return {"success": True}
                
            if response.headers.get("Content-Type", "").startswith("application/json"):
                data = response.json()
                if not response.ok:
                    return {"error": f"HTTP {response.status_code}", "details": data}
                return data
            else:
                if not response.ok:
                    return {"error": f"HTTP {response.status_code}", "details": response.text}
                return {"success": True, "content": response.text}
                
        except Exception as e:
            return {"error": str(e)}

client = ConfluenceClient()
