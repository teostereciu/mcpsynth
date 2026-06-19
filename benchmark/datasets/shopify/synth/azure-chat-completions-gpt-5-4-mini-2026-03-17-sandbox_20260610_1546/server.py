from mcp.server.fastmcp import FastMCP
import os, json, urllib.request, urllib.error

mcp = FastMCP("shopify-admin-rest")
BASE_URL = f"https://{os.environ.get('SHOPIFY_STORE_URL','')}/admin/api/2026-01"
TOKEN = os.environ.get('SHOPIFY_ACCESS_TOKEN','')


def _request(method, path, params=None, body=None):
    url = BASE_URL + path
    if params:
        from urllib.parse import urlencode
        url += "?" + urlencode(params, doseq=True)
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-Shopify-Access-Token', TOKEN)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


@mcp.tool()
def shopify_request(method: str, path: str, params: dict | None = None, body: dict | None = None):
    return _request(method, path, params, body)


if __name__ == '__main__':
    mcp.run()
