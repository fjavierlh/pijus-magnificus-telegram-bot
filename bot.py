import os
import auth
import logging
from telegram.ext import Updater

logging.basicConfig(
    filename='bot.log',
    filemode='w',
    #Uncomment for Python3.9
    #encoding='utf-8', 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)

logger = logging.getLogger('Pijus Magnificus')

#updater = Updater(os.environ['TOKEN'])
#dispatcher = updater.dispatcher
print(os.environ['TOKEN'])