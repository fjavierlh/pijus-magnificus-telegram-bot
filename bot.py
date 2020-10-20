import logging
from telegram.ext import Updater

logging.basicConfig(
    filename="bot.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,",
    level= logging.INFO
)
logger = logging.getLogger('Pijus Magnificus')