import os
import requests
from fastmcp.server.fastmcp import FastMCP

# Environment variables for Zulip authentication
ZULIP_EMAIL = os.getenv("ZULIP_EMAIL")
ZULIP_API_KEY = os.getenv("ZULIP_API_KEY")
ZULIP_SITE = os.getenv("ZULIP_SITE")

if not all([ZULIP_EMAIL, ZULIP_API_KEY, ZULIP_SITE]):
    raise ValueError("ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables must be set.")

BASE_URL = f"{ZULIP_SITE}/api/v1"

class ZulipClient:
    def __init__(self, email, api_key, base_url):
        self.auth = (email, api_key)
        self.base_url = base_url

    def _request(self, method, path, **kwargs):
        url = f"{self.base_url}{path}"
        try:
            response = requests.request(method, url, auth=self.auth, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            return {"error": f"HTTP error: {e.response.status_code} - {e.response.text}"}
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {e}"}

zulip_client = ZulipClient(ZULIP_EMAIL, ZULIP_API_KEY, BASE_URL)
app = FastMCP()

from generated_tools import messages
from generated_tools import streams
from generated_tools import topics
from generated_tools import users
from generated_tools import reactions
from generated_tools import scheduled_messages
from generated_tools import file_uploads

# Tools will be registered here
app.register_tool(messages.send_message)
app.register_tool(messages.get_message_history)
app.register_tool(messages.edit_message)
app.register_tool(messages.delete_message)
app.register_tool(messages.update_message_flags)
app.register_tool(streams.create_stream)
app.register_tool(streams.subscribe_to_stream)
app.register_tool(streams.archive_stream)
app.register_tool(streams.update_stream_settings)
app.register_tool(topics.get_topics_in_stream)
app.register_tool(topics.rename_topic)
app.register_tool(users.get_user_profile)
app.register_tool(users.get_user_presence)
app.register_tool(reactions.add_reaction)
app.register_tool(reactions.remove_reaction)
app.register_tool(scheduled_messages.schedule_message)
app.register_tool(file_uploads.upload_file)

if __name__ == "__main__":
    app.run()
