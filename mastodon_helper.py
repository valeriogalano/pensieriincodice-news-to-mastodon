import logging
import os

import requests
from tweepy.parsers import JSONParser

TWEET_PARSER = JSONParser()
TOKEN_ENDPOINT = "https://api.mastodon.social/oauth/token"
AUTHORIZE_ENDPOINT = "https://api.mastodon.social/oauth/authorize"
API_URL = 'https://api.mastodon.social'

logger = logging.getLogger("mastodon")


class MastodonHelper:
    token = None

    def __init__(self):
        self.token = os.environ["MASTODON_TOKEN"]

        logger.debug("Mastodon helper inizializzato!")

    def __send_mastodon_post(self, status: str):
        response = requests.post(
            "https://mastodon.social/api/v1/statuses",
            headers={
                "Authorization": f"Bearer {self.token}"
            },
            json={
                'status': TWEET_PARSER.parse(status)
            }
        )

        if response.status_code != 201:
            raise Exception(f"Error sending status: {response.text}")

    def post(self, status):
        self.__send_mastodon_post(status)
