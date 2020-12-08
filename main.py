"""French Governement Data Browser API"""

import logging as log

from client import gov_api
from env import LOG_LEVEL
from exceptions import DatasetBrowserException


if __name__ == "__main__":
    log.getLogger().setLevel(LOG_LEVEL)
    try:
        resp = gov_api.get_datasets()
        log.debug(resp)
    except DatasetBrowserException as err:
        log.error("Terminating due to a fatal error: %s", err)
    except Exception as err:  # pylint: disable=broad-except
        log.error("Terminating due to an unknown error: %s", err)
    finally:
        gov_api.close()
