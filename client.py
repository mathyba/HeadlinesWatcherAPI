"""French Governement Data Browser API"""

import logging as log
import time

import httpx

from env import SECRET_KEY, BASE_URL, LOG_LEVEL, REFRESH_RATE, COUNTRY
from exceptions import DatasetBrowserException


class _Client:
    """Client for requests to a target API"""

    def __init__(self, base_url, secret_key, country="FR", refresh=300):
        """Get ready to interact with the source API"""

        self._base_url = base_url
        self._secret_key = secret_key
        self._headers = {"x-api-key": self._secret_key}
        self._session = None
        self._refresh_rate = refresh
        self._url = {"country": (country).lower()}

    @property
    def session(self):
        """Use existing connection if any, or create a fresh one"""

        if self._session is None:
            log.info("Instanciate an HTTP connection with the target API")
            self._session = httpx.Client(headers=self._headers)
        return self._session

    @property
    def url(self):
        """Complete URL

        Returns URL with base url, parametrized endpoint and secret key
        """

        full_url = f"{self._base_url}?" + "&".join(
            [f"{key}={value}" for key, value in self._url.items()]
        )
        return full_url

    def _get(self):
        """Make a GET request

        Returns response json if request successful
        Raises exception in case of error
        """

        try:
            log.debug("Making GET request to url %s", self.url)
            r_get = self.session.get(self.url).json()
            log.info(r_get)
            if r_get["status"] == "error":
                log.error("There was a problem with a GET request: %s", r_get)
                raise DatasetBrowserException from Exception
            return r_get
        except httpx.RequestError as err:
            log.error("Unable to complete GET request")
            raise DatasetBrowserException from err

    def run(self):
        """Start queries to retrieve headlines at predefined intervals"""

        while True:
            r_data = self._get()
            log.info("Going asleep for %s seconds", self._refresh_rate)
            log.debug(r_data)
            time.sleep(self._refresh_rate)

    def close(self):
        """Close down HTTP session if active"""

        if self._session is not None:
            log.info("Closing HTTP session")
            self._session.close()
            self._session = None


log.getLogger().setLevel(LOG_LEVEL)
client = _Client(BASE_URL.rstrip(), SECRET_KEY, COUNTRY, REFRESH_RATE)

if __name__ == "__main__":
    try:
        client.run()
    except Exception as err:
        log.error("Terminating after fatal error: %s", err)
        raise DatasetBrowserException from err
    finally:
        client.session.close()
