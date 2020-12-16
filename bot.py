import os
import auth
import logging
import telegram
from telegram.ext import Updater, CommandHandler

#Logging configuration
logging.basicConfig(
    filename='bot.log',
    #Uncomment for Python3.9
    #encoding='utf-8', 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)

logger = logging.getLogger('Pijus Magnificus')


#Messages Handlers
def start(update, context):
    name = update.message.chat.first_name
    logger.info(f"El usuario {name} ha iniciado una conversación")
    update.message.reply_text(f"Hola {name}, ¡bienvenido!")

def getUpdate(update, context):
    print(update)


def main():
    updater = Updater(os.environ["TOKEN"], use_context=True)

    dp = updater.dispatcher
    
    #Handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("update", getUpdate))

    #Running bot
    updater.start_polling()
    logging.info(f"Bot run")
    updater.idle()


if __name__ == "__main__":
    main()