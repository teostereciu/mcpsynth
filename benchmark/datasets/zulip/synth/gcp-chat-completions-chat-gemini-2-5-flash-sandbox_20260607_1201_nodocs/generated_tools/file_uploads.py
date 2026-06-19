from typing import BinaryIO

def upload_file(client, file: BinaryIO, file_name: str):
    """Upload a file to Zulip.

    Args:
        client: The Zulip API client.
        file: The file object (binary) to upload.
        file_name: The name of the file.
    """
    files = {
        'file': (file_name, file, 'application/octet-stream')
    }
    return client._request("POST", "/user_uploads", files=files)
