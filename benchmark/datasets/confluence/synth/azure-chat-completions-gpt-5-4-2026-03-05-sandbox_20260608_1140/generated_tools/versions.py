from typing import Any, Optional

from confluence_client import client


def restore_content_version(
    content_id: str,
    version_number: int,
    message: Optional[str] = None,
    restore_title: Optional[bool] = None,
    expand: Optional[list[str]] = None,
) -> Any:
    return client.request(
        "POST",
        f"/rest/api/content/{content_id}/version",
        params={"expand": expand},
        json_body={
            "operationKey": "restore",
            "params": {
                "versionNumber": version_number,
                "message": message,
                "restoreTitle": restore_title,
            },
        },
    )


def delete_content_version(content_id: str, version_number: int) -> Any:
    return client.request(
        "DELETE",
        f"/rest/api/content/{content_id}/version/{version_number}",
    )
