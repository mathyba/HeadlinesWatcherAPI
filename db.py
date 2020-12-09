"""Database module

Connects to database upon import
"""

import logging as log
from time import time
from uuid import uuid4

from tinydb import TinyDB, Query

from env import DB_PATH
from exceptions import DatasetBrowserException


class _Database:
    """Database of recent major headline articles"""

    TinyDB.DEFAULT_TABLE = "Headline Articles"

    def __init__(self, file_path):
        """Get ready to connect to the database"""

        self.path = file_path
        self.exp_time = 3600 * 24
        self._store = None

    @property
    def store(self):
        """Use existing connection or open one"""

        if self._store is None:
            log.info("Open a connection to the database")
            self._store = TinyDB(self.path)
        return self._store

    def get_item(self, item_id):
        """Look up an item by id"""

        return self.store.search(Query()["id"] == int(item_id))

    def add_data(self, data):
        """Add data if not already in database

        If new article has no id, providex one and checkx presence by title
        Returns the number of added items
        """

        field = "title"
        article_id = int(uuid4())
        if hasattr(data, "id"):
            field = "id"
            article_id = data["id"]
        found = self.store.contains(Query()[field] == data[field])
        if not found:
            article_id = data["id"] if field == "id" else int(uuid4())
            log.info("Adding headling with id %s to database", article_id)
            self.store.insert(
                # {"details": data, "last_check": int(time()), "id": article_id}
                {**data, "last_check": int(time()), "id": article_id}
            )
            return 1
        return 0

    def update_dataset(self, dataset):
        """Retrieve a set of articles and update database content"""

        # Find and remove expired articles
        stored = lambda x: int(time()) > int((x + self.exp_time))
        exp_articles = self.store.search(Query()["last_check"].test(stored))
        log.info("Remove %s expired articles", len(exp_articles))
        self.store.remove(Query()["last_check"] < int(time() - self.exp_time))
        new = 0
        for article in dataset:
            new += self.add_data(article)
        log.info("Add %s new articles", new)

    def close(self):
        """Close the connection if any"""

        if self._store is not None:
            log.info("Closing connection to database")
            self._store.close()


try:
    db = _Database(DB_PATH)
except Exception as err:
    log.error("Terminating following a fatal error")
    raise DatasetBrowserException from err
finally:
    db.close()
