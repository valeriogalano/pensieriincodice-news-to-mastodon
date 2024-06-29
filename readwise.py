import os

import requests
import logging

logger = logging.getLogger("readwise")


class Readwise:
    def __init__(self):
        self.readwise_api_key = os.environ["READWISE_ACCESS_TOKEN"]
        self.api_url = "https://readwise.io/api/v3/"

        logger.debug("Readwise inizializzato!")

    def get_published_documents(self, updated_after):
        response = self.get_documents(updated_after)
        logger.debug(f"Documenti da pubblicare: {response}")
        return self.__filter_tags(response)

    def get_documents(self, updated_after):
        url = f"{self.api_url}list/"
        headers = {"Authorization": f"Token {self.readwise_api_key}"}
        response = requests.get(
            url,
            params={"updatedAfter": updated_after},
            headers=headers
        )
        return response.json()

    @staticmethod
    def __filter_tags(response):
        to_return = []

        for document in response["results"]:
            if document["tags"] is None:
                continue

            if 'publish' in document["tags"].keys():
                to_return.append(document)

        return to_return
