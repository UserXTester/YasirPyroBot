# needed to appropriately, select ENV vars / Config vars
import os

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from bot.config import Config
from pyrogram import (
    Client,
    __version__
)

API_ID = Config.API_ID
API_HASH = Config.API_HASH
COMMAND_HANDLER = Config.COMMAND_HANDLER
BOT_TOKEN = Config.BOT_TOKEN

plugins = dict(root="bot/plugins")
app = Client(
    "Yasir-Bot",
    plugins=plugins,
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)


