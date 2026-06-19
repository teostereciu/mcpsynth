import os
import requests
from typing import Any, Dict, Optional

class JiraClient:
    def __init__(self):
        self.base_url = os.getenv("JIRA_BASE_URL")
        self.email = os.getenv("JIRA_EMAIL")
        self.api_token = os.getenv("JIRA_API_TOKEN")
        
        if not self.base_url:
            raise ValueError("JIRA_BASE_URL environment variable is required")
        if not self.email:
            raise ValueError("JIRA_EMAIL environment variable is required")
        if not self.api_token:
            raise ValueError("JIRA_API_TOKEN environment variable is required")
            
        # Normalize base URL
        self.base_url = self.base_url.rstrip("/")
        if not self.base_url.endswith("/rest/api/3"):
            # If it's just the domain, append /rest/api/3
            if "/rest/api/3" not in self.base_url:
                self.base_url = f"{self.base_url}/rest/api/3"
                
        self.session = requests.Session()
        self.session.auth = (self.email, self.api_token)
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

    def request(self, method: str, path: str, params: Optional[Dict[str, Any]] = None, json_data: Optional[Any] = None, data: Optional[Any] = None, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{path.lstrip('/')}"
        
        # If headers are provided, merge them
        req_headers = {}
        if headers:
            req_headers.update(headers)

        try:
            # For multipart/form-data (like attachments), we shouldn't force Content-Type to application/json
            if data is not None or "Content-Type" in req_headers:
                # Let requests handle Content-Type for files, or use custom headers
                response = self.session.request(
                    method=method,
                    url=url,
                    params=params,
                    data=data,
                    headers=req_headers if req_headers else None
                )
            else:
                response = self.session.request(
                    method=method,
                    url=url,
                    params=params,
                    json=json_data
                )
            
            # Handle empty response
            if response.status_code == 204:
                return {"status": "success", "message": "Operation completed successfully with no content returned."}
                
            if not response.text:
                return {"status": "success", "statusCode": response.status_code}

            try:
                res_json = response.json()
                if not response.ok:
                    return {
                        "error": f"HTTP {response.status_code} Error",
                        "details": res_json
                    }
                return res_json
            except ValueError:
                if response.ok:
                    return {"status": "success", "text": response.text}
                return {
                    "error": f"HTTP {response.status_code} Error",
                    "details": response.text
                }
        except Exception as e:
            return {"error": f"Request failed: {str(e)}"}

client = None

def get_client() -> JiraClient:
    global client
    if client is None:
        client = JiraClient()
    return client
