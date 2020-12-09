"""Headline Watcher API"""

import logging as log

import connexion

from db import db
from env import LOG_LEVEL
from exceptions import DatasetBrowserException


def get_dataset():
    """Return all data in articles database"""

    return db.store.all()


def get_headline(id_headline):
    """Return details for a target headline

    Returns 404 if ressource is unknown or invalid
    """
    try:
        item = db.get_item(id_headline)[0]
        return item
    except (ValueError, IndexError):
        return "Not found", 404, {"x-error": "not found"}


app = connexion.FlaskApp(__name__, debug=LOG_LEVEL == log.DEBUG)
app.add_api("swagger.yml")

if __name__ == "__main__":
    log.getLogger().setLevel(LOG_LEVEL)
    try:
        app.run()
    except DatasetBrowserException as err:
        log.error("Terminating after a Fatal error")
    finally:
        db.store.close()
