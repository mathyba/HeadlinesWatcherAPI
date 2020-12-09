"""Environment for Headlines Watcher API"""

import os
import logging as log

from dotenv import load_dotenv

# Make KEY=value pairs in .env available as system env variables
load_dotenv(override=True)

BASE_URL = "https://newsapi.org/v2/top-headlines"
SECRET_KEY = os.getenv("SECRET_KEY", "YOUR_SECRET_KEY")
DB_PATH = "db.json"
LOG_LEVEL = log.DEBUG if os.getenv("DEBUG") else log.INFO
REFRESH_RATE = int(os.getenv("REFRESH_RATE", "300"))
EXP_TIME = int(os.getenv("EXP_TIME", "86400"))  # default 24h
COUNTRY = os.getenv("COUNTRY", "CA")
