"""French Governement Data Browser API"""

import logging as log
import threading

from api import app
from env import LOG_LEVEL
from client import client
from exceptions import DatasetBrowserException


if __name__ == "__main__":
    log.getLogger().setLevel(LOG_LEVEL)
    try:
        client.run()
        threading.Thread(target=app.run())
    except DatasetBrowserException as err:
        log.error("Terminating due to a fatal error: %s", err)
    except Exception as err:  # pylint: disable=broad-except
        log.error("Terminating due to an unknown error: %s", err)
    finally:
        client.close()
