import os
from dotenv import load_dotenv

# apparently, no error appears even if the path does not exists
load_dotenv("config.env")

class Config:
    LOGGER = True
    BOT_TOKEN = "TOKEN"
    API_ID = xxxx
    API_HASH = "xxxxxxxxxxxxxxxxxx"
    COMMAND_HANDLER = "/"

class Production(Config):
    LOGGER = False

class Development(Config):
    LOGGER = True
