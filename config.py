import os

from utils import load_env_file

load_env_file()

BOT_TOKEN = os.environ["BOT_TOKEN"]
BASE_URL = "https://lalafo.kg"
AD_LIST_URL = BASE_URL + os.environ["AD_LIST_URL"]
