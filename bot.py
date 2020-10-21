import logging
from telegram.ext import Updater

logging.basicConfig(
    filename='bot.log',
    encoding='utf-8',
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,",
    level= logging.INFO
)
logger = logging.getLogger('Pijus Magnificus')

logger.debug('Mensaje para darnos información a l@s desarrollador@s.')
logger.info('Para información del funcionamiento normal del progama.')
logger.warning('Algo no ha ido como esperábamos, habrá que echarle un ojo.')
logger.error('Algo está dando problemas chungos.')
logger.critical('Esto ha petado.')