"""Environment for Headlines Watcher API"""

import os
import logging as log

from dotenv import load_dotenv

# Make KEY=value pairs in .env available as system env variables
load_dotenv(override=True)

BASE_URL = "https://newsapi.org/v2/top-headlines"
SECRET_KEY = os.getenv("SECRET_KEY", "YOUR_SECRET_KEY")
LOG_LEVEL = log.DEBUG if os.getenv("DEBUG") else log.INFO
REFRESH_RATE = int(os.getenv("REFRESH_RATE", "300"))
COUNTRY = os.getenv("COUNTRY", "CA")
