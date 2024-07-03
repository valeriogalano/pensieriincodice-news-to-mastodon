import logging
import os

import requests

API_URL = 'https://mastodon.uno'

logger = logging.getLogger("mastodon")


class MastodonHelper:
    token = None

    def __init__(self):
        self.token = os.environ["MASTODON_TOKEN"]

        logger.debug("Mastodon helper inizializzato!")

    def __send_mastodon_post(self, status: str):
        response = requests.post(
            f"{API_URL}/api/v1/statuses",
            headers={
                "Authorization": f"Bearer {self.token}"
            },
            json={
                'status': status
            }
        )

        if response.status_code != 201:
            raise Exception(f"Error sending status: {response.text}")

    def post(self, status):
        self.__send_mastodon_post(status)
