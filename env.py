"""API Browser environment"""

import os
import logging as log

from dotenv import load_dotenv

# Make KEY=value pairs in .env available as system env variables
load_dotenv(override=True)

API_URL = "https://www.data.gouv.fr/api/1/"
API_KEY = os.getenv("API_KEY", "YOUR-API-KEY")
LOG_LEVEL = log.DEBUG if os.getenv("DEBUG") else log.INFO
