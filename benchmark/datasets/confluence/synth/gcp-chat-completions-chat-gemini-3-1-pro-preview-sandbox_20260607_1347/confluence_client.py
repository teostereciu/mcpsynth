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

        self.session = requests.Session()
        self.session.auth = (self.email, self.api_token)
        self.session.headers.update({
            "Accept": "application/json"
        })

    def request(self, method: str, path: str, **kwargs) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        
        if "json" in kwargs:
            self.session.headers.update({"Content-Type": "application/json"})
            
        try:
            response = self.session.request(method, url, **kwargs)
            
            if response.status_code == 204:
                return {"success": True}
                
            if not response.ok:
                try:
                    error_data = response.json()
                    return {"error": f"HTTP {response.status_code}", "details": error_data}
                except ValueError:
                    return {"error": f"HTTP {response.status_code}", "details": response.text}
                    
            try:
                return response.json()
            except ValueError:
                return {"success": True, "text": response.text}
                
        except Exception as e:
            return {"error": str(e)}

client = ConfluenceClient()
