from generated_tools.common import mastodon_request


def get_poll(poll_id: str):
    return mastodon_request("GET", f"/api/v1/polls/{poll_id}")


def vote_poll(poll_id: str, choices: list[int]):
    return mastodon_request("POST", f"/api/v1/polls/{poll_id}/votes", data={"choices[]": choices})
