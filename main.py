"""French Governement Data Browser API"""

import logging as log

import httpx

from env import API_KEY, API_URL, LOG_LEVEL
from exceptions import DatasetBrowserException


class SourceApi:
    """Everything to interact with the source API"""

    def __init__(self):
        """Get ready to interact with the source API"""
        self._base_url = API_URL.rstrip("/")
        self.secret_key = API_KEY
        self.headers = {"X-API-KEY": API_KEY}
        self._session = None
        self.endpoint = None

    @property
    def session(self):
        """Use existing connection if any, or create a fresh one"""

        if self._session is None:
            log.info("Instanciate an HTTP connection with the target API")
            self._session = httpx.Client(headers=self.headers)
        log.debug("HTTP session already active")
        return self._session

    def url(self):
        """Complete URL"""

        return self._base_url + self.endpoint

    def _get(self):
        """Make a GET request"""
        try:
            res = self.session.get(self.url)
            res.raise_for_status()
            log.info(resp)
        except httpx.RequestError as err:
            log.error("The request to %s failed: %s", self.url, err)
            raise DatasetBrowserException from err

    def get_datasets(self):
        """Collect datasets from source API"""
        log.info("Preparing to retrieve datasets from source API")
        self.endpoint = "/datasets"
        return self._get()

    def close(self):
        """Close down HTTP session if active"""
        if self._session is not None:
            log.info("Closing HTTP session")
            self._session.close()
            self._session = None


if __name__ == "__main__":
    log.getLogger().setLevel(LOG_LEVEL)
    try:
        api = SourceApi()
        resp = api.get_datasets()
        log.debug(resp)
    except DatasetBrowserException as err:
        log.error("Terminating due to a fatal error: %s", err)
    except Exception as err:  # pylint: disable=broad-except
        log.error("Terminating due to an unknown error: %s", err)
    finally:
        api.close()