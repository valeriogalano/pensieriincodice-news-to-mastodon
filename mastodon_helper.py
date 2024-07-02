import logging
import os

from requests_oauthlib import OAuth1Session, OAuth1
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

    def _get_oauth_session(self):
        oauth = OAuth1(
            client_key=os.environ['MASTODON_CLIENT_ID'],
            client_secret=os.environ['MASTODON_CLIENT_SECRET'],
            resource_owner_key=self.token,
            signature_method='HMAC-SHA1',
        )

        return OAuth1Session(oauth)

    def __send_mastodon_post(self, status: str):
        session = self._get_oauth_session()
        response = session.post(
            f'{API_URL}/api/v1/statuses', params={'status': TWEET_PARSER.parse(status)},
            json={"visibility": "public"}
        )

        if response.status_code != 200:
            raise Exception(f"Error sending status: {response.text}")

    def post(self, status):
        self.__send_mastodon_post(status)
